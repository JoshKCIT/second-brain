---
title: "Concepts for operators"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - "docs/platform-decision-records/RC-2026-05-27-146-raw-inbox-staging.md"
  - "docs/platform-decision-records/RC-2026-06-10-018-platform-support-documentation.md"
  - "templates/workspace/routing-map.md"
---

# Concepts for operators

Plain-language governance for CEOs and daily operators. Authoritative rules remain in [AGENTS.md](../../../AGENTS.md); this page explains **why** the gates exist and **how** to use them without reading the full agent spec.

## Approval culture

Second Brain is **filesystem-first** with **approval-gated mutations**. Agents propose file changes; you approve important saves. This is intentional:

- **Trust** — you see diffs before wiki becomes "truth"
- **Audit** — `wiki/log.md` records compile, publish, stage transitions
- **Safety** — fail closed; agents stop rather than silently overwrite

Read-only operations (query, advisory align) do not need batch approval. Anything touching `wiki/**` from raw, publish to Confluence, or platform canonical files needs explicit consent.

You are the CEO in the project chain — stage gates are not bureaucracy; they prevent downstream agents from reopening settled scope.

## RC-146

**Compile and wiki writes from raw require explicit batch approval.**

What it means in practice:

1. Ingest may write `raw/` without compile approval
2. Before any `wiki/**` mutation from a compile batch, agent asks **y/n**
3. Small batches still require approval — no "implicit yes"

Applies to: Confluence compile, inbox staging compile, RSS promoted items, vendor compile batches.

What RC-146 does **not** block: writing raw, reports, handoff/orientation drafts, support doc regen (separate CEO merge on support docs).

If an agent compiles without asking, stop the session and revert.

## RC-151

**No unattended or scheduled wiki compile.**

Background automation (CI, cron) may:

- Validate support docs
- Ingest raw (if you configure it)
- Run lint/tests

Background automation may **not** silently compile to wiki. You must be in the loop for wiki mutations.

Support doc regen follows its own merge gate — still human-approved PR, not auto-commit to wiki.

## Citation and closure

**Citation-grounded:** Claims in project artifacts should trace to sources that exist on disk. `align-cite` verifies before publish.

**Closure:** Published project set must be jr-engineer-executable — no body wikilinks at review/published; internal standards inlined; vendor claims with parenthetical + See Also URL.

**Cross-project:** In-progress work cannot depend on another in-progress or archived project. Resolution: finish dependency, archive it, or restate.

**Vendor truth:** Claims about vendor products cite vendor-domain raw paths — internal docs lose on conflict for vendor capabilities.

## PH-006

When a **workspace** session surfaces Second Brain product ideas (transcripts, "we should change AGENTS.md", architecture proposals):

1. **Stop** workspace-lane edits to protected files
2. Switch to **platform** lane: `platform-transcript-librarian` or `platform-research-review`
3. Route through claim review and draft ADR
4. Implement only via approved PIC cycle (`platform-implement-backlog`)

Protected without explicit approval: `wiki/workspace-standards/**`, workspace projects (for platform claims), `PRD.md`, `product-brief.md`, `docs/product/roadmap.md`, `docs/product/architecture-rationale.md`, `AGENTS.md`.

## See Also

- [ceo-approval-guide.md](ceo-approval-guide.md)
- [lanes-and-approval-gates.md](lanes-and-approval-gates.md)
- [glossary.md](glossary.md)

## Sources consulted

- AGENTS.md, RC-146 ADR, RC-2026-06-10-018 ADR (RC-151), routing-map.md
