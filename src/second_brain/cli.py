"""Thin `second-brain` CLI — the stable verb surface (Decision C).

This is a *boundary, not a framework*. Each verb either shells out to an existing
script in `scripts/` unchanged, or calls an in-package deterministic validator
(e.g. align-cite, added in PR-4). Judgment-bearing operations stay as prompts and
are intentionally NOT verbs here.

Rules for keeping it thin:
- Add a verb only when the operation is deterministic and verifiable.
- Pass every extra argument through to the underlying script/module verbatim.
- Do not add orchestration, plugins, or config loading.
"""

from __future__ import annotations

import argparse
import importlib
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"

# verb -> script filename under scripts/. Dispatched by shelling out to the
# script unchanged; all trailing argv is forwarded verbatim.
SCRIPT_VERBS: dict[str, str] = {
    "verify-setup": "verify-setup.py",
    "lint-workspace": "lint-workspace.py",
    "lint-support-docs": "lint-platform-support-docs.py",
    "lint-research": "lint-platform-research.py",
}

# verb -> "module:function" called in-process. The function takes a single
# argument (argv: list[str]) and returns an int exit code. These are the
# deterministic validators — the mechanical half of the hybrid align gates.
MODULE_VERBS: dict[str, str] = {
    "align-cite": "second_brain.validation.align_cite:cli",
}


def verbs() -> list[str]:
    """All registered verbs, sorted."""
    return sorted([*SCRIPT_VERBS, *MODULE_VERBS])


def _run_script(filename: str, argv: list[str]) -> int:
    script = SCRIPTS_DIR / filename
    if not script.is_file():
        print(f"second-brain: script not found: {script}", file=sys.stderr)
        return 2
    return subprocess.call([sys.executable, str(script), *argv])


def _run_module(target: str, argv: list[str]) -> int:
    mod_name, _, func_name = target.partition(":")
    module = importlib.import_module(mod_name)
    func = getattr(module, func_name)
    return int(func(argv))


def dispatch(verb: str, argv: list[str]) -> int:
    """Run a verb with the given pass-through argv. Returns its exit code."""
    if verb in MODULE_VERBS:
        return _run_module(MODULE_VERBS[verb], argv)
    if verb in SCRIPT_VERBS:
        return _run_script(SCRIPT_VERBS[verb], argv)
    print(
        f"second-brain: unknown verb '{verb}'. Try 'second-brain list'.",
        file=sys.stderr,
    )
    return 2


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = argparse.ArgumentParser(
        prog="second-brain",
        description="Thin verb surface over Second Brain's deterministic operations.",
    )
    parser.add_argument("verb", nargs="?", help="operation to run, or 'list'")
    parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="arguments forwarded verbatim to the verb",
    )
    ns = parser.parse_args(argv)

    if ns.verb in (None, "list"):
        print("second-brain verbs:")
        for v in verbs():
            print(f"  {v}")
        if not ns.verb:
            print("\nRun: second-brain <verb> [args...]")
        return 0
    return dispatch(ns.verb, ns.args)


if __name__ == "__main__":
    sys.exit(main())
