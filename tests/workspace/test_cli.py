"""Tests for the thin `second-brain` CLI boundary (Decision C)."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from tests.workspace._load import SRC  # noqa: F401  (ensures src/ is on sys.path)

from second_brain import cli


class TestCliVerbs(unittest.TestCase):
    def test_core_verbs_registered(self) -> None:
        registered = cli.verbs()
        self.assertIn("verify-setup", registered)
        self.assertIn("lint-workspace", registered)

    def test_script_verbs_resolve_to_real_files(self) -> None:
        for verb, filename in cli.SCRIPT_VERBS.items():
            target = cli.SCRIPTS_DIR / filename
            self.assertTrue(target.is_file(), f"{verb} -> missing {target}")

    def test_list_returns_zero_and_prints_verbs(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            rc = cli.main(["list"])
        self.assertEqual(rc, 0)
        self.assertIn("lint-workspace", out.getvalue())

    def test_no_verb_lists(self) -> None:
        out = io.StringIO()
        with redirect_stdout(out):
            rc = cli.main([])
        self.assertEqual(rc, 0)

    def test_unknown_verb_is_nonzero(self) -> None:
        err = io.StringIO()
        with redirect_stderr(err):
            rc = cli.main(["no-such-verb"])
        self.assertEqual(rc, 2)
        self.assertIn("unknown verb", err.getvalue())


if __name__ == "__main__":
    unittest.main()
