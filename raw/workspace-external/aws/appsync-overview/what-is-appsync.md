---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html
vendor: aws
topic: appsync-overview
fetched_at: 2026-06-10T06:24:03Z
revalidate_after: 2026-08-09T06:24:03Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.md)

What is AWS AppSync? - AWS AppSync GraphQL

## What is AWS AppSync?

AWS AppSync enables developers to connect their applications and services to data and events with secure, serverless and high-performing GraphQL and Pub/Sub APIs. You can do the following with AWS AppSync:

- Access data from one or more data sources from a single GraphQL API endpoint.
- Combine multiple source GraphQL APIs into a single, merged GraphQL API.
- Publish real-time data updates to your applications.
- Leverage built-in security, monitoring, logging, and tracing, with optional caching for low latency.
- Only pay for API requests and any real-time messages that are delivered.

###### Important

As of Mar 13, 2025, you can build a real-time PubSub API powered by WebSockets using AWS AppSync Events. For more information, see [Publish events via WebSocket](https://docs.aws.amazon.com/appsync/latest/eventapi/publish-websocket.html) in the *AWS AppSync Events Developer Guide*.

## AWS AppSync features

- Simplified data access and querying, powered by GraphQL
- Serverless WebSockets for GraphQL subscriptions and pub/sub channels
- Server-side caching to make data available in high speed in-memory caches for low latency
- JavaScript and TypeScript support to write business logic
- Enterprise security with Private APIs to restrict API access and integration with AWS WAF
- Built in authorization controls, with support for API keys, IAM, Amazon Cognito, OpenID Connect providers, and Lambda authorization for custom logic.
- Merged APIs to support federated use cases

For more details about each of these capabilities, see [AWS AppSync features](https://aws.amazon.com/appsync/product-details).

## Are you a first-time AWS AppSync user?

We recommend that first-time AWS AppSync users begin by reading the following sections:

- If you're unfamiliar with GraphQL, see the [Getting started: Creating your first GraphQL API in AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html).
- If you're building applications that consume GraphQL APIs, see [Building a client application using Amplify client](https://docs.aws.amazon.com/appsync/latest/devguide/building-a-client-app.html) and [Using subscriptions for real-time data applications in AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-data.html).
- If you're looking for GraphQL resolver information, see the following:
	JavaScript/TypeScript
	- [Resolver tutorials (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials-js.html)
	- [Resolver reference (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html)
	VTL
	- [Resolver tutorials (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials.html)
	- [AWS AppSync resolver mapping template reference (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html)
- If you're looking for AWS AppSync example projects, updates, and more, see the [AppSync blog](https://aws.amazon.com/blogs/mobile/category/mobile-services/aws-appsync/).

## Related services

If you're building a web or mobile app from the ground up, consider using [AWS Amplify](https://aws.amazon.com/amplify/). Amplify leverages AWS AppSync and other AWS services to help you build more robust, powerful web and mobile apps with less work.

## Pricing for AWS AppSync

AWS AppSync is priced based on millions of requests and updates. Caching costs an additional fee. For more information, see [AWS AppSync pricing](https://aws.amazon.com/appsync/pricing/).

The following lists the exceptions to general AWS AppSync pricing:

- Requests are not charged for authorization and authentication failures.
- Calls to methods that require API keys are not charged when API keys are missing or invalid.