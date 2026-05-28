# ADR: PH-2026-05-27-003 - Inter-Stage Output Contract

## Status

Accepted (PIC-2026-05-27-013)
## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-013
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source

- Hygiene item: PH-2026-05-27-003
- Review: `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`
- Not a transcript-derived claim

## Context

RC-058 added per-stage `handoff.md` for session restart. PH-001 added `meta.yml` stage state. Gaps remained: downstream agents could re-litigate CEO-settled facts, and open questions did not accumulate across VP → PM → Architect → Engineer without the CEO re-explaining.

## Decision

Extend RC-058 handoff with **Locked decisions** and **Forwarded open decisions** sections. Orchestrator (`start-project`) owns population at CEO gates; downstream stage agents must read and honor forwarded state before drafting.

## Intent

- **Intended outcome:** Reduce rework and CEO re-explanation between chain stages.
- **In scope:** Handoff template, inter-stage contract template, agent prompt hooks, start-project gate forwarding.
- **Out of scope:** PH-004 advisory align-cite per stage (PH-005 implemented separately).

## Safety and non-goals

- **Safety posture:** Handoff remains draft-tier; excluded from publish set and finalize.
- **Non-goals:** Replacing stage artifact bodies; auto-promoting handoff to wiki.

## Rationale

Filesystem-first inspectability: the next agent reads one handoff file and sees cumulative locks and open forwards without parsing chat history.

## Alternatives Considered

- Embed forwards only in artifact bodies (rejected: session handoff and publish artifact conflated)
- New `decisions.yml` per project (rejected: extra file type; handoff already stage-scoped)

## Consequences

### Positive

- PM/Architect/Engineer invoke with explicit upstream decision state
- Cumulative locked decision IDs (`L-`) traceable across the chain

### Negative / Risks

- Stale forwards if orchestrator skips gate checklist
- Mitigation: log `stage-forward` entries; agents surface conflicts to CEO

## Implementation

| Artifact | Change |
|---|---|
| `templates/workspace/handoff.md` | Locked + forwarded open sections |
| `templates/workspace/inter-stage-contract.md` | Extraction map and obligations |
| `AGENTS.md` | PH-003 summary in agent chain section |
| `.github/prompts/workspace-*-agent.prompt.md` | Read/honor/forward hooks |
| `.github/prompts/workspace-start-project.prompt.md` | Gate forwarding checklist |

## See also

- RC-058: `docs/platform-decision-records/RC-2026-05-27-058-project-session-handoff.md`
- PH-001: `templates/workspace/project-meta.yml.md`
