# ADR: RC-2026-05-27-122 - Read-Before-Write Agent Principle

## Status

Accepted (PIC-2026-05-27-007, bundled with RC-157)
## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-007
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source Claim

- Claim ID: RC-2026-05-27-122
- Source transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
- Speaker: Noah Breyer
- Timestamp: 00:25:30-00:26:30
- Claim type: principle_claim

## Context

Speaker argues generative focus is overemphasized: models' read/comprehension capability is more useful day-to-day than writing. Second Brain already requires index-guided reads before compile (RC-001/002) but does not state read-before-write as an explicit agent operating principle.

## Decision

Codify read-before-write as a workspace agent default: agents must read scoped index/catalog and relevant sources before proposing artifact edits; retrieval and questioning precede generation.

## Intent

- **Intended outcome:** Stronger grounding and fewer uncited generations during project chains.
- **In scope:** Agent shims (`.cursor/rules`, `.github/copilot-instructions.md`, workspace prompts), align with RC-001 page-index retrieval.
- **Out of scope:** Banning all generation; replacing align-cite.

## Safety and non-goals

- **Safety posture:** Read steps are inspectable (logged paths); reads do not substitute citation verification.
- **Non-goals:** Mandating read of entire repo without scope config.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Reinforces governance-and-closure niche; aligns with inspectable retrieval policy already adopted.

## Impact Scores

Total: 11 (adopt)

## Alternatives Considered

- Implicit in existing prompts only (rejected: not consistently enforced)
- RAG-first generation (rejected: RC-002 similarity≠citation)

## Consequences

### Positive

- Clear operator expectation for all workspace agents

### Negative / Risks

- Slightly slower first response in sessions

### Safeguards

- Scope reads via `config/second-brain.yml`; log consulted articles in handoff

## Validation Plan

Review next three workspace agent runs for documented read list before first artifact write; align-cite pass rate baseline comparison.

## Files Proposed for Future Change

- `AGENTS.md` workspace agent section (after user approval)
- `.github/prompts/workspace-*.prompt.md`
- `.cursor/rules/agents.mdc`
