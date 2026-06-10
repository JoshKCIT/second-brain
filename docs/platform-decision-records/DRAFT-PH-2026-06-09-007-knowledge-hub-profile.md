# DRAFT ADR: PH-2026-06-09-007 - Knowledge Hub Chain Profile

## Status

Draft

## Context

CEO request: building a Knowledge Hub (curated wiki from Confluence scope). Overlaps compile lane (RC-146, RC-148) but needs distinct deliverables and stage flow.

## Decision

Ship `templates/workspace/chain-profiles/knowledge-hub.yml` with stages:

1. **charter** — VP/PM-lite hub scope, in-scope spaces, retrieval contract
2. **ingest-compile** — gated ingest + compile batches (RC-146, RC-148)
3. **structure** — information architecture (navigation, Base views, index updates)
4. **authoring** — technical writer landing pages
5. **qa** — align + lint on hub artifact set
6. **publish** — CEO-gated

**Closure rule:** Hub must be navigable from `wiki/index.md` with cited sources per concept/standard article.

## Approval

- Pending PIC; workspace trigger: first hub project declared at start-project
