---
source_url: https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit
vendor: snowflake
topic: streamlit
fetched_at: 2026-06-10T06:43:51Z
revalidate_after: 2026-07-10T06:43:51Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

This topic describes key features of Streamlit in Snowflake.

## What is Streamlit?

[Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy to create and share custom web apps for machine learning and data science. By using Streamlit you can quickly build and deploy powerful data applications. For more information about the open-source library, see the [Streamlit documentation](https://docs.streamlit.io/).

![](https://docs.snowflake.com/static/images/streamlit/streamlit-visual.png)

## Deploy Streamlit apps in Snowflake

Streamlit in Snowflake helps developers securely build, deploy, and share Streamlit apps on Snowflake’s data cloud. Using Streamlit in Snowflake, you can build applications that process and use data in Snowflake without moving data or application code to an external system.

![](https://docs.snowflake.com/static/images/streamlit/sis-example-app.png)

### Key features of Streamlit in Snowflake

- Snowflake manages the underlying compute and storage for your Streamlit app.
- Snowflake stores your source code and environment configuration within a Snowflake object that uses [Role-based Access Control (RBAC)](https://docs.snowflake.com/user-guide/security-access-control-overview) to manage access to your Streamlit app.
- You can choose between a warehouse and container runtime.
- Streamlit in Snowflake works seamlessly with Snowpark, user-defined functions (UDFs), stored procedures, and Snowflake Native App Framework.
- When working in Snowsight, you can use the side-by-side editor and app preview to quickly modify your source code and environment.

## Use cases

For additional use cases on building dashboards, data tools, and ML/AI, see [Streamlit in Snowflake demos](https://github.com/Snowflake-Labs/snowflake-demo-streamlit).

> [!note] Note
> These quickstarts are only shown as examples. Following along with the example may require additional rights to third-party data, products, or services that are not owned or provided by Snowflake. Snowflake does not guarantee the accuracy of these examples or cover them under any Service Level Agreement.

## Developer guides

The following guides explain working with Streamlit in Snowflake.

| Guide | Description |
| --- | --- |
| [Getting started with Streamlit in Snowflake](https://docs.snowflake.com/developer-guide/streamlit/getting-started/overview) | Deploy your first app with sample code and learn the basics. |
| [Create your Streamlit app](https://docs.snowflake.com/developer-guide/streamlit/app-development/creating-your-app) | Deploy a Streamlit app from your existing code using Snowsight, SQL, or Snowflake CLI. |
| [Runtime environments for Streamlit apps](https://docs.snowflake.com/developer-guide/streamlit/app-development/runtime-environments) | Understand the container and warehouse runtime environments for Streamlit in Snowflake apps. |