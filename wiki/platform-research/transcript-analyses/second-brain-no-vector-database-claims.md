# Claims Analysis: second-brain-no-vector-database

## Source

- Transcript: `raw/platform-transcripts/second-brain-no-vector-database.txt`
- Processing limitations: short social transcript; performance claims are unvalidated.

## Executive Judgment

This transcript strongly reinforces Second Brain's existing v1 retrieval direction. The useful idea is not "never use vectors"; it is that long-document retrieval should preserve document structure and produce an inspectable trail. That is already close to Second Brain's index-guided retrieval policy and strengthens the rationale for requiring `workspace-align-cite` rather than trusting retrieval similarity.

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-001 | `architecture_proposal` | adopt | Prefer structure-aware page-index retrieval over vector chunking for long documents. |
| RC-2026-05-27-002 | `risk_claim` | adopt | Similarity is not support; citation checks must verify the claim against source content. |

## Grounding Notes

- `AGENTS.md` already defines index-guided query and inspectable retrieval as core operations.
- `docs/architecture-rationale.md` already defers embeddings until the wiki passes roughly 500 articles.
- `PRD.md` treats `workspace-align-cite` as production quality, which directly answers the "similarity is not relevance" risk.

## Recommended Next Actions

- Draft an ADR codifying page-index retrieval as the v1 default and defining what evidence would justify hybrid retrieval later.
- Keep `workspace-align-cite` as a publish blocker.
