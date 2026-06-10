# ADR: PH-2026-06-09-001 - Chain Profile Schema

## Status

Accepted (PIC-2026-06-09-026, 2026-06-09)

## Approval

- Approved: 2026-06-09
- Cycle: PIC-2026-06-09-026
- Notes: Chain profile schema; meta.yml fields; chain-profiles templates; start-project picker.

## Source Claim

- Claim ID: PH-2026-06-09-001
- Source transcript: CEO-directed (chain profiles discussion, 2026-06-09)
- Speaker: CEO
- Timestamp: n/a
- Claim type: hygiene

## Context

Second Brain ships one implicit agent chain (VP → PM → Architect? → Engineer → finalize) for all projects. CEOs need different workflows for technical initiatives, meeting synthesis, and knowledge-hub builds. PH-001–007 and RC-130 established stage state and scaffolds; this ADR adds a **declared chain profile** without removing CEO gates or approval-gated mutations.

## Decision

Add `chain_profile` to `wiki/workspace-projects/{slug}/meta.yml` and a `templates/workspace/chain-profiles/` directory. Each profile defines:

- `profile_id` (stable slug)
- `stages[]` with `id`, `prompt` path, optional `skip_when`, and deliverable filename
- `closure_rule` (default: jr-engineer-executable published set; profiles may declare advisory-only endings)
- `ceo_gate_policy` (default: gate after every stage)

`workspace-start-project` asks the CEO to pick a profile (default: `technical-doc-initiative` after PH-2026-06-09-002). Orchestrator reads `chain_profile` + `stages` instead of hard-coded stage list.

## Intent

- **Intended outcome:** Project-type-specific agent chains with explicit contracts; preserved CEO review between stages.
- **In scope:** `meta.yml` schema; chain-profiles README + one stub profile file; start-project profile picker; routing-map row.
- **Out of scope:** New always-on personas; email/Teams responders; autonomous background mutation.

## Safety and non-goals

- **Safety posture:** Profiles cannot disable align-cite, align-closure, or ingest/compile/publish approval gates.
- **Non-goals:** Agent zoo without I/O contracts; platform-lane work in workspace profiles (use `platform-*` verbs).

## Rationale

RC-136 (sub-agent registry) was parked for sprawl risk; profiles with stage contracts address that risk. RC-167 subprojects remain for parallel workstreams inside a profile.

## Alternatives Considered

| Alternative | Why not |
|---|---|
| One mega-prompt with mode switch | Bloats default load; RC-165 pointer pattern violated |
| Per-persona always-on shims | Rejected personal-OS patterns (RC-128, RC-168) |
| Hard-code three project types in AGENTS.md | PH-007 registry pattern prefers templates |

## Consequences

- **Positive:** Clear extension point for Technical Writer, Architect Reviewer, QA stages (PH-003–005).
- **Negative:** Orchestrator and `meta.yml` transition table grow; existing projects need default profile backfill on resume.

## Implementation Notes

- Template: `templates/workspace/chain-profiles/README.md`
- Update: `templates/workspace/project-meta.yml.md`, `.github/prompts/workspace-start-project.prompt.md`
- Tests: extend meta.yml validation if present; manual resume smoke on one project

## Approval

- Pending PIC cycle
