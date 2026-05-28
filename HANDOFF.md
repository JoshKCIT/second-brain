# HANDOFF.md — Build handoff to VS Code + GitHub Copilot

This document tells the next agent session (VS Code with GitHub Copilot in agent mode) what state Second Brain is in, what to build first, what to read for context, and what guardrails apply. Read this first, then follow the pointers below.

---

## Read these in order

1. `.github/copilot-instructions.md` — your shim and operating instructions for this repo
2. `AGENTS.md` — canonical operating spec (longer; comprehensive)
3. `product-brief.md` — problem statement, scope, constraints, decisions log
4. `PRD.md` — what v1 builds (functional requirements, user stories, milestones)
5. `docs/roadmap.md` — phase plan; **current phase: Phase 1A (vendor docs)**; Phase 1B (Confluence) blocked
6. `docs/vendor-catalog.md` — vendor slugs, doc roots, Tier A/B/C integration
7. `docs/architecture-rationale.md` — why the architectural choices were made
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

### v1 workspace build — Phase 1A active (vendor docs; no Confluence required)

The repo contains planning and scaffolding for workspace operations:

- **Top-level:** `README.md`, `AGENTS.md`, `CLAUDE.md`, `PRD.md`, `product-brief.md`, `.windsurfrules`, `.env.example`, `.gitignore`, `HANDOFF.md`
- **Per-agent shims:** `.github/copilot-instructions.md`, `.cursor/rules/agents.mdc`, `CLAUDE.md`, `.windsurfrules`
- **Workspace prompts:** `workspace-*` verbs in `.github/prompts/` (ingest, compile, query, align, publish, archive, lint, agent chain, onboarding)
- **Platform prompts:** `platform-research-review/` tree + `platform-research-review.prompt.md`
- **Skills:** `obsidian-markdown`, `obsidian-bases`, `defuddle`, `platform-research-review`
- **Agents:** `workspace-adr-generator.agent.md`; Cursor `platform-research-reviewer`
- **Hooks:** `secrets-scanner`, `tool-guardian`, `session-logger`, `governance-audit` — ported, **not verified** for Copilot (Phase 1)
- **Config:** `config/second-brain.example.yml`, `config/platform-research-review.example.yml`
- **Personas:** `templates/personas/ceo/` **populated**; other personas are v1.x stubs
- **Scripts:** `scripts/lint-platform-research.py` (no `verify-setup.py` yet)
- **Wiki:** layout placeholders + `wiki/platform-research/` content; **no** `wiki/index.md` or `wiki/log.md` yet

### What is NOT yet done (v1 blockers)

- `scripts/verify-setup.py` — Phase 1A deliverable (Atlassian optional)
- Vendor doc seed caches under `raw/workspace-external/` — Phase 1A exit
- Atlassian / Confluence — **Phase 1B, blocked** until user has space access
- Hook verification or documented deferral — Phase 1A
- `wiki/index.md`, `wiki/log.md`, workspace compile on vendor raw pages — Phase 2
- Workspace structural lint (checks 1–7) — Phase 2
- End-to-end project through agent chain — Phase 3
- Exemplar final polish — Phase 6

---

## Phase 1A — vendor bootstrap (ready to start)

Per `docs/roadmap.md` Phase 1A and `docs/vendor-catalog.md`:

### 0. Confirm start checklist with the user

- `defuddle` installed (`npm install -g defuddle`)
- `config/second-brain.yml` with `vendor_sources.enabled` (AWS, Azure, GCP, Snowflake, etc.)
- 3–5 specific vendor doc URLs to cache for the user's current doc buildout
- **No Confluence required**

### 1. Write `scripts/verify-setup.py` (highest priority)

Specification:

- Creates required runtime directories per `AGENTS.md` layout
- Initializes `wiki/index.md` and `wiki/log.md` if missing (structure in `AGENTS.md`)
- Validates `config/second-brain.yml` exists (or guides copy from example)
- If `atlassian.enabled` is true in config, validate `.env` and test Atlassian connectivity; otherwise skip with clear message
- Prints a success summary with what was created and verified
- Document that setup health also expects: `python -m unittest discover -s tests` and `python scripts/lint-platform-research.py --root .`

Reference: `docs/setup-kit.md`.

### 2. Seed vendor documentation caches

For each user-approved URL, run `/workspace-ingest-vendor-doc` (vendor slug, topic, URL). Targets listed in `docs/vendor-catalog.md`.

### 3. Verify hook compatibility

Per `.github/hooks/README.md`. If hooks do not fire in Copilot's prompt-driven model, document the gap in `docs/progress-log.md` and propose prompt-invoked alternatives.

### 4. Exercise revalidation

Run `/workspace-revalidate-vendor-docs` (dry-run first). Document behavior in `docs/progress-log.md`.

### 5. Append `docs/progress-log.md`

Log Phase 1A exit: verify-setup pass, vendor cache count, vendors enabled.

---

## Phase 1B — Confluence (when access is available)

Defer until user has Atlassian credentials and a test space.

### 1. Spike the Atlassian Remote MCP Server

**Goal:** validate whether the MCP exposes the page metadata Second Brain needs (ADF body, version, last_modified, labels, ancestors, attachments, source_url, page_id, space_key). See `docs/architecture-rationale.md` §5.

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
| Phase plan | `docs/roadmap.md` |
| Platform backlog | `wiki/platform-research/implementation-backlog.md` |
| Workspace prompts | `.github/prompts/workspace-*.prompt.md` |
| Platform prompts | `.github/prompts/platform-research-review*` |
| Platform lint | `scripts/lint-platform-research.py` |
| Config templates | `config/second-brain.example.yml`, `config/platform-research-review.example.yml` |
| Runtime output (gitignored) | `raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/` |

---

## First action

Confirm Phase 1A checklist (`defuddle`, vendor list, seed URLs). Implement `verify-setup.py` and seed vendor caches. Do not block on Confluence. When the user gains Atlassian access, open Phase 1B per `docs/roadmap.md`.
