# ADR: RC-2026-06-10-018 — Platform support documentation

## Status

Accepted (PIC-2026-06-10-018, 2026-06-10)

## Approval

- Approved: 2026-06-10
- Cycle: PIC-2026-06-10-018
- Notes: Promoted per PH-2026-05-27-008 (Option A filename sync).


## Context

Second Brain documentation is distributed across `README.md`, `docs/platform-support-documentation/`, `AGENTS.md`, prompts, ADRs, and lifecycle templates. Users and engineers lack a single derived manual. RC-135 proposed a disposable agent hub index; this lane subsumes that intent into tracked, linted support documentation.

## Decision

Add `docs/platform-support-documentation/` as a **derived, full-regen** documentation compile lane:

1. **Inventory** — `scripts/sync-support-doc-inventory.py` scans prompts, scripts, lifecycles, ADRs, routing map.
2. **Compile** — `/platform-sync-support-docs` regenerates all support pages with citation-grounded frontmatter.
3. **Validate** — `scripts/lint-platform-support-docs.py` checks links, sections, prompt parity, contamination.
4. **Merge gate** — CEO accepts diff or PR; no silent auto-commit.

## Intent

- **Intended outcome:** One place for user, operator, and engineer documentation; background agent may regen; humans approve merge.
- **v2 (2026-06-10):** Self-contained operator and new-user manual — workflow pages, worked examples, depth lint, install in `getting-started.md`; removed redundant `docs/setup-kit.md` (v2.1).
- **In scope:** `docs/platform-support-documentation/**`, inventory JSON, lint, prompt, tests.
- **Out of scope:** Replacing `AGENTS.md`; autonomous `wiki/**` writes (RC-151/146).

## Safety and non-goals

- **RC-146:** Support docs describe compile gates; sync does not bypass them.
- **RC-151:** No unattended wiki compile.
- **RC-135:** Superseded by tracked support docs with lint (disposable reports optional for sync-log only).

## Validation

| ID | Check |
|----|-------|
| G-1 | Sync prompt allowlist excludes `wiki/**` |
| G-2 | CEO y/n or PR before commit |
| G-3 | Pages state AGENTS.md is authoritative |
| G-4 | DRAFT ADRs labeled in adr-index |
| G-5 | Frontmatter sources exist on disk |
| G-6 | Full regen updates manifest; lint passes |

Automated: `python -m unittest discover -s tests/platform_support_docs`; `lint-platform-support-docs.py --strict`; GitHub Actions `.github/workflows/validate-support-docs.yml` (IDE-agnostic; no LLM regen in CI).

## Automation (IDE-agnostic)

- **Validation:** GitHub Actions on push/PR + weekly cron — inventory drift, lint, unit tests.
- **Full regen:** `/platform-sync-support-docs` in any agent-capable IDE; CEO approves PR.
- **Non-goal:** IDE-specific schedulers as the canonical path (Cursor-only automations are not required).

## See also

- `docs/platform-support-documentation/README.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-135-agent-hub-compile-artifacts.md`
