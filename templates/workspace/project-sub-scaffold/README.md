# Project sub-scaffold (RC-167)

Optional **workstream threads** under a stage directory for long-running sub-efforts within one project stage (e.g., a security review thread during architecture, or a component spec thread during engineering).

Maps Cowork workstation nesting to governed enterprise scope: **not** personal-life workstations (RC-168 reject).

## Layout

```text
wiki/workspace-projects/{slug}/0X-{stage}/
├── handoff.md                    # RC-058 stage restart
├── orientation.md                # RC-163 stage session notes
├── research/ | chats/ | daily-progress/   # RC-130
├── {stage-artifact}.md           # publish-bound stage output
└── subprojects/{workstream}/     # RC-167 optional sub-scaffold
    ├── STAGE-SCAFFOLD.md         # Tier-3 instruction shim (this workstream)
    ├── orientation.md            # workstream-local session notes
    └── resources/                # clipped assets, links, scratch (optional)
```

## Three-level instruction stack (RC-161 + RC-167)

| Tier | Source | Scope |
|---|---|---|
| 1 | `AGENTS.md` | Root invariants; non-overridable |
| 2 | `.github/prompts/workspace-{stage}-agent.prompt.md` | Stage agent contract |
| 3 | `subprojects/{workstream}/STAGE-SCAFFOLD.md` | Workstream voice, focus, local rules |

Load order on invoke when working a sub-scaffold:

1. Read Tier 1 invariants (via prompt inheritance)
2. Read Tier 2 stage agent prompt scope
3. Read parent stage `handoff.md` and `orientation.md` (RC-058, RC-163)
4. Read `subprojects/{workstream}/STAGE-SCAFFOLD.md` and local `orientation.md`

Tier 3 must declare `inherits: AGENTS.md` and must **not** restate Tier-1 governance bullets.

## Frontmatter contract

All files under `subprojects/**` require:

```yaml
publish_scope: exclude
draft_tier: true
not_canonical: true
type: project-sub-scaffold   # or session-orientation for orientation.md
status: draft
project: "{slug}"
stage: vp-brief | pm-prd | architecture | engineering
workstream: "{workstream-slug}"
```

`STAGE-SCAFFOLD.md` additionally:

```yaml
inherits: AGENTS.md
instruction_stack_tier: 3
```

## Usage rules

| Rule | Detail |
|---|---|
| When to create | CEO or stage agent identifies a parallel workstream that would clutter stage `handoff.md` |
| Naming | Lowercase kebab-case `{workstream}`; max ~40 chars |
| Writes | Notes and resources only; verified decisions compile into stage artifact or parent handoff |
| Cross-project | Sub-scaffold wikilinks must not reference in-progress or archived projects (same as stage artifacts) |
| Finalize | **Exclude** entire `subprojects/**` tree from wikilink rewrite and `review` promotion |
| align-closure | Published artifact set = stage `*.md` project artifacts only; sub-scaffold paths never in publish set |
| Publish | CEO may archive/delete `subprojects/` after stage approval; not part of jr-engineer-executable set |

## Fail closed

- Sub-scaffold content is never canonical wiki knowledge without compile + approval + align-cite.
- Do not cite `subprojects/**` paths in stage artifact body at `review` or `published`.
- Do not create sub-scaffolds for platform-lane work; use `platform-*` prompts instead.

## Templates

- Sub-scaffold shim: `templates/workspace/project-sub-scaffold/STAGE-SCAFFOLD.md`
- Local orientation: `templates/workspace/project-sub-scaffold/orientation.md`

## See also

- RC-130 stage scaffold: `templates/workspace/project-stage-scaffold/README.md`
- RC-161 instruction stack: `templates/workspace/instruction-stack-header.md`
- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-167-project-subfolder-rule-stacking.md`
- RC-130 ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-130-project-stage-scaffold.md`
