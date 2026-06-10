#!/usr/bin/env python3
"""One-off repair: fix double-wrapped title quotes in RSS item frontmatter."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from rss_common import FRONTMATTER_RE, build_item_frontmatter, parse_item_file  # noqa: E402


def repair_file(path: Path) -> bool:
    try:
        parse_item_file(path)
        return False
    except Exception:
        pass

    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(f"no frontmatter: {path}")

    body = m.group(2)
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.strip().startswith("-"):
            continue
        key, _, val = line.partition(":")
        meta[key.strip()] = val.strip().strip('"')

    path.write_text(
        build_item_frontmatter(
            title=meta.get("title", ""),
            source_url=meta.get("source_url", ""),
            feed_slug=meta.get("feed_slug", ""),
            item_id=meta.get("item_id", ""),
            published_at=meta.get("published_at", ""),
            ingested_at=meta.get("ingested_at", ""),
            domain=meta.get("domain", "informational"),
            authority=meta.get("authority", "informational"),
            inbox_status=meta.get("inbox_status", "unprocessed"),
            triage_status=meta.get("triage_status", "pending"),
        )
        + body.lstrip(),
        encoding="utf-8",
    )
    parse_item_file(path)
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    items_dir = args.root / "raw" / "workspace-rss-feed" / "items"
    fixed = 0
    for path in sorted(items_dir.rglob("*.md")):
        if repair_file(path):
            fixed += 1
            print(f"fixed {path.relative_to(args.root)}")
    print(f"Done: {fixed} file(s) repaired")
    return 0


if __name__ == "__main__":
    sys.exit(main())
