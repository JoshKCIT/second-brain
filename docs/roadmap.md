# Roadmap

**Status:** v1.1 (revalidated)
**Last updated:** 2026-05-27
**Current phase:** Phase 2 — Wiki layer and compile (Phase 1A complete; Phase 1B blocked)

The phase plan aligns with `PRD.md` §9.3. Platform foundation work (May 2026) is complete. **Confluence ingest (Phase 1B) is blocked until Atlassian access.** Vendor doc cache (Phase 1A) is the active build track. See `docs/vendor-catalog.md`.

---

## Platform foundation (May 2026) — complete

Transcript-driven platform improvements shipped before the v1 workspace build. These constrain *how* Phases 2–4 run but do not replace ingest, compile, or end-to-end project delivery.

### Done

| Area | Deliverables |
|------|----------------|
| Platform research review | `/platform-research-review` prompt tree, `.github/skills/platform-research-review/`, Cursor `platform-research-reviewer` agent |
| Artifact package + priority loop | `wiki/platform-research/{claim-register,rejected-ideas,open-hypotheses,implementation-backlog,transcript-analyses}/`, `templates/platform-research/` |
| Lint + tests | `scripts/lint-platform-research.py`, `tests/platform_research/` |
| Config | `config/platform-research-review.example.yml` |
| Accepted ADRs | RC-014 (artifacts), RC-010 (trust loop), RC-001 (page-index retrieval), RC-002 (citation ≠ similarity), RC-015 (intent records, experiment), RC-003 (controlled gap review, experiment), implementation-priority-loop |
| Canonical policy | `AGENTS.md`, `PRD.md` (retrieval), `docs/architecture-rationale.md`, `workspace-query.prompt.md` |

### Active experiments (non-blocking)

| ID | Hypothesis | Next action |
|----|------------|-------------|
| H-001 | Monthly platform gap-review finds useful candidates | Run `/platform-gap-review` when ready |
| H-005 | Lightweight intent/safety records improve ADR auditability | Apply template on next 3 platform ADRs |

### Deferred / blocked (platform backlog)

| Claim | Status | Re-enter when |
|-------|--------|---------------|
| RC-007, RC-008 | deferred | Obsidian graph / Bases insufficient for relationship review |
| RC-012 | blocked | Real lint/align/publish failure traces exist |
| RC-005, RC-011 | deferred | v2 scope or v1 pilot usage exists |

Implementation queue: **idle** (all queued PIC cycles through RC-003 accepted or deferred).

---

## v1 workspace build (10–14 weeks)

### Phase 1A: Vendor documentation bootstrap (week 1–2) — **COMPLETE** (2026-05-28)

**Unblocked without Confluence.** Vendor stack: **AWS, Snowflake, Informatica** (IBM Db2 z/OS skipped).

**Exit report:** `docs/phase-1a-exit-report.md`

**Deliverables:**

- [x] `scripts/verify-setup.py` — creates runtime dirs, initializes `wiki/index.md` and `wiki/log.md`; **Atlassian check optional**
- [x] Setup health checks: `python -m unittest discover -s tests` and `python scripts/lint-platform-research.py --root .`
- [x] `scripts/seed-vendor-docs.py`, `scripts/revalidate-vendor-docs.py`, `config/vendor-seed-stack.yml`
- [x] `defuddle` on PATH (Windows: `defuddle.cmd` via npm global; see `scripts/_vendor_fetch.py`)
- [x] `config/second-brain.yml` with `vendor_sources.enabled` (aws, snowflake, informatica)
- [x] **15** vendor topics cached under `raw/workspace-external/`
- [x] Revalidation dry-run (`python scripts/revalidate-vendor-docs.py --dry-run`) — all fresh
- [x] Starter concepts compiled (2): snowflake S3 storage integration, AWS S3 SSE
- [x] align-vendor-truth dry run: `reports/workspace-align-vendor-truth-phase-1a-dry-run-2026-05-28.md`
- [x] Hooks: **deferred** (documented in exit report; Copilot session events not verified)

**Exit:** Met. See `docs/phase-1a-exit-report.md`.

**Start checklist:**

1. `defuddle` installed
2. `config/second-brain.yml` copied; `vendor_sources.enabled` lists vendors you use
3. Pick 3–5 concrete doc URLs to cache (per project or stack you are documenting)

---

### Phase 1B: Atlassian / Confluence ingest (blocked)

**Blocked until:** user has Confluence space read access and credentials.

**Deliverables:**

- [ ] Atlassian Remote MCP Server validation spike (5–10 page test space)
- [ ] Port Confluence ingestion skill if MCP insufficient
- [ ] First small Confluence space ingested to `raw/workspace-confluence/`
- [ ] `.env` Atlassian fields; `verify-setup.py` full mode with connectivity test

**Exit:** one Confluence space ingested end-to-end; path (MCP vs API) documented in `docs/progress-log.md`.

**Note:** Atlassian **product** docs (developer.atlassian.com) are `vendor:atlassian` and can be cached in Phase 1A. Company Confluence **spaces** are internal workspace sources (Phase 1B).

---

### Phase 2: Wiki layer and compile workflow (week 3–4) — **ACTIVE**

**Policy dependency (RC-001):** `wiki/index.md` and Base views in `wiki/workspace-views/` are the v1 retrieval substrate—not optional catalog polish.

**Deliverables:**

- [x] `wiki/` directory layout (placeholders; platform-research content exists)
- [x] `wiki/index.md` and `wiki/log.md` initialized (update on every compile ongoing)
- [ ] `wiki/workspace-views/` Base files for active projects, standards, stale vendor docs
- [ ] `workspace-compile.prompt.md` verified with `obsidian-markdown` on real ingest output
- [ ] Quarantine folder behavior exercised
- [ ] Post-ingest manifest UX
- [ ] Frontmatter schema validation
- [ ] Workspace lint scaffold (structural checks 1–7 from `AGENTS.md`; distinct from `lint-platform-research.py`)

**Exit:** wiki layer coherent with index, log, Base views, and zero structural workspace lint errors. **Without Confluence:** exit using vendor compile + manual/internal articles; **with Confluence:** ~100-page ingest is the full bar.

---

### Phase 3: Query and agent chain skeleton (week 5–6)

**Deliverables:**

- [x] `workspace-query.prompt.md` (index-guided; RC-001/002 policy in prompt)
- [x] Agent prompts: `workspace-vp-agent`, `workspace-pm-agent`, `workspace-architect-agent`, `workspace-engineer-agent`
- [x] `workspace-start-project.prompt.md` orchestration
- [ ] Finalize step exercised (sub-step in `workspace-engineer-agent`; no standalone `finalize.prompt.md`)
- [ ] Project lifecycle: status field, draft → review transitions on a real project
- [ ] Cross-project dependency rules in workspace lint
- [ ] First end-to-end project run (small internal initiative)
- [ ] Legacy prompt cleanup: treat `workspace-*` as canonical; retire or alias duplicate `*.prompt.md` names without `workspace-` prefix

**Exit:** one project completed via the agent chain; CEO operator confirms the workflow is usable.

---

### Phase 4: Alignment and vendor truth (week 7–8)

**Policy dependency (RC-002, RC-010):** retrieved context is not citation support; align reports should support trust-loop fields where applicable.

**Deliverables:**

- [ ] `workspace-align-cite` at production quality (gating before publish)
- [ ] `workspace-align-vendor-truth` at production quality
- [ ] `workspace-align-closure` at production quality
- [ ] `workspace-align-conformance` and `workspace-align-coverage` (best-effort tier)
- [ ] `defuddle` skill integration for vendor doc fetch
- [x] `workspace-revalidate-vendor-docs` prompt
- [ ] TTL behavior verified end-to-end

**Exit:** align-cite passes on a project's full artifact set; align-vendor-truth catches a planted contradiction.

---

### Phase 5: Publish, archive, and Bases integration (week 9–10)

**Note:** RC-007/008 (custom graph projection) deferred; Obsidian graph + Bases remain the v1 navigation story.

**Deliverables:**

- [x] `workspace-publish`, `workspace-prepare-for-confluence`, `workspace-publish-to-confluence` prompts (refine Markdown → storage-format conversion)
- [x] `workspace-archive`, `workspace-unarchive` prompts
- [ ] `obsidian-bases` skill integration; live `wiki/workspace-views/` Base files
- [ ] Markdown-to-Confluence-storage-format library chosen and wired

**Exit:** one project published to Confluence successfully; Bases views render in Obsidian.

---

### Phase 6: Persona templates, exemplar, polish (week 11–12)

**Deliverables:**

- [x] `templates/personas/ceo/` populated (`AGENTS-additions.md`, `example-prompts/`, `starter-wiki/`)
- [x] Engineer, Architect, PM, Director, VP stubs (READMEs; v1.x population)
- [ ] `docs/style/exemplar-published-doc.md` cleaned and finalized
- [ ] README, setup-kit, adoption-checklist polished against real pilot
- [ ] End-to-end pilot with a real project (may overlap Phase 3 exit)
- [ ] `product-brief.md` gaps (`[NEEDS INPUT]` sections) filled where blocking adoption narrative

**Exit:** a new clone can be set up and the first project run within ~30 minutes of starting (per adoption checklist).

---

### Phase 7: Buffer (week 13–14)

- ADF macro coverage long tail
- Workspace lint quality tuning (separate from platform research lint)
- Documentation polish
- Pilot feedback incorporated
- Resolve duplicate prompt trees (`research-review/` vs `platform-research-review/` if still redundant)
- Optional ADR filename hygiene (`DRAFT-*` → accepted naming)
- Run platform gap-review (H-001) after first real ingest/pilot if not done earlier

**Exit:** v1 release.

---

## v1.x (post-v1, prioritized)

- Jira ingestion (using `atlassian-requirements-to-jira` agent pattern from `build-inputs/`)
- Pre-ingestion of vendor doc **bundles** via vendor MCPs (AWS, Snowflake, Terraform MCP) where configured — complements Tier A URL cache (`docs/vendor-catalog.md`)
- Google Drive / SharePoint / OneNote as **internal** content sources (not `vendor:*`)
- SharePoint and OneNote ingestion
- Population of Engineer, Architect, PM, Director, VP persona templates
- `align-conformance` and `align-coverage` at production quality (labeled standards or rule-based extraction)
- Atlassian Remote MCP Server as the primary ingest path (if Phase 1 spike validates and user prefers)
- Custom chat-participant extension for `/second-brain` slash command
- Workflow automations (`build-inputs/workflows/`): scheduled Confluence sync, vendor doc revalidation
- `obsidian-cli` skill adoption for live-update workflows
- **Embeddings / hybrid retrieval:** holdout-gated per RC-001—only adopt if evaluation shows improved citation precision and inspectability without weakening junior-engineer closure; page-index remains default
- Monthly `/platform-gap-review` as recurring maintenance (RC-003 experiment)
- RC-012 advisory harness failure review when failure traces accumulate
- RC-011 local weekly digest from `wiki/log.md` (after v1 pilot usage exists)

## v2 candidates

- Multi-user / shared wiki with merge protocols (RC-005 deferred here)
- Confluence write-back (edits to existing pages, not just new)
- Mobile or web UI
- Code-as-source (ingest a repo as a knowledge source)
- Cross-tenant federation (read from multiple Atlassian Cloud tenants)
- Custom disposable graph projection (RC-007/008) if Obsidian graph is insufficient
