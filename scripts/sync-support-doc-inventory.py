#!/usr/bin/env python3
"""
Build docs/platform-support-documentation/.inventory/inventory.json from repo sources.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

from support_doc_common import (  # noqa: E402
    INVENTORY_REL,
    inventory_hash,
    parse_frontmatter,
)

PROMPT_GLOB = ".github/prompts/**/*.prompt.md"
ROUTING_INVOKE_RE = re.compile(r"`([a-z0-9-]+)`")


def scan_prompts(root: Path) -> list[dict[str, Any]]:
    prompts: list[dict[str, Any]] = []
    for path in sorted(root.glob(PROMPT_GLOB)):
        if not path.is_file():
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        rel = path.relative_to(root).as_posix()
        stem = path.stem.replace(".prompt", "")
        if path.parent.name == "platform-research-review":
            stem = f"platform-research-review/{path.stem.replace('.prompt', '')}"
        prompts.append(
            {
                "stem": stem,
                "path": rel,
                "lane": meta.get("lane", ""),
                "description": meta.get("description", ""),
            }
        )
    return prompts


def scan_scripts(root: Path) -> list[dict[str, Any]]:
    scripts: list[dict[str, Any]] = []
    scripts_dir = root / "scripts"
    for path in sorted(scripts_dir.glob("*.py")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        doc = ""
        if text.startswith('"""'):
            end = text.find('"""', 3)
            if end > 0:
                doc = text[3:end].strip().splitlines()[0]
        scripts.append({"name": path.name, "path": path.relative_to(root).as_posix(), "summary": doc})
    return scripts


def scan_lifecycles(root: Path) -> list[dict[str, Any]]:
    templates = root / "templates" / "workspace"
    items: list[dict[str, Any]] = []
    for path in sorted(templates.glob("*-lifecycle.md")):
        items.append({"name": path.name, "path": path.relative_to(root).as_posix(), "type": "lifecycle"})
    profiles = templates / "chain-profiles"
    if profiles.is_dir():
        for path in sorted(profiles.glob("*.md")):
            items.append({"name": path.name, "path": path.relative_to(root).as_posix(), "type": "chain-profile"})
    return items


def scan_adrs(root: Path) -> dict[str, list[dict[str, str]]]:
    adr_dir = root / "docs" / "platform-decision-records"
    accepted: list[dict[str, str]] = []
    draft: list[dict[str, str]] = []
    for path in sorted(adr_dir.glob("*.md")):
        if path.name == "README.md":
            continue
        entry = {"name": path.name, "path": path.relative_to(root).as_posix()}
        if path.name.startswith("DRAFT-"):
            draft.append(entry)
        else:
            accepted.append(entry)
    return {"accepted": accepted, "draft": draft}


def scan_routing(root: Path) -> list[str]:
    path = root / "templates" / "workspace" / "routing-map.md"
    if not path.is_file():
        return []
    invokes: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if "|" not in line or line.strip().startswith("|--"):
            continue
        for match in ROUTING_INVOKE_RE.finditer(line):
            stem = match.group(1)
            if stem not in ("workspace", "platform", "second-brain"):
                invokes.add(stem)
    return sorted(invokes)


def build_inventory(root: Path) -> dict[str, Any]:
    prompts = scan_prompts(root)
    scripts = scan_scripts(root)
    lifecycles = scan_lifecycles(root)
    adrs = scan_adrs(root)
    routing = scan_routing(root)
    prompt_stems = {p["stem"] for p in prompts}
    routing_orphans = [s for s in routing if s not in prompt_stems and not s.endswith("-agent")]
    data = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "prompts": prompts,
        "scripts": scripts,
        "lifecycles": lifecycles,
        "adrs": adrs,
        "routing_invokes": routing,
        "routing_orphans": routing_orphans,
        "prompt_inventory_count": len(prompts),
        "script_inventory_count": len(scripts),
    }
    data["inventory_hash"] = inventory_hash(data)
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync platform support doc inventory")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if committed inventory_hash differs from current repo scan",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print inventory JSON to stdout")
    args = parser.parse_args()

    root = args.root.resolve()
    data = build_inventory(root)

    if args.json:
        print(json.dumps(data, indent=2))
        return 0

    print(
        f"Inventory: prompts={data['prompt_inventory_count']} "
        f"scripts={data['script_inventory_count']} "
        f"lifecycles={len(data['lifecycles'])} "
        f"routing_orphans={len(data['routing_orphans'])}"
    )

    if args.check:
        out = root / INVENTORY_REL
        if not out.is_file():
            print(f"ERROR: missing {out.relative_to(root)}", file=sys.stderr)
            return 1
        committed = json.loads(out.read_text(encoding="utf-8"))
        if data["inventory_hash"] != committed.get("inventory_hash"):
            print(
                "ERROR: inventory.json is stale. Run: python scripts/sync-support-doc-inventory.py --write",
                file=sys.stderr,
            )
            return 1
        print("Inventory hash matches committed inventory.json")
        return 0

    if args.dry_run:
        return 0

    if args.write:
        out = root / INVENTORY_REL
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Wrote {out.relative_to(root)}")
    else:
        print("Use --write to persist inventory.json")

    return 0


if __name__ == "__main__":
    sys.exit(main())
