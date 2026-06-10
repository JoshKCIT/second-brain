#!/usr/bin/env python3
"""
Fetch RSS/Atom feeds into raw/workspace-rss-feed/items/ with dedupe state.

Approval-gated batch logging: pass --yes to skip interactive prompt.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

try:
    import feedparser
except ImportError:
    feedparser = None  # type: ignore

from rss_common import (  # noqa: E402
    SEEN_FILE,
    append_rss_log,
    build_item_frontmatter,
    ensure_rss_dirs,
    entry_published_iso,
    entry_summary,
    item_id_from_entry,
    item_rel_path,
    load_rss_config,
    load_json_state,
    parse_domain,
    save_json_state,
)


def parse_feed_source(feed: dict[str, Any], root: Path) -> Any:
    if feedparser is None:
        raise RuntimeError("feedparser required. pip install feedparser")
    url = feed.get("url", "")
    fixture = feed.get("fixture")
    if fixture:
        fixture_path = root / fixture
        if not fixture_path.is_file():
            raise FileNotFoundError(f"fixture not found: {fixture}")
        return feedparser.parse(fixture_path.read_text(encoding="utf-8"))
    if not url:
        raise ValueError("feed requires url or fixture")
    return feedparser.parse(url)


def ingest_entries(
    root: Path,
    feed: dict[str, Any],
    parsed: Any,
    *,
    max_items: int | None = None,
    dry_run: bool = False,
) -> dict[str, int]:
    slug = feed["slug"]
    domain, authority = parse_domain(feed)
    seen = load_json_state(root / SEEN_FILE)
    ingested_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    date_prefix = ingested_at[:10]

    stats = {"new": 0, "skipped": 0, "failed": 0}

    entries = list(parsed.entries or [])
    if max_items is not None:
        entries = entries[:max_items]

    for entry in entries:
        link = str(getattr(entry, "link", "") or "").strip()
        guid = str(getattr(entry, "id", "") or getattr(entry, "guid", "") or "").strip()
        title = str(getattr(entry, "title", "") or "Untitled").strip()
        if not link and not guid:
            stats["failed"] += 1
            continue
        try:
            item_id = item_id_from_entry(guid, link)
        except ValueError:
            stats["failed"] += 1
            continue

        if item_id in seen:
            stats["skipped"] += 1
            continue

        published_at = entry_published_iso(entry)
        summary = entry_summary(entry).strip()
        body = summary or "_No summary in feed entry._"

        dest_dir = root / "raw" / "workspace-rss-feed" / "items" / date_prefix / slug
        dest = dest_dir / f"{item_id}.md"
        if dest.is_file():
            stats["skipped"] += 1
            continue

        content = build_item_frontmatter(
            title=title,
            source_url=link or guid,
            feed_slug=slug,
            item_id=item_id,
            published_at=published_at,
            ingested_at=ingested_at,
            domain=domain,
            authority=authority,
        ) + body

        if dry_run:
            stats["new"] += 1
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        seen[item_id] = {
            "feed_slug": slug,
            "source_url": link or guid,
            "guid": guid,
            "first_seen": ingested_at,
            "raw_path": item_rel_path(dest, root),
            "triage_status": "pending",
            "inbox_status": "unprocessed",
        }
        stats["new"] += 1

    if not dry_run and stats["new"]:
        save_json_state(root / SEEN_FILE, seen)

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest RSS feeds to raw/workspace-rss-feed/")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--yes", "-y", action="store_true")
    parser.add_argument("--feed", help="Only ingest this feed slug")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-items", type=int, help="Cap entries per feed")
    parser.add_argument("--allow-example-config", action="store_true", help="For tests only")
    args = parser.parse_args()

    root = args.root.resolve()
    try:
        cfg = load_rss_config(root, allow_example=args.allow_example_config)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    feeds = [f for f in (cfg.get("feeds") or []) if f.get("enabled", True)]
    if args.feed:
        feeds = [f for f in feeds if f.get("slug") == args.feed]

    if not feeds:
        print("No enabled feeds to ingest.")
        return 0

    if feedparser is None:
        print("ERROR: feedparser required. pip install feedparser", file=sys.stderr)
        return 1

    print(f"Will ingest {len(feeds)} feed(s){' (dry-run)' if args.dry_run else ''}:")
    for f in feeds:
        src = f.get("fixture") or f.get("url")
        print(f"  - {f['slug']}: {src}")

    if not args.yes and not args.dry_run:
        reply = input("\nProceed? [y/N]: ").strip().lower()
        if reply not in ("y", "yes"):
            print("Aborted.")
            return 0

    if not args.dry_run:
        ensure_rss_dirs(root)

    totals = {"new": 0, "skipped": 0, "failed": 0}
    for feed in feeds:
        try:
            parsed = parse_feed_source(feed, root)
            if getattr(parsed, "bozo", False) and not parsed.entries:
                raise RuntimeError(getattr(parsed, "bozo_exception", "feed parse error"))
            stats = ingest_entries(
                root,
                feed,
                parsed,
                max_items=args.max_items,
                dry_run=args.dry_run,
            )
            for k in totals:
                totals[k] += stats[k]
            print(f"OK  {feed['slug']}: new={stats['new']} skipped={stats['skipped']} failed={stats['failed']}")
        except Exception as exc:
            print(f"FAIL {feed['slug']}: {exc}", file=sys.stderr)
            totals["failed"] += 1

    print(f"\nDone: new={totals['new']} skipped={totals['skipped']} failed={totals['failed']}")
    if not args.dry_run and totals["new"]:
        append_rss_log(
            root,
            f"{totals['new']} new item(s)",
            [f"feeds: {len(feeds)}", f"skipped: {totals['skipped']}"],
        )
    return 1 if totals["failed"] and not totals["new"] else 0


if __name__ == "__main__":
    sys.exit(main())
