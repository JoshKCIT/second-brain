# Claims Analysis: Why OpenClaw and Hermes Are Distractions

## Source

- Transcript: `raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt`
- Slug: `openclaw-hermes-distractions`
- Processing limitations: Personal productivity / creator workflow; security anecdotes unverified.

## Executive Judgment

Strong **scope-discipline** transcript for Second Brain users: build portable skills (SOPs) and solve one bottleneck before autonomous always-on agents. Reinforces fail-closed and skills-first platform design. Reject OpenClaw/Hermes as Second Brain substrates.

## Discussion Blocks

| Block | Timestamp | Topic |
|---|---|---|
| 1 | 00:00:00–00:02:30 | OpenClaw setup pain, breakage, security of full-computer access |
| 2 | 00:02:30–00:04:30 | Trading agent failure → need explicit skills/limits |
| 3 | 00:04:00–00:06:00 | Skip shiny agents; one bottleneck; skills as SOPs |
| 4 | 00:06:00–00:08:00 | Portable AI system: files + skills; port skills later to automation |

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-075 | `workflow_proposal` | adopt | Master repeatable skills/SOPs before always-on autonomous agent stacks. |
| RC-2026-05-27-076 | `principle_claim` | adopt | Start with one concrete workflow bottleneck, not influencer automation bundles. |
| RC-2026-05-27-077 | `architecture_proposal` | reject | Second Brain should be built on OpenClaw/Hermes always-on personal agents. |
| RC-2026-05-27-078 | `workflow_proposal` | adopt | Portable skills/prompts let the same SOP run across models/tools without retraining the org stack. |

## Grounding Notes

- **RC-033:** Approval-gated verbs, `platform-transcript-librarian` checkpoints, skills in `.github/skills/` — already_supported.
- **RC-034:** Aligns with v1 governance band and deferred digest/automation (RC-011) — already_supported.
- **RC-035:** Second Brain is filesystem Markdown compiler, not VPS babysitter — contradicted.
- **RC-036:** Prompt files + skills + `AGENTS.md` schema — already_supported.

## Safer Variants

| Rejected-as-stated | Safer variant |
|---|---|
| OpenClaw/Hermes as brain runtime | Second Brain `raw/`+`wiki/` with explicit human approval on mutations |
| Full-computer trading/automation agents | Governed workspace/project artifacts with inlined rules at publish |
| "Portable AI system" with 8 factors | Map portable **skills** to `.github/skills/`; keep canonical knowledge in `wiki/` |

## Recommended Next Actions

- Use RC-033/034 in onboarding (`second-brain` prompt) as scope guidance — via future ADR only.
- Record RC-035 in rejected-ideas.
- No OpenClaw integration experiments in v1.
