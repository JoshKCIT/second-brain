# ADR: PH-2026-05-27-008 - ADR Promotion on PIC Accept (Option A)

## Status

Accepted (PIC-2026-05-28-008, 2026-05-28)

## Approval

- Approved: 2026-05-28
- Cycle: PIC-2026-05-28-008
- Notes: CEO selected Option A — filename, title, and Status align after PIC accept.

## Source

- Hygiene item: PH-2026-05-27-008
- Trigger: ADR filename/title drift (accepted ADRs still named `DRAFT-*`)
- Depends on: RC-015 (Approval sections), RC-implementation-priority-loop (PIC workflow)
- Not a transcript-derived claim

## Context

Platform ADRs were created under `docs/platform-decision-records/DRAFT-{id}-{slug}.md`. PIC acceptance updated `## Status` in many files but **did not rename files or H1 titles**, leaving ~27 accepted records misleadingly prefixed with `DRAFT-`. Cross-repo references (~150) used the draft path as a stable permalink, which discouraged renames.

## Decision

Adopt **Option A — promote on accept**:

| Lifecycle | Filename | H1 title | Written by |
|---|---|---|---|
| Proposed | `DRAFT-{id}-{slug}.md` | `# ADR:` | platform-research-review |
| Accepted | `{id}-{slug}.md` (no `DRAFT-` prefix) | `# ADR:` | PIC accept step |

**PIC accept checklist** (add to implementation loop):

1. Update `## Status` → `Accepted (PIC-{n}, {date})`
2. Add/update `## Approval` (RC-015)
3. H1 → `# ADR:` (drop `DRAFT`)
4. **`platform-implement-backlog` agent** runs `python scripts/promote-platform-adr.py --root . --claim-id {id} --pic-cycle {cycle}` (not the CEO)
5. Verify references and lint

**Batch migration:** One-time promotion of all accepted ADRs via `--all-accepted` (2026-05-28).

**Exceptions:**

- `DRAFT-template-research-claim.md` — template only; never promoted
- Pending ADRs remain `DRAFT-*` until PIC accept

## Intent

- **Intended outcome:** `DRAFT-*` grep finds pending proposals only; accepted ADR paths match their status.
- **In scope:** Promotion script, README, PIC loop update, one-time batch rename + reference sync.
- **Out of scope:** Moving accepted ADRs to a different directory; auto-promote without CEO accept.

## Safety and non-goals

- **Safety posture:** Promotion is metadata + path only; does not mutate AGENTS/wiki without separate implementation PIC.
- **Non-goals:** Renaming pending drafts; rewriting ADR decision text on promote.

## Rationale

Filename–status alignment improves inspectability and matches user mental model. Stable permalinks after accept are acceptable because promotion happens once at a known gate.

## Alternatives Considered

| Alternative | Verdict |
|---|---|
| Option B — stable DRAFT- permalink | Rejected by CEO 2026-05-28 |
| Option C — draft/accepted subdirs | Rejected; same link churn, more path complexity |

## Consequences

### Positive

- Clear pending vs accepted namespace
- `glob DRAFT-*.md` = queue; accepted ADRs listed without prefix filter

### Negative / Risks

- One-time reference churn (~150 paths)
- Future PICs: **`platform-implement-backlog` agent** runs promote script on accept or drift recurs

### Safeguards

- `scripts/promote-platform-adr.py` for single-file and batch promote
- `docs/platform-decision-records/README.md` documents convention
- Lint/platform config keeps `DRAFT-*.md` as research-review write scope only

## Validation Plan

1. All accepted ADRs exist without `DRAFT-` prefix after batch run.
2. `rg 'platform-decision-records/DRAFT-'` returns only pending ADRs + template + this policy doc references to pending paths.
3. `python scripts/lint-platform-research.py --root .` passes.

## See also

- `docs/platform-decision-records/README.md`
- `scripts/promote-platform-adr.py`
- `wiki/platform-research/implementation-backlog.md` § Recursive loop
