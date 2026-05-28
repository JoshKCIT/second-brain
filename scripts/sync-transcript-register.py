#!/usr/bin/env python3
"""
Rebuild wiki/platform-research/transcript-register.md from raw transcripts
and platform-research-review artifacts.

Preserves manual fields (title, notes, skipped status, imported date) on
existing records when the source path still matches.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

REGISTER_REL = Path("wiki/platform-research/transcript-register.md")
TRANSCRIPT_LINE = re.compile(
    r"^- Transcript:\s*`(raw/platform-transcripts/[^`]+)`",
    re.MULTILINE,
)
RECORD_RE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)
FIELD_RE = re.compile(r"^([a-z_]+):\s*(.*)$", re.MULTILINE)
H1_CLAIMS = re.compile(r"^#\s+Claims Analysis:\s*(.+)$", re.MULTILINE)
H1_REPORT = re.compile(r"^#\s+Research Impact Report:\s*(.+)$", re.MULTILINE)

RAW_GLOBS = ("*.txt", "*.md", "**/*.txt", "**/transcript.md", "**/transcript.txt")
SKIP_NAMES = {".gitkeep", "transcript-register.md", "metadata.yml"}


@dataclass
class Record:
    slug: str
    status: str = "queued"
    source: str = ""
    title: str = ""
    imported: str = ""
    reviewed: str = ""
    claims_analysis: str = ""
    impact_report: str = ""
    notes: str = ""

    def as_yaml(self) -> str:
        lines = [
            "```yaml",
            f"slug: {self.slug}",
            f"status: {self.status}",
            f"source: {self.source}",
            f'title: "{_escape_yaml(self.title)}"' if self.title else 'title: ""',
            f"imported: {self.imported or ''}",
            f"reviewed: {self.reviewed or ''}",
            f"claims_analysis: {self.claims_analysis}",
            f"impact_report: {self.impact_report}",
            f'notes: "{_escape_yaml(self.notes)}"' if self.notes else 'notes: ""',
            "```",
        ]
        return "\n".join(lines)


def _escape_yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _norm_source(path: Path, root: Path) -> str:
    rel = path.relative_to(root / "raw" / "platform-transcripts")
    return "raw/platform-transcripts/" + rel.as_posix()


def _slug_from_claims_path(path: Path) -> str:
    name = path.name
    if name.endswith("-claims.md"):
        return name[: -len("-claims.md")]
    return path.stem


def _slug_from_impact_path(path: Path) -> str:
    name = path.name
    if name.endswith("-impact-report.md"):
        return name[: -len("-impact-report.md")]
    return path.stem


def _parse_yaml_block(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in block.strip().splitlines():
        m = FIELD_RE.match(line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith('"') and raw.endswith('"'):
            raw = raw[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        data[key] = raw
    return data


def load_existing_register(path: Path) -> dict[str, Record]:
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    by_source: dict[str, Record] = {}
    for block in RECORD_RE.findall(text):
        data = _parse_yaml_block(block)
        source = data.get("source", "")
        if not source:
            continue
        rec = Record(
            slug=data.get("slug", ""),
            status=data.get("status", "queued"),
            source=source,
            title=data.get("title", ""),
            imported=data.get("imported", ""),
            reviewed=data.get("reviewed", ""),
            claims_analysis=data.get("claims_analysis", ""),
            impact_report=data.get("impact_report", ""),
            notes=data.get("notes", ""),
        )
        by_source[source] = rec
    return by_source


def discover_raw_sources(root: Path) -> dict[str, Path]:
    raw_dir = root / "raw" / "platform-transcripts"
    found: dict[str, Path] = {}
    if not raw_dir.is_dir():
        return found
    for pattern in RAW_GLOBS:
        for path in raw_dir.glob(pattern):
            if not path.is_file() or path.name in SKIP_NAMES:
                continue
            if path.name == "transcript.md" and path.parent == raw_dir:
                continue
            source = _norm_source(path, root)
            found[source] = path
    return found


def index_artifacts(
    root: Path,
    subdir: str,
    suffix: str,
    slug_fn,
) -> tuple[dict[str, str], dict[str, str]]:
    """Return maps source_path -> artifact_rel, slug -> artifact_rel."""
    by_source: dict[str, str] = {}
    by_slug: dict[str, str] = {}
    base = root / subdir
    if not base.is_dir():
        return by_source, by_slug
    for path in base.glob(f"*{suffix}"):
        if path.name.startswith("."):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(root).as_posix()
        slug = slug_fn(path)
        by_slug[slug] = rel
        matched = False
        for m in TRANSCRIPT_LINE.finditer(text):
            by_source[m.group(1)] = rel
            matched = True
        if not matched:
            by_slug[slug] = rel
    return by_source, by_slug


def _title_from_file(path: Path, pattern: re.Pattern[str]) -> str:
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = pattern.search(text)
    return m.group(1).strip() if m else ""


def derive_slug(source: str, existing: Record | None) -> str:
    if existing and existing.slug:
        return existing.slug
    name = Path(source).name
    if name in ("transcript.md", "transcript.txt"):
        return Path(source).parent.name
    stem = Path(name).stem
    return stem.lower().replace("_", "-")[:80] or "unknown"


def compute_status(
    rec: Record,
    has_claims: bool,
    has_impact: bool,
) -> str:
    if rec.status == "skipped":
        return "skipped"
    if has_claims and has_impact:
        return "reviewed"
    if has_claims or has_impact:
        return "partial"
    return "queued"


def build_register(root: Path) -> tuple[str, list[str]]:
    today = date.today().isoformat()
    warnings: list[str] = []
    existing_by_source = load_existing_register(root / REGISTER_REL)

    raw_sources = discover_raw_sources(root)
    claims_by_source, claims_by_slug = index_artifacts(
        root,
        "wiki/platform-research/transcript-analyses",
        "-claims.md",
        _slug_from_claims_path,
    )
    impact_by_source, impact_by_slug = index_artifacts(
        root,
        "reports/platform-research-review",
        "-impact-report.md",
        _slug_from_impact_path,
    )

    all_sources = set(raw_sources) | set(claims_by_source) | set(impact_by_source)
    records: list[Record] = []

    for source in sorted(all_sources):
        prev = existing_by_source.get(source)
        claims_rel = claims_by_source.get(source, "")
        impact_rel = impact_by_source.get(source, "")
        slug = (prev.slug if prev and prev.slug else "")
        if claims_rel:
            slug = _slug_from_claims_path(root / claims_rel)
        elif impact_rel:
            slug = _slug_from_impact_path(root / impact_rel)
        if not slug:
            slug = derive_slug(source, prev)
        if not claims_rel:
            claims_rel = claims_by_slug.get(slug, "")
        if not impact_rel:
            impact_rel = impact_by_slug.get(slug, "")

        has_claims = bool(claims_rel)
        has_impact = bool(impact_rel)
        status = compute_status(
            prev or Record(slug=slug, source=source),
            has_claims,
            has_impact,
        )

        title = (prev.title if prev else "") or _title_from_file(
            root / claims_rel, H1_CLAIMS
        ) or _title_from_file(root / impact_rel, H1_REPORT) or slug

        imported = (prev.imported if prev else "") or (
            today if source in raw_sources else ""
        )
        reviewed = ""
        if status == "reviewed":
            reviewed = (prev.reviewed if prev else "") or today

        rec = Record(
            slug=slug,
            status=status,
            source=source,
            title=title,
            imported=imported,
            reviewed=reviewed,
            claims_analysis=claims_rel,
            impact_report=impact_rel,
            notes=prev.notes if prev else "",
        )
        records.append(rec)

        if source not in raw_sources and status != "skipped":
            warnings.append(f"Artifact references missing raw file: {source}")

    for source, path in raw_sources.items():
        if source not in all_sources:
            warnings.append(f"Unexpected: raw file not indexed: {source}")

    # Orphan slugs: artifacts without any source line match handled above via all_sources

    summary_rows = []
    for rec in records:
        claims_link = rec.claims_analysis.split("/")[-1] if rec.claims_analysis else "—"
        impact_link = rec.impact_report.split("/")[-1] if rec.impact_report else "—"
        summary_rows.append(
            f"| {rec.slug} | `{rec.status}` | `{rec.source}` | {claims_link} | {impact_link} |"
        )

    body = [
        "# Platform Transcript Register",
        "",
        "Operational index of product-intelligence sources under `raw/platform-transcripts/`. "
        "This file is the queue board: what is imported, what is ready for "
        "`/platform-research-review`, and what is already reviewed.",
        "",
        "Sync after import or review:",
        "",
        "```bash",
        "python scripts/sync-transcript-register.py --root .",
        "```",
        "",
        "## Status legend",
        "",
        "| Status | Meaning |",
        "|--------|---------|",
        "| `queued` | Present in `raw/platform-transcripts/`; not yet reviewed |",
        "| `partial` | Review started — claims analysis or impact report missing |",
        "| `reviewed` | Claims analysis and impact report both exist |",
        "| `skipped` | User marked intentionally not reviewed (duplicate, noise, off-scope) |",
        "",
        "## Summary",
        "",
        "| Slug | Status | Source | Claims | Impact |",
        "|------|--------|--------|--------|--------|",
    ]
    if summary_rows:
        body.extend(summary_rows)
    else:
        body.append("| _No transcripts discovered._ | | | | |")

    queued = sum(1 for r in records if r.status == "queued")
    partial = sum(1 for r in records if r.status == "partial")
    reviewed = sum(1 for r in records if r.status == "reviewed")
    skipped = sum(1 for r in records if r.status == "skipped")
    body.extend(
        [
            "",
            f"_Last synced: {today}. {len(records)} total — "
            f"{queued} queued, {partial} partial, {reviewed} reviewed, {skipped} skipped._",
            "",
            "## Records",
            "",
        ]
    )
    for rec in records:
        body.append(rec.as_yaml())
        body.append("")

    return "\n".join(body).rstrip() + "\n", warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repo root")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if register would change (for CI)",
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress stdout")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    out_path = root / REGISTER_REL
    new_content, warnings = build_register(root)

    changed = True
    if out_path.is_file():
        changed = out_path.read_text(encoding="utf-8") != new_content

    if args.check:
        if changed:
            if not args.quiet:
                print(f"Register is out of date: {REGISTER_REL}", file=sys.stderr)
            return 1
        if not args.quiet:
            print("Register is up to date.")
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_content, encoding="utf-8")

    if not args.quiet:
        print(f"Wrote {REGISTER_REL}")
        for w in warnings:
            print(f"  warning: {w}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
