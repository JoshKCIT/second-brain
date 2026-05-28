# AGENTS.md - Second Brain Operating Spec

> Canonical schema and operating instructions for any AI coding agent (Copilot, Claude Code, Cursor, Windsurf, Codex CLI, etc.) working with this repo. Per-agent shim files (`.github/copilot-instructions.md`, `CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules`) reference this document for full content. If you are an agent reading a shim, also read this file.

## Purpose

Second Brain is a personal knowledge base maintained by an LLM, sourced from the user's organizational documentation (Confluence first; Jira and others later) plus on-demand vendor documentation, and used to author new project documentation that is grounded in canonical sources and executable by a junior engineer using only the published artifact set.

This document tells you how the system is structured, how to ingest content, how to maintain the wiki layer, how to author project artifacts, how to verify alignment and closure, and how to publish.

## Scope discipline

Target band: governance-and-closure. The capabilities Second Brain implements:

- Claim-domain authority and vendor truth arbitration
- Vendor truth validation with TTL-cached vendor docs
- Junior-engineer-executable closure rule (published artifact set must be self-sufficient)
- Multi-page stage-gated technical-doc generation with Confluence-storage-format output
- Mandatory section-level citation discipline across multi-page artifacts
- Inspectable retrieval enforced before generation as policy
- Project artifact lifecycle (in-progress / published / archived) with cross-project dependency rules

Out of scope (covered by alternatives such as Rovo, Glean, Microsoft Copilot for M365, Notion AI, Sourcegraph Cody): generic enterprise search, Q&A, multi-step agents without governance constraints, IDE-integrated codebase chat, basic page templates.

When the user asks for a feature, classify it as governance-band or generic-band. Generic-band requests should be declined or punted to the appropriate alternative tool. Governance-band requests can be considered. The `product-brief.md` §1.2 capability table and §8.1 Risk 7 are the canonical scope filter.

---

## The compiler analogy

Adapted from Cole's claude-memory-compiler:

```
raw/                = source code        (immutable input)
LLM (this agent)    = compiler           (extracts and organizes knowledge)
wiki/               = executable         (structured, queryable knowledge base)
align + lint        = test suite         (correctness and closure checks)
queries + drafts    = runtime            (using the knowledge to produce work)
```

The user does not manually organize the wiki. They configure scope, request operations, and review artifacts. You do the synthesis, cross-referencing, citation, alignment checking, and bookkeeping.

---

## Lane vocabulary: platform vs workspace

Second Brain has two explicit operating lanes. Classify the user's task before touching files.

| Lane | Meaning | Use when... | Path prefix |
|---|---|---|---|
| `platform` | Work that improves Second Brain itself | The user provides transcripts, product ideas, competitor research, architecture proposals, or asks how to make Second Brain better | `platform-*` |
| `workspace` | Everyday use of Second Brain for company/project documentation | The user ingests, compiles, queries, aligns, publishes, archives, or authors normal work artifacts from Confluence/vendor sources | `workspace-*` |

Platform-lane evidence may produce claim records, reports, experiments, and draft platform decision records. It must not directly mutate workspace standards, workspace recommendations, workspace projects, the PRD, roadmap, architecture rationale, or `AGENTS.md` without explicit user approval.

Workspace-lane operations must not read platform research outputs by default. Use platform research only when the user explicitly asks to improve Second Brain or review product-intelligence evidence.

---

## Routing map (RC-162)

Task-type → prompt/skill → first read paths. **Orientation only** — does not auto-load content or bypass RC-122/RC-018/align-cite. Full table: `templates/workspace/routing-map.md`.

| Task type | Lane | Invoke | Read first |
|---|---|---|---|
| Onboard / configure | workspace | `second-brain` | `config/second-brain.yml`, `wiki/index.md` |
| Start / resume project | workspace | `workspace-start-project` | `meta.yml`, stage `handoff.md`, `wiki/index.md` |
| Stage agent work | workspace | `workspace-{vp,pm,architect,engineer}-agent` | Stage artifact, `handoff.md`, scoped wiki/raw |
| Thinking-partner exploration | workspace | `workspace-thinking-partner` | Stage `handoff.md`, upstream artifacts |
| Ingest / compile / query | workspace | `workspace-ingest-*`, `workspace-compile`, `workspace-query` | `wiki/index.md`, scoped sources per RC-018 |
| Align / publish / lint | workspace | `workspace-align-*`, `workspace-publish`, `workspace-lint` | Target artifacts + cited paths |
| Session audit | workspace | `workspace-session-audit` | Stage `handoff.md`, `orientation.md` |
| **Platform escalation (PH-006)** | **platform** | **`platform-transcript-librarian` / `platform-research-review`** | **`wiki/platform-research/**` — no protected workspace/PRD edits without approval** |
| Transcript / research / stack-lift | platform | `platform-*`, implementation backlog | Register, claim register, approved ADR |

When workspace work surfaces Second Brain product ideas, **escalate to platform lane** (PH-006); do not promote transcript claims into workspace standards or projects without review.

---

## Instruction stacking (RC-2026-05-27-161)

Agents load rules in three tiers. Lower tiers add scope; they never override Tier 1.

| Tier | Source | Role |
|---|---|---|
| 1 | `AGENTS.md` | Root invariants: approval gates, citation/closure, lane boundaries, fail closed |
| 2 | Lane/stage prompts (`.github/prompts/workspace-*.prompt.md`, `platform-*.prompt.md`) and IDE shims (`.cursor/rules/agents.mdc`, `CLAUDE.md`, `.github/copilot-instructions.md`) | Task-type scope; must declare `inherits: AGENTS.md` in frontmatter |
| 3 | Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds under `wiki/workspace-projects/{slug}/`) | Project/stage scope only; draft-tier unless compiled to wiki |

**Non-overridable (Tier 1):** approval-gated ingest/sync/archive/publish; `align-cite` and `align-closure` before publish; citation-grounded claims; platform research cannot mutate canonical workspace standards/projects/PRD/roadmap/`AGENTS.md` without explicit user approval; scoped retrieval per `config/second-brain.yml`; no secrets in artifacts.

Tier-2 shims and Tier-3 scaffolds must not restate full Tier-1 rule lists—reference `AGENTS.md` and add delta only. Template: `templates/workspace/instruction-stack-header.md`. Routing map: `templates/workspace/routing-map.md` (RC-162). Advisory duplicate-root check: `workspace-lint` check 16.

---

## Architecture: three layers + agent chain

### Three layers

1. **`raw/` - immutable source**
   - `raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md` and `attachments/`
   - `raw/workspace-jira/{project-key}/tickets/` (v1.x)
   - `raw/workspace-external/{vendor}/{topic}/{slug}.md` for cached vendor docs
   - `raw/workspace-inbox/{YYYY-MM-DD}/` for manual clips and unprocessed captures (RC-146)
   - `raw/platform-transcripts/{slug}/transcript.md` for product-intelligence transcripts
   - You read from here; you never modify it after the initial ingest write.

2. **`wiki/` - LLM-curated knowledge**
   - You own this directory entirely. The user reads it; you write it.
   - Subdirectories defined below.

3. **`AGENTS.md` (this file) - the schema**
   - Tells you how to behave. Co-evolves with the user as the project domain develops.

### Agent chain (project workflow)

When the user (CEO) declares a project intent, you orchestrate this chain:

```
CEO declares high-level project intent
   ↓
VP Agent (works with CEO) → wiki/workspace-projects/{slug}/01-vp-brief/product-brief.md
   ↓
PM Agent (uses VP output) → wiki/workspace-projects/{slug}/02-pm-prd/product-requirements.md
   ↓
Architect Agent (if technical) → wiki/workspace-projects/{slug}/03-architecture/architectural-approaches.md
   ↓
Engineer Agent → wiki/workspace-projects/{slug}/04-engineering/{spec-files}.md
   ↓
Engineer-led finalize step → status: review
```

Each workspace agent has a prompt file in `.github/prompts/workspace-{agent}-agent.prompt.md` with role definition, input contract, output contract, source-of-truth scope, and human checkpoint logic.

**Read-before-write (RC-122):** Workspace agents read scoped index/catalog and relevant sources before proposing artifact edits; record consulted paths in frontmatter `sources`. Retrieval precedes generation; `align-cite` still required before publish.

**Session handoff (RC-058):** Optional `handoff.md` per stage directory holds draft-tier restart context (`starting_context`, `next_steps`, `open_decisions`, `last_session`). Agents read on resume; update at session end after CEO confirms. Template: `templates/workspace/handoff.md`. Excluded from finalize and published artifact set.

**Inter-stage output contract (PH-003):** At each CEO gate, the orchestrator forwards **locked decisions** (CEO-confirmed, do not reopen) and **forwarded open decisions** (still unresolved upstream) into the next stage's `handoff.md`. Downstream agents read and honor locks before drafting; address forwarded open items in the stage artifact or escalate. Contract: `templates/workspace/inter-stage-contract.md`. ADR: `docs/platform-decision-records/DRAFT-PH-2026-05-27-003-inter-stage-output-contract.md`.

**Stage evidence scaffold (RC-130):** Optional per-stage folders `research/`, `chats/`, `daily-progress/` plus `handoff.md` for multi-day catch-up. Draft-tier only; excluded from publish set. Template: `templates/workspace/project-stage-scaffold/README.md`.

**Project stage state (PH-001):** `meta.yml` fields `current_stage`, `stage_gate`, and `last_completed` are the authoritative resumability signal. Template: `templates/workspace/project-meta.yml.md`. Orchestrator updates at CEO gates; stage agents read on invoke and set `stage_gate: awaiting_ceo_review` when draft work completes.

**Reopen stage protocol (PH-005):** When the CEO reopens an upstream stage, the orchestrator sets `invalidated_stages` and `reopen_reason` in `meta.yml`, marks downstream project artifacts `invalidated: true` (files retained for audit), and resumes at the target stage. Agents must not cite invalidated artifacts. Protocol: `templates/workspace/reopen-stage-protocol.md`. ADR: `docs/platform-decision-records/DRAFT-PH-2026-05-27-005-reopen-stage-protocol.md`.

**Advisory align-cite per stage (PH-004):** Optional non-blocking citation check on the current stage artifact before each CEO gate. Stage agents or orchestrator invoke `/workspace-align-cite` with `--advisory`; violations are reported but do not block gate progression. Blocking align-cite still runs at pre-publish (Step 12). Protocol: `templates/workspace/advisory-align-cite-per-stage.md`. ADR: `docs/platform-decision-records/DRAFT-PH-2026-05-27-004-advisory-align-cite-per-stage.md`.

**Disposable session orientation (RC-163):** Optional `orientation.md` per stage holds non-canonical session notes and preferences (`not_canonical: true`). Distinct from `handoff.md`; excluded from finalize and publish. Promotion to wiki requires compile + user approval + align-cite. Template: `templates/workspace/orientation.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-163-disposable-session-orientation.md`.

**Thinking vs artifact mode (RC-116):** Optional `agent_mode: thinking | artifact` on draft stage artifacts (default `artifact`). Thinking mode forbids publish-shaped output in artifact bodies; notes go to `orientation.md` or `research/`. Finalize blocks `review` while any artifact remains in thinking mode. Template: `templates/workspace/agent-mode.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-116-thinking-artifact-mode-separation.md`.

**Project sub-scaffold rule stacking (RC-167):** Optional `subprojects/{workstream}/` under a stage with Tier-3 `STAGE-SCAFFOLD.md`, local orientation, and resources. Inherits AGENTS + stage prompt; all sub-scaffold files use `publish_scope: exclude`. Excluded from finalize, align-closure publish set, and publish. Template: `templates/workspace/project-sub-scaffold/README.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-167-project-subfolder-rule-stacking.md`.

**Session audit (RC-164):** Optional end-of-session skill (`.github/skills/session-audit/`) scans conversation and proposes `orientation.md` or `handoff.md` updates. Proposal-only; CEO approves each item before write. Never auto-writes wiki or canonical knowledge. Prompt: `.github/prompts/workspace-session-audit.prompt.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-164-session-audit-skill.md`.

**Thinking-partner sub-agent (RC-117):** Optional interview-style exploration via `.github/prompts/workspace-thinking-partner.prompt.md`. Writes only to `thinking-notes/` (`type: thinking-notes`, `not_canonical: true`); excluded from finalize and publish. Pairs with RC-116 `agent_mode: thinking`. Template: `templates/workspace/thinking-partner.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-117-thinking-partner-subagent.md`.

**Raw inbox staging (RC-146):** Captures land in scoped `raw/` paths (including `raw/workspace-inbox/`); compile into `wiki/` only after explicit user approval per batch. Orphan raw in lint is advisory until compile. Template: `templates/workspace/raw-inbox-staging.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-146-raw-inbox-staging.md`.

**Task-type routing map (RC-162):** Shims and `AGENTS.md` include task → prompt → first-read-path table for workspace and platform lanes. PH-006 platform escalation row routes mid-project product ideas to platform research without protected-file mutation. Template: `templates/workspace/routing-map.md`. ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-162-routing-map-agents-shim.md`.

CEO reviews and edits between stages. Do not invoke the next agent without explicit CEO approval.

---

## Source authority and domain

Every source carries two tags:

### Authority levels

| Level | Meaning |
|---|---|
| `standard` | Authoritative; takes precedence in conflicts |
| `recommendation` | Strong guidance; can be overridden with reason |
| `informational` | Background context; not binding |

### Domains

| Domain | Authoritative for... | Examples |
|---|---|---|
| `internal` | Internal architecture, decisions, patterns, runbooks | Architecture team space, SRE runbooks |
| `vendor:{name}` | What the named vendor's product can do | `vendor:aws`, `vendor:snowflake`, `vendor:atlassian` |
| `industry:{name}` | Regulatory, compliance, or industry norms | `industry:nist`, `industry:hipaa` |

### Conflict resolution rule

**The source authoritative for the claim's domain wins.** If internal docs say "S3 cannot be encrypted" and AWS docs say it can, AWS wins because the claim is a vendor capability. The internal doc is flagged as outdated by `align-vendor-truth`.

When citing in generated artifacts:
- Internal architecture claims: cite internal sources (Architecture, Security, Audit, etc.)
- Vendor capability claims: cite vendor docs from `raw/workspace-external/{vendor}/`
- Compliance claims: cite industry standards

---

## Article types in `wiki/`

```
wiki/
├── index.md              # Master catalog; Obsidian home; embeds Base views
├── log.md                # Append-only chronological build log
├── workspace-standards/            # Authority: standard
├── workspace-recommendations/      # Authority: recommendation
├── workspace-informational/        # Authority: informational (default for ungraded)
├── workspace-concepts/             # Atomic knowledge articles compiled from workspace raw sources
├── workspace-connections/          # Cross-cutting insights linking 2+ concepts
├── workspace-qa/                   # Filed query answers (compounding knowledge)
├── workspace-projects/{slug}/      # Project-specific artifact sets (per-stage subdirs)
├── workspace-archives/             # Completed and deprecated content (excluded from default search)
├── workspace-views/                # Obsidian Base files for live navigation
└── platform-research/              # Transcript-derived platform intelligence; not canonical workspace knowledge
```

### Concept article (`wiki/workspace-concepts/{slug}.md`)

```markdown
---
title: "Concept Name"
type: concept
authority: standard | recommendation | informational
domain: internal | vendor:aws | industry:nist | ...
aliases: [alternate-name]
tags: [domain, topic]
sources:
  - "raw/workspace-confluence/SECURITY/pages/12345--encryption-at-rest.md"
status: published
created: 2026-04-28
updated: 2026-04-28
---

# Concept Name

[2-4 sentence core explanation]

## Key Points

- [Self-contained bullet points]

## Details

[Deeper explanation, encyclopedia-style paragraphs]

## See Also

- [[workspace-concepts/related-concept]] — How it connects

## Sources

- [[raw/workspace-confluence/SECURITY/pages/12345--encryption-at-rest]] (Section 3.2)
```

### Standard / Recommendation / Informational article

Same shape as concept; lives in `wiki/workspace-standards/{team}/{slug}.md` etc. The directory placement encodes the authority. Frontmatter `domain` is required.

### Connection article (`wiki/workspace-connections/{slug}.md`)

```markdown
---
title: "Connection: X and Y"
type: connection
connects:
  - "workspace-concepts/concept-x"
  - "workspace-concepts/concept-y"
sources:
  - "raw/workspace-confluence/SPACE/pages/...md"
status: published
created: 2026-04-28
updated: 2026-04-28
---

# Connection: X and Y

## The Connection

[What links these concepts]

## Key Insight

[The non-obvious relationship]

## Evidence

[Examples drawn from sources]

## See Also

- [[workspace-concepts/concept-x]]
- [[workspace-concepts/concept-y]]
```

### Q&A article (`wiki/workspace-qa/{slug}.md`)

```markdown
---
title: "Q: Original Question"
type: qa
question: "The exact question asked"
consulted:
  - "workspace-concepts/article-1"
  - "workspace-concepts/article-2"
status: published
filed: 2026-04-28
---

# Q: Original Question

## Answer

[Synthesized answer with section-anchored citations]

## Sources Consulted

- [[workspace-concepts/article-1]] — Relevant because...
- [[workspace-concepts/article-2]] — Provided context on...

## Follow-Up Questions

- [Open questions raised by the answer]
```

### Research claim register (`wiki/platform-research/claim-register.md`)

Research review captures transcript-derived product-intelligence claims. These claims are evidence for product decisions, not canonical internal standards, vendor truth, or roadmap facts.

````markdown
# Research Claim Register

## Claim Records

```yaml
claim_id: RC-YYYY-MM-DD-001
source_transcript: raw/platform-transcripts/path/to/transcript.md
claim_type: product_requirement
atomic_claim: ""
current_design_status: unsupported
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 0
decision: adopt | experiment | defer | reject | monitor
decision_rationale: ""
next_action: ""
```
````

Platform research-review agents may write `wiki/platform-research/**`, `reports/platform-research-review/**`, and `docs/platform-decision-records/DRAFT-*.md`. They must not directly update `wiki/workspace-standards/**`, `wiki/workspace-recommendations/**`, `PRD.md`, `product-brief.md`, `docs/roadmap.md`, `docs/architecture-rationale.md`, `AGENTS.md`, or any `raw/**` source mirror based on transcript claims alone.

Approved platform ADRs may change protected files in a separate user-approved implementation pass.

### Platform research artifact package

Each transcript review produces a **claim-plus-evidence package**, not a summary. Preserve negative knowledge, validation gaps, and decision rationale alongside adopted ideas.

| Artifact | Path | Purpose |
|---|---|---|
| Transcript register | `wiki/platform-research/transcript-register.md` | Queue index: imported vs reviewed (`sync-transcript-register.py`) |
| Claim register | `wiki/platform-research/claim-register.md` | Atomic YAML claim records with scores and decisions |
| Rejection register | `wiki/platform-research/rejected-ideas.md` | Full history for rejected claims and recurring unsafe patterns |
| Open hypotheses | `wiki/platform-research/open-hypotheses.md` | Active experiments and validation targets |
| Implementation backlog | `wiki/platform-research/implementation-backlog.md` | Stack-lift queue for one-change-at-a-time delivery |
| Transcript analysis | `wiki/platform-research/transcript-analyses/{slug}-claims.md` | Per-source claim extraction and grounding notes |
| Impact report | `reports/platform-research-review/{slug}-impact-report.md` | Executive judgment and recommended next actions |
| Batch synthesis | `reports/platform-research-review/batch-synthesis-{date}.md` | Cross-transcript clustering when reviewing batches |
| Draft ADR | `docs/platform-decision-records/DRAFT-{claim_id}-{short-title}.md` | Proposed canonical change; requires explicit user approval |

Required claim record fields: `claim_id`, `source_transcript`, `claim_type`, `atomic_claim`, `current_design_status`, `impact_scores`, `total_score`, `decision`, `decision_rationale`, `next_action`, `validation_status`, `correction_route`. Rejected claims must also appear in `rejected-ideas.md` with `next_review_after`.

### Trust loop pattern

Platform and workspace workflows that affect downstream decisions should follow the trust loop: capture → schema → audit → confidence → guardrail → surface → correct. Template: `templates/platform-research/trust-loop.md`.

| Trust field | Purpose |
|---|---|
| `validation_status` | Records how confidently the claim is grounded |
| `requires_external_validation` | Flags vendor/market claims needing primary-source checks |
| `correction_route` | Tells the user how to approve, reject, or reopen the claim |

Fail closed: do not `adopt` a claim when `requires_external_validation: true` and `validation_status` is `unvalidated`. Impact reports must include `## Trust Loop Summary` and `## Correction Routes`.

Run `python scripts/lint-platform-research.py --root .` after creating or updating platform research artifacts.

### Project stage artifact (`wiki/workspace-projects/{slug}/0X-{stage}/{name}.md`)

```markdown
---
title: "Document Title"
type: project-artifact
project: "{slug}"
stage: "vp-brief" | "pm-prd" | "architecture" | "engineering"
status: draft | review | published | archived
agent_mode: thinking | artifact   # RC-116; draft only; default artifact when absent
authored_by_agent: vp | pm | architect | engineer
sources:
  - "wiki/workspace-standards/architecture/microservice-sizing.md"
  - "raw/workspace-external/aws/s3/encryption.md"
created: 2026-04-28
updated: 2026-04-28
---

# Document Title

[Body prose. At draft status, wikilinks allowed. At review/published, body must be link-free.]

## See Also

[Optional navigation; only at review/published]

## Open Questions

[Optional; allowed at any status]
```

---

## Index format

`wiki/index.md` is the primary navigation entry. Structure:

```markdown
# Knowledge Base Index

## Active projects

[Embed: wiki/workspace-views/active-projects.base, or table here]

## Standards by team

[Embed: wiki/workspace-views/standards-by-team.base]

## Recent activity

[Embed: wiki/workspace-views/recent-activity.base]

## All concepts

| Article | Authority | Domain | Sources | Updated |
|---|---|---|---|---|
| [[workspace-concepts/encryption-at-rest]] | Standard | Internal | 2 | 2026-04-28 |
| ... |

## All connections

| Article | Connects | Updated |
|---|---|---|

## Stale vendor docs

[Embed: wiki/workspace-views/stale-vendor-docs.base]
```

You update this file on every compile. It is the agent's primary retrieval mechanism for queries: read `index.md` first to identify relevant articles, then read those articles in full.

---

## Log format

`wiki/log.md` is append-only, parseable by grep. Format:

```markdown
# Build Log

## [2026-04-28T14:30:00Z] ingest | Confluence space ARCH
- Pages fetched: 47
- Pages compiled: 45
- Quarantined: 2 ([[quarantine/2026-04-28/12345]], [[quarantine/2026-04-28/12346]])
- Wiki articles created: [[workspace-concepts/microservice-sizing]], [[workspace-standards/architecture/microservice-sizing]]
- Index updated

## [2026-04-28T15:12:00Z] query | "What is our microservice sizing standard?"
- Consulted: [[workspace-standards/architecture/microservice-sizing]], [[workspace-concepts/service-boundaries]]
- Filed to: [[workspace-qa/microservice-sizing-explained]]

## [2026-04-28T16:00:00Z] align-vendor-truth | wiki/workspace-projects/customer-data-replatform/02-pm-prd/product-requirements.md
- Vendor claims checked: 7
- Violations: 1 (Snowflake claim cited internal source instead of vendor doc)
- Resolution suggested: refetch raw/workspace-external/snowflake/data-types.md

## [2026-04-28T16:30:00Z] publish | review | wiki/workspace-projects/customer-data-replatform/02-pm-prd/product-requirements.md
- Output: confluence-review/customer-data-replatform/product-requirements-2026-04-28-1630.html
- align-cite: passed
- align-closure: passed
```

---

## Wikilinks and the closure rule

### Closure rule

A project's **active authored set** is the documents inside `wiki/workspace-projects/{slug}/0X-{stage}/`. The set must be jr-engineer-executable using only itself.

### Body prose rule (status-aware)

| Status | Body wikilinks allowed in prose? |
|---|---|
| `draft` | Yes (agent collaboration) |
| `review` | No (move to `## See Also` or frontmatter) |
| `published` | No |
| `archived` | No (frozen state) |

External Markdown links (`[text](url)`) for vendor docs and public references are allowed in body at any status.

### Cross-project rule

An `in-progress` project (status `draft` or `review` on any of its files) cannot reference:
- Another `in-progress` project
- An `archived` project

It CAN reference:
- A `published` project
- Internal `wiki/workspace-standards/`, `wiki/workspace-recommendations/`, `wiki/workspace-concepts/` content
- External vendor docs (in raw/workspace-external/)
- External public URLs

When `align-closure` detects a forbidden cross-project dependency, present the user with options:
1. Finish the dependency project (move it to `published`)
2. Archive the dependency project (move it to `wiki/workspace-archives/`; the dependent project must then be restated)
3. Restate the dependent project to remove the dependency

### Vendor citation pattern

In body prose: parenthetical attribution.
> S3 supports server-side encryption with KMS-managed keys (per AWS docs).

In `## See Also`: external link.
> - [AWS S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) (cached 2026-04-28)

The cached vendor doc in `raw/workspace-external/{vendor}/{topic}/{slug}.md` is the actual source; the See Also URL points to the live source for the reader to verify.

### Internal standard reference pattern

In body prose: inline the relevant rules.
> Per the Architecture team's microservice sizing standard, services with fewer than three deployments per quarter and one or fewer engineers should remain consolidated rather than split. New services require Architecture review.

In `## See Also`: link to the Confluence URL (not the wiki article path).
> - [Microservice Sizing Standard](https://yourcompany.atlassian.net/wiki/spaces/ARCH/pages/12345/Microservice+Sizing+Standard) - Architecture team

The reader may not have access to the Confluence page. The inlined rules guarantee execution; the URL is a courtesy for verification.

---

## Core operations

### 1. Ingest (Confluence)

Use the user's existing API-based skill (REST API v2 with `body-format=atlas_doc_format`). Per-page workflow:

1. Fetch the page (and attachments and comments)
2. Convert ADF to Markdown
3. Write `raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md` with frontmatter (`source_url`, `space_key`, `page_id`, `title`, `ancestors`, `version`, `last_modified`, `labels`, `ingested_at`, `content_hash`, `domain`, `authority`)
4. **Compile only after explicit user approval** per batch (RC-146). Ingest may use `--raw-only` for inbox staging; otherwise ask before invoking compile.
5. Update `wiki/index.md` and `wiki/log.md` when compile is approved
6. On conversion failure: write payload + error to `quarantine/{date}/{page-id}/`; do NOT block the run

After the run, print a manifest:

```
Ingested: 47 pages (45 compiled, 2 quarantined)
Wiki articles created: 12
Wiki articles updated: 8
Index updated.
Run smoke-test query? (y/n)
```

The Atlassian Remote MCP Server is documented as an alternative path. Build week 1 spike validates whether it is viable on the user's tenant.

### 2. Ingest (vendor doc, on demand)

When you are about to cite a vendor capability, check:
- Is there a cached doc in `raw/workspace-external/{vendor}/` covering the topic?
- Is it within TTL (90 days default; per-vendor overrides; 365 day hard max)?

If no cache or stale: offer to fetch.

```
About to cite: "S3 supports server-side encryption with KMS-managed keys"
Cached AWS doc: raw/workspace-external/aws/s3/encryption.md (fetched 2026-01-15, 103 days old, beyond 90-day TTL)
Refetch? (y/n)
```

If yes:
1. Use `defuddle` skill to fetch and clean Markdown from the vendor URL
2. Write `raw/workspace-external/{vendor}/{topic}/{slug}.md` with frontmatter (`source_url`, `vendor`, `topic`, `fetched_at`, `revalidate_after`, `domain`, `authority`)
3. Update `wiki/index.md`
4. Append to `wiki/log.md`

### 3. Compile (raw → wiki)

**Compile approval gate (RC-146):** Stop before any wiki write until the user explicitly approves the compile batch. Orphan raw pages are expected inbox state until approved compile.

**Retrieval contract first (RC-2026-05-27-018):** Before compile or multi-standard project authoring, document the context bundle (purpose, in-scope sources, required wiki/raw paths, authority, freshness, exclusions). Template: `templates/workspace/retrieval-contract-checklist.md`. Storage/index choice follows the contract; default remains page-index (RC-001). Optional for single-source Q&A; required before `review` on multi-standard project artifacts.

When processing newly ingested raw/ pages:

1. Read the raw page
2. Read `wiki/index.md` to understand current knowledge state
3. Read existing wiki articles that may be affected
4. For each piece of knowledge in the raw page:
   - If a concept article covers this topic: UPDATE it; add the raw page as a source
   - If new: CREATE a new `wiki/workspace-concepts/` article
   - If the page is a standard (per the source-domain mapping in `config/second-brain.yml`): CREATE or UPDATE in `wiki/workspace-standards/{team}/`
5. If the page reveals a non-obvious connection between 2+ existing concepts: CREATE a `wiki/workspace-connections/` article
6. Use the `obsidian-markdown` skill for output formatting (frontmatter, wikilinks, callouts)
7. UPDATE `wiki/index.md` with new or modified entries
8. APPEND to `wiki/log.md`

Guidelines:
- A single raw page may touch 3-15 wiki articles
- Prefer updating existing articles over creating near-duplicates
- Every article must have valid frontmatter and a Sources section
- Encyclopedia style: factual, concise, self-contained

### 4. Query (index-guided)

**v1 retrieval policy (RC-2026-05-27-001, RC-2026-05-27-002):** Page-index / structure-aware retrieval is the default. The agent navigates by catalog entries, document hierarchy, and section anchors—not embedding similarity alone. **Retrieved context is not citation support.** Similarity, chunk proximity, or retrieval confidence never substitutes for `align-cite` verification before publish.

**Read-before-write (RC-2026-05-27-122):** Workspace agents read scoped index/catalog and relevant sources before proposing artifact edits. Retrieval and questioning precede generation. Scoped reads per `config/second-brain.yml`; do not read the entire repo without scope.

**Citation-grounded query (RC-2026-05-27-157):** Every query response lists **Sources consulted** (wiki paths, `raw/` paths, and vendor cache paths actually read) before the synthesized answer. Listed paths must exist on disk. The source list does not substitute for `align-cite` at publish time.

For long structured sources (Confluence pages, multi-section artifacts), prefer section-tree navigation over blind chunking. Any future vector, hybrid, graph, or rerank retriever must pass a holdout evaluation showing improved citation precision and inspectability without weakening junior-engineer closure before adoption.

1. Read `wiki/index.md` first
2. Identify 3-10 relevant articles based on the question
3. Read those articles in full
4. List sources consulted (paths that exist on disk)
5. Synthesize an answer with section-anchored citations
6. If `--file-back`: create a `wiki/workspace-qa/` article and update index and log

Decision records: `docs/platform-decision-records/DRAFT-RC-2026-05-27-001-page-index-retrieval.md`, `DRAFT-RC-2026-05-27-122-read-before-write-retrieval.md`, `DRAFT-RC-2026-05-27-157-citation-grounded-query.md`

### 5. Transcript librarian (import and queue)

Use `platform-transcript-librarian` to import product-intelligence transcripts, sync `wiki/platform-research/transcript-register.md`, and process the review queue.

1. Run `python scripts/sync-transcript-register.py --root .` and read the register.
2. For imports: propose slug and path; **stop for user approval** before writing `raw/platform-transcripts/**`.
3. For each `queued` row: delegate to `platform-research-review` / `platform-research-reviewer`.
4. After each review: sync register, run lint, **stop** if the user asked for step-by-step confirmation.

Prompt: `.github/prompts/platform-transcript-librarian.prompt.md`. Checkpoints: `templates/platform-research/librarian-checkpoint.md`.

### 6. Research review

Use `platform-research-review` for transcripts, meeting notes, interviews, or product-improvement discussions about Second Brain.

1. Read the transcript under `raw/platform-transcripts/**` or the user-specified source note
2. Read `AGENTS.md`, `product-brief.md`, `PRD.md`, `docs/architecture-rationale.md`, `docs/roadmap.md`, and `wiki/platform-research/claim-register.md` when present
3. Segment the source into discussion blocks
4. Extract atomic claims and classify each claim
5. Ground claims against existing Second Brain docs and vendor docs when relevant
6. Run skeptical review and score each claim on governance, closure, grounding, vendor truth, inspectability, maintainability, differentiation, enterprise fit, and human review leverage
7. Decide `adopt`, `experiment`, `defer`, `reject`, or `monitor`
8. Write `wiki/platform-research/transcript-analyses/{slug}-claims.md`
9. Update `wiki/platform-research/claim-register.md`
10. Write `reports/platform-research-review/{slug}-impact-report.md`
11. Create draft ADRs under `docs/platform-decision-records/DRAFT-*.md` only for adopted or experimental claims
12. Mirror every `reject` decision in `wiki/platform-research/rejected-ideas.md` (run `python scripts/sync-rejected-register.py --root .` after bulk claim-register updates)
13. Update `wiki/platform-research/open-hypotheses.md` for experimental claims
14. For batch reviews, write `reports/platform-research-review/batch-synthesis-{date}.md` and update `wiki/platform-research/implementation-backlog.md` when adopt/experiment/defer claims need stack-lift ordering

Research review is deliberately separated from compile. Transcripts may influence Second Brain through review artifacts and draft ADRs, but they do not become canonical knowledge by default.

#### Platform implementation priority loop

After the user approves a draft ADR, deliver approved platform changes one claim at a time:

1. Load `wiki/platform-research/implementation-backlog.md`
2. Select the highest `priority_score` item with status `queued` and satisfied dependencies
3. Implement the smallest reversible change set described in the approved ADR
4. Run validation:
   - `python -m unittest discover -s tests`
   - `python scripts/lint-platform-research.py --root .`
5. Present diff, test results, and rollback steps to the user
6. On **accept**: mark the backlog item `accepted`, append decision history, re-score the queue
7. On **reject**: rollback, mark `rolled_back`, capture reason, re-score the queue
8. Repeat with the next queued item

`priority_score` uses stack lift, platform lift, validation clarity, implementability, evidence strength, canonical risk, and experiment uncertainty (see `config/platform-research-review.example.yml`). Transcript `total_score` decides whether to adopt/experiment/defer/reject; `priority_score` decides implementation order among approved items.

Process ADR: `docs/platform-decision-records/DRAFT-RC-implementation-priority-loop.md`

### 7. Align (cite | conformance | coverage)

Three depths. Run `align-cite` automatically before publish; others on demand.

**align-cite** (production quality):
- Walk every citation in the artifact
- For each, verify the cited source exists and contains content matching the claim
- Output: structured report listing each violation (claim text, claimed source, problem)

**align-conformance** (best-effort, advisory):
- For each in-scope standard, check whether the artifact's structure, terminology, and decisions match
- Output: advisory report; user-judged

**align-coverage** (best-effort, advisory):
- For each in-scope standard, extract a requirements list
- Check the artifact addresses each relevant requirement
- Output: advisory report listing addressed and missing requirements

### 8. Align (vendor-truth)

- Identify vendor-domain claims in the artifact (claims about AWS, Snowflake, etc.)
- Verify each claim's citation is in the matching vendor domain (`raw/workspace-external/{vendor}/`)
- Flag claims that cite internal sources instead of vendor sources
- For flagged claims, suggest the vendor doc to fetch

### 9. Align (closure)

Status-aware. Read the artifact's `status` frontmatter and apply rules:

- All statuses: cross-project dependency check (no in-progress → in-progress; no in-progress → archived)
- `review` and `published`: body prose contains no `[[wikilinks]]`
- `published`: all TODO / Open-Questions / NEEDS-INPUT markers resolved or moved to a clearly-marked addendum

Output: structured report. Run automatically before publish.

### 10. Publish

Branch on user choice:

**Review branch:**
1. Convert Markdown to vanilla HTML (browser-readable preview, NOT Confluence storage format)
2. Write `confluence-review/{project-slug}/{doc-slug}-{timestamp}.html`
3. Print full path
4. Open the folder using OS-native opener (`explorer` Windows, `open` macOS, `xdg-open` Linux)

**Confluence branch:**
1. Run `align-cite` and `align-closure` automatically; block on violations unless user explicitly overrides; log overrides
2. Convert Markdown to Confluence storage format (or ADF)
3. Use the user's existing API code (or MCP server alternative) to create new pages in the target Confluence space

### 11. Archive

1. Move project directory: `wiki/workspace-projects/{slug}/` → `wiki/workspace-archives/projects/{slug}/`
2. Set `archived: true` and `archived_at: timestamp` in frontmatter on every file
3. Update `wiki/index.md` to remove from active project lists
4. Append to `wiki/log.md`

`unarchive` reverses: moves back to `wiki/workspace-projects/{slug}/`, removes archived frontmatter, updates index.

### 12. Lint

Seven structural checks plus engineering additions:

| Check | Type | Catches |
|---|---|---|
| Broken links | Structural | Wikilinks pointing to non-existent articles |
| Orphan pages | Structural | Articles with zero inbound links from other articles in the same set |
| Orphan sources | Structural | Raw pages not yet compiled (RC-146: advisory for inbox staging) |
| Stale articles | Structural | Source raw page changed since article was last compiled (content_hash differs) |
| Missing backlinks | Structural | A links to B but B does not link back |
| Sparse articles | Structural | Under 200 words |
| Contradictions | LLM | Conflicting claims across articles |
| Deprecated standards | Engineering | Standards marked deprecated still being referenced |
| Cross-team requirement conflicts | Engineering | Two teams' standards giving incompatible guidance |
| Missing alignment | Engineering | Project artifact lacks citation to relevant in-scope standards |
| Incomplete ingestion | Engineering | Page in `raw/` without a wiki article referencing it |
| Stale vendor docs | Engineering | Past TTL or hard max |
| Status-aware closure | Engineering | Body wikilinks at review/published; cross-project violations |
| Research review integrity | Engineering | Invalid claim records, report shape gaps, protected-file contamination |
| Instruction stack shim duplication | Engineering | Tier-1 governance rules copied verbatim into shims instead of referencing AGENTS.md (RC-161) |
| Orientation integrity | Engineering | RC-163: orientation files missing `not_canonical`, promoted status, or cited as wiki sources |
| Agent mode | Engineering | RC-116: `thinking` mode artifacts at review/published or with publish-shaped markers |
| Sub-scaffold integrity | Engineering | RC-167: `subprojects/**` missing `publish_scope: exclude`, promoted status, or cited as publish sources |
| Thinking-notes integrity | Engineering | RC-117: `thinking-notes/**` missing `not_canonical`, promoted status, or cited as publish sources |

Output: `reports/workspace-lint-{date}.md` with severity per finding.

---

## Lifecycle states

Project artifacts move through:

| State | Sub-states | Notes |
|---|---|---|
| `in-progress` | `draft`, `review` | Active project work |
| `published` | (single state) | Completed; referenceable by other projects |
| `archived` | (single state) | Removed from active consideration; on disk for audit |

Transition rules:
- `draft` → `review`: requires Engineer-led finalize step (body wikilinks removed, See Also populated, status updated)
- `review` → `published`: requires `align-cite` and `align-closure` to pass (or explicit override)
- `published` → `archived`: explicit `archive` operation
- `archived` → any: requires explicit `unarchive`

---

## Conventions

- **Wikilinks:** Obsidian-style `[[path/to/article]]` without `.md` extension. Section anchors: `[[file#heading]]`. Block IDs: `^block-id`.
- **Writing style:** Encyclopedia-style, factual, third-person where appropriate. Match the exemplar in `docs/style/exemplar-published-doc.md` for project artifacts.
- **Dates:** ISO 8601 (`YYYY-MM-DD` for dates; `YYYY-MM-DDTHH:MM:SSZ` for timestamps).
- **File naming:** lowercase, hyphens for spaces (e.g., `microservice-sizing-standard.md`).
- **Frontmatter:** Every article must have YAML frontmatter with at minimum `title`, `type`, `sources`, `status`, `created`, `updated`. Articles with authority require `authority` and `domain`.
- **Sources:** Always link back to the raw page or external URL that contributed.

---

## File structure (full)

```
second-brain/
├── README.md
├── AGENTS.md                              # this file
├── LICENSE
├── .gitignore
├── .env.example
│
├── .github/
│   ├── README.md
│   ├── copilot-instructions.md            # Copilot shim
│   ├── prompts/
│   │   ├── second-brain.prompt.md
│   │   ├── workspace-start-project.prompt.md
│   │   ├── workspace-vp-agent.prompt.md
│   │   ├── workspace-pm-agent.prompt.md
│   │   ├── workspace-architect-agent.prompt.md
│   │   ├── workspace-engineer-agent.prompt.md
│   │   ├── finalize.prompt.md
│   │   ├── workspace-ingest-confluence.prompt.md
│   │   ├── ingest-jira.prompt.md          # v1.x
│   │   ├── workspace-ingest-vendor-doc.prompt.md
│   │   ├── revalidate-vendor-docs.prompt.md
│   │   ├── workspace-compile.prompt.md
│   │   ├── workspace-query.prompt.md
│   │   ├── workspace-session-audit.prompt.md
│   │   ├── platform-transcript-librarian.prompt.md
│   │   ├── platform-research-review.prompt.md
│   │   ├── platform-research-review/
│   │   ├── workspace-align-cite.prompt.md
│   │   ├── workspace-align-conformance.prompt.md
│   │   ├── workspace-align-coverage.prompt.md
│   │   ├── workspace-align-vendor-truth.prompt.md
│   │   ├── workspace-align-closure.prompt.md
│   │   ├── workspace-publish.prompt.md
│   │   ├── workspace-prepare-for-confluence.prompt.md
│   │   ├── workspace-publish-to-confluence.prompt.md
│   │   ├── workspace-archive.prompt.md
│   │   ├── workspace-unarchive.prompt.md
│   │   └── workspace-lint.prompt.md
│   ├── agents/                            # placeholder
│   │   └── README.md
│   └── skills/
│       ├── README.md
│       ├── obsidian-markdown/SKILL.md
│       ├── obsidian-bases/SKILL.md
│       ├── defuddle/SKILL.md
│       └── platform-research-review/SKILL.md
│
├── CLAUDE.md                              # Claude Code shim
├── .cursor/rules/agents.mdc               # Cursor shim
├── .windsurfrules                         # Windsurf shim
│
├── docs/
│   ├── product-brief.md
│   ├── PRD.md
│   ├── architecture-rationale.md
│   ├── roadmap.md
│   ├── progress-log.md
│   ├── platform-intelligence/
│   ├── platform-decision-records/
│   ├── setup-kit.md
│   ├── adoption-checklist.md
│   └── style/
│       └── exemplar-published-doc.md
│
├── config/
│   ├── second-brain.example.yml
│   └── second-brain.yml                   # gitignored
│
├── templates/
│   └── personas/
│       ├── ceo/                           # populated in v1
│       ├── engineer/                      # stub
│       ├── architect/                     # stub
│       ├── product-manager/               # stub
│       ├── director/                      # stub
│       └── vp/                            # stub
│
├── raw/                                   # content gitignored; structure tracked
│   ├── README.md
│   ├── workspace-confluence/
│   ├── workspace-jira/                    # v1.x
│   ├── workspace-external/
│   └── platform-transcripts/
│
├── wiki/                                  # content gitignored; structure tracked
│   ├── index.md
│   ├── log.md
│   ├── workspace-standards/
│   ├── workspace-recommendations/
│   ├── workspace-informational/
│   ├── workspace-concepts/
│   ├── workspace-connections/
│   ├── workspace-qa/
│   ├── workspace-projects/
│   ├── workspace-archives/
│   ├── workspace-views/
│   └── platform-research/
│
├── confluence-review/                     # gitignored
├── quarantine/                            # gitignored
├── reports/                               # gitignored
│
├── reference-documents/
│   └── README.md
│
├── .obsidian/                             # tracked
│   ├── workspace.json
│   ├── app.json
│   └── plugins/
│
└── scripts/
    ├── verify-setup.py
    └── README.md
```

---

## Vendor doc TTL configuration

In `config/second-brain.yml`:

```yaml
vendor_revalidation:
  default_ttl_days: 90
  per_vendor: {}                 # user can override per vendor, e.g., aws: 60
  hard_max_age_days: 365

confluence_sync:
  default_cadence: weekly
  reminder_after_days: 7
```

Behavior:
- Within TTL: cache is fresh; cite with `(cached YYYY-MM-DD)` annotation
- Past TTL but under hard max: flag stale and offer refetch before citing
- Past hard max: always prompt for refetch; cannot cite without refresh

---

## Project closure rules (summary)

1. Body prose at `review` and `published` contains no `[[wikilinks]]`. Navigation goes in `## See Also` or frontmatter.
2. Vendor capability claims use parenthetical attribution + See Also link. Inline detail not required.
3. Internal team standards: inline the relevant rules + provide Confluence URL in See Also.
4. In-progress project cannot reference another in-progress or archived project. Resolution: finish, archive, or restate.
5. `align-closure` runs automatically before publish; violations block unless user explicitly overrides.
6. The bar: a junior engineer can execute the work using only the published artifact set.

---

## On co-evolution

This document is the operating spec, but it is also the user's working knowledge of how Second Brain operates. As you and the user discover better patterns, update this document. Record changes in `docs/progress-log.md`. The schema is yours to refine; the user's job is to direct the work and accept or reject your suggestions.
