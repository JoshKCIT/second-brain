# Claims Analysis: You've Been Using Git Wrong

## Source

- Transcript: `raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt`
- Slug: `git-workflow-wrong`
- Processing limitations: Git/GitHub collaboration theory; not documentation-compiler specific.

## Executive Judgment

Limited direct feature yield. One **experiment** candidate: bind decision/discussion context to artifact revisions in-repo (`wiki/log.md`, project stages) so publish-time closure has traceable rationale. Reject mandating kernel-style patch workflow for Second Brain markdown. **Monitor** enterprise GitHub vs distributed-git ownership tradeoff for future team rollout.

## Discussion Blocks

| Block | Timestamp | Topic |
|---|---|---|
| 1 | 00:00:00–00:02:00 | Git vs GitHub misalignment; discussions outside VCS |
| 2 | 00:02:00–00:05:30 | Self-hosted git + gitweb; distributed remotes |
| 3 | 00:05:30–00:08:30 | Patch workflow vs branches/PRs; local review advantages |
| 4 | 00:08:30–00:11:30 | CI limits; centralized maintainers vs GitHub distributed ownership |

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-079 | `workflow_proposal` | experiment | Link review/decision context to artifact revisions in-repo (log + stage dirs) for publish traceability. |
| RC-2026-05-27-080 | `workflow_proposal` | reject | Second Brain collaboration should abandon GitHub PR branches for email/patch-only kernel workflow. |
| RC-2026-05-27-081 | `principle_claim` | monitor | GitHub centralizes code while distributing merge ownership; relevant for future multi-user vault, not v1. |

## Grounding Notes

- **RC-037:** `wiki/log.md` append-only audit exists; PR/Slack discussion split is problem_evidence — partially_supported.
- **RC-038:** Second Brain artifacts are Markdown in git; patch workflow adds friction without closure gain — contradicted for v1.
- **RC-039:** v1 single-user local constraint (RC-005) — defer/monitor for v2.

## Safer Variants

| Rejected-as-stated | Safer variant |
|---|---|
| Send patches not PRs | Keep GitHub/git for repo; store **decision records** and align reports under `reports/` + `wiki/log.md` |
| Move all discussion into git | Append structured decision snippets to `wiki/log.md` and platform ADRs when user approves |

## Recommended Next Actions

- Experiment RC-037: template "decision snippet" append format for publish/align events.
- Do not change ingest/compile for patch workflow.
