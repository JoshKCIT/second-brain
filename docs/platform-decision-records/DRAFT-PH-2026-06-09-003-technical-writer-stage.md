# DRAFT ADR: PH-2026-06-09-003 - Technical Writer Stage

## Status

Draft

## Context

Profiles need a publish-shaped prose stage between engineering specs and finalize. Overlaps with finalize; this stage owns exemplar style, body-prose-clean prep, and See Also population per `docs/style/exemplar-published-doc.md`.

## Decision

Add `.github/prompts/workspace-technical-writer-agent.prompt.md` and optional chain stage `technical-writing` in profiles that include it (not required in default profile v1).

**Input contract:** Approved upstream stage artifacts + in-scope standards (retrieval contract).  
**Output contract:** Draft-tier edits to stage artifact or dedicated `technical-spec.md` per profile; `authored_by_agent: technical-writer`.

## Intent

- **In scope:** Prompt, routing-map row, profile optional stage slot.
- **Out of scope:** Autonomous publish; bypassing CEO gate.

## Approval

- Pending PIC; depends on PH-2026-06-09-001
