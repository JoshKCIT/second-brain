from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

REPO_ROOT = Path(__file__).resolve().parents[2]
SYNC_SCRIPT = REPO_ROOT / "scripts" / "sync-transcript-register.py"


def load_sync_module():
    spec = importlib.util.spec_from_file_location("sync_transcript_register", SYNC_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load sync-transcript-register.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sync = load_sync_module()


class SyncTranscriptRegisterTests(unittest.TestCase):
    def test_queued_when_raw_only(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw/platform-transcripts"
            raw.mkdir(parents=True)
            (raw / "new-idea.txt").write_text("speaker: hello\n", encoding="utf-8")
            content, warnings = sync.build_register(root)
            self.assertIn("status: queued", content)
            self.assertIn("new-idea.txt", content)
            self.assertEqual(warnings, [])

    def test_reviewed_when_claims_and_impact_exist(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw/platform-transcripts"
            raw.mkdir(parents=True)
            (raw / "demo.txt").write_text("content", encoding="utf-8")

            analyses = root / "wiki/platform-research/transcript-analyses"
            analyses.mkdir(parents=True)
            (analyses / "demo-topic-claims.md").write_text(
                "# Claims Analysis: demo-topic\n\n## Source\n\n"
                "- Transcript: `raw/platform-transcripts/demo.txt`\n",
                encoding="utf-8",
            )

            reports = root / "reports/platform-research-review"
            reports.mkdir(parents=True)
            (reports / "demo-topic-impact-report.md").write_text(
                "# Research Impact Report: demo-topic\n\n## Source\n\n"
                "- Transcript: `raw/platform-transcripts/demo.txt`\n",
                encoding="utf-8",
            )

            content, _ = sync.build_register(root)
            self.assertIn("status: reviewed", content)
            self.assertIn("demo-topic-claims.md", content)
            self.assertIn("demo-topic-impact-report.md", content)

    def test_partial_when_claims_only(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw/platform-transcripts"
            raw.mkdir(parents=True)
            (raw / "half.txt").write_text("x", encoding="utf-8")

            analyses = root / "wiki/platform-research/transcript-analyses"
            analyses.mkdir(parents=True)
            (analyses / "half-done-claims.md").write_text(
                "## Source\n\n- Transcript: `raw/platform-transcripts/half.txt`\n",
                encoding="utf-8",
            )

            content, _ = sync.build_register(root)
            self.assertIn("status: partial", content)

    def test_preserves_skipped_status(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            reg = root / "wiki/platform-research"
            reg.mkdir(parents=True)
            (reg / "transcript-register.md").write_text(
                """# Platform Transcript Register

## Records

```yaml
slug: noise
status: skipped
source: raw/platform-transcripts/noise.txt
title: "Noise"
imported: 2026-01-01
reviewed: ""
claims_analysis: ""
impact_report: ""
notes: "Off-topic"
```
""",
                encoding="utf-8",
            )
            raw = root / "raw/platform-transcripts"
            raw.mkdir(parents=True)
            (raw / "noise.txt").write_text("x", encoding="utf-8")

            content, _ = sync.build_register(root)
            self.assertIn("status: skipped", content)
            self.assertIn("Off-topic", content)


if __name__ == "__main__":
    unittest.main()
