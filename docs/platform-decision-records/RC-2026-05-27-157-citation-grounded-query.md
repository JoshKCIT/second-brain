# ADR: RC-2026-05-27-157 - Citation-Grounded Query Responses

## Status

Accepted (PIC-2026-05-27-007, bundled with RC-122)
## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-007
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source Claim

- Claim ID: RC-2026-05-27-157
- Source transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
- Speaker: Matt Wolfe
- Timestamp: 00:10:30-00:11:30
- Claim type: principle_claim

## Context

Matt Wolfe queries his wiki for AEO strategy and receives a concise answer with an explicit list of wiki sources referenced. Second Brain's `workspace-query` operation already requires index-guided reads and section-anchored citations, but does not always surface a visible **Sources consulted** block in every query response.

## Decision

Codify **citation-grounded query** as a default: every workspace query response lists consulted wiki/raw paths (and external vendor cache paths when used) before synthesis; retrieval lists do not substitute for align-cite at publish time (RC-002).

## Intent

- **Intended outcome:** Auditable query answers matching practitioner expectations from Karpathy demos.
- **In scope:** `workspace-query` prompt, optional Q&A filing format in `wiki/workspace-qa/`.
- **Out of scope:** Auto-writing query results to wiki without review (RC-101 rejected).

## Safety and non-goals

- **Safety posture:** Listed sources must exist on disk; user can verify paths immediately.
- **Non-goals:** Treating source list as align-cite pass for publish-bound artifacts.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Reinforces governance-and-closure niche vs generic ChatGPT answers; complements RC-122 read-before-write.

## Impact Scores

Total: 11 (adopt)

## Alternatives Considered

- RAG confidence as citation (rejected: RC-002)
- Parametric LLM answers without source list (rejected)

## Consequences

### Positive

- Faster human verification of query grounding.

### Negative / Risks

- Verbose responses if source lists are duplicated unnecessarily.

### Safeguards

- Scope source list to articles actually read; dedupe paths.

## Validation Plan

Run three workspace queries; verify each response includes consulted paths that exist; spot-check one claim against source text.

## Files Proposed for Future Change

- `.github/prompts/workspace-query.prompt.md`
- `AGENTS.md` §4 Query (Sources consulted requirement)
