---
source_url: https://docs.snowflake.com/en/sql-reference/sql/create-notification-integration
vendor: snowflake
topic: notification-integrations
fetched_at: 2026-06-10T06:43:25Z
revalidate_after: 2026-07-10T06:43:25Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## CREATE NOTIFICATION INTEGRATION

Creates a new notification integration in the account or replaces an existing integration. A notification integration is a Snowflake object that provides an interface between Snowflake and third-party messaging services (third-party cloud message queuing services, email services, webhooks, etc.).

The syntax of the command depends on the type of the messaging service and whether the message is inbound or outbound. The following topics explain the syntax for creating notification integrations for different use cases:

- [CREATE NOTIFICATION INTEGRATION (inbound from an Azure Event Grid topic)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-queue-inbound-azure)
- [CREATE NOTIFICATION INTEGRATION (inbound from a Google Pub/Sub topic)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-queue-inbound-gcp)
- [CREATE NOTIFICATION INTEGRATION (outbound to an Amazon SNS topic)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-queue-outbound-aws)
- [CREATE NOTIFICATION INTEGRATION (outbound to an Azure Event Grid topic)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-queue-outbound-azure)
- [CREATE NOTIFICATION INTEGRATION (outbound to a Google Pub/Sub topic)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-queue-outbound-gcp)
- [CREATE NOTIFICATION INTEGRATION (email)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-email)
- [CREATE NOTIFICATION INTEGRATION (webhooks)](https://docs.snowflake.com/sql-reference/sql/create-notification-integration-webhooks)

See also:

[ALTER NOTIFICATION INTEGRATION](https://docs.snowflake.com/sql-reference/sql/alter-notification-integration), [DESCRIBE INTEGRATION](https://docs.snowflake.com/sql-reference/sql/desc-integration), [DROP INTEGRATION](https://docs.snowflake.com/sql-reference/sql/drop-integration), [SHOW INTEGRATIONS](https://docs.snowflake.com/sql-reference/sql/show-integrations)