"""Tests for the deterministic align-cite core (PR-4, Decision A keystone)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tests.workspace._load import SRC  # noqa: F401  (ensures src/ is on sys.path)

from second_brain.validation import align_cite as ac


SOURCE_TEXT = """---
title: Using server-side encryption
type: concept
domain: vendor:aws
---

Amazon S3 applies AES-256 encryption with keys managed by Amazon S3.
New object uploads are encrypted by default at no additional charge.
"""


def write_artifact(root: Path, *, sources, domain="vendor:aws", body="") -> Path:
    art_dir = root / "wiki" / "workspace-projects" / "demo" / "01-vp-brief"
    art_dir.mkdir(parents=True, exist_ok=True)
    src_lines = "\n".join(f'  - "{s}"' for s in sources)
    art = art_dir / "product-brief.md"
    art.write_text(
        f"---\n"
        f"title: Demo brief\n"
        f"type: project-artifact\n"
        f"project: demo\n"
        f"status: review\n"
        f"domain: {domain}\n"
        f"sources:\n{src_lines}\n"
        f"---\n\n{body}\n",
        encoding="utf-8",
    )
    return art


def seed_vendor_source(root: Path) -> str:
    rel = "raw/workspace-external/aws/s3-sse/using-server-side-encryption.md"
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(SOURCE_TEXT, encoding="utf-8")
    return rel


class TestExtractQuotedSpans(unittest.TestCase):
    def test_blockquote_captured(self) -> None:
        spans = ac.extract_quoted_spans("> this is a quoted line from the source doc\n")
        self.assertEqual(len(spans), 1)

    def test_short_inline_quote_ignored(self) -> None:
        self.assertEqual(ac.extract_quoted_spans('The "thinking" mode is set.'), [])

    def test_long_inline_quote_captured(self) -> None:
        spans = ac.extract_quoted_spans('He said "encrypted by default at no additional charge today".')
        self.assertEqual(len(spans), 1)


class TestCheckArtifact(unittest.TestCase):
    def test_valid_artifact_passes(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            rel = seed_vendor_source(root)
            art = write_artifact(
                root,
                sources=[rel],
                body="> New object uploads are encrypted by default at no additional charge.",
            )
            res = ac.check_artifact(root, art)
            self.assertFalse(res.failed, [r.__dict__ for r in res.rows if r.verdict == "FAIL"])

    def test_fabricated_source_path_fails(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            art = write_artifact(root, sources=["raw/workspace-external/aws/ghost/none.md"], body="x")
            res = ac.check_artifact(root, art)
            self.assertTrue(res.failed)
            self.assertTrue(any(r.check == "source-exists" and r.verdict == "FAIL" for r in res.rows))

    def test_fabricated_quote_fails(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            rel = seed_vendor_source(root)
            art = write_artifact(
                root,
                sources=[rel],
                body="> S3 charges a premium fee for every encrypted object written.",
            )
            res = ac.check_artifact(root, art)
            self.assertTrue(res.failed)
            self.assertTrue(any(r.check == "quote-grounded" and r.verdict == "FAIL" for r in res.rows))

    def test_vendor_domain_without_vendor_source_fails(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            # Internal source only, but domain claims vendor:aws.
            internal = root / "wiki" / "workspace-standards" / "sec.md"
            internal.parent.mkdir(parents=True, exist_ok=True)
            internal.write_text("---\ntitle: Sec\ndomain: internal\n---\nbody\n", encoding="utf-8")
            art = write_artifact(root, sources=["wiki/workspace-standards/sec.md"], body="text")
            res = ac.check_artifact(root, art)
            self.assertTrue(any(r.check == "vendor-grounded" and r.verdict == "FAIL" for r in res.rows))


class TestRunAndReport(unittest.TestCase):
    def test_run_passes_and_writes_report(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            rel = seed_vendor_source(root)
            write_artifact(root, sources=[rel], body="Plain prose, no quotes.")
            code, report, results = ac.run(root, "demo", date="2026-06-11")
            self.assertEqual(code, 0)
            self.assertTrue(report.exists())
            self.assertIn("Overall verdict: **PASS**", report.read_text(encoding="utf-8"))

    def test_run_fails_nonzero_on_bad_cite(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_artifact(root, sources=["raw/workspace-external/aws/ghost/none.md"], body="x")
            code, report, results = ac.run(root, "demo", date="2026-06-11")
            self.assertEqual(code, 1)
            self.assertIn("Overall verdict: **FAIL**", report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
