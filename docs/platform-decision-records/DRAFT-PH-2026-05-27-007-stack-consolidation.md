# DRAFT ADR: PH-2026-05-27-007 - Stack Consolidation (Experiment Registry + Draft-Tier Map)

## Status

Draft

## Source

- Hygiene item: PH-2026-05-27-007
- Trigger: Post-PIC-023 stack audit (2026-05-28 CEO review)
- Depends on: RC-161 (instruction stacking), RC-165 (pointer resources), PH-001–006 (agent chain hygiene complete)
- Not a transcript-derived claim

## Context

PIC-001 through PIC-023 accepted **23 platform changes** spanning foundation policy, session ergonomics, compile lane, and experiments. Each cycle added:

1. **Inline bullets** to `AGENTS.md` § Agent chain (15+ feature paragraphs since RC-058)
2. **Optional draft-tier paths** under project stages (`handoff`, `orientation`, `thinking-notes`, `research`, `chats`, `daily-progress`, `subprojects`)
3. **Active hypotheses** in `wiki/platform-research/open-hypotheses.md` with limited pilot validation

RC-165 trimmed Tier-2 shims (~100 lines) but **did not consolidate Tier-1 experiment prose**. `AGENTS.md` is ~719 lines; the agent chain section alone repeats template paths, ADR links, and exclusion rules that belong in pointer files.

CEO and agents face two clarity gaps:

- **“Which experiment applies?”** — requires scanning long AGENTS prose
- **“Where do I write this note?”** — eight draft-tier targets with overlapping purposes

PH-001–006 fixed structural agent-chain gaps. PH-007 addresses **documentation stack debt** without rolling back accepted experiments.

## Decision

Introduce two consolidation artifacts and refactor `AGENTS.md` to **pointer-first** experiment documentation:

| Artifact | Path | Role |
|---|---|---|
| **Experiment registry** | `templates/workspace/experiment-registry.md` | Single table: accepted RC/PH experiments → template, ADR, hypothesis, pilot status |
| **Draft-tier map** | `templates/workspace/draft-tier-map.md` | CEO/agent cheat sheet: which file to write for which intent |

**AGENTS.md § Agent chain** retains:

- Agent chain diagram and stage flow
- **Structural invariants** (RC-122 read-before-write, RC-058 handoff, PH-001–006 contracts)
- One pointer line: *“Accepted experiments: `templates/workspace/experiment-registry.md`; draft-tier write targets: `templates/workspace/draft-tier-map.md`”*

**AGENTS.md removes** per-experiment inline paragraphs for accepted experiments (RC-130, RC-163, RC-116, RC-167, RC-164, RC-117, RC-162, RC-146, RC-148, RC-165). Those rows move to the registry; behavior unchanged.

## Intent

- **Intended outcome:** Lower Tier-1 context load; faster CEO/agent orientation; unchanged governance behavior.
- **In scope:** Registry + draft-tier map templates; AGENTS refactor; `start-project` and routing-map cross-links; optional lint advisory for AGENTS experiment-bullet drift.
- **Out of scope:** Rolling back accepted experiments; merging draft-tier paths into one file; auto-generating registry from claim register (manual curation v1).

## Safety and non-goals

- **Safety posture:** Structural PH-001–006 and Tier-1 invariants stay in default AGENTS load. Registry is reference material loaded on task match (RC-165). No experiment behavior changes without a separate ADR.
- **Non-goals:** Hiding approval gates, align-cite, or closure rules in optional pointers; deleting ADRs; promoting experiments to canonical wiki without pilot + accept.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

- **RC-161:** Tier 1 holds invariants; Tier 2/3 and pointer files hold deltas. Experiment prose is Tier-2/reference scope.
- **RC-165:** Extends pointer-resources pattern to platform experiment catalog.
- **Product brief §1.2:** Consolidation improves inspectability without adding generic-band features.

Stack audit finding: validation debt (10+ active hypotheses, no pilot owner) is a process problem; PH-007 makes the stack **legible** so pilots can proceed deliberately.

## Alternatives Considered

| Alternative | Verdict |
|---|---|
| Leave inline AGENTS bullets | Rejected: unbounded Tier-1 growth per PIC cycle |
| Auto-sync registry from claim-register | Deferred: v1 manual curation; script later if drift recurs |
| Merge all draft-tier into `handoff.md` only | Rejected: loses RC-163/117 separation; lint exclusions break |
| Full experiment rollback | Rejected: foundation and compile lane are validated directionally |

## Consequences

### Positive

- Shorter default AGENTS load for every session
- Single CEO “where to write” reference
- New PIC cycles add registry rows instead of AGENTS paragraphs
- Easier stack audits (registry row count vs AGENTS line count)

### Negative / Risks

- Agents skip registry read unless routing map or prompt enforces it
- Registry drift if PIC accept forgets to update the table
- Mitigation: lint advisory; `start-project` CEO checkpoint lists draft-tier map

### Safeguards

- PH-001–006 bullets remain inline in AGENTS (structural, not experimental)
- Registry columns include `hypothesis_id` and `pilot_status` for validation tracking
- Implementation blocked until explicit CEO approval of this ADR

## Validation Plan

1. **Line audit:** AGENTS § Agent chain ≤ 25 lines post-refactor (excluding diagram); total AGENTS reduction ≥ 40 lines.
2. **CEO quiz:** Given five intents (“session preference”, “exploration question”, “reading note”, “lock for next stage”, “publish requirement”), CEO maps to correct path using draft-tier map in ≤ 2 minutes.
3. **Agent holdout:** Five compile/resume tasks; agent cites registry or draft-tier map when choosing write target (log in pilot project `orientation.md`).
4. **No regression:** `python -m unittest discover -s tests`; `lint-workspace.py`; `lint-platform-research.py` pass after implementation.

## Proposed registry shape

```markdown
| ID | Status | Template | ADR | Hypothesis | Pilot |
|---|---|---|---|---|---|
| RC-163 | accepted | templates/workspace/orientation.md | DRAFT-RC-...-163-... | H-026 | active |
| RC-116 | accepted | templates/workspace/agent-mode.md | DRAFT-RC-...-116-... | H-021 | active |
...
```

Columns: `id`, `decision`, `template_or_prompt`, `adr_path`, `hypothesis_id`, `pilot_status` (`active` | `validated` | `demote_candidate`).

## Proposed draft-tier map shape

| Intent | Write to | Canonical? | Promoted how |
|---|---|---|---|
| Resume / locks / forwarded decisions | `{stage}/handoff.md` | No | PH-003 forward at gate |
| Session preferences / scratch | `{stage}/orientation.md` | No | Never without compile + approval |
| Interview exploration | `{stage}/thinking-notes/` | No | Verify in artifact + sources |
| Reading notes with sources | `{stage}/research/` | No | Merge into stage artifact |
| Publish-bound deliverable | `{stage}/{artifact}.md` | Yes (when published) | align-cite + align-closure |

Include exclusion reminder: all rows except stage artifact excluded from finalize/publish set.

## Implementation (future PIC cycle)

| Artifact | Change |
|---|---|
| `templates/workspace/experiment-registry.md` | **New** — curated table through PIC-023 |
| `templates/workspace/draft-tier-map.md` | **New** — CEO/agent cheat sheet |
| `AGENTS.md` | Replace experiment inline bullets with registry + draft-tier pointers; keep PH-001–006 + RC-122 + RC-058 inline |
| `templates/workspace/pointer-resources/README.md` | Add registry + draft-tier map to catalog |
| `templates/workspace/routing-map.md` | Row: stack orientation → registry + draft-tier map |
| `.github/prompts/workspace-start-project.prompt.md` | CEO onboarding: link draft-tier map at project create |
| `wiki/platform-research/implementation-backlog.md` | PH-007 hygiene row → accepted on PIC accept |
| `scripts/lint-workspace.py` (optional) | Advisory: AGENTS agent-chain section > N lines or duplicate experiment ADR paths |

**Rollback:** Restore inline AGENTS bullets from git; delete two templates; no wiki mutation.

## Priority

| Field | Value |
|---|---|
| Suggested priority_score | 14 (hygiene; unblocks pilot clarity) |
| Stack tier | 3c — Documentation hygiene (after PH-001–006, alongside pilot validation) |
| Bundling | Standalone; do not bundle with RC-050/055 |

## See also

- Stack audit: CEO review 2026-05-28 (conversation)
- RC-165 ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-165-lean-root-pointer-resources.md`
- Agent chain hygiene: `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`
- Implementation backlog: `wiki/platform-research/implementation-backlog.md`
- Open hypotheses: `wiki/platform-research/open-hypotheses.md`
