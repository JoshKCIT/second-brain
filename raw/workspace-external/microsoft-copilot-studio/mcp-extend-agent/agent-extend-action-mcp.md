---
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
vendor: microsoft-copilot-studio
topic: mcp-extend-agent
fetched_at: 2026-06-10T07:02:49Z
revalidate_after: 2026-09-08T07:02:49Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:microsoft-copilot-studio
authority: standard
ingest_mode: defuddle
---

## Extend your agent with Model Context Protocol

You can extend your agent with tools by using Model Context Protocol (MCP).

## What is Model Context Protocol?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) helps you connect to existing knowledge servers and data sources directly within Copilot Studio. When you connect to an MCP server, you get access to:

- Resources: File-like data that an agent can read for more context, such as API responses or file contents
- Tools: Functions that a language model can call to perform an action
- Prompts: Predefined prompt templates to accomplish specific tasks

Note

Copilot Studio currently supports MCP tools and resources.

## How does MCP work?

Each tool or resource that a connected MCP server publishes is automatically available for use in Copilot Studio. The server provides the name, description, inputs, and outputs. When you update or remove tools and resources on the MCP server, Copilot Studio dynamically reflects these changes. This process ensures users always have the latest versions and removes obsolete tools and resources. A single MCP server can integrate and manage multiple tools and resources. Copilot Studio agents can access each tool.

When you connect to a non-Microsoft product, including an external MCP server, you're responsible for the tools and resources you access from within Copilot Studio.

Note

You must turn on [generative orchestration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions) to use MCP.

## How do you extend an agent by using MCP in Copilot Studio?

To integrate MCP in Copilot Studio:

1. Use the MCP onboarding wizard to [connect your agent to an existing MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent).
2. [Create an MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-create-new-server) if you don't already have an MCP server.
3. [Add MCP server tools and resources to your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-components-to-agent) so that your Copilot Studio agent can use them.
4. (Optional) [Publish your MCP connector](https://learn.microsoft.com/en-us/connectors/custom-connectors/submit-certification) to allow the connector to be used across tenants.

For more information on troubleshooting MCP integration, see [Troubleshooting Model Context Protocol (MCP) integration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-troubleshooting).