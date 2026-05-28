# DRAFT ADR: RC-2026-05-27-135 - Agent Hub Compile Artifacts

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-135
- Source transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
- Speaker: Simon (Better Creating)
- Timestamp: 00:13:30-00:15:30
- Claim type: architecture_proposal

## Context

Notion LifeOS exposes an "agent hub" DB combining personal instructions, skills registry, and agent-readable knowledge scopes. Second Brain already has `.github/prompts/`, `.github/skills/`, and `wiki/index.md` but no single generated orientation artifact for agents at session start.

## Decision

Generate a disposable **agent hub compile artifact** (Markdown index) listing: global governance shims, operation prompts, skills, and scoped KB pointers — regenerated from repo sources, not hand-maintained as canonical.

## Intent

- **Intended outcome:** Agents orient faster with explicit always-on vs on-demand guidance separation.
- **In scope:** Generated index under `reports/` or `wiki/platform-research/`; lint for staleness.
- **Out of scope:** Notion DB hub; live mutable agent-private knowledge silos.

## Safety and non-goals

- **Safety posture:** Hub is orientation only; mutations still require approval-gated verbs.
- **Non-goals:** Replacing AGENTS.md; storing transcript claims as agent KB truth.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Maps Notion agent hub pattern to filesystem-first compile artifacts (RC-135, reinforces RC-137/066).

## Impact Scores

Total: 7 (experiment)

## Alternatives Considered

- Rely on ad hoc repo traversal (status quo; higher mis-route risk)
- Embed hub in Notion (rejected: RC-131)

## Consequences

### Positive

- Lower orientation token cost; clearer skill invocation

### Negative / Risks

- Stale index if generation not wired to CI

### Safeguards

- Generate from prompts/skills/index; mark disposable; no wiki writes from hub reads

## Validation Plan

Pilot generated hub; measure orientation file reads on 5 compile tasks vs baseline.

## Files Proposed for Future Change

- `scripts/generate-agent-hub-index.py` (new)
- `.github/prompts/workspace-compile.prompt.md` (reference hub at session start)
