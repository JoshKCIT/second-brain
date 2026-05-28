# DRAFT ADR: RC-2026-05-27-161 - Hierarchical Instruction Stacking

## Status

Implemented (PIC-2026-05-27-009, pending user review)

## Source Claim

- Claim ID: RC-2026-05-27-161
- Source transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
- Speaker: Jeff
- Timestamp: 00:03:30-00:05:00
- Claim type: architecture_proposal

## Context

Jeff maps Cowork workspaces to constitution/state-law stacking: root CLAUDE.md applies everywhere; workstation CLAUDE.md adds scoped rules. Second Brain already has AGENTS.md, agent prompt shims, and stage-gated project directories but lacks an explicit stacking contract.

## Decision

Document and enforce a three-tier instruction stack: (1) root AGENTS.md invariants, (2) lane/stage prompt shims (workspace-* vs platform-*), (3) optional project-stage or sub-scaffold shims that add scope without restating root governance rules.

## Intent

- **Intended outcome:** Agents load only applicable rules per task; root policy always applies.
- **In scope:** ADR documentation, prompt header contracts, lint guidance for duplicate root rules in shims.
- **Out of scope:** Consumer life workstations (Email HQ, personal finance); Cowork folder layout.

## Safety and non-goals

- **Safety posture:** Root invariants (approval gates, align-cite, closure) cannot be overridden by nested shims.
- **Non-goals:** Personal OS product direction; unbounded nested workstations.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Cowork analogy validates existing agent chain; explicit stacking reduces drift when adding stage or project prompts.

## Impact Scores

Total: 10 (adopt)

## Alternatives Considered

- Single monolithic AGENTS.md — rejected (token load, maintainability).
- Cowork life-OS folders — rejected (RC-168).

## Consequences

### Positive

- Clearer handoffs between CEO → VP → PM → Engineer agents.
- Safer project sub-scaffolds without governance regression.

### Negative / Risks

- Operators create deep nests without routing maps (mitigate RC-162).

### Safeguards

- Shim files must declare `inherits: AGENTS.md` and list non-overridable root rules.

## Validation Plan

Verify one multi-stage project session loads root + single stage shim; nested shim does not duplicate align-cite rules.

## Files Proposed for Future Change

- `AGENTS.md` (stacking section) — **done**
- `.github/prompts/*.prompt.md` (inheritance header) — **done** (24 prompts)
- `templates/workspace/instruction-stack-header.md` (new) — **done**
- `.cursor/rules/agents.mdc`, `CLAUDE.md`, `.github/copilot-instructions.md` (Tier-2 shim notes) — **done**
- `docs/setup-kit.md` (onboarding note) — **done**
- `.github/prompts/workspace-lint.prompt.md` (shim duplication check 16) — **done**
