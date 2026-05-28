# Inter-stage output contract (PH-003)

Formalizes what passes between workspace agent stages so downstream agents do not re-ask the CEO for settled facts. Complements RC-058 session handoff and PH-001 `meta.yml` stage state.

## Decision types

| Type | Meaning | Downstream rule |
|---|---|---|
| **Locked** | CEO confirmed at a stage gate; recorded with source | Do not reopen or contradict without explicit CEO override |
| **Forwarded open** | Unresolved at upstream stage; carried forward | Must address in artifact, escalate in `Open Questions`, or mark `[NEEDS INPUT]` |
| **Open (this stage)** | New or still-local to current stage | Normal RC-058 `open_decisions` table |

## Stage transitions

| CEO approves | Orchestrator forwards into | Upstream artifact | Upstream handoff |
|---|---|---|---|
| VP brief | `02-pm-prd/handoff.md` | `01-vp-brief/product-brief.md` | `01-vp-brief/handoff.md` |
| PRD (technical) | `03-architecture/handoff.md` | `02-pm-prd/product-requirements.md` | `02-pm-prd/handoff.md` |
| PRD (non-technical) | `04-engineering/handoff.md` | `02-pm-prd/product-requirements.md` | `02-pm-prd/handoff.md` |
| Architecture | `04-engineering/handoff.md` | `03-architecture/architectural-approaches.md` (+ ADRs) | `03-architecture/handoff.md` |

Engineering → finalize does not forward a new stage handoff; locked decisions remain in `04-engineering/handoff.md` for finalize and align.

## Extraction map (orchestrator at CEO gate)

Read the approved upstream artifact and upstream `handoff.md`. Merge into the next stage `handoff.md` per `templates/workspace/handoff.md`.

| Upstream stage | Lock candidates (CEO confirmed at gate) | Forward open |
|---|---|---|
| `vp-brief` | `## Success criteria`, `## High-level constraints`, `## Out of scope (explicit)` | `## Open questions for PM Agent`, unresolved rows from upstream `open_decisions` |
| `pm-prd` | Requirements/NFRs CEO affirmed; resolved risks; chosen scope boundaries | PRD open questions / risks needing architecture or engineering |
| `architecture` | Recommended approach, accepted tradeoffs, ADR decisions | Unresolved technical questions, deferred ADRs |

When the CEO says "Approved, proceed" without listing locks explicitly, treat all upstream **Locked decisions** plus artifact sections the CEO edited during review as locked. Remaining upstream open rows become **Forwarded open**.

## Orchestrator checklist (start-project)

At each CEO gate after approval, before invoking the next agent:

1. Read upstream `handoff.md` (`locked_decisions`, `forwarded_open_decisions`, `open_decisions`).
2. Read approved upstream stage artifact decision-bearing sections (table above).
3. Create or update next-stage `handoff.md`:
   - Set frontmatter `forwarded_from`, `upstream_artifact`, `updated`.
   - Copy cumulative **Locked decisions** (append new IDs; never drop without CEO override).
   - Copy unresolved items into **Forwarded open decisions**.
   - Initialize **Open decisions (this stage)** empty or with net-new CEO deltas from the gate conversation.
4. Append to `wiki/log.md`:
   ```
   ## [{ISO timestamp}] stage-forward | {slug} | {upstream} → {downstream}
   - Locked added: {count}
   - Forwarded open: {count}
   ```
5. Pass next-stage `handoff.md` path when invoking the downstream agent.

## Stage agent obligations

**On invoke (downstream stages):**

1. Read `handoff.md` **Locked decisions** and **Forwarded open decisions** before drafting.
2. Honor every locked row; cite `L-{nnn}` in artifact prose where the decision binds content.
3. Address each forwarded open row in the artifact body or in stage-appropriate open-questions section.

**On session end:**

1. Propose new locks only in `handoff.md` with `status: proposed` until CEO gate.
2. Do not remove locked rows; mark superseded only with CEO explicit override noted in `Notes`.

**PH-005 reopen:** When orchestrator reopens to an earlier stage, locks from `invalidated_stages` move to target `handoff.md` **Locks to reconfirm** until CEO re-approves. Do not forward invalidated-stage artifacts into PH-003 handoffs.

**VP (first stage):** No upstream forward. Populate `open_decisions` and artifact `## Open questions for PM Agent` so the VP→PM gate has forwardable content.

## ID conventions

| Prefix | Example | Use |
|---|---|---|
| `L-` | `L-001` | Locked decision (cumulative across chain) |
| `F-` | `F-003` | Forwarded open (may become `L-` at next gate) |

## See also

- Handoff template: `templates/workspace/handoff.md`
- PH-001 resumability: `templates/workspace/project-meta.yml.md`
- ADR: `docs/platform-decision-records/DRAFT-PH-2026-05-27-003-inter-stage-output-contract.md`
- Reopen protocol: `templates/workspace/reopen-stage-protocol.md` (PH-005)
- Advisory cite: `templates/workspace/advisory-align-cite-per-stage.md` (PH-004)
- Hygiene review: `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`
