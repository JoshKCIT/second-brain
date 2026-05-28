# Article formats reference (RC-165)

Quick pointer to wiki article shapes. **Canonical schemas remain in `AGENTS.md` § Article types.** Read this for orientation; cite AGENTS.md for lint and publish.

## Types and paths

| type | Path pattern |
|---|---|
| concept | `wiki/workspace-concepts/{slug}.md` |
| standard | `wiki/workspace-standards/{team}/{slug}.md` |
| recommendation | `wiki/workspace-recommendations/{team}/{slug}.md` |
| informational | `wiki/workspace-informational/{slug}.md` |
| connection | `wiki/workspace-connections/{slug}.md` |
| qa | `wiki/workspace-qa/{slug}.md` |
| project-artifact | `wiki/workspace-projects/{slug}/0X-{stage}/{name}.md` |

## Required frontmatter (minimum)

```yaml
title: "..."
type: concept | standard | ...
sources: []
status: published | draft | ...
created: YYYY-MM-DD
updated: YYYY-MM-DD
```

Standards/recommendations/informational also require `authority` and `domain`.

## Project artifact statuses

`draft` → `review` → `published` → `archived`. Body wikilinks allowed at `draft` only.

## See also

- Exemplar: `docs/style/exemplar-published-doc.md`
- Obsidian formatting: `.github/skills/obsidian-markdown/SKILL.md`
