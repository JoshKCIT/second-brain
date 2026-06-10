"""Unit tests for sync-rss-register.py."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from tests.workspace_rss._load import REPO_ROOT, load_module

ingest_rss = load_module("ingest_rss_sync", "ingest-rss.py")
triage_rss = load_module("triage_rss_sync", "triage-rss.py")
sync_rss = load_module("sync_rss_register", "sync-rss-register.py")
rss_common = load_module("rss_common_sync", "rss_common.py")


class TestSyncRssRegister(unittest.TestCase):
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
        old_argv = sys.argv
        sys.argv = ["ingest-rss.py", "--root", str(self.tmp), "--yes"]
        try:
            ingest_rss.main()
            sys.argv = ["triage-rss.py", "--root", str(self.tmp), "--yes"]
            triage_rss.main()
        finally:
            sys.argv = old_argv

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_register_has_review_queue(self) -> None:
        old_argv = sys.argv
        sys.argv = ["sync-rss-register.py", "--root", str(self.tmp)]
        try:
            sync_rss.main()
        finally:
            sys.argv = old_argv

        reg = (self.tmp / "raw" / "workspace-rss-feed" / "rss-register.md").read_text(encoding="utf-8")
        self.assertIn("## Review queue", reg)
        self.assertIn("item_id:", reg)
        self.assertIn("summary_excerpt:", reg)
        self.assertIn("Microsoft Copilot Studio documents MCP server integration.", reg)

    def test_fixture_url_flag(self) -> None:
        old_argv = sys.argv
        sys.argv = ["sync-rss-register.py", "--root", str(self.tmp)]
        try:
            sync_rss.main()
        finally:
            sys.argv = old_argv
        reg = (self.tmp / "raw" / "workspace-rss-feed" / "rss-register.md").read_text(encoding="utf-8")
        self.assertIn("review_flags:", reg)
        self.assertIn("fixture_url", reg)

    def test_preserve_notes(self) -> None:
        reg_path = self.tmp / "raw" / "workspace-rss-feed" / "rss-register.md"
        rss_common.ensure_rss_dirs(self.tmp)
        item_id = ""
        for path in rss_common.iter_item_files(self.tmp):
            meta, _ = rss_common.parse_item_file(path)
            if meta.get("triage_status") in ("suggested", "high_signal", "borderline"):
                item_id = str(meta["item_id"])
                break
        self.assertTrue(item_id, "expected at least one queued item")
        reg_path.write_text(
            "# RSS Feed Register\n\n## Review queue\n\n```yaml\n"
            f"item_id: {item_id}\nnotes: \"CEO note\"\n```\n",
            encoding="utf-8",
        )

        old_argv = sys.argv
        sys.argv = ["sync-rss-register.py", "--root", str(self.tmp)]
        try:
            sync_rss.main()
        finally:
            sys.argv = old_argv

        text = reg_path.read_text(encoding="utf-8")
        self.assertIn('notes: "CEO note"', text)


if __name__ == "__main__":
    unittest.main()
