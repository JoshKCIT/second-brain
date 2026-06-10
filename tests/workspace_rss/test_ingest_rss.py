"""Unit tests for ingest-rss.py."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from tests.workspace_rss._load import REPO_ROOT, load_module

ingest_rss = load_module("ingest_rss", "ingest-rss.py")
rss_common = load_module("rss_common", "rss_common.py")


class TestIngestRss(unittest.TestCase):
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

    def test_ingest_writes_items_with_frontmatter(self) -> None:
        import sys

        argv = [
            "ingest-rss.py",
            "--root",
            str(self.tmp),
            "--yes",
        ]
        old_argv = sys.argv
        sys.argv = argv
        try:
            self.assertEqual(ingest_rss.main(), 0)
        finally:
            sys.argv = old_argv

        items = list((self.tmp / "raw" / "workspace-rss-feed" / "items").rglob("*.md"))
        self.assertGreaterEqual(len(items), 4)
        meta, body = rss_common.parse_item_file(items[0])
        self.assertIn("item_id", meta)
        self.assertIn("feed_slug", meta)
        self.assertEqual(meta.get("inbox_status"), "unprocessed")
        self.assertTrue(body.strip())

    def test_dedupe_second_run(self) -> None:
        import sys

        argv = ["ingest-rss.py", "--root", str(self.tmp), "--yes"]
        old_argv = sys.argv
        sys.argv = argv
        try:
            ingest_rss.main()
            first_count = len(list((self.tmp / "raw" / "workspace-rss-feed" / "items").rglob("*.md")))
            ingest_rss.main()
            second_count = len(list((self.tmp / "raw" / "workspace-rss-feed" / "items").rglob("*.md")))
        finally:
            sys.argv = old_argv
        self.assertEqual(first_count, second_count)

    def test_dry_run_no_writes(self) -> None:
        import sys

        argv = ["ingest-rss.py", "--root", str(self.tmp), "--yes", "--dry-run"]
        old_argv = sys.argv
        sys.argv = argv
        try:
            ingest_rss.main()
        finally:
            sys.argv = old_argv
        items_dir = self.tmp / "raw" / "workspace-rss-feed" / "items"
        if items_dir.exists():
            self.assertEqual(len(list(items_dir.rglob("*.md"))), 0)

    def test_max_items_cap(self) -> None:
        import sys

        argv = ["ingest-rss.py", "--root", str(self.tmp), "--yes", "--max-items", "1", "--feed", "signal-feed"]
        old_argv = sys.argv
        sys.argv = argv
        try:
            ingest_rss.main()
        finally:
            sys.argv = old_argv
        signal_items = list(
            (self.tmp / "raw" / "workspace-rss-feed" / "items").rglob("signal-feed/*.md")
        )
        self.assertEqual(len(signal_items), 1)

    def test_frontmatter_parses_titles_with_quotes(self) -> None:
        fm = rss_common.build_item_frontmatter(
            title='"Amazon Quick ARNs: Cross-account migration"',
            source_url="https://aws.amazon.com/blogs/machine-learning/example/",
            feed_slug="aws-ml-blog",
            item_id="abc123",
            published_at="2026-06-08T16:07:29Z",
            ingested_at="2026-06-10T22:00:00Z",
            domain="vendor:aws",
            authority="informational",
        )
        path = self.tmp / "quoted-title.md"
        path.write_text(fm + "Summary body.", encoding="utf-8")
        meta, body = rss_common.parse_item_file(path)
        self.assertEqual(meta["title"], '"Amazon Quick ARNs: Cross-account migration"')
        self.assertEqual(body.strip(), "Summary body.")


if __name__ == "__main__":
    unittest.main()
