"""Tests for the deterministic closure check (PR-5).

Locks the body-wikilink-at-review/published rule (AGENTS.md §498-507, §720)
that blocks publish. Draft allows body wikilinks; See Also and frontmatter are
always allowed.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tests.workspace._load import load_module

lint = load_module("lint_workspace_closure", "lint-workspace.py")


def write_artifact(root: Path, *, status: str, body: str) -> Path:
    art_dir = root / "wiki" / "workspace-projects" / "demo" / "02-pm-prd"
    art_dir.mkdir(parents=True, exist_ok=True)
    art = art_dir / "product-requirements.md"
    art.write_text(
        f"---\n"
        f"title: Demo PRD\n"
        f"type: project-artifact\n"
        f"project: demo\n"
        f"status: {status}\n"
        f"sources: []\n"
        f"created: 2026-06-11\n"
        f"updated: 2026-06-11\n"
        f"---\n\n{body}\n",
        encoding="utf-8",
    )
    return art


def closure(root: Path) -> list[str]:
    articles = lint.collect_wiki_articles(root, None)
    return lint.lint_body_wikilink_closure(root, articles)


class TestBodyWikilinkClosure(unittest.TestCase):
    def test_published_body_wikilink_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_artifact(root, status="published", body="See [[other-concept]] for detail.")
            findings = closure(root)
            self.assertEqual(len(findings), 1, findings)
            self.assertIn("other-concept", findings[0])

    def test_review_body_wikilink_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_artifact(root, status="review", body="Body links to [[a-thing]].")
            self.assertEqual(len(closure(root)), 1)

    def test_draft_body_wikilink_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_artifact(root, status="draft", body="Draft may link [[a-thing]] freely.")
            self.assertEqual(closure(root), [])

    def test_published_wikilink_in_see_also_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            body = "Clean body prose.\n\n## See Also\n\n- [[related-concept]]\n"
            write_artifact(root, status="published", body=body)
            self.assertEqual(closure(root), [])

    def test_published_clean_body_passes(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            body = "Uses an external link [AWS](https://aws.amazon.com) only.\n\n## See Also\n\n- [docs](https://x)\n"
            write_artifact(root, status="published", body=body)
            self.assertEqual(closure(root), [])

    def test_closure_registered_as_error_severity(self) -> None:
        self.assertEqual(lint.severity_map().get("body_wikilink_closure"), "error")


if __name__ == "__main__":
    unittest.main()
