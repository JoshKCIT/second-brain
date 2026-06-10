# Technical Writer stage (PH-2026-06-09-003)

Optional chain stage between engineering approval and Engineer finalize. **Not included in default `technical-doc-initiative` profile v1.**

## Directory

```
wiki/workspace-projects/{slug}/05-technical-writing/
├── handoff.md
├── orientation.md          (optional, RC-163)
├── research/               (optional)
└── see-also-draft.md       (optional — finalize input)
```

Upstream artifacts are polished in place unless orchestrator directs companion copies here.

## Invoke

```text
/workspace-technical-writer-agent
```

Or orchestrator step after engineering CEO approval when profile includes `technical-writing` stage.

## Prompt

`.github/prompts/workspace-technical-writer-agent.prompt.md`

## ADR

`docs/platform-decision-records/PH-2026-06-09-003-technical-writer-stage.md`
