# Research Impact Report: Custom Instructions vs Custom Agents vs Agent Skills

## Executive Judgment

This transcript is **high-signal for Second Brain's operating model** even though it describes GitHub Copilot. It validates the instructions/agents/skills separation Second Brain already uses under different names, and offers one experiment (path-scoped compile guidance). It is not a product pivot toward Copilot.

## Source

- Transcript: `raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt`
- Date: unknown
- Participants: unknown (Microsoft/Copilot tutorial voice)
- Processing limitations: Vendor feature names and paths not externally validated; mapped to Second Brain design docs only.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 3 |
| Experiment | 1 |
| Defer | 0 |
| Reject | 0 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-066 | adopt | Reinforces lane-labeled governance: schema always on, specialists on demand, recipes pulled in for verbs. |
| RC-2026-05-27-068 | adopt | Prevents context bloat and keeps multi-step publish/align flows in explicit prompts/skills. |
| RC-2026-05-27-069 | adopt | Tool/scope restrictions strengthen fail-closed platform and workspace review lanes. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-067 | experiment | Path rules could fork team standards per folder if not tied to authority tags and compile policy. |

## Claim Register Entries

- `RC-2026-05-27-066` through `RC-2026-05-27-069`

## Recommended Next Actions

### Immediate changes

- None to canonical docs in this pass.

### Experiments

- Path-scoped compile/query orientation tied to `config/second-brain.yml` project paths (RC-025).

### ADRs to draft

- None required; RC-024/026/027 are already_supported reinforcements.

### Claims to reject

- Any implicit claim that Copilot repo features replace Second Brain's `raw/` immutability or wiki ownership model.

### Claims requiring external validation

- Copilot-specific file layout and `/instructions` behavior (not scored as adopt targets).

## Trust Loop Summary

Copilot vendor mechanics marked unvalidated where cited. Adopt decisions grounded against `AGENTS.md` and existing prompt/skill layout (`validation_status: validated_against_design`). Fail-closed: no promotion of Copilot hosting as canonical storage.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-066–027 | see register | Approve/reject via implementation backlog per decision. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, `AGENTS.md`, or raw files were modified based on this transcript.
