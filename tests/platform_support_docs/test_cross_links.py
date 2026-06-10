"""Hub and support-doc cross-link tests."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_links", "support_doc_common.py")


class TestCrossLinks(unittest.TestCase):
    def test_hub_links_to_workflow_pages(self) -> None:
        readme = common.support_doc_root(REPO_ROOT) / "README.md"
        text = readme.read_text(encoding="utf-8").lower()
        missing = [link for link in common.HUB_WORKFLOW_LINKS if link.lower() not in text]
        self.assertEqual(missing, [], f"hub missing: {missing}")

    def test_support_tree_links_resolve(self) -> None:
        broken: list[str] = []
        for path in common.iter_support_pages(REPO_ROOT):
            rel = path.relative_to(REPO_ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            base = path.parent
            for match in common.MARKDOWN_LINK_RE.finditer(text):
                target = match.group(1).split("#")[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not common.resolve_repo_path(REPO_ROOT, target, base=base):
                    broken.append(f"{rel} -> {target}")
        self.assertEqual(broken, [], "\n".join(broken[:20]))


if __name__ == "__main__":
    unittest.main()
