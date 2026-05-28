# Session handoff template (RC-058, PH-003, PH-004, PH-005)

Optional per-stage file: `wiki/workspace-projects/{slug}/0X-{stage}/handoff.md`

Draft-tier project state only — **not** part of the published artifact set. Excluded from finalize, align-cite, and publish. Agents read on session start; update at session end after CEO confirms accuracy.

Inter-stage forwarding (PH-003): orchestrator populates **Locked decisions** and **Forwarded open decisions** at CEO gates; downstream agents honor locks before drafting.

## File template

```markdown
---
title: "Session Handoff — {stage label}"
type: project-handoff
project: "{slug}"
stage: vp-brief | pm-prd | architecture | engineering
status: draft
draft_tier: true
forwarded_from: null | vp-brief | pm-prd | architecture
upstream_artifact: null | wiki/workspace-projects/{slug}/0X-{stage}/{artifact}.md
last_session: {ISO-8601 timestamp}
created: {ISO date}
updated: {ISO date}
---

# Session Handoff — {stage label}

> Draft-tier session state. Not canonical wiki knowledge. Do not cite in published project prose.

## Starting context

Facts the next session needs to resume without chat history: current artifact paths, CEO intent deltas, scoped sources consulted, blockers.

## Reopen context (PH-005)

Present only when orchestrator reopened to this stage. Clear after target stage is CEO-approved again.

| Field | Value |
|---|---|
| Reopened at | {ISO timestamp} |
| Invalidated stages | {from meta.yml} |
| CEO reason | {reopen_reason} |
| Locks to reconfirm | {L- IDs from invalidated stages, or none} |

## Locked decisions (do not reopen)

| ID | Decision | Locked at stage | Source | Notes |
|---|---|---|---|---|
| L-001 | {text} | vp-brief | product-brief.md §Success criteria | CEO confirmed at VP gate |

CEO-approved facts and constraints. Downstream agents must not contradict without explicit CEO override documented here. After PH-005 reopen, locks from invalidated stages move to **Locks to reconfirm** until the CEO re-approves.

## Forwarded open decisions (from upstream)

| ID | Decision | Owner | From stage | Source | Notes |
|---|---|---|---|---|---|
| F-001 | {text} | CEO | vp-brief | product-brief.md §Open questions | Address in PRD or escalate |

Unresolved upstream items. Address in this stage's artifact, move to **Open decisions (this stage)**, or mark `[NEEDS INPUT]`.

## Open decisions (this stage)

| ID | Decision | Owner | Status | Notes |
|---|---|---|---|---|
| | {question} | CEO / agent | open | {context} |

Local to this stage session. Orchestrator may promote rows to locked or forward at the next CEO gate.

## Advisory cite check (PH-004)

Optional pre-gate citation integrity run. Orchestrator skips duplicate offer if current.

| Field | Value |
|---|---|
| Last run | {ISO timestamp \| skipped \| not run} |
| Artifact | {path or —} |
| Result | pass (advisory) \| fail (advisory) \| skipped \| not run |
| Report | {reports/workspace-advisory-align-cite-* path or —} |
| Violations | {count or —} |

## Next steps

- [ ] {concrete next action}
- [ ] {CEO approval pending if any}

## Last session

- **When:** {ISO timestamp}
- **Stage agent:** vp | pm | architect | engineer | orchestrator
- **Completed this session:** {bullets}
- **Left incomplete:** {bullets}
- **Sources consulted:** {wiki/raw paths, max 10}
```

## Usage rules

| Rule | Detail |
|---|---|
| Location | One `handoff.md` per active stage directory |
| Write trigger | End of agent session or before waiting on CEO |
| Read trigger | Start of resumed session (`start-project` resumability or stage agent invoke) |
| PH-003 forward | Orchestrator writes locked/forwarded sections at CEO gate before next agent |
| CEO gate | Agent asks CEO to confirm handoff accuracy before closing session |
| Finalize | **Exclude** `handoff.md` from wikilink rewrite and `review` status promotion |
| Publish set | Never included in jr-engineer-executable published artifact set |

## See also

- Inter-stage contract: `templates/workspace/inter-stage-contract.md` (PH-003)
- Reopen protocol: `templates/workspace/reopen-stage-protocol.md` (PH-005)
- Session audit: `.github/skills/session-audit/SKILL.md` (RC-164)
- Advisory cite: `templates/workspace/advisory-align-cite-per-stage.md` (PH-004)
- Orientation: `templates/workspace/orientation.md` (RC-163)
- ADR: `docs/platform-decision-records/RC-2026-05-27-058-project-session-handoff.md`
- PH-003 ADR: `docs/platform-decision-records/PH-2026-05-27-003-inter-stage-output-contract.md`
- Instruction stack tier 3: RC-161
- Stage scaffold (extends RC-058): `templates/workspace/project-stage-scaffold/README.md` (RC-130)
