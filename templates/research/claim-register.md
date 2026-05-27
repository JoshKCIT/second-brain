# Research Claim Register

This register tracks transcript-derived claims about Second Brain.

Transcripts are product-intelligence evidence. They are not canonical knowledge by default.

## Decision Legend

| Decision | Meaning |
|---|---|
| `adopt` | Implement or document immediately after user approval |
| `experiment` | Test before adoption |
| `defer` | Valuable but blocked by dependency |
| `reject` | Harmful, redundant, generic, or misaligned |
| `monitor` | External market/vendor claim to revisit later |

## Claim Records

Add new records below. Use one YAML block per claim.

```yaml
claim_id: RC-YYYY-MM-DD-001
source_transcript: raw/transcripts/path/to/transcript.md
speaker: unknown
timestamp: unknown
claim_type: product_requirement
atomic_claim: ""
verbatim_excerpt: ""
implied_assumption: ""
current_design_status: unsupported
evidence_supplied_by_speaker: none
requires_external_validation: false
validation_status: unvalidated
affected_components:
  - ""
related_second_brain_principles:
  - source_authority
  - claim_level_conflict_resolution
  - junior_engineer_closure
expected_benefit: ""
possible_regression: ""
validation_method: ""
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 0
decision: experiment
decision_rationale: ""
next_action: ""
owner: unassigned
status: open
last_reviewed: YYYY-MM-DD
```
