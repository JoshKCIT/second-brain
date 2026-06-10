"""Doc path existence and stale reference guards after doc restructure."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BUILD_HISTORY_FILES = [
    "docs/build-history/README.md",
    "docs/build-history/phase-1a-exit-report.md",
    "docs/build-history/phase-2-exit-report.md",
    "docs/build-history/phase-2-plan.md",
]

OLD_PHASE_PATHS = [
    "docs/phase-1a-exit-report.md",
    "docs/phase-2-exit-report.md",
    "docs/phase-2-plan.md",
]

PRODUCT_FILES = [
    "docs/product/README.md",
    "docs/product/roadmap.md",
    "docs/product/architecture-rationale.md",
    "docs/product/vendor-catalog.md",
]

OLD_PRODUCT_PATHS = [
    "docs/roadmap.md",
    "docs/architecture-rationale.md",
    "docs/vendor-catalog.md",
]

STALE_PRODUCT_REF = re.compile(
    r"docs/(?:roadmap|architecture-rationale|vendor-catalog)\.md"
)


class TestDocPathsExist(unittest.TestCase):
    def test_build_history_files_exist(self) -> None:
        for rel in BUILD_HISTORY_FILES:
            self.assertTrue((ROOT / rel).is_file(), f"missing {rel}")

    def test_old_phase_paths_removed(self) -> None:
        for rel in OLD_PHASE_PATHS:
            self.assertFalse((ROOT / rel).exists(), f"stale path still exists: {rel}")

    def test_product_files_exist(self) -> None:
        for rel in PRODUCT_FILES:
            self.assertTrue((ROOT / rel).is_file(), f"missing {rel}")

    def test_old_product_paths_removed(self) -> None:
        for rel in OLD_PRODUCT_PATHS:
            self.assertFalse((ROOT / rel).exists(), f"stale path still exists: {rel}")

    def test_lint_protected_product_paths_exist(self) -> None:
        lint_path = ROOT / "scripts" / "lint-platform-research.py"
        text = lint_path.read_text(encoding="utf-8")
        for rel in (
            "docs/product/roadmap.md",
            "docs/product/architecture-rationale.md",
        ):
            self.assertIn(rel, text)
            self.assertTrue((ROOT / rel).is_file(), f"missing protected {rel}")

    def test_no_stale_phase_refs_in_tracked_docs(self) -> None:
        STALE_PHASE_REF = re.compile(
            r"docs/phase-(?:1a-exit-report|2-exit-report|2-plan)\.md"
        )
        scan_roots = [
            ROOT / "docs",
            ROOT / "scripts",
            ROOT / "tests",
            ROOT / ".github",
        ]
        skip_files = {
            ROOT / "docs" / "progress-log.md",
        }
        violations: list[str] = []
        for base in scan_roots:
            if not base.exists():
                continue
            for path in base.rglob("*"):
                if not path.is_file():
                    continue
                if path.suffix not in (".md", ".py", ".yml", ".yaml", ".prompt.md"):
                    continue
                if path in skip_files:
                    continue
                if path.name == "test_doc_paths_exist.py":
                    continue
                if "build-history" in path.parts and path.name.startswith("phase-"):
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
                if STALE_PHASE_REF.search(text):
                    rel = path.relative_to(ROOT).as_posix()
                    violations.append(rel)
        self.assertEqual(violations, [], f"stale phase paths in: {violations}")

    def test_no_stale_product_refs_in_active_docs(self) -> None:
        scan_roots = [
            ROOT / "docs",
            ROOT / "scripts",
            ROOT / "tests",
            ROOT / ".github",
            ROOT / "templates",
            ROOT / "config",
        ]
        skip_files = {
            ROOT / "docs" / "progress-log.md",
        }
        violations: list[str] = []
        for base in scan_roots:
            if not base.exists():
                continue
            for path in base.rglob("*"):
                if not path.is_file():
                    continue
                if path.suffix not in (".md", ".py", ".yml", ".yaml", ".mdc"):
                    continue
                if path in skip_files:
                    continue
                if path.name == "test_doc_paths_exist.py":
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
                if STALE_PRODUCT_REF.search(text):
                    rel = path.relative_to(ROOT).as_posix()
                    violations.append(rel)
        self.assertEqual(violations, [], f"stale product paths in: {violations}")


if __name__ == "__main__":
    unittest.main()
