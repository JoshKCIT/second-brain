#!/usr/bin/env python3
"""
Seed vendor documentation caches from config/vendor-seed-stack.yml using defuddle.

Approval-gated: pass --yes to fetch without interactive prompt.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SEED_FILE = ROOT / "config" / "vendor-seed-stack.yml"


def load_config(root: Path) -> dict:
    for name in ("second-brain.yml", "second-brain.example.yml"):
        path = root / "config" / name
        if path.is_file():
            with path.open(encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
    return {}


def ttl_days(cfg: dict, vendor: str) -> int:
    vr = cfg.get("vendor_revalidation") or {}
    per = vr.get("per_vendor") or {}
    return int(per.get(vendor) or per.get(vendor.replace("-", "_")) or vr.get("default_ttl_days", 90))


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "page"


def frontmatter(
    *,
    source_url: str,
    vendor: str,
    topic: str,
    fetched_at: str,
    revalidate_after: str,
    query: str,
    authority: str = "standard",
    ingest_mode: str = "defuddle",
) -> str:
    return f"""---
source_url: {source_url}
vendor: {vendor}
topic: {topic}
fetched_at: {fetched_at}
revalidate_after: {revalidate_after}
fetched_by_query: {query}
domain: vendor:{vendor}
authority: {authority}
ingest_mode: {ingest_mode}
---

"""


def fetch_with_defuddle(url: str, out_path: Path) -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _vendor_fetch import run_defuddle

    run_defuddle(url, out_path)


def append_log(root: Path, vendor: str, topic: str, url: str, revalidate_after: str) -> None:
    log_path = root / "wiki" / "log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = (
        f"\n## [{ts}] ingest-vendor-doc | {vendor}/{topic}\n"
        f"- Source: {url}\n"
        f"- Fetched by query: seed-vendor-docs.py (stack bootstrap)\n"
        f"- Cache valid until: {revalidate_after}\n"
    )
    if log_path.is_file():
        log_path.write_text(log_path.read_text(encoding="utf-8") + entry, encoding="utf-8")
    else:
        log_path.write_text(f"# Build Log\n{entry}", encoding="utf-8")


def update_index_row(root: Path, vendor: str, topic: str, rel_path: str, cached_date: str) -> None:
    index_path = root / "wiki" / "index.md"
    if not index_path.is_file():
        return
    text = index_path.read_text(encoding="utf-8")
    row = f"| {vendor} | {topic} | [[{rel_path}]] | {cached_date} |\n"
    marker = "## Cached vendor documentation\n\n| Vendor | Topic | Path | Cached |\n|---|---|---|---|\n"
    if marker in text and row.strip() not in text:
        text = text.replace(marker, marker + row)
        index_path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed vendor doc caches")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--seed-file", type=Path, default=DEFAULT_SEED_FILE)
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompt")
    parser.add_argument("--vendor", help="Only seed this vendor slug")
    args = parser.parse_args()

    root = args.root.resolve()
    if not args.seed_file.is_file():
        print(f"ERROR: seed file not found: {args.seed_file}", file=sys.stderr)
        return 1

    with args.seed_file.open(encoding="utf-8") as f:
        seed_data = yaml.safe_load(f) or {}

    topics = seed_data.get("seed_topics") or []
    if args.vendor:
        topics = [t for t in topics if t.get("vendor") == args.vendor]

    if not topics:
        print("No seed topics to fetch.")
        return 0

    print(f"Will seed {len(topics)} vendor doc(s) from {args.seed_file.name}:")
    for t in topics:
        mode = t.get("ingest_mode", "defuddle")
        target = t.get("url") or t.get("canonical_doc_url") or t.get("manual_template")
        print(f"  - {t['vendor']}/{t['topic']} ({mode}): {target}")

    if not args.yes:
        reply = input("\nProceed? [y/N]: ").strip().lower()
        if reply not in ("y", "yes"):
            print("Aborted.")
            return 0

    cfg = load_config(root)
    ok_count = 0
    fail_count = 0

    for item in topics:
        vendor = item["vendor"]
        topic = item["topic"]
        ingest_mode = item.get("ingest_mode", "defuddle")
        authority = item.get("authority", "standard")
        url = item.get("url") or item.get("canonical_doc_url", "")
        slug = item.get("slug") or slugify(topic)
        days = ttl_days(cfg, vendor)
        now = datetime.now(timezone.utc)
        fetched_at = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        revalidate = (now + timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")

        dest_dir = root / "raw" / "workspace-external" / vendor / topic
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / f"{slug}.md"

        try:
            if ingest_mode == "manual":
                template = item.get("manual_template")
                if not template:
                    raise RuntimeError("manual ingest_mode requires manual_template path")
                template_path = root / template
                if not template_path.is_file():
                    raise RuntimeError(f"manual template not found: {template}")
                body = template_path.read_text(encoding="utf-8")
                if body.startswith("---"):
                    parts = body.split("---", 2)
                    body = parts[2].lstrip() if len(parts) >= 3 else body
                source_url = item.get("canonical_doc_url") or url
            else:
                if not url:
                    raise RuntimeError("defuddle ingest requires url")
                with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
                    tmp_path = Path(tmp.name)
                fetch_with_defuddle(url, tmp_path)
                body = tmp_path.read_text(encoding="utf-8")
                tmp_path.unlink(missing_ok=True)
                source_url = url

            dest.write_text(
                frontmatter(
                    source_url=source_url,
                    vendor=vendor,
                    topic=topic,
                    fetched_at=fetched_at,
                    revalidate_after=revalidate,
                    query="seed-vendor-docs.py stack bootstrap",
                    authority=authority,
                    ingest_mode=ingest_mode,
                )
                + body,
                encoding="utf-8",
            )
            rel = f"raw/workspace-external/{vendor}/{topic}/{slug}"
            append_log(root, vendor, topic, url, revalidate)
            update_index_row(root, vendor, topic, rel, now.strftime("%Y-%m-%d"))
            print(f"OK  {vendor}/{topic} -> {dest.relative_to(root)}")
            ok_count += 1
        except Exception as exc:
            print(f"FAIL {vendor}/{topic}: {exc}", file=sys.stderr)
            fail_count += 1

    print(f"\nDone: {ok_count} cached, {fail_count} failed.")
    return 1 if fail_count else 0


if __name__ == "__main__":
    sys.exit(main())
