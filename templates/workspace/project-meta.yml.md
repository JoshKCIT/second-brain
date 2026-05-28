# Project meta.yml template (PH-001)

Machine-readable project state for orchestrator and stage agents. Path: `wiki/workspace-projects/{slug}/meta.yml`

Draft-tier orientation only for `status: in-progress` projects. Update on every stage transition and CEO gate.

## Template

```yaml
slug: {slug}
name: {project name}
status: in-progress          # in-progress | published | archived
sub_status: draft            # draft | review (mirrors active artifact set)
created: {ISO date}
updated: {ISO date}
technical: {true|false}

# PH-001 stage state machine
current_stage: vp-brief      # vp-brief | pm-prd | architecture | engineering | finalize | align | ready-for-publish
stage_gate: agent_work         # agent_work | awaiting_ceo_review | approved | blocked
last_completed: null           # null | vp-brief | pm-prd | architecture | engineering | finalize

in_scope_spaces:
  - {space-key}
in_scope_jira_projects: []
authority_overrides: {}
alignment_defaults:
  align_cite: production
  align_conformance: best-effort
  align_coverage: best-effort
```

## Field definitions

| Field | Values | Meaning |
|---|---|---|
| `current_stage` | `vp-brief`, `pm-prd`, `architecture`, `engineering`, `finalize`, `align`, `ready-for-publish` | Active chain step |
| `stage_gate` | `agent_work`, `awaiting_ceo_review`, `approved`, `blocked` | Who acts next |
| `last_completed` | stage id or `null` | Last CEO-approved stage |

## Transition rules

| Event | Update |
|---|---|
| New project skeleton | `current_stage: vp-brief`, `stage_gate: agent_work`, `last_completed: null` |
| Stage agent finishes draft | `stage_gate: awaiting_ceo_review` (keep `current_stage`) |
| CEO approves stage | `last_completed: {approved stage}`, advance `current_stage` to next, `stage_gate: agent_work` |
| CEO requests edits | `stage_gate: agent_work` (same `current_stage`) |
| CEO stops / blocked | `stage_gate: blocked` |
| Finalize starts | `current_stage: finalize`, `stage_gate: agent_work` |
| Finalize complete | `sub_status: review`, `current_stage: align`, `stage_gate: agent_work`, `last_completed: finalize` |
| Align gates pass | `current_stage: ready-for-publish`, `stage_gate: awaiting_ceo_review` |
| Publish (Confluence) | `status: published`, `stage_gate: approved` |

## Non-technical projects

Skip `architecture` stage: after PM approval set `current_stage: engineering` and `last_completed: pm-prd`.

## Resumability (read order)

1. **`meta.yml`** — `current_stage` + `stage_gate` + `last_completed` (authoritative when present)
2. **`handoff.md`** — session context (RC-058)
3. **`daily-progress/`** — catch-up (RC-130)
4. **Artifact frontmatter** — fallback only if PH-001 fields missing

## Agent obligations

- **Orchestrator (`start-project`):** owns transitions at CEO gates and chain steps; updates `updated` timestamp.
- **Stage agents:** on invoke read `meta.yml`; on session end set `stage_gate: awaiting_ceo_review` if draft complete; do not advance `current_stage` without CEO approval.
- **Publish:** set `status: published` per `workspace-publish.prompt.md`.

## See also

- Hygiene review: `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`
- Handoff: `templates/workspace/handoff.md`
