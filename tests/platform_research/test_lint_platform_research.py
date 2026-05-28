from __future__ import annotations

import importlib.util
import sys
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[2]
LINT_SCRIPT = REPO_ROOT / "scripts" / "lint-platform-research.py"


def load_lint_module():
    spec = importlib.util.spec_from_file_location("lint_platform_research", LINT_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load lint-platform-research.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lint_platform_research = load_lint_module()


VALID_CLAIM = """\
```yaml
claim_id: RC-2026-05-27-001
source_transcript: raw/platform-transcripts/example/transcript.md
speaker: unknown
timestamp: unknown
claim_type: product_requirement
atomic_claim: "Every generated architecture section should cite its source."
verbatim_excerpt: "Every architecture section should cite the source."
implied_assumption: "Citations increase trust and review speed."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Keep existing citation requirements."
affected_components:
  - align-cite
related_second_brain_principles:
  - grounding
expected_benefit: "Improves traceability."
possible_regression: "More verbose drafts."
validation_method: "Review generated artifacts."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "Strengthens the core workflow."
next_action: "Keep existing citation requirements."
```
"""


VALID_REPORT = """\
# Research Impact Report: Example

## Executive Judgment

This transcript contains one useful claim.

## Source

- Transcript: raw/platform-transcripts/example/transcript.md

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 1 |

## Highest-Value Claims

RC-2026-05-27-001

## Highest-Risk Claims

None.

## Recommended Next Actions

None.

## Trust Loop Summary

No fail-closed violations in this fixture review.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-001 | adopt | Approve draft ADR via implementation backlog. |

## Protected Files Not Modified

Confirmed.
"""


class ResearchLintTests(unittest.TestCase):
    def write(self, root: Path, rel: str, text: str) -> Path:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_non_strict_fresh_repo_passes_without_artifacts(self) -> None:
        with TemporaryDirectory() as tmp:
            result = lint_platform_research.lint(Path(tmp), strict=False)
            self.assertEqual(result.errors, [])
            self.assertEqual(result.warnings, [])

    def test_strict_requires_register_and_report_directory(self) -> None:
        with TemporaryDirectory() as tmp:
            result = lint_platform_research.lint(Path(tmp), strict=True)
            self.assertIn("Missing wiki/platform-research/claim-register.md", result.errors)
            self.assertIn("Missing reports/platform-research-review directory", result.errors)

    def test_valid_claim_register_and_report_pass(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "wiki/platform-research/claim-register.md", "# Register\n\n" + VALID_CLAIM)
            self.write(root, "reports/platform-research-review/example-impact-report.md", VALID_REPORT)

            result = lint_platform_research.lint(root, strict=False)
            self.assertEqual(result.errors, [])
            self.assertEqual(result.warnings, [])

    def test_invalid_claim_records_are_errors(self) -> None:
        bad_claim = textwrap.dedent(
            """\
            ```yaml
            claim_id: RC-2026-05-27-002
            source_transcript: raw/platform-transcripts/example/transcript.md
            claim_type: product_requirement
            current_design_status: unsupported
            impact_scores:
              governance: 3
            total_score: high
            decision: maybe
            decision_rationale: ""
            next_action: ""
            ```
            """
        )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "wiki/platform-research/claim-register.md", "# Register\n\n" + bad_claim)

            result = lint_platform_research.lint(root, strict=False)
            self.assertTrue(any("missing required field: atomic_claim" in error for error in result.errors))
            self.assertTrue(any("invalid decision: maybe" in error for error in result.errors))
            self.assertTrue(any("out-of-range impact score for governance: 3" in error for error in result.errors))
            self.assertTrue(any("non-integer total_score: high" in error for error in result.errors))

    def test_template_claim_record_is_allowed(self) -> None:
        template_claim = (REPO_ROOT / "templates" / "platform-research" / "claim-record.yml").read_text(encoding="utf-8")

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "wiki/platform-research/claim-register.md", f"# Register\n\n```yaml\n{template_claim}\n```")

            result = lint_platform_research.lint(root, strict=False)
            self.assertEqual(result.errors, [])

    def test_report_shape_warnings(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "reports/platform-research-review/bad.md", "# Research Impact Report: Bad\n")

            result = lint_platform_research.lint(root, strict=False)
            self.assertTrue(any("missing section: ## Executive Judgment" in warning for warning in result.warnings))

    def test_protected_file_contamination_warning(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "PRD.md", "source_transcript: raw/platform-transcripts/example/transcript.md\n")

            result = lint_platform_research.lint(root, strict=False)
            self.assertTrue(any("Protected file may contain transcript-derived claim content: PRD.md" in warning for warning in result.warnings))

    def test_imported_prompts_use_current_root_doc_paths(self) -> None:
        imported_files = [
            REPO_ROOT / ".github" / "prompts" / "platform-research-review.prompt.md",
            REPO_ROOT / ".github" / "prompts" / "platform-research-review" / "grounding-agent.prompt.md",
            REPO_ROOT / ".github" / "skills" / "platform-research-review" / "SKILL.md",
            REPO_ROOT / ".cursor" / "agents" / "platform-research-reviewer.md",
            REPO_ROOT / "config" / "platform-research-review.example.yml",
            REPO_ROOT / "docs" / "platform-intelligence" / "platform-research-review-setup.md",
        ]

        for path in imported_files:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("docs/product-brief.md", text, path.as_posix())
            self.assertNotIn("docs/PRD.md", text, path.as_posix())

    def test_old_unlabeled_paths_are_absent(self) -> None:
        old_paths = [
            "raw/transcripts",
            "wiki/research",
            "reports/research-review",
            ".github/prompts/research-review",
            ".github/prompts/research-review.prompt.md",
            ".github/skills/research-review",
            "config/research-review.example.yml",
            "templates/research",
            "docs/product-intelligence",
            "docs/decision-records",
            "scripts/lint-research.py",
            "tests/research_review",
            "tests/fixtures/research-review",
            ".cursor/agents/research-reviewer.md",
            ".cursor/rules/second-brain-research-safety.mdc",
        ]

        for rel in old_paths:
            self.assertFalse((REPO_ROOT / rel).exists(), rel)

    def test_workspace_prompts_do_not_depend_on_platform_research(self) -> None:
        prompt_dir = REPO_ROOT / ".github" / "prompts"
        workspace_prompts = sorted(prompt_dir.glob("workspace-*.prompt.md"))
        self.assertTrue(workspace_prompts)

        for path in workspace_prompts:
            if path.name == "workspace-lint.prompt.md":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("raw/platform-transcripts", text, path.as_posix())
            self.assertNotIn("wiki/platform-research", text, path.as_posix())
            self.assertNotIn("reports/platform-research-review", text, path.as_posix())

    def test_rejected_claims_are_mirrored_in_rejection_register(self) -> None:
        result = lint_platform_research.lint(REPO_ROOT, strict=False)
        self.assertFalse(
            any("missing from wiki/platform-research/rejected-ideas.md" in error for error in result.errors),
            result.errors,
        )

    def test_fail_closed_blocks_adopt_with_unvalidated_external_claim(self) -> None:
        bad_claim = textwrap.dedent(
            """\
            ```yaml
            claim_id: RC-2026-05-27-099
            source_transcript: raw/platform-transcripts/example/transcript.md
            claim_type: product_requirement
            atomic_claim: "Vendor X supports feature Y."
            current_design_status: unsupported
            requires_external_validation: true
            validation_status: unvalidated
            correction_route: "Validate against vendor docs."
            impact_scores:
              governance: 1
              closure: 0
              grounding: 1
              vendor_truth: 1
              inspectability: 0
              maintainability: 0
              differentiation: 0
              enterprise_fit: 0
              human_review_leverage: 0
            total_score: 3
            decision: adopt
            decision_rationale: "Should not pass fail-closed."
            next_action: "Validate first."
            ```
            """
        )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "wiki/platform-research/claim-register.md", "# Register\n\n" + bad_claim)

            result = lint_platform_research.lint(root, strict=False)
            self.assertTrue(
                any("fail-closed violation" in error for error in result.errors),
                result.errors,
            )

    def test_implementation_backlog_shape(self) -> None:
        result = lint_platform_research.lint(REPO_ROOT, strict=False)
        self.assertFalse(
            any("implementation-backlog.md missing section" in error for error in result.errors),
            result.errors,
        )

    def test_implementation_backlog_missing_sections_are_errors(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "wiki/platform-research/implementation-backlog.md", "# Backlog\n")

            result = lint_platform_research.lint(root, strict=False)
            self.assertTrue(
                any("implementation-backlog.md missing section: ## Active policy" in error for error in result.errors)
            )


if __name__ == "__main__":
    unittest.main()
