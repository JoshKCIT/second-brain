#!/usr/bin/env python3
"""
Promote an RSS item: fetch full article via defuddle, write promoted/{item_id}/article.md.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

from _vendor_fetch import run_defuddle  # noqa: E402
from rss_common import (  # noqa: E402
    SEEN_FILE,
    ensure_rss_dirs,
    find_item_path,
    load_json_state,
    parse_item_file,
    patch_item_frontmatter,
    rss_base,
    save_json_state,
)


def promote_item(root: Path, item_id: str, *, dry_run: bool = False) -> dict[str, Any]:
    path = find_item_path(root, item_id)
    if path is None:
        raise FileNotFoundError(f"item_id not found: {item_id}")

    meta, _ = parse_item_file(path)
    source_url = str(meta.get("source_url", "")).strip()
    if not source_url:
        raise ValueError(f"item {item_id} has no source_url")

    promoted_dir = rss_base(root) / "promoted" / item_id
    dest = promoted_dir / "article.md"

    if dry_run:
        return {"item_id": item_id, "source_url": source_url, "promoted_path": str(dest)}

    promoted_dir.mkdir(parents=True, exist_ok=True)
    try:
        run_defuddle(source_url, dest)
    except Exception as exc:
        quarantine = rss_base(root) / "quarantine" / item_id
        quarantine.mkdir(parents=True, exist_ok=True)
        (quarantine / "error.txt").write_text(str(exc), encoding="utf-8")
        raise

    promoted_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = dest.read_text(encoding="utf-8")
    if not text.startswith("---"):
        header = (
            f"---\n"
            f"title: {meta.get('title', '')!r}\n"
            f"source_url: {source_url}\n"
            f"item_id: {item_id}\n"
            f"feed_slug: {meta.get('feed_slug', '')}\n"
            f"ingest_mode: defuddle\n"
            f"promoted_at: {promoted_at}\n"
            f"domain: {meta.get('domain', 'informational')}\n"
            f"authority: {meta.get('authority', 'informational')}\n"
            f"---\n\n"
        )
        dest.write_text(header + text, encoding="utf-8")

    patch_item_frontmatter(path, {"inbox_status": "promoted"})
    seen = load_json_state(root / SEEN_FILE)
    if item_id in seen:
        seen[item_id]["inbox_status"] = "promoted"
        save_json_state(root / SEEN_FILE, seen)

    return {
        "item_id": item_id,
        "source_url": source_url,
        "promoted_path": dest.relative_to(root).as_posix(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote RSS item to full article")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--item-id", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    ensure_rss_dirs(root)
    try:
        result = promote_item(root, args.item_id, dry_run=args.dry_run)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Promoted {result['item_id']} -> {result.get('promoted_path', '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
