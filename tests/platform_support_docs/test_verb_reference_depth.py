"""Verb reference depth tests."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_verb", "support_doc_common.py")


class TestVerbReferenceDepth(unittest.TestCase):
    def test_top_verbs_documented(self) -> None:
        path = common.support_doc_root(REPO_ROOT) / "operator-guide" / "verb-reference.md"
        self.assertTrue(path.is_file())
        body = path.read_text(encoding="utf-8").lower()
        missing_verbs = [v for v in common.TOP_WORKSPACE_VERBS if v.lower() not in body]
        self.assertEqual(missing_verbs, [], f"missing verbs: {missing_verbs}")

    def test_per_verb_when_approve_outputs(self) -> None:
        path = common.support_doc_root(REPO_ROOT) / "operator-guide" / "verb-reference.md"
        body = path.read_text(encoding="utf-8")
        detail_idx = body.lower().find("## per-verb detail")
        self.assertGreater(detail_idx, 0, "missing Per-verb detail section")
        detail = body[detail_idx:]
        failures: list[str] = []
        for verb in common.TOP_WORKSPACE_VERBS:
            idx = detail.lower().find(verb.lower())
            if idx < 0:
                failures.append(f"{verb}: not in detail section")
                continue
            chunk = detail[idx : idx + 800].lower()
            for label in ("when", "approve", "output"):
                if label not in chunk:
                    failures.append(f"{verb}: missing {label} in chunk")
        self.assertEqual(failures, [], "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
