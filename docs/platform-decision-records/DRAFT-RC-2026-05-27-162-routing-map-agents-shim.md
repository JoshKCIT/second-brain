# DRAFT ADR: RC-2026-05-27-162 - Routing Map in AGENTS Shim

## Status

Accepted (PIC-2026-05-27-020)

## Source Claim

- Claim ID: RC-2026-05-27-162
- Source transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
- Speaker: Jeff
- Timestamp: 00:07:00-00:07:30
- Claim type: workflow_proposal

## Context

Jeff's root CLAUDE.md includes a routing map table mapping task types to workstation folders. Second Brain has index-guided retrieval (RC-001) and retrieval-contract-first (RC-018) but no explicit task→path routing table in agent shims.

## Decision

Add an optional **Routing map** section to AGENTS shims: task type → prompt verb, wiki subtree, or project stage path. Table is orientation-only; does not auto-load content or bypass align-cite.

## Intent

- **Intended outcome:** Agents pick correct compile/query scope on first read.
- **In scope:** Template table, RC-135 agent hub cross-link, platform vs workspace lane rows.
- **Out of scope:** Auto-retrieval; Cowork workstation folders for personal life.

## Safety and non-goals

- **Safety posture:** Routing map entries must point to approval-gated operations where mutations occur.
- **Non-goals:** Replacing wiki/index.md catalog; vector routing.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Inspectability win with low canonical risk if kept in shims and updated with prompt changes.

## Impact Scores

Total: 8 (experiment)

## Alternatives Considered

- Wiki-only navigation — insufficient for verb→prompt mapping.
- Full Cowork routing table copy — rejected (life-OS paths).

## Consequences

### Positive

- Fewer mis-routed platform vs workspace reads.

### Negative / Risks

- Stale rows if prompts rename without table update.

### Safeguards

- Lint check for broken routing targets optional in v1 pilot.

## Validation Plan

5-task holdout: compile, query, platform-research-review, align-cite, publish — measure mis-routed reads vs baseline.

## Files Proposed for Future Change

- `AGENTS.md` (routing section) — **done**
- `templates/workspace/routing-map.md` (new) — **done**
- `.cursor/rules/agents.mdc`, `CLAUDE.md`, `.github/copilot-instructions.md` — **done**
- `.github/prompts/workspace-start-project.prompt.md` (PH-006 escalation) — **done**
- `.github/prompts/workspace-lint.prompt.md` (routing freshness advisory) — **done**
- PH-2026-05-27-006 bundled — **done** (platform escalation row)
