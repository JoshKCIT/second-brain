# DRAFT ADR: RC-2026-05-27-130 - Project Stage Evidence Scaffold

## Status

Accepted (PIC-2026-05-27-011)

## Source Claim

- Claim ID: RC-2026-05-27-130
- Source transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
- Speaker: Noah Breyer
- Timestamp: 00:16:00-00:17:00
- Claim type: workflow_proposal

## Context

Speaker organizes in-progress talk work into subfolders: `chats/`, `daily-progress/`, `research/`, and ad hoc thinking notes. Second Brain has stage directories but no standard scaffold for draft-tier evidence and session continuity (extends RC-058 handoff).

## Decision

Introduce optional scaffold under `wiki/workspace-projects/{slug}/0X-{stage}/`:

- `research/` — clipped sources and reading notes (draft, authority-tagged)
- `chats/` — imported external chat transcripts (informational, not canonical)
- `daily-progress/` — dated session summaries
- `handoff.md` — per RC-058

All scaffold contents remain `draft` and excluded from published artifact set until compiled into stage artifacts.

## Intent

- **Intended outcome:** Multi-day project resumption without chat-only memory; supports RC-118/119 catch-up reads.
- **In scope:** Template in `templates/workspace/`, workspace-start-project hook.
- **Out of scope:** PARA vault-wide organization; auto-promotion to wiki.

## Safety and non-goals

- **Safety posture:** Scaffold files never satisfy jr-engineer closure alone; publish set remains stage artifacts after align-cite.
- **Non-goals:** Merging personal Obsidian vaults; consumer PKM product features.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Filesystem-first session continuity with inspectable dated reads; complements RC-058 without cross in-progress wiki dependencies.

## Impact Scores

Total: 9 (experiment)

## Alternatives Considered

- Single handoff.md only (insufficient for dated catch-up)
- Wiki workspace-qa auto-capture (rejected: RC-040 pattern)

## Consequences

### Positive

- Transparent project archaeology for CEO and agents

### Negative / Risks

- Folder proliferation if not cleaned at publish

### Safeguards

- Archive scaffold to project addendum or delete at publish transition

## Validation Plan

Pilot on one active project for two weeks; measure successful "catch up last N days" resumption without re-explaining context.

## Files Proposed for Future Change

- `templates/workspace/project-stage-scaffold/` — **done**
- `.github/prompts/workspace-start-project.prompt.md` — **done**
- `.github/prompts/workspace-{vp,pm,architect,engineer}-agent.prompt.md` — **done**
- `.github/prompts/workspace-engineer-agent.prompt.md` (finalize exclusions) — **done**
- `.github/prompts/workspace-publish.prompt.md` (scaffold cleanup) — **done**
- `AGENTS.md` — **done**
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md` (cross-link via templates) — **done**
