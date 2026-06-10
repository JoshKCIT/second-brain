---
source_url: https://docs.snowflake.com/en/user-guide/oauth
vendor: snowflake
topic: oauth
fetched_at: 2026-06-10T06:39:53Z
revalidate_after: 2026-07-10T06:39:53Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## Introduction to OAuth

Snowflake enables OAuth for clients through integrations. An integration is a Snowflake object that provides an interface between Snowflake and third-party services. Administrators configure OAuth using a [Security integration](https://docs.snowflake.com/sql-reference/sql/create-security-integration), which enables clients that support OAuth to redirect users to an authorization page and generate access tokens (and optionally, refresh tokens) for accessing Snowflake.

Snowflake supports the [OAuth 2.0](https://oauth.net/2/) protocol for authentication and authorization using one of the options below:

- [Snowflake OAuth](https://docs.snowflake.com/user-guide/oauth-snowflake-overview)
- [External OAuth](https://docs.snowflake.com/user-guide/oauth-ext-overview)

The following table compares Snowflake OAuth and External OAuth:

| Category | Snowflake OAuth | External OAuth |
| --- | --- | --- |
| Modify client application | Required | Required |
| Client application browser access | Required | Not required |
| Programmatic clients | Requires a browser | Best fit |
| Driver property | `authenticator = oauth` | `authenticator = oauth` |
| Security integration syntax | `create security integration type = oauth ...` | `create security integration type = external_oauth` |
| OAuth flow | OAuth 2.0 code grant flow | Any OAuth flow that the client can initiate with the External OAuth server |

## Private connectivity

Snowflake supports External OAuth with private connectivity to the Snowflake service.

Snowflake OAuth and Tableau can be used with private connectivity to Snowflake as follows:

> Tableau Desktop:
> 
> Starting with Tableau 2020.4, Tableau contains an embedded OAuth client that supports connecting to Snowflake with the account URL for private connectivity to the Snowflake service.
> 
> After upgrading to Tableau 2020.4, no further configuration is needed; use the corresponding private connectivity URL for either AWS or Azure to connect to Snowflake.
> 
> Tableau Cloud:
> 
> Starting with Tableau 2020.4, users can optionally configure Tableau Cloud to use the embedded OAuth Client to connect to Snowflake with the account URL for private connectivity to the Snowflake service.
> 
> To use this feature, create a new [Custom Client](https://docs.snowflake.com/user-guide/oauth-custom) security integration and follow the [Tableau instructions](https://help.tableau.com/current/server/en-us/config_oauth_snowflake.htm).
> 
> > [!important] Important
> > To determine the account URL to use with private connectivity to the Snowflake service, call the [SYSTEM$GET\_PRIVATELINK\_CONFIG](https://docs.snowflake.com/sql-reference/functions/system_get_privatelink_config) function.
> 
> Looker:
> 
> Currently, combining Snowflake OAuth and Looker requires access to the public Internet. Therefore, you cannot use Snowflake OAuth and Looker with private connectivity to the Snowflake service.

For more information, refer to:

- [SSO with private connectivity](https://docs.snowflake.com/user-guide/admin-security-fed-auth-overview#label-sso-private-connectivity)
- [Configure Snowflake OAuth for partner applications](https://docs.snowflake.com/user-guide/oauth-partner)

## Clients, drivers, and connectors

Supported clients, drivers, and connectors can use OAuth to verify user login credentials.

Note the following:

- It is necessary to set the `authenticator` parameter to `oauth` and the `token` parameter to the `oauth_access_token`.
- When passing the `token` value as a URL query parameter, it is necessary to URL-encode the `oauth_access_token` value.
- When passing the `token` value to a Properties object (e.g. JDBC Driver), no modifications are necessary.

For more information about connection parameters, refer to the reference documentation for the following clients, drivers, or connectors:

- [Snowflake CLI](https://docs.snowflake.com/developer-guide/snowflake-cli/connecting/configure-connections#label-snowcli-snow-connection-command)
- [SnowSQL](https://docs.snowflake.com/user-guide/snowsql-start#label-snowsql-auth)
- [Python](https://docs.snowflake.com/developer-guide/python-connector/python-connector-connect#label-oauth-python)
- [Go](https://godoc.org/github.com/snowflakedb/gosnowflake#hdr-Connection_Parameters)
- [JDBC](https://docs.snowflake.com/developer-guide/jdbc/jdbc-configure#label-jdbc-connection-parameters)
- [ODBC](https://docs.snowflake.com/developer-guide/odbc/odbc-parameters#label-conn-param-odbc)
- [Spark Connector](https://docs.snowflake.com/user-guide/spark-connector-use#label-spark-ext-oauth)
- [.NET Driver](https://github.com/snowflakedb/snowflake-connector-net/blob/master/README.md#create-a-connection)
- [Node.js Driver](https://docs.snowflake.com/developer-guide/node-js/nodejs-driver-authenticate#label-nodejs-oauth)

## Client Redirect

Snowflake supports using Client Redirect with Snowflake OAuth and External OAuth, including using Client Redirect and OAuth with supported Snowflake Clients.

For more information, refer to [Redirecting client connections](https://docs.snowflake.com/user-guide/client-redirect).

## Replication

Snowflake supports replication and failover/failback with both the Snowflake OAuth and External OAuth security integrations from the source account to the target account.

For details, refer to [Replication of security integrations & network policies across multiple accounts](https://docs.snowflake.com/user-guide/account-replication-security-integrations).