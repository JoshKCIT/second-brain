# DRAFT ADR: RC-2026-05-27-055 - Identity Packs Before Compile

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-055
- Source transcript: raw/platform-transcripts/The_AI-Native_Shift_-_Second_Brain_for_AI_with_George_B._Thomas.txt
- Speaker: George B. Thomas
- Timestamp: 00:16:30-00:18:30
- Claim type: product_requirement

## Context

Practitioner loads structured identity files (voice, values, personas) before generation so the model does not guess tone. Second Brain has persona stubs under `templates/personas/` but workspace agent prompts do not require loading them at compile time.

## Decision

Require workspace VP/PM/Engineer agent prompts to load a declared identity pack path (project or client) before drafting stage artifacts.

## Intent

- **Intended outcome:** Publishable artifacts need fewer tone corrections; internal rules inlined with correct voice.
- **In scope:** Prompt contracts, persona template schema, project frontmatter `identity_pack:` optional field.
- **Out of scope:** Autonomous identity mutation; CRM command-center features.

## Safety and non-goals

- **Safety posture:** Identity packs are recommendation-tier inputs; standards still cite authority-tagged sources.
- **Non-goals:** Replacing align-cite; merging client identities without explicit path.

## Regulatory posture (optional)

- **Legal/regulatory claims:** unvalidated (client compliance in personas)
- **Notes:** Validate client packs with legal on pilot only.

## Rationale

Direct compile-for-publish grounding per closure-compile brief (RC-054 reinforcement).

## Impact Scores

Total: 9 (experiment)

## Alternatives Considered

- Ad-hoc tone instructions in chat only (rejected: not durable)
- Full identity inheritance tree in v1 (defer to RC-062 phase 2)

## Consequences

### Positive

- Less guessing; better closure on voice-sensitive deliverables

### Negative / Risks

- Stale personas; maintenance burden

### Safeguards

- CEO edits persona files; version in git; no auto-update from transcripts

## Validation Plan

A/B one VP brief with and without identity pack; measure edit distance and tone violations.

## Files Proposed for Future Change

- `.github/prompts/workspace-vp-agent.prompt.md`
- `.github/prompts/workspace-pm-agent.prompt.md`
- `.github/prompts/workspace-engineer-agent.prompt.md`
- `templates/personas/` (schema README)
