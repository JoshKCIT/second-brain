# Thinking-partner notes template (RC-117)

Optional per-stage folder: `wiki/workspace-projects/{slug}/0X-{stage}/thinking-notes/`

Use with `.github/prompts/workspace-thinking-partner.prompt.md`. One file per thinking session or topic.

## File template

```markdown
---
title: "Thinking — {topic}"
type: thinking-notes
project: "{slug}"
stage: vp-brief | pm-prd | architecture | engineering
status: draft
draft_tier: true
publish_scope: exclude
not_canonical: true
agent_mode: thinking
topic: "{short topic label}"
sources:
  - "wiki/workspace-projects/{slug}/0X-{stage}/handoff.md"
created: {ISO date}
updated: {ISO date}
---

# Thinking — {topic}

> Draft-tier exploration log. **Not canonical.** Stage agents must verify facts and add proper sources before placing content in the stage artifact. Excluded from finalize and publish.

## Context

{Why this thinking session started — 1–2 sentences}

## Questions explored

### Q1: {question}

- CEO answer / working assumption: {text}
- Follow-up: {optional}

### Q2: {question}

- ...

## Ideas and hypotheses

- {idea} `[unverified]` when not sourced

## Themes

- {pattern or tension surfaced}

## Open questions for CEO

- {question for stage agent or next session}

## Suggested locks (CEO gate only)

| ID | Decision | Rationale |
|---|---|---|
| T-{n} | {proposed lock} | {why} |

## Handoff to artifact mode

When exploration is sufficient, set stage `agent_mode: artifact` and invoke the stage agent. Cite thinking-notes paths in stage agent session context only — not in published prose.
```

## Rules

| Rule | Detail |
|---|---|
| Location | `thinking-notes/{YYYY-MM-DD}-{topic-slug}.md` under active stage |
| Canonical? | No — `not_canonical: true`, `publish_scope: exclude` |
| Citation support? | No — facts must be re-verified with sources in artifact mode |
| Finalize / publish | Excluded — same tier as `research/` and `orientation.md` |
| Promotion | Requires compile path + user approval + align-cite if ever wiki-bound |

## Distinction from other draft files

| File | Purpose |
|---|---|
| `orientation.md` (RC-163) | Disposable session preferences and scratch context |
| `research/` (RC-130) | Reading notes with source paths |
| `thinking-notes/` (RC-117) | Interview-style exploration log from thinking-partner |
| Stage artifact | Publish-bound deliverable when `agent_mode: artifact` |

## See also

- Prompt: `.github/prompts/workspace-thinking-partner.prompt.md`
- Agent mode: `templates/workspace/agent-mode.md` (RC-116)
- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-117-thinking-partner-subagent.md`
