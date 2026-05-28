# Platform Research Artifact Package

Each transcript review produces a claim-plus-evidence package. Preserve negative knowledge and validation gaps alongside adopted ideas.

## Required artifacts

| Artifact | Path |
|---|---|
| Claim register | `wiki/platform-research/claim-register.md` |
| Rejection register | `wiki/platform-research/rejected-ideas.md` |
| Open hypotheses | `wiki/platform-research/open-hypotheses.md` |
| Implementation backlog | `wiki/platform-research/implementation-backlog.md` |
| Transcript analysis | `wiki/platform-research/transcript-analyses/{slug}-claims.md` |
| Impact report | `reports/platform-research-review/{slug}-impact-report.md` |

## Optional artifacts

| Artifact | Path |
|---|---|
| Batch synthesis | `reports/platform-research-review/batch-synthesis-{date}.md` |
| Final recommendations | `reports/platform-research-review/final-recommendations-{date}.md` |
| Stack analysis | `reports/platform-research-review/claim-stack-analysis-{date}.md` |
| Draft ADR | `docs/platform-decision-records/DRAFT-{claim_id}-{short-title}.md` |
| Platform ADR template | `templates/platform-research/platform-adr.md` |

## Validation

```bash
python scripts/lint-platform-research.py --root .
```

## Delivery loop

After user ADR approval, deliver canonical changes through `wiki/platform-research/implementation-backlog.md` one claim at a time with validation and rollback.
