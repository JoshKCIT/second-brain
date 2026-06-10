"""Manifest schema tests."""

from __future__ import annotations

import re
import unittest

try:
    import yaml
except ImportError:
    yaml = None

from tests.platform_support_docs._load import REPO_ROOT, load_module

support_common = load_module("support_doc_common_manifest", "support_doc_common.py")
MANIFEST_REQUIRED_KEYS = support_common.MANIFEST_REQUIRED_KEYS
load_manifest = support_common.load_manifest


class TestManifestSchema(unittest.TestCase):
    def test_manifest_has_required_keys(self) -> None:
        if yaml is None:
            self.skipTest("pyyaml not installed")
        manifest = load_manifest(REPO_ROOT)
        for key in MANIFEST_REQUIRED_KEYS:
            self.assertIn(key, manifest, key)
        if manifest.get("last_sync"):
            ts = str(manifest["last_sync"])
            self.assertRegex(ts, r"^\d{4}-\d{2}-\d{2}")


if __name__ == "__main__":
    unittest.main()
