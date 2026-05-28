---
description: Orchestrates the Second Brain agent chain (CEO declares intent; VP, PM, Architect, Engineer produce artifacts in sequence with CEO review between stages)
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# Start Project

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are orchestrating a new Second Brain project. The user (CEO) declares high-level intent; you guide them through the agent chain (VP → PM → Architect (if technical) → Engineer → finalize), pausing for explicit CEO approval between stages.

## Pre-flight checks (before greeting)

1. Verify `config/second-brain.yml` exists and lists default in-scope spaces. If missing, tell the user to run `/second-brain` for onboarding first.
2. Verify `wiki/index.md` exists. If missing, the wiki has not been initialized; run setup.
3. Verify `.env` is loaded with valid Atlassian credentials. If credential check fails, surface the error.

## Step 1: Capture project intent

Greet the CEO and ask for:

- **Project name** (becomes `slug`, lowercase kebab-case)
- **One-paragraph description** (the WHAT)
- **Business outcome** (the WHY; what changes if this succeeds)
- **Technical or non-technical?** (determines whether Architect Agent runs)
- **Top 2-3 concerns or constraints** known up front

If the user is unsure whether technical applies, default to yes.

## Step 2: Create project skeleton

```
wiki/workspace-projects/{slug}/
├── 01-vp-brief/
│   ├── handoff.md          (optional — RC-058)
│   ├── research/           (optional — RC-130)
│   ├── chats/              (optional — RC-130)
│   └── daily-progress/     (optional — RC-130)
├── 02-pm-prd/
│   ├── handoff.md
│   ├── research/
│   ├── chats/
│   └── daily-progress/
├── 03-architecture/        (created only if technical)
│   └── … same scaffold …
├── 04-engineering/
│   └── … same scaffold …
├── meta.yml
├── retrieval-contract.md   (optional; recommended for multi-standard projects — RC-018)
└── README.md
```

`meta.yml` content (template: `templates/workspace/project-meta.yml.md`, PH-001):

```yaml
slug: {slug}
name: {project name}
status: in-progress
sub_status: draft
created: {ISO date}
updated: {ISO date}
technical: {true|false}
current_stage: vp-brief
stage_gate: agent_work
last_completed: null
in_scope_spaces:
  - {space-key}
in_scope_jira_projects: []
authority_overrides: {}
alignment_defaults:
  align_cite: production
  align_conformance: best-effort
  align_coverage: best-effort
```

## Project stage state (PH-001)

Update `meta.yml` at every chain step and CEO gate. **`current_stage` + `stage_gate` + `last_completed` are authoritative for resumability.**

| Step / event | `current_stage` | `stage_gate` | `last_completed` |
|---|---|---|---|
| Skeleton created | `vp-brief` | `agent_work` | `null` |
| VP draft complete | `vp-brief` | `awaiting_ceo_review` | unchanged |
| CEO approves VP | `pm-prd` | `agent_work` | `vp-brief` |
| PM draft complete | `pm-prd` | `awaiting_ceo_review` | unchanged |
| CEO approves PM (technical) | `architecture` | `agent_work` | `pm-prd` |
| CEO approves PM (non-technical) | `engineering` | `agent_work` | `pm-prd` |
| Architect draft complete | `architecture` | `awaiting_ceo_review` | unchanged |
| CEO approves architecture | `engineering` | `agent_work` | `architecture` |
| Engineer draft complete | `engineering` | `awaiting_ceo_review` | unchanged |
| CEO approves engineering | `finalize` | `agent_work` | `engineering` |
| Finalize complete | `align` | `agent_work` | `finalize` |
| Align gates pass | `ready-for-publish` | `awaiting_ceo_review` | `finalize` |
| CEO stops | unchanged | `blocked` | unchanged |

Always set `updated` when writing `meta.yml`. Append transition to `wiki/log.md`:

```
## [{ISO timestamp}] project-state | {slug} | stage={current_stage} gate={stage_gate} last_completed={last_completed}
```

`README.md` is a brief project overview generated from the CEO's intent.

When creating stage directories, optionally create empty `research/`, `chats/`, and `daily-progress/` subdirs per `templates/workspace/project-stage-scaffold/README.md` (RC-130). Scaffold is draft-tier; never part of publish set.

Append entry to `wiki/log.md`:

```
## [{ISO timestamp}] start-project | {slug}
- Created: wiki/workspace-projects/{slug}/{subdirs}
- Technical: {true|false}
- In-scope spaces: {list}
```

## Step 3: Invoke VP agent

Invoke `.github/prompts/workspace-vp-agent.prompt.md` with the captured intent. Pass:

- Project slug
- CEO's description and business outcome
- Top constraints
- In-scope spaces

The VP agent produces `wiki/workspace-projects/{slug}/01-vp-brief/product-brief.md` at status `draft`.

## Step 4: CEO review (gate)

Show the VP brief to the CEO. Wait for one of:

- "Approved, proceed" → Step 5
- "Edit X" → make the requested edits, then re-review
- "Stop" → exit

Do not proceed without explicit approval.

## Step 5: Invoke PM agent

Invoke `.github/prompts/workspace-pm-agent.prompt.md` with the approved VP brief.

Output: `wiki/workspace-projects/{slug}/02-pm-prd/product-requirements.md` at status `draft`.

## Step 6: CEO review (gate)

Same as Step 4. Wait for explicit approval.

## Step 7: Branch on technical

If `technical: true` in `meta.yml`, proceed to Step 8.

If `technical: false`, skip to Step 10 (Engineer agent reads the PRD directly instead of the architecture doc).

## Step 8: Invoke Architect agent (technical only)

Invoke `.github/prompts/workspace-architect-agent.prompt.md` with the approved PRD.

Output: `wiki/workspace-projects/{slug}/03-architecture/architectural-approaches.md` at status `draft`. May also produce ADRs in `wiki/workspace-projects/{slug}/03-architecture/adrs/` for specific decisions.

## Step 9: CEO review (gate)

Same as Step 4.

## Step 10: Invoke Engineer agent

Invoke `.github/prompts/workspace-engineer-agent.prompt.md` with the approved architecture doc (or PRD if non-technical).

Output: `wiki/workspace-projects/{slug}/04-engineering/{spec-files}.md` at status `draft`.

## Step 11: Finalize

Run the finalize step per `.github/prompts/workspace-engineer-agent.prompt.md` **Finalize step** section (Engineer-led). Do not duplicate finalize rules here.

Engineer must exclude draft-tier files and scaffold paths (`handoff.md`, `retrieval-contract.md`, `README.md`, `research/**`, `chats/**`, `daily-progress/**`) from wikilink rewrite and `review` promotion.

## Step 12: Run pre-publish align gates

Run automatically:

- `.github/prompts/workspace-align-cite.prompt.md` against the active set
- `.github/prompts/workspace-align-closure.prompt.md` against the active set

Report results to the CEO. If violations, present resolution options. If clean, update `meta.yml`: `current_stage: ready-for-publish`, `stage_gate: awaiting_ceo_review`, `last_completed: finalize`.

## Step 13: Closing

Append summary to `wiki/log.md`:

```
## [{ISO timestamp}] start-project complete | {slug}
- Stages: vp-brief, pm-prd, {architecture if technical}, engineering, finalize
- Pre-publish align: {cite=pass|N violations}, {closure=pass|N violations}
- Status: ready-for-publish | needs-revision
```

Tell the CEO: project is at `review` status; run `/workspace-publish` when ready, or run additional align checks (`align-conformance`, `align-coverage`, `align-vendor-truth`) for deeper verification before publish.

## Resumability

If invoked again on a project that already has artifacts (detected by `wiki/workspace-projects/{slug}/meta.yml` exists), resume using **PH-001 state first**:

1. Read `meta.yml` **`current_stage`**, **`stage_gate`**, and **`last_completed`**.
   - `stage_gate: awaiting_ceo_review` → present the artifact for `current_stage`; wait for CEO (do not invoke next agent).
   - `stage_gate: agent_work` → invoke the agent for `current_stage` (or finalize/align if `current_stage` is `finalize` / `align`).
   - `stage_gate: blocked` → report state; ask CEO how to proceed.
   - `stage_gate: approved` at stage boundary → advance per transition table above.
2. Read `handoff.md` in the active stage directory (RC-058).
3. Read `daily-progress/` in the active stage (newest 3 files, RC-130).
4. **Fallback only** if PH-001 fields missing: infer from artifact frontmatter and `wiki/log.md`.
5. At session end, update `handoff.md` and `meta.yml`; ask CEO to confirm.

## On error

If any agent invocation fails or produces invalid output:

- Append the failure to `wiki/log.md`
- Report to the CEO with the failure mode
- Offer to retry, edit manually, or skip the stage
- Do not silently proceed to the next stage on failure
