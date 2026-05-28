# DRAFT ADR: RC-2026-05-27-142 - Weekly Pulse Disposable Report

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-142
- Source transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
- Speaker: Simon (Better Creating) / Jakob
- Timestamp: 00:10:00-00:10:30
- Claim type: workflow_proposal

## Context

Notion LifeOS command center emits a locked weekly pulse aggregating activity across databases — explicitly a read-only reporting view. Second Brain has `wiki/log.md`, workspace-lint reports, and deferred digest experiments (RC-011, RC-019) but no named weekly pulse artifact.

## Decision

Add an optional **weekly pulse** generator producing `reports/workspace-pulse-{date}.md` from log entries, active projects index, and latest lint summary — labeled disposable, never merged into wiki.

## Intent

- **Intended outcome:** CEO orientation snapshot without polluting canonical knowledge.
- **In scope:** Report generator script, template, no-telemetry local-only execution.
- **Out of scope:** PACT life dashboards; CRM/time-tracking aggregates.

## Safety and non-goals

- **Safety posture:** Read-only aggregation; no wiki/raw mutations.
- **Non-goals:** Autonomous weekly wiki optimization (RC-085 rejected class).

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Experiment RC-142; safer filesystem mapping of Notion command center.

## Impact Scores

Total: 7 (experiment)

## Alternatives Considered

- Obsidian dashboard embed (user preference; defer)
- Notion locked DB view (rejected: RC-131)

## Consequences

### Positive

- Faster weekly review; complements lint cadence

### Negative / Risks

- Misread as canonical if labeling weak

### Safeguards

- Frontmatter `disposable: true`, `type: orientation_report`; exclude from default compile/index

## Validation Plan

Generate one pulse; confirm zero wiki writes; CEO rates usefulness vs reading log.md directly.

## Files Proposed for Future Change

- `scripts/generate-workspace-pulse.py` (new)
- `templates/platform-research/weekly-pulse.md` (new)
