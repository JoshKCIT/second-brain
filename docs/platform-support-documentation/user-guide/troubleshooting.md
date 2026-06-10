---
title: "Troubleshooting"
audience: user
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "README.md"
  - "scripts/verify-setup.py"
  - "scripts/README.md"
---

# Troubleshooting

Operational fixes for common Second Brain problems. For install detail see [getting-started.md](getting-started.md). For governance confusion see [concepts-for-operators.md](../operator-guide/concepts-for-operators.md).

## Common gotchas

| Problem | What to try |
|---------|-------------|
| AI ignores `/commands` | Open matching file in `.github/prompts/` manually; see [using-your-ide.md](../operator-guide/using-your-ide.md) |
| Empty wiki after ingest | Ingest only writes raw — run `/workspace-compile` and approve y/n |
| Agent wrote wiki without asking | Stop session; revert; remind agent of RC-146; file issue if prompt regression |
| Broken wikilinks in Obsidian | Run `/workspace-lint`; fix paths or recompile |
| Cross-project dependency error | Finish, archive, or restate dependent project per closure rule |
| Quarantine folder growing | Review `quarantine/{date}/` payloads — macro conversion failures |

## Auth issues

| Problem | What to try |
|---------|-------------|
| Atlassian auth fails on verify-setup | Refresh API token; remove trailing slash from `ATLASSIAN_SITE_URL` |
| SSO / Guard blocks token | Switch to OAuth fields in `.env` |
| IP allowlist 403 | Contact Atlassian admin to allowlist your IP |
| Permission denied on page | User lost access after ingest — cached raw remains; refetch when access restored |
| Rate limit 429 on large ingest | Ingest in smaller batches; agent should backoff |

## Defuddle issues

| Problem | What to try |
|---------|-------------|
| `defuddle` not found | `npm install -g defuddle`; verify `defuddle --version` |
| Vendor fetch returns empty | Site may need JavaScript — try `defuddle parse {URL} --md` directly |
| Stale vendor doc cited | `/workspace-revalidate-vendor-docs` or refetch via ingest-vendor-doc |
| Wrong vendor domain on claim | Run align-vendor-truth; cite `raw/workspace-external/{vendor}/` |

## Lint remediation

| Problem | What to try |
|---------|-------------|
| workspace-lint many orphans | Compile orphaned raw or archive unused articles |
| Sparse articles warning | Expand concept articles or merge duplicates |
| Stale vendor docs | Refetch past TTL (90-day default) |
| Body wikilinks at review | Finalize step should move links to See Also |
| align-cite violations | Fix citation path or restate claim with correct source |
| Support doc lint fails | Run `python scripts/lint-platform-support-docs.py --root . --strict`; fix broken links or missing sections |
| Copilot agent mode disabled | Enable agent mode in VS Code settings; update Copilot extension |
| Project stage stuck at awaiting_ceo_review | Read artifact; say proceed or request revisions — check `meta.yml` stage_gate |
| OAuth token expired mid-ingest | Refresh `.env`; resume ingest in smaller batch |

## Recovery playbook

When unsure where to restart:

1. Run `python scripts/verify-setup.py` — fix environment first
2. Read `wiki/log.md` — last successful operation timestamps
3. Check `meta.yml` for project stage if chain stalled
4. Run `/workspace-lint` — structural issues often explain broken links
5. Consult [everyday-workflows.md](everyday-workflows.md) for verb routing

If problems persist after recovery playbook, capture the last agent prompt file used and open a troubleshooting session with `/workspace-query` against `wiki/workspace-qa/` if prior answers exist.

## See Also

- [getting-started.md](getting-started.md)
- [workflow-compile-and-query.md](workflow-compile-and-query.md)
- [scripts/README.md](../../../scripts/README.md)

## Sources consulted

- README.md, verify-setup.py, scripts/README.md
