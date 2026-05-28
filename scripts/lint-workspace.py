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

    return findings


def severity_map() -> dict[str, str]:
    return {
        "broken_links": "error",
        "frontmatter": "error",
        "orphan_sources": "error",
        "stale_vendor_docs": "warning",
        "orphan_pages": "warning",
        "missing_backlinks": "warning",
        "sparse_articles": "suggestion",
        "stale_articles": "warning",
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

{"".join(errors) if errors else "_None._\n"}

## Warnings

{"".join(warnings) if warnings else "_None._\n"}

## Suggestions

{"".join(suggestions) if suggestions else "_None._\n"}

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
