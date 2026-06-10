---
source_url: https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions
vendor: github
topic: mcp-overview
fetched_at: 2026-06-10T07:13:57Z
revalidate_after: 2026-09-08T07:13:57Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:github
authority: standard
ingest_mode: defuddle
---

## Overview of Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard that defines how applications share context with large language models (LLMs). MCP provides a standardized way to connect AI models to different data sources and tools, enabling them to work together more effectively.

You can use MCP to extend the capabilities of GitHub Copilot by integrating it with a wide range of existing tools and services. MCP works across all major Copilot surfaces—whether you're working in an IDE, using GitHub Copilot CLI, working in the GitHub Copilot app, or delegating tasks to an agent on GitHub.com. You can also use MCP to create new tools and services that work with Copilot, allowing you to customize and enhance your experience.

For more information on MCP, see [the official MCP documentation](https://modelcontextprotocol.io/introduction). For a curated list of MCP servers from partners and the community, see the [GitHub MCP Registry](https://github.com/mcp).

To learn how to configure and use MCP servers, see:

- [Extending GitHub Copilot Chat with Model Context Protocol (MCP) servers](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) for Copilot Chat in your IDE
- [Adding MCP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) for Copilot CLI
- [Configure MCP servers for your repository](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers) for repository MCP configuration on GitHub.com
- [Customizing the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app) for information on MCP server support in the GitHub Copilot app Enterprises and organizations can choose to enable or disable use of MCP for members of their organization or enterprise with the **MCP servers in Copilot** policy. The policy is disabled by default. See [Managing policies and features for GitHub Copilot in your enterprise](https://docs.github.com/en/copilot/how-tos/administer/enterprises/managing-policies-and-features-for-copilot-in-your-enterprise) and [Managing policies and features for GitHub Copilot in your organization](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies). The MCP policy **only** applies to users who have a Copilot Business or Copilot Enterprise subscription from an organization or enterprise that configures the policy. Copilot Free, Copilot Pro, Copilot Pro+, or Copilot Max **do not** have their MCP access governed by this policy.

## Availability

MCP is supported across the following clients:

- **IDEs**: There is broad support for local MCP servers in clients such as Visual Studio Code, JetBrains IDEs, Xcode, and others. Support for remote MCP servers is growing, with editors like Visual Studio Code, Visual Studio, JetBrains IDEs, Xcode, Eclipse, Cursor, and Windsurf providing this functionality with OAuth or PAT. To find out if your preferred editor supports remote MCP servers, check the documentation for your specific editor.
- **Copilot CLI**: GitHub Copilot CLI supports both local and remote MCP servers. The GitHub MCP server is built in and available without additional configuration.
- **GitHub Copilot app**: The GitHub Copilot app (in technical preview) supports MCP servers configured in your repository or Copilot CLI and lets you add additional MCP servers in app settings.
- **Copilot cloud agent and Copilot code review**: GitHub.com supports MCP servers configured at the repository level. The configuration applies to both Copilot cloud agent and Copilot code review. The GitHub MCP server and Playwright MCP server are configured by default.

## About the GitHub MCP server

The GitHub MCP server is a Model Context Protocol (MCP) server provided and maintained by GitHub.

GitHub MCP server can be used to:

- Automate and streamline code-related tasks.
- Connect third-party tools (like Cursor, Windsurf, or future integrations) to leverage GitHub’s context and AI capabilities.
- Enable cloud-based workflows that work from any device, without local setup.
- Invoke GitHub tools, such as Copilot cloud agent (requires GitHub Copilot subscription) and code scanning (requires GitHub Advanced Security subscription), to assist with code generation and security analysis.

To learn how to set up and use the GitHub MCP server, see [Using the GitHub MCP Server in your IDE](https://docs.github.com/en/copilot/how-tos/context/model-context-protocol/using-the-github-mcp-server).

To find out whether your editor supports the GitHub MCP server, and which connection and authentication methods are available, see [Support by host application](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/README.md#support-by-host-application) in the `github/github-mcp-server` repository.

### Remote access

You can access the GitHub MCP server remotely through Copilot Chat in Visual Studio Code without any local setup. The remote server has access to additional toolsets only available in the remote GitHub MCP server. For a list of such tools, see [Additional toolsets](https://github.com/github/github-mcp-server?tab=readme-ov-file#additional-toolsets-in-remote-github-mcp-server) in the `github/github-mcp-server` repository.

The GitHub MCP server can also run locally in any MCP-compatible editor, if necessary.

### Toolset customization

The GitHub MCP server supports enabling or disabling specific groups of functionalities via toolsets. Toolsets allow you to control which GitHub API capabilities are available to your AI tools.

Enabling only the toolsets you need improves your AI assistant's performance and security. Fewer tools means better tool selection accuracy and fewer errors. Disabling unused toolsets also frees up tokens in the AI's context window.

Toolsets do not only include tools, but also relevant MCP resources and prompts where applicable.

To learn how to configure toolsets for the GitHub MCP server, see [Configuring toolsets for the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/context/use-mcp/configure-toolsets).

### Security

For all public repositories, and private repositories covered by GitHub Advanced Security, interactions with the GitHub MCP server are secured by push protection, which blocks secrets in AI-generated responses and prevents them from being included in actions taken on your behalf. You can also proactively scan your code for exposed secrets from within your AI coding agent. For more information, see [Scanning for secrets with the GitHub MCP server](https://docs.github.com/en/code-security/how-tos/use-ghas-with-ai-coding-agents/scan-for-secrets-with-github-mcp-server).

## About the GitHub MCP Registry

The GitHub MCP Registry is a curated list of MCP servers from partners and the community. You can use the registry to discover new MCP servers and find ones that meet your specific needs. See [the GitHub MCP Registry](https://github.com/mcp).

## Next steps

- [Extending GitHub Copilot Chat with Model Context Protocol (MCP) servers](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) —Add MCP servers to Copilot Chat in your IDE
- [Adding MCP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) —Add MCP servers to Copilot CLI
- [Configure MCP servers for your repository](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers) —Configure repository MCP servers for Copilot cloud agent and Copilot code review
- [Setting up the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server) —Set up the GitHub MCP server
- [Using the GitHub MCP Server in your IDE](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server) —Use the GitHub MCP server
- [Enhancing GitHub Copilot agent mode with MCP](https://docs.github.com/en/copilot/tutorials/enhancing-copilot-agent-mode-with-mcp)
- [Copilot customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)