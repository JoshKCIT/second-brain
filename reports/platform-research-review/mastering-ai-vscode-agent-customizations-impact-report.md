# Research Impact Report: Mastering AI with VS Code's New Agent Customizations

## Executive Judgment

This transcript is **mostly roadmap noise for Second Brain** (IDE product tour) with **two experiment-worthy governance hooks**: convention-discovery bootstrap and lifecycle hooks for approval-gated side effects. Treating VS Code's codebase specialist agents as platform direction is rejected as generic IDE scope.

## Source

- Transcript: `raw/platform-transcripts/Mastering_AI_with_VS_Code_s_New_Agent_Customizations.txt`
- Date: unknown
- Participants: unknown (VS Code / GitHub changelog demo presenter)
- Processing limitations: vendor feature demo; no independent validation of marketplace or hook behavior.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 0 |
| Experiment | 2 |
| Defer | 0 |
| Reject | 1 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-033 | experiment | `/init`-style discovery could keep AGENTS.md shims and prompts aligned with repo conventions—compile-time maintainability. |
| RC-2026-05-27-034 | experiment | Hooks model maps to approval-gated mutations (commit/publish checkpoints). |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-035 | reject | C# Azure Functions specialist agent is codebase-assistant scope—RC-009a territory. |
| RC-2026-05-27-032 | monitor | Chasing IDE UI parity could distract from governance-and-closure band. |

## Claim Register Entries

- `RC-2026-05-27-032` through `RC-2026-05-27-035` — see `wiki/platform-research/claim-register.md`

## Recommended Next Actions

### Immediate changes

- None to canonical docs in this pass.

### Experiments

- RC-033: Run `/init` equivalent on Second Brain; propose prompt/shim diff via draft ADR only.
- RC-034: Spec optional publish/commit hook pattern in platform docs (experiment).

### ADRs to draft

- Optional: `DRAFT-RC-2026-05-27-033-convention-discovery-bootstrap.md` if user approves experiment.

### Claims to reject

- RC-2026-05-27-035 — mirrored in `rejected-ideas.md`.

### Claims requiring external validation

- RC-032: VS Code chat customizations GA behavior and MCP marketplace registry.

## Trust Loop Summary

RC-034 experiment must fail closed: hooks surface actions, never auto-mutate canonical wiki or protected files. RC-033 outputs are advisory draft diffs only.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-033, RC-034 | experiment | Approve experiment ADR; reject via backlog rollback. |
| RC-035 | reject | Reopen only with approved code-as-source v2 ADR. |
| RC-032 | monitor | Re-score when Cursor/VS Code docs cached. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
