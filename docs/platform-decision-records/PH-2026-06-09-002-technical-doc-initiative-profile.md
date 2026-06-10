# ADR: PH-2026-06-09-002 - Technical Doc Initiative Profile (Default)

## Status

Accepted (PIC-2026-06-09-027, 2026-06-09)

## Approval

- Approved: 2026-06-09
- Cycle: PIC-2026-06-09-027
- Notes: Full default profile spec in `templates/workspace/chain-profiles/technical-doc-initiative.md`; zero behavior change.

## Source Claim

- Claim ID: PH-2026-06-09-002
- Source transcript: CEO-directed (chain profiles discussion, 2026-06-09)
- Claim type: hygiene

## Context

Depends on PH-2026-06-09-001. Today's behavior must become the explicit default profile so new profiles do not break existing projects.

## Decision

Ship `templates/workspace/chain-profiles/technical-doc-initiative.yml` (or `.md` with embedded YAML) documenting:

| Stage | Prompt | Deliverable | Skip when |
|---|---|---|---|
| vp-brief | `workspace-vp-agent` | `product-brief.md` | never |
| pm-prd | `workspace-pm-agent` | `product-requirements.md` | never |
| architecture | `workspace-architect-agent` | `architectural-approaches.md` | `technical: false` |
| engineering | `workspace-engineer-agent` | engineering specs | never |
| finalize | engineer finalize step | status → `review` | never |

`meta.yml` default: `chain_profile: technical-doc-initiative`.

## Intent

- **Intended outcome:** Zero behavior change for current users; explicit documentation of the default chain.
- **In scope:** Profile file; start-project default; experiment-registry row after accept.
- **Out of scope:** New stages in this cycle.

## Safety and non-goals

- **Non-goals:** Altering PH-001 stage transitions or PH-003 inter-stage contract.

## Approval

- Pending PIC cycle; depends on PH-2026-06-09-001 accepted
