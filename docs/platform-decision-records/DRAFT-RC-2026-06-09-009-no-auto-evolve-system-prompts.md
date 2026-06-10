# DRAFT ADR: RC-2026-06-09-009 - No Auto-Evolve System Prompts

## Status

Draft

## Source Claim

- Claim ID: RC-2026-06-09-009
- Source transcript: `raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt`
- Speaker: unknown
- Timestamp: 00:06:30-00:07:30
- Claim type: risk_claim

## Context

A-H-E ablation found that evolving tools, middleware, and memory improved benchmark performance, but evolving the system prompt alone caused regression. Second Brain's Tier-1 rules live in prose instruction files (`AGENTS.md`, tier-2 shims, stage prompts). Autonomous prompt mutation would bypass CEO approval and destabilize governance invariants.

## Decision

Forbid autonomous evolution of system prompts and prose instruction files. Platform improvements to prompts, shims, and stage contracts route only through explicit user-approved PIC cycles and draft ADRs.

## Intent

- **Intended outcome:** Preserve instruction-stack integrity while allowing code-based tooling improvements.
- **In scope:** Policy statement; lint/advisory checks; PIC routing for any prompt edits.
- **Out of scope:** Autonomous prompt rewriting; self-evolving agent instructions.

## Safety and non-goals

- **Safety posture:** Fail closed—agents may propose prompt changes in reports/DRAFT ADRs only.
- **Non-goals:** Full A-H-E autonomous evolution loop; unattended harness commits.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Transcript ablation aligns with existing RC-012 advisory-only posture and RC-161 instruction stacking. Code-based tools (`scripts/`, skills) can evolve with tests; prose strategy in system prompts does not transfer reliably across tasks.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | +2 | Protects Tier-1 invariants |
| Closure | +1 | Stable rules improve publish consistency |
| Grounding | +1 | Prevents uncited prompt drift |
| Vendor truth | 0 | Neutral |
| Inspectability | +1 | Changes remain diff-reviewable |
| Maintainability | +2 | Avoids prompt entropy |
| Differentiation | +1 | Governance band vs generic agents |
| Enterprise fit | +2 | Audit-friendly |
| Human review leverage | +2 | CEO retains prompt authority |

## Alternatives Considered

1. Allow agents to auto-edit shims when lint fails.
2. Quarterly human-only prompt review without automation proposals.
3. Explicit ban on autonomous prompt mutation; advisory proposals only.

## Consequences

### Positive

- Prevents regression from self-modifying instructions.
- Clarifies safe evolution surface (scripts, skills, reports).

### Negative / Risks

- Slower harness iteration if all prompt edits require CEO review.

### Safeguards

- RC-012 advisory failure reports may propose prompt edits.
- PIC accept/rollback for approved changes only.

## Validation Plan

After adoption, verify zero autonomous writes to `AGENTS.md`, `.cursor/rules/agents.mdc`, `CLAUDE.md`, and `.github/prompts/*.prompt.md` outside PIC cycles over three platform sessions.

## Files Proposed for Future Change

```text
AGENTS.md
templates/platform-research/
.github/prompts/platform-implement-backlog.prompt.md
scripts/lint-platform-research.py
```
