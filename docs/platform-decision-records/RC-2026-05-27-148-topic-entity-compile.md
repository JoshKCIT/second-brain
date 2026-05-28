# ADR: RC-2026-05-27-148 - Topic Entity Compile From Raw

## Status

Accepted (PIC-023, 2026-05-28)
## Approval

- Approved: 2026-05-28
- Cycle: PIC-023
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source Claim

- Claim ID: RC-2026-05-27-148
- Source transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
- Speaker: Matt Wolfe
- Timestamp: 00:05:30-00:06:30
- Claim type: workflow_proposal

## Context

Matt Wolfe's vault uses LLM-generated **topics** and **entities** with Wikipedia-style cross-links. Second Brain already has `workspace-concepts/` and `workspace-connections/` but compile prompts do not explicitly mirror topic/entity synthesis steps from Karpathy tutorials.

## Decision

Pilot explicit compile steps: from immutable raw sources, create or update concept articles and connection articles with mandatory `## Sources` sections and wikilinks traceable to raw paths—subject to align-cite before any publish-bound artifact cites them.

## Intent

- **Intended outcome:** Structured cross-link compile without embedding-only graphs or ungrounded LLM links.
- **In scope:** Compile prompt additions, one Confluence ingest pilot.
- **Out of scope:** Personal consumer topics vault as product direction (RC-152 rejected).

## Safety and non-goals

- **Safety posture:** Every new wikilink target must appear in Sources with section anchor; align-cite verifies excerpts.
- **Non-goals:** Autonomous nightly link mutation (RC-151 rejected).

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Captures teachable Karpathy cross-link value within Second Brain authority and citation discipline.

## Impact Scores

Total: 6 (experiment)

## Alternatives Considered

- Graph+embedding substrate (rejected: RC-109)
- Personal topics/entities PKM (rejected: RC-152)

## Consequences

### Positive

- Better navigation for compiled enterprise knowledge.

### Negative / Risks

- LLM may invent cross-links without raw support.

### Safeguards

- align-cite on pilot batch; reject links without matching raw excerpt.

## Validation Plan

One compile batch from Confluence raw: count new concepts/connections; run align-cite; measure false-link rate.

## Files Proposed for Future Change

- `.github/prompts/workspace-compile.prompt.md`
- `wiki/workspace-concepts/` (pilot articles only after user approval)
