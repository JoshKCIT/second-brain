# ADR: RC-2026-05-27-058 - Project Session Handoff Files

## Status

Accepted (PIC-2026-05-27-010)
## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-010
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source Claim

- Claim ID: RC-2026-05-27-058
- Source transcript: raw/platform-transcripts/The_AI-Native_Shift_-_Second_Brain_for_AI_with_George_B._Thomas.txt
- Speaker: George B. Thomas
- Timestamp: 00:32:00-00:33:00
- Claim type: workflow_proposal

## Context

Speaker uses a "save context" step to persist next actions and restart facts across sessions. Second Brain uses stage directories but lacks a standard handoff artifact between agent sessions.

## Decision

Introduce optional `handoff.md` per project stage with schema: next_steps, starting_context, open_decisions, last_session.

## Intent

- **Intended outcome:** Multi-day project chains resume without cross in-progress wikilinks or chat-only memory.
- **In scope:** Template + finalize/workspace-engineer prompt hook to write/update handoff at session end.
- **Out of scope:** Autonomous wiki mutation (slash dream pattern).

## Safety and non-goals

- **Safety posture:** Handoff is draft-tier project state; not published canonical knowledge.
- **Non-goals:** Replacing stage artifact bodies; syncing to external CRM.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Supports junior-engineer closure across sessions via filesystem-first inspectability.

## Impact Scores

Total: 10 (experiment)

## Alternatives Considered

- Rely on chat transcripts only (rejected)
- Store handoff only in wiki/log (rejected: not stage-scoped)

## Consequences

### Positive

- Clear restart for CEO and next agent in chain

### Negative / Risks

- Stale handoffs if not updated

### Safeguards

- Engineer finalize prompts user to confirm handoff accuracy

## Validation Plan

One pilot project uses handoff.md for two sessions; measure successful resumption without re-explaining context.

## Files Proposed for Future Change

- `templates/workspace/handoff.md` (template) — **done**
- `.github/prompts/workspace-engineer-agent.prompt.md` (finalize hook + exclusions) — **done**
- `.github/prompts/workspace-start-project.prompt.md` (skeleton + resumability) — **done**
- `.github/prompts/workspace-{vp,pm,architect,engineer}-agent.prompt.md` (session read/write) — **done**
- `AGENTS.md` (agent chain note) — **done**
- `wiki/platform-research/open-hypotheses.md` (H-009 active) — **done**
