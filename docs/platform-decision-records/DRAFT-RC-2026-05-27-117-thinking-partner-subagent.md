# DRAFT ADR: RC-2026-05-27-117 - Thinking-Partner Sub-Agent

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-117
- Source transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
- Speaker: Noah Breyer
- Timestamp: 00:22:00-00:23:00
- Claim type: workflow_proposal

## Context

Speaker spawns a "thinking partner" sub-agent that facilitates exploration, asks questions, and logs uncovered ideas without writing the deliverable. Complements RC-055 identity packs and RC-058 handoffs for draft-stage projects.

## Decision

Document an optional thinking-partner sub-agent prompt pattern for workspace project stages: interview-style questioning, note logging to designated draft files, explicit prohibition on publish-shaped output.

## Intent

- **Intended outcome:** Better problem exploration before PM/Engineer artifact generation.
- **In scope:** Prompt template, subfolder write targets (`research/`, thinking notes), integration with RC-116 mode flag.
- **Out of scope:** Replacing VP/PM/Architect agents; CRM or personal PKM features.

## Safety and non-goals

- **Safety posture:** Sub-agent writes only to `draft` status paths; notes are not citation support until compiled with sources.
- **Non-goals:** Autonomous promotion of thinking notes to wiki or standards.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Mirrors ghostwriter interview pattern; increases human review leverage without bypassing align-cite.

## Impact Scores

Total: 8 (experiment)

## Alternatives Considered

- Single agent with long system prompt (rejected: mode drift)
- External chat tools only (rejected: loses filesystem handoff)

## Consequences

### Positive

- Richer exploration artifacts for next agent in chain

### Negative / Risks

- Extra sub-agent complexity for users

### Safeguards

- Thinking-partner output tagged `type: thinking-notes` in frontmatter

## Validation Plan

A/B one PM stage: with vs without thinking-partner pass; CEO rates clarity of requirements before Engineer handoff.

## Files Proposed for Future Change

- `.github/prompts/workspace-pm-agent.prompt.md` or new thinking-partner prompt stub
- `templates/workspace/thinking-partner.md`
