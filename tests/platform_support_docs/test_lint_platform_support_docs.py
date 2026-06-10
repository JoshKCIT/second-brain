"""Tests for lint-platform-support-docs.py."""

from __future__ import annotations

import unittest
from pathlib import Path

from tests.platform_support_docs._load import REPO_ROOT, load_module

lint_mod = load_module("lint_platform_support_docs", "lint-platform-support-docs.py")


class TestLintPlatformSupportDocs(unittest.TestCase):
    def test_live_repo_passes_strict(self) -> None:
        result = lint_mod.run_lint(REPO_ROOT, strict=True)
        self.assertEqual(result.errors, [], msg="\n".join(result.errors))

    def test_missing_manifest_fails(self) -> None:
        # Use invalid fixture if present; otherwise skip structural test
        fixture = REPO_ROOT / "tests/fixtures/platform-support-docs/invalid-root"
        if not fixture.is_dir():
            self.skipTest("invalid-root fixture not present")
        result = lint_mod.run_lint(fixture, strict=False)
        self.assertTrue(result.errors)


if __name__ == "__main__":
    unittest.main()
