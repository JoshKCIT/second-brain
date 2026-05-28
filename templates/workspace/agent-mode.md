# Agent mode: thinking vs artifact (RC-116)

Optional frontmatter on project stage artifacts and in `meta.yml` to separate exploration from publish-bound generation.

## Fields

| Location | Field | Values | Default |
|---|---|---|---|
| Stage artifact frontmatter | `agent_mode` | `thinking` \| `artifact` | `artifact` (when absent) |
| `meta.yml` | `agent_mode_default` | `thinking` \| `artifact` | `artifact` |

Artifact frontmatter overrides `meta.yml` default for that file.

## Mode contracts

### `thinking`

- Ask clarifying questions; facilitate exploration
- Write notes to `orientation.md` (RC-163), `research/`, or `thinking-notes/` (RC-117) only
- **Forbidden:** outlines, section drafts, publish-shaped prose in stage artifact bodies
- **Allowed in artifact:** `[NEEDS INPUT]` placeholders and frontmatter updates (`agent_mode`, `updated`)
- Exception: user explicitly requests a file under `research/` or other designated draft subfolder

### `artifact`

- Normal stage agent output rules apply
- Draft status allows body wikilinks; finalize rewrites for `review`

## Lifecycle

| Status | `agent_mode` behavior |
|---|---|
| `draft` | Mode enforced |
| `review`, `published`, `archived` | Mode ignored; artifact is publish-shaped |

Engineer finalize **blocks** `review` promotion when any stage artifact still has `agent_mode: thinking`. CEO must set `artifact` before finalize.

## Pilot validation (H-021)

Track on one draft project: count unpublishable draft fragments in stage bodies with vs without thinking mode.

## Thinking-partner sub-agent (RC-117)

Optional interview-style exploration before artifact generation:

- Invoke: `.github/prompts/workspace-thinking-partner.prompt.md`
- Writes: `thinking-notes/{YYYY-MM-DD}-{topic}.md` only (`type: thinking-notes`, `not_canonical: true`)
- Stage agents read thinking notes on resume but must verify and source facts before artifact body
- Does not replace VP/PM/Architect agents; pairs with `agent_mode: thinking`

Template: `templates/workspace/thinking-partner.md`. Pilot: H-022 A/B one PM stage.

## See also

- ADR: `docs/platform-decision-records/RC-2026-05-27-116-thinking-artifact-mode-separation.md`
- Orientation (RC-163): `templates/workspace/orientation.md`
- RC-117 thinking-partner: `templates/workspace/thinking-partner.md`
