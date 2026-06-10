---
title: "Architecture map"
audience: engineer
generated: true
last_sync: 2026-06-10T20:00:00Z
status: draft
sources:
  - "AGENTS.md"
  - "docs/product/architecture-rationale.md"
  - "README.md"
---

# Architecture map

## Three layers

```
raw/     — immutable source (Confluence, vendor, RSS, transcripts)
wiki/    — LLM-curated knowledge (standards, concepts, projects)
AGENTS.md — schema and operating spec (Tier 1)
```

**Compiler analogy:** raw = source; agent = compiler; wiki = executable knowledge; align + lint = test suite.

Personal/gitignored raw: `raw/workspace-rss-feed/`, most Confluence/wiki content locally.

## Instruction stack

| Tier | Source | Role |
|------|--------|------|
| 1 | AGENTS.md | Governance invariants |
| 2 | Prompts, IDE shims | Task scope |
| 3 | meta.yml, stage scaffolds | Project scope |

Pointer depth: [templates/workspace/pointer-resources/](../../../templates/workspace/pointer-resources/).

## Operator and user workflows (v2)

- [how-second-brain-works.md](../user-guide/how-second-brain-works.md) — mental model
- [workflow-ingest.md](../user-guide/workflow-ingest.md) — ingest flows
- [workflow-project-chain.md](../user-guide/workflow-project-chain.md) — agent chain
- [concepts-for-operators.md](../operator-guide/concepts-for-operators.md) — governance plain language

## See Also

- [docs/product/architecture-rationale.md](../../product/architecture-rationale.md)
- [adr-index.md](adr-index.md)
- [extending-the-platform.md](extending-the-platform.md)
- [scripts-and-automation.md](scripts-and-automation.md)

## Sources consulted

- AGENTS.md, docs/product/architecture-rationale.md, README.md
