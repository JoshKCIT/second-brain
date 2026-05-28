# Instruction stack header (RC-161)

Copy into `.github/prompts/*.prompt.md` after the title. Tier-1 IDE shims (`.cursor/rules/agents.mdc`, `CLAUDE.md`, `.github/copilot-instructions.md`) inherit `AGENTS.md` and add tool-specific invocation only.

## Prompt frontmatter (tier 2)

```yaml
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace   # or platform
```

## Body block (tier 2)

```markdown
## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only (`workspace-*` or `platform-*`).
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.
```

## Tier 3 project scaffolds (optional)

Place under `wiki/workspace-projects/{slug}/` or stage subdirs when multi-session work needs scoped rules:

```yaml
# frontmatter on STAGE-SCAFFOLD.md (draft-tier, not canonical)
inherits: AGENTS.md
instruction_stack_tier: 3
project: {slug}
stage: vp-brief | pm-prd | architecture | engineering
```

Scaffolds may add voice, scope, or handoff notes. They must not duplicate Tier-1 governance bullets or weaken approval gates.

## Routing (RC-162)

Before loading project depth, classify task type using `templates/workspace/routing-map.md` or `AGENTS.md` § Routing map. Routing is orientation-only; RC-122 read-before-write still applies.

## Tier 3 sub-scaffolds (RC-167)

Optional workstream threads: `wiki/workspace-projects/{slug}/0X-{stage}/subprojects/{workstream}/`

- `STAGE-SCAFFOLD.md` — workstream instruction shim (`instruction_stack_tier: 3`)
- Local `orientation.md` and `resources/` — draft-tier only
- All sub-scaffold files require `publish_scope: exclude` and `not_canonical: true`

Template: `templates/workspace/project-sub-scaffold/README.md`
