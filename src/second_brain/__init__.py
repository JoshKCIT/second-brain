"""Second Brain — thin shared operation boundary.

This package is deliberately small. It exposes a stable verb surface (see
`second_brain.cli`) that every IDE (Claude Code, Cursor, VS Code, Cowork) and a
future voice client can call for the *deterministic, verifiable* half of the
system. Judgment-bearing work stays in the prompts under `.github/prompts/`.

Keep it thin: wrap existing scripts and the deterministic validators; do not add
a framework, plugin system, or config loader until a real project proves prompt
orchestration insufficient.
"""

__version__ = "0.1.0"
