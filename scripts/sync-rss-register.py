#!/usr/bin/env python3
"""
Rebuild raw/workspace-rss-feed/rss-register.md from item files and state.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

from rss_common import (  # noqa: E402
    REGISTER_REL,
    ensure_rss_dirs,
    iter_item_files,
    item_rel_path,
    load_json_state,
    parse_item_file,
    review_flags,
    rss_base,
    summary_excerpt,
    SEEN_FILE,
)

RECORD_RE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)
FIELD_RE = re.compile(r"^([a-z_]+):\s*(.*)$", re.MULTILINE)


def _escape_yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def parse_existing_notes(register_path: Path) -> dict[str, str]:
    if not register_path.is_file():
        return {}
    text = register_path.read_text(encoding="utf-8")
    notes: dict[str, str] = {}
    for block in RECORD_RE.findall(text):
        fields = {m.group(1): m.group(2).strip().strip('"') for m in FIELD_RE.finditer(block)}
        item_id = fields.get("item_id", "")
        note = fields.get("notes", "")
        if item_id and note:
            notes[item_id] = note
    return notes


def collect_records(root: Path, preserved_notes: dict[str, str]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    promoted_dir = rss_base(root) / "promoted"

    for path in iter_item_files(root):
        meta, body = parse_item_file(path)
        item_id = str(meta.get("item_id", ""))
        if not item_id:
            continue
        excerpt = summary_excerpt(body)
        source_url = str(meta.get("source_url", ""))
        promoted_path = promoted_dir / item_id / "article.md"
        records.append(
            {
                "item_id": item_id,
                "feed_slug": str(meta.get("feed_slug", "")),
                "title": str(meta.get("title", "")),
                "source_url": source_url,
                "published_at": str(meta.get("published_at", "")),
                "domain": str(meta.get("domain", "informational")),
                "authority": str(meta.get("authority", "informational")),
                "triage_status": str(meta.get("triage_status", "pending")),
                "inbox_status": str(meta.get("inbox_status", "unprocessed")),
                "triage_score": meta.get("triage_score"),
                "summary_excerpt": excerpt,
                "review_flags": review_flags(source_url, excerpt),
                "raw_path": item_rel_path(path, root),
                "promoted_path": item_rel_path(promoted_path, root) if promoted_path.is_file() else "",
                "matched_rules": meta.get("matched_rules") or [],
                "notes": preserved_notes.get(item_id, ""),
            }
        )
    return records


def record_yaml(rec: dict[str, Any]) -> str:
    lines = [
        "```yaml",
        f"item_id: {rec['item_id']}",
        f"feed_slug: {rec['feed_slug']}",
        f"domain: {rec.get('domain', 'informational')}",
        f"authority: {rec.get('authority', 'informational')}",
        f'title: "{_escape_yaml(rec["title"])}"',
        f"source_url: {rec['source_url']}",
        f"published_at: {rec['published_at']}",
        f"triage_status: {rec['triage_status']}",
        f"inbox_status: {rec['inbox_status']}",
        f"raw_path: {rec['raw_path']}",
    ]
    if rec.get("promoted_path"):
        lines.append(f"promoted_path: {rec['promoted_path']}")
    if rec.get("triage_score") is not None:
        lines.append(f"triage_score: {rec['triage_score']}")
    if rec.get("summary_excerpt"):
        lines.append(f'summary_excerpt: "{_escape_yaml(rec["summary_excerpt"])}"')
    if rec.get("matched_rules"):
        lines.append("matched_rules:")
        for rule in rec["matched_rules"]:
            lines.append(f"  - {rule}")
    if rec.get("review_flags"):
        lines.append("review_flags:")
        for flag in rec["review_flags"]:
            lines.append(f"  - {flag}")
    if rec.get("notes"):
        lines.append(f'notes: "{_escape_yaml(rec["notes"])}"')
    lines.append("```")
    return "\n".join(lines)


def build_register(root: Path) -> str:
    register_path = root / REGISTER_REL
    preserved = parse_existing_notes(register_path)
    records = collect_records(root, preserved)

    review_statuses = {"suggested", "high_signal", "borderline"}
    review = [r for r in records if r["triage_status"] in review_statuses and r["inbox_status"] == "unprocessed"]
    review.sort(key=lambda r: float(r.get("triage_score") or 0), reverse=True)

    promoted = [r for r in records if r["inbox_status"] == "promoted"]
    promoted.sort(key=lambda r: r["published_at"], reverse=True)

    cutoff = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%dT")
    archived = [
        r
        for r in records
        if r["inbox_status"] in ("archived", "dismissed") and r["published_at"] >= cutoff
    ]

    auto_skip_count = sum(1 for r in records if r["triage_status"] == "auto_skip")

    lines = [
        "# RSS Feed Register",
        "",
        f"Last synced: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "## How to review",
        "",
        "Each **Review queue** block includes `summary_excerpt` (RSS teaser), `matched_rules`,",
        "and `review_flags`. Open `source_url` in a browser before **promote** (defuddle fetches",
        "the full article). Reply to `/workspace-review-rss` with:",
        "",
        "```text",
        "promote: {item_id}",
        "archive: {item_id}, ...",
        "dismiss: {item_id}, ...",
        "```",
        "",
        "| Action | When |",
        "|--------|------|",
        "| **promote** | Worth caching full article → wiki compile candidate |",
        "| **archive** | Read; keep for audit; not wiki-worthy now |",
        "| **dismiss** | Noise or `fixture_url` test data |",
        "",
        "## Summary",
        "",
        f"- Review queue: {len(review)}",
        f"- Promoted awaiting compile: {len(promoted)}",
        f"- Auto-skipped (not listed): {auto_skip_count}",
        "",
        "## Review queue",
        "",
    ]
    if review:
        for rec in review:
            lines.append(record_yaml(rec))
            lines.append("")
    else:
        lines.append("_No items in review queue._")
        lines.append("")

    lines.extend(["## Promoted awaiting compile", ""])
    if promoted:
        for rec in promoted:
            lines.append(record_yaml(rec))
            lines.append("")
    else:
        lines.append("_No promoted items._")
        lines.append("")

    lines.extend(["## Recently archived or dismissed (7 days)", ""])
    if archived:
        for rec in archived:
            lines.append(record_yaml(rec))
            lines.append("")
    else:
        lines.append("_None._")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync RSS register")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()

    root = args.root.resolve()
    ensure_rss_dirs(root)
    content = build_register(root)
    out = root / REGISTER_REL
    out.write_text(content, encoding="utf-8")
    print(f"Wrote {out.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
