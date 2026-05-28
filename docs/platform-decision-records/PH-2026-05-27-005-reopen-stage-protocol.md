# ADR: PH-2026-05-27-005 - Reopen Stage Protocol

## Status

Accepted (PIC-2026-05-27-014)
## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-014
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source

- Hygiene item: PH-2026-05-27-005
- Review: `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`
- Depends on: PH-001 (meta.yml stage state)
- Not a transcript-derived claim

## Context

PH-001 added resumable `current_stage` / `stage_gate` / `last_completed`. PH-003 forwarded decisions across stages. There was no documented behavior when the CEO rejects downstream work because an upstream artifact is wrong—agents could still cite stale PRD, architecture, or engineering specs.

## Decision

Add **PH-005 reopen protocol**: CEO may reopen to an earlier artifact stage; orchestrator updates `meta.yml`, marks downstream artifacts `invalidated: true`, updates handoffs, and resumes the chain at the target stage.

## Intent

- **Intended outcome:** Inspectable rollback without deleting audit history.
- **In scope:** Reopen template, meta.yml fields, start-project CEO gate option, agent do-not-cite-invalidated rule.
- **Out of scope:** Automatic git revert; cross-project invalidation.

## Safety and non-goals

- **Safety posture:** Invalidated artifacts stay on disk but are excluded from authoritative source lists and publish sets until re-approved.
- **Non-goals:** Silently rewriting downstream bodies; removing PH-003 lock history without CEO reconfirm.

## Rationale

Filesystem-first audit trail: `wiki/log.md` records `stage-reopen` events; frontmatter flags make staleness machine-checkable.

## Alternatives Considered

- Delete downstream directories (rejected: loses audit trail)
- Only meta.yml rollback without artifact flags (rejected: agents could still read stale specs)

## Consequences

### Positive

- Clear CEO path when PRD/architecture/engineering must be redone
- Align and finalize steps can reset without ambiguous state

### Negative / Risks

- Forgetting to clear `invalidated_stages` after re-approval
- Mitigation: orchestrator checklist clears flags on PH-003 forward after target gate

## Implementation

| Artifact | Change |
|---|---|
| `templates/workspace/reopen-stage-protocol.md` | Protocol reference |
| `templates/workspace/project-meta.yml.md` | `invalidated_stages`, `reopen_reason` |
| `templates/workspace/handoff.md` | Reopen context section |
| `.github/prompts/workspace-start-project.prompt.md` | CEO reopen branch + checklist |
| Stage agent prompts | Skip invalidated sources |

## See also

- PH-003 ADR: `docs/platform-decision-records/PH-2026-05-27-003-inter-stage-output-contract.md`
