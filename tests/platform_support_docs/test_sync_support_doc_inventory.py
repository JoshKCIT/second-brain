"""Tests for sync-support-doc-inventory.py."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from tests.platform_support_docs._load import REPO_ROOT, load_module

sync_inv = load_module("sync_support_doc_inventory", "sync-support-doc-inventory.py")


class TestSyncSupportDocInventory(unittest.TestCase):
    def test_live_repo_inventory(self) -> None:
        data = sync_inv.build_inventory(REPO_ROOT)
        self.assertGreaterEqual(data["prompt_inventory_count"], 30)
        self.assertGreaterEqual(data["script_inventory_count"], 10)
        stems = {p["stem"] for p in data["prompts"]}
        self.assertIn("workspace-compile", stems)
        self.assertIn("platform-sync-support-docs", stems)

    def test_write_creates_json(self) -> None:
        tmp = Path(tempfile.mkdtemp())
        try:
            shutil.copytree(REPO_ROOT / ".github", tmp / ".github")
            shutil.copytree(REPO_ROOT / "scripts", tmp / "scripts")
            (tmp / "templates" / "workspace").mkdir(parents=True)
            shutil.copy(
                REPO_ROOT / "templates" / "workspace" / "routing-map.md",
                tmp / "templates" / "workspace" / "routing-map.md",
            )
            (tmp / "docs" / "platform-decision-records").mkdir(parents=True)
            old_argv = sys.argv
            sys.argv = ["sync-support-doc-inventory.py", "--root", str(tmp), "--write"]
            try:
                sync_inv.main()
            finally:
                sys.argv = old_argv
            out = tmp / "docs/platform-support-documentation/.inventory/inventory.json"
            self.assertTrue(out.is_file())
            data = json.loads(out.read_text(encoding="utf-8"))
            self.assertIn("inventory_hash", data)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_hash_stable(self) -> None:
        a = sync_inv.build_inventory(REPO_ROOT)
        b = sync_inv.build_inventory(REPO_ROOT)
        self.assertEqual(a["inventory_hash"], b["inventory_hash"])


if __name__ == "__main__":
    unittest.main()
