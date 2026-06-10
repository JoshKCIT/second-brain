"""Feature coverage matrix vs feature-catalog.md."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

support_common = load_module("support_doc_common_test", "support_doc_common.py")
FEATURE_COVERAGE_KEYWORDS = support_common.FEATURE_COVERAGE_KEYWORDS
support_doc_root = support_common.support_doc_root


class TestFeatureCoverageMatrix(unittest.TestCase):
    def test_catalog_covers_matrix(self) -> None:
        catalog = support_doc_root(REPO_ROOT) / "operator-guide" / "feature-catalog.md"
        self.assertTrue(catalog.is_file())
        text = catalog.read_text(encoding="utf-8").lower()
        missing: list[str] = []
        for category, keywords in FEATURE_COVERAGE_KEYWORDS.items():
            for kw in keywords:
                if kw.lower() not in text:
                    missing.append(f"{category}:{kw}")
        self.assertEqual(missing, [], f"missing keywords: {missing}")


class TestLiveRepoRegression(unittest.TestCase):
    def test_readme_links_support_docs(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("platform-support-documentation", readme)

    def test_no_stale_paths_in_support_docs(self) -> None:
        base = support_doc_root(REPO_ROOT)
        for path in base.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("docs/PRD.md", text, path.as_posix())


if __name__ == "__main__":
    unittest.main()
