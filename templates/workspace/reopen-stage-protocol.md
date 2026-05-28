# Reopen stage protocol (PH-005)

Documents how the orchestrator rolls back the workspace agent chain when the CEO invalidates downstream work and reopens an earlier stage. Depends on PH-001 (`meta.yml` state) and PH-003 (inter-stage decisions).

## When to use

| CEO intent | Action |
|---|---|
| Revise **current** stage draft | `stage_gate: agent_work` on same `current_stage`; **no** PH-005 (normal edit loop) |
| **Upstream** artifact is wrong; downstream work is stale | PH-005 reopen to the corrected stage |
| Stop project | `stage_gate: blocked` (PH-001); no reopen |

## Stage chains

| `technical` | Ordered artifact stages |
|---|---|
| `true` | `vp-brief` → `pm-prd` → `architecture` → `engineering` |
| `false` | `vp-brief` → `pm-prd` → `engineering` |

Post-engineering steps (`finalize`, `align`, `ready-for-publish`) are orchestrator states, not separate artifact directories.

## Allowed reopen targets

From the stage awaiting CEO review (or the stage CEO names as wrong):

| `current_stage` at gate | CEO may reopen to |
|---|---|
| `pm-prd` | `vp-brief` |
| `architecture` | `vp-brief`, `pm-prd` |
| `engineering` | `vp-brief`, `pm-prd`, `architecture` (if technical) |
| `engineering` (non-technical) | `vp-brief`, `pm-prd` |
| `finalize`, `align`, `ready-for-publish` | Any artifact stage above that exists for the project |

## Invalidation rule

**Invalidate** = every artifact stage **strictly after** the reopen target in the chain.

| Reopen target | `invalidated_stages` (technical) | `invalidated_stages` (non-technical) |
|---|---|---|
| `vp-brief` | `pm-prd`, `architecture`, `engineering` | `pm-prd`, `engineering` |
| `pm-prd` | `architecture`, `engineering` | `engineering` |
| `architecture` | `engineering` | — |

Do not delete files; mark artifacts non-authoritative for agents and publish.

## meta.yml updates (orchestrator)

On reopen to `{target}`:

```yaml
current_stage: {target}
stage_gate: agent_work
last_completed: {stage immediately before target, or null if target is vp-brief}
sub_status: draft
invalidated_stages: [{downstream stages per table}]
reopen_reason: "{CEO one-line reason}"
updated: {ISO date}
```

Clear `reopen_reason` after the target stage is CEO-approved again.

If reopening from `finalize` / `align` / `ready-for-publish`, also reset any engineering specs promoted to `review` back to `draft` with invalidation flags.

## Artifact marking

For each project artifact (not `handoff.md`, scaffolds, `README.md`, `retrieval-contract.md`) under invalidated stage directories:

```yaml
status: draft
invalidated: true
invalidated_at: {ISO-8601 timestamp}
invalidated_reason: "{reopen_reason}"
superseded_by_reopen_to: {target}
```

Agents and `align-*` must **not** treat invalidated artifacts as authoritative sources. Prefer upstream non-invalidated artifacts and standards.

## Handoff updates

**Target stage** `handoff.md` — add or update **Reopen context (PH-005)**:

```markdown
## Reopen context (PH-005)

| Field | Value |
|---|---|
| Reopened at | {ISO timestamp} |
| Invalidated stages | pm-prd, architecture, … |
| CEO reason | {reopen_reason} |
| Locks to reconfirm | {L- IDs from invalidated stages, or "none"} |
```

Move `L-` rows that originated only from invalidated stages into **Forwarded open decisions** or **Locks to reconfirm** until the CEO re-approves at the target gate.

**Invalidated stage** `handoff.md` — prepend:

```markdown
> **Superseded (PH-005):** Reopened to `{target}` on {date}. Do not use this handoff for new work.
```

## Locked decisions on reopen

| Lock source | After reopen |
|---|---|
| Stages before `{target}` | Remain locked |
| `{target}` stage (prior approval) | Treat as **proposed** until CEO re-approves at gate |
| Invalidated downstream stages | Move to reconfirm / forwarded open; do not enforce in new drafts |

## Orchestrator checklist

1. Confirm reopen target with CEO (show which stages will invalidate).
2. Update `meta.yml` per table above.
3. Mark invalidated artifacts (frontmatter).
4. Update target and invalidated `handoff.md` files.
5. Append `wiki/log.md`:
   ```
   ## [{ISO timestamp}] stage-reopen | {slug} | target={target} invalidated={list} reason={short}
   ```
6. Invoke the stage agent for `{target}` (do not skip to downstream agents).
7. On target re-approval: clear `invalidated_stages` entries for re-approved path, run PH-003 forward, continue chain.

## Log format

```
## [{ISO timestamp}] stage-reopen | {slug} | target=pm-prd invalidated=architecture,engineering reason="PRD scope wrong"
```

## See also

- PH-001: `templates/workspace/project-meta.yml.md`
- PH-003: `templates/workspace/inter-stage-contract.md`
- ADR: `docs/platform-decision-records/PH-2026-05-27-005-reopen-stage-protocol.md`
