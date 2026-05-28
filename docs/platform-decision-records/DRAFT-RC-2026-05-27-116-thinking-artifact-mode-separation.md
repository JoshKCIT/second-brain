# DRAFT ADR: RC-2026-05-27-116 - Thinking vs Artifact Mode Separation

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-116
- Source transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
- Speaker: Noah Breyer
- Timestamp: 00:15:30-00:16:30
- Claim type: workflow_proposal

## Context

Speaker uses frontmatter to tell Claude Code not to help write artifacts during exploration—only to think and ask questions. Models default to generative output; Second Brain draft stages need explicit mode separation before publish-bound generation.

## Decision

Add optional project-artifact frontmatter field `agent_mode: thinking | artifact` with prompt contracts that fail closed: `thinking` mode forbids outlines, drafts, and publish-shaped prose; `artifact` mode enables stage output under normal agent rules.

## Intent

- **Intended outcome:** Reduce premature artifact slop during VP/PM/Architect exploration without weakening align-cite at publish.
- **In scope:** Frontmatter schema, workspace agent prompt guards, lint warning when `thinking` files contain publish markers.
- **Out of scope:** Replacing CEO review gates; autonomous wiki mutation.

## Safety and non-goals

- **Safety posture:** Mode flag is draft-tier only; `review`/`published` artifacts ignore thinking mode.
- **Non-goals:** Blocking all generation in thinking mode when user explicitly requests a draft file in a designated subfolder.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Separates exploration from compilation output, improving human review leverage and grounding before citation verification.

## Impact Scores

Total: 10 (experiment)

## Alternatives Considered

- Rely on chat instructions only (rejected: models drift to writing)
- Separate vault for thinking notes (rejected: splits inspectability)

## Consequences

### Positive

- Clearer agent behavior during early project stages

### Negative / Risks

- Users may forget to switch modes

### Safeguards

- Engineer finalize prompts mode check before `review` transition

## Validation Plan

One pilot project uses `agent_mode: thinking` for one week; measure reduction in unpublishable draft fragments in stage bodies.

## Files Proposed for Future Change

- `AGENTS.md` project artifact frontmatter (after user approval)
- `.github/prompts/workspace-vp-agent.prompt.md`
- `.github/prompts/workspace-pm-agent.prompt.md`
- `scripts/lint-platform-research.py` or workspace lint extension
