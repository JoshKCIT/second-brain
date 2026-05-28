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
- Write notes to `orientation.md` (RC-163) or `research/` only
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

## See also

- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-116-thinking-artifact-mode-separation.md`
- Orientation (RC-163): `templates/workspace/orientation.md`
- RC-117 thinking-partner (depends on RC-116)
