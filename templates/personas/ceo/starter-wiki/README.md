# CEO Starter Wiki

This directory documents the recommended structure of `wiki/` for a fresh CEO operator instance. The actual content emerges from the user's own ingestion and project work; this is the recommended starting structure.

## Recommended initial structure

After running `/second-brain` onboarding and an initial ingest of the user's default in-scope spaces, the CEO's `wiki/` should look approximately:

```
wiki/
├── index.md                 # populated by initial ingest
├── log.md                   # populated by every operation
├── standards/
│   ├── strategy/            # if Strategy space is in-scope
│   ├── architecture/
│   ├── security/
│   ├── audit/
│   └── (other in-scope teams)
├── recommendations/
│   ├── product/             # if Product space is in-scope
│   ├── engineering-leadership/
│   └── sre/
├── informational/
│   └── (board materials, market context, etc.)
├── concepts/                # populated as compile runs identify atomic concepts
├── connections/             # populated when compile detects cross-cutting insights
├── qa/                      # populated as queries are filed back
├── projects/
│   └── (your active projects)
├── archives/
│   └── (completed and deprecated work)
└── views/
    ├── standards-by-team.base       # CEO-relevant Base view
    ├── active-projects.base
    ├── recent-activity.base
    └── stale-vendor-docs.base
```

## Recommended Bases for CEO operator

Beyond the default Base views, the CEO may benefit from:

- `views/portfolio.base` — all active and recently-published projects with status, owner, and last-activity columns
- `views/risks.base` — articles tagged `#risk` across all in-scope sources
- `views/commitments.base` — articles tagged `#commitment` from Strategy and team-leadership spaces
- `views/board-relevant.base` — articles tagged `#board-relevant` for quick board-prep retrieval

Define these in `wiki/workspace-views/*.base` files using the `obsidian-bases` skill format.

## Tagging recommendations for CEO use

Encourage these tags when authoring or compiling articles:

- `#strategic` — relates to org strategy
- `#commitment` — represents a published commitment
- `#risk` — names a risk
- `#board-relevant` — likely relevant for board context
- `#vendor-dependency` — depends on a vendor capability that should be revalidated periodically

These can be added to article frontmatter or inline. Bases queries reference them.

## What does NOT ship pre-populated

This starter structure is documented but not pre-populated with content. The wiki populates from the user's own ingestion. Pre-populating would create stale or org-irrelevant content.

## When you are operating

After your first project completes and is `published`, this directory's `examples/` (if you create one) can hold reference snapshots of "what a good CEO project artifact set looks like in our org" — useful for future projects and for new operators adopting the kit.
