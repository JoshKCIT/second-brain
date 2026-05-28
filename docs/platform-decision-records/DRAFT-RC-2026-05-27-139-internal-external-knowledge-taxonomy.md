# DRAFT ADR: RC-2026-05-27-139 - Internal vs External Knowledge Taxonomy

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-139
- Source transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
- Speaker: Simon (Better Creating)
- Timestamp: 00:12:30-00:13:00
- Claim type: workflow_proposal

## Context

Notion LifeOS splits knowledge into internal notes vs external references/clippings, with meeting notes in a separate lane. Second Brain already separates `raw/workspace-confluence/` (internal) and `raw/workspace-external/` (vendor) but compile policy does not always surface `capture_lane` explicitly at ingest.

## Decision

Require `capture_lane: internal | external` (and optional `capture_type: meeting | reference | standard`) in raw frontmatter at ingest; compile routes accordingly.

## Intent

- **Intended outcome:** Fewer authority conflicts; clearer align-vendor-truth behavior.
- **In scope:** Ingest frontmatter schema, compile routing hints, lint check.
- **Out of scope:** Personal habit/workout tracking lanes.

## Safety and non-goals

- **Safety posture:** External lane requires vendor/domain tags before wiki promotion.
- **Non-goals:** Merging meeting transcripts directly into workspace-standards without review.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Experiment RC-139; highest score (+10) in Notion review batch; aligns with claim-domain authority model.

## Impact Scores

Total: 10 (experiment)

## Alternatives Considered

- Folder-only separation (partially exists; less explicit at compile)
- Single mixed knowledge base (rejected: speaker and Second Brain both reject)

## Consequences

### Positive

- Stronger vendor-truth routing; less clutter in concept articles

### Negative / Risks

- Mis-tagged ingest requires quarantine rework

### Safeguards

- Ingest lint validates capture_lane; compile fails closed on missing external domain tag

## Validation Plan

Pilot one Confluence + one vendor ingest batch; run align-vendor-truth on compiled output.

## Files Proposed for Future Change

- `.github/prompts/workspace-ingest-confluence.prompt.md`
- `.github/prompts/workspace-ingest-vendor-doc.prompt.md`
- `scripts/lint-platform-research.py` or workspace lint rules
