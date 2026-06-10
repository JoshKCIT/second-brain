"""Getting-started install doc tests (replaces setup-kit pointer checks)."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_setup", "support_doc_common.py")


class TestGettingStartedInstall(unittest.TestCase):
    def test_getting_started_is_canonical_install_doc(self) -> None:
        path = common.support_doc_root(REPO_ROOT) / "user-guide" / "getting-started.md"
        self.assertTrue(path.is_file(), "getting-started.md missing")
        text = path.read_text(encoding="utf-8")
        self.assertIn("status: published", text)
        for section in ("## Credentials", "## Verify setup", "## Onboarding"):
            self.assertIn(section, text, section)

    def test_no_setup_kit_file(self) -> None:
        self.assertFalse((REPO_ROOT / "docs/setup-kit.md").is_file(), "setup-kit.md should be removed")


if __name__ == "__main__":
    unittest.main()
