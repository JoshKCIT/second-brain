# Chain profiles (PH-2026-06-09-001)

Declarative agent chains for workspace projects. Each profile lists ordered stages, prompts, deliverables, and skip rules. CEO review between stages is mandatory (`ceo_gate_policy: every_stage`).

Profiles live in this directory. Project state references a profile via `chain_profile` and optional `chain_profile_path` in `wiki/workspace-projects/{slug}/meta.yml`.

## Profile schema

```yaml
profile_id: technical-doc-initiative    # stable slug; matches filename stem
title: "Technical documentation initiative"
status: active                        # active | draft | deprecated
closure_rule: jr-engineer-executable  # default; profiles may declare advisory-only
ceo_gate_policy: every_stage          # cannot disable align-cite / publish gates

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
  # …
```

| Field | Required | Meaning |
|---|---|---|
| `profile_id` | yes | Stable slug; stored in `meta.yml` `chain_profile` |
| `title` | yes | Human label for start-project picker |
| `status` | yes | `active` profiles appear in picker; `draft` requires explicit CEO opt-in |
| `closure_rule` | yes | Publish closure bar for this profile |
| `ceo_gate_policy` | yes | Always `every_stage` in v1 |
| `stages[]` | yes | Ordered stage list |
| `stages[].id` | yes | Matches `meta.yml` `current_stage` values where applicable |
| `stages[].prompt` | yes | Tier-2 prompt stem under `.github/prompts/` |
| `stages[].stage_dir` | yes | Project subdirectory |
| `stages[].deliverable` | yes | Primary artifact filename |
| `stages[].skip_when` | yes | `never` \| `non_technical` \| `profile_defined` |

## Available profiles

| profile_id | File | Status | Notes |
|---|---|---|---|
| `technical-doc-initiative` | `technical-doc-initiative.md` | **active (default)** | VP → PM → Architect? → Engineer → finalize → align → publish (PH-2026-06-09-002) |

| Optional stage `technical-writing` | PH-2026-06-09-003 | `workspace-technical-writer-agent` — polish before finalize; not in default profile v1 |
| Optional stage `architect-review` | PH-2026-06-09-004 | `workspace-architect-reviewer-agent` — advisory standards conformance report; not in default profile v1 |

Planned (PH-2026-06-09-005 … 007): meeting-synthesis, knowledge-hub profiles; qa optional stage.

## Orchestrator rules

1. At project create, CEO picks `chain_profile` (default: `technical-doc-initiative`).
2. On resume, read `meta.yml` `chain_profile` → load profile file → resolve next stage from `stages[]` and `current_stage`.
3. If `chain_profile` absent on legacy projects, treat as `technical-doc-initiative` and offer backfill on resume.
4. Profiles cannot remove approval-gated ingest, compile, or publish; align-cite and align-closure remain mandatory before publish.
5. Platform-lane work uses `platform-*` verbs, not workspace chain profiles.

## See also

- `templates/workspace/project-meta.yml.md` — `chain_profile` fields
- `templates/workspace/experiment-registry.md` — structural hygiene PH-001–008
- ADR: `docs/platform-decision-records/PH-2026-06-09-001-chain-profile-schema.md`
- Default profile ADR: `docs/platform-decision-records/PH-2026-06-09-002-technical-doc-initiative-profile.md`
