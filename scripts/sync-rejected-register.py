#!/usr/bin/env python3
"""
Rebuild wiki/platform-research/rejected-ideas.md from rejected claims in
wiki/platform-research/claim-register.md.

Preserves existing rejected_pattern (RP-*) YAML blocks and decision history
rows when re-run.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

REGISTER_REL = Path("wiki/platform-research/claim-register.md")
OUTPUT_REL = Path("wiki/platform-research/rejected-ideas.md")
TEMPLATE_REL = Path("templates/platform-research/rejected-ideas.md")

CLAIM_BLOCK_RE = re.compile(r"```yaml\s*(.*?)```", re.DOTALL | re.IGNORECASE)
TRANSCRIPT_LINE = re.compile(
    r"^- Transcript:\s*`(raw/platform-transcripts/[^`]+)`",
    re.MULTILINE,
)
FIELD_RE = re.compile(r"^([a-z_]+):\s*(.*)$", re.MULTILINE)
RECORD_BLOCK_RE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)


def _escape_yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def get_scalar(block: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}\s*:\s*([^\n#]+)", block, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def is_template_claim(block: str) -> bool:
    return "RC-YYYY-MM-DD" in block


def parse_claim_blocks(text: str) -> list[str]:
    return [b for b in CLAIM_BLOCK_RE.findall(text) if "claim_id:" in b]


def index_transcript_artifacts(root: Path) -> dict[str, tuple[str, str]]:
    """Map raw transcript path -> (claims_analysis, impact_report) relative paths."""
    mapping: dict[str, tuple[str, str]] = {}

    analyses_dir = root / "wiki/platform-research/transcript-analyses"
    if analyses_dir.is_dir():
        for path in sorted(analyses_dir.glob("*-claims.md")):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for source in TRANSCRIPT_LINE.findall(text):
                rel = path.relative_to(root).as_posix()
                claims, impact = mapping.get(source, ("", ""))
                mapping[source] = (rel, impact)

    reports_dir = root / "reports/platform-research-review"
    if reports_dir.is_dir():
        for path in sorted(reports_dir.glob("*-impact-report.md")):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for source in TRANSCRIPT_LINE.findall(text):
                claims, impact = mapping.get(source, ("", ""))
                rel = path.relative_to(root).as_posix()
                mapping[source] = (claims, rel)

    return mapping


def default_next_review(last_reviewed: str) -> str:
    try:
        base = date.fromisoformat(last_reviewed)
    except ValueError:
        base = date.today()
    return (base + timedelta(days=90)).isoformat()


def short_idea(atomic_claim: str, limit: int = 72) -> str:
    text = atomic_claim.strip().strip('"')
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


@dataclass
class RejectedRecord:
    claim_id: str
    source_transcript: str
    claim_analysis: str
    impact_report: str
    atomic_claim: str
    verbatim_excerpt: str
    total_score: str
    decision_rationale: str
    rejection_reason: str
    safer_variant: str
    reopen_conditions: str
    next_review_after: str
    decision_date: str
    last_reviewed: str
    owner: str

    def as_yaml(self) -> str:
        lines = [
            "```yaml",
            f"record_id: {self.claim_id}",
            "record_type: rejected_claim",
            f"source_transcript: {self.source_transcript}",
            f"claim_analysis: {self.claim_analysis}",
            f"impact_report: {self.impact_report}",
            f'atomic_claim: "{_escape_yaml(self.atomic_claim)}"',
            f'verbatim_excerpt: "{_escape_yaml(self.verbatim_excerpt)}"',
            "decision: reject",
            f"decision_date: {self.decision_date}",
            f"next_review_after: {self.next_review_after}",
            "review_cadence: quarterly",
            f"total_score: {self.total_score}",
            f'decision_rationale: "{_escape_yaml(self.decision_rationale)}"',
            f'rejection_reason: "{_escape_yaml(self.rejection_reason)}"',
            f'safer_variant: "{_escape_yaml(self.safer_variant)}"',
            "reopen_conditions:",
            f'  - "{_escape_yaml(self.reopen_conditions)}"',
            f"owner: {self.owner}",
            "status: closed",
            f"last_reviewed: {self.last_reviewed}",
            "```",
        ]
        return "\n".join(lines)


def claim_to_record(block: str, artifact_index: dict[str, tuple[str, str]]) -> RejectedRecord | None:
    if is_template_claim(block):
        return None
    if get_scalar(block, "decision") != "reject":
        return None

    claim_id = get_scalar(block, "claim_id")
    if not claim_id:
        return None

    source = get_scalar(block, "source_transcript") or ""
    claims_rel, impact_rel = artifact_index.get(source, ("", ""))

    atomic = get_scalar(block, "atomic_claim") or ""
    rationale = get_scalar(block, "decision_rationale") or ""
    regression = get_scalar(block, "possible_regression") or ""
    next_action = get_scalar(block, "next_action") or ""
    validation = get_scalar(block, "validation_method") or ""

    last_reviewed = get_scalar(block, "last_reviewed") or date.today().isoformat()
    next_review = get_scalar(block, "next_review_after") or default_next_review(last_reviewed)

    safer = next_action
    if "safer" not in safer.lower():
        safer = next_action or "Submit a narrower claim scoped to Second Brain governance band."

    reopen = validation or next_action or "Re-review when inspectable, citation-grounded variant is proposed."

    return RejectedRecord(
        claim_id=claim_id,
        source_transcript=source,
        claim_analysis=claims_rel,
        impact_report=impact_rel,
        atomic_claim=atomic,
        verbatim_excerpt=get_scalar(block, "verbatim_excerpt") or "",
        total_score=get_scalar(block, "total_score") or "0",
        decision_rationale=rationale,
        rejection_reason=regression or rationale,
        safer_variant=safer,
        reopen_conditions=reopen,
        next_review_after=next_review,
        decision_date=last_reviewed,
        last_reviewed=last_reviewed,
        owner=get_scalar(block, "owner") or "unassigned",
    )


def extract_pattern_blocks(existing: str) -> list[str]:
    blocks: list[str] = []
    in_patterns = False
    for block in RECORD_BLOCK_RE.findall(existing):
        if get_scalar(block, "record_type") == "rejected_pattern":
            blocks.append("```yaml\n" + block.strip() + "\n```")
    return blocks


def extract_decision_history(existing: str) -> list[str]:
    rows: list[str] = []
    in_history = False
    for line in existing.splitlines():
        if line.strip() == "## Decision history":
            in_history = True
            continue
        if in_history and line.startswith("## "):
            break
        if in_history and line.startswith("|") and not line.startswith("| Date"):
            if line.strip() != "|---|---|---|---|":
                rows.append(line)
    return rows


def build_register(root: Path) -> tuple[str, list[str]]:
    warnings: list[str] = []
    register_path = root / REGISTER_REL
    if not register_path.is_file():
        raise FileNotFoundError(f"Missing {REGISTER_REL}")

    claim_text = register_path.read_text(encoding="utf-8")
    artifact_index = index_transcript_artifacts(root)

    records: list[RejectedRecord] = []
    for block in parse_claim_blocks(claim_text):
        rec = claim_to_record(block, artifact_index)
        if rec:
            records.append(rec)

    records.sort(key=lambda r: r.claim_id)

    existing = ""
    out_path = root / OUTPUT_REL
    if out_path.is_file():
        existing = out_path.read_text(encoding="utf-8")

    pattern_blocks = extract_pattern_blocks(existing)
    history_rows = extract_decision_history(existing)

    today = date.today().isoformat()
    next_scheduled = default_next_review(today)

    summary_rows = []
    for rec in records:
        summary_rows.append(
            f"| {rec.claim_id} | {short_idea(rec.atomic_claim)} | {rec.decision_date} | "
            f"{rec.next_review_after} | closed | {rec.claim_analysis or '—'} |"
        )

    body = [
        "# Rejected Claims Register",
        "",
        "This register preserves rejected claims and recurring rejection patterns so they are not "
        "rediscovered repeatedly.",
        "",
        "Each rejected claim from `wiki/platform-research/claim-register.md` must have a matching "
        "record here with rationale, safer variant, and re-review date.",
        "",
        "Sync after claim register updates:",
        "",
        "```bash",
        "python scripts/sync-rejected-register.py --root .",
        "```",
        "",
        "## Review cadence",
        "",
        "| Rule | Value |",
        "|---|---|",
        "| Default re-review interval | Every 3 months |",
        f"| Next scheduled re-review | {next_scheduled} |",
        "",
        "## Summary index",
        "",
        "| ID | Idea (short) | Rejected | Next review | Status | Primary artifact |",
        "|---|---|---|---|---|---|",
    ]
    if summary_rows:
        body.extend(summary_rows)
    else:
        body.append("| _No rejected claims._ | | | | | |")

    body.extend(
        [
            "",
            f"_Last synced: {today}. {len(records)} rejected claim(s)._",
            "",
            "## Rejected claim records",
            "",
            "One YAML block per rejected claim ID (`RC-*`). Generated from claim register; edit "
            "`safer_variant` / `reopen_conditions` manually if needed.",
            "",
        ]
    )

    for rec in records:
        if not rec.claim_analysis:
            warnings.append(f"{rec.claim_id}: no matching transcript-analyses file for source")
        body.append(rec.as_yaml())
        body.append("")

    body.extend(
        [
            "## Rejected recurring patterns",
            "",
            "One YAML block per cross-transcript pattern (`RP-*`). Preserved across sync when present.",
            "",
        ]
    )
    if pattern_blocks:
        body.extend(pattern_blocks)
        body.append("")
    else:
        body.append("_No recurring patterns recorded yet._")
        body.append("")

    body.extend(
        [
            "## Decision history",
            "",
            "| Date | ID | Action | Notes |",
            "|---|---|---|---|",
        ]
    )
    sync_row = f"| {today} | _sync_ | synced | Rebuilt from claim-register.md ({len(records)} rejects) |"
    if sync_row not in history_rows:
        history_rows.append(sync_row)
    if history_rows:
        body.extend(history_rows)
    else:
        body.append(f"| {today} | — | initialized | Register created |")

    return "\n".join(body).rstrip() + "\n", warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repo root")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if rejected-ideas.md would change (for CI)",
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress stdout")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    out_path = root / OUTPUT_REL

    try:
        new_content, warnings = build_register(root)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    changed = True
    if out_path.is_file():
        changed = out_path.read_text(encoding="utf-8") != new_content

    if args.check:
        if changed:
            if not args.quiet:
                print(f"Register is out of date: {OUTPUT_REL}", file=sys.stderr)
            return 1
        if not args.quiet:
            print("Rejected register is up to date.")
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_content, encoding="utf-8")

    if not args.quiet:
        print(f"Wrote {OUTPUT_REL}")
        for w in warnings:
            print(f"  warning: {w}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
