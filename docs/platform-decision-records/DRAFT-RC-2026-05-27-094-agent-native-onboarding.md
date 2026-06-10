# DRAFT ADR: RC-2026-05-27-094 - Agent-Native Onboarding

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-094
- Source transcript: `raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt`
- Speaker: Andrej Karpathy
- Timestamp: 00:25:30-00:26:00
- Claim type: workflow_proposal

## Context

Karpathy argues agent executors—not humans clicking URLs—are the primary consumer of setup and integration instructions. Second Brain already ships `.github/prompts/` and skills; install docs live in `docs/platform-support-documentation/user-guide/getting-started.md`.

## Decision

Pilot agent-native onboarding blocks (copy-paste skills / prompt stubs) as the **primary** setup path, with human-readable verification URLs relegated to See Also.

## Intent

- **Intended outcome:** Faster time-to-first successful `workspace-compile` for agent-led setup.
- **In scope:** `docs/platform-support-documentation/user-guide/getting-started.md`, optional `.github/skills/second-brain-setup/`, shim references in `CLAUDE.md` / `.cursor/rules/agents.mdc`.
- **Out of scope:** Changing publish/align rules; autonomous wiki mutation.

## Safety and non-goals

- **Safety posture:** Skills must reference `AGENTS.md` approval gates; no bypass of ingest/compile approval.
- **Non-goals:** Replacing jr-engineer closure checks; removing human CEO review from project chain.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Experiment score +5; improves inspectability for agent operators without weakening published artifact governance. Aligns with Karpathy "copy-paste to agent" pattern while keeping URLs for human verification only.

## Impact Scores

See claim register RC-2026-05-27-094.

## Alternatives Considered

1. Keep human-first setup docs only — slower agent onboarding.
2. Full agent-only docs with no URLs — worse human auditability.

## Consequences

### Positive

- Reduced setup friction for Cursor/Copilot/Claude Code users.
- Clearer separation: agents execute, humans verify via See Also.

### Negative / Risks

- Skill/prompt drift from canonical `AGENTS.md`.
- Duplicate instructions across shims and skills.

### Safeguards

- Lint that skills link to `AGENTS.md` sections.
- Single canonical setup skill; shims point to it.

## Validation Plan

1. Add agent-native block to getting-started (draft).
2. Run one fresh-clone setup with agent only; record time-to-first compile.
3. User approves or rolls back via implementation backlog.

## Files Proposed for Future Change

- `docs/platform-support-documentation/user-guide/getting-started.md`
- `.github/skills/` (new setup skill, if approved)
- `CLAUDE.md` / `.cursor/rules/agents.mdc` (one-line pointer only, if approved)
