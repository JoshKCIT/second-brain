"""Manifest parity tests."""

from __future__ import annotations

import unittest

from tests.platform_support_docs._load import REPO_ROOT, load_module

common = load_module("support_doc_common_manifest", "support_doc_common.py")


class TestManifestParity(unittest.TestCase):
    def test_manifest_pages_exist(self) -> None:
        manifest = common.load_manifest(REPO_ROOT)
        pages = manifest.get("pages_written") or []
        self.assertGreaterEqual(len(pages), common.MANIFEST_MIN_PAGES)
        missing = []
        for rel in pages:
            p = REPO_ROOT / str(rel).replace("\\", "/")
            if not p.is_file():
                missing.append(str(rel))
        self.assertEqual(missing, [], f"missing: {missing}")

    def test_strict_pages_in_manifest(self) -> None:
        manifest = common.load_manifest(REPO_ROOT)
        written = {str(p).replace("\\", "/") for p in (manifest.get("pages_written") or [])}
        missing = []
        for rel in common.STRICT_PAGES:
            full = f"docs/platform-support-documentation/{rel}"
            if full not in written:
                missing.append(full)
        self.assertEqual(missing, [], f"not in manifest: {missing}")


if __name__ == "__main__":
    unittest.main()
