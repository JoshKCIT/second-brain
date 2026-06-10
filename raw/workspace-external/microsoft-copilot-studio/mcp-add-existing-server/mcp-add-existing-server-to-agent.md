---
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
vendor: microsoft-copilot-studio
topic: mcp-add-existing-server
fetched_at: 2026-06-10T07:02:50Z
revalidate_after: 2026-09-08T07:02:50Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:microsoft-copilot-studio
authority: standard
ingest_mode: defuddle
---

## Connect your agent to an existing Model Context Protocol (MCP) server

If you already set up a Model Context Protocol (MCP) server, you can connect the MCP server to your agent.

There are two ways to connect your agent to an MCP server in Copilot Studio:

- Add the MCP server in Copilot Studio by using the *MCP onboarding wizard* (recommended)
- Create a custom connector to your server through Power Apps

This article describes details for both of these methods.

Alternatively, you can register your existing MCP server in Agents 365 using the Agents 365 CLI and Microsoft 365 Admin Center. Once the server is properly registered and approved, it becomes available for use in Copilot Studio. For more information, see [Bring your own (BYO) MCP server](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-tools-for-agent#bring-your-own-byo-mcp-server).

If you don't yet have an MCP server set up, see [Create a new MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-create-new-server) for information on how to get started.

## Supported transports

In MCP, [transports](https://modelcontextprotocol.io/docs/concepts/transports) are the foundation for client-server communication. Transports handle the mechanics of sending and receiving messages. Currently, Copilot Studio supports the Streamable transport type.

Note

Given that SSE transport is [deprecated](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http), Copilot Studio no longer supports SSE for MCP after August 2025.

## Option 1: Use the MCP onboarding wizard (recommended)

The simplest way to connect to an existing MCP server is directly within Copilot Studio by using the MCP onboarding wizard.

This method has two parts:

- Configure the basic MCP server details
- Configure authentication with your MCP server

### Configure basic server details

1. Go to the **Tools** page for your agent.
2. Select **Add a tool**.
3. Select **New tool**.
4. Select **Model Context Protocol**. The MCP onboarding wizard appears.
	![Screenshot of MCP onboarding wizard](https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/mcp-add-existing-server-to-agent/mcp-onboarding-wizard.png)
	Screenshot of MCP onboarding wizard
5. Fill in the required fields **Server name**, **Server description**, and **Server URL**. Write a brief, but clear description of what your MCP server does. The agent orchestrator uses this information to identify whether to call your server at runtime.
6. Select the authentication type for your MCP server, if applicable. You have three options:
	- **None**
		- **API key**: [Configure API key authentication](#configure-authentication-with-your-mcp-server)
		- **OAuth 2.0**: [Configure OAuth 2.0 authentication](#configure-authentication-with-your-mcp-server)
7. If you selected **None**, select **Create**. The **Add tool** dialog appears. Skip to [Create a new connection and add the MCP server to your agent](#create-a-new-connection-and-add-the-mcp-server-to-your-agent).

### Configure authentication with your MCP server

If your server requires authentication, you have two options:

- **API key**: Select this option if your MCP server requires an API key for authentication. An API key is a simple option to authenticate with the server. The user of the agent provides the API key, and the agent includes it in the requests to the MCP server.
- **OAuth 2.0**: Select this option if your MCP server uses OAuth 2.0 for authentication. OAuth 2.0 lets individual users authenticate with the server and grant permissions to your application (agent) without sharing their credentials.

If you choose to use authentication, you need to configure the authentication details. The steps depend on the authentication type you select.

#### Configure API key authentication

1. Select **API key** as the authentication type. More fields appear for you to configure the API key.
2. Select the **Type** of API key to use. You have two options:
	- **Header**: Select this option if your MCP server requires the API key to be sent in the request header.
		- **Query**: Select this option if your MCP server requires the API key to be sent as a query parameter in the URL.
3. Enter the name of the header or query parameter where the API key should be included.
4. Select **Create**. The **Add tool** dialog appears. Skip to [Create a new connection and add the MCP server to your agent](#create-a-new-connection-and-add-the-mcp-server-to-your-agent).

#### Configure OAuth 2.0 authentication

1. Select **OAuth 2.0** as the authentication type.
2. Select the **Type** of OAuth 2.0 authentication to use. You have three options:
	- [Dynamic discovery](#dynamic-discovery): Select this option if your MCP server supports the OAuth 2.0 dynamic client registration (DCR) with discovery mechanism. The client can use a discovery endpoint to automatically discover the necessary endpoints and register itself with the identity provider.
		- [Dynamic](#dynamic): Select this option if your MCP server supports dynamic OAuth 2.0 DCR, but doesn't support the dynamic discovery mechanism. The client can still register itself with the identity provider, but you need to provide the necessary endpoints manually.
		- [Manual](#manual): Select this option if your MCP server requires manual configuration of OAuth 2.0 settings.

##### Dynamic discovery

If your MCP server supports the OAuth 2.0 Dynamic Client Registration (DCR) mechanism, you can use the dynamic discovery option. If supported, DCR with discovery is the simplest method to configure OAuth 2.0 authentication with your MCP server in Copilot Studio.

![Screenshot of MCP onboarding wizard with dynamic discovery for OAuth 2.0 selected](https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/mcp-add-existing-server-to-agent/mcp-onboard-wizard-dynamic-client-registration.png)

Screenshot of MCP onboarding wizard with dynamic discovery for OAuth 2.0 selected

1. Select **Dynamic discovery** as the OAuth 2.0 authentication type.
2. Select **Create** to add the server. The client uses the discovery endpoint to automatically find the necessary endpoints and register itself with the identity provider.
3. Select **Next** to continue. The **Add tool** dialog appears.
4. Continue to [Create a new connection and add the MCP server to your agent](#create-a-new-connection-and-add-the-mcp-server-to-your-agent).

##### Dynamic

1. Select **Dynamic** as the OAuth 2.0 authentication type.
2. Fill in the required fields:
	- **Authorization URL**: The URL of the identity provider server where the client registration and authorization endpoints can be accessed.
		- **Token URL template**: The endpoint where your agent exchanges an authorization code (or refresh token) for an *access token* and *refresh token*. The access token lets your agent use the MCP server on behalf of the user. Refresh tokens let your agent get new access and refresh tokens from the refresh endpoint when the previous access token expires.
3. Select **Create** to add the server. Depending on the configuration, a *callback URL* might appear. The callback URL is where the identity provider responds with the authorization code once the user signs in and grants permissions to your agent.
4. If you see the callback URL, copy the callback URL to add to your application's registration with your identity provider.
5. Select **Next** to continue. The **Add tool** dialog appears.
6. Continue to [Create a new connection and add the MCP server to your agent](#create-a-new-connection-and-add-the-mcp-server-to-your-agent).

##### Manual

1. Select **Manual** as the OAuth 2.0 type. More fields appear for you to configure the OAuth 2.0 settings.
2. Fill in the required fields:
	- **Client ID**: The client identifier the identity provider issues when you register your app. The client ID lets the identity provider know what app is making the request.
		- **Client secret**: The client secret the identity provider issues when you register your app. Your agent sends the client secret along with the client ID to prove your agent is authorized to request access tokens for the MCP server.
		- **Authorization URL**: The identity provider endpoint where your agent redirects the user to sign in and grant permissions to your agent (consent card presented in the agent chat). The user authenticates here and then the identity provider responds back to the agent with an *authorization code*.
		- **Token URL template**: The endpoint where your agent exchanges the authorization code (or refresh token) for an *access token* and *refresh token*. The access token lets your agent use the MCP server on behalf of the user. Refresh tokens let your agent get new access and refresh tokens from the refresh endpoint when the previous access token expires.
		- **Refresh URL**: The endpoint to request a new access token using a refresh token (so that the user doesn't have to sign in again when the token expires).
		- **Scopes** (Optional): The permissions your app is asking for, as a space-separated list.
3. Select **Create** to add the server. A *callback URL* appears. The callback URL is where the identity provider responds with the authorization code once the user signs in and grants permissions to your agent.
4. Copy the callback URL to add to your application's registration with your identity provider.
5. Select **Next** to continue. The **Add tool** dialog appears.
6. Continue to [Create a new connection and add the MCP server to your agent](#create-a-new-connection-and-add-the-mcp-server-to-your-agent).

### Create a new connection and add the MCP server to your agent

1. On **Add tool**, select **Create a new connection** for your MCP server or use an existing one.
2. Select **Add to agent** to finish adding the MCP server to your agent.

## Option 2: Create a custom MCP connector in Power Apps

You can create a custom connector in Power Apps manually to configure a connection to the server.

To carry out this procedure, you need a schema file for your MCP server. The schema file is an OpenAPI specification YAML file that describes the API of your MCP server.

For guidance on what the specification file should look like, check out some of the provided [MCP server schema example](#mcp-server-schema-example).

1. Go to the **Tools** page for your agent.
2. Select **Add a tool**.
3. Select **New tool**.
4. Select **Custom connector**. You're taken to Power Apps to create a new custom connector.
5. Select **New custom connector**.
6. Select **Import OpenAPI file**.
7. Navigate to your schema file and select **Import** to import the file.
8. Select **Continue** to complete the setup in Power Apps. You can read more about the setup process in the Power Apps documentation at [Import the OpenAPI definition](https://learn.microsoft.com/en-us/connectors/custom-connectors/define-openapi-definition#import-the-openapi-definition).

## MCP server schema example

Here's a sample OpenAPI schema file for an MCP server using fictional data, in YAML format. You need to fill in the details for your own MCP server. This sample uses the Streamable transport type.

```yaml
swagger: '2.0'
info:
  title: Contoso
  description: MCP Test Specification, YAML for streamable MCP support in Copilot Studio
  version: 1.0.0
host: contoso.com
basePath: /
schemes:
  - https
paths:
  /mcp:
    post:
      summary: Contoso Lead Management Server
      x-ms-agentic-protocol: mcp-streamable-1.0
      operationId: InvokeMCP
      responses:
        '200':
          description: Success
```

## Edit an MCP connection

To edit your MCP connector or add custom parameters:

1. Go to the Power Apps or Power Automate portal and select **Custom connectors**.
2. Locate your connector file in the list of connectors and make the necessary updates using one of the available methods.

## MCP servers and data policies

Access to MCP servers in Copilot Studio relies on Power Platform connectors for connectivity. This condition means that if a data policy regulates Power Platform connectors, it also regulates access to the MCP server and its tools for your agent. For more information, see [configure a data policy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention#configure-a-data-policy-in-the-power-platform-admin-center).