#!/usr/bin/env python3
"""
Promote accepted platform ADRs: strip DRAFT- prefix from filename and update repo references.

Option A (PH-2026-05-27-008): filename, title, and Status align after PIC accept.

Usage:
  python scripts/promote-platform-adr.py --root . --all-accepted
  python scripts/promote-platform-adr.py --root . --file docs/platform-decision-records/DRAFT-RC-....md
  python scripts/promote-platform-adr.py --root . --claim-id RC-2026-05-27-014 --pic-cycle PIC-2026-05-28-026
  python scripts/promote-platform-adr.py --root . --all-accepted --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ADR_DIR = Path("docs/platform-decision-records")
STATUS_RE = re.compile(r"^## Status\s*\n\s*\n([^\n#]+)", re.MULTILINE)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
TEXT_SUFFIXES = {".md", ".mdc", ".yml", ".yaml", ".py", ".prompt.md", ".txt", ".json"}


def is_accepted(content: str) -> bool:
    m = STATUS_RE.search(content)
    if not m:
        return False
    status = m.group(1).strip()
    return status.startswith("Accepted")


def is_draft_filename(name: str) -> bool:
    return name.startswith("DRAFT-") and name.endswith(".md")


def promoted_name(name: str) -> str:
    if not is_draft_filename(name):
        return name
    return name[len("DRAFT-") :]


def normalize_content(content: str, pic_cycle: str | None = None) -> str:
    content = content.replace("# DRAFT ADR:", "# ADR:")
    content = re.sub(
        r"(Accepted \([^)]*)— pending CEO confirm\)",
        r"\1)",
        content,
    )
    content = re.sub(
        r"(Accepted \([^)]*) — pending CEO confirm\)",
        r"\1)",
        content,
    )
    if "## Approval" not in content and "## Status" in content:
        m = STATUS_RE.search(content)
        if m:
            status_line = m.group(1).strip()
            pic = pic_cycle or "unknown"
            if not pic_cycle:
                pic_m = re.search(r"PIC-[\w-]+", status_line)
                if pic_m:
                    pic = pic_m.group(0)
            date_m = re.search(r"(\d{4}-\d{2}-\d{2})", status_line)
            approved = date_m.group(1) if date_m else "2026-05-28"
            approval = (
                f"\n## Approval\n\n"
                f"- Approved: {approved}\n"
                f"- Cycle: {pic}\n"
                f"- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).\n"
            )
            insert_at = m.end()
            content = content[:insert_at] + approval + content[insert_at:]
    return content


def resolve_draft_adr(root: Path, claim_id: str) -> Path | None:
    """Find DRAFT ADR path for claim_id (e.g. RC-2026-05-27-014 or PH-2026-05-27-008)."""
    adr_root = root / ADR_DIR
    cid = claim_id.strip()
    matches = sorted(adr_root.glob(f"DRAFT-{cid}-*.md"))
    if matches:
        return matches[0]
    # Hygiene ids without date segment in glob: DRAFT-RC-implementation-priority-loop.md
    direct = adr_root / f"DRAFT-{cid}.md"
    if direct.is_file():
        return direct
    return None


def already_promoted(root: Path, claim_id: str) -> Path | None:
    adr_root = root / ADR_DIR
    cid = claim_id.strip()
    matches = sorted(adr_root.glob(f"{cid}-*.md"))
    if matches:
        return matches[0]
    direct = adr_root / f"{cid}.md"
    if direct.is_file():
        return direct
    return None


def collect_renames(root: Path, explicit: list[Path] | None) -> list[tuple[Path, Path]]:
    adr_root = root / ADR_DIR
    pairs: list[tuple[Path, Path]] = []
    if explicit:
        for p in explicit:
            if not p.is_file():
                raise FileNotFoundError(p)
            if not is_draft_filename(p.name):
                print(f"skip (not DRAFT- filename): {p}", file=sys.stderr)
                continue
            pairs.append((p, adr_root / promoted_name(p.name)))
        return pairs

    for path in sorted(adr_root.glob("DRAFT-*.md")):
        if path.name == "DRAFT-template-research-claim.md":
            continue
        text = path.read_text(encoding="utf-8")
        if is_accepted(text):
            pairs.append((path, adr_root / promoted_name(path.name)))
    return pairs


def replace_refs(root: Path, old_rel: str, new_rel: str, dry_run: bool) -> int:
    count = 0
    old_posix = old_rel.replace("\\", "/")
    new_posix = new_rel.replace("\\", "/")
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix not in TEXT_SUFFIXES and path.suffix != "":
            continue
        if path.name.endswith(".pyc"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if old_posix not in text:
            continue
        new_text = text.replace(old_posix, new_posix)
        if new_text != text:
            count += 1
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
    return count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--file", type=Path, action="append", help="Single ADR to promote")
    parser.add_argument(
        "--claim-id",
        action="append",
        help="Claim ID (e.g. RC-2026-05-27-014); resolves DRAFT-{id}-*.md",
    )
    parser.add_argument("--pic-cycle", help="PIC cycle id for Approval notes (e.g. PIC-2026-05-28-026)")
    parser.add_argument("--all-accepted", action="store_true", help="Promote all accepted DRAFT-* ADRs")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()

    if not args.all_accepted and not args.file and not args.claim_id:
        parser.error("Specify --all-accepted, --file, or --claim-id")

    explicit: list[Path] = []
    if args.file:
        explicit.extend(root / f if not f.is_absolute() else f for f in args.file)
    if args.claim_id:
        for cid in args.claim_id:
            draft = resolve_draft_adr(root, cid)
            if draft:
                explicit.append(draft)
            elif already_promoted(root, cid):
                print(f"already promoted: {cid}", file=sys.stderr)
            else:
                print(f"error: no DRAFT ADR for claim-id {cid}", file=sys.stderr)
                return 1

    pairs = collect_renames(root, explicit if explicit else None)

    if not pairs:
        print("No ADRs to promote.")
        return 0

    print(f"Promoting {len(pairs)} ADR(s){' (dry-run)' if args.dry_run else ''}:")
    for old, new in pairs:
        print(f"  {old.relative_to(root)} -> {new.relative_to(root)}")

    if args.dry_run:
        return 0

    for old, new in pairs:
        if new.exists():
            print(f"error: target exists: {new}", file=sys.stderr)
            return 1
        content = normalize_content(old.read_text(encoding="utf-8"), pic_cycle=args.pic_cycle)
        old.write_text(content, encoding="utf-8")
        old.rename(new)

    ref_updates = 0
    for old, new in pairs:
        old_rel = old.relative_to(root).as_posix()
        new_rel = new.relative_to(root).as_posix()
        ref_updates += replace_refs(root, old_rel, new_rel, dry_run=False)

    print(f"Updated references in {ref_updates} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
