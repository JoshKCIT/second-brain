---
source_url: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
vendor: github
topic: custom-agents
fetched_at: 2026-06-10T07:13:56Z
revalidate_after: 2026-09-08T07:13:56Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:github
authority: standard
ingest_mode: defuddle
---

## About custom agents

Custom agents are specialized versions of the Copilot agent that you can tailor to your unique workflows, coding conventions, and use cases. They act like tailored teammates that follow your standards, use the right tools, and implement team-specific practices. You define these agents once instead of repeatedly providing the same instructions and context.

You define custom agents using Markdown files called agent profiles. These files specify prompts, tools, and MCP servers. This allows you to encode your conventions, frameworks, and desired outcomes directly into Copilot.

The agent profile defines the custom agent's behavior. When you assign the agent to a task or issue, it instantiates the custom agent.

## Agent profile format

Agent profiles are Markdown files with YAML frontmatter. In their simplest form, they include:

- **Name** (optional): A display name for the custom agent. If omitted, the agent's filename is used as its identifier and default display name.
- **Description**: Explains the agent's purpose and capabilities.
- **Prompt**: Custom instructions that define the agent's behavior and expertise.
- **Tools** (optional): Specific tools the agent can access. By default, agents can access all available tools, including built-in tools, and MCP server tools.

Agent profiles can also include MCP server configurations using the `mcp-servers` property.

### Example agent profile

This example is a basic agent profile with name, description, and prompt configured.

```
---
name: readme-creator
description: Agent specializing in creating and improving README files
---

You are a documentation specialist focused on README files. Your scope is limited to README files or other related documentation files only - do not modify or analyze code files.

Focus on the following instructions:
- Create and update README.md files with clear project descriptions
- Structure README sections logically: overview, installation, usage, contributing
- Write scannable content with proper headings and formatting
- Add appropriate badges, links, and navigation elements
- Use relative links (e.g., \`docs/CONTRIBUTING.md\`) instead of absolute URLs for files within the repository
- Make links descriptive and add alt text to images
```

## Where you can configure custom agents

You can define agent profiles at different levels:

- **Repository level**: Create `.github/agents/CUSTOM-AGENT-NAME.md` in your repository for project-specific agents.
- **Organization or enterprise level**: Create `/agents/CUSTOM-AGENT-NAME.md` in a `.github-private` repository for broader availability.

For more information, see [Preparing to use custom agents in your organization](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents) and [Preparing to use custom agents in your enterprise](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents).

## Where you can use custom agents

Once you create custom agents, they become available to:

- **Copilot cloud agent on GitHub.com**: The agents tab and panel, issue assignment, and pull requests
- **Copilot cloud agent in IDEs**: Visual Studio Code, JetBrains IDEs, Eclipse, and Xcode
- **GitHub Copilot CLI**

You can use agent profiles directly in Visual Studio Code, JetBrains IDEs, Eclipse, and Xcode. Some properties may function differently or be ignored between environments.

For more information on using custom agents in Visual Studio Code, see [Custom agents in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-agents).

## Next steps

To create your own custom agents, see:

- [Creating custom agents for Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents)
- [Creating and using custom agents for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [Copilot customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)