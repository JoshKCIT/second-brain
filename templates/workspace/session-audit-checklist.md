# Session audit checklist (RC-164)

Use with `.github/skills/session-audit/SKILL.md` at workspace project session end.

## Pre-audit read

- [ ] `wiki/workspace-projects/{slug}/meta.yml` — confirm `status: in-progress`
- [ ] Active stage `handoff.md`
- [ ] Active stage `orientation.md` (create from template if audit will write orientation rows)
- [ ] Sub-scaffold orientation if auditing a workstream (RC-167)

## Proposal table (fill before asking CEO)

| ID | Route | Target section | Proposed text | Already persisted? |
|---|---|---|---|---|
| SA-001 | orientation \| handoff \| reject | | | yes / no |

## CEO checkpoint (required)

- [ ] Presented proposal table
- [ ] CEO chose: accept all / accept IDs: ___ / skip / edit
- [ ] No writes before checkpoint answer

## Post-audit

- [ ] Only accepted IDs written
- [ ] Frontmatter `updated` timestamps set
- [ ] `wiki/log.md` entry appended
- [ ] Confirmed zero unapproved mutations

## Validation metrics (H-027 pilot)

Track per session: proposals count, accepted count, rejected count, unapproved writes (must be 0).

## See also

- Orientation template: `templates/workspace/orientation.md`
- Handoff template: `templates/workspace/handoff.md`
- ADR: `docs/platform-decision-records/RC-2026-05-27-164-session-audit-skill.md`
