# Mandatory default load (RC-165)

Content that **must** appear in Tier-2 IDE shims without requiring a pointer read first.

## Always in shims

1. **Identity** — Second Brain repo; read `AGENTS.md` for canonical spec
2. **Architecture** — three layers: `raw/`, `wiki/`, `AGENTS.md`
3. **Agent chain** — CEO → VP → PM → Architect (if technical) → Engineer → finalize
4. **Lane vocabulary** — `workspace-*` vs `platform-*`; classify before touching files
5. **Routing map pointer** — `AGENTS.md` § Routing map + `templates/workspace/routing-map.md`
6. **Instruction stack** — Tier 1/2/3; shims are Tier 2; inherit AGENTS.md
7. **Critical rules (compact)** — all 15 numbered invariants (short form)
8. **Verb names** — list of `.github/prompts/` stems (no long descriptions required in shim)
9. **Skills list** — directory names under `.github/skills/`
10. **Quality bar pointer** — `docs/style/exemplar-published-doc.md`
11. **PH-006 escalation** — workspace → platform for product ideas; no protected edits

## Never only in optional pointers

- Approval-gated mutations (ingest, sync, archive, publish)
- align-cite + align-closure before publish
- Citation-grounded claims; authority + domain
- Read-before-write (RC-122)
- Scoped retrieval per config
- Project closure / jr-engineer-executable rule
- Body-prose-clean at review/published
- Cross-project dependency rules
- Fail closed; no secrets; no telemetry
- Platform research cannot mutate canonical workspace without approval

## May live in pointers only

- Expanded explanations of each critical rule
- Per-verb operation walkthroughs
- Article format YAML templates (canonical copy remains in `AGENTS.md`)
- Worked examples and persona detail
- Lint check inventory detail beyond check names

## Audit baseline (2026-05-28)

| Shim | Lines (post RC-165) |
|---|---:|
| `.cursor/rules/agents.mdc` | 84 |
| `CLAUDE.md` | 77 |
| `.github/copilot-instructions.md` | 63 |

Re-run line audit after stack-lift cycles; record in implementation backlog PIC notes.
