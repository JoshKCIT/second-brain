---
source_url: https://developers.openai.com/api/docs/guides/tools
vendor: openai
topic: tools
fetched_at: 2026-06-10T07:11:49Z
revalidate_after: 2026-09-08T07:11:49Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:openai
authority: standard
ingest_mode: defuddle
---

When generating model responses or building agents, you can extend capabilities using built‑in tools, function calling, tool search, and remote MCP servers. These enable the model to search the web, retrieve from your files, load deferred tool definitions at runtime, call your own functions, or access third‑party services. Only `gpt-5.4` and later models support `tool_search`.

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5.5",
    tools: [
        { type: "web_search" },
    ],
    input: "What was a positive news story from today?",
});

console.log(response.output_text);
```

## Available tools

Here’s an overview of the tools available in the OpenAI platform—select one of them for further guidance on usage.

[

Function calling

Call custom code to give the model access to additional data and capabilities.

](https://developers.openai.com/api/docs/guides/function-calling)[

Web search

Include data from the Internet in model response generation.

](https://developers.openai.com/api/docs/guides/tools-web-search)[

Remote MCP servers

Give the model access to new capabilities via Model Context Protocol (MCP) servers.

](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)[

Skills

Upload and reuse versioned skill bundles in hosted shell environments.

](https://developers.openai.com/api/docs/guides/tools-skills)[

Shell

Run shell commands in hosted containers or in your own local runtime.

](https://developers.openai.com/api/docs/guides/tools-shell)[

Computer use

Create agentic workflows that enable a model to control a computer interface.

](https://developers.openai.com/api/docs/guides/tools-computer-use)[

Image generation

Generate or edit images using GPT Image.

](https://developers.openai.com/api/docs/guides/tools-image-generation)[

File search

Search the contents of uploaded files for context when generating a response.

](https://developers.openai.com/api/docs/guides/tools-file-search)[

Tool search

Dynamically load relevant tools into the model’s context to optimize token usage.

](https://developers.openai.com/api/docs/guides/tools-tool-search)

## Usage in the API

When making a request to generate a [model response](https://developers.openai.com/api/docs/api-reference/responses/create), you usually enable tool access by specifying configurations in the `tools` parameter. Each tool has its own unique configuration requirements—see the [Available tools](#available-tools) section for detailed instructions.

Based on the provided [prompt](https://developers.openai.com/api/docs/guides/text), the model automatically decides whether to use a configured tool. For instance, if your prompt requests information beyond the model’s training cutoff date and web search is enabled, the model will typically invoke the web search tool to retrieve relevant, up-to-date information.

Some advanced workflows can also load more tool definitions during the interaction. For example, [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search) can defer function definitions until the model decides they’re needed.

You can explicitly control or guide this behavior by setting the `tool_choice` parameter [in the API request](https://developers.openai.com/api/docs/api-reference/responses/create).

## Usage in the Agents SDK

In the Agents SDK, the tool semantics stay the same, but the wiring moves into the agent definition and workflow design rather than a single Responses API request.

- Attach hosted tools, function tools, or hosted MCP tools directly on the agent when one specialist should call them itself.
- Expose a specialist as a tool when a manager should stay in control of the user-facing reply.
- Keep shell, apply patch, and computer-use harnesses in your runtime even when the SDK models the tool decision.

```typescript
import { tool } from "@openai/agents";
import { z } from "zod";

const getWeatherTool = tool({
  name: "get_weather",
  description: "Get the weather for a given city.",
  parameters: z.object({ city: z.string() }),
  async execute({ city }) {
    return \`The weather in ${city} is sunny.\`;
  },
});
```

```typescript
import { Agent } from "@openai/agents";

const summarizer = new Agent({
  name: "Summarizer",
  instructions: "Generate a concise summary of the supplied text.",
});

const mainAgent = new Agent({
  name: "Research assistant",
  tools: [
    summarizer.asTool({
      toolName: "summarize_text",
      toolDescription: "Generate a concise summary of the supplied text.",
    }),
  ],
});
```

Use [Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents) when you are shaping a single specialist, [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) when tools affect ownership, [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) when tools affect approvals, and [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability#mcp) when the capability comes from MCP.