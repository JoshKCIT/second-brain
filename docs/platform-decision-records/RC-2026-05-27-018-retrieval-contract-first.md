# ADR: RC-2026-05-27-018 - Retrieval Contract First

## Status

Accepted (PIC-2026-05-27-008)
## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-008
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Source Claim

- Claim ID: RC-2026-05-27-018
- Source transcript: raw/platform-transcripts/Pinecone_Just_Demoted_Vector_Search._Here_s_the_Knowledge_Layer.txt
- Speaker: unknown
- Timestamp: "00:14:30-00:17:00"
- Claim type: workflow_proposal

## Context

Transcript evidence argues agents fail when builders pick a database (vector, graph, lakehouse) before defining what context the agent must receive—field by field, with authority, freshness, and permissions. Second Brain already enforces scoped retrieval and authority tags but lacks an explicit **retrieval contract** checklist at compile time.

## Decision

Add a lightweight retrieval-contract step to `workspace-compile` and project authoring workflows: before retrieval or orientation, document the bundle shape (fields, sources, authority, freshness rules) for the artifact being drafted. Storage/index choice follows the contract; hybrid retrieval remains eval-gated.

## Intent

- **Intended outcome:** Compile-time pulls the right standards and sources; published sets remain jr-engineer-executable with inlined rules.
- **In scope:** Checklist template, compile/query prompt guidance, orientation-map inputs for RC-009.
- **Out of scope:** New vector/graph databases, vendor stack selection, auto-assembled bundles without align-cite.

## Safety and non-goals

- **Safety posture:** Fail closed—missing authority or freshness on a bundle field blocks publish until resolved or explicitly waived.
- **Non-goals:** Database-first architecture; maximum context dumping; treating orientation maps as canonical truth.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Aligns with closure-compile brief: authoring-time assembly vs publish-time self-containment. Reinforces RC-001/002 without mandating embeddings.

## Impact Scores

governance +2, closure +1, grounding +1, inspectability +2, enterprise_fit +2 — total +11 (adopt band).

## Alternatives Considered

- Default vector index first — rejected (RC-002 similarity≠support).
- Skip contract; rely on wiki/index only — insufficient for multi-source bundles.

## Consequences

### Positive

- Clearer compile handoffs; fewer blind reads; evaluable bundle completeness.

### Negative / Risks

- Checklist overhead for small artifacts; teams may treat it as bureaucracy.

### Safeguards

- Optional for single-source Q&A; mandatory for multi-standard project artifacts at review status.

## Validation Plan

- Run 5 project compile sessions with contract checklist vs baseline; measure align-cite pass rate and orientation read count.

## Files Proposed for Future Change

- `.github/prompts/workspace-compile.prompt.md` (contract step) — **done**
- `templates/workspace/retrieval-contract-checklist.md` (new) — **done**
- `AGENTS.md` (compile operation note) — **done**
- `.github/prompts/workspace-query.prompt.md` (multi-source contract) — **done**
- `.github/prompts/workspace-start-project.prompt.md` (retrieval-contract.md skeleton) — **done**
- `.github/prompts/workspace-engineer-agent.prompt.md` (finalize gate) — **done**
