# DRAFT ADR: RC-2026-05-27-163 - Disposable Session Orientation

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-163
- Source transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
- Speaker: Jeff
- Timestamp: 00:06:30-00:08:30
- Claim type: workflow_proposal

## Context

Cowork uses memory.md for active projects and "remember this" entries. Second Brain has RC-058 handoff.md and RC-020 disposable memory hypothesis but no standard orientation file distinct from wiki canonical layer.

## Decision

Introduce optional `orientation.md` per project stage (or `handoff.md` extension) marked **draft-tier, not canonical**. Holds active context, next actions, and session notes. Promotion to wiki requires compile + user approval + align-cite.

## Intent

- **Intended outcome:** Multi-session resumption without wiki pollution or RC-169 memory-as-truth pattern.
- **In scope:** Template, frontmatter banner, finalize prompt hook, lint rule blocking wiki promotion without compile.
- **Out of scope:** Auto "remember this" writes; Gmail-derived memory.

## Safety and non-goals

- **Safety posture:** Fail closed — orientation writes never update `wiki/workspace-standards/**` or published artifacts.
- **Non-goals:** Replacing handoff.md; unbounded persistent memory as truth.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Safer Cowork memory pattern mapped to governed project stages.

## Impact Scores

Total: 9 (experiment)

## Alternatives Considered

- Cowork memory.md auto-write — rejected (RC-169).
- Wiki-only session state — rejected (closure risk at publish).

## Consequences

### Positive

- CEO and agents restart with filesystem inspectable state.

### Negative / Risks

- Stale orientation if not updated at session end (mitigate RC-164 audit skill).

### Safeguards

- Required frontmatter: `type: session-orientation`, `status: draft`, `not_canonical: true`.

## Validation Plan

Pilot on one project stage for two weeks; verify zero wiki writes from orientation without explicit compile approval.

## Files Proposed for Future Change

- `templates/workspace/orientation.md` (new)
- `.github/prompts/finalize.prompt.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md` (cross-link)
