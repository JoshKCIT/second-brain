#!/usr/bin/env python3
"""
Verify Second Brain workspace setup for Phase 1A (vendor bootstrap) or full mode (Atlassian).

Creates runtime directories, initializes wiki/index.md and wiki/log.md, checks config,
optional Atlassian connectivity, defuddle CLI, and unittest / platform-research lint.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


ROOT = Path(__file__).resolve().parent.parent

RUNTIME_DIRS = [
    "raw/workspace-confluence",
    "raw/workspace-jira",
    "raw/workspace-external",
    "raw/platform-transcripts",
    "wiki/workspace-standards",
    "wiki/workspace-recommendations",
    "wiki/workspace-informational",
    "wiki/workspace-concepts",
    "wiki/workspace-connections",
    "wiki/workspace-qa",
    "wiki/workspace-projects",
    "wiki/workspace-archives",
    "wiki/workspace-views",
    "wiki/platform-research",
    "wiki/platform-research/transcript-analyses",
    "confluence-review",
    "quarantine",
    "reports",
]

INDEX_TEMPLATE = """# Knowledge Base Index

## Active projects

_No active projects yet._

## Standards by team

_No compiled standards yet. Vendor caches live under `raw/workspace-external/`._

## Recent activity

_See [[log]] for chronological operations._

## All concepts

| Article | Authority | Domain | Sources | Updated |
|---|---|---|---|---|

## Cached vendor documentation

| Vendor | Topic | Path | Cached |
|---|---|---|---|

## All connections

| Article | Connects | Updated |
|---|---|---|

## Stale vendor docs

_Run `/workspace-revalidate-vendor-docs` to list stale caches._
"""

LOG_TEMPLATE = """# Build Log

## [{timestamp}] verify-setup | workspace initialized
- Directories created or verified
- Index and log initialized
- Phase: 1A vendor bootstrap (Atlassian optional)
"""


def load_yaml(path: Path) -> dict | None:
    if not path.is_file():
        return None
    if yaml is None:
        print(f"WARN: PyYAML not installed; cannot parse {path}")
        return None
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def ensure_dirs(root: Path) -> list[str]:
    created = []
    for rel in RUNTIME_DIRS:
        path = root / rel
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(rel)
        elif path.is_dir():
            gitkeep = path / ".gitkeep"
            if not any(path.iterdir()) and not gitkeep.exists():
                gitkeep.touch()
    return created


def init_wiki_files(root: Path) -> list[str]:
    from datetime import datetime, timezone

    initialized = []
    index_path = root / "wiki" / "index.md"
    log_path = root / "wiki" / "log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not index_path.is_file():
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(INDEX_TEMPLATE, encoding="utf-8")
        initialized.append("wiki/index.md")

    if not log_path.is_file():
        log_path.write_text(LOG_TEMPLATE.format(timestamp=ts), encoding="utf-8")
        initialized.append("wiki/log.md")

    return initialized


def check_config(root: Path) -> tuple[bool, str]:
    local = root / "config" / "second-brain.yml"
    example = root / "config" / "second-brain.example.yml"
    if local.is_file():
        cfg = load_yaml(local)
        if cfg is None:
            return True, "config/second-brain.yml present (not parsed)"
        atlassian = (cfg or {}).get("atlassian") or {}
        enabled = atlassian.get("enabled", False)
        vendors = ((cfg or {}).get("vendor_sources") or {}).get("enabled") or []
        return True, f"config/second-brain.yml OK (atlassian.enabled={enabled}, vendors={len(vendors)})"
    if example.is_file():
        return False, "Copy config/second-brain.example.yml to config/second-brain.yml"
    return False, "Missing config/second-brain.example.yml"


def check_defuddle() -> tuple[bool, str]:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _vendor_fetch import defuddle_available

    return defuddle_available()


def check_atlassian(root: Path) -> tuple[bool, str]:
    cfg = load_yaml(root / "config" / "second-brain.yml") or {}
    atlassian = cfg.get("atlassian") or {}
    if not atlassian.get("enabled", False):
        return True, "Atlassian skipped (atlassian.enabled=false)"

    env_path = root / ".env"
    if not env_path.is_file():
        return False, "atlassian.enabled=true but .env missing (copy from .env.example)"

    site = os.environ.get("ATLASSIAN_SITE_URL", "")
    email = os.environ.get("ATLASSIAN_EMAIL", "")
    token = os.environ.get("ATLASSIAN_API_TOKEN", "")
    if env_path.is_file():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip()
            if key == "ATLASSIAN_SITE_URL" and val:
                site = val
            elif key == "ATLASSIAN_EMAIL" and val:
                email = val
            elif key == "ATLASSIAN_API_TOKEN" and val:
                token = val

    if not all([site, email, token]):
        return False, "Atlassian enabled but ATLASSIAN_SITE_URL, ATLASSIAN_EMAIL, or ATLASSIAN_API_TOKEN empty in .env"

    try:
        import urllib.request
        import base64

        url = site.rstrip("/") + "/wiki/rest/api/space?limit=1"
        creds = base64.b64encode(f"{email}:{token}".encode()).decode()
        req = urllib.request.Request(url, headers={"Authorization": f"Basic {creds}"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            if 200 <= resp.status < 300:
                return True, f"Atlassian connectivity OK ({site})"
    except Exception as exc:
        return False, f"Atlassian connectivity failed: {exc}"

    return False, "Atlassian connectivity check failed"


def run_command(cmd: list[str], cwd: Path, label: str) -> tuple[bool, str]:
    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)
    except Exception as exc:
        return False, f"{label} failed to run: {exc}"
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()[:500]
        return False, f"{label} exited {proc.returncode}: {err}"
    return True, f"{label} passed"


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Second Brain setup")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--skip-tests", action="store_true", help="Skip unittest and platform lint")
    parser.add_argument("--skip-defuddle", action="store_true", help="Do not require defuddle")
    args = parser.parse_args()
    root = args.root.resolve()

    print(f"Second Brain verify-setup (root={root})\n")
    errors: list[str] = []
    warnings: list[str] = []

    created = ensure_dirs(root)
    if created:
        print(f"Created {len(created)} directories:")
        for d in created:
            print(f"  + {d}")
    else:
        print("Runtime directories: OK (already present)")

    init = init_wiki_files(root)
    if init:
        print(f"Initialized: {', '.join(init)}")
    else:
        print("wiki/index.md and wiki/log.md: OK (already present)")

    ok, msg = check_config(root)
    print(f"Config: {msg}")
    if not ok:
        errors.append(msg)

    if not args.skip_defuddle:
        ok, msg = check_defuddle()
        print(f"Defuddle: {msg}")
        if not ok:
            warnings.append(msg)
    else:
        print("Defuddle: skipped")

    ok, msg = check_atlassian(root)
    print(f"Atlassian: {msg}")
    if not ok:
        errors.append(msg)

    if not args.skip_tests:
        ok, msg = run_command(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            root,
            "unittest",
        )
        print(f"Tests: {msg}")
        if not ok:
            errors.append(msg)

        lint_script = root / "scripts" / "lint-platform-research.py"
        if lint_script.is_file():
            ok, msg = run_command(
                [sys.executable, str(lint_script), "--root", str(root)],
                root,
                "lint-platform-research",
            )
            print(f"Platform lint: {msg}")
            if not ok:
                warnings.append(msg)

    print()
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        print("\nNext: fix errors above, then run:")
        print("  python scripts/seed-vendor-docs.py")
        return 1

    print("SUCCESS: Second Brain workspace verified.")
    print("Phase 1A complete. See docs/phase-1a-exit-report.md")
    print("Next: Phase 2 (compile, Base views) or /workspace-start-project (Phase 3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
