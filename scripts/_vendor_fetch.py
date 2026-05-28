"""Shared vendor doc fetch helpers (defuddle resolution on Windows)."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def defuddle_command() -> list[str]:
    """Return argv prefix to invoke defuddle."""
    for name in ("defuddle", "defuddle.cmd", "defuddle.exe"):
        path = shutil.which(name)
        if path:
            return [path]
    # npm global on Windows often exposes defuddle.ps1; npx is reliable cross-platform
    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if npx:
        return [npx, "defuddle"]
    return ["defuddle"]


def run_defuddle(url: str, out_path: Path) -> None:
    cmd = defuddle_command() + ["parse", url, "--md", "-o", str(out_path)]
    use_shell = sys.platform == "win32"
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=False,
        shell=use_shell,
    )
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "defuddle failed").strip())


def defuddle_available() -> tuple[bool, str]:
    cmd = defuddle_command()
    try:
        proc = subprocess.run(
            cmd + ["parse", "https://example.com", "--md"],
            capture_output=True,
            text=True,
            timeout=45,
            check=False,
            shell=sys.platform == "win32",
        )
    except FileNotFoundError:
        return False, "defuddle not found; run: npm install -g defuddle"
    except subprocess.TimeoutExpired:
        return False, "defuddle timed out"
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()[:200]
        return False, f"defuddle check failed: {err}"
    return True, f"defuddle CLI available ({cmd[0]})"
