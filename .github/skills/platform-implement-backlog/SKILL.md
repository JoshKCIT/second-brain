# Platform implement backlog

Use when the CEO accepts a platform PIC cycle or asks to implement the next item from `wiki/platform-research/implementation-backlog.md`.

## When to use

- "Start PIC-026" / "implement the next backlog item"
- After research review: CEO approved a draft ADR and wants implementation
- Completing a PIC cycle with accept/reject and ADR promotion

Do **not** use for transcript import (`platform-transcript-librarian`) or claim scoring (`platform-research-review`).

## Workflow

Follow `.github/prompts/platform-implement-backlog.prompt.md`:

1. Load backlog → select item → implement → validate
2. Present to CEO → wait for accept/reject
3. On accept: update ADR Status/Approval, then **you** run:

```bash
python scripts/promote-platform-adr.py --root . --claim-id {claim_id} --pic-cycle {cycle_id}
```

4. Update backlog queue path to promoted ADR (no `DRAFT-` prefix)

**Never ask the CEO to run `promote-platform-adr.py`.** PH-008.

## See also

- Process ADR: `docs/platform-decision-records/RC-implementation-priority-loop.md`
- Promotion policy: `docs/platform-decision-records/PH-2026-05-27-008-adr-promotion-on-accept.md`
- Script: `scripts/promote-platform-adr.py`
