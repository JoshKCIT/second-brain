---
description: Controlled platform gap review. Identifies missing platform knowledge and candidate sources without mutating canonical docs or workspace knowledge.
mode: agent
---

# /platform-gap-review

You are running a **controlled platform gap-review cycle** for Second Brain (experiment RC-2026-05-27-003).

## Objective

Proactively find platform knowledge gaps and propose **candidate sources** for future review. Output hypotheses and a gap-review report only. Do not self-update canonical docs, workspace wiki, or raw mirrors.

## Non-negotiable rules

- **Platform lane only.** Scope is improving Second Brain itself, not workspace project documentation.
- **Candidate sources only.** Propose transcripts, papers, vendor docs, or benchmarks to review later via `/platform-research-review`. Do not ingest or mutate `raw/**` without explicit user approval.
- **No protected writes.** Allowed outputs: `wiki/platform-research/**`, `reports/platform-research-review/**`, `docs/platform-decision-records/DRAFT-*.md`.
- **Check rejection history.** Read `wiki/platform-research/rejected-ideas.md` before proposing ideas that match recurring rejection patterns (`RP-*`).
- **Evidence quality required.** Every gap and candidate source must name evidence quality and a validation method.

## Inputs (read before analyzing)

```text
product-brief.md
PRD.md
docs/architecture-rationale.md
docs/roadmap.md
wiki/platform-research/claim-register.md
wiki/platform-research/rejected-ideas.md
wiki/platform-research/open-hypotheses.md
wiki/platform-research/implementation-backlog.md
AGENTS.md
```

Optionally scan recent platform research reports under `reports/platform-research-review/`.

## Workflow

1. Summarize current platform direction from canonical docs (one paragraph).
2. List **open gaps**: missing evals, unresolved hypotheses, blocked backlog items, scope questions, or weakly grounded claims in the claim register.
3. For each gap, propose zero or more **candidate sources** (title, URL or search query, why it might help, evidence quality, validation method).
4. Flag any candidate that resembles a **rejected pattern** or would require protected-file mutation without an ADR.
5. Update `wiki/platform-research/open-hypotheses.md` only when a new testable hypothesis emerges.
6. Write `reports/platform-research-review/gap-review-{YYYY-MM-DD}.md` using `templates/platform-research/gap-review-report.md`.
7. Run `python scripts/lint-platform-research.py --root .` if claim register or other linted artifacts changed.

## Cadence

Default: **monthly**, manual, user-triggered. Do not run autonomously on a schedule without user invocation.

## Output files

```text
reports/platform-research-review/gap-review-{YYYY-MM-DD}.md
wiki/platform-research/open-hypotheses.md   (if updated)
```

## Final response

Summarize:

- Gaps identified (count)
- Candidate sources proposed (count)
- Hypotheses added or updated
- Rejected patterns avoided
- Protected files not modified

Experiment ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-003-controlled-gap-research.md`
