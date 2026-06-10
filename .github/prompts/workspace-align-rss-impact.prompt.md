---
description: Phase 2 advisory report — how promoted RSS items relate to the knowledge hub. No wiki writes.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-align-rss-impact

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.

**Non-overridable:** reports only; wiki mutations require separate `/workspace-compile` approval (RC-146).

## Purpose

**Phase 2 — advisory.** After core RSS funnel is validated, analyze how one or more promoted (or compiled) RSS items relate to existing hub knowledge.

## Inputs

- One or more paths under `raw/workspace-rss-feed/promoted/` or compiled wiki articles citing RSS raw

## Read first (RC-018)

Document a minimal retrieval contract in the report header:

- `wiki/index.md`
- Matched `wiki/workspace-concepts/**`, standards, connections
- Relevant `raw/workspace-external/{vendor}/` when vendor-domain claims appear

## Output

Write `reports/workspace-rss-impact-{YYYY-MM-DD}.md` per batch or per item:

```markdown
# RSS impact report — {title}

## Retrieval contract
- Consulted: {paths}

## Reinforces
- {wiki path} — {section anchor} — {one line}

## Contradicts
- RSS claim vs {wiki or vendor raw} — {flag}

## Suggests
- New concept or connection — {rationale}

## Monitor only
- {item} — {reason}

## Suggested actions
- refetch vendor cache | compile batch | no action
```

## Trust

- Cite only paths that exist on disk.
- Contradictions must reference both RSS raw and wiki/vendor raw.
- Vendor capability claims are **informational** until `align-vendor-truth`.

## Write scope

- `reports/workspace-rss-impact-*.md` only
- **No** `wiki/**` mutations

## Follow-up

If report suggests stale vendor docs, offer `/workspace-revalidate-vendor-docs` or `/workspace-ingest-vendor-doc` for specific URLs.
