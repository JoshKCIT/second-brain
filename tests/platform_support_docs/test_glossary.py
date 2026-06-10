"""Glossary term count tests."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_glossary", "support_doc_common.py")


class TestGlossary(unittest.TestCase):
    def test_glossary_term_count(self) -> None:
        path = common.support_doc_root(REPO_ROOT) / "operator-guide" / "glossary.md"
        self.assertTrue(path.is_file())
        body = common.extract_body_for_depth(path.read_text(encoding="utf-8"))
        terms = common.count_glossary_terms(body)
        self.assertGreaterEqual(terms, common.GLOSSARY_MIN_TERMS, f"only {terms} terms")


if __name__ == "__main__":
    unittest.main()
