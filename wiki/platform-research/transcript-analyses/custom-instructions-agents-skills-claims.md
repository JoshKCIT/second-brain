# Claims Analysis: Custom Instructions vs Custom Agents vs Agent Skills

## Source

- Transcript: `raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt`
- Slug: `custom-instructions-agents-skills`
- Processing limitations: Microsoft Copilot/GitHub feature tutorial; vendor-specific paths (`.github/copilot-instructions.md`, `.github/agents/`). Grounded against Second Brain's lane-labeled prompt/skill/agent-chain model, not Copilot product truth.

## Executive Judgment

Useful as a **taxonomy reinforcement** transcript: always-on conventions, on-demand specialists with permissions, and pull-in workflow recipes map cleanly to Second Brain's shims, workspace agent chain, and `.github/prompts` + `.github/skills`. Path-scoped instructions are the one net-new experiment candidate for compile-time grounding. No claim to replace Second Brain with Copilot hosting.

## Discussion Blocks

| Block | Timestamp | Topic |
|---|---|---|
| 1 | 00:00:00–00:02:30 | Why customization matters; three instruction layers (repo, path, personal) |
| 2 | 00:02:30–00:05:00 | Custom agents: roles, tool restrictions, isolated context |
| 3 | 00:05:00–00:08:30 | Skills: on-demand recipes, helper scripts, vs instructions/agents |
| 4 | 00:08:30–00:09:00 | Layering all three; recap |

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-066 | `architecture_proposal` | adopt | Three layers: always-on rules (shims/AGENTS), specialist agents (chain), on-demand skills/prompts (workflows). |
| RC-2026-05-27-067 | `workflow_proposal` | experiment | Path-scoped instructions apply only when editing matching wiki/raw/project paths during compile. |
| RC-2026-05-27-068 | `workflow_proposal` | adopt | Multi-step repeatable workflows belong in skills/prompts, not always-loaded global instructions. |
| RC-2026-05-27-069 | `risk_claim` | adopt | Specialist agents should declare tool/scope restrictions (read-only reviewer vs full editor). |

## Grounding Notes

- **RC-050:** `AGENTS.md` agent chain, `.github/prompts/`, `.github/skills/`, `.cursor/rules/agents.mdc` — already_supported.
- **RC-051:** `config/second-brain.yml` project scoping exists; path-specific *instruction files* per directory are not implemented — partially_supported.
- **RC-052:** Operation-specific prompts (`workspace-compile`, `platform-research-review`) vs canonical `AGENTS.md` — already_supported.
- **RC-053:** `platform-transcript-librarian` checkpoints, approval-gated mutations, fail-closed rules — partially_supported; Copilot's explicit tool deny lists are stronger than current prompt text.

## Safer Variants (closure–compile lens)

| Surface pattern | Safer variant for Second Brain |
|---|---|
| Repo-wide Copilot instructions | `AGENTS.md` + agent shims as always-on governance schema |
| Path-specific Copilot instructions | Scoped compile/query hints in `config/second-brain.yml` or per-project orientation, not a second canonical wiki |
| Copilot custom agents | Workspace stage agents + platform reviewers with explicit input/output contracts |
| Copilot skills with bash scripts | `.github/skills/` + `scripts/` with human approval before mutating `wiki/` or `raw/` |

## Recommended Next Actions

- Document the three-layer taxonomy in a future platform ADR (optional; already reflected in architecture).
- Experiment: prototype path-scoped compile hints for `wiki/workspace-projects/{slug}/` only.
- Reject any claim that Copilot repo hosting replaces filesystem-first `raw/` + `wiki/` separation.
