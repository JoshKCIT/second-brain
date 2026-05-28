# Platform Transcript Register

Operational index of product-intelligence sources under `raw/platform-transcripts/`. This file is the queue board: what is imported, what is ready for `/platform-research-review`, and what is already reviewed.

Sync after import or review:

```bash
python scripts/sync-transcript-register.py --root .
```

## Status legend

| Status | Meaning |
|--------|---------|
| `queued` | Present in `raw/platform-transcripts/`; not yet reviewed |
| `partial` | Review started — claims analysis or impact report missing |
| `reviewed` | Claims analysis and impact report both exist |
| `skipped` | User marked intentionally not reviewed (duplicate, noise, off-scope) |

## Summary

| Slug | Status | Source | Claims | Impact |
|------|--------|--------|--------|--------|
| 5-skills-ai-operating-system-1-percent-guide | `reviewed` | `raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt` | 5-skills-ai-operating-system-1-percent-guide-claims.md | 5-skills-ai-operating-system-1-percent-guide-impact-report.md |
| analog-vs-ai-second-brain | `reviewed` | `raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt` | analog-vs-ai-second-brain-claims.md | analog-vs-ai-second-brain-impact-report.md |
| karpathy-vibe-coding-agentic-engineering | `reviewed` | `raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt` | karpathy-vibe-coding-agentic-engineering-claims.md | karpathy-vibe-coding-agentic-engineering-impact-report.md |
| build-claude-knowledge-base-self-improves | `reviewed` | `raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt` | build-claude-knowledge-base-self-improves-claims.md | build-claude-knowledge-base-self-improves-impact-report.md |
| build-ai-second-brain-knowledge-base-step-by-step | `reviewed` | `raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt` | build-ai-second-brain-knowledge-base-step-by-step-claims.md | build-ai-second-brain-knowledge-base-step-by-step-impact-report.md |
| second-brain-singapore-keynote | `reviewed` | `raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt` | second-brain-singapore-keynote-claims.md | second-brain-singapore-keynote-impact-report.md |
| claude-code-obsidian-second-brain-learns | `reviewed` | `raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt` | claude-code-obsidian-second-brain-learns-claims.md | claude-code-obsidian-second-brain-learns-impact-report.md |
| claude-code-can-be-your-second-brain | `reviewed` | `raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt` | claude-code-can-be-your-second-brain-claims.md | claude-code-can-be-your-second-brain-impact-report.md |
| custom-instructions-agents-skills | `reviewed` | `raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt` | custom-instructions-agents-skills-claims.md | custom-instructions-agents-skills-impact-report.md |
| gitkb-distributed-knowledge-graph-texas-ready-ai | `reviewed` | `raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt` | gitkb-distributed-knowledge-graph-texas-ready-ai-claims.md | gitkb-distributed-knowledge-graph-texas-ready-ai-impact-report.md |
| graphify-instant-knowledge-graph | `reviewed` | `raw/platform-transcripts/Graphify_-_Instant_Knowledge_Graph_for_Claude_Code_Antigravity_FREE.txt` | graphify-instant-knowledge-graph-claims.md | graphify-instant-knowledge-graph-impact-report.md |
| how-i-organise-my-life-using-notion---in-the-ai-era | `reviewed` | `raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt` | how-i-organise-my-life-using-notion---in-the-ai-era-claims.md | how-i-organise-my-life-using-notion---in-the-ai-era-impact-report.md |
| how-did-i-build-second-brain-with-ai | `reviewed` | `raw/platform-transcripts/How_did_I_build_a_second_brain_with_AI.txt` | how-did-i-build-second-brain-with-ai-claims.md | how-did-i-build-second-brain-with-ai-impact-report.md |
| human-brilliance-rag-second-brains-ep1 | `reviewed` | `raw/platform-transcripts/Human_Brilliance_Augmented_-_Mastering_Medical_Information_Overload_with_RAG_Second_Brains_-_Ep._1.txt` | human-brilliance-rag-second-brains-ep1-claims.md | human-brilliance-rag-second-brains-ep1-impact-report.md |
| i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe | `reviewed` | `raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt` | i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe-claims.md | i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe-impact-report.md |
| is-your-ai-slop-or-real-second-brain | `reviewed` | `raw/platform-transcripts/Is_Your_AI_Just_Slop_Or_a_Real_Second_Brain.txt` | is-your-ai-slop-or-real-second-brain-claims.md | is-your-ai-slop-or-real-second-brain-impact-report.md |
| mastering-ai-vscode-agent-customizations | `reviewed` | `raw/platform-transcripts/Mastering_AI_with_VS_Code_s_New_Agent_Customizations.txt` | mastering-ai-vscode-agent-customizations-claims.md | mastering-ai-vscode-agent-customizations-impact-report.md |
| my-simple-claude-cowork-system-for-normal-people | `reviewed` | `raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt` | my-simple-claude-cowork-system-for-normal-people-claims.md | my-simple-claude-cowork-system-for-normal-people-impact-report.md |
| opencode-graphify-stop-wasting-tokens | `reviewed` | `raw/platform-transcripts/OpenCode_+_Graphify_-_Stop_Wasting_Tokens_in_Opencode_Every_Developer_Use_this.txt` | opencode-graphify-stop-wasting-tokens-claims.md | opencode-graphify-stop-wasting-tokens-impact-report.md |
| pinecone-knowledge-layer-demoted-vectors | `reviewed` | `raw/platform-transcripts/Pinecone_Just_Demoted_Vector_Search._Here_s_the_Knowledge_Layer.txt` | pinecone-knowledge-layer-demoted-vectors-claims.md | pinecone-knowledge-layer-demoted-vectors-impact-report.md |
| remio-vs-alter-ai-review | `reviewed` | `raw/platform-transcripts/Remio.ai_Review_-_The_Ultimate_AI_Second_Brain_That_is_So_Much_More_vs._Alter_AI.txt` | remio-vs-alter-ai-review-claims.md | remio-vs-alter-ai-review-impact-report.md |
| stanford-meta-harness | `reviewed` | `raw/platform-transcripts/Researcher_at_Stanford_released_a_new_paper_for_an_automated_ai_agent_harmess_ai_tech_fyp.txt` | stanford-meta-harness-claims.md | stanford-meta-harness-impact-report.md |
| robot-girlfriends-recursive-ai-agents-ai-news | `reviewed` | `raw/platform-transcripts/Robot_girlfriends_recursive_AI_agents_full_AI_research_Happy_Horse_-_AI_NEWS.txt` | robot-girlfriends-recursive-ai-agents-ai-news-claims.md | robot-girlfriends-recursive-ai-agents-ai-news-impact-report.md |
| ai-native-shift-george-thomas | `reviewed` | `raw/platform-transcripts/The_AI-Native_Shift_-_Second_Brain_for_AI_with_George_B._Thomas.txt` | ai-native-shift-george-thomas-claims.md | ai-native-shift-george-thomas-impact-report.md |
| pi-coding-agent-competitor | `reviewed` | `raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt` | pi-coding-agent-competitor-claims.md | pi-coding-agent-competitor-impact-report.md |
| why-2026-build-second-brain | `reviewed` | `raw/platform-transcripts/Why_2026_Is_the_Year_to_Build_a_Second_Brain_And_Why_You_NEED_One.txt` | why-2026-build-second-brain-claims.md | why-2026-build-second-brain-impact-report.md |
| openclaw-hermes-distractions | `reviewed` | `raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt` | openclaw-hermes-distractions-claims.md | openclaw-hermes-distractions-impact-report.md |
| git-workflow-wrong | `reviewed` | `raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt` | git-workflow-wrong-claims.md | git-workflow-wrong-impact-report.md |
| second-brain-no-vector-database | `reviewed` | `raw/platform-transcripts/second-brain-no-vector-database.txt` | second-brain-no-vector-database-claims.md | second-brain-no-vector-database-impact-report.md |
| second-brain-self-learning-ideas | `reviewed` | `raw/platform-transcripts/second-brain-self-learning-ideas.txt` | second-brain-self-learning-ideas-claims.md | second-brain-self-learning-ideas-impact-report.md |

_Last synced: 2026-05-27. 30 total — 0 queued, 0 partial, 30 reviewed, 0 skipped._

## Records

```yaml
slug: 5-skills-ai-operating-system-1-percent-guide
status: reviewed
source: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
title: "5-skills-to-build-an-ai-operating-system-like-the-1%-full-guide"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/5-skills-ai-operating-system-1-percent-guide-claims.md
impact_report: reports/platform-research-review/5-skills-ai-operating-system-1-percent-guide-impact-report.md
notes: ""
```

```yaml
slug: analog-vs-ai-second-brain
status: reviewed
source: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
title: "analog-vs.-ai---which-is-better-for-your-second-brain"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/analog-vs-ai-second-brain-claims.md
impact_report: reports/platform-research-review/analog-vs-ai-second-brain-impact-report.md
notes: ""
```

```yaml
slug: karpathy-vibe-coding-agentic-engineering
status: reviewed
source: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
title: "andrej-karpathy---from-vibe-coding-to-agentic-engineering"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/karpathy-vibe-coding-agentic-engineering-claims.md
impact_report: reports/platform-research-review/karpathy-vibe-coding-agentic-engineering-impact-report.md
notes: ""
```

```yaml
slug: build-claude-knowledge-base-self-improves
status: reviewed
source: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
title: "build-a-claude-knowledge-base-that-self-improves"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/build-claude-knowledge-base-self-improves-claims.md
impact_report: reports/platform-research-review/build-claude-knowledge-base-self-improves-impact-report.md
notes: ""
```

```yaml
slug: build-ai-second-brain-knowledge-base-step-by-step
status: reviewed
source: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
title: "build-an-ai-second-brain-knowledge-base-step-by-step"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/build-ai-second-brain-knowledge-base-step-by-step-claims.md
impact_report: reports/platform-research-review/build-ai-second-brain-knowledge-base-step-by-step-impact-report.md
notes: ""
```

```yaml
slug: second-brain-singapore-keynote
status: reviewed
source: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
title: "building-a-second-brain---opportunities-risks-and-implications-for-ai-adoption-i"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/second-brain-singapore-keynote-claims.md
impact_report: reports/platform-research-review/second-brain-singapore-keynote-impact-report.md
notes: ""
```

```yaml
slug: claude-code-obsidian-second-brain-learns
status: reviewed
source: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
title: "claude-code-+-obsidian---build-a-second-brain-that-actually-learns"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/claude-code-obsidian-second-brain-learns-claims.md
impact_report: reports/platform-research-review/claude-code-obsidian-second-brain-learns-impact-report.md
notes: ""
```

```yaml
slug: claude-code-can-be-your-second-brain
status: reviewed
source: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
title: "claude-code-can-be-your-second-brain"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/claude-code-can-be-your-second-brain-claims.md
impact_report: reports/platform-research-review/claude-code-can-be-your-second-brain-impact-report.md
notes: ""
```

```yaml
slug: custom-instructions-agents-skills
status: reviewed
source: raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt
title: "custom-instructions-vs-custom-agents-vs-agent-skills-explained"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/custom-instructions-agents-skills-claims.md
impact_report: reports/platform-research-review/custom-instructions-agents-skills-impact-report.md
notes: ""
```

```yaml
slug: gitkb-distributed-knowledge-graph-texas-ready-ai
status: reviewed
source: raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt
title: "GitKB Distributed Knowledge Graph + Texas Responsible AI"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/gitkb-distributed-knowledge-graph-texas-ready-ai-claims.md
impact_report: reports/platform-research-review/gitkb-distributed-knowledge-graph-texas-ready-ai-impact-report.md
notes: ""
```

```yaml
slug: graphify-instant-knowledge-graph
status: reviewed
source: raw/platform-transcripts/Graphify_-_Instant_Knowledge_Graph_for_Claude_Code_Antigravity_FREE.txt
title: "Graphify Instant Knowledge Graph"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/graphify-instant-knowledge-graph-claims.md
impact_report: reports/platform-research-review/graphify-instant-knowledge-graph-impact-report.md
notes: ""
```

```yaml
slug: how-i-organise-my-life-using-notion---in-the-ai-era
status: reviewed
source: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
title: "how-i-organise-my-life-using-notion---in-the-ai-era"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/how-i-organise-my-life-using-notion---in-the-ai-era-claims.md
impact_report: reports/platform-research-review/how-i-organise-my-life-using-notion---in-the-ai-era-impact-report.md
notes: ""
```

```yaml
slug: how-did-i-build-second-brain-with-ai
status: reviewed
source: raw/platform-transcripts/How_did_I_build_a_second_brain_with_AI.txt
title: "how-did-i-build-a-second-brain-with-ai"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/how-did-i-build-second-brain-with-ai-claims.md
impact_report: reports/platform-research-review/how-did-i-build-second-brain-with-ai-impact-report.md
notes: ""
```

```yaml
slug: human-brilliance-rag-second-brains-ep1
status: reviewed
source: raw/platform-transcripts/Human_Brilliance_Augmented_-_Mastering_Medical_Information_Overload_with_RAG_Second_Brains_-_Ep._1.txt
title: "human-brilliance-augmented---mastering-medical-information-overload-with-rag-sec"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/human-brilliance-rag-second-brains-ep1-claims.md
impact_report: reports/platform-research-review/human-brilliance-rag-second-brains-ep1-impact-report.md
notes: ""
```

```yaml
slug: i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe
status: reviewed
source: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
title: "i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe-claims.md
impact_report: reports/platform-research-review/i-built-a-second-brain-with-codex-in-15-minutes-matt-wolfe-impact-report.md
notes: ""
```

```yaml
slug: is-your-ai-slop-or-real-second-brain
status: reviewed
source: raw/platform-transcripts/Is_Your_AI_Just_Slop_Or_a_Real_Second_Brain.txt
title: "is-your-ai-just-slop-or-a-real-second-brain"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/is-your-ai-slop-or-real-second-brain-claims.md
impact_report: reports/platform-research-review/is-your-ai-slop-or-real-second-brain-impact-report.md
notes: ""
```

```yaml
slug: mastering-ai-vscode-agent-customizations
status: reviewed
source: raw/platform-transcripts/Mastering_AI_with_VS_Code_s_New_Agent_Customizations.txt
title: "mastering-ai-with-vs-code-s-new-agent-customizations"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/mastering-ai-vscode-agent-customizations-claims.md
impact_report: reports/platform-research-review/mastering-ai-vscode-agent-customizations-impact-report.md
notes: ""
```

```yaml
slug: my-simple-claude-cowork-system-for-normal-people
status: reviewed
source: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
title: "my-simple-claude-cowork-system-for-normal-people"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/my-simple-claude-cowork-system-for-normal-people-claims.md
impact_report: reports/platform-research-review/my-simple-claude-cowork-system-for-normal-people-impact-report.md
notes: ""
```

```yaml
slug: opencode-graphify-stop-wasting-tokens
status: reviewed
source: raw/platform-transcripts/OpenCode_+_Graphify_-_Stop_Wasting_Tokens_in_Opencode_Every_Developer_Use_this.txt
title: "OpenCode + Graphify"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/opencode-graphify-stop-wasting-tokens-claims.md
impact_report: reports/platform-research-review/opencode-graphify-stop-wasting-tokens-impact-report.md
notes: ""
```

```yaml
slug: pinecone-knowledge-layer-demoted-vectors
status: reviewed
source: raw/platform-transcripts/Pinecone_Just_Demoted_Vector_Search._Here_s_the_Knowledge_Layer.txt
title: "pinecone-just-demoted-vector-search.-here-s-the-knowledge-layer"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/pinecone-knowledge-layer-demoted-vectors-claims.md
impact_report: reports/platform-research-review/pinecone-knowledge-layer-demoted-vectors-impact-report.md
notes: ""
```

```yaml
slug: remio-vs-alter-ai-review
status: reviewed
source: raw/platform-transcripts/Remio.ai_Review_-_The_Ultimate_AI_Second_Brain_That_is_So_Much_More_vs._Alter_AI.txt
title: "remio.ai-review---the-ultimate-ai-second-brain-that-is-so-much-more-vs.-alter-ai"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/remio-vs-alter-ai-review-claims.md
impact_report: reports/platform-research-review/remio-vs-alter-ai-review-impact-report.md
notes: ""
```

```yaml
slug: stanford-meta-harness
status: reviewed
source: raw/platform-transcripts/Researcher_at_Stanford_released_a_new_paper_for_an_automated_ai_agent_harmess_ai_tech_fyp.txt
title: "Stanford Meta Harness"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/stanford-meta-harness-claims.md
impact_report: reports/platform-research-review/stanford-meta-harness-impact-report.md
notes: ""
```

```yaml
slug: robot-girlfriends-recursive-ai-agents-ai-news
status: reviewed
source: raw/platform-transcripts/Robot_girlfriends_recursive_AI_agents_full_AI_research_Happy_Horse_-_AI_NEWS.txt
title: "Robot Girlfriends Recursive AI Agents AI News"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/robot-girlfriends-recursive-ai-agents-ai-news-claims.md
impact_report: reports/platform-research-review/robot-girlfriends-recursive-ai-agents-ai-news-impact-report.md
notes: ""
```

```yaml
slug: ai-native-shift-george-thomas
status: reviewed
source: raw/platform-transcripts/The_AI-Native_Shift_-_Second_Brain_for_AI_with_George_B._Thomas.txt
title: "the-ai-native-shift---second-brain-for-ai-with-george-b.-thomas"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/ai-native-shift-george-thomas-claims.md
impact_report: reports/platform-research-review/ai-native-shift-george-thomas-impact-report.md
notes: ""
```

```yaml
slug: pi-coding-agent-competitor
status: reviewed
source: raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt
title: "the-pi-coding-agent---the-only-real-claude-code-competitor"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/pi-coding-agent-competitor-claims.md
impact_report: reports/platform-research-review/pi-coding-agent-competitor-impact-report.md
notes: ""
```

```yaml
slug: why-2026-build-second-brain
status: reviewed
source: raw/platform-transcripts/Why_2026_Is_the_Year_to_Build_a_Second_Brain_And_Why_You_NEED_One.txt
title: "Why 2026 Is the Year to Build a Second Brain"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/why-2026-build-second-brain-claims.md
impact_report: reports/platform-research-review/why-2026-build-second-brain-impact-report.md
notes: ""
```

```yaml
slug: openclaw-hermes-distractions
status: reviewed
source: raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt
title: "why-openclaw-and-hermes-are-distractions-do-this-instead-to-become-ai-fluent"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/openclaw-hermes-distractions-claims.md
impact_report: reports/platform-research-review/openclaw-hermes-distractions-impact-report.md
notes: ""
```

```yaml
slug: git-workflow-wrong
status: reviewed
source: raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt
title: "you-ve-been-using-git-wrong"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/git-workflow-wrong-claims.md
impact_report: reports/platform-research-review/git-workflow-wrong-impact-report.md
notes: ""
```

```yaml
slug: second-brain-no-vector-database
status: reviewed
source: raw/platform-transcripts/second-brain-no-vector-database.txt
title: "second-brain-no-vector-database"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/second-brain-no-vector-database-claims.md
impact_report: reports/platform-research-review/second-brain-no-vector-database-impact-report.md
notes: ""
```

```yaml
slug: second-brain-self-learning-ideas
status: reviewed
source: raw/platform-transcripts/second-brain-self-learning-ideas.txt
title: "second-brain-self-learning-ideas"
imported: 2026-05-27
reviewed: 2026-05-27
claims_analysis: wiki/platform-research/transcript-analyses/second-brain-self-learning-ideas-claims.md
impact_report: reports/platform-research-review/second-brain-self-learning-ideas-impact-report.md
notes: ""
```
