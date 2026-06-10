# Experiment registry (PH-007)

Curated catalog of **accepted platform experiments** through PIC-023. Structural agent-chain invariants (RC-058, RC-122, PH-001–006) remain inline in `AGENTS.md`. Load this file on task match when applying an experiment feature.

**Maintenance:** On each PIC accept, add or update one row. Do not add experiment prose back to `AGENTS.md` § Agent chain.

| ID | Decision | Template / prompt | ADR | Hypothesis | Pilot status |
|---|---|---|---|---|---|
| RC-058 | accepted | `templates/workspace/handoff.md` | `docs/platform-decision-records/RC-2026-05-27-058-project-session-handoff.md` | H-2026-05-27-009 | active |
| RC-130 | accepted | `templates/workspace/project-stage-scaffold/README.md` | `docs/platform-decision-records/RC-2026-05-27-130-project-stage-scaffold.md` | H-2026-05-27-023 | active |
| RC-163 | accepted | `templates/workspace/orientation.md` | `docs/platform-decision-records/RC-2026-05-27-163-disposable-session-orientation.md` | H-2026-05-27-026 | active |
| RC-116 | accepted | `templates/workspace/agent-mode.md` | `docs/platform-decision-records/RC-2026-05-27-116-thinking-artifact-mode-separation.md` | H-2026-05-27-021 | active |
| RC-167 | accepted | `templates/workspace/project-sub-scaffold/README.md` | `docs/platform-decision-records/RC-2026-05-27-167-project-subfolder-rule-stacking.md` | H-2026-05-27-029 | active |
| RC-164 | accepted | `.github/skills/session-audit/SKILL.md` | `docs/platform-decision-records/RC-2026-05-27-164-session-audit-skill.md` | H-2026-05-27-027 | active |
| RC-117 | accepted | `templates/workspace/thinking-partner.md` | `docs/platform-decision-records/RC-2026-05-27-117-thinking-partner-subagent.md` | H-2026-05-27-022 | active |
| RC-162 | accepted | `templates/workspace/routing-map.md` | `docs/platform-decision-records/RC-2026-05-27-162-routing-map-agents-shim.md` | H-2026-05-27-025 | active |
| RC-165 | accepted | `templates/workspace/pointer-resources/README.md` | `docs/platform-decision-records/RC-2026-05-27-165-lean-root-pointer-resources.md` | H-2026-05-27-028 | active |
| RC-146 | accepted | `templates/workspace/raw-inbox-staging.md` | `docs/platform-decision-records/RC-2026-05-27-146-raw-inbox-staging.md` | H-2026-05-27-025 (146) | active |
| RC-148 | accepted | `templates/workspace/topic-entity-compile.md` | `docs/platform-decision-records/RC-2026-05-27-148-topic-entity-compile.md` | H-2026-05-27-026 (148) | active |
| PH-2026-06-09-003 | experiment | `templates/workspace/technical-writer-stage.md` | `docs/platform-decision-records/PH-2026-06-09-003-technical-writer-stage.md` | H-2026-06-09-005 | active |
| PH-2026-06-09-004 | experiment | `templates/workspace/architect-reviewer-stage.md` | `docs/platform-decision-records/PH-2026-06-09-004-architect-reviewer-stage.md` | H-2026-06-09-005 | active |

## Pilot status values

| Value | Meaning |
|---|---|
| `active` | Accepted; pilot validation in progress or not started |
| `validated` | Pilot passed; candidate to fold into Tier-1 invariants |
| `demote_candidate` | Pilot failed or low leverage; candidate to park or rollback |

Track hypotheses in `wiki/platform-research/open-hypotheses.md`.

## Structural hygiene (inline in AGENTS, not experiments)

| ID | Role |
|---|---|
| PH-001 | `meta.yml` stage state machine |
| PH-002 | start-project finalize alignment |
| PH-003 | Inter-stage locked / forwarded decisions |
| PH-004 | Advisory align-cite per stage |
| PH-005 | Reopen stage protocol |
| PH-006 | Platform escalation routing row |
| PH-2026-06-09-001 | Chain profile schema (`chain_profile` in meta.yml; `templates/workspace/chain-profiles/`) |
| PH-2026-06-09-002 | Default profile `technical-doc-initiative` — `templates/workspace/chain-profiles/technical-doc-initiative.md` |
| RC-122 + RC-157 | Read-before-write; citation-grounded query |
| RC-018 | Retrieval contract first |
| RC-161 | Instruction stacking tiers |

## See also

- Draft-tier write targets: `templates/workspace/draft-tier-map.md`
- Open hypotheses: `wiki/platform-research/open-hypotheses.md`
- ADR: `docs/platform-decision-records/PH-2026-05-27-007-stack-consolidation.md`
