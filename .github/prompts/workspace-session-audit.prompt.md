---
description: End-of-session audit for workspace projects. Proposes orientation and handoff updates from conversation; writes only after explicit CEO approval per item.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-session-audit

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `handoff.md`, `orientation.md`) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are running an **RC-164 session audit** on an in-progress workspace project. Follow `.github/skills/session-audit/SKILL.md` in full.

## Inputs

- Project slug (required)
- Optional stage override (`vp-brief`, `pm-prd`, `architecture`, `engineering`); default from `meta.yml` `current_stage`
- Optional workstream path under `subprojects/{name}/` (RC-167)

## Workflow

1. Read the skill and `templates/workspace/session-audit-checklist.md`.
2. Read current stage `handoff.md` and `orientation.md`.
3. Scan the session conversation for unsaved preferences, context, and decisions.
4. Classify each candidate: **orientation**, **handoff**, or **reject**.
5. Present the proposal table; **stop** for CEO approval.
6. Write only accepted rows to draft-tier files.
7. Append audit log entry to `wiki/log.md`.

## Output

Structured proposal report (in chat) plus optional file write to:

`reports/workspace-session-audit-{slug}-{stage}-{date}.md`

when the CEO requests a saved audit record.

## Pass criteria

- Zero unapproved file mutations
- Every write targets `handoff.md` or `orientation.md` (or sub-scaffold orientation) only
- Rejected and skipped items logged

## See also

- Skill: `.github/skills/session-audit/SKILL.md`
- RC-163 orientation: `templates/workspace/orientation.md`
- RC-058 handoff: `templates/workspace/handoff.md`
