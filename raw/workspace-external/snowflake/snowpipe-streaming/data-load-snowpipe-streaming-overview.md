---
source_url: https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-overview
vendor: snowflake
topic: snowpipe-streaming
fetched_at: 2026-06-10T06:43:32Z
revalidate_after: 2026-07-10T06:43:32Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## Snowpipe Streaming

Snowpipe Streaming is Snowflake’s real-time ingestion service built on the high-performance architecture. It enables applications to load streaming data directly into Snowflake tables as rows arrive, without staging files or managing intermediate storage. Data becomes available for query within seconds of ingestion, supporting use cases from IoT telemetry and Change Data Capture (CDC) pipelines to fraud detection and live analytics.

Snowpipe Streaming delivers:

- Up to **10 GB/s** throughput per table
- **As low as 5 second** end-to-end ingest-to-query latency
- **Exactly-once delivery** through built-in offset token tracking
- **Ordered ingestion** within each channel
- Streaming into Snowflake-managed [Apache Iceberg](https://docs.snowflake.com/user-guide/tables-iceberg) tables

## Why use Snowpipe Streaming

- **Exactly-once delivery**: Built-in offset token tracking enables exactly-once semantics. Your application tracks committed offsets and replays from the last committed position on recovery, preventing duplicate data and data loss. For more information, see [Offset tokens and exactly-once delivery](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-channels#label-replication-snowpipe-offset-tokens).
- **Ordered ingestion**: Rows are ingested in order within each [channel](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-channels#label-replication-snowpipe-channels). Channels map naturally to source partitions (for example, Kafka topic partitions), enabling deterministic replay and zero-loss recovery.
- **High throughput, low latency**: Designed to support ingest speeds of up to 10 GB/s per table, with data available for query in as low as 5 seconds.
- **In-flight transformations**: Cleanse, reshape, and transform data during ingestion by using COPY command syntax within the PIPE object. Filter rows, reorder columns, cast types, and apply expressions before data is committed to the target table, with no separate ETL step needed.
- **Pre-clustering at ingest time**: Sort data during ingestion for optimized query performance on tables with clustering keys.
- **Apache Iceberg table support**: Stream data into Snowflake-managed Iceberg tables, including both Iceberg v2 and [Iceberg v3](https://docs.snowflake.com/user-guide/tables-iceberg-v3-specification-support) tables. For more information, see [Snowpipe Streaming high-performance architecture with Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-iceberg).
- **Schema evolution**: Automatically adapt table schemas to changing data structures. Snowflake can add new columns detected in the incoming stream without manual DDL changes.
- **Simplified pipelines**: SDKs write rows directly into tables, bypassing the need for staging files or intermediate cloud storage.
- **Serverless and scalable**: Compute resources scale automatically based on ingestion load. No infrastructure to manage.
- **Transparent pricing**: Throughput-based billing calculated by credits per uncompressed GB of data ingested. For more information, see [Snowpipe Streaming high-performance architecture: Understand your costs](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-cost).

## How to connect

Snowpipe Streaming supports multiple ingestion paths to fit different workloads:

| Integration | Best for |
| --- | --- |
| [Java SDK](https://central.sonatype.com/artifact/com.snowflake/snowpipe-streaming) ([Java API reference](https://docs.snowflake.com/user-guide/snowpipe-streaming-sdk/reference/java/com/snowflake/ingest/streaming/package-summary.html)) | High-throughput custom applications. Requires Java 11 or later. |
| [Python SDK](https://pypi.org/project/snowpipe-streaming/) ([Python API reference](https://docs.snowflake.com/en/user-guide/snowpipe-streaming-sdk-python/reference/latest/index)) | Data engineering and Python-native workflows. Requires Python 3.9 or later. |
| [Node.js SDK](https://www.npmjs.com/package/snowpipe-streaming) ([Node.js API reference](https://docs.snowflake.com/user-guide/snowpipe-streaming-sdk/reference/nodejs/index.html)) | JavaScript and TypeScript applications. Requires Node.js 20 or later. |
| [REST API](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-rest-api) | Lightweight workloads, IoT devices, and edge deployments. |
| [Snowflake Connector for Kafka](https://docs.snowflake.com/user-guide/kafka-connector/index) | Apache Kafka topic ingestion. |

The Java, Python, and Node.js SDKs use a shared Rust-based client core for improved client-side performance and lower resource usage.

> [!note] Note
> We recommend that you begin with the Snowpipe Streaming SDK over the REST API to benefit from the improved performance and getting-started experience.

To get started, see [Tutorial: Get started with the SDK](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-getting-started) or [Tutorial: Get started with the REST API](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-rest-tutorial).

For technical details about the PIPE object, channels, offset tokens, and supported data types, see [Key concepts](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview).

## Snowpipe Streaming versus Snowpipe

Snowpipe Streaming is intended to complement Snowpipe, not replace it. Use Snowpipe Streaming in scenarios where data arrives as rows (for example, from Apache Kafka topics, IoT devices, or application events) instead of files. With Snowpipe Streaming, you don’t need to create files to load data into Snowflake tables.

> ![Snowpipe Streaming](https://docs.snowflake.com/static/images/data-load-snowpipe-streaming.png)
> 
> Snowpipe Streaming

The following table describes the differences between Snowpipe Streaming and Snowpipe:

| Category | Snowpipe Streaming | Snowpipe |
| --- | --- | --- |
| Form of data to load | Rows | Files. If your existing data pipeline generates files in blob storage, we recommend using Snowpipe instead. |
| Data ordering | Ordered insertions within each channel | Not supported. Snowpipe can load data from files in an order different from the file creation timestamps in cloud storage. |
| Load history | Load history recorded in [SNOWPIPE\_STREAMING\_FILE\_MIGRATION\_HISTORY view](https://docs.snowflake.com/sql-reference/account-usage/snowpipe_streaming_file_migration_history) (Account Usage) | Load history recorded in [COPY\_HISTORY](https://docs.snowflake.com/sql-reference/account-usage/copy_history) (Account Usage) and [COPY\_HISTORY function](https://docs.snowflake.com/sql-reference/functions/copy_history) (Information Schema) |
| Pipe object | The PIPE object is the server-side processing layer for all streaming ingestion. It handles schema validation, in-flight transformations, and pre-clustering. A default pipe is created automatically for each table, or you can create a custom pipe for advanced processing. | A pipe object queues and loads staged file data into target tables. |

## In this section

**Key concepts**

- [Channels and exactly-once delivery](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-channels)
- [The PIPE object](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-pipe-object)
- [Table support and schema](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-table-support)
- [Operations and reference](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-operations)

**Get started**

- [Tutorial: Get started with the SDK](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-getting-started)
- [Tutorial: Get started with the REST API](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-rest-tutorial)
- [Configurations and examples](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-configurations)

**Ingestion targets**

- [Iceberg tables](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-iceberg)

**Operations**

- [Best practices](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-best-practices)
- [Error handling](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-error-handling)
- [Error logging](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-error-tables)
- [Run the SDK in Snowpark Container Services](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-spcs)
- [Costs](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-cost)
- [Limitations and considerations](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-limitations)
- [Migration from classic architecture](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-migration)

**Reference**

- [REST API endpoints](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-rest-api)
- [Python SDK Reference](https://docs.snowflake.com/en/user-guide/snowpipe-streaming-sdk-python/reference/latest/index)
- [Node.js SDK Reference](https://docs.snowflake.com/user-guide/snowpipe-streaming-sdk/reference/nodejs/index.html)
- [Java SDK Reference](https://docs.snowflake.com/user-guide/snowpipe-streaming-sdk/reference/java/index.html)
- [Comparison: Classic vs current SDK](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-comparison)

## Classic architecture

> [!important] Important
> The classic architecture, which uses the [snowflake-ingest-sdk](https://mvnrepository.com/artifact/net.snowflake/snowflake-ingest-sdk) Java SDK, is planned for deprecation. No immediate changes are required. Current workloads continue to be fully supported.
> 
> For full details, see [Notice of planned deprecation](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-classic-deprecation).

If you have existing workloads running on the classic architecture, see [Classic architecture](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-classic-overview). For a detailed comparison of differences, see [Comparison between high-performance and classic SDKs](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-comparison).

If you’re upgrading to the high-performance architecture, see [Migration guide](https://docs.snowflake.com/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-migration).