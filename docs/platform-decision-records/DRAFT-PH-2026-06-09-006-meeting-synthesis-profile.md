# DRAFT ADR: PH-2026-06-09-006 - Meeting Synthesis Chain Profile

## Status

Draft

## Context

CEO request: Solution Architecture meeting → governed decision documentation. RC-140 (meeting notes lane) and H-2026-05-27-018 provide capture foundation.

## Decision

Ship `templates/workspace/chain-profiles/meeting-synthesis.yml` with stages:

1. **capture** — human-approved ingest to `raw/workspace-meetings/` (RC-140)
2. **synthesize** — thinking-partner or dedicated synthesizer → `research/`
3. **requirements** — PM-lite decisions/open questions
4. **document** — technical writer (PH-003) optional
5. **qa** — PH-005 optional
6. **publish** — CEO-gated

**Closure rule:** Published set must cite meeting raw sources; may be decision-record shaped rather than full jr-engineer engineering specs.

## Intent

- **Out of scope:** Auto-ingest Slack/Teams; messaging responders (rejected).

## Approval

- Pending PIC; workspace trigger: first meeting ingest pilot (RC-140)
