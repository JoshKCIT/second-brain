#!/usr/bin/env python3
"""
Compile raw/workspace-external vendor caches into wiki/workspace-concepts articles.

Deterministic bootstrap for Phase 2. For richer synthesis, use /workspace-compile (LLM).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,3}\s+(.+)$", re.MULTILINE)


def parse_raw(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if m and yaml:
        meta = yaml.safe_load(m.group(1)) or {}
        body = m.group(2).strip()
    else:
        meta, body = {}, text
    return meta, body


def slug_for(vendor: str, topic: str) -> str:
    return f"{vendor}-{topic}".replace("_", "-")


def title_for(vendor: str, topic: str) -> str:
    return f"{vendor.upper()} — {topic.replace('-', ' ').title()}"


def extract_summary(body: str, max_len: int = 500) -> str:
    lines = []
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith("!") or s.startswith("["):
            continue
        if s.startswith("#"):
            break
        lines.append(s)
        if len(" ".join(lines)) > max_len:
            break
    summary = " ".join(lines)[:max_len].strip()
    return summary or "Vendor documentation cache compiled from public source."


def extract_key_points(body: str, limit: int = 6) -> list[str]:
    points = []
    for m in HEADING_RE.finditer(body):
        t = m.group(1).strip()
        if t.lower() in ("see also", "syntax", "note", "important"):
            continue
        if len(t) > 120:
            t = t[:117] + "..."
        points.append(t)
        if len(points) >= limit:
            break
    if not points:
        for line in body.splitlines():
            if line.strip().startswith("- "):
                points.append(line.strip()[2:][:200])
            if len(points) >= limit:
                break
    return points or ["See cached vendor source for full detail."]


def concept_path(root: Path, slug: str) -> Path:
    return root / "wiki" / "workspace-concepts" / f"{slug}.md"


def source_already_compiled(root: Path, raw_rel: str) -> str | None:
    concepts = root / "wiki" / "workspace-concepts"
    if not concepts.is_dir():
        return None
    needle = raw_rel.replace("\\", "/")
    for path in concepts.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if needle in text:
            return path.stem
    return None


def write_concept(
    root: Path,
    *,
    slug: str,
    meta: dict,
    body: str,
    raw_rel: str,
    force: bool,
) -> str:
    dest = concept_path(root, slug)
    if dest.exists() and not force:
        return "skipped"

    vendor = meta.get("vendor", "unknown")
    topic = meta.get("topic", slug)
    title = title_for(vendor, topic)
    authority = meta.get("authority", "standard")
    domain = meta.get("domain", f"vendor:{vendor}")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    summary = extract_summary(body)
    bullets = extract_key_points(body)
    source_url = meta.get("source_url", "")

    key_points = "\n".join(f"- {b}" for b in bullets)
    content = f"""---
title: "{title}"
type: concept
authority: {authority}
domain: {domain}
tags: [{vendor}, {topic}]
sources:
  - "{raw_rel}"
status: published
created: {today}
updated: {today}
---

# {title}

{summary}

## Key Points

{key_points}

## Details

Compiled from vendor cache. For authoritative wording, see the cached source and live vendor URL in See Also.

## See Also

- [{source_url}]({source_url}) (cached {today})

## Sources

- [[{raw_rel.replace('.md', '')}]] — vendor cache
"""
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")


def update_index(root: Path, entries: list[tuple[str, str, str, str]]) -> None:
    index_path = root / "wiki" / "index.md"
    if not index_path.is_file():
        return
    text = index_path.read_text(encoding="utf-8")
    marker = "## All concepts\n\n| Article | Authority | Domain | Sources | Updated |\n|---|---|---|---|---|\n"
    if marker not in text:
        return
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for slug, authority, domain, _ in entries:
        row = f"| [[workspace-concepts/{slug}]] | {authority.title()} | {domain} | 1 | {today} |\n"
        link = f"[[workspace-concepts/{slug}]]"
        if link in text:
            continue
        text = text.replace(marker, marker + row)
    index_path.write_text(text, encoding="utf-8")


def append_log(root: Path, created: int, updated: int, skipped: int) -> None:
    log_path = root / "wiki" / "log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = (
        f"\n## [{ts}] compile | workspace-external batch\n"
        f"- Script: compile-workspace-external.py\n"
        f"- Created: {created}\n"
        f"- Updated: {updated}\n"
        f"- Skipped (existing): {skipped}\n"
        f"- Index updated: yes\n"
    )
    log_path.write_text(log_path.read_text(encoding="utf-8") + entry, encoding="utf-8")


def update_state(root: Path, compiled: list[dict]) -> None:
    state_path = root / "state.json"
    state = {}
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            state = {}
    for item in compiled:
        state[item["raw"]] = {
            "compiled_at": item["at"],
            "wiki_articles": [item["concept"]],
        }
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def print_manifest(created: list[str], updated: list[str], skipped: list[str]) -> None:
    print("\n--- Post-compile manifest ---")
    print(f"Compiled: {len(created) + len(updated)} articles ({len(created)} created, {len(updated)} updated, {len(skipped)} skipped)")
    if created:
        print("Created:")
        for s in created[:10]:
            print(f"  + workspace-concepts/{s}.md")
    if updated:
        print("Updated:")
        for s in updated[:10]:
            print(f"  ~ workspace-concepts/{s}.md")
    print("Index updated: wiki/index.md")
    print("Next: python scripts/lint-workspace.py")
    print("---\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile vendor external raw to wiki concepts")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--force", action="store_true", help="Overwrite existing concepts")
    args = parser.parse_args()
    root = args.root.resolve()

    raw_base = root / "raw" / "workspace-external"
    if not raw_base.is_dir():
        print("No raw/workspace-external/ directory.", file=sys.stderr)
        return 1

    created, updated, skipped = [], [], []
    index_entries = []
    state_items = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for raw_path in sorted(raw_base.rglob("*.md")):
        raw_rel = str(raw_path.relative_to(root)).replace("\\", "/")
        meta, body = parse_raw(raw_path)
        vendor = meta.get("vendor") or raw_path.parts[-3]
        topic = meta.get("topic") or raw_path.parent.name
        slug = slug_for(vendor, topic)

        existing = source_already_compiled(root, raw_rel)
        if existing and not args.force:
            skipped.append(existing)
            continue

        if concept_path(root, slug).exists() and not args.force:
            skipped.append(slug)
            continue

        existed = concept_path(root, slug).exists()
        write_concept(root, slug=slug, meta=meta, body=body, raw_rel=raw_rel, force=args.force)
        if existed:
            updated.append(slug)
        else:
            created.append(slug)

        index_entries.append(
            (slug, meta.get("authority", "standard"), meta.get("domain", f"vendor:{vendor}"), raw_rel)
        )
        state_items.append(
            {"raw": raw_rel, "at": now, "concept": f"wiki/workspace-concepts/{slug}.md"}
        )

    if index_entries:
        update_index(root, index_entries)
    append_log(root, len(created), len(updated), len(skipped))
    update_state(root, state_items)
    print_manifest(created, updated, skipped)
    return 0


if __name__ == "__main__":
    sys.exit(main())
