"""Workflow page structure tests."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_workflow", "support_doc_common.py")


class TestWorkflowPages(unittest.TestCase):
    def test_workflow_pages_have_example_and_approval(self) -> None:
        base = common.support_doc_root(REPO_ROOT) / "user-guide"
        failures: list[str] = []
        for path in sorted(base.glob("workflow-*.md")):
            text = path.read_text(encoding="utf-8").lower()
            rel = path.relative_to(REPO_ROOT).as_posix()
            if "worked example" not in text:
                failures.append(f"{rel}: no worked example")
            if "approval checkpoint" not in text and "approval gate" not in text:
                failures.append(f"{rel}: no approval section")
        self.assertEqual(failures, [], "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
