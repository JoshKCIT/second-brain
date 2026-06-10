# HANDOFF.md — Build handoff to VS Code + GitHub Copilot

This document tells the next agent session (VS Code with GitHub Copilot in agent mode) what state Second Brain is in, what to build first, what to read for context, and what guardrails apply. Read this first, then follow the pointers below.

---

## Read these in order

1. `.github/copilot-instructions.md` — your shim and operating instructions for this repo
2. `AGENTS.md` — canonical operating spec (longer; comprehensive)
3. `product-brief.md` — problem statement, scope, constraints, decisions log
4. `PRD.md` — what v1 builds (functional requirements, user stories, milestones)
5. `docs/product/roadmap.md` — phase plan; **Phases 1A–2 complete**; **current phase: Phase 3**; Phase 1B (Confluence) blocked
6. `docs/product/vendor-catalog.md` — vendor slugs, doc roots, Tier A/B/C integration
7. `docs/product/architecture-rationale.md` — why the architectural choices were made
8. `docs/progress-log.md` — session history; append your sessions here

---

## Current state (2026-05-27)

### Platform foundation — complete

Platform-lane work from transcript review is shipped. It does **not** replace v1 workspace build (ingest, compile, E2E project).

- Platform research review: prompts, skill, Cursor agent, lint script, tests
- Accepted ADRs: RC-014, RC-010, RC-001, RC-002, RC-015 (experiment), RC-003 (experiment), implementation-priority-loop
- `wiki/platform-research/` populated (claim register, backlog, transcript analyses)
- Page-index retrieval and citation≠similarity policy in `AGENTS.md`, `PRD.md`, `workspace-query.prompt.md`
- Implementation backlog queue: **idle** (RC-007/008 deferred; RC-012 blocked on failure data)

### v1 workspace build — Phases 1A–2 complete; Phase 3 active

The repo contains planning and scaffolding for workspace operations:

- **Top-level:** `README.md`, `AGENTS.md`, `CLAUDE.md`, `PRD.md`, `product-brief.md`, `.windsurfrules`, `.env.example`, `.gitignore`, `HANDOFF.md`
- **Per-agent shims:** `.github/copilot-instructions.md`, `.cursor/rules/agents.mdc`, `CLAUDE.md`, `.windsurfrules`
- **Workspace prompts:** `workspace-*` verbs in `.github/prompts/` (ingest, compile, query, align, publish, archive, lint, agent chain, onboarding)
- **Platform prompts:** `platform-research-review/` tree, `platform-research-review.prompt.md`, `platform-transcript-librarian.prompt.md`
- **Skills:** `obsidian-markdown`, `obsidian-bases`, `defuddle`, `platform-research-review`
- **Agents:** `workspace-adr-generator.agent.md`; Cursor `platform-research-reviewer`, `platform-transcript-librarian`
- **Hooks:** `secrets-scanner`, `tool-guardian`, `session-logger`, `governance-audit` — ported, **not verified** for Copilot (Phase 1)
- **Config:** `config/second-brain.example.yml`, `config/platform-research-review.example.yml`
- **Personas:** `templates/personas/ceo/` **populated**; other personas are v1.x stubs
- **Scripts:** `verify-setup.py`, `seed-vendor-docs.py`, `revalidate-vendor-docs.py`, `compile-workspace-external.py`, `lint-workspace.py`, `lint-platform-research.py`, `sync-transcript-register.py`
- **Wiki (local, gitignored):** `wiki/index.md`, `wiki/log.md`, 14 vendor concepts, 4 Base views (tracked under `wiki/workspace-views/`), platform transcript analyses (tracked)

### What is NOT yet done (v1 blockers)

- End-to-end project through agent chain — **Phase 3** (active)
- Atlassian / Confluence ingest — **Phase 1B, blocked** until user has space access
- Hook verification in Copilot — deferred; documented in progress log
- Exemplar final polish — Phase 6

### Phase 1A–2 — complete (2026-05-28)

- Vendor stack: AWS (6 topics), Snowflake (7), Informatica (2); IBM Db2 removed
- Exit reports: `docs/build-history/phase-1a-exit-report.md`, `docs/build-history/phase-2-exit-report.md`
- Regenerate locally: `python scripts/verify-setup.py`, `python scripts/lint-workspace.py`, `python scripts/revalidate-vendor-docs.py --dry-run`

---

## Phase 3 — first workspace project (active)

Per `docs/product/roadmap.md` Phase 3:

### 0. Confirm prerequisites

- `config/second-brain.yml` copied from example; `vendor_sources` enabled
- Local wiki initialized (`verify-setup.py` or existing `wiki/index.md`)
- User declares project intent (e.g. AWS + Snowflake + Informatica hybrid data platform doc buildout)

### 1. Run `/workspace-start-project`

CEO → VP → PM → Architect (if technical) → Engineer → finalize. CEO approval between stages.

### 2. Append `docs/progress-log.md`

Log Phase 3 milestones and any align/publish dry runs.

---

## Phase 1B — Confluence (when access is available)

Defer until user has Atlassian credentials and a test space.

### 1. Spike the Atlassian Remote MCP Server

**Goal:** validate whether the MCP exposes the page metadata Second Brain needs (ADF body, version, last_modified, labels, ancestors, attachments, source_url, page_id, space_key). See `docs/product/architecture-rationale.md` §5.

### 2. Port API ingestion skill if MCP insufficient

### 3. First Confluence space ingest to `raw/workspace-confluence/`

---

## Critical context (do not violate)

1. **Scope discipline.** Governance + closure + vendor-truth band only. See `product-brief.md` §1.2 and §8.1 Risk 7.

2. **Lane discipline.** Platform research outputs do not directly mutate workspace standards, PRD, roadmap, or `AGENTS.md` without user-approved ADR implementation. Workspace operations do not read platform research by default.

3. **Closure rule.** Published artifacts are jr-engineer-executable; no body wikilinks at review/published.

4. **Retrieval (RC-001).** Page-index / structure-aware retrieval is default—not embedding similarity alone.

5. **Citation (RC-002).** Retrieved context is not citation support; `align-cite` gates publish.

6. **Approval gates.** Ingest, sync, archive, remove, publish require explicit user approval.

7. **No telemetry.**

8. **Self-contained shipped files.** No runtime dependency on `build-inputs/`.

9. **Brief is the user's domain.** Do not modify `product-brief.md` without explicit user request.

10. **Surface decisions before acting** on operational spec changes (unless user directed implementation from an approved ADR).

---

## Locked decisions (from planning + May 2026 platform ADRs)

- Karpathy three-layer + Cole compiler refinements
- GitHub repo distribution; per-agent shims
- Atlassian Cloud Enterprise (Confluence; Jira v1.x)
- Obsidian reader; personal wiki per user
- CEO operator persona populated; other personas v1.x
- Multi-agent chain: CEO → VP → PM → Architect → Engineer; finalize in engineer-agent
- Three-state lifecycle; cross-project dependency rules
- Page-index retrieval default (RC-001); citation≠similarity (RC-002)
- Platform research artifact package + implementation priority loop (RC-014)
- Trust loop on platform research artifacts (RC-010)
- Vendor truth: defuddle, 90-day TTL, 365-day hard max
- Embeddings: holdout-gated per RC-001; not default for v1
- Graph projection RC-007/008: deferred; Obsidian graph preferred

---

## Open questions deferred to build time

- Atlassian MCP validation on user's Enterprise tenant (Phase 1 — **now**)
- Markdown-to-HTML library (Phase 5)
- Markdown-to-Confluence-storage-format library (Phase 5)
- Hook adaptation if Copilot session events do not fire (Phase 1)

---

## Known cleanup items

- Legacy duplicate prompts without `workspace-` prefix (Phase 3/7)
- `research-review/` vs `platform-research-review/` prompt trees — consolidate when convenient
- `docs/style/exemplar-published-doc.md` formatting polish (Phase 6)
- `build-inputs/plugins/ai-team-orchestration/` duplicate — manual delete if still present

---

## Where things live

| What | Where |
|---|---|
| This handoff | `HANDOFF.md` |
| Operating spec | `AGENTS.md` |
| Phase plan | `docs/product/roadmap.md` |
| Platform backlog | `wiki/platform-research/implementation-backlog.md` |
| Workspace prompts | `.github/prompts/workspace-*.prompt.md` |
| Platform prompts | `.github/prompts/platform-research-review*`, `.github/prompts/platform-transcript-librarian.prompt.md` |
| Transcript register (tracked) | `wiki/platform-research/transcript-register.md` |
| Platform lint | `scripts/lint-platform-research.py` |
| Config templates | `config/second-brain.example.yml`, `config/platform-research-review.example.yml` |
| Runtime output (gitignored) | `raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/` |

---

## First action

**Workspace lane:** Confirm Phase 3 project intent with the user; run `/workspace-start-project`. Do not block on Confluence.

**Platform lane:** Read `wiki/platform-research/transcript-register.md`, `implementation-backlog.md`, and `open-hypotheses.md` (local). Use `/platform-transcript-librarian` for import/queue; `/platform-research-review` for claim review; implementation from **user-approved** ADRs only.
