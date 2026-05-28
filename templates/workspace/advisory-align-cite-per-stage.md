# Advisory align-cite per stage (PH-004)

Optional, non-blocking citation integrity check on the **current stage artifact** before each CEO gate. Complements blocking pre-publish `align-cite` (Step 12 in `start-project`).

## When to offer

| Trigger | Who offers |
|---|---|
| Stage agent completes draft (`stage_gate: awaiting_ceo_review`) | Stage agent at session end |
| Orchestrator reaches CEO gate (Steps 4, 6, 9, 10b) | `start-project` if not run in session |

Recommend (do not require) advisory cite when the artifact has **five or more** CITED claims or any vendor-domain capability assertion.

## How to run

```text
/workspace-align-cite {artifact-path} --advisory
```

Or invoke `.github/prompts/workspace-align-cite.prompt.md` with `--advisory`.

## CEO choices

| Response | Action |
|---|---|
| **Run advisory cite** | Execute align-cite in advisory mode; show report summary |
| **Skip** | Proceed to CEO gate; log `advisory-cite-skipped` in `wiki/log.md` |
| *(default if CEO silent at gate)* | Skip; do not block |

Advisory failures **never** block PH-003 forward, PH-005 reopen, or gate approval.

## Report and log

- Report path: `reports/workspace-advisory-align-cite-{stage}-{slug}-{date}.md`
- Log entry:
  ```
  ## [{ISO timestamp}] advisory-align-cite | {slug} | {stage}
  - Artifact: {path}
  - Status: pass | fail (advisory)
  - Violations: {count}
  - Report: {path}
  ```

## Handoff record

After run (or explicit skip at session end), update stage `handoff.md` **Advisory cite check** section:

| Field | Value |
|---|---|
| Last run | {ISO timestamp or skipped} |
| Artifact | {path} |
| Result | pass \| fail (advisory) \| skipped |
| Report | {path or —} |
| Violations | {count} |

## Exclusions

Do **not** run advisory align-cite on:

- `handoff.md`, `retrieval-contract.md`, scaffold paths (`research/**`, `thinking-notes/**`, `chats/**`, `daily-progress/**`, `subprojects/**`)
- Artifacts with `invalidated: true` (PH-005)
- Files outside the active stage artifact set

## Stage → artifact map

| Stage | Primary artifact |
|---|---|
| `vp-brief` | `01-vp-brief/product-brief.md` |
| `pm-prd` | `02-pm-prd/product-requirements.md` |
| `architecture` | `03-architecture/architectural-approaches.md` (+ ADRs if cited heavily) |
| `engineering` | All `04-engineering/*.md` project artifacts at `draft` (run per file or slug batch) |

## See also

- ADR: `docs/platform-decision-records/PH-2026-05-27-004-advisory-align-cite-per-stage.md`
- align-cite prompt: `.github/prompts/workspace-align-cite.prompt.md`
- Inter-stage contract: `templates/workspace/inter-stage-contract.md` (PH-003)
