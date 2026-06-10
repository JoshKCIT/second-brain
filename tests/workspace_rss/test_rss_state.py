"""State file integrity tests."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from tests.workspace_rss._load import REPO_ROOT, load_module

ingest_rss = load_module("ingest_rss_state", "ingest-rss.py")
rss_common = load_module("rss_common_state", "rss_common.py")


class TestRssState(unittest.TestCase):
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

    def test_seen_json_no_duplicate_item_ids(self) -> None:
        old_argv = sys.argv
        sys.argv = ["ingest-rss.py", "--root", str(self.tmp), "--yes"]
        try:
            ingest_rss.main()
            ingest_rss.main()
        finally:
            sys.argv = old_argv

        seen_path = self.tmp / rss_common.SEEN_FILE
        self.assertTrue(seen_path.is_file())
        data = json.loads(seen_path.read_text(encoding="utf-8"))
        ids = list(data.keys())
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
