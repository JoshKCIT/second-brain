#!/usr/bin/env python3
"""
Deterministic triage for RSS items: score against interest config, assign triage_status.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

from rss_common import (  # noqa: E402
    SEEN_FILE,
    TRIAGE_SCORES_FILE,
    ensure_rss_dirs,
    iter_item_files,
    load_active_project_slugs,
    load_in_scope_keywords,
    load_json_state,
    load_rss_config,
    parse_domain,
    parse_item_file,
    patch_item_frontmatter,
    save_json_state,
)


def normalize_text(*parts: str) -> str:
    return " ".join(p.lower() for p in parts if p)


def score_item(
    meta: dict[str, Any],
    body: str,
    feed: dict[str, Any],
    interest: dict[str, Any],
    project_slugs: list[str],
    in_scope_keywords: list[str],
) -> tuple[float, list[str]]:
    title = str(meta.get("title", ""))
    text = normalize_text(title, body, str(meta.get("source_url", "")))
    matched: list[str] = []
    score = 0.0

    vendor_slugs = [str(v) for v in (interest.get("vendor_slugs") or [])]
    feed_domain, _ = parse_domain(feed)
    feed_vendor = feed_domain.replace("vendor:", "") if feed_domain.startswith("vendor:") else ""
    if feed_vendor and feed_vendor in vendor_slugs:
        score += 0.35
        matched.append(f"vendor:{feed_vendor}")

    for kw in interest.get("keywords") or []:
        kw_l = str(kw).lower()
        if kw_l and kw_l in text:
            score += 0.15
            matched.append(f"keyword:{kw}")

    for kw in in_scope_keywords:
        kw_l = kw.lower()
        if len(kw_l) >= 4 and kw_l in text:
            score += 0.05
            matched.append(f"in_scope:{kw_l[:40]}")

    for slug in project_slugs + [str(s) for s in (interest.get("project_slugs") or [])]:
        slug_l = slug.lower().replace("-", " ")
        if slug_l and slug_l in text:
            score += 0.1
            matched.append(f"project:{slug}")

    for ex in interest.get("exclude_keywords") or []:
        ex_l = str(ex).lower()
        if ex_l and ex_l in text:
            score -= 0.5
            matched.append(f"exclude:{ex}")

    return max(0.0, min(1.0, score)), matched


def classify_score(score: float, thresholds: dict[str, Any]) -> str:
    auto_skip = float(thresholds.get("auto_skip_below", 0.25))
    suggest = float(thresholds.get("suggest_above", 0.45))
    high = float(thresholds.get("high_signal_above", 0.70))
    band = thresholds.get("borderline_band") or [0.40, 0.55]
    low_b = float(band[0])
    high_b = float(band[1]) if len(band) > 1 else low_b

    if score < auto_skip:
        return "auto_skip"
    if score >= high:
        return "high_signal"
    if low_b <= score <= high_b:
        return "borderline"
    if score >= suggest:
        return "suggested"
    return "auto_skip"


def feeds_by_slug(cfg: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {f["slug"]: f for f in (cfg.get("feeds") or []) if f.get("slug")}


def triage_all(root: Path, *, dry_run: bool = False) -> dict[str, int]:
    cfg = load_rss_config(root, allow_example=True)
    interest = cfg.get("interest") or {}
    thresholds = interest.get("thresholds") or {}
    max_queue = int(interest.get("max_queue_size", 30))

    feeds = feeds_by_slug(cfg)
    project_slugs = load_active_project_slugs(root)
    vendor_slugs = [str(v) for v in (interest.get("vendor_slugs") or [])]
    in_scope_kw = load_in_scope_keywords(root, vendor_slugs)

    candidates: list[tuple[float, Path, str, list[str]]] = []
    stats = {"pending": 0, "auto_skip": 0, "queued": 0, "skipped_status": 0}

    for path in iter_item_files(root):
        meta, body = parse_item_file(path)
        inbox_status = str(meta.get("inbox_status", "unprocessed"))
        if inbox_status != "unprocessed":
            stats["skipped_status"] += 1
            continue

        triage_status = str(meta.get("triage_status", "pending"))
        if triage_status not in ("pending", ""):
            stats["skipped_status"] += 1
            continue

        feed_slug = str(meta.get("feed_slug", ""))
        feed = feeds.get(feed_slug, {"slug": feed_slug, "domain": meta.get("domain", "informational")})
        score, matched = score_item(meta, body, feed, interest, project_slugs, in_scope_kw)
        status = classify_score(score, thresholds)
        stats["pending"] += 1

        if status == "auto_skip":
            stats["auto_skip"] += 1
            if not dry_run:
                patch_item_frontmatter(
                    path,
                    {"triage_status": status, "triage_score": round(score, 4), "matched_rules": matched},
                )
            continue

        candidates.append((score, path, status, matched))

    candidates.sort(key=lambda x: x[0], reverse=True)
    queue = candidates[:max_queue]
    rest = candidates[max_queue:]

    scores_out: dict[str, Any] = load_json_state(root / TRIAGE_SCORES_FILE)
    seen = load_json_state(root / SEEN_FILE)

    for score, path, status, matched in queue:
        stats["queued"] += 1
        meta, _ = parse_item_file(path)
        item_id = str(meta.get("item_id", ""))
        if not dry_run:
            patch_item_frontmatter(
                path,
                {"triage_status": status, "triage_score": round(score, 4), "matched_rules": matched},
            )
            if item_id in seen:
                seen[item_id]["triage_status"] = status
            scores_out[item_id] = {"score": score, "status": status, "matched_rules": matched}

    for score, path, _status, matched in rest:
        stats["auto_skip"] += 1
        if not dry_run:
            patch_item_frontmatter(
                path,
                {"triage_status": "auto_skip", "triage_score": round(score, 4), "matched_rules": matched},
            )

    if not dry_run:
        save_json_state(root / TRIAGE_SCORES_FILE, scores_out)
        save_json_state(root / SEEN_FILE, seen)

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic RSS triage")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--yes", "-y", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if not args.yes and not args.dry_run:
        reply = input("Run RSS triage? [y/N]: ").strip().lower()
        if reply not in ("y", "yes"):
            print("Aborted.")
            return 0

    ensure_rss_dirs(root)
    stats = triage_all(root, dry_run=args.dry_run)
    print(
        f"Triage: pending={stats['pending']} auto_skip={stats['auto_skip']} "
        f"queued={stats['queued']} skipped_status={stats['skipped_status']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
