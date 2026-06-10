"""Unit tests for triage-rss.py."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from tests.workspace_rss._load import REPO_ROOT, load_module

ingest_rss = load_module("ingest_rss_triage", "ingest-rss.py")
triage_rss = load_module("triage_rss", "triage-rss.py")
rss_common = load_module("rss_common_triage", "rss_common.py")


def _setup_tmp() -> Path:
    tmp = Path(tempfile.mkdtemp())
    shutil.copytree(
        REPO_ROOT / "tests" / "fixtures" / "workspace-rss",
        tmp / "tests" / "fixtures" / "workspace-rss",
    )
    (tmp / "config").mkdir(parents=True)
    shutil.copy(
        tmp / "tests" / "fixtures" / "workspace-rss" / "rss-feeds.yml",
        tmp / "config" / "rss-feeds.yml",
    )
    old_argv = sys.argv
    sys.argv = ["ingest-rss.py", "--root", str(tmp), "--yes"]
    try:
        ingest_rss.main()
    finally:
        sys.argv = old_argv
    return tmp


class TestTriageRss(unittest.TestCase):
    def tearDown(self) -> None:
        if hasattr(self, "tmp"):
            shutil.rmtree(self.tmp, ignore_errors=True)

    def test_signal_items_queue_noise_auto_skip(self) -> None:
        self.tmp = _setup_tmp()
        old_argv = sys.argv
        sys.argv = ["triage-rss.py", "--root", str(self.tmp), "--yes"]
        try:
            triage_rss.main()
        finally:
            sys.argv = old_argv

        statuses: dict[str, int] = {}
        for path in rss_common.iter_item_files(self.tmp):
            meta, _ = rss_common.parse_item_file(path)
            s = str(meta.get("triage_status", ""))
            statuses[s] = statuses.get(s, 0) + 1

        self.assertGreater(statuses.get("auto_skip", 0), 0)
        queued = sum(statuses.get(s, 0) for s in ("suggested", "high_signal", "borderline"))
        self.assertGreater(queued, 0)

    def test_max_queue_size_respected(self) -> None:
        self.tmp = _setup_tmp()
        cfg_path = self.tmp / "config" / "rss-feeds.yml"
        text = cfg_path.read_text(encoding="utf-8")
        text = text.replace("max_queue_size: 30", "max_queue_size: 1")
        cfg_path.write_text(text, encoding="utf-8")

        old_argv = sys.argv
        sys.argv = ["triage-rss.py", "--root", str(self.tmp), "--yes"]
        try:
            triage_rss.main()
        finally:
            sys.argv = old_argv

        queued = 0
        for path in rss_common.iter_item_files(self.tmp):
            meta, _ = rss_common.parse_item_file(path)
            if meta.get("triage_status") in ("suggested", "high_signal", "borderline"):
                queued += 1
        self.assertLessEqual(queued, 1)


if __name__ == "__main__":
    unittest.main()
