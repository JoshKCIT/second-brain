# DRAFT ADR: RC-2026-05-27-050 - Verbatim Cite Excerpts in Align Reports

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-050
- Source transcript: raw/platform-transcripts/Remio.ai_Review_-_The_Ultimate_AI_Second_Brain_That_is_So_Much_More_vs._Alter_AI.txt
- Speaker: unknown
- Timestamp: 00:10:30-00:11:00
- Claim type: product_requirement

## Context

Remio exposes an optional "LLM dump" that includes verbatim quotes with navigation anchors for precise citation review. Second Brain already runs `align-cite` before publish but reports may not surface excerpt text inline.

## Decision

Add an optional `verbatim_excerpt` field to structured `align-cite` violation/success rows when the cited source supports it.

## Intent

- **Intended outcome:** Faster human verification of citations at review/publish without opening every raw file.
- **In scope:** Report format only; optional flag default off until pilot passes.
- **Out of scope:** Changing wiki article bodies; auto-trusting excerpts without source open.

## Safety and non-goals

- **Safety posture:** Excerpts are evidence pointers, not new canonical claims.
- **Non-goals:** Replacing full `align-cite` source reads; passive background indexing.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Improves inspectability and human review leverage (closure-compile brief) with minimal canonical risk.

## Impact Scores

Total: 10 (experiment)

## Alternatives Considered

- Status quo text-only violation messages
- Always-on excerpts (rejected: token/report bloat)

## Consequences

### Positive

- Faster CEO review before publish

### Negative / Risks

- Verbose reports; agents might treat excerpts as sufficient without full check

### Safeguards

- Keep align-cite as blocking gate; excerpts supplementary only

## Validation Plan

Pilot on one `review` artifact; measure time-to-verify and false positives.

## Files Proposed for Future Change

- `.github/prompts/workspace-align-cite.prompt.md`
- `reports/` align-cite output template (if codified)
