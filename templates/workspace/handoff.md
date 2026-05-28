# Session handoff template (RC-058)

Optional per-stage file: `wiki/workspace-projects/{slug}/0X-{stage}/handoff.md`

Draft-tier project state only — **not** part of the published artifact set. Excluded from finalize, align-cite, and publish. Agents read on session start; update at session end after CEO confirms accuracy.

## File template

```markdown
---
title: "Session Handoff — {stage label}"
type: project-handoff
project: "{slug}"
stage: vp-brief | pm-prd | architecture | engineering
status: draft
draft_tier: true
last_session: {ISO-8601 timestamp}
created: {ISO date}
updated: {ISO date}
---

# Session Handoff — {stage label}

> Draft-tier session state. Not canonical wiki knowledge. Do not cite in published project prose.

## Starting context

Facts the next session needs to resume without chat history: current artifact paths, CEO intent deltas, scoped sources consulted, blockers.

## Next steps

- [ ] {concrete next action}
- [ ] {CEO approval pending if any}

## Open decisions

| Decision | Owner | Status | Notes |
|---|---|---|---|
| {question} | CEO / agent | open | {context} |

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
| CEO gate | Agent asks CEO to confirm handoff accuracy before closing session |
| Finalize | **Exclude** `handoff.md` from wikilink rewrite and `review` status promotion |
| Publish set | Never included in jr-engineer-executable published artifact set |

## See also

- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md`
- Instruction stack tier 3: RC-161
- Stage scaffold (extends RC-058): RC-130
