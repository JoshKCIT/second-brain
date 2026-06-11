"""Clean-template guarantees (PR-7, Decision B).

Locks two things:
1. A fresh clone has an empty workspace wiki — only .gitkeep is tracked under
   the per-user workspace wiki subtrees. (The acceptance: "fresh clone has empty
   wiki.")
2. The committed worked example under examples/ stays align-cite clean, so it
   remains a known-good reference fixture.
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

from tests.workspace._load import SRC  # noqa: F401  (ensures src/ is on sys.path)

from second_brain.validation import align_cite as ac

REPO_ROOT = Path(__file__).resolve().parents[2]

WORKSPACE_WIKI_SUBTREES = [
    "wiki/workspace-standards",
    "wiki/workspace-recommendations",
    "wiki/workspace-informational",
    "wiki/workspace-concepts",
    "wiki/workspace-connections",
    "wiki/workspace-qa",
    "wiki/workspace-projects",
    "wiki/workspace-archives",
]


class TestEmptyWorkspaceWiki(unittest.TestCase):
    def test_only_gitkeep_tracked_in_workspace_wiki(self) -> None:
        result = subprocess.run(
            ["git", "ls-files", *WORKSPACE_WIKI_SUBTREES],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        tracked = [line for line in result.stdout.splitlines() if line.strip()]
        leaked = [p for p in tracked if not p.endswith(".gitkeep")]
        self.assertEqual(
            leaked,
            [],
            f"Workspace wiki must be empty on a fresh clone; leaked: {leaked}",
        )


class TestExampleArtifactStaysClean(unittest.TestCase):
    def test_example_passes_align_cite(self) -> None:
        artifact = (
            "examples/workspace-projects/demo-s3-encryption/"
            "02-pm-prd/product-requirements.md"
        )
        self.assertTrue((REPO_ROOT / artifact).is_file(), "example artifact missing")
        code, report, results = ac.run(REPO_ROOT, artifact, date="2026-01-01")
        self.assertEqual(code, 0, "example artifact must pass deterministic align-cite")
        self.assertTrue(results and not results[0].failed)


if __name__ == "__main__":
    unittest.main()
