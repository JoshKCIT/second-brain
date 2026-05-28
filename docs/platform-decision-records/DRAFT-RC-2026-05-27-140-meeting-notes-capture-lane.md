# DRAFT ADR: RC-2026-05-27-140 - Meeting Notes Capture Lane

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-140
- Source transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
- Speaker: Simon (Better Creating)
- Timestamp: 00:17:30-00:20:00
- Claim type: workflow_proposal

## Context

Speaker advocates a dedicated meeting-notes area separate from reference knowledge, with optional task extraction. Second Brain uses `raw/platform-transcripts/` for product intelligence with skeptical review; workspace meeting capture lane is undefined. RC-144 rejects auto task promotion without approval.

## Decision

Define `raw/workspace-meetings/{slug}/transcript.md` for workspace-lane meeting evidence; compile to wiki only after explicit CEO approval; task extractions go to `reports/` drafts, not directly to project artifacts.

## Intent

- **Intended outcome:** Conversational evidence preserved immutably; curated knowledge stays citation-grounded.
- **In scope:** Raw path schema, ingest prompt, compile gate, platform-transcript-librarian pattern reuse.
- **Out of scope:** Notion AI meeting notes as required capture tool (RC-145 monitor only).

## Safety and non-goals

- **Safety posture:** Meeting raw is evidence; never canonical wiki without compile + align-cite.
- **Non-goals:** RC-144 auto task database writes.

## Regulatory posture (optional)

- **Legal/regulatory claims:** unvalidated (meeting recording consent)
- **Notes:** Enterprise pilots need legal review on recording policy.

## Rationale

Experiment RC-140; extends proven platform-transcript pattern to workspace meetings.

## Impact Scores

Total: 8 (experiment)

## Alternatives Considered

- Store meetings in wiki/workspace-qa directly (rejected: bypasses raw immutability)
- Notion-native meeting store (rejected: RC-131)

## Consequences

### Positive

- Clear separation of conversation vs compiled standards/concepts

### Negative / Risks

- Extra ingest verb and approval friction

### Safeguards

- Mirror platform-transcript-librarian checkpoints; reject RC-144 automation path

## Validation Plan

One meeting ingest pilot; verify compile gate and no auto wiki writes.

## Files Proposed for Future Change

- `raw/README.md` (structure)
- `.github/prompts/workspace-ingest-meeting.prompt.md` (new, optional v1.x)
