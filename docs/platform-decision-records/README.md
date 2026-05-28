# Platform Decision Records

Architecture decisions for Second Brain platform lane (RC/PH claims). Per **PH-2026-05-27-008**.

## Naming convention

| State | Path pattern | H1 title | Who writes |
|---|---|---|---|
| **Proposed** | `DRAFT-{id}-{slug}.md` | `# DRAFT ADR:` | `platform-research-review` |
| **Accepted** | `{id}-{slug}.md` | `# ADR:` | **`platform-implement-backlog`** on PIC accept |
| **Template** | `DRAFT-template-research-claim.md` | — | Never promoted |

Examples:

- Pending: `DRAFT-RC-2026-05-27-050-verbatim-cite-excerpts.md`
- Accepted: `RC-2026-05-27-014-platform-research-artifacts.md`

## PIC accept promotion

After CEO accepts a PIC cycle, the **`platform-implement-backlog` agent** runs (not the CEO):

```bash
python scripts/promote-platform-adr.py --root . --claim-id {id} --pic-cycle {cycle_id}
```

Fallback for hygiene ADRs without standard id prefix:

```bash
python scripts/promote-platform-adr.py --root . --file docs/platform-decision-records/DRAFT-{id}-{slug}.md
```

The script:

1. Strips `DRAFT-` from the filename
2. Updates `# DRAFT ADR:` → `# ADR:`
3. Adds `## Approval` if missing
4. Rewrites references across the repo

## Required sections

All ADRs (per RC-015):

- `## Status`
- `## Approval` (on accept)
- `## Context`, `## Decision`, `## Rationale`
- Experiment ADRs: `## Intent`, `## Safety and non-goals`

Template: `templates/platform-research/platform-adr.md`

## See also

- Policy ADR: `PH-2026-05-27-008-adr-promotion-on-accept.md`
- Implementation loop: `RC-implementation-priority-loop.md`
- Research review write scope: `config/platform-research-review.example.yml` (`DRAFT-*.md` only)
