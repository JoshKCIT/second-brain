---
title: "Lanes and approval gates"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - "docs/platform-decision-records/RC-2026-05-27-146-raw-inbox-staging.md"
  - "templates/workspace/routing-map.md"
---

# Lanes and approval gates

Reference for lane prefixes and the approval gates that protect wiki and canonical files.

## Lane table

| Lane | Prefix | Use when | Example paths |
|------|--------|----------|---------------|
| Workspace | `workspace-*` | Everyday docs: ingest, compile, projects, query | `raw/workspace-confluence/`, `wiki/workspace-projects/` |
| Platform | `platform-*` | Improve Second Brain: transcripts, research, PIC | `raw/platform-transcripts/`, `wiki/platform-research/` |

**PH-006:** Mid-project product ideas → escalate to platform lane; do not mutate protected workspace/PRD files without approval.

Protected without explicit approval: `wiki/workspace-standards/**`, workspace projects (for platform claims), `PRD.md`, `product-brief.md`, `docs/product/roadmap.md`, `docs/product/architecture-rationale.md`, `AGENTS.md`.

## RC-146

Compile and wiki writes from raw require **explicit batch approval**.

- Ingest may stage raw only
- Compile asks **"Compile these N items to wiki? (y/n)"** before `wiki/**` mutations
- Applies to: Confluence compile, inbox staging, RSS promoted items, vendor compile batches

Orphan raw in inbox is expected until you approve compile (RC-146 inbox staging).

## RC-151

No unattended or scheduled **wiki compile**. Background jobs may ingest raw, validate support docs, or run lint — wiki updates always need CEO approval in the loop.

Support doc full regen uses a separate CEO merge gate on the support doc diff — still not wiki compile.

## CEO workflow

| Operation | Steps |
|-----------|-------|
| **Compile** | Review batch list → y/n |
| **Project stage** | Review artifact → proceed or reopen |
| **Publish** | align-cite + align-closure → review HTML → confluence optional |
| **Platform ADR** | Review draft ADR → approve → PIC cycle |
| **Support doc sync** | `/platform-sync-support-docs` → lint strict → accept sync batch y/n or PR |

Detail: [ceo-approval-guide.md](ceo-approval-guide.md).

## Sources consulted

- AGENTS.md, RC-146 ADR, routing-map.md
