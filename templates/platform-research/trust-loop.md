# Trust Loop Workflow Pattern

Reliable Second Brain workflows use small loops with explicit trust state, not silent automation.

## Loop stages

| Stage | Meaning | Platform research example |
|---|---|---|
| Capture | Record raw input without mutation | Transcript preserved under `raw/platform-transcripts/**` |
| Schema | Route into typed artifacts | Claim record YAML with required fields |
| Audit | Log decisions and evidence | `wiki/log.md`, decision history in implementation backlog |
| Confidence | Record validation state | `validation_status` on each claim |
| Guardrail | Fail closed on uncertainty | No `adopt` when `requires_external_validation: true` and status is `unvalidated` |
| Surface | Present reviewable package | Impact report + draft ADR |
| Correct | Explicit user correction path | `correction_route` on each claim; backlog accept/rollback |

## Required trust fields (claim records)

```yaml
validation_status: unvalidated | supported_by_current_design | validated_against_design | validated
requires_external_validation: true | false
correction_route: "How the user approves, rejects, or reopens this claim."
```

## Validation status values

| Value | Meaning |
|---|---|
| `unvalidated` | Not yet checked against primary sources or design |
| `supported_by_current_design` | Consistent with existing docs but not re-verified this review |
| `validated_against_design` | Checked against AGENTS.md, PRD, or related canonical docs |
| `validated` | Checked against primary external source when required |

## Fail-closed rule

When `requires_external_validation: true` and `validation_status` is `unvalidated`:

- Do not decide `adopt`
- Prefer `monitor`, `defer`, or `experiment` with explicit validation gap
- Record the gap in the impact report `## Trust Loop Summary`

## Correction routes by decision

| Decision | Default correction route |
|---|---|
| adopt | Approve draft ADR via implementation backlog; reject via backlog rollback |
| experiment | Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback |
| defer | Re-enter queue when blocker clears; update claim register |
| reject | Re-review per `rejected-ideas.md` `next_review_after`; submit safer variant as new claim |
| monitor | Re-review when external validation is available |

## Impact report sections

Every impact report should include:

- `## Trust Loop Summary` — validation gaps and confidence guardrails applied
- `## Correction Routes` — how the user approves, rejects, or reopens each top claim
