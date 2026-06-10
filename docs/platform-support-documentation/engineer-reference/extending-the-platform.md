---
title: "Extending the platform"
audience: engineer
generated: true
last_sync: 2026-06-10T18:00:00Z
status: draft
sources:
  - "AGENTS.md"
  - "templates/workspace/routing-map.md"
  - "wiki/platform-research/implementation-backlog.md"
---

# Extending the platform

## Adding a workspace feature

1. Add prompt under `.github/prompts/workspace-*.prompt.md` with `inherits: AGENTS.md`.
2. Update [routing-map.md](../../../templates/workspace/routing-map.md) and AGENTS.md routing row (minimal delta).
3. Add lifecycle doc under `templates/workspace/` if needed.
4. Run `/platform-sync-support-docs` to refresh support documentation.
5. Add tests under `tests/`.

## Adding a platform feature

1. Route through platform research review or draft ADR.
2. Queue in [implementation-backlog.md](../../../wiki/platform-research/implementation-backlog.md).
3. Deliver via `/platform-implement-backlog` one PIC at a time.
4. Agent runs `promote-platform-adr.py` on accept.

## Protected files

Do not mutate without explicit approval: `AGENTS.md`, `PRD.md`, `product-brief.md`, `docs/product/roadmap.md`, `wiki/workspace-standards/**`, workspace projects.

## See Also

- [architecture-map.md](architecture-map.md)
- [adr-index.md](adr-index.md)
- [docs/platform-intelligence/](../../platform-intelligence/)

## Sources consulted

- AGENTS.md, routing-map.md, implementation-backlog.md
