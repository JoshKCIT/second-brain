---
title: "Scripts and automation"
audience: engineer
generated: true
last_sync: 2026-06-10T20:00:00Z
status: draft
sources:
  - "scripts/README.md"
  - "scripts/verify-setup.py"
  - "scripts/sync-support-doc-inventory.py"
  - "scripts/lint-platform-support-docs.py"
  - ".github/workflows/validate-support-docs.yml"
---

# Scripts and automation

See [scripts/README.md](../../../scripts/README.md) for the full table.

## Support documentation pipeline

Works in **any IDE** (VS Code + Copilot, Claude Code, Cursor, Windsurf):

```bash
python scripts/sync-support-doc-inventory.py --write
# Invoke /platform-sync-support-docs in your agent chat (LLM full regen)
python scripts/lint-platform-support-docs.py --root . --strict
# Review diff → merge via PR or explicit CEO accept
```

## Verify setup (local)

```bash
python scripts/verify-setup.py
```

Creates runtime dirs, runs unit tests, optional platform-research and support-docs lint.

## Scheduled validation (recommended — IDE-agnostic)

**GitHub Actions** [`.github/workflows/validate-support-docs.yml`](../../../.github/workflows/validate-support-docs.yml) is the canonical optional scheduler. It runs on:

- Push/PR when prompts, scripts, or support docs change
- Weekly cron (Monday 09:00 UTC)
- Manual `workflow_dispatch`

The workflow runs inventory drift check, `lint-platform-support-docs.py --strict`, and `tests/platform_support_docs/`. It does **not** run LLM regen or commit changes — merge gates unchanged (RC-146).

| Step | Who | Tool |
|------|-----|------|
| Validate inventory + lint | CI (any contributor IDE) | GitHub Actions |
| Full prose regen | Human + agent | `/platform-sync-support-docs` in VS Code, Cursor, etc. |
| Merge | CEO | PR review |

### Local / OS scheduler (alternative)

Same commands as CI, without GitHub:

```bash
python scripts/sync-support-doc-inventory.py --write
python scripts/lint-platform-support-docs.py --root . --strict
python -m unittest discover -s tests/platform_support_docs -q
```

Use cron or Windows Task Scheduler if you want local reminders; still require human merge.

## Support doc v2 lint depth (strict)

`lint-platform-support-docs.py --strict` enforces:

| Check | Purpose |
|-------|---------|
| `strict_pages` | 21 required pages under user/operator/engineer guides |
| `page_depth` | Min word counts per page class (workflows ≥500, getting-started ≥800) |
| `required_sections` | Per-page `##` headings from `support_doc_common.REQUIRED_SECTIONS` |
| `workflow_structure` | Worked example + approval content on `workflow-*.md` |
| `getting_started_setup` | getting-started contains Credentials, Verify setup, Onboarding sections |
| `manifest_parity` | `manifest.yml` `pages_written` matches disk |
| `glossary_terms` | ≥20 glossary entries |
| `verb_reference_depth` | Top 10 workspace verbs with When / Approve / Outputs |

Definitions: [scripts/support_doc_common.py](../../../scripts/support_doc_common.py).

## Regression gates

```bash
python -m unittest discover -s tests
python scripts/lint-platform-research.py --root .
python scripts/lint-platform-support-docs.py --root . --strict
python scripts/verify-setup.py
python -m unittest discover -s tests/platform_support_docs -q
```

## Sources consulted

- scripts/README.md, verify-setup.py, validate-support-docs.yml, sync-support-doc-inventory.py, lint-platform-support-docs.py
