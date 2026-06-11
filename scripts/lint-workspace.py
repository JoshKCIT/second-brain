#!/usr/bin/env python3
"""
Structural workspace lint (checks 1-7, orphan sources, stale vendor docs).

Output: reports/workspace-lint-{date}.md
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
REQUIRED_FM = ["title", "type", "status", "sources", "created", "updated"]
AUTHORITY_TYPES = {"standard", "recommendation", "informational", "concept", "connection", "qa", "project-artifact"}
TIER2_SHIM_PATHS = (
    ".cursor/rules/agents.mdc",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
)
SHIM_LINE_BUDGET = 100
AGENTS_AGENT_CHAIN_LINE_BUDGET = 35  # PH-007: prose lines excluding diagram block


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if m and yaml:
        return yaml.safe_load(m.group(1)) or {}
    return {}


def word_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    body = m.group(0)[m.group(0).rfind("---", 3) + 3 :] if m else text
    if m:
        parts = text.split("---", 2)
        body = parts[2] if len(parts) >= 3 else text
    return len(re.findall(r"\w+", body))


def resolve_wikilink(root: Path, source_file: Path, target: str) -> Path | None:
    target = target.strip()
    if target.startswith("http"):
        return Path("/")  # external, treat as ok
    candidates = [
        root / f"{target}.md",
        root / target / "index.md",
        root / "wiki" / f"{target}.md",
    ]
    if not target.startswith("wiki/") and not target.startswith("raw/"):
        candidates.append(root / "wiki" / f"{target}.md")
    if target == "log":
        candidates.append(root / "wiki" / "log.md")
    for c in candidates:
        if c.is_file():
            return c
    return None


def collect_wiki_articles(root: Path, scope: Path | None) -> list[Path]:
    wiki = root / "wiki"
    articles = []
    for path in wiki.rglob("*.md"):
        if path.name in ("index.md", "log.md"):
            continue
        if "platform-research" in path.parts and scope != wiki:
            continue
        if scope and scope != wiki and scope not in path.parents and path != scope:
            continue
        articles.append(path)
    return articles


def collect_raw_external(root: Path) -> list[Path]:
    base = root / "raw" / "workspace-external"
    if not base.is_dir():
        return []
    return [p for p in base.rglob("*.md") if p.name != ".gitkeep"]


def parse_iso(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def collect_project_orientation_files(root: Path) -> list[Path]:
    base = root / "wiki" / "workspace-projects"
    if not base.is_dir():
        return []
    return [p for p in base.rglob("orientation.md") if p.is_file()]


def collect_sub_scaffold_files(root: Path) -> list[Path]:
    base = root / "wiki" / "workspace-projects"
    if not base.is_dir():
        return []
    return [p for p in base.rglob("*") if p.is_file() and "subprojects" in p.parts and p.suffix == ".md"]


def lint_sub_scaffold(root: Path, articles: list[Path]) -> list[str]:
    issues: list[str] = []
    for path in collect_sub_scaffold_files(root):
        rel = path.relative_to(root)
        fm = parse_frontmatter(path)
        if fm.get("publish_scope") != "exclude":
            issues.append(f"{rel}: missing publish_scope: exclude (RC-167)")
        if not fm.get("not_canonical"):
            issues.append(f"{rel}: missing not_canonical: true (RC-167)")
        if fm.get("status") in ("review", "published"):
            issues.append(f"{rel}: sub-scaffold must stay draft-tier (RC-167)")

    for article in articles:
        rel_article = article.relative_to(root)
        fm = parse_frontmatter(article)
        if fm.get("status") not in ("review", "published"):
            continue
        for src in fm.get("sources", []) or []:
            if isinstance(src, str) and "subprojects/" in src.replace("\\", "/"):
                issues.append(
                    f"{rel_article}: cites subprojects/ in sources at publish tier (RC-167)"
                )
    return issues


def collect_thinking_notes_files(root: Path) -> list[Path]:
    base = root / "wiki" / "workspace-projects"
    if not base.is_dir():
        return []
    return [
        p
        for p in base.rglob("*")
        if p.is_file() and "thinking-notes" in p.parts and p.suffix == ".md"
    ]


def lint_thinking_notes(root: Path, articles: list[Path]) -> list[str]:
    issues: list[str] = []
    for path in collect_thinking_notes_files(root):
        rel = path.relative_to(root)
        fm = parse_frontmatter(path)
        if fm.get("type") != "thinking-notes":
            issues.append(f"{rel}: expected type thinking-notes (RC-117)")
        if not fm.get("not_canonical"):
            issues.append(f"{rel}: missing not_canonical: true (RC-117)")
        if fm.get("publish_scope") != "exclude":
            issues.append(f"{rel}: missing publish_scope: exclude (RC-117 advisory)")
        if fm.get("status") in ("review", "published"):
            issues.append(f"{rel}: thinking-notes must stay draft-tier (RC-117)")

    for article in articles:
        rel_article = article.relative_to(root)
        fm = parse_frontmatter(article)
        if fm.get("status") not in ("review", "published"):
            continue
        for src in fm.get("sources", []) or []:
            if isinstance(src, str) and "thinking-notes/" in src.replace("\\", "/"):
                issues.append(
                    f"{rel_article}: cites thinking-notes/ in sources at publish tier (RC-117)"
                )
    return issues


def lint_topic_entity_compile(root: Path, articles: list[Path]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    advisories: list[str] = []
    for article in articles:
        rel = article.relative_to(root)
        rel_str = str(rel).replace("\\", "/")
        fm = parse_frontmatter(article)
        text = article.read_text(encoding="utf-8", errors="replace")
        body = text.split("---", 2)[2] if text.startswith("---") and text.count("---") >= 2 else text

        if fm.get("type") == "connection":
            connects = fm.get("connects") or []
            if len(connects) < 2:
                errors.append(f"{rel}: connection needs at least 2 connects entries (RC-148)")
            raw_sources = [
                s for s in (fm.get("sources") or []) if isinstance(s, str) and s.startswith("raw/")
            ]
            if not raw_sources:
                errors.append(f"{rel}: connection missing raw/ path in sources (RC-148)")
            if "## Evidence" not in body and "## Sources" not in body:
                advisories.append(f"{rel}: connection missing ## Evidence or ## Sources (RC-148)")

        if "workspace-concepts" in rel_str and fm.get("type") == "concept":
            if "## Sources" not in body:
                advisories.append(f"{rel}: concept missing ## Sources section (RC-148)")

    return errors, advisories


def lint_shim_line_budget(root: Path) -> list[str]:
    issues: list[str] = []
    for rel in TIER2_SHIM_PATHS:
        path = root / rel
        if not path.is_file():
            continue
        line_count = len(path.read_text(encoding="utf-8", errors="replace").splitlines())
        if line_count > SHIM_LINE_BUDGET:
            issues.append(
                f"{rel}: {line_count} lines exceeds RC-165 budget {SHIM_LINE_BUDGET} (advisory)"
            )
    return issues


def lint_agents_agent_chain_budget(root: Path) -> list[str]:
    """PH-007: advisory if AGENTS § Agent chain prose grows beyond pointer-first budget."""
    agents_path = root / "AGENTS.md"
    if not agents_path.is_file():
        return []
    text = agents_path.read_text(encoding="utf-8", errors="replace")
    marker = "### Agent chain (project workflow)"
    start = text.find(marker)
    if start < 0:
        return ["AGENTS.md: missing ### Agent chain section"]
    rest = text[start + len(marker) :]
    end = rest.find("\n## ")
    section = rest[:end] if end >= 0 else rest
    # Exclude fenced diagram block from prose line count
    prose = re.sub(r"```[\s\S]*?```", "", section)
    prose_lines = [ln for ln in prose.splitlines() if ln.strip()]
    if len(prose_lines) > AGENTS_AGENT_CHAIN_LINE_BUDGET:
        return [
            f"AGENTS.md § Agent chain: {len(prose_lines)} prose lines exceeds "
            f"PH-007 budget {AGENTS_AGENT_CHAIN_LINE_BUDGET} — move experiment detail to "
            "templates/workspace/experiment-registry.md (advisory)"
        ]
    # Drift: inline experiment ADR paths should not reappear in agent chain
    drift = re.findall(r"DRAFT-RC-2026-05-27-(?:1(?:16|17|30|46|48|62|63|64|65|67))", section)
    if drift:
        return [
            f"AGENTS.md § Agent chain: inline experiment ADR references {drift} — "
            "use experiment-registry.md instead (advisory)"
        ]
    return []


def lint_orientation_and_agent_mode(root: Path, articles: list[Path]) -> dict[str, list[str]]:
    orientation_issues: list[str] = []
    agent_mode_issues: list[str] = []
    publish_markers = ("## See Also", "## Success criteria", "## Acceptance criteria")

    for path in collect_project_orientation_files(root):
        rel = path.relative_to(root)
        fm = parse_frontmatter(path)
        if fm.get("type") != "session-orientation":
            orientation_issues.append(f"{rel}: expected type session-orientation")
        if not fm.get("not_canonical"):
            orientation_issues.append(f"{rel}: missing not_canonical: true (RC-163)")
        if fm.get("status") in ("review", "published"):
            orientation_issues.append(f"{rel}: orientation must stay draft-tier (RC-163)")

    for article in articles:
        rel_article = article.relative_to(root)
        fm = parse_frontmatter(article)
        rel_str = str(rel_article).replace("\\", "/")

        for src in fm.get("sources", []) or []:
            if isinstance(src, str) and "orientation.md" in src:
                orientation_issues.append(
                    f"{rel_article}: cites orientation.md in sources — not canonical (RC-163)"
                )

        if "workspace-projects" not in rel_str or fm.get("type") != "project-artifact":
            continue

        mode = fm.get("agent_mode")
        status = fm.get("status", "")
        if mode == "thinking":
            if status in ("review", "published"):
                agent_mode_issues.append(
                    f"{rel_article}: agent_mode thinking with status {status} (RC-116)"
                )
            text = article.read_text(encoding="utf-8", errors="replace")
            body = text.split("---", 2)[2] if text.startswith("---") and text.count("---") >= 2 else text
            for marker in publish_markers:
                if marker in body and status == "draft":
                    agent_mode_issues.append(
                        f"{rel_article}: thinking mode with publish marker `{marker}` (RC-116 advisory)"
                    )
                    break

    return {
        "orientation_integrity": orientation_issues,
        "agent_mode": agent_mode_issues,
    }


def run_lint(root: Path, scope: Path | None) -> dict:
    findings: dict[str, list[str]] = {
        "broken_links": [],
        "orphan_pages": [],
        "orphan_sources": [],
        "stale_articles": [],
        "missing_backlinks": [],
        "sparse_articles": [],
        "frontmatter": [],
        "stale_vendor_docs": [],
        "orientation_integrity": [],
        "agent_mode": [],
        "sub_scaffold_integrity": [],
        "thinking_notes_integrity": [],
        "shim_line_budget": [],
        "topic_entity_compile": [],
        "topic_entity_compile_advisory": [],
    }

    articles = collect_wiki_articles(root, scope)
    article_set = {a.resolve() for a in articles}
    inbound: dict[Path, set[Path]] = {a.resolve(): set() for a in articles}

    referenced_raw: set[str] = set()

    for article in articles:
        text = article.read_text(encoding="utf-8", errors="replace")
        rel_article = article.relative_to(root)
        fm = parse_frontmatter(article)

        for field in REQUIRED_FM:
            if field not in fm:
                findings["frontmatter"].append(f"{rel_article}: missing `{field}`")
        if fm.get("type") in ("concept", "standard", "recommendation") and not fm.get("domain"):
            findings["frontmatter"].append(f"{rel_article}: missing `domain`")
        if fm.get("type") in ("standard", "recommendation", "informational") and not fm.get("authority"):
            findings["frontmatter"].append(f"{rel_article}: missing `authority`")

        for src in fm.get("sources", []) or []:
            if isinstance(src, str) and src.startswith("raw/"):
                referenced_raw.add(src.replace("\\", "/"))

        wc = word_count(article)
        if wc < 200:
            findings["sparse_articles"].append(f"{rel_article}: {wc} words (advisory)")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            resolved = resolve_wikilink(root, article, target)
            if resolved is None:
                findings["broken_links"].append(f"{rel_article}: broken link [[{target}]]")
            elif resolved.resolve() in article_set:
                inbound[resolved.resolve()].add(article.resolve())

    for article in articles:
        if len(inbound.get(article.resolve(), set())) == 0:
            rel = article.relative_to(root)
            if "workspace-concepts" in rel.parts or "workspace-connections" in rel.parts:
                findings["orphan_pages"].append(f"{rel}: no inbound wikilinks (advisory)")

    for raw_path in collect_raw_external(root):
        raw_rel = str(raw_path.relative_to(root)).replace("\\", "/")
        if raw_rel not in referenced_raw:
            # also check partial path without .md
            found = any(raw_rel.replace(".md", "") in r or raw_rel in r for r in referenced_raw)
            if not found:
                findings["orphan_sources"].append(f"{raw_rel}: not referenced in wiki sources frontmatter")

    now = datetime.now(timezone.utc)
    for raw_path in collect_raw_external(root):
        meta = parse_frontmatter(raw_path)
        revalidate = parse_iso(str(meta.get("revalidate_after", "")))
        raw_rel = str(raw_path.relative_to(root)).replace("\\", "/")
        if revalidate and now > revalidate:
            findings["stale_vendor_docs"].append(f"{raw_rel}: past revalidate_after ({meta.get('revalidate_after')})")

    extra = lint_orientation_and_agent_mode(root, articles)
    for key, items in extra.items():
        findings[key] = items
    findings["sub_scaffold_integrity"] = lint_sub_scaffold(root, articles)
    findings["thinking_notes_integrity"] = lint_thinking_notes(root, articles)
    findings["shim_line_budget"] = lint_shim_line_budget(root)
    findings["agents_agent_chain_budget"] = lint_agents_agent_chain_budget(root)
    te_errors, te_advisories = lint_topic_entity_compile(root, articles)
    findings["topic_entity_compile"] = te_errors
    findings["topic_entity_compile_advisory"] = te_advisories

    return findings


def severity_map() -> dict[str, str]:
    return {
        "broken_links": "error",
        "frontmatter": "error",
        "orphan_sources": "warning",  # RC-146: expected for raw inbox until approved compile
        "stale_vendor_docs": "warning",
        "orphan_pages": "warning",
        "missing_backlinks": "warning",
        "sparse_articles": "suggestion",
        "stale_articles": "warning",
        "orientation_integrity": "error",
        "agent_mode": "warning",
        "sub_scaffold_integrity": "error",
        "thinking_notes_integrity": "error",
        "shim_line_budget": "warning",
        "agents_agent_chain_budget": "warning",
        "topic_entity_compile": "error",
        "topic_entity_compile_advisory": "warning",
    }


def write_report(root: Path, findings: dict) -> Path:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = root / "reports" / f"workspace-lint-{date}.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    sev = severity_map()

    errors, warnings, suggestions = [], [], []
    for check, items in findings.items():
        if not items:
            continue
        level = sev.get(check, "warning")
        block = f"### {check.replace('_', ' ')}\n" + "\n".join(f"- {i}" for i in items) + "\n"
        if level == "error":
            errors.append(block)
        elif level == "suggestion":
            suggestions.append(block)
        else:
            warnings.append(block)

    summary_rows = []
    for check, items in findings.items():
        summary_rows.append(f"| {check.replace('_', ' ')} | {len(items)} | {sev.get(check, 'warning')} |")

    body = f"""# Lint Report - {date}

Scope: wiki (excluding platform-research claim registers)
Generated by: `scripts/lint-workspace.py`

## Errors

{"".join(errors) if errors else "_None._" + chr(10)}

## Warnings

{"".join(warnings) if warnings else "_None._" + chr(10)}

## Suggestions

{"".join(suggestions) if suggestions else "_None._" + chr(10)}

## Summary

| Check | Findings | Severity |
|---|---|---|
{chr(10).join(summary_rows)}

## Recommended actions

1. Fix all errors before publish.
2. Re-run: `python scripts/lint-workspace.py`
"""
    report_path.write_text(body, encoding="utf-8")
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Workspace structural lint")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--scope", type=Path, help="Limit to wiki subtree")
    args = parser.parse_args()
    root = args.root.resolve()
    scope = args.scope.resolve() if args.scope else None

    findings = run_lint(root, scope)
    report = write_report(root, findings)

    err_count = sum(
        len(v)
        for k, v in findings.items()
        if severity_map().get(k) == "error"
    )
    print(f"Report: {report}")
    print(f"Errors: {err_count}")
    for check, items in findings.items():
        if items:
            print(f"  {check}: {len(items)}")
    return 1 if err_count else 0


if __name__ == "__main__":
    sys.exit(main())
