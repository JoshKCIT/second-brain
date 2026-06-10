#!/usr/bin/env python3
"""Set inbox_status on an RSS item (archive or dismiss)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from rss_common import (  # noqa: E402
    SEEN_FILE,
    ensure_rss_dirs,
    find_item_path,
    load_json_state,
    patch_item_frontmatter,
    save_json_state,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update RSS item inbox_status")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--item-id", required=True)
    parser.add_argument("--status", choices=("archived", "dismissed"), required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    ensure_rss_dirs(root)
    path = find_item_path(root, args.item_id)
    if path is None:
        print(f"ERROR: item not found: {args.item_id}", file=sys.stderr)
        return 1

    patch_item_frontmatter(path, {"inbox_status": args.status})
    seen = load_json_state(root / SEEN_FILE)
    if args.item_id in seen:
        seen[args.item_id]["inbox_status"] = args.status
        save_json_state(root / SEEN_FILE, seen)

    print(f"Set {args.item_id} inbox_status={args.status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
