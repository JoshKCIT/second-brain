# DRAFT ADR: PH-2026-05-27-004 - Advisory align-cite per Stage

## Status

Accepted (PIC-2026-05-27-015)

## Source

- Hygiene item: PH-2026-05-27-004
- Review: `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`
- Depends on: RC-122 (read-before-write)
- Not a transcript-derived claim

## Context

RC-122 and RC-157 established read-before-write and citation-grounded query. Pre-publish `align-cite` (Step 12 in `start-project`) runs only after engineering finalize—late for catching citation drift in VP briefs, PRDs, and architecture docs. Stage agents produce fact-bearing claims at `draft` status; CEOs review artifacts without structural citation verification until the end of the chain.

## Decision

Add **PH-004 advisory align-cite**: an optional, non-blocking citation integrity check on the current stage artifact before each CEO gate. Uses the same three-layer verification as `/workspace-align-cite` with `--advisory` mode. Violations are reported but do not block gate progression.

## Intent

- **Intended outcome:** Surface DISPUTED and FABRICATION RISK citations early so CEOs fix upstream claims before downstream agents inherit them.
- **In scope:** Advisory mode in align-cite prompt, pre-gate offer in start-project, stage agent session-end hook, handoff advisory cite section.
- **Out of scope:** Replacing blocking pre-publish align-cite; auto-fixing violations; running advisory cite on handoff or scaffold files.

## Safety and non-goals

- **Safety posture:** Advisory only—CEO may skip; orchestrator never blocks PH-003 forward or PH-005 reopen on advisory failures.
- **Non-goals:** Mandatory cite checks at draft; lint integration; changing publish gate criteria.

## Rationale

Early feedback reduces rework: a PM PRD citing a non-existent standard is cheaper to fix at the PM gate than after architecture and engineering build on it. Optional preserves CEO velocity when citations are thin at VP stage.

## Alternatives Considered

- Mandatory align-cite at every gate (rejected: too slow for strategic VP briefs with few citations)
- Separate `align-cite-lite` prompt (rejected: duplicate verification logic; `--advisory` flag suffices)
- Only engineer-stage advisory (rejected: hygiene review identified all four gates)

## Consequences

### Positive

- CEOs see citation violations before approving stage handoff
- Handoff records last advisory run for session resume
- Same verification layers as publish gate; consistent ratings

### Negative / Risks

- CEOs may skip and defer problems to Step 12 anyway
- Mitigation: stage agents recommend advisory cite when artifact has 5+ cited claims or vendor-domain assertions

## Implementation

| Artifact | Change |
|---|---|
| `templates/workspace/advisory-align-cite-per-stage.md` | Protocol reference |
| `.github/prompts/workspace-align-cite.prompt.md` | `--advisory` mode, report naming, non-blocking pass/fail |
| `.github/prompts/workspace-start-project.prompt.md` | Pre-gate offer at Steps 4, 6, 9, 10b |
| `.github/prompts/workspace-*-agent.prompt.md` | Session-end offer + handoff update |
| `templates/workspace/handoff.md` | Advisory cite check section |
| `AGENTS.md` | PH-004 summary in agent chain section |

## See also

- RC-122 ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-122-read-before-write-retrieval.md`
- PH-003 ADR: `docs/platform-decision-records/DRAFT-PH-2026-05-27-003-inter-stage-output-contract.md`
- align-cite prompt: `.github/prompts/workspace-align-cite.prompt.md`
