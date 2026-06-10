#!/usr/bin/env python3
"""
Lint docs/platform-support-documentation/ for structure, links, and inventory parity.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

from support_doc_common import (  # noqa: E402
    FEATURE_COVERAGE_KEYWORDS,
    GLOSSARY_MIN_TERMS,
    MANIFEST_MIN_PAGES,
    MANIFEST_REQUIRED_KEYS,
    PAGE_FM_REQUIRED,
    REQUIRED_SECTIONS,
    STALE_PATHS,
    STRICT_PAGES,
    TOP_WORKSPACE_VERBS,
    TRANSCRIPT_PATTERNS,
    TROUBLESHOOTING_MIN_ROWS,
    count_glossary_terms,
    count_table_rows,
    count_words,
    depth_rule_for_filename,
    extract_body_for_depth,
    has_flow_diagram,
    iter_support_pages,
    load_inventory,
    load_manifest,
    parse_frontmatter,
    resolve_repo_path,
    support_doc_root,
)

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


@dataclass
class LintResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add(self, msg: str, *, warning: bool = False) -> None:
        (self.warnings if warning else self.errors).append(msg)


def lint_manifest(root: Path, result: LintResult) -> None:
    manifest = load_manifest(root)
    path = root / "docs/platform-support-documentation/manifest.yml"
    if not path.is_file():
        result.add("manifest_present: manifest.yml missing")
        return
    for key in MANIFEST_REQUIRED_KEYS:
        if key not in manifest:
            result.add(f"manifest_present: missing key {key}")


def lint_page_frontmatter(root: Path, result: LintResult) -> None:
    for path in iter_support_pages(root):
        rel = path.relative_to(root).as_posix()
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not meta:
            result.add(f"page_frontmatter: {rel} missing YAML frontmatter")
            continue
        for key in PAGE_FM_REQUIRED:
            if key not in meta:
                result.add(f"page_frontmatter: {rel} missing {key}")
        sources = meta.get("sources") or []
        if not isinstance(sources, list) or not sources:
            result.add(f"page_frontmatter: {rel} sources must be non-empty list")


def lint_sources_exist(root: Path, result: LintResult) -> None:
    for path in iter_support_pages(root):
        rel = path.relative_to(root).as_posix()
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        for src in meta.get("sources") or []:
            src_str = str(src).rstrip("/")
            if src_str.endswith("/") or src_str.endswith("\\"):
                result.add(f"sources_exist: {rel} cites directory not file {src}", warning=True)
                continue
            if not resolve_repo_path(root, src_str):
                result.add(f"sources_exist: {rel} cites missing path {src}")


def lint_markdown_links(root: Path, result: LintResult) -> None:
    from support_doc_common import MARKDOWN_LINK_RE

    for path in iter_support_pages(root):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        base = path.parent
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not resolve_repo_path(root, target, base=base):
                result.add(f"markdown_links: {rel} broken link {target}")


def lint_wikilinks(root: Path, result: LintResult) -> None:
    from support_doc_common import WIKILINK_RE

    for path in iter_support_pages(root):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            wiki_path = root / "wiki" / f"{target}.md"
            if not wiki_path.is_file():
                result.add(f"wikilinks: {rel} unresolved wikilink [[{target}]]", warning=True)


def lint_stale_paths(root: Path, result: LintResult) -> None:
    base = support_doc_root(root)
    for path in base.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        for stale in STALE_PATHS:
            if stale in text:
                result.add(f"stale_paths: {rel} contains deprecated path {stale}")


def lint_transcript_contamination(root: Path, result: LintResult) -> None:
    base = support_doc_root(root)
    for path in base.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        for pattern in TRANSCRIPT_PATTERNS:
            if pattern.search(text):
                result.add(f"transcript_contamination: {rel} matches {pattern.pattern}")


def lint_required_sections(root: Path, result: LintResult) -> None:
    for path in iter_support_pages(root):
        name = path.name
        if name not in REQUIRED_SECTIONS:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        for section in REQUIRED_SECTIONS[name]:
            if f"## {section}" not in text and f"# {section}" not in text:
                result.add(f"required_sections: {rel} missing section '{section}'")


def lint_prompt_parity(root: Path, result: LintResult) -> None:
    inventory = load_inventory(root)
    if not inventory:
        result.add("prompt_parity: inventory.json missing; run sync-support-doc-inventory.py --write")
        return
    catalog = support_doc_root(root) / "operator-guide" / "feature-catalog.md"
    if not catalog.is_file():
        result.add("prompt_parity: feature-catalog.md missing")
        return
    catalog_text = catalog.read_text(encoding="utf-8").lower()
    for prompt in inventory.get("prompts") or []:
        stem = str(prompt.get("stem", ""))
        path = str(prompt.get("path", ""))
        if stem and stem not in catalog_text and path not in catalog_text:
            result.add(f"prompt_parity: feature-catalog missing prompt {stem}")


def lint_routing_parity(root: Path, result: LintResult) -> None:
    inventory = load_inventory(root)
    orphans = inventory.get("routing_orphans") or []
    for stem in orphans:
        result.add(f"routing_parity: routing-map invoke '{stem}' has no prompt file", warning=True)


def lint_readme_map_link(root: Path, result: LintResult) -> None:
    readme = root / "README.md"
    if not readme.is_file():
        return
    if "platform-support-documentation" not in readme.read_text(encoding="utf-8"):
        result.add("readme_map_link: README.md missing platform-support-documentation link", warning=True)


def lint_feature_coverage(root: Path, result: LintResult) -> None:
    catalog = support_doc_root(root) / "operator-guide" / "feature-catalog.md"
    if not catalog.is_file():
        return
    text = catalog.read_text(encoding="utf-8").lower()
    for category, keywords in FEATURE_COVERAGE_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() not in text:
                result.add(f"feature_coverage: feature-catalog missing {category} keyword '{kw}'", warning=True)


def lint_strict_pages(root: Path, result: LintResult) -> None:
    for rel in STRICT_PAGES:
        if not (root / "docs/platform-support-documentation" / rel).is_file():
            result.add(f"strict: missing required page {rel}")


def lint_page_depth(root: Path, result: LintResult, *, strict: bool) -> None:
    for path in iter_support_pages(root):
        rule = depth_rule_for_filename(path.name)
        if rule is None:
            continue
        min_words, extra = rule
        text = path.read_text(encoding="utf-8")
        body = extract_body_for_depth(text)
        words = count_words(body)
        rel = path.relative_to(root).as_posix()
        if words < min_words:
            msg = f"page_depth: {rel} has {words} words (min {min_words})"
            result.add(msg, warning=not strict)
        if extra == "flow_diagram" and not has_flow_diagram(body):
            msg = f"page_depth: {rel} missing flow diagram"
            result.add(msg, warning=not strict)
        if extra == "workflow":
            lower = body.lower()
            if "worked example" not in lower:
                result.add(f"workflow_structure: {rel} missing worked example section", warning=not strict)
            if "approval" not in lower:
                result.add(f"workflow_structure: {rel} missing approval content", warning=not strict)
        if extra == "glossary":
            terms = count_glossary_terms(body)
            if terms < GLOSSARY_MIN_TERMS:
                result.add(f"glossary_terms: {rel} has {terms} terms (min {GLOSSARY_MIN_TERMS})", warning=not strict)
        if extra == "trouble_rows":
            rows = count_table_rows(body)
            if rows < TROUBLESHOOTING_MIN_ROWS:
                result.add(f"troubleshooting_rows: {rel} has {rows} problem rows (min {TROUBLESHOOTING_MIN_ROWS})", warning=not strict)
        if extra == "verb_detail":
            lower = body.lower()
            for verb in TOP_WORKSPACE_VERBS:
                if verb.lower() not in lower:
                    result.add(f"verb_reference_depth: {rel} missing verb {verb}", warning=not strict)
            detail_idx = lower.find("## per-verb detail")
            detail = body[detail_idx:] if detail_idx >= 0 else body
            missing_labels = 0
            for verb in TOP_WORKSPACE_VERBS:
                chunk_idx = detail.lower().find(verb.lower())
                if chunk_idx < 0:
                    missing_labels += 3
                    continue
                chunk = detail[chunk_idx : chunk_idx + 800].lower()
                for label in ("when", "approve", "output"):
                    if label not in chunk:
                        missing_labels += 1
            if missing_labels > 3:
                result.add(f"verb_reference_depth: {rel} per-verb When/Approve/Outputs incomplete", warning=not strict)


def lint_getting_started_setup(root: Path, result: LintResult, *, strict: bool) -> None:
    path = support_doc_root(root) / "user-guide" / "getting-started.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(root).as_posix()
    for section in ("Credentials", "Verify setup", "Onboarding"):
        if f"## {section}" not in text:
            result.add(f"getting_started_setup: {rel} missing section '{section}'", warning=not strict)


def lint_manifest_parity(root: Path, result: LintResult, *, strict: bool) -> None:
    manifest = load_manifest(root)
    pages_written = manifest.get("pages_written") or []
    if len(pages_written) < MANIFEST_MIN_PAGES:
        msg = f"manifest_parity: pages_written has {len(pages_written)} entries (min {MANIFEST_MIN_PAGES})"
        result.add(msg, warning=not strict)
    for rel in pages_written:
        rel_str = str(rel).replace("\\", "/")
        if not (root / rel_str).is_file():
            result.add(f"manifest_parity: pages_written entry missing on disk: {rel_str}")
    manifest_set = {str(p).replace("\\", "/") for p in pages_written}
    for rel in STRICT_PAGES:
        full = f"docs/platform-support-documentation/{rel}"
        if full not in manifest_set:
            result.add(f"manifest_parity: STRICT page not in manifest pages_written: {full}", warning=not strict)


def write_report(root: Path, result: LintResult) -> Path:
    reports = root / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = reports / f"platform-support-doc-lint-{date}.md"
    lines = [
        "# Platform support documentation lint",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        f"Errors: {len(result.errors)}",
        f"Warnings: {len(result.warnings)}",
        "",
    ]
    if result.errors:
        lines.append("## Errors")
        lines.extend(f"- {e}" for e in result.errors)
        lines.append("")
    if result.warnings:
        lines.append("## Warnings")
        lines.extend(f"- {w}" for w in result.warnings)
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def run_lint(root: Path, *, strict: bool = False) -> LintResult:
    result = LintResult()
    lint_manifest(root, result)
    lint_page_frontmatter(root, result)
    lint_sources_exist(root, result)
    lint_markdown_links(root, result)
    lint_wikilinks(root, result)
    lint_stale_paths(root, result)
    lint_transcript_contamination(root, result)
    lint_required_sections(root, result)
    lint_prompt_parity(root, result)
    lint_routing_parity(root, result)
    lint_readme_map_link(root, result)
    lint_feature_coverage(root, result)
    if strict:
        lint_strict_pages(root, result)
        lint_page_depth(root, result, strict=True)
        lint_getting_started_setup(root, result, strict=True)
        lint_manifest_parity(root, result, strict=True)
    else:
        lint_page_depth(root, result, strict=False)
        lint_getting_started_setup(root, result, strict=False)
        lint_manifest_parity(root, result, strict=False)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint platform support documentation")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    result = run_lint(root, strict=args.strict)
    report = write_report(root, result)
    print(f"Wrote {report.relative_to(root)}")
    print(f"Errors: {len(result.errors)}  Warnings: {len(result.warnings)}")
    for err in result.errors:
        print(f"  ERROR: {err}")
    for warn in result.warnings:
        print(f"  WARN: {warn}")
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
