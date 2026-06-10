"""Integration: inventory + lint pipeline."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from tests.platform_support_docs._load import REPO_ROOT, load_module

sync_inv = load_module("sync_pipe_inv", "sync-support-doc-inventory.py")
lint_mod = load_module("lint_pipe", "lint-platform-support-docs.py")


class TestSupportDocsPipeline(unittest.TestCase):
    def test_full_pipeline_on_live_repo(self) -> None:
        old_argv = sys.argv
        sys.argv = ["sync-support-doc-inventory.py", "--root", str(REPO_ROOT), "--write"]
        try:
            self.assertEqual(sync_inv.main(), 0)
        finally:
            sys.argv = old_argv
        result = lint_mod.run_lint(REPO_ROOT, strict=True)
        self.assertEqual(result.errors, [])


if __name__ == "__main__":
    unittest.main()
