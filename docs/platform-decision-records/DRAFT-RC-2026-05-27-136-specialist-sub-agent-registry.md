# DRAFT ADR: RC-2026-05-27-136 - Specialist Sub-Agent Registry

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-136
- Source transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
- Speaker: Simon (Better Creating)
- Timestamp: 00:14:00-00:16:00
- Claim type: workflow_proposal

## Context

Notion LifeOS uses global personal agent instructions plus a specialist sub-agent database with mode picker routing. Second Brain has a workspace agent chain (VP→PM→Architect→Engineer) and platform reviewers but no explicit machine-readable registry with input/output contracts.

## Decision

Add a **specialist sub-agent registry** artifact (YAML or Markdown table) mapping agent roles to prompt paths, allowed tools/scopes, and handoff contracts.

## Intent

- **Intended outcome:** Clearer stage routing and platform vs workspace lane separation.
- **In scope:** Registry file, prompt references, mode/routing documentation.
- **Out of scope:** Notion mode picker UI; autonomous agent spawning without CEO gates.

## Safety and non-goals

- **Safety posture:** Each registry entry declares read-only vs mutate scope and approval checkpoints.
- **Non-goals:** Unlimited sub-agent proliferation without contracts.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Experiment RC-136; aligns with RC-069 tool restrictions and existing agent chain.

## Impact Scores

Total: 7 (experiment)

## Alternatives Considered

- Monolithic AGENTS.md only (harder for agents to pick specialist)
- Dynamic Notion DB routing (rejected: RC-131)

## Consequences

### Positive

- Better multi-session handoffs; explicit platform-research-reviewer invocation

### Negative / Risks

- Registry drift if prompts rename without registry update

### Safeguards

- Lint registry entries against existing prompt files; CEO approves new entries

## Validation Plan

Pilot registry on one workspace project; measure restart friction vs chat-only context (H-2026-05-27-015).

## Files Proposed for Future Change

- `config/agent-registry.yml` (new)
- `.github/prompts/workspace-start-project.prompt.md`
