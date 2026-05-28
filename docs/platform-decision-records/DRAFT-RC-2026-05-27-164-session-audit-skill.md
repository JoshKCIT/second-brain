# DRAFT ADR: RC-2026-05-27-164 - Session Audit Skill

## Status

Accepted (PIC-2026-05-27-019)

## Source Claim

- Claim ID: RC-2026-05-27-164
- Source transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
- Speaker: Jeff
- Timestamp: 00:18:30-00:19:30
- Claim type: workflow_proposal

## Context

Jeff uses a `/session audit` Cowork skill to extract unsaved preferences at session end. Second Brain lacks a structured close step that proposes orientation updates with explicit approval.

## Decision

Add optional `.github/skills/session-audit/` skill invoked at session end (or via finalize prompt) that: (1) scans conversation for preferences/principles, (2) outputs proposed orientation/handoff diffs, (3) writes only after explicit user approval.

## Intent

- **Intended outcome:** Capture session learnings with audit trail; replace silent memory.md writes.
- **In scope:** Skill template, proposal-only default, integration with RC-163 orientation and RC-058 handoff.
- **Out of scope:** Auto wiki mutation; Gmail/Notion connector actions.

## Safety and non-goals

- **Safety posture:** Proposal-only mode default; writes require user confirm per item.
- **Non-goals:** Nightly autonomous preference extraction (RC-059 pattern).

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Governance-friendly alternative to Cowork "remember this" without validation.

## Impact Scores

Total: 10 (experiment band — pilot first)

## Alternatives Considered

- Chat-only handoff — insufficient audit trail.
- Auto memory.md — rejected (RC-169).

## Consequences

### Positive

- Human review leverage at session boundary.

### Negative / Risks

- Skill over-captures chat noise as "principles."

### Safeguards

- Output classified: orientation | handoff | reject; user selects before write.

## Validation Plan

Three pilot sessions; count proposals vs accepted writes; verify zero unapproved file mutations.

## Files Proposed for Future Change

- `.github/skills/session-audit/SKILL.md` (new) — **done**
- `.github/prompts/workspace-session-audit.prompt.md` — **done**
- `templates/workspace/session-audit-checklist.md` — **done**
- `.github/prompts/workspace-{vp,pm,architect,engineer}-agent.prompt.md` (session-end offer) — **done**
- `.github/prompts/workspace-start-project.prompt.md` (resumability hook) — **done**
- `.github/prompts/workspace-engineer-agent.prompt.md` (finalize optional audit) — **done**
- IDE shims (`CLAUDE.md`, `.cursor/rules/agents.mdc`, `.github/copilot-instructions.md`) — **done**
