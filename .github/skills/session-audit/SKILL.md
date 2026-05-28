---
name: session-audit
description: End-of-session audit for workspace projects. Scans conversation for unsaved preferences and proposes orientation or handoff updates with explicit CEO approval before any write. Use at session end on in-progress projects.
---

# Session Audit Skill (RC-164)

Use when the CEO or stage agent closes a workspace project session and wants to capture learnings without silent memory writes.

## Purpose

Governance-friendly alternative to Cowork `/session audit` and auto `memory.md` writes (RC-169 reject). Proposes updates to **draft-tier** project files only; never promotes content to canonical wiki.

## When to invoke

- Stage agent **session end** (after draft work, before CEO confirms handoff)
- Engineer **finalize** (optional pass before post-finalize handoff update)
- CEO explicit request: `/workspace-session-audit` or "run session audit"

## Read first

- Active stage `handoff.md` (RC-058, PH-003 sections)
- Active stage `orientation.md` if present (RC-163)
- Sub-scaffold `subprojects/{workstream}/orientation.md` if auditing a workstream (RC-167)
- `templates/workspace/session-audit-checklist.md`

## Core rule

**Proposal-only by default.** Classify candidates; present diffs; **stop** for CEO approval per item. Write nothing until the CEO accepts specific rows.

## Workflow

### 1. Scan

Review the session conversation and current `handoff.md` / `orientation.md`. Extract candidates not already persisted:

| Category | Examples |
|---|---|
| Preferences / principles | Voice, formatting, decision style |
| Active context | Current focus, blockers, next file to open |
| Open decisions | Unresolved questions for CEO or next agent |
| Working assumptions | Unverified hypotheses (orientation only) |
| Handoff deltas | Next steps, completed/left incomplete |

**Exclude:** chat noise, one-off typos, content already in handoff/orientation, anything requiring wiki compile, vendor claims without sources, platform-lane product ideas (route to platform research).

### 2. Classify each candidate

| Route | Target file | Use when |
|---|---|---|
| **orientation** | `{stage}/orientation.md` or sub-scaffold orientation | Preferences, session notes, unverified assumptions |
| **handoff** | `{stage}/handoff.md` | Next steps, open decisions, starting context, last session block |
| **reject** | — | Noise, duplicate, ungrounded, or belongs in stage artifact body |

### 3. Propose (mandatory checkpoint)

Present a table before any write:

```markdown
## Session audit proposals — {slug} / {stage}

| ID | Route | Section | Proposed addition | Rationale |
|---|---|---|---|---|
| SA-001 | orientation | Remember this | … | CEO stated preference … |
| SA-002 | handoff | Next steps | … | Agreed next action … |
| SA-003 | reject | — | … | Already in handoff L-002 |
```

Ask CEO: **Accept all / Accept selected IDs / Skip audit / Edit then accept.**

Do **not** proceed past this checkpoint in the same turn without an answer.

### 4. Write (approved items only)

For each accepted row:

- Append to the target section in `orientation.md` or `handoff.md`
- Update frontmatter `updated` and `last_updated` (orientation) or `last_session` (handoff)
- Create `orientation.md` from `templates/workspace/orientation.md` if missing and route is orientation

**Never write:**

- `wiki/workspace-standards/**`, `wiki/workspace-recommendations/**`, `wiki/workspace-concepts/**`
- Stage artifact bodies at `review`/`published` without a separate CEO-approved edit pass
- `raw/**`

### 5. Log

Append to `wiki/log.md`:

```
## [{ISO timestamp}] session-audit | {slug} | {stage}
- Proposed: {N}
- Accepted: {N} (orientation={n}, handoff={n})
- Rejected: {N}
- Unapproved writes: 0
```

## Fail closed

- Zero file mutations before CEO accepts specific proposal IDs
- If CEO skips audit, log `session-audit-skipped` only — do not write orientation/handoff from audit
- Do not treat audit output as citation support or locked decisions (PH-003 locks require CEO gate)

## Integration

- RC-163: primary write target for preferences is `orientation.md` **Remember this**
- RC-058: handoff **Next steps**, **Open decisions**, **Last session**
- RC-167: may audit sub-scaffold orientation; merge summaries to parent handoff when workstream closes

## See also

- Checklist template: `templates/workspace/session-audit-checklist.md`
- Prompt: `.github/prompts/workspace-session-audit.prompt.md`
- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-164-session-audit-skill.md`
