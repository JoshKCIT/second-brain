---
profile_id: technical-doc-initiative
title: Technical documentation initiative
status: active
closure_rule: jr-engineer-executable
ceo_gate_policy: every_stage
default: true
pic_accepted: PH-2026-06-09-002
---

# Chain profile: technical-doc-initiative

**Default Second Brain project chain.** Explicit documentation of pre-PH-2026-06-09 behavior. Zero workflow change when `meta.yml` sets `chain_profile: technical-doc-initiative`.

ADR: `docs/platform-decision-records/PH-2026-06-09-001-chain-profile-schema.md` (schema), `docs/platform-decision-records/PH-2026-06-09-002-technical-doc-initiative-profile.md` (this profile).

## When to use

- Cross-team technical initiatives with a full artifact set (brief → PRD → architecture → engineering specs)
- Projects that must pass align-cite and align-closure before publish
- Jr-engineer-executable published documentation

## Stage table

| Order | Stage `id` | Prompt | Stage dir | Deliverable | Skip when |
|---:|---|---|---|---|---|
| 1 | `vp-brief` | `workspace-vp-agent` | `01-vp-brief/` | `product-brief.md` | never |
| 2 | `pm-prd` | `workspace-pm-agent` | `02-pm-prd/` | `product-requirements.md` | never |
| 3 | `architecture` | `workspace-architect-agent` | `03-architecture/` | `architectural-approaches.md` | `meta.yml` `technical: false` |
| 4 | `engineering` | `workspace-engineer-agent` | `04-engineering/` | `{spec-files}.md` | never |
| 5 | `finalize` | `workspace-engineer-agent` (finalize step) | `04-engineering/` | artifacts → `status: review` | never |
| 6 | `align` | `workspace-align-cite` + `workspace-align-closure` | — | align reports | never |
| 7 | `ready-for-publish` | `workspace-publish` | — | CEO publish choice | never |

## Machine-readable stages

```yaml
stages:
  - id: vp-brief
    prompt: workspace-vp-agent
    stage_dir: 01-vp-brief
    deliverable: product-brief.md
    skip_when: never
  - id: pm-prd
    prompt: workspace-pm-agent
    stage_dir: 02-pm-prd
    deliverable: product-requirements.md
    skip_when: never
  - id: architecture
    prompt: workspace-architect-agent
    stage_dir: 03-architecture
    deliverable: architectural-approaches.md
    skip_when: non_technical
  - id: engineering
    prompt: workspace-engineer-agent
    stage_dir: 04-engineering
    deliverable: "{spec-files}.md"
    skip_when: never
  - id: finalize
    prompt: workspace-engineer-agent
    stage_dir: 04-engineering
    deliverable: "(finalize — status review)"
    skip_when: never
  - id: align
    prompt: workspace-align-cite
    stage_dir: null
    deliverable: "(align-cite + align-closure)"
    skip_when: never
  - id: ready-for-publish
    prompt: workspace-publish
    stage_dir: null
    deliverable: "(CEO publish)"
    skip_when: never
```

## meta.yml mapping (PH-001)

Orchestrator uses `current_stage`, `stage_gate`, and `last_completed` per `templates/workspace/project-meta.yml.md`. This profile's `id` values match PH-001 stage ids.

| Event | `current_stage` after | Notes |
|---|---|---|
| Skeleton created | `vp-brief` | Set `chain_profile: technical-doc-initiative` |
| CEO approves VP | `pm-prd` | PH-003 forward to `02-pm-prd/handoff.md` |
| CEO approves PM (technical) | `architecture` | |
| CEO approves PM (non-technical) | `engineering` | Skip architecture row |
| CEO approves architecture | `engineering` | |
| CEO approves engineering | `finalize` | |
| Finalize complete | `align` | `sub_status: review` |
| Align pass | `ready-for-publish` | `stage_gate: awaiting_ceo_review` |

## CEO gates

Every stage transition requires explicit CEO approval per `workspace-start-project` shared gate options. PH-004 advisory align-cite optional before each gate. PH-005 reopen allowed per `templates/workspace/reopen-stage-protocol.md`.

## Draft-tier exclusions

Not part of publish set: `handoff.md`, `orientation.md`, `retrieval-contract.md`, `research/**`, `thinking-notes/**`, `chats/**`, `daily-progress/**`, `subprojects/**` (RC-167). See `templates/workspace/draft-tier-map.md`.

## Closure rule

Published artifact set under `wiki/workspace-projects/{slug}/0X-{stage}/` must be **jr-engineer-executable** using only that set. Body prose at `review`/`published` has no wikilinks; navigation in `## See Also`.

## Non-technical variant

When `technical: false`, stage 3 (`architecture`) is skipped. Engineer reads approved PRD directly. Directory `03-architecture/` may be omitted at skeleton create.

## See also

- Orchestrator: `.github/prompts/workspace-start-project.prompt.md`
- Inter-stage contract: `templates/workspace/inter-stage-contract.md`
- Example CEO workflow: `templates/personas/ceo/example-prompts/cross-team-initiative.md`
