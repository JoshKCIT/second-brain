"""Unit tests for rss_common helpers."""

from __future__ import annotations

import unittest

from tests.workspace_rss._load import load_module

rss_common = load_module("rss_common_unit", "rss_common.py")


class TestRssCommonHelpers(unittest.TestCase):
    def test_summary_excerpt_truncates(self) -> None:
        body = "word " * 100
        excerpt = rss_common.summary_excerpt(body, max_len=50)
        self.assertLessEqual(len(excerpt), 50)
        self.assertTrue(excerpt.endswith("…"))

    def test_review_flags_fixture_url(self) -> None:
        flags = rss_common.review_flags("https://example.com/post", "summary")
        self.assertIn("fixture_url", flags)


if __name__ == "__main__":
    unittest.main()
