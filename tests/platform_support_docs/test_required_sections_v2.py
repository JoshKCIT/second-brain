"""Required section tests for support documentation v2."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_sections", "support_doc_common.py")


class TestRequiredSectionsV2(unittest.TestCase):
    def test_all_registry_pages_have_sections(self) -> None:
        missing: list[str] = []
        for path in common.iter_support_pages(REPO_ROOT):
            name = path.name
            if name not in common.REQUIRED_SECTIONS:
                continue
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(REPO_ROOT).as_posix()
            for section in common.REQUIRED_SECTIONS[name]:
                if f"## {section}" not in text:
                    missing.append(f"{rel}: '{section}'")
        self.assertEqual(missing, [], "\n".join(missing))


if __name__ == "__main__":
    unittest.main()
