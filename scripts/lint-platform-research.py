#!/usr/bin/env python3
"""
Lightweight lint checks for Second Brain platform-research-review artifacts.

The default mode is friendly to a fresh clone: missing research output is allowed
until the workflow has actually run. Use --strict for release or CI validation.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REQUIRED_CLAIM_FIELDS = [
    "claim_id",
    "source_transcript",
    "claim_type",
    "atomic_claim",
    "current_design_status",
    "validation_status",
    "correction_route",
    "impact_scores",
    "total_score",
    "decision",
    "decision_rationale",
    "next_action",
]

VALID_VALIDATION_STATUSES = {
    "unvalidated",
    "supported_by_current_design",
    "validated_against_design",
    "validated",
}

DEFAULT_CORRECTION_ROUTES = {
    "adopt": "Approve draft ADR via implementation backlog; reject via backlog rollback.",
    "experiment": "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback.",
    "defer": "Re-enter queue when blocker clears; update claim register decision.",
    "reject": "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim.",
    "monitor": "Re-review when external validation is available; do not promote without validation.",
}

SCORING_AXES = [
    "governance",
    "closure",
    "grounding",
    "vendor_truth",
    "inspectability",
    "maintainability",
    "differentiation",
    "enterprise_fit",
    "human_review_leverage",
]

VALID_DECISIONS = {"adopt", "experiment", "defer", "reject", "monitor"}

PROTECTED_PATHS = [
    "wiki/workspace-standards",
    "wiki/workspace-recommendations",
]

PROTECTED_FILES = [
    "PRD.md",
    "product-brief.md",
    "docs/product/roadmap.md",
    "docs/product/architecture-rationale.md",
    "AGENTS.md",
]

TRANSCRIPT_DERIVED_PATTERNS = [
    re.compile(r"claim_id:\s*RC-\d{4}-\d{2}-\d{2}-\d+", re.IGNORECASE),
    re.compile(r"source_transcript:\s*raw/platform-transcripts/", re.IGNORECASE),
]

REQUIRED_REPORT_SECTIONS = [
    "## Executive Judgment",
    "## Source",
    "## Claim Summary",
    "## Highest-Value Claims",
    "## Highest-Risk Claims",
    "## Recommended Next Actions",
    "## Protected Files Not Modified",
]

TRUST_LOOP_REPORT_SECTIONS = [
    "## Trust Loop Summary",
    "## Correction Routes",
]

REQUIRED_BACKLOG_SECTIONS = [
    "## Active policy",
    "## Priority formula",
    "## Queue",
    "## Current cycle",
    "## Decision history",
]


@dataclass
class LintResult:
    errors: list[str]
    warnings: list[str]

    def extend(self, other: "LintResult") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


def iter_files(root: Path, rels: Iterable[str]) -> Iterable[Path]:
    for rel in rels:
        path = root / rel
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from path.rglob("*.md")


def split_yaml_blocks(text: str) -> list[str]:
    return re.findall(r"```yaml\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)


def is_template_claim(block: str) -> bool:
    return "RC-YYYY-MM-DD" in block


def get_scalar(block: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}\s*:\s*([^\n#]+)", block, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def lint_claim_block(block: str, idx: int) -> LintResult:
    result = LintResult(errors=[], warnings=[])
    template = is_template_claim(block)

    for field in REQUIRED_CLAIM_FIELDS:
        if not re.search(rf"^\s*{re.escape(field)}\s*:", block, flags=re.MULTILINE):
            result.errors.append(f"Claim block {idx} missing required field: {field}")

    if template:
        return result

    decision = get_scalar(block, "decision")
    if decision is not None and decision not in VALID_DECISIONS:
        result.errors.append(f"Claim block {idx} has invalid decision: {decision}")

    scores_match = re.search(r"^\s*impact_scores:[ \t]*(.*?)(?:\n\S|\Z)", block + "\nEND:", flags=re.DOTALL | re.MULTILINE)
    if not scores_match:
        result.errors.append(f"Claim block {idx} missing impact_scores mapping")
        return result

    scores_text = scores_match.group(1)
    for axis in SCORING_AXES:
        axis_match = re.search(rf"^\s+{re.escape(axis)}\s*:\s*(-?\d+)\s*$", scores_text, flags=re.MULTILINE)
        if not axis_match:
            result.errors.append(f"Claim block {idx} missing impact score axis: {axis}")
            continue
        value = int(axis_match.group(1))
        if value < -2 or value > 2:
            result.errors.append(f"Claim block {idx} has out-of-range impact score for {axis}: {value}")

    total_score = get_scalar(block, "total_score")
    if total_score is not None and not re.fullmatch(r"-?\d+", total_score):
        result.errors.append(f"Claim block {idx} has non-integer total_score: {total_score}")

    validation_status = get_scalar(block, "validation_status")
    if validation_status is not None and validation_status not in VALID_VALIDATION_STATUSES:
        result.errors.append(
            f"Claim block {idx} has invalid validation_status: {validation_status}"
        )

    requires_external = get_scalar(block, "requires_external_validation")
    if (
        decision == "adopt"
        and requires_external == "true"
        and validation_status == "unvalidated"
    ):
        result.errors.append(
            f"Claim block {idx} fail-closed violation: adopt with unvalidated external validation"
        )

    return result


def lint_claim_register(root: Path, strict: bool) -> LintResult:
    result = LintResult(errors=[], warnings=[])
    register = root / "wiki/platform-research/claim-register.md"

    if not register.exists():
        if strict:
            result.errors.append("Missing wiki/platform-research/claim-register.md")
        return result

    text = register.read_text(encoding="utf-8")
    blocks = split_yaml_blocks(text)
    claim_blocks = [block for block in blocks if "claim_id:" in block]

    if not claim_blocks:
        result.errors.append("wiki/platform-research/claim-register.md contains no YAML claim records")
        return result

    for idx, block in enumerate(claim_blocks, start=1):
        result.extend(lint_claim_block(block, idx))

    result.extend(lint_rejected_claim_register(root, claim_blocks))

    return result


def extract_rejected_claim_ids(claim_blocks: list[str]) -> set[str]:
    rejected: set[str] = set()
    for block in claim_blocks:
        if is_template_claim(block):
            continue
        if get_scalar(block, "decision") != "reject":
            continue
        claim_id = get_scalar(block, "claim_id")
        if claim_id:
            rejected.add(claim_id)
    return rejected


def extract_rejection_register_ids(text: str) -> set[str]:
    ids: set[str] = set()
    for block in split_yaml_blocks(text):
        record_id = get_scalar(block, "record_id")
        if record_id and re.fullmatch(r"(RC|RP)-\d{4}-\d{2}-\d{2}-\d+[a-z]?", record_id):
            ids.add(record_id)
    return ids


def lint_rejected_claim_register(root: Path, claim_blocks: list[str]) -> LintResult:
    result = LintResult(errors=[], warnings=[])
    rejected_register = root / "wiki/platform-research/rejected-ideas.md"
    rejected_claim_ids = extract_rejected_claim_ids(claim_blocks)

    if not rejected_claim_ids:
        return result

    if not rejected_register.exists():
        result.errors.append(
            "Missing wiki/platform-research/rejected-ideas.md for rejected claim history"
        )
        return result

    register_text = rejected_register.read_text(encoding="utf-8")
    register_ids = extract_rejection_register_ids(register_text)

    for claim_id in sorted(rejected_claim_ids):
        if claim_id not in register_ids:
            result.errors.append(
                f"Rejected claim {claim_id} missing from wiki/platform-research/rejected-ideas.md"
            )

    return result


def strip_fenced_code(text: str) -> str:
    text = re.sub(r"````.*?````", "", text, flags=re.DOTALL)
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def lint_protected_files(root: Path) -> LintResult:
    result = LintResult(errors=[], warnings=[])

    for path in iter_files(root, [*PROTECTED_PATHS, *PROTECTED_FILES]):
        try:
            text = strip_fenced_code(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            continue

        rel = path.relative_to(root)
        for pattern in TRANSCRIPT_DERIVED_PATTERNS:
            if pattern.search(text):
                result.warnings.append(
                    f"Protected file may contain transcript-derived claim content: {rel} "
                    f"matched /{pattern.pattern}/"
                )

    return result


def lint_implementation_backlog(root: Path) -> LintResult:
    result = LintResult(errors=[], warnings=[])
    backlog = root / "wiki/platform-research/implementation-backlog.md"

    if not backlog.exists():
        return result

    text = backlog.read_text(encoding="utf-8")
    for section in REQUIRED_BACKLOG_SECTIONS:
        if section not in text:
            result.errors.append(
                f"wiki/platform-research/implementation-backlog.md missing section: {section}"
            )

    return result


def lint_reports(root: Path, strict: bool) -> LintResult:
    result = LintResult(errors=[], warnings=[])
    report_dir = root / "reports/platform-research-review"

    if not report_dir.exists():
        if strict:
            result.errors.append("Missing reports/platform-research-review directory")
        return result

    reports = list(report_dir.rglob("*.md"))
    if strict and not reports:
        result.errors.append("No platform-research-review reports found under reports/platform-research-review")

    for path in reports:
        text = path.read_text(encoding="utf-8")
        sections = list(REQUIRED_REPORT_SECTIONS)
        if path.name.endswith("-impact-report.md"):
            sections.extend(TRUST_LOOP_REPORT_SECTIONS)
        for section in sections:
            if section not in text:
                result.warnings.append(f"{path.relative_to(root)} missing section: {section}")

    return result


def lint(root: Path, strict: bool) -> LintResult:
    result = LintResult(errors=[], warnings=[])
    result.extend(lint_claim_register(root, strict=strict))
    result.extend(lint_implementation_backlog(root))
    result.extend(lint_protected_files(root))
    result.extend(lint_reports(root, strict=strict))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Second Brain platform-research-review artifacts.")
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--strict", action="store_true", help="Require platform-research-review artifacts to exist.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    result = lint(root, strict=args.strict)

    if result.errors:
        print("ERRORS:", file=sys.stderr)
        for item in result.errors:
            print(f"- {item}", file=sys.stderr)

    if result.warnings:
        print("WARNINGS:", file=sys.stderr)
        for item in result.warnings:
            print(f"- {item}", file=sys.stderr)

    if not result.errors and not result.warnings:
        print("Platform research lint passed.")
    elif not result.errors:
        print("Platform research lint completed with warnings.")

    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
