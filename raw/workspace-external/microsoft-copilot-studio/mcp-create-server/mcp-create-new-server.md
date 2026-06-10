---
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-create-new-server
vendor: microsoft-copilot-studio
topic: mcp-create-server
fetched_at: 2026-06-10T07:02:50Z
revalidate_after: 2026-09-08T07:02:50Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:microsoft-copilot-studio
authority: standard
ingest_mode: defuddle
---

## Create a new Model Context Protocol (MCP) server

You can use [MCP software development kits (SDKs)](https://github.com/modelcontextprotocol) to set up an MCP server in one of the supported languages.

If you already have an MCP server set up, see [Add an existing Model Context Protocol (MCP) server to your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent) for information on how to add the server to your agent.

## Authentication support

When you create an MCP server, you can choose to implement authentication or not. If you choose to implement authentication, you can use one of the following methods:

- **API key**: A simple way to secure your server by making your application include a key with requests.
- **OAuth 2.0**: A more robust authentication method that lets individual users grant access to their data without sharing their credentials with the agent.

Choose the method that best fits your needs and follow the implementation guidelines for that method.

You must register your application with an identity provider to obtain the necessary client credentials. The credentials are either an application key for API key authentication or a client ID and client secret for OAuth 2.0 authentication.

You must provide the authentication credentials from your identity provider when you add the MCP server to your agent in Copilot Studio. To learn more, see [Configure authentication with your MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent#configure-authentication-with-your-mcp-server).

If you use OAuth 2.0 authentication, you receive a callback URL from Copilot Studio after you add the MCP server. You need to update your app registration with your identity provider to add this URL. This URL is where the identity provider responds once the user signs in and grants permissions to your agent.