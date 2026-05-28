#!/usr/bin/env python3
"""Scan vendor doc caches and report fresh/stale/expired status. Use --dry-run to list only."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FM_RE.match(text)
    if not m or yaml is None:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def parse_iso(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_config(root: Path) -> dict:
    for name in ("second-brain.yml", "second-brain.example.yml"):
        path = root / "config" / name
        if path.is_file() and yaml:
            with path.open(encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
    return {"vendor_revalidation": {"hard_max_age_days": 365}}


def scan(root: Path, vendor_filter: str | None) -> list[dict]:
    hard_max = int(
        (load_config(root).get("vendor_revalidation") or {}).get("hard_max_age_days", 365)
    )
    now = datetime.now(timezone.utc)
    rows: list[dict] = []

    base = root / "raw" / "workspace-external"
    if not base.is_dir():
        return rows

    for path in sorted(base.rglob("*.md")):
        if path.name == ".gitkeep":
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        vendor = meta.get("vendor", "")
        if vendor_filter and vendor != vendor_filter:
            continue
        fetched = parse_iso(str(meta.get("fetched_at", "")))
        revalidate = parse_iso(str(meta.get("revalidate_after", "")))
        if not fetched:
            status = "unknown"
        elif revalidate and now < revalidate:
            status = "fresh"
        elif fetched and (now - fetched).days > hard_max:
            status = "expired"
        else:
            status = "stale"
        rows.append(
            {
                "vendor": vendor,
                "topic": meta.get("topic", path.parent.name),
                "path": str(path.relative_to(root)),
                "status": status,
                "source_url": meta.get("source_url", ""),
                "fetched_at": meta.get("fetched_at", ""),
                "revalidate_after": meta.get("revalidate_after", ""),
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="List vendor cache TTL status")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--vendor", help="Filter by vendor slug")
    parser.add_argument("--dry-run", action="store_true", default=True, help="List only (default)")
    parser.add_argument("--apply", action="store_true", help="Refetch stale (not implemented; use seed/ingest prompts)")
    args = parser.parse_args()
    dry_run = not args.apply

    rows = scan(args.root.resolve(), args.vendor)
    if not rows:
        print("No vendor caches found under raw/workspace-external/")
        return 0

    counts = {"fresh": 0, "stale": 0, "expired": 0, "unknown": 0}
    print(f"Vendor cache scan ({'dry-run' if dry_run else 'apply'}): {len(rows)} file(s)\n")
    print(f"{'Vendor':<12} {'Topic':<28} {'Status':<8} Path")
    print("-" * 90)
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
        print(f"{r['vendor']:<12} {r['topic']:<28} {r['status']:<8} {r['path']}")

    print(f"\nSummary: fresh={counts['fresh']} stale={counts['stale']} expired={counts['expired']} unknown={counts['unknown']}")
    if dry_run and counts["stale"] + counts["expired"] > 0:
        print("Refetch: use /workspace-revalidate-vendor-docs or /workspace-ingest-vendor-doc (approval required).")
    if args.apply:
        print("NOTE: --apply refetch not automated in v1; use workspace prompts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
