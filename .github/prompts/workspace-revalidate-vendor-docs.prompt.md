---
description: Enumerate stale vendor doc caches under raw/workspace-external/ and offer batch refresh via workspace-ingest-vendor-doc.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-revalidate-vendor-docs

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are refreshing expired vendor documentation caches so cites stay within TTL policy. This prompt does not bulk-crawl vendor sites; it re-fetches **already cached** URLs whose `revalidate_after` date has passed.

## Inputs

- Optional `--vendor {slug}` — limit to one vendor (e.g., `aws`, `snowflake`)
- Optional `--dry-run` — list stale entries only; do not fetch

## Configuration

Read TTL rules from `config/second-brain.yml` (or `config/second-brain.example.yml` if local config missing):

- `vendor_revalidation.default_ttl_days` (default 90)
- `vendor_revalidation.per_vendor`
- `vendor_revalidation.hard_max_age_days` (365; past this, refetch is mandatory)

Enabled vendors: `vendor_sources.enabled` when present.

## Workflow

### Step 1: Scan cache

Walk `raw/workspace-external/**/*.md` (skip `.gitkeep`). For each file with frontmatter:

- Parse `fetched_at`, `revalidate_after`, `source_url`, `vendor`, `topic`
- Classify:
  - **fresh** — `revalidate_after` in the future
  - **stale** — past `revalidate_after` but within hard max age
  - **expired** — past hard max age (must refetch before cite at publish)

### Step 2: Report

Print a table:

| Vendor | Topic | Path | Status | Source URL | Last fetched |
|--------|-------|------|--------|------------|--------------|

### Step 3: User approval (required)

For each **stale** or **expired** entry (unless `--dry-run`):

- Present count and estimated refetch list
- Ask: refresh all, refresh selected vendors, or skip
- **Do not refetch without explicit user approval** (approval-gated mutation)

### Step 4: Refresh

For each approved entry, invoke the same pipeline as `/workspace-ingest-vendor-doc`:

1. Use defuddle on `source_url`
2. Rewrite the cache file with updated body and frontmatter (`fetched_at`, `revalidate_after`)
3. Append to `wiki/log.md`:

```
## [{ISO}] revalidate-vendor-docs | {vendor}/{topic}
- Source: {URL}
- Previous fetched_at: {old}
- New revalidate_after: {new}
```

### Step 5: Wiki compile (optional)

If the stale doc had a compiled `wiki/workspace-concepts/` or `wiki/workspace-standards/{vendor}/` article, offer to re-run `/workspace-compile` for that source only.

## Return value

Summary: fresh / stale / expired counts; refetched count; failures with URLs for manual follow-up.

## Failures

- Defuddle or network error: leave prior cache in place; mark failure in report; do not delete the old file
- Missing `source_url` in frontmatter: flag for manual fix; skip auto-refresh

## See also

- `.github/prompts/workspace-ingest-vendor-doc.prompt.md`
- `docs/vendor-catalog.md`
- `AGENTS.md` — vendor doc TTL and align-vendor-truth
