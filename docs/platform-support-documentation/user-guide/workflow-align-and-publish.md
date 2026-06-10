---
title: "Workflow: Align and publish"
audience: user
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - ".github/prompts/workspace-align-cite.prompt.md"
  - ".github/prompts/workspace-align-closure.prompt.md"
  - ".github/prompts/workspace-align-vendor-truth.prompt.md"
  - ".github/prompts/workspace-publish.prompt.md"
  - "docs/style/exemplar-published-doc.md"
---

# Workflow: Align and publish

**Audience:** Operators preparing project artifacts or wiki content for external consumption.

**Purpose:** **Align** operations verify citations, closure, and vendor truth before **publish**. The published artifact set must be **jr-engineer-executable** — a junior engineer can execute using only that set, without hunting wiki links in body prose.

## Terms

| Term | Meaning |
|------|---------|
| **align-cite** | Walk citations; verify source exists and supports claim |
| **align-closure** | Cross-project rules, body wikilinks at review/published, TODO resolution |
| **align-vendor-truth** | Vendor claims cite `raw/workspace-external/{vendor}/` not internal docs |
| **Review branch** | HTML preview in `confluence-review/` — no Confluence API |
| **Confluence branch** | Storage-format push via API |

## When to run which align

| Check | Blocking at publish? | Use when |
|-------|---------------------|----------|
| align-cite | Yes (default) | Every publish; optional `--advisory` per stage gate |
| align-closure | Yes (default) | Before publish; status-aware |
| align-vendor-truth | Recommended | Artifacts cite AWS/Snowflake/etc. |
| align-conformance / align-coverage | Advisory | Standard shape and requirements coverage |

Reports land in `reports/` — they do not mutate wiki unless you approve fixes.

## Align cite

For each citation in target artifact:

1. Verify cited path exists on disk
2. Verify content matches claim (section anchor when possible)
3. Output violations: claim text, source, problem

Fix violations by correcting citation, restating claim, or updating source wiki/raw.

## Align closure

Checks include:

- No wikilinks in body at `review` / `published` status
- No in-progress → in-progress or in-progress → archived project references
- Published: TODO / Open Questions resolved or in addendum

Navigation belongs in `## See Also` or frontmatter at review+.

## Vendor truth

Vendor-domain claims (what AWS S3 can do, etc.) must cite vendor cache paths. Internal docs flagged as outdated when they conflict — vendor wins for vendor claims.

Stale vendor cache (>90 day TTL default): refetch via `/workspace-ingest-vendor-doc` before citing.

## Publish branches

```text
/workspace-publish
  ├── review  →  confluence-review/{slug}/{doc}-{timestamp}.html  →  open folder in browser
  └── confluence  →  align-cite + align-closure pass  →  API create/update pages
```

Pre-publish: align-cite and align-closure run automatically on confluence branch unless you explicitly override (logged).

## Worked example

**Scenario:** Publish PM PRD after engineering finalize.

1. Artifacts at `status: review` under `wiki/workspace-projects/{slug}/`
2. You: `/workspace-align-cite` on `product-requirements.md` — 0 violations
3. You: `/workspace-align-closure` on project set — 0 violations
4. You: `/workspace-align-vendor-truth` — 1 violation: Snowflake claim cited internal doc
5. Agent: suggests fetch `raw/workspace-external/snowflake/...` — you approve refetch and fix citation
6. You: `/workspace-publish` → **review** — HTML path printed; folder opens
7. You: read in browser — inline rules present for internal standards; See Also has Confluence URLs
8. You: `/workspace-publish` → **confluence** — pages created; status → `published`

## Approval checkpoints

| Step | Approval |
|------|----------|
| align override | Explicit if violations remain |
| confluence publish | Implicit after align pass or logged override |
| status → published | CEO confirms artifact set complete |

## Jr-engineer-executable bar

Published set must include:

- Inlined rules for internal standards (not just wiki links)
- Parenthetical vendor attribution + See Also URL for vendor claims
- Self-contained stage artifacts in project directory
- No dependency on another in-progress or archived project

See [docs/style/exemplar-published-doc.md](../../style/exemplar-published-doc.md) for quality target.

## Common mistakes

- Publishing with body wikilinks still in prose
- Skipping vendor truth when PRD mentions cloud capabilities
- Using query retrieval as citation proof — align-cite still required
- Cross-project wikilinks to unfinished work — use published projects or restate

## See Also

- [workflow-project-chain.md](workflow-project-chain.md)
- [operator-guide/concepts-for-operators.md](../operator-guide/concepts-for-operators.md)
- [workspace-lint](../operator-guide/feature-catalog.md)

## Sources consulted

- AGENTS.md, align prompts, workspace-publish.prompt.md, exemplar-published-doc.md
