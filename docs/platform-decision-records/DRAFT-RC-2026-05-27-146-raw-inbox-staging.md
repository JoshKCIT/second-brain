# DRAFT ADR: RC-2026-05-27-146 - Raw Inbox Staging Lane

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-146
- Source transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
- Speaker: Matt Wolfe
- Timestamp: 00:07:30-00:08:30
- Claim type: workflow_proposal

## Context

Karpathy/Codex tutorials teach a `raw/` inbox for unprocessed clips. Second Brain already uses immutable `raw/` but does not always document inbox staging vs curated `wiki/` in ingest prompts. Matt Wolfe dumps Chrome clips into `raw/` and compiles on demand—Second Brain must keep compile approval-gated.

## Decision

Document and pilot an explicit **raw inbox staging** convention: captures land in scoped `raw/` paths with authority/domain frontmatter; compile into `wiki/` only after explicit user approval per batch.

## Intent

- **Intended outcome:** Teachable Karpathy clipper workflow without nightly or implicit auto-compile.
- **In scope:** Ingest/compile prompt text, optional lint for unprocessed raw orphan hints.
- **Out of scope:** Chrome clipper integration; unattended schedulers.

## Safety and non-goals

- **Safety posture:** `raw/` remains immutable after write; compile logs paths to `wiki/log.md`.
- **Non-goals:** Consumer clipper as default workspace substrate (RC-150 rejected).

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Separates capture from curation while preserving approval-gated mutations. Safer variant of Matt Wolfe's inbox pattern.

## Impact Scores

Total: 7 (experiment)

## Alternatives Considered

- Nightly auto-process (rejected: RC-151)
- Clip directly to wiki (rejected: RC-104)

## Consequences

### Positive

- Clear operator mental model: inbox vs curated knowledge.

### Negative / Risks

- Operators may skip approval on "small" batches.

### Safeguards

- Compile prompt requires explicit user confirmation; lint flags unprocessed raw without blocking.

## Validation Plan

One user-approved ingest batch: clip or ingest → raw/ → explicit compile → verify wiki Sources link back to raw.

## Files Proposed for Future Change

- `.github/prompts/workspace-compile.prompt.md`
- `.github/prompts/workspace-ingest-vendor-doc.prompt.md` (inbox staging note)
