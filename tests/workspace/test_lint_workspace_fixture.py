"""Fixture-level checks for lint-workspace.

These lock the deterministic link checker and the report renderer (the PR-2
chr(10) fix). The pair test_clean_fixture / test_planted_broken_link is the
"green on fixture, red on planted error" acceptance for the workspace CI job.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tests.workspace._load import load_module

lint = load_module("lint_workspace_unit", "lint-workspace.py")


class TestWikilinkResolution(unittest.TestCase):
    def _wiki_root(self, tmp: Path) -> Path:
        wiki = tmp / "wiki"
        wiki.mkdir(parents=True)
        return wiki

    def test_clean_fixture_resolves(self) -> None:
        """A wikilink to an existing article resolves (green)."""
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            wiki = self._wiki_root(root)
            (wiki / "target.md").write_text("# Target\n", encoding="utf-8")
            source = wiki / "source.md"
            source.write_text("Link to [[target]]\n", encoding="utf-8")

            resolved = lint.resolve_wikilink(root, source, "target")
            self.assertIsNotNone(resolved)
            self.assertEqual(resolved.name, "target.md")

    def test_planted_broken_link_is_caught(self) -> None:
        """A wikilink to a missing article does not resolve (planted error)."""
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            wiki = self._wiki_root(root)
            source = wiki / "source.md"
            source.write_text("Link to [[does-not-exist]]\n", encoding="utf-8")

            resolved = lint.resolve_wikilink(root, source, "does-not-exist")
            self.assertIsNone(resolved)


class TestReportRenderer(unittest.TestCase):
    def test_empty_sections_render_none_placeholder(self) -> None:
        """Regression lock for PR-2: empty sections render `_None._` and the
        report builds without a backslash-in-f-string-brace SyntaxError."""
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            # All-empty findings exercise the `_None._` branch in every section.
            findings = {"broken_links": [], "orphan_pages": []}
            report_path = lint.write_report(root, findings)
            body = report_path.read_text(encoding="utf-8")
            self.assertIn("_None._", body)
            self.assertIn("## Errors", body)


if __name__ == "__main__":
    unittest.main()
