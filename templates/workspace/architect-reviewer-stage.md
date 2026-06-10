# Architect Reviewer stage (PH-2026-06-09-004)

Optional chain stage for **advisory standards conformance** across the project artifact set. **Not included in default `technical-doc-initiative` profile v1.**

## Typical placement

- After architecture CEO approval, or
- After engineering drafts, before technical-writing or finalize

## Output

Primary (canonical for this stage):

```text
reports/workspace-architect-reviewer-{slug}-{YYYY-MM-DD}.md
```

Optional draft-tier working notes:

```text
wiki/workspace-projects/{slug}/03-architecture/research/architect-reviewer-notes.md
wiki/workspace-projects/{slug}/03-architecture/research/architect-reviewer-handoff.md
```

## Invoke

```text
/workspace-architect-reviewer-agent
```

## Prompt

`.github/prompts/workspace-architect-reviewer-agent.prompt.md`

## Report template

`templates/workspace/architect-reviewer-report.md`

## Related verbs

- `workspace-align-conformance` — single-artifact deep dive
- `workspace-align-cite` — citation verification (blocking at publish)
- PH-004 — advisory align-cite per stage

## ADR

`docs/platform-decision-records/PH-2026-06-09-004-architect-reviewer-stage.md`
