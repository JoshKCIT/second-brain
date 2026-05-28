from __future__ import annotations

import importlib.util
import sys
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

REPO_ROOT = Path(__file__).resolve().parents[2]
SYNC_SCRIPT = REPO_ROOT / "scripts" / "sync-rejected-register.py"
LINT_SCRIPT = REPO_ROOT / "scripts" / "lint-platform-research.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sync = load_module(SYNC_SCRIPT, "sync_rejected_register")
lint = load_module(LINT_SCRIPT, "lint_platform_research")


REJECTED_CLAIM = textwrap.dedent(
    """\
    ```yaml
    claim_id: RC-2026-05-27-099
    source_transcript: raw/platform-transcripts/example/transcript.md
    speaker: unknown
    timestamp: unknown
    claim_type: product_requirement
    atomic_claim: "Replace filesystem with vector-only search."
    verbatim_excerpt: "just use vectors"
    current_design_status: contradicted
    validation_status: unvalidated
    correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
    impact_scores:
      governance: -2
      closure: -1
      grounding: -1
      vendor_truth: 0
      inspectability: -2
      maintainability: 0
      differentiation: -1
      enterprise_fit: 0
      human_review_leverage: -1
    total_score: -8
    decision: reject
    decision_rationale: "Conflicts with inspectable page-index retrieval."
    next_action: "Monitor for hybrid retrieval with citation eval."
    possible_regression: "Opaque retrieval breaks align-cite."
    validation_method: "Re-open when holdout eval exists."
    last_reviewed: 2026-05-27
    next_review_after: 2026-08-27
    ```
    """
)


class SyncRejectedRegisterTests(unittest.TestCase):
    def test_builds_record_for_rejected_claim(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            register = root / "wiki/platform-research"
            register.mkdir(parents=True)
            (register / "claim-register.md").write_text(
                "# Register\n\n## Claim Records\n\n" + REJECTED_CLAIM,
                encoding="utf-8",
            )
            content, _ = sync.build_register(root)
            self.assertIn("record_id: RC-2026-05-27-099", content)
            self.assertIn("record_type: rejected_claim", content)
            self.assertIn("Conflicts with inspectable page-index retrieval.", content)

    def test_sync_satisfies_lint_mirror_check(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            pr = root / "wiki/platform-research"
            pr.mkdir(parents=True)
            (pr / "claim-register.md").write_text(
                "# Register\n\n" + REJECTED_CLAIM,
                encoding="utf-8",
            )
            content, _ = sync.build_register(root)
            (pr / "rejected-ideas.md").write_text(content, encoding="utf-8")

            register_text = (pr / "claim-register.md").read_text(encoding="utf-8")
            blocks = lint.split_yaml_blocks(register_text)
            claim_blocks = [b for b in blocks if "claim_id:" in b]
            result = lint.lint_rejected_claim_register(root, claim_blocks)
            self.assertEqual(result.errors, [])


class RejectedRegisterIntegrationTests(unittest.TestCase):
    def test_repo_rejected_register_matches_claim_register(self) -> None:
        result = lint.lint(REPO_ROOT, strict=False)
        mirror_errors = [
            e for e in result.errors if "missing from wiki/platform-research/rejected-ideas.md" in e
        ]
        self.assertEqual(mirror_errors, [], mirror_errors)


if __name__ == "__main__":
    unittest.main()
