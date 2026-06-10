"""Shared helpers for platform support documentation inventory and lint."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

SUPPORT_DOC_REL = Path("docs/platform-support-documentation")
INVENTORY_REL = SUPPORT_DOC_REL / ".inventory" / "inventory.json"
MANIFEST_REL = SUPPORT_DOC_REL / "manifest.yml"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'_-]*")
GLOSSARY_TERM_RE = re.compile(r"^\|\s*`?([^`|]+?)`?\s*\|", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\|[^|]+\|", re.MULTILINE)

STALE_PATHS = [
    "docs/PRD.md",
    "docs/product-brief.md",
    "raw/transcripts/",
]

TRANSCRIPT_PATTERNS = [
    re.compile(r"claim_id:\s*RC-\d{4}-\d{2}-\d{2}-\d+", re.IGNORECASE),
    re.compile(r"source_transcript:\s*raw/platform-transcripts/", re.IGNORECASE),
]

MANIFEST_REQUIRED_KEYS = [
    "last_sync",
    "generator",
    "inventory_hash",
    "sources_consulted",
    "pages_written",
    "prompt_inventory_count",
    "script_inventory_count",
]

PAGE_FM_REQUIRED = ["title", "audience", "sources", "generated"]

GLOSSARY_MIN_TERMS = 20
MANIFEST_MIN_PAGES = 22
TROUBLESHOOTING_MIN_ROWS = 8

WORKFLOW_PAGE_GLOB = "workflow-*.md"

TOP_WORKSPACE_VERBS = [
    "second-brain",
    "workspace-ingest-confluence",
    "workspace-compile",
    "workspace-query",
    "workspace-start-project",
    "workspace-align-cite",
    "workspace-align-closure",
    "workspace-publish",
    "workspace-lint",
    "workspace-ingest-vendor-doc",
]

STRICT_PAGES: list[str] = [
    "user-guide/how-second-brain-works.md",
    "user-guide/getting-started.md",
    "user-guide/adoption-checklist.md",
    "user-guide/first-week-checklist.md",
    "user-guide/workflow-ingest.md",
    "user-guide/workflow-compile-and-query.md",
    "user-guide/workflow-project-chain.md",
    "user-guide/workflow-align-and-publish.md",
    "user-guide/everyday-workflows.md",
    "user-guide/troubleshooting.md",
    "operator-guide/concepts-for-operators.md",
    "operator-guide/using-your-ide.md",
    "operator-guide/ceo-approval-guide.md",
    "operator-guide/glossary.md",
    "operator-guide/lanes-and-approval-gates.md",
    "operator-guide/verb-reference.md",
    "operator-guide/feature-catalog.md",
    "operator-guide/platform-lane-overview.md",
    "engineer-reference/architecture-map.md",
    "engineer-reference/scripts-and-automation.md",
    "engineer-reference/adr-index.md",
    "engineer-reference/extending-the-platform.md",
]

REQUIRED_SECTIONS: dict[str, list[str]] = {
    "how-second-brain-works.md": [
        "Three layers",
        "Compiler analogy",
        "Lanes",
        "What agents do",
        "What you approve",
    ],
    "getting-started.md": [
        "Prerequisites",
        "Credentials",
        "Verify setup",
        "IDE open",
        "Onboarding",
        "First ingest",
        "First project",
        "Per-agent IDE",
        "See Also",
    ],
    "first-week-checklist.md": [
        "Day 0",
        "Days 1",
        "Days 3",
        "Ongoing rhythm",
        "Red flags",
    ],
    "adoption-checklist.md": [
        "Prerequisites checklist",
        "Setup checklist",
        "First project checklist",
        "Ongoing rhythm checklist",
        "Red flags",
    ],
    "workflow-ingest.md": [
        "Confluence flow",
        "Vendor flow",
        "Inbox staging",
        "RSS flow",
        "Approval gates",
        "Worked example",
        "Approval checkpoints",
    ],
    "workflow-compile-and-query.md": [
        "Compile batch",
        "RC-146 gate",
        "Query flow",
        "File-back",
        "Worked example",
        "Approval checkpoints",
    ],
    "workflow-project-chain.md": [
        "Stage table",
        "CEO gates",
        "Handoff locks",
        "Finalize and publish",
        "Worked example",
        "Approval checkpoints",
    ],
    "workflow-align-and-publish.md": [
        "Align cite",
        "Align closure",
        "Vendor truth",
        "Publish branches",
        "Worked example",
        "Approval checkpoints",
    ],
    "everyday-workflows.md": [
        "Quick reference table",
        "Workflow index",
    ],
    "troubleshooting.md": [
        "Common gotchas",
        "Auth issues",
        "Defuddle issues",
        "Lint remediation",
    ],
    "concepts-for-operators.md": [
        "Approval culture",
        "RC-146",
        "RC-151",
        "Citation and closure",
        "PH-006",
    ],
    "using-your-ide.md": [
        "Copilot",
        "Cursor",
        "Claude Code",
        "Windsurf",
        "Prompt discovery",
    ],
    "ceo-approval-guide.md": [
        "Compile batches",
        "Stage gates",
        "Publish gate",
        "Platform escalation",
    ],
    "glossary.md": [
        "Term table",
    ],
    "feature-catalog.md": ["Workspace lane", "Platform lane", "Scripts", "Config files"],
    "verb-reference.md": ["Workspace verbs", "Platform verbs", "Per-verb detail"],
    "lanes-and-approval-gates.md": ["Lane table", "RC-146", "RC-151", "CEO workflow"],
    "platform-lane-overview.md": ["When to escalate", "Transcript flow", "PIC pointer"],
    "architecture-map.md": ["Three layers", "Instruction stack", "See Also"],
}

# (filename or glob, min_words, extra_check)
PAGE_DEPTH_RULES: list[tuple[str, int, str | None]] = [
    ("how-second-brain-works.md", 800, "flow_diagram"),
    ("getting-started.md", 800, "flow_diagram"),
    ("workflow-*.md", 500, "workflow"),
    ("concepts-for-operators.md", 400, None),
    ("ceo-approval-guide.md", 400, None),
    ("verb-reference.md", 600, "verb_detail"),
    ("troubleshooting.md", 400, "trouble_rows"),
    ("glossary.md", 300, "glossary"),
    ("first-week-checklist.md", 300, None),
    ("adoption-checklist.md", 400, None),
    ("using-your-ide.md", 350, None),
    ("platform-lane-overview.md", 250, None),
]

FEATURE_COVERAGE_KEYWORDS: dict[str, list[str]] = {
    "onboarding": ["second-brain", "getting-started"],
    "ingest": ["ingest-confluence", "ingest-vendor-doc", "ingest-rss", "triage-rss", "review-rss"],
    "compile_query": ["workspace-compile", "workspace-query"],
    "project_chain": [
        "workspace-start-project",
        "workspace-vp-agent",
        "workspace-pm-agent",
        "workspace-architect-agent",
        "workspace-engineer-agent",
        "chain-profiles",
        "technical-writer",
        "architect-reviewer",
    ],
    "align_publish": ["workspace-align", "workspace-publish", "workspace-archive", "workspace-lint"],
    "vendor": ["seed-vendor-docs", "revalidate-vendor", "vendor-catalog"],
    "platform": ["platform-transcript-librarian", "platform-research-review", "platform-implement-backlog"],
    "session": ["workspace-session-audit", "workspace-thinking-partner"],
    "rss_impact": ["align-rss-impact"],
    "scripts": ["verify-setup", "lint-platform", "sync-", "promote-"],
}

HUB_WORKFLOW_LINKS = [
    "workflow-ingest.md",
    "workflow-compile-and-query.md",
    "workflow-project-chain.md",
    "workflow-align-and-publish.md",
    "how-second-brain-works.md",
    "getting-started.md",
    "adoption-checklist.md",
    "first-week-checklist.md",
]


def support_doc_root(root: Path) -> Path:
    return root / SUPPORT_DOC_REL


def parse_frontmatter(text: str) -> dict[str, Any]:
    if yaml is None:
        return {}
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def extract_body_for_depth(text: str) -> str:
    """Body text excluding frontmatter and trailing meta sections."""
    body = strip_frontmatter(text)
    lines = body.splitlines()
    cut: int | None = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("## Sources consulted") or stripped.startswith("## See also") or stripped.startswith("## See Also"):
            cut = i
            break
    if cut is not None:
        body = "\n".join(lines[:cut])
    return body


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def count_table_rows(text: str) -> int:
    rows = [line for line in text.splitlines() if TABLE_ROW_RE.match(line)]
    # exclude header separator rows like |---|---|
    data_rows = [r for r in rows if not re.match(r"^\|\s*[-:]+\s*\|", r)]
    return max(0, len(data_rows) - 1)  # minus header row


def count_glossary_terms(text: str) -> int:
    terms = set()
    for match in GLOSSARY_TERM_RE.finditer(text):
        term = match.group(1).strip()
        if term and term.lower() not in ("term", "definition", "---"):
            terms.add(term.lower())
    return len(terms)


def has_flow_diagram(text: str) -> bool:
    lower = text.lower()
    return "```mermaid" in lower or "```text" in lower or "```\n" in text and "→" in text


def depth_rule_for_filename(name: str) -> tuple[int, str | None] | None:
    for pattern, min_words, extra in PAGE_DEPTH_RULES:
        if pattern.startswith("workflow-") and pattern.endswith("*.md"):
            if name.startswith("workflow-") and name.endswith(".md"):
                return min_words, extra
        elif name == pattern:
            return min_words, extra
    return None


def load_manifest(root: Path) -> dict[str, Any]:
    path = root / MANIFEST_REL
    if not path.is_file() or yaml is None:
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_inventory(root: Path) -> dict[str, Any]:
    path = root / INVENTORY_REL
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def inventory_hash(data: dict[str, Any]) -> str:
    payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def iter_support_pages(root: Path) -> list[Path]:
    base = support_doc_root(root)
    if not base.is_dir():
        return []
    skip = {".inventory", "sync-log"}
    pages: list[Path] = []
    for path in sorted(base.rglob("*.md")):
        if any(part in skip for part in path.parts):
            continue
        if path.name == "README.md" and path.parent == base:
            continue
        pages.append(path)
    return pages


def resolve_repo_path(root: Path, ref: str, *, base: Path | None = None) -> Path | None:
    ref = ref.strip().strip('"').strip("'")
    if not ref or ref.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if ref.startswith("/"):
        ref = ref.lstrip("/")
    anchor_stripped = ref.split("#")[0]
    if not anchor_stripped:
        return None
    if base is not None and not Path(anchor_stripped).is_absolute():
        candidate = (base / anchor_stripped).resolve()
    else:
        candidate = (root / anchor_stripped.replace("\\", "/")).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    if candidate.is_file():
        return candidate
    if candidate.with_suffix(".md").is_file():
        return candidate.with_suffix(".md")
    if candidate.is_dir() and (candidate / "README.md").is_file():
        return candidate / "README.md"
    if candidate.is_dir():
        return candidate
    return None
