# Session orientation template (RC-163)

Optional per-stage file: `wiki/workspace-projects/{slug}/0X-{stage}/orientation.md`

**Distinct from `handoff.md` (RC-058):** orientation holds disposable session context—active notes, preferences, and "remember this" items. Handoff holds structured restart state, PH-003 locks/forwards, and PH-004 advisory cite. Both are draft-tier; neither is canonical wiki knowledge.

## File template

```markdown
---
title: "Session Orientation — {stage label}"
type: session-orientation
project: "{slug}"
stage: vp-brief | pm-prd | architecture | engineering
status: draft
not_canonical: true
draft_tier: true
last_updated: {ISO-8601 timestamp}
created: {ISO date}
updated: {ISO date}
---

# Session Orientation — {stage label}

> **NOT CANONICAL.** Draft-tier session state only. Never cite in published project prose or wiki articles. Promotion to `wiki/` requires explicit compile + user approval + align-cite.

## Active context

What the next session must know immediately: current focus, artifact paths, CEO deltas since last session.

## Remember this

CEO or agent preferences and principles for this stage. Proposal-only until CEO confirms at session end.

- {preference or working note}

## Session notes

Free-form working notes, scratch ideas, and exploration log. Unverified until compiled into stage artifact.

## Working assumptions (unverified)

Hypotheses not yet grounded in scoped sources. Do not treat as locked decisions (use `handoff.md` for PH-003 locks).

| Assumption | Source / reason | Verified? |
|---|---|---|
| | | no |
```

## Usage rules

| Rule | Detail |
|---|---|
| Location | One optional `orientation.md` per active stage directory |
| Write trigger | During exploration; session end after CEO confirms accuracy (optional RC-164 session audit before confirm) |
| Read trigger | Session start after `handoff.md` (resumability order) |
| Promotion | **Never** auto-promote to wiki, standards, or published artifacts |
| Finalize | **Exclude** from wikilink rewrite and `review` promotion (RC-163) |
| Compile path | Extract verified facts into stage artifact `sources`; run compile only with user approval |

## Fail closed

- Agents must not write orientation content into `wiki/workspace-standards/**`, `wiki/workspace-recommendations/**`, or published project artifacts without compile approval.
- Do not cite `orientation.md` in stage artifact body at `review` or `published` status.
- RC-116 `agent_mode: thinking` may write exploration notes here or under `research/` only.
- RC-164 session audit proposes **Remember this** rows; CEO approves before write.

## See also

- Session audit (RC-164): `.github/skills/session-audit/SKILL.md`

- Handoff (RC-058): `templates/workspace/handoff.md`
- Stage scaffold (RC-130): `templates/workspace/project-stage-scaffold/README.md`
- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-163-disposable-session-orientation.md`
- RC-058 ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md`
