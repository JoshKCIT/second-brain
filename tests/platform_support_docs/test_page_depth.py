"""Page depth floor tests for support documentation v2."""

from __future__ import annotations

import unittest
from pathlib import Path

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_depth", "support_doc_common.py")


class TestPageDepth(unittest.TestCase):
    def test_strict_pages_meet_depth_floors(self) -> None:
        failures: list[str] = []
        for path in common.iter_support_pages(REPO_ROOT):
            rule = common.depth_rule_for_filename(path.name)
            if rule is None:
                continue
            min_words, extra = rule
            text = path.read_text(encoding="utf-8")
            body = common.extract_body_for_depth(text)
            words = common.count_words(body)
            rel = path.relative_to(REPO_ROOT).as_posix()
            if words < min_words:
                failures.append(f"{rel}: {words} < {min_words}")
            if extra == "flow_diagram" and not common.has_flow_diagram(body):
                failures.append(f"{rel}: missing flow diagram")
            if extra == "glossary":
                terms = common.count_glossary_terms(body)
                if terms < common.GLOSSARY_MIN_TERMS:
                    failures.append(f"{rel}: {terms} glossary terms")
            if extra == "trouble_rows":
                rows = common.count_table_rows(body)
                if rows < common.TROUBLESHOOTING_MIN_ROWS:
                    failures.append(f"{rel}: {rows} trouble rows")
        self.assertEqual(failures, [], "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
