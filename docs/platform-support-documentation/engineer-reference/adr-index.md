---
title: "ADR index"
audience: engineer
generated: true
last_sync: 2026-06-10T18:00:00Z
status: draft
sources:
  - "docs/platform-decision-records/"
  - "docs/platform-decision-records/README.md"
---

# ADR index

Accepted ADRs live in [docs/platform-decision-records/](../../platform-decision-records/). **`DRAFT-*` files are Draft — not shipped** until promoted via PIC.

## Key accepted records

| ADR | Topic |
|-----|-------|
| RC-2026-05-27-001 | Page-index retrieval |
| RC-2026-05-27-122 | Read-before-write |
| RC-2026-05-27-146 | Raw inbox staging / compile gate |
| RC-2026-05-27-161 | Instruction stacking |
| RC-2026-05-27-162 | Routing map |
| RC-2026-05-27-165 | Pointer resources |
| PH-2026-05-27-003 | Inter-stage output contract |
| PH-2026-05-27-008 | ADR promotion on PIC accept |
| PH-2026-06-09-001–004 | Chain profiles, optional stages |

## Draft (not shipped)

| ADR | Topic |
|-----|-------|
| DRAFT-RC-2026-06-10-017 | RSS feed lane |
| RC-2026-06-10-018 | Platform support documentation lane |
| DRAFT-RC-2026-05-27-135 | Agent hub (superseded by support docs lane) |

Run `python scripts/promote-platform-adr.py` on PIC accept (agent executes, not CEO).

## See Also

- [docs/platform-decision-records/README.md](../../platform-decision-records/README.md)
- [extending-the-platform.md](extending-the-platform.md)

## Sources consulted

- docs/platform-decision-records/
