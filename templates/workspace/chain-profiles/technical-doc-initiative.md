---
profile_id: technical-doc-initiative
title: Technical documentation initiative
status: active
closure_rule: jr-engineer-executable
ceo_gate_policy: every_stage
---

# Chain profile: technical-doc-initiative

Default Second Brain project chain. Matches pre-PH-2026-06-09 behavior: VP → PM → Architect (if technical) → Engineer → finalize → align → publish.

Full profile documentation expands in PH-2026-06-09-002.

## Stages

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
    deliverable: "(finalize step — status review)"
    skip_when: never
  - id: align
    prompt: workspace-align-cite
    stage_dir: null
    deliverable: "(align-cite + align-closure reports)"
    skip_when: never
  - id: ready-for-publish
    prompt: workspace-publish
    stage_dir: null
    deliverable: "(CEO publish choice)"
    skip_when: never
```

## Skip rules

| Condition | Effect |
|---|---|
| `technical: false` in `meta.yml` | Skip `architecture` stage; PM → engineering |
| PH-005 reopen | Orchestrator uses PH-001 transitions; profile stages remain authoritative for deliverable paths |

## Closure rule

Published artifact set under `wiki/workspace-projects/{slug}/0X-{stage}/` must be jr-engineer-executable using only that set (align-closure).
