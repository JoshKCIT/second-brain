# DRAFT ADR: RC-2026-05-27-165 - Lean Root Pointer Resources

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-165
- Source transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
- Speaker: Jeff
- Timestamp: 00:07:30-00:20:00
- Claim type: architecture_proposal

## Context

Jeff keeps root CLAUDE.md under ~300 lines and uses pointer references to resources loaded on demand. Second Brain AGENTS.md and shims grow with platform research; RC-018 retrieval contract supports bundle fields loaded when needed.

## Decision

Audit root shims for lean default load: keep governance invariants and routing in root; move extended examples, persona detail, and operation deep-dives to pointer files under `templates/` or `docs/` loaded on explicit read or task match.

## Intent

- **Intended outcome:** Lower default context while preserving fail-closed rules in every session.
- **In scope:** Shim audit, pointer file convention, mandatory-read list for critical rules.
- **Out of scope:** Model tier selection (RC-174); removing governance rules from default load.

## Safety and non-goals

- **Safety posture:** Critical rules (approval gates, align-cite, closure) stay in default-loaded root shim.
- **Non-goals:** Hiding governance in rarely-loaded pointers.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Operational hygiene aligned with RC-018 and RC-161 stacking.

## Impact Scores

Total: 7 (experiment)

## Alternatives Considered

- Monolithic AGENTS.md — maintainability and token cost regression.
- Cowork 00_resources life folders — rejected (RC-168).

## Consequences

### Positive

- Cheaper frequent sessions; clearer separation of core vs reference material.

### Negative / Risks

- Agents skip pointer reads unless routing map or prompt enforces them.

### Safeguards

- Retrieval contract checklist marks mandatory vs optional bundle fields.

## Validation Plan

Line-count audit before/after; 5 compile tasks verify mandatory rules still loaded; optional pointers read when task requires.

## Files Proposed for Future Change

- `AGENTS.md` (pointer section — user-approved)
- `.cursor/rules/agents.mdc`
- `templates/workspace/pointer-resources/` (new convention doc)
