"""Phase/status consistency across canonical docs (Phase 0 gate)."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class TestPhaseStatusConsistency(unittest.TestCase):
    def test_roadmap_shows_phase3_active_and_early_phases_complete(self) -> None:
        text = _read("docs/product/roadmap.md")
        self.assertIn("Phase 3", text)
        self.assertRegex(text, r"Phase 3.*ACTIVE|Current phase.*Phase 3", re.IGNORECASE | re.DOTALL)
        self.assertRegex(text, r"Phase 1A.*COMPLETE", re.IGNORECASE | re.DOTALL)
        self.assertRegex(text, r"Phase 2.*COMPLETE", re.IGNORECASE | re.DOTALL)

    def test_phase2_plan_not_in_progress(self) -> None:
        plan_path = ROOT / "docs" / "build-history" / "phase-2-plan.md"
        text = plan_path.read_text(encoding="utf-8")
        self.assertNotIn("In progress", text)
        self.assertIn("Complete", text)

    def test_no_stale_phase1_active_in_adoption_checklist(self) -> None:
        paths = [
            ROOT / "docs" / "adoption-checklist.md",
            ROOT
            / "docs"
            / "platform-support-documentation"
            / "user-guide"
            / "adoption-checklist.md",
        ]
        text = ""
        for p in paths:
            if p.exists():
                text = p.read_text(encoding="utf-8")
                break
        self.assertTrue(text, "adoption checklist not found")
        self.assertNotRegex(text, r"Phase 1 active", re.IGNORECASE)

    def test_prd_no_phase1a_active(self) -> None:
        text = _read("PRD.md")
        self.assertNotRegex(text, r"Phase 1A.*ACTIVE", re.IGNORECASE)
        self.assertRegex(text, r"Phase 3.*ACTIVE", re.IGNORECASE | re.DOTALL)

    def test_forbidden_stale_strings_absent_in_docs(self) -> None:
        forbidden = [
            re.compile(r"Phase 1 active", re.IGNORECASE),
            re.compile(r"Phase 1A.*ACTIVE", re.IGNORECASE),
            re.compile(r"\*\*Status:\*\* In progress"),
        ]
        docs_dir = ROOT / "docs"
        for path in docs_dir.rglob("*.md"):
            if "build-history" in path.parts:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel == "docs/progress-log.md":
                continue
            text = path.read_text(encoding="utf-8")
            for pat in forbidden:
                self.assertIsNone(
                    pat.search(text),
                    f"{rel} contains stale pattern {pat.pattern!r}",
                )


if __name__ == "__main__":
    unittest.main()
