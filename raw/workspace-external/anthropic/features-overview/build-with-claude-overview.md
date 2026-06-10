---
source_url: https://platform.claude.com/docs/en/build-with-claude/overview
vendor: anthropic
topic: features-overview
fetched_at: 2026-06-10T07:11:53Z
revalidate_after: 2026-09-08T07:11:53Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:anthropic
authority: standard
ingest_mode: defuddle
---

Claude's API surface is organized into five areas:

- **Model capabilities:** Control how Claude reasons and formats responses.
- **Tools:** Let Claude take actions on the web or in your environment.
- **Tool infrastructure:** Handles discovery and orchestration at scale.
- **Context management:** Keeps long-running sessions efficient.
- **Files and assets:** Manage the documents and data you provide to Claude.

If you're new, start with [model capabilities](#model-capabilities) and [tools](#tools). Return to the other sections when you're ready to optimize cost, latency, or scale.

For administration and governance, see the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api), the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api), and the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api).

## Feature availability

Features on the Claude Platform are assigned one of the following availability classifications per platform (shown in the Availability column of each following table). Not all features pass through every stage. A feature may enter at any classification and may skip stages.

| Classification | Description |
| --- | --- |
| **Beta** <sup>*</sup> | Preview features used for gathering feedback and iterating on a less mature use case. Availability may be limited, including through sign-up requirements or waitlists, and may not be publicly announced.      Features may change significantly or be discontinued based on feedback. Not guaranteed for ongoing production use. Breaking changes are possible with notice, and some platform-specific limitations may apply. Beta features on the Claude API and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) have a [beta header](https://platform.claude.com/docs/en/api/beta-headers). |
| **Generally available (GA)** | Feature is stable, fully supported, and recommended for production use. Should not have a beta header or other indicator that the feature is in a preview state. Covered by standard API [versioning](https://platform.claude.com/docs/en/api/versioning) guarantees. |
| **Deprecated** | Feature is still functional but no longer recommended. A migration path and removal timeline are provided. |
| **Retired** | Feature is no longer available. |

*<sup>*</sup> May carry a qualifier indicating narrower availability or added constraints (for example, "beta: research preview"). See the feature's page for details.*

**Platform labels:** Claude API (Anthropic first-party) · [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) (Anthropic-operated on AWS) · [Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock) (AWS-operated) · [Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai) (Google-operated) · [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) (Anthropic-operated on Azure)

## Model capabilities

Ways to steer Claude and Claude's direct outputs, including response format, reasoning depth, and input modalities.

You can discover which capabilities a model supports programmatically. The [Models API](https://platform.claude.com/docs/en/api/models/list) returns `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

| Feature | Description | Zero Data Retention (ZDR) | Availability |
| --- | --- | --- | --- |
| [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) | Up to 1M tokens for processing large documents, extensive code bases, and long conversations. | ZDR eligible | Claude API (GA)      Claude Platform on AWS (GA)      Bedrock (GA)      Vertex AI (GA)      Microsoft Foundry (Beta) |
| [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) | Let Claude dynamically decide when and how much to think. The only thinking mode on Claude Opus 4.8 and Claude Opus 4.7. Use the effort parameter to control thinking depth. | ZDR eligible | Claude API (GA)      Claude Platform on AWS (GA)      Bedrock (GA)      Vertex AI (GA)      Microsoft Foundry (Beta) |
| [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls cost 50% less than standard API calls. | Not ZDR eligible | Claude API (GA) |

## Tools

Built-in tools that Claude invokes through `tool_use`. Server-side tools are run by the platform; client-side tools are implemented and executed by you.

### Server-side tools

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) | Pair a faster executor model with a higher-intelligence advisor model that provides strategic guidance mid-generation for long-horizon agentic workloads. | ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta) |
| [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) | Run code in a sandboxed environment for advanced data analysis, calculations, and file processing. Free when used with web search or web fetch. | Not ZDR eligible | Claude API (GA)      Claude Platform on AWS (GA)      Microsoft Foundry (Beta) |
| [Web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) | Retrieve full content from specified web pages and PDF documents for in-depth analysis. | ZDR eligible\* | Claude API (GA)      Claude Platform on AWS (GA)      Microsoft Foundry (Beta) |
| [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) |

### Client-side tools

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Bash](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) | Execute bash commands and scripts to interact with the system shell and perform command-line operations. | ZDR eligible | Claude API (GA)      Claude Platform on AWS (GA)      Bedrock (GA)      Vertex AI (GA)      Microsoft Foundry (Beta) |
| [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. | ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta)      Bedrock (Beta)      Vertex AI (Beta)      Microsoft Foundry (Beta) |
| [Memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | ZDR eligible | Claude API (GA)      Claude Platform on AWS (GA) |

## Tool infrastructure

Infrastructure that supports discovering, orchestrating, and scaling tool use.

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context. | Not ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta)      Microsoft Foundry (Beta) |
| [Fine-grained tool streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. | ZDR eligible | Claude API (GA)      Claude Platform on AWS (GA)      Bedrock (GA)      Vertex AI (GA)      Microsoft Foundry (GA) |
| [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) | Connect to remote [MCP](https://platform.claude.com/docs/en/mcp) servers directly from the Messages API without a separate MCP client. | Not ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta) |

## Context management

Infrastructure for controlling and optimizing Claude's context window.

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) | Server-side context summarization for long-running conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation. Supported on Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. | ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta)      Bedrock (Beta)      Vertex AI (Beta)      Microsoft Foundry (Beta) |
| [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) | Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations. | ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta)      Bedrock (Beta)      Vertex AI (Beta)      Microsoft Foundry (Beta) |
| [Automatic prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) | Simplify prompt caching to a single API parameter. The system automatically caches the last cacheable block in your request, moving the cache point forward as conversations grow. |

## Files and assets

Manage files and assets for use with Claude.

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files) | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. | Not ZDR eligible | Claude API (Beta)      Claude Platform on AWS (Beta)      Microsoft Foundry (Beta) |

\* **Structured outputs:** Your prompts and Claude's outputs are not stored. Only JSON schemas are cached, for up to 24 hours since last use. **Web search and web fetch:** ZDR-eligible except when [dynamic filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#dynamic-filtering) is enabled. See [ZDR details](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility).

Was this page helpful?