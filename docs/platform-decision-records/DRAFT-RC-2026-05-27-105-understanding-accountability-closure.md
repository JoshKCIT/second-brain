# DRAFT ADR: RC-2026-05-27-105 - Understanding and Accountability Closure

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-105 (bundles RC-2026-05-27-115 reinforcement)
- Source transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
- Speaker: Dr Vivian Balakrishnan
- Timestamp: 00:01:30-00:02:00; 00:14:30-00:15:00
- Claim type: principle_claim

## Context

Keynote states personal understanding cannot be outsourced and accountability cannot be delegated. Second Brain's jr-engineer closure rule already requires inlined rules at publish, but agents can still produce fluent prose that **looks** complete while outsourcing comprehension to the model.

## Decision

Add explicit **understanding/accountability checkpoints** to finalize and publish workflows: (1) reviewer confirms inlined rules are sufficient without opening wiki links; (2) CEO explicit approval between agent stages remains mandatory; (3) publish prompt includes a non-delegable comprehension attestation line for the human reviewer.

## Intent

- **Intended outcome:** Published artifact sets remain executable by juniors because a human owner verified comprehension, not because the model sounded confident.
- **In scope:** Finalize prompt, publish prompt, workspace agent handoff templates.
- **Out of scope:** Automated comprehension scoring; parliamentary auto-answers.

## Safety and non-goals

- **Safety posture:** Agents draft; humans own sign-off—no autonomous publish.
- **Non-goals:** WhatsApp always-on agents; delegating accountability to sub-agents without CEO review.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

RC-105 total +11, RC-115 total +9; both validated against `AGENTS.md` agent chain and closure rules.

## Impact Scores

Combined governance +2, closure +2, human_review_leverage +2, enterprise_fit +2.

## Alternatives Considered

- Trust model fluency at review — rejected.
- Remove CEO checkpoints for speed — rejected.

## Consequences

### Positive

- Stronger governance story for enterprise adopters.

### Negative / Risks

- Additional reviewer friction.

### Safeguards

- Attestation is one line in publish checklist, not a new artifact type.

## Validation Plan

One project artifact set: reviewer completes attestation; junior executes from published set only.

## Files Proposed for Future Change

- `.github/prompts/finalize.prompt.md`
- `.github/prompts/workspace-publish.prompt.md`
- `wiki/workspace-projects/{slug}/` handoff templates (user-approved)
