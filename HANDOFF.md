# HANDOFF.md — Build handoff to VS Code + GitHub Copilot

This document tells the next agent session (VS Code with GitHub Copilot in agent mode) what state Second Brain is in, what to build first, what to read for context, and what guardrails apply. Read this first, then follow the pointers below.

---

## Read these in order

1. `.github/copilot-instructions.md` — your shim and operating instructions for this repo
2. `AGENTS.md` — canonical operating spec (longer; comprehensive)
3. `docs/product-brief.md` — problem statement, scope, constraints, decisions log
4. `docs/PRD.md` — what v1 builds (functional requirements, user stories, milestones)
5. `docs/roadmap.md` — phase plan (your build sequence)
6. `docs/architecture-rationale.md` — why the architectural choices were made
7. `docs/progress-log.md` — where the planning session left off; where you append your sessions

---

## Current state (planning complete)

The repo contains:

- **Top-level:** `README.md`, `AGENTS.md`, `CLAUDE.md`, `PRD.md`, `product-brief.md`, `.windsurfrules`, `.env.example`, `.gitignore`, `HANDOFF.md` (this file)
- **Per-agent shims:** `.github/copilot-instructions.md`, `.cursor/rules/agents.mdc`, plus `CLAUDE.md` and `.windsurfrules` at root
- **17 prompts** in `.github/prompts/`: orchestration (`start-project`), agent chain (`vp-agent`, `pm-agent`, `architect-agent`, `engineer-agent`), align (`align-cite`, `align-vendor-truth`, `align-closure`, `align-conformance`, `align-coverage`), ingest (`ingest-confluence`, `ingest-vendor-doc`), `compile`, `query`, publish (`publish`, `prepare-for-confluence`, `publish-to-confluence`), lifecycle (`archive`, `unarchive`), `lint`, onboarding (`second-brain`)
- **1 specialized agent** in `.github/agents/`: `adr-generator.agent.md`
- **3 skills** in `.github/skills/`: `obsidian-markdown`, `obsidian-bases`, `defuddle` (copied from `build-inputs/skills/`)
- **4 hooks** in `.github/hooks/`: `secrets-scanner`, `tool-guardian`, `session-logger`, `governance-audit` — **PORTED BUT NOT VERIFIED for Copilot compatibility** (your Phase 1 task; see `.github/hooks/README.md`)
- **docs/**: `product-brief.md`, `PRD.md`, `architecture-rationale.md`, `roadmap.md`, `setup-kit.md`, `adoption-checklist.md`, `progress-log.md`, `style/exemplar-published-doc.md`
- **config/**: `second-brain.example.yml` (template tracked; user's `second-brain.yml` is gitignored)
- **templates/personas/**: `ceo/` populated (with `AGENTS-additions.md`, `example-prompts/`, `starter-wiki/`); `engineer/`, `architect/`, `product-manager/`, `director/`, `vp/` are documented stubs for v1.x population
- **Runtime content directories** (gitignored content): `raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/` will be created by `verify-setup.py`

## What is NOT yet done

- `scripts/verify-setup.py` does not exist yet — you write it in Phase 1
- Atlassian Rovo MCP Server has not been validated on the user's Enterprise tenant — this is your Phase 1 spike
- Hook compatibility with Copilot's session event model has not been verified
- The exemplar at `docs/style/exemplar-published-doc.md` was cleaned of stray bold artifacts but is otherwise unedited; may need formatting polish before final use
- No Confluence content has been ingested
- No project has been run through the agent chain end-to-end

---

## Build week 1 (Phase 1) — your first session

Per `docs/roadmap.md` Phase 1, in order of priority:

### 1. Spike the Atlassian Rovo MCP Server (highest priority)

**Goal:** validate whether the MCP exposes the page metadata Second Brain's wiki layer needs.

**Required metadata per page:** ADF body content (or sufficient equivalent), version number, last_modified timestamp, labels, ancestors, attachments references, source_url, page_id, space_key.

**Procedure:**

1. Ask the user for MCP server configuration (URL, auth approach for their tenant)
2. Configure in `.env` (extend `.env.example` with the MCP fields if needed)
3. Pick a small test space (5-10 pages) the user designates
4. Use the MCP to fetch one page; verify the response contains all required metadata
5. **If MCP provides everything:** proceed with MCP-first ingestion path; wire `ingest-confluence.prompt.md` to use MCP tools
6. **If MCP is insufficient:** identify exactly what is missing or filtered; fall back to porting the user's existing API-based Confluence ingestion skill (Step 4 below)

Decision rationale: `docs/architecture-rationale.md` §5.

### 2. Write `scripts/verify-setup.py`

Specification:
- Validates `.env` is present and Atlassian credentials parse
- Creates required runtime directories (`raw/confluence/`, `raw/external/`, `wiki/standards/`, `wiki/concepts/`, etc., per the layout in `AGENTS.md`)
- Initializes `wiki/index.md` and `wiki/log.md` if missing (with the structure documented in `AGENTS.md`)
- Tests Atlassian connectivity (one read-only API call against the configured tenant)
- Prints a success summary with what was created and verified

Reference: `docs/setup-kit.md` describes what setup verification should accomplish from the user's perspective.

### 3. Verify hook compatibility

The four ported hooks target Copilot's session event model (`sessionStart`, `sessionEnd`, `preToolUse`, `userPromptSubmitted`). Verify each fires as expected during the prompt-driven workflow described in `AGENTS.md`.

Per `.github/hooks/README.md`, the verification checklist:
- `secrets-scanner` fires at `sessionEnd` and catches a planted test secret
- `tool-guardian` blocks a planted destructive command at `preToolUse`
- `session-logger` writes to `wiki/log.md` (will require adaptation; default writes to a generic logs directory)
- `governance-audit` is verified or explicitly deferred to v1.x

If hooks do not fire as expected in Copilot's prompt-driven model, document the gap in `docs/progress-log.md` and propose an alternative (e.g., adapt the hook scripts as Python modules invoked by prompts rather than fired by session events).

### 4. Port the user's API ingestion skill (only if MCP spike fails or has gaps)

If Step 1 showed MCP cannot provide complete metadata:

- Get the user's existing skill code (ask)
- Port into the repo (likely under `scripts/` or invoked by `.github/prompts/ingest-confluence.prompt.md`)
- Adapt the output format to match the frontmatter schema in `AGENTS.md` (source_url, space_key, page_id, version, content_hash, authority, domain, etc.)
- Confirm the ported skill produces files matching `raw/confluence/{space-key}/pages/{page-id}--{slug}.md`

### 5. Update `docs/progress-log.md`

After each session, append an entry per the format already in the file:

```
## [YYYY-MM-DD] session | short title
- Changed:
- Open:
- Next:
```

---

## Critical context (do not violate)

1. **Scope discipline.** Do not build generic enterprise search, Q&A, multi-step agents without governance, IDE codebase chat, or basic page templates. Those are covered by Rovo, Glean, Microsoft Copilot, Notion AI, and Sourcegraph Cody. Second Brain targets governance + closure + vendor-truth band only. The capability table in `product-brief.md` §1.2 and §8.1 Risk 7 are the canonical scope filter. Reject any feature request that does not fall in the governance band.

2. **Closure rule.** Project artifacts at `published` status must be jr-engineer-executable using only the artifact set. No body wikilinks at review or published. Vendor citations use parenthetical + See Also link pattern. Internal standards: inline relevant rules in body + provide Confluence URL in See Also.

3. **Authority + domain tagging.** Every source has `authority` (standard/recommendation/informational) and `domain` (internal/vendor:X/industry:Y). Vendor claims cite vendor sources; internal claims cite internal sources. Conflicts resolved by claim domain (vendor-vs-internal arbitration).

4. **Approval gates.** Ingestion, sync, archive, remove, publish all require explicit user approval after diff or preview. Never silently mutate.

5. **No telemetry. No phone-home. No analytics.**

6. **Self-contained shipped files.** Do not add references from shipped files (`.github/`, `docs/`, `config/`, `templates/`, repo-root files) back to `build-inputs/`. The shipped repo must work standalone after `build-inputs/` is deleted.

7. **The user is the CEO operator.** Tone of all interactions: direct, terse, technical. Skip pleasantries; surface substantive answers first.

8. **Brief is the user's domain.** `docs/product-brief.md` is currently at v0.1 with several updates applied during planning. Do not modify it without explicit user request. The PRD, AGENTS.md, README, and architecture-rationale carry the operational decisions and are canonical for build behavior.

9. **Surface decisions before acting.** If you propose changing AGENTS.md, prompts, or any `docs/` file, surface the proposed change to the user via Copilot chat first. Do not silently update operational specs.

---

## Locked decisions (from planning conversation)

- **Pattern:** Karpathy three-layer (raw + curated wiki + schema) + Cole compiler refinements (two-stage extraction, formalized article types, structured index/log, lint, state tracking)
- **Distribution:** GitHub repo, clone-and-run; per-agent shims for Copilot, Claude Code, Cursor, Windsurf
- **Source:** Atlassian Cloud Enterprise tier (Confluence + Jira on same tenant; Jira ingestion deferred to v1.x)
- **Reader:** Obsidian (bundled `.obsidian/` config in repo)
- **Wiki:** personal, per user (not shared)
- **Persona model:** CEO operator (literal user) fully populated; 5 stub personas (Engineer, Architect, PM, Director, VP) for v1.x population
- **Multi-agent workflow:** CEO → VP → PM → Architect → Engineer; CEO reviews between stages
- **Three-state project lifecycle:** in-progress (draft, review) → published → archived; in-progress projects cannot reference other in-progress or archived projects
- **Closure rule** with status-aware lint (body-prose-clean at review and published)
- **Vendor citation pattern:** parenthetical attribution + See Also link
- **Internal standard pattern:** inline relevant rules + Confluence URL in See Also
- **Three align levels in v1:** `align-cite` (production), `align-conformance` and `align-coverage` (best-effort with documented quality tier); plus `align-vendor-truth` and `align-closure` (production)
- **Vendor truth handling:** fetch-on-demand via `defuddle`, cache to `raw/external/`, 90-day TTL default, 365-day hard max
- **Confluence sync cadence:** weekly default; reminder after 7 days
- **Publish flow:** branch on review (HTML to `confluence-review/`) vs Confluence (MCP primary if validated, API fallback)
- **Embeddings deferred:** revisit only if wiki passes ~500 articles
- **Plugin policy:** zero VS Code or Obsidian plugins required for v1
- **`/second-brain` invocation:** via prompt file, not chat participant extension
- **Naming:** Second Brain
- **Build calendar:** 10-14 weeks for v1
- **Build budget:** no monthly ceiling; TTL and sync cadence shape spend
- **Five kill criteria** documented in `product-brief.md` §7.3

## Open questions deferred to build time

- Atlassian Rovo MCP Server validation on the user's Enterprise tenant (Phase 1 spike)
- Markdown-to-HTML library for review-folder publish path (Phase 5)
- Markdown-to-Confluence-storage-format library for API publish path (Phase 5)
- Whether to populate the Engineer persona template alongside CEO (currently CEO only; v1.x for others)
- Hook adaptation if Copilot session events do not fire as expected (Phase 1)

## Known cleanup items

- `ai-team-orchestration` plugin duplicate at `build-inputs/plugins/ai-team-orchestration/` is awaiting manual deletion. Windows readonly attributes prevented FUSE-mount delete. The user can delete from Windows file explorer.
- `docs/style/exemplar-published-doc.md` had 220 stray `**bold**` artifacts removed; may have other formatting issues from the original export. Cosmetic only.

---

## Where things live

| What | Where |
|---|---|
| This handoff | `HANDOFF.md` (root) |
| Operating spec | `AGENTS.md` (root) |
| Per-agent shims | `.github/copilot-instructions.md`, `CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules` |
| Reusable prompts (verbs) | `.github/prompts/*.prompt.md` |
| Reusable skills | `.github/skills/{obsidian-markdown,obsidian-bases,defuddle}/SKILL.md` |
| Specialized agents | `.github/agents/adr-generator.agent.md` |
| Safety hooks (verify before relying) | `.github/hooks/{secrets-scanner,tool-guardian,session-logger,governance-audit}/` |
| Planning docs | `docs/{product-brief,PRD,architecture-rationale,roadmap,setup-kit,adoption-checklist,progress-log}.md` |
| Writing-style exemplar | `docs/style/exemplar-published-doc.md` |
| Config template | `config/second-brain.example.yml` |
| User's local config (gitignored) | `config/second-brain.yml` |
| Persona templates | `templates/personas/{ceo (populated), engineer, architect, product-manager, director, vp}/` |
| Source materials (planning-time only; do NOT depend on at runtime) | `build-inputs/` |
| Runtime output (gitignored, created by verify-setup) | `raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/` |

---

## How to operate

1. Read this file. Then read the rest of the "Read these in order" list above.
2. Follow the Phase 1 → Phase 7 plan in `docs/roadmap.md`.
3. Append to `docs/progress-log.md` at the end of every session with what changed, what is open, and what is next.
4. Surface proposed changes to operational files (AGENTS.md, prompts, agents, docs) to the user before applying.
5. When a feature request comes in, classify it: governance-band (consider) or generic-band (decline or punt to the appropriate alternative tool). The capability table in `product-brief.md` §1.2 is the filter.
6. When in doubt, re-read `AGENTS.md`. It is the canonical operating spec.

---

## First action

Greet the user. Tell them what you just read (this file + AGENTS.md + product-brief.md + roadmap.md). Ask them to share their Atlassian Rovo MCP Server configuration so you can run the Phase 1 spike. Do not start ingesting Confluence content until the spike completes and the data-layer path is locked.
