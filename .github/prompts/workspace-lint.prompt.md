---
description: Run all health checks on the wiki. Seven structural checks plus engineering additions. Output a structured report with severity per finding.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-lint

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are running the full lint pass on the wiki. Catches drift, orphans, contradictions, deprecated references, and rule violations.

## Inputs

- Optional `--structural-only` flag: skip LLM-driven checks (contradictions, conformance); free to run
- Optional `--scope {path}` flag: limit lint to a specific subtree of `wiki/`

## Checks

### Structural (always run)

1. **Broken links.** Walk every `[[wikilink]]` in `wiki/`; flag any that point to non-existent files.
2. **Orphan pages.** Articles with zero inbound links from other articles in the same set. Flag (advisory).
3. **Orphan sources.** Files in `raw/` with no corresponding wiki article referencing them. Flag.
4. **Stale articles.** Wiki articles whose source raw page has changed `content_hash` since the article was last compiled. Flag for re-compile.
5. **Missing backlinks.** A links to B; B does not link back to A. Flag (advisory; not always required).
6. **Sparse articles.** Articles under 200 words. Flag (advisory; sparse is sometimes correct).
7. **Frontmatter completeness.** Articles missing required fields (title, type, status, sources, created, updated, plus authority and domain where applicable). Flag.

### Engineering additions (always run)

8. **Deprecated standards in use.** Standards with frontmatter `deprecated: true` that are still referenced by active artifacts. Flag.
9. **Cross-team requirement conflicts.** Two standards from different teams giving incompatible guidance on the same topic. LLM-judged; advisory.
10. **Missing alignment.** Project artifacts that should cite an in-scope standard for a given claim type but do not. LLM-judged; advisory.
11. **Incomplete ingestion.** Pages in `raw/` without any wiki article referencing them, OR wiki articles in `index.md` whose corresponding raw source is missing. Flag.
12. **Stale vendor docs.** Cached vendor docs past `revalidate_after`. Flag with action: refetch.
13. **Status-aware closure violations.** Artifacts at `review` or `published` with body wikilinks; cross-project dependency violations. Flag (use `align-closure` for full check).
14. **Manually edited content.** Articles with `manually_edited: true` in frontmatter; flag for LLM review (the LLM owns the wiki layer).
15. **Platform research-review integrity.** If research artifacts exist, validate `wiki/platform-research/claim-register.md` claim-record fields, decision values, impact score ranges, required report sections, and transcript-derived claim leakage into protected canonical files. The helper script is `python scripts/lint-platform-research.py --root .`; use `--strict` when release validation requires platform-research-review artifacts to exist.
16. **Instruction stack shim duplication (RC-161).** Scan `.cursor/rules/*.mdc`, `CLAUDE.md`, `.github/copilot-instructions.md`, and `.github/prompts/*.prompt.md` for repeated Tier-1 governance bullets (e.g., full align-cite/closure rule lists copied verbatim). Flag advisory when a shim restates more than two root invariants instead of referencing `AGENTS.md`. Tier-3 project scaffolds excluded.

### LLM-driven (skipped with `--structural-only`)

17. **Contradictions.** Two articles making conflicting claims on the same topic. LLM-judged; flag for resolution.

## Output

Write to `reports/workspace-lint-{date}.md`:

```markdown
# Lint Report - {date}

Scope: {full wiki | --scope path}
Total articles checked: {N}

## Errors (block downstream operations)

### {check name}
- {finding 1 with context}
- ...

## Warnings (advisory)

### {check name}
- {finding}
- ...

## Suggestions (low-priority)

### {check name}
- {finding}
- ...

## Summary

| Check | Findings | Severity |
|---|---|---|
| Broken links | {N} | error |
| Orphan pages | {N} | warning |
| Platform research-review integrity | {N} | error/warning |
| ... |

## Recommended actions

1. {Action with priority}
2. ...
```

## Severity levels

- **Error:** blocks publish or other downstream operations until resolved (broken links, missing required frontmatter, stale-vendor-doc-past-hard-max, incomplete ingestion)
- **Warning:** advisory; degrades wiki quality (orphans, missing backlinks, deprecated standards in use, vendor docs past TTL but under hard max)
- **Suggestion:** low-priority polish (sparse articles, missing optional frontmatter)

## Append to log

```
## [{ISO timestamp}] lint | {scope}
- Articles checked: {N}
- Errors: {N}
- Warnings: {N}
- Suggestions: {N}
- Report: {path}
```

## Cadence

Recommended: weekly via `/workspace-lint` invocation, or after any large ingest, or before any publish.
