# Platform ADR Template

Use for **proposed** platform decision records under `docs/platform-decision-records/DRAFT-{claim_id}-{short-title}.md`. On PIC accept, **`platform-implement-backlog`** runs `python scripts/promote-platform-adr.py --root . --claim-id {claim_id} --pic-cycle {cycle}` → `{claim_id}-{short-title}.md` with H1 `# ADR:`.

See `docs/platform-decision-records/README.md`.

Experiment (RC-2026-05-27-015): include **Intent**, **Safety and non-goals**, and optional **Regulatory posture** on new platform ADRs. Keep each field brief and decision-focused.

```markdown
# DRAFT ADR: {Claim ID} - {Short Title}

## Status

Draft

## Source Claim

- Claim ID:
- Source transcript:
- Speaker:
- Timestamp:
- Claim type:

## Context

## Decision

## Intent

- **Intended outcome:**
- **In scope:**
- **Out of scope:**

## Safety and non-goals

- **Safety posture:**
- **Non-goals:**

## Regulatory posture (optional)

- **Legal/regulatory claims:** none | unvalidated | validated
- **Notes:**

## Rationale

## Impact Scores

## Alternatives Considered

## Consequences

### Positive

### Negative / Risks

### Safeguards

## Validation Plan

## Files Proposed for Future Change
```

Canonical copy: `docs/platform-decision-records/DRAFT-template-research-claim.md`

Experiment ADR: `docs/platform-decision-records/RC-2026-05-27-015-lightweight-intent-records.md`

Validation: use intent sections on the next three platform ADRs; remove if they add noise without improving review clarity.
