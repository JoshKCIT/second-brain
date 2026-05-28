# Topic / entity compile (RC-148)

Explicit compile workflow mapping Karpathy-style **topics** and **entities** to Second Brain wiki types. Runs inside `/workspace-compile` after RC-146 batch approval.

## Terminology map

| Karpathy / Matt Wolfe term | Second Brain target | Notes |
|---|---|---|
| **Topic** | `wiki/workspace-concepts/{slug}.md` (or standards path when `authority: standard`) | Atomic subject; encyclopedia-style |
| **Entity** | Same as topic when a named thing (service, team, product) | Use concept article; tag `tags: [entity]` when helpful |
| **Cross-link** | `wiki/workspace-connections/{slug}.md` | Non-obvious relationship between 2+ topics/entities |
| **Source trace** | `sources` frontmatter + `## Sources` body | Every compiled claim anchors to `raw/` path + section |

Out of scope: personal consumer topics vault (RC-152 rejected); embedding-only graphs (RC-109 rejected).

## Compile phases (per raw page)

### Phase 1 — Extract topics

1. Read raw page section tree.
2. List candidate **topics**: definitions, patterns, decisions, named capabilities.
3. For each topic, check `wiki/index.md` for an existing concept/standard.
4. **Update** if covered; **create** concept (or standard/recommendation per `authority`) if new.
5. Record raw path in frontmatter `sources`; add `## Sources` with section anchor.

### Phase 2 — Extract entities (optional)

When raw names a durable thing (team, system, vendor product):

1. Prefer one concept article per entity unless merged with an existing topic.
2. Set `aliases` for alternate names found in raw.
3. Do not create duplicate concepts for the same entity under different slugs—merge via update.

### Phase 3 — Synthesize connections

Only when raw **explicitly supports** a relationship between 2+ compiled topics:

1. Create or update `wiki/workspace-connections/{slug}.md`.
2. Set `connects` to wiki paths (no `.md`): e.g. `workspace-concepts/concept-a`, `workspace-concepts/concept-b`.
3. **`## Evidence`** must quote or paraphrase with raw section anchor—no invented links.
4. Add raw path to frontmatter `sources`.
5. **Forbidden:** cross-links with no supporting excerpt in raw; links to concepts not yet compiled from this batch or index.

### Phase 4 — Index and verify

1. Update `wiki/index.md` (concepts table + connections table).
2. Append compile log with topic/connection counts.
3. Offer **advisory align-cite** on new/changed concept and connection articles (`--advisory`).

## Wikilink discipline

| Rule | Detail |
|---|---|
| Raw support required | Every new relationship claim needs a raw excerpt in `## Sources` or `## Evidence` |
| `connects` frontmatter | Lists both endpoints for connection articles; must match Evidence |
| See Also wikilinks | Allowed for navigation; must not introduce unsupported claims |
| Publish-bound cite | Project artifacts citing compiled wiki still require align-cite at publish |

## Batch manifest fields

After compile, report:

```text
Topics created: {n}
Topics updated: {n}
Connections created: {n}
Connections updated: {n}
Advisory align-cite offered: yes | no
```

## Pilot validation (H-026)

One Confluence raw batch: count new concepts/connections; run align-cite; measure false-link rate (links without raw excerpt).

## See also

- Compile prompt: `.github/prompts/workspace-compile.prompt.md`
- Raw inbox: `templates/workspace/raw-inbox-staging.md` (RC-146)
- ADR: `docs/platform-decision-records/RC-2026-05-27-148-topic-entity-compile.md`
