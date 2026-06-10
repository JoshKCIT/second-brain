"""Integration test: ingest → triage → sync."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from tests.workspace_rss._load import REPO_ROOT, load_module

ingest_rss = load_module("ingest_rss_pipe", "ingest-rss.py")
triage_rss = load_module("triage_rss_pipe", "triage-rss.py")
sync_rss = load_module("sync_rss_pipe", "sync-rss-register.py")


class TestRssPipeline(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(
            REPO_ROOT / "tests" / "fixtures" / "workspace-rss",
            self.tmp / "tests" / "fixtures" / "workspace-rss",
        )
        (self.tmp / "config").mkdir(parents=True)
        shutil.copy(
            self.tmp / "tests" / "fixtures" / "workspace-rss" / "rss-feeds.yml",
            self.tmp / "config" / "rss-feeds.yml",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_full_pipeline(self) -> None:
        old_argv = sys.argv
        try:
            sys.argv = ["ingest-rss.py", "--root", str(self.tmp), "--yes"]
            self.assertEqual(ingest_rss.main(), 0)
            sys.argv = ["triage-rss.py", "--root", str(self.tmp), "--yes"]
            self.assertEqual(triage_rss.main(), 0)
            sys.argv = ["sync-rss-register.py", "--root", str(self.tmp)]
            self.assertEqual(sync_rss.main(), 0)
        finally:
            sys.argv = old_argv

        reg = (self.tmp / "raw" / "workspace-rss-feed" / "rss-register.md").read_text(encoding="utf-8")
        self.assertIn("Review queue:", reg)
        # noise items should be auto_skip (not in review section count from summary)
        self.assertIn("Auto-skipped", reg)


if __name__ == "__main__":
    unittest.main()
