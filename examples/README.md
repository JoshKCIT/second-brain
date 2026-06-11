# examples/

Clean, self-contained reference material for **adopters** — the "clean user
template" half of Decision B (one repo, internal platform boundary, clean
template). Nothing here is live runtime state: the working wiki under `wiki/` is
empty on a fresh clone, and the lab's own platform-research data stays under
`wiki/platform-research/` and `reports/platform-research-review/` until Decision
B's split trigger fires (first external adopter confused by platform content, or
the lab needs independent release/CI).

## What's here

| Path | Purpose |
|------|---------|
| `workspace-projects/demo-s3-encryption/` | A minimal worked project artifact that passes the deterministic align-cite gate. Use it as a shape reference and as a known-good fixture. |

## Run the deterministic align-cite gate against the example

```
second-brain align-cite examples/workspace-projects/demo-s3-encryption/02-pm-prd/product-requirements.md
```

(equivalently `python -m second_brain align-cite ...`). Expect overall verdict
**PASS**: the cited vendor source exists, the blockquote is grounded verbatim in
that source, and the `domain: vendor:aws` artifact cites an `aws` source.

## What this is not

- Not a place to keep your real projects — those live under
  `wiki/workspace-projects/{slug}/` (gitignored; per-user).
- Not the lab's research data — that is platform-lane content and stays in
  `wiki/platform-research/`.
