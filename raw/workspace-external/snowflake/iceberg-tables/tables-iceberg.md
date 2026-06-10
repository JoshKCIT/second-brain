---
source_url: https://docs.snowflake.com/en/user-guide/tables-iceberg
vendor: snowflake
topic: iceberg-tables
fetched_at: 2026-06-10T06:43:47Z
revalidate_after: 2026-07-10T06:43:47Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## Apache Iceberg™ tables

Apache Iceberg™ tables for Snowflake combine the performance and query semantics of typical Snowflake tables with external cloud storage that you manage. They are ideal for existing data lakes that you cannot, or choose not to, store in Snowflake.

Iceberg tables use the [Apache Iceberg™](https://iceberg.apache.org/) open table format specification, which provides an abstraction layer on data files stored in open formats and supports features such as:

- ACID (atomicity, consistency, isolation, durability) transactions
- Schema evolution
- Hidden partitioning
- Table snapshots

Snowflake supports Iceberg tables that use the [Apache Parquet™](https://parquet.apache.org/) file format.

## Getting started

To get started with Iceberg tables, see [Tutorial: Create your first Apache Iceberg™ table](https://docs.snowflake.com/user-guide/tutorials/create-your-first-iceberg-table).

## How it works

This section provides information specific to working with Iceberg tables *in Snowflake*. To learn more about the Iceberg table format specification, see the official [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/) and the [Iceberg Table Spec](https://iceberg.apache.org/spec/).

### Data storage

Iceberg tables store their data and metadata files in an external cloud storage location (Amazon S3, Google Cloud Storage, or Azure Storage). The external storage is not part of Snowflake. You are responsible for all management of the external cloud storage location, including the configuration of data protection and recovery. Snowflake does not provide [Fail-safe](https://docs.snowflake.com/user-guide/data-failsafe) storage for Iceberg tables.

Snowflake connects to your storage location using an [external volume](#label-tables-iceberg-external-volume-def), and Iceberg tables incur no Snowflake storage costs. For more information, see [Billing](#label-tables-iceberg-billing).

To learn more about storage for Iceberg tables, see [Storage for Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg-storage).

#### External volume

An external volume is a named, account-level Snowflake object that you use to connect Snowflake to your external cloud storage for Iceberg tables. An external volume stores an identity and access management (IAM) entity for your storage location. Snowflake uses the IAM entity to securely connect to your storage for accessing table data, Iceberg metadata, and manifest files that store the table schema, partitions, and other metadata.

A single external volume can support one or more Iceberg tables.

To set up an external volume for Iceberg tables, see [Configure an external volume](https://docs.snowflake.com/user-guide/tables-iceberg-configure-external-volume).

### Catalog

An Iceberg catalog enables a compute engine to manage and load Iceberg tables. The catalog forms the first architectural layer in the [Iceberg table specification](https://iceberg.apache.org/spec/#overview) and must support:

- Storing the current metadata pointer for one or more Iceberg tables. A metadata pointer maps a table name to the location of that table’s current metadata file.
- Performing atomic operations so that you can update the current metadata pointer for a table.

To learn more about Iceberg catalogs, see the [Apache Iceberg documentation](https://iceberg.apache.org/terms/#catalog-implementations).

Snowflake supports different [catalog options](#label-tables-iceberg-catalog-options). For example, you can use Snowflake as the Iceberg catalog, or use a [catalog integration](#label-tables-iceberg-catalog-integration-def) to connect Snowflake to an external Iceberg catalog.

#### Catalog integration

A catalog integration is a named, account-level Snowflake object that stores information about how your table metadata is organized for the following scenarios:

- When you don’t use [Snowflake as the Iceberg catalog](https://docs.snowflake.com/user-guide/tables-iceberg#label-tables-iceberg-snowflake-as-catalog). For example, you need a catalog integration if your table is managed by AWS Glue.
- When you want to integrate with [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview) to:
	- Query an Iceberg table in Snowflake Open Catalog using Snowflake.
		- Sync a Snowflake-managed Iceberg table with Snowflake Open Catalog so that third-party compute engines can query the table.

A single catalog integration can support one or more Iceberg tables that use the same external catalog.

To set up a catalog integration, see [Configure a catalog integration](https://docs.snowflake.com/user-guide/tables-iceberg-configure-catalog-integration).

### Metadata and snapshots

Iceberg uses a snapshot-based querying model, where data files are mapped using manifest and metadata files. A snapshot represents the state of a table at a point in time and is used to access the complete set of data files in the table.

To learn about table metadata and Time Travel support, see [Metadata and retention for Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg-metadata).

### Cross-cloud/cross-region support

Snowflake supports using an external volume storage location with a different cloud provider (in a different region) from the one that hosts your Snowflake account.

| Table type | Cross-cloud/cross-region support | Notes |
| --- | --- | --- |
| Tables that use an external catalog with a [catalog integration](#label-tables-iceberg-catalog-integration) | ✔ | If your Snowflake account and external volume are in different regions, your external cloud storage account incurs egress costs when you query the table. |
| Tables that use [Snowflake as the catalog](#label-tables-iceberg-snowflake-as-catalog) | ✔ | If your Snowflake account and external volume are in different regions, your external cloud storage account incurs egress costs when you query the table.  These tables incur costs for cross-region data transfer usage. For more information, see [Billing](#label-tables-iceberg-billing). |

### Billing

Snowflake bills your account for virtual warehouse (compute) usage and cloud services when you work with Iceberg tables. Snowflake also bills your account if you use [automated refresh](https://docs.snowflake.com/user-guide/tables-iceberg-auto-refresh#label-tables-iceberg-auto-refresh-billing) or an [external query engine through Snowflake Horizon Catalog](https://docs.snowflake.com/user-guide/tables-iceberg-access-using-external-query-engine-snowflake-horizon#label-tables-iceberg-query-using-external-query-engine-snowflake-horizon-billing).

If a [Snowflake-managed](#label-tables-iceberg-snowflake-as-catalog) Iceberg table is cross-cloud/cross-region, Snowflake bills your cross-region data transfer usage under the TRANSFER\_TYPE of DATA\_LAKE. To learn more, see:

- [DATA\_TRANSFER\_HISTORY view](https://docs.snowflake.com/sql-reference/organization-usage/data_transfer_history) in the ORGANIZATION\_USAGE schema.
- [DATA\_TRANSFER\_HISTORY view](https://docs.snowflake.com/sql-reference/account-usage/data_transfer_history) in the ACCOUNT\_USAGE schema.

Snowflake does not bill your account for the following:

- Iceberg table storage costs when the table uses an external volume that you manage. Your cloud storage provider bills you directly for data storage usage. However, if the table uses [Snowflake Storage](https://docs.snowflake.com/user-guide/tables-iceberg-internal-storage) (`EXTERNAL_VOLUME = SNOWFLAKE_MANAGED`), Snowflake charges for the storage. For more information, see [Snowflake storage for Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg-internal-storage).
- Active bytes used by Iceberg tables. However, the [INFORMATION\_SCHEMA.TABLE\_STORAGE\_METRICS](https://docs.snowflake.com/sql-reference/info-schema/table_storage_metrics) and [ACCOUNT\_USAGE.TABLE\_STORAGE\_METRICS](https://docs.snowflake.com/sql-reference/account-usage/table_storage_metrics) views display ACTIVE\_BYTES for Iceberg tables to help you track how much storage a table occupies. To view an example, see [Retrieve storage metrics](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-get-storage-metrics).

> [!note] Note
> If your Snowflake account and external volume are in different regions, your external cloud storage account incurs egress costs when you query the table.

## Catalog options

Snowflake supports the following Iceberg catalog options:

- Use Snowflake as the [Iceberg catalog](#label-tables-iceberg-catalog-def)
- Use an external Iceberg catalog

The following table summarizes the differences between these catalog options.

|  | [Use Snowflake as the catalog](#label-tables-iceberg-snowflake-as-catalog) | [Use an external catalog](#label-tables-iceberg-catalog-integration) |
| --- | --- | --- |
| Read access | ✔ | ✔ |
| Write access | ✔ | ✔ |
| Catalog-vended credentials |  | ✔ |
| Write access across regions | ✔ | ✔ with [Write support for externally managed tables](https://docs.snowflake.com/user-guide/tables-iceberg-externally-managed-writes) |
| Data and metadata storage | External volume (cloud storage) | External volume (cloud storage) |
| Snowflake platform support | ✔ |  |
| Integrates with Snowflake Open Catalog | ✔  You can sync a Snowflake-managed table with Open Catalog to query a table using other compute engines. | ✔  You can use Snowflake to query or write to Iceberg tables managed by Open Catalog. |
| Works with the [Snowflake Catalog SDK](https://docs.snowflake.com/user-guide/tables-iceberg-catalog) | ✔ | ✔ |
| Replication for tables | ✔  See [Configure replication for Snowflake-managed Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg-replication). |  |

### Use Snowflake as the catalog

An Iceberg table that uses Snowflake as the Iceberg catalog (Snowflake-managed Iceberg table) provides full Snowflake platform support with read and write access. You can choose where the table data and metadata files are stored:

- [Snowflake storage](https://docs.snowflake.com/user-guide/tables-iceberg-internal-storage): Snowflake stores and manages the Iceberg table files for you, so you don’t need to configure or grant access to external cloud storage.
- External cloud storage that you manage, which Snowflake accesses using an [external volume](#label-tables-iceberg-external-volume-def).

Snowflake handles all lifecycle maintenance, such as compaction, for the table. However, you can [disable compaction for the table](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-manage-set-data-compaction), if needed.

![How Iceberg tables that use Snowflake as the Iceberg catalog work](https://docs.snowflake.com/static/images/tables-iceberg-snowflake-as-catalog.svg)

How Iceberg tables that use Snowflake as the Iceberg catalog work

### Use an external catalog

An Iceberg table that uses an external catalog provides limited Snowflake platform support.

With this table type, Snowflake uses a [catalog integration](#label-tables-iceberg-catalog-integration-def) to retrieve information about your Iceberg metadata and schema.

You can use this option to create an Iceberg table for the following sources:

- [Remote Iceberg REST catalog](https://docs.snowflake.com/user-guide/tables-iceberg-configure-catalog-integration-rest), including [AWS Glue](https://docs.snowflake.com/user-guide/tables-iceberg-configure-catalog-integration-rest-glue) and [Snowflake Open Catalog](https://docs.snowflake.com/user-guide/tables-iceberg-open-catalog). Snowflake supports writes to externally managed tables that use a remote Iceberg REST catalog.
	> [!tip] Tip
	> To bring your external data from a remote Iceberg REST catalog into Snowflake, you can create a catalog-linked database. The database automatically discovers and stays in sync with the namespaces and tables in your remote catalog. You can use a catalog-linked database to read and write to the tables in your remote catalog from Snowflake, while preserving full interoperability with your existing Iceberg ecosystem. For more information, see the following topics:
	> 
	> - [Use a catalog-linked database for Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg-catalog-linked-database)
	> - If your external data is in Unity Catalog, see [Tutorial: Set up bidirectional access to Apache Iceberg™ tables in Databricks Unity Catalog](https://docs.snowflake.com/user-guide/tutorials/tables-iceberg-set-up-bidirectional-access-to-unity-catalog)
	> - If your external data is in AWS Glue, see [Build Data Lakes using Apache Iceberg with Snowflake and AWS Glue](https://www.snowflake.com/en/developers/guides/data-lake-using-apache-iceberg-with-snowflake-and-aws-glue/)
- [Delta table files in object storage](https://docs.snowflake.com/user-guide/tables-iceberg-configure-catalog-integration-object-storage#label-tables-iceberg-create-cat-int-delta) (**Delta Direct**; see [CREATE ICEBERG TABLE (Delta files in object storage)](https://docs.snowflake.com/sql-reference/sql/create-iceberg-table-delta))
- [Iceberg metadata files in object storage](https://docs.snowflake.com/user-guide/tables-iceberg-configure-catalog-integration-object-storage#label-tables-iceberg-create-cat-int-iceberg-files)

Snowflake does not assume any life-cycle management on the table.

The table data and metadata are stored in external cloud storage, which Snowflake accesses using an [external volume](#label-tables-iceberg-external-volume-def).

> [!note] Note
> If you want full Snowflake platform support for an Iceberg table that uses an external catalog, you can convert it to use Snowflake as the catalog. For more information, see [Convert an Apache Iceberg™ table to use Snowflake as the catalog](https://docs.snowflake.com/user-guide/tables-iceberg-conversion).

The following diagram shows how an Iceberg table uses a catalog integration with an external Iceberg catalog.

![How Iceberg tables that use a catalog integration work](https://docs.snowflake.com/static/images/tables-iceberg-external-catalog.svg)

How Iceberg tables that use a catalog integration work

## Considerations and limitations

The following considerations and limitations apply to Iceberg tables, and are subject to change:

**Clouds and regions**

> - Iceberg tables are available for all Snowflake accounts, on all cloud platforms and in all regions.
> - Cross-cloud/cross-region tables are supported. For more information, see [Cross-cloud/cross-region support](#label-tables-iceberg-cross-cloud-support).

**Iceberg**

> - Versions 1, 2, and 3 of the Apache Iceberg specification are supported, excluding the following [features](https://iceberg.apache.org/spec/):
> 	- Row-level equality deletes. However, tables that use Snowflake as the catalog support Snowflake [DELETE](https://docs.snowflake.com/sql-reference/sql/delete) statements.
> 		- Using the `history.expire.min-snapshots-to-keep` [table property](https://iceberg.apache.org/docs/1.2.1/configuration/#table-behavior-properties) to specify the default minimum number of snapshots to keep. For more information, see [Metadata and snapshots](#label-tables-iceberg-snapshots).
> - Iceberg partitioning with the `bucket` transform function impacts performance for queries that use conditional clauses to filter results.
> - For Iceberg tables that aren’t managed by Snowflake, be aware of the following:
> 	- Time travel to any snapshot generated after table creation is supported as long as you periodically refresh the table before the snapshot expires.
> 		- Converting a table that has an un-materialized identity partition column isn’t supported. An un-materialized identity partition column is created when a table defines an identity transform using a source column that doesn’t exist in a Parquet file.
> 		- For [row-level deletes](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-row-level-deletes):
> 		- Snowflake supports [position deletes](https://iceberg.apache.org/spec/#position-delete-files) only for v2 Iceberg tables, and [deletion vectors](https://iceberg.apache.org/spec/#deletion-vectors) for v3 Iceberg tables.
> 		- Snowflake only supports position deletes with externally managed Iceberg tables.
> 		- For the best read performance when you use row-level deletes, perform regular compaction and table maintenance to remove old delete files. For information, see [Maintain tables that use an external catalog](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-manage-external-catalog).
> 		- Excessive position deletes, especially dangling position deletes, might prevent table creation and refresh operations. To avoid this issue, perform table maintenance to remove extra position deletes.
> 			The table maintenance method to use depends on your external Iceberg engine. For example, you can use the `rewrite_data_files` method for Spark with the `delete-file-threshold` or `rewrite-all` options. For more information, see [rewrite\_data\_files](https://iceberg.apache.org/docs/latest/spark-procedures/#rewrite_data_files) in the Apache Iceberg™ documentation.

**File formats**

> - Iceberg tables support Apache Parquet files.
> - Parquet files that use the unsigned integer logical type aren’t supported.
> - For Parquet files that use the `LIST` logical type, be aware of the following:
> 	- The three-level annotation structure with the `element` keyword is supported. For more information, see [Parquet Logical Type Definitions](https://github.com/apache/parquet-format/blob/master/LogicalTypes.md#lists). If your Parquet file uses an obsolete format with the `array` keyword, you must regenerate your data based on the supported format.

**External volumes**

> - You can’t access the cloud storage locations in external volumes using a storage integration.
> - You must configure a separate trust relationship for each external volume that you create.
> - You can use [outbound private connectivity](https://docs.snowflake.com/user-guide/private-connectivity-outbound) to access Snowflake-managed Iceberg tables and Iceberg tables that use a catalog integration for object storage, but cannot use it to access Iceberg tables that use other catalog integrations.
> - After you create a Snowflake-managed table, the path to its files in external storage does not change, even if you rename the table.
> - Snowflake can’t support external volumes with S3 bucket names that contain dots (for example, `my.s3.bucket`). S3 doesn’t support SSL for virtual-hosted-style buckets with dots in the name, and Snowflake uses virtual-host-style paths and HTTPS to access data in S3.

**Metadata files**

> - The metadata files don’t identify the most recent snapshot of an Iceberg table.
> - You can’t modify the location of the data files or snapshot using the ALTER ICEBERG TABLE command. To modify either of these settings, you must recreate the table (using the CREATE OR REPLACE ICEBERG TABLE syntax).
> - For tables that use an external catalog:
> 	- Ensure that manifest files don’t contain duplicates. If duplicate files are present in the *same* snapshot, Snowflake returns an error that includes the path of the duplicate file.
> 		- You can’t create a table if the Parquet metadata contains invalid UTF-8 characters. Ensure that your Parquet metadata is UTF-8 compliant.
> - Snowflake detects corruptions and inconsistencies in Parquet metadata produced outside of Snowflake, and surfaces issues through error messages.
> 	It’s possible to create, refresh, or query externally managed (or converted) tables, even if the table metadata is inconsistent. When writing Iceberg data, ensure that the table’s metadata statistics (for example, `RowCount` or `NullCount`) match the data content.
> - For tables that use Snowflake as the catalog, Snowflake processes DDL statements individually and produces metadata in a way that might differ from other catalogs. For more information, see [DDL statements](https://docs.snowflake.com/user-guide/tables-iceberg-transactions#label-tables-iceberg-transactions-ddl).

**Clustering**

> [Clustering](https://docs.snowflake.com/user-guide/tables-clustering-keys) support depends on the type of Iceberg table.
> 
> | Table type | Notes |
> | --- | --- |
> | Tables that use Snowflake as the Iceberg catalog | Set a clustering key by using either the CREATE ICEBERG TABLE or the ALTER ICEBERG TABLE command. To set or manage a clustering key, see [CREATE ICEBERG TABLE (Snowflake as the Iceberg catalog)](https://docs.snowflake.com/sql-reference/sql/create-iceberg-table-snowflake) and [ALTER ICEBERG TABLE](https://docs.snowflake.com/sql-reference/sql/alter-iceberg-table). |
> | Tables that use an external catalog | Clustering is not supported. |
> | Converted tables | Snowflake only clusters files if they were created after converting the table, or if the files have since been modified using a DML statement. |

**Delta**

> - Snowflake supports minReaderVersion 3 and can read all tables written by engines that use the latest version of Delta Lake, which is 4.0.0. Delta Lake version 4.0.0 includes support for deletion vectors and liquid clustering.
> - Snowflake streams aren’t supported for Iceberg tables created from Delta table files with partition columns. However, insert-only streams for tables created from Delta files *without* partition columns are supported.
> - Iceberg tables created from Delta files that were created before the [2024\_04](https://docs.snowflake.com/release-notes/bcr-bundles/2025_04_bundle) release bundle are not supported in dynamic tables.
> - Snowflake doesn’t support creating Iceberg tables from Delta table definitions in the AWS Glue Data Catalog.
> 
> - Parquet files (data files for Delta tables) that use any of the following features or data types aren’t supported:
> 	- Field IDs.
> 		- The INTERVAL data type.
> 		- The DECIMAL data type with precision higher than 38.
> 		- LIST or MAP types with one-level or two-level representation.
> 		- Unsigned integer types (INT(signed = false)).
> 		- The FLOAT16 data type.
> - You can use the Parquet physical type `int96` for TIMESTAMP, but Snowflake doesn’t support `int96` for TIMESTAMP\_NTZ.
> 
> - For more information about Delta data types and Iceberg tables, see [Delta data types](https://docs.snowflake.com/user-guide/tables-iceberg-data-types#label-tables-iceberg-delta-source-data-types).
> - Snowflake processes a maximum of 1000 Delta commit files each time you refresh a table using CREATE/ALTER … REFRESH. If your table has over 1000 commit files, you can do additional manual refreshes. Each time, the refresh process continues from where the last one stopped.
> 	> [!note] Note
> 	> Snowflake uses Delta checkpoint files when creating an Iceberg table. The 1,000 commit file limit only applies to commits after the latest checkpoint.
> 	> 
> 	> When you refresh an existing table, Snowflake processes Delta commit files, but not checkpoint files. If table maintenance removes stale log and data files for the source Delta table, you should refresh Delta-based Iceberg tables in Snowflake more frequently than the retention period of Delta logs and data files.
> - The following Delta Lake features aren’t currently supported: Row Tracking, change data files, change metadata, DataChange, CDC, protocol evolution.

**Automated refresh**

> - For catalog integrations created before Snowflake version 8.22 (or 9.2 for Delta-based tables), you must manually set the `REFRESH_INTERVAL_SECONDS` parameter before you enable automated refresh on tables that depend on that catalog integration. For instructions, see [ALTER CATALOG INTEGRATION … SET AUTO\_REFRESH](https://docs.snowflake.com/sql-reference/sql/alter-catalog-integration).
> - For [catalog integrations for object storage](https://docs.snowflake.com/user-guide/tables-iceberg-configure-catalog-integration-object-storage), automated refresh is only supported for integrations with `TABLE_FORMAT = DELTA`.
> - For tables with frequent updates, using a shorter polling interval (`REFRESH_INTERVAL_SECONDS`) can cause performance degradation.
> - Automated refresh synchronizes schema changes alongside [DML](https://docs.snowflake.com/sql-reference/sql-dml) operations such as INSERT, UPDATE, or DELETE. To apply schema changes made through DDL operations alone, perform a [manual refresh](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-refresh-metadata).

**Catalog-linked databases and automatic table discovery**

> - Supported only when you use a catalog integration for Iceberg REST (for example, Snowflake Open Catalog).
> - To limit automatic table discovery to a specific set of namespaces, use the ALLOWED\_NAMESPACES parameter. You can also use the BLOCKED\_NAMESPACES parameter to block a set of namespaces.
> - Snowflake doesn’t sync remote catalog access control for users or roles.
> - You can create schemas, externally managed Iceberg tables, or database roles in a catalog-linked database. Creating other Snowflake objects isn’t currently supported.
> - When you create a catalog-linked database, you can’t specify the default Iceberg version or merge-on-read behavior to use for Iceberg tables.
> 	However, you can modify these properties for an existing database by using the [ALTER DATABASE (catalog-linked)](https://docs.snowflake.com/sql-reference/sql/alter-database-catalog-linked) command to set the following parameters:
> 	- ICEBERG\_VERSION\_DEFAULT
> 		- ICEBERG\_MERGE\_ON\_READ\_BEHAVIOR
> - For Iceberg tables in a catalog-linked database:
> 	- Snowflake bidirectionally syncs table and column descriptions between the remote catalog and Snowflake. Sync can update a description to a new value, but never replaces a non-empty description with an empty one. Other remote catalog table properties, such as retention policies or buffers, aren’t copied, and altering table properties isn’t currently supported.
> 		- [Automated refresh](https://docs.snowflake.com/user-guide/tables-iceberg-auto-refresh) is enabled by default. If the `table-uuid` of an external table and the catalog-linked database table don’t match, refresh fails and Snowflake drops the table from the catalog-linked database; Snowflake doesn’t change the remote table.
> 		- If you drop a table from the remote catalog, Snowflake drops the table from the catalog-linked database. This action is asynchronous, so you might not see the change in the remote catalog right away.
> 		- If you rename a table in the remote catalog, Snowflake drops the existing table from the catalog-linked database and creates a table with the new name.
> 		- Masking policies and tags are supported. Other Snowflake-specific features, including replication and cloning, aren’t supported.
> 		- The character that you choose for the NAMESPACE\_FLATTEN\_DELIMITER parameter can’t appear in your remote namespaces. During the auto discovery process, Snowflake skips any namespace that contains the delimiter, and doesn’t create a corresponding schema in your catalog-linked database.
> 		- If you specify anything other than `_`, `$`, or numbers for the NAMESPACE\_FLATTEN\_DELIMITER parameter, you must put the schema name in quotes when you query the table.
> 		- For databases linked to AWS Glue, you must use lowercase letters and surround the schema, table, and column names in double quotes. This is also required for other Iceberg REST catalogs that only support lowercase identifiers.
> 		The following example shows a valid query:
> 		```sql
> 		CREATE SCHEMA "s1";
> 		```
> 		The following statements aren’t valid, because they use uppercase letters or omit the double quotes:
> 		```sql
> 		CREATE SCHEMA s1;
> 		CREATE SCHEMA "Schema1";
> 		```
> 		- Using UNDROP ICEBERG TABLE isn’t supported.
> 		- Sharing:
> 		- Sharing with a listing isn’t currently supported
> 				- Direct sharing is supported
> - For writing to tables in a catalog-linked database:
> 	- Creating tables in nested namespaces isn’t currently supported.
> 		- Writing to tables in nested namespaces isn’t currently supported.
> 		- Position [row-level deletes](https://iceberg.apache.org/spec/#row-level-deletes) are supported for tables stored on Amazon S3, Azure, or Google Cloud. Row-level deletes with equality delete files aren’t supported. For more information about row-level deletes, see [Use row-level deletes](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-row-level-deletes). To turn off position deletes, which enable running the Data Manipulation Language (DML) operations in copy-on-write mode, set the `ICEBERG_MERGE_ON_READ_BEHAVIOR` parameter to `'DISABLED'` at the table, schema, or database level.

**Externally managed write support**

> - Snowflake supports externally managed writes for Iceberg tables that use version 2 or version 3 of the [Iceberg table specification](https://iceberg.apache.org/spec/).
> - Snowflake provides Data Definition Language (DDL) and Data Manipulation Language (DML) commands for externally managed tables. However, you configure metadata and data retention using your external catalog and the tools provided by your external storage provider. For more information, see [Tables that use an external catalog](https://docs.snowflake.com/user-guide/tables-iceberg-metadata#label-tables-iceberg-metadata-externally-managed).
> 	For writes, Snowflake ensures that changes are committed to your remote catalog before updating the table in Snowflake.
> - If you use a catalog-linked database, you can use the CREATE ICEBERG TABLE syntax with column definitions to create a table in Snowflake *and* in your remote catalog. If you use a standard Snowflake database (not linked to a catalog), you must first create a table in your remote catalog. After that, you can use the [CREATE ICEBERG TABLE (Iceberg REST catalog)](https://docs.snowflake.com/sql-reference/sql/create-iceberg-table-rest) syntax to create an Iceberg table in Snowflake and write to it.
> - For the AWS Glue Data Catalog: Dropping an externally managed table through Snowflake doesn’t delete the underlying table files. This behavior is specific to the AWS Glue Data Catalog implementation.
> - You can’t drop an Amazon S3 Table through Snowflake. The Amazon S3 Tables service requires the `purge` option to be specified with the DROP command, which Snowflake doesn’t currently support.
> - Position [row-level deletes](https://iceberg.apache.org/spec/#row-level-deletes) are supported for tables stored on Amazon S3, Azure, or Google Cloud. Row-level deletes with equality delete files aren’t supported. For more information about row-level deletes, see [Use row-level deletes](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-row-level-deletes). To turn off position deletes, which enable running the DML operations in copy-on-write mode, set the `ICEBERG_MERGE_ON_READ_BEHAVIOR` parameter to `'DISABLED'` at the table, schema, or database level.
> - Writing to externally managed tables with the following Iceberg data types isn’t supported:
> 	- `uuid`
> 		- `fixed(L)`
> - The following features aren’t currently supported when you use Snowflake to write to externally managed Iceberg tables:
> 	- Server-side encryption (SSE) for Azure external volumes.
> 		- Multi-statement transactions. Snowflake supports autocommit transactions only.
> 		- Conversion to Snowflake-managed tables.
> 		- External Iceberg catalogs that don’t conform to the Iceberg REST protocol.
> 		- Using the OR REPLACE option when creating a table.
> 		- Using the CREATE ICEBERG TABLE (catalog-linked database) … AS SELECT syntax if you use one of the following catalogs as your remote catalog:
> 		- AWS Glue
> 				- Databricks Unity Catalog
> 		Alternatively, you can use the [CREATE ICEBERG TABLE (Iceberg REST catalog)](https://docs.snowflake.com/sql-reference/sql/create-iceberg-table-rest) syntax to create an empty Iceberg table and then use an [INSERT INTO … SELECT](https://docs.snowflake.com/sql-reference/sql/insert) statement to insert data into the empty table. However, this alternative uses two separate transactions, so it doesn’t guarantee atomicity.
> - For creating schemas in a catalog-linked database, be aware of the following:
> 	- The CREATE SCHEMA command creates a corresponding namespace in your remote catalog only when you use a catalog-linked database.
> 		- The ALTER and CLONE options aren’t supported.
> 		- Delimiters aren’t supported for schema names. Only alphanumeric schema names are supported.
> - You can set a target file size for a table’s Parquet files. For more information, see [Set a target file size](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-target-file-size).
> - For Azure cloud storage services: Snowflake only supports externally managed writes for Iceberg tables that use the following services for external storage:
> 	- Blob Storage
> 		- Data Lake Storage Gen2
> 		Connecting Snowflake to Data Lake Storage Gen2 storage by using an external volume is in public preview. This configuration enables externally managed writes to catalogs that are only configured to use Data Lake Storage, such as Unity Catalog. For more information, see [Configure an external volume for Azure](https://docs.snowflake.com/user-guide/tables-iceberg-configure-external-volume-azure)
> 		> [!note] Note
> 		> Connecting Snowflake to Data Lake Storage Gen2 storage by using catalog-vended credentials isn’t supported.
> 		- General-purpose v1
> 		- General-purpose v2
> 		- Microsoft Fabric OneLake
> - Sharing:
> 	- Sharing with a listing isn’t currently supported.
> 		- Direct sharing isn’t currently supported.

**Access by third-party clients to Iceberg data, metadata**

> - Third-party clients can’t append to, delete from, or upsert data to Iceberg tables that use Snowflake as the catalog.

**Table optimization**

- Snowflake doesn’t support orphan file deletion for Snowflake-managed Iceberg tables. If you see a mismatch between storage usage for your external cloud storage and Snowflake, you might have orphan files in your external cloud storage. To see your storage usage for Snowflake, you can use the [TABLE\_STORAGE\_METRICS view](https://docs.snowflake.com/sql-reference/info-schema/table_storage_metrics) or [TABLE\_STORAGE\_METRICS view](https://docs.snowflake.com/sql-reference/account-usage/table_storage_metrics). If you see a mismatch, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support) for assistance with determining whether you have orphan files and removing them.
- For Snowflake-managed Iceberg tables, if a DML operation fails unexpectedly and rolls back, some Parquet files might get written to your external cloud storage but won’t be tracked or referenced by your Iceberg table metadata. These Parquet files are orphan files.

**External query engines through Snowflake Horizon Catalog**

This section lists the considerations for accessing, querying, and writing to Iceberg tables with an external query engine.

Consider the following items when you access Iceberg tables with an external query engine:

- Iceberg
	- For tables in Snowflake:
		- Only Snowflake-managed Iceberg tables are supported.
- Listings:
	- Iceberg tables that you share through [auto-fulfillment for listings](https://docs.snowflake.com/collaboration/provider-listings-auto-fulfillment) aren’t accessible through the consumer account’s Horizon Iceberg REST Catalog API.
- Network and private connectivity:
	- Using network policies that are set at the user level isn’t supported with this feature.
		- For [Snowflake-managed network rules](https://docs.snowflake.com/user-guide/network-rules#label-snowflake-managed-network-rules), egress IP addresses that are static aren’t supported.
		- Explicitly granting the Horizon Catalog endpoint access to your storage accounts isn’t supported. We recommend that you use private connectivity for secure connectivity from external engines to Horizon Catalog and from Horizon Catalog to your storage account.
- Clouds:
	- Commercial: This feature is only supported for Snowflake-managed Iceberg tables that are stored on Amazon S3, Google Cloud, or Microsoft Azure for all commercial cloud regions. S3-compatible non-AWS storage isn’t yet supported.
		- FedRAMP (Moderate): This feature is supported for Snowflake-managed Iceberg tables that are stored on FedRAMP (Moderate) deployments on AWS Commercial Gov (US) in the us-east-1 and us-west-2 regions.
		- For Iceberg tables stored on Amazon S3:
		- If you want to use SSE-KMS encryption, contact customer support or your account team for assistance with enabling access.
		- Reading and writing Iceberg v3 tables via the Horizon Iceberg REST Catalog API is supported for customer-managed and Snowflake-managed storage.
		- For Iceberg tables stored on Azure:
		- If you want to use Azure Virtual Network (VNet) for connectivity, contact customer support or your account team for assistance.

Consider the following items when you query (read) Iceberg tables with an external query engine:

- Iceberg
	- Querying the following tables isn’t supported:
		- Remote tables
				- Snowflake native tables
				- Externally managed Iceberg tables including Delta-based Iceberg tables and Snowflake-managed Iceberg tables that you loaded with data from Iceberg-compatible Parquet data files by using the COPY INTO table command
		- Reading Iceberg v2 and v3 tables is supported.
- Access control:
	- Tables protected by the following fine-grained data policies can be accessed over Apache Spark™ through Snowflake Horizon Catalog:
		- Masking policies
				- Tag-based masking policies
				- Row access policies
		For more information, see [Enforce data protection policies when querying Apache Iceberg™ tables from Apache Spark™](https://docs.snowflake.com/user-guide/tables-iceberg-query-using-external-query-engine-snowflake-horizon-enforce-access-policies).
- Cloned and converted tables:
	- Reading and writing cloned or converted tables is not supported with vended credentials. To read these tables, use direct access to object storage.

Consider the following items when you write to Iceberg tables with an external query engine:

- Table operations:
	- You can’t specify a base location with your CREATE TABLE statement.
		When you create a Snowflake-managed table without specifying a base location, Snowflake constructs the following path for your table: `STORAGE_BASE_URL/*database*/*schema*/*table_name*.*randomId*/[data | metadata]/`
		- CREATE TABLE AS SELECT (CTAS) from an external engine is not supported.
		- Equality deletes aren’t supported.
		- Creating Iceberg tags and branches isn’t supported.
		- Writing to dynamic tables in Snowflake isn’t supported.
		- Writing to shared Iceberg tables isn’t supported.
		- Registering Iceberg tables isn’t supported.
- Maintenance operations:
	- You can’t roll back a table to a previous snapshot.
		- You can’t upgrade an Iceberg table from v2 to v3.
- Cloned and converted tables:
	- Writing to cloned or converted tables is not supported with vended credentials. To write to these tables, connect your external query engine directly to the object storage where your tables are stored.
		- You can’t write to an Iceberg table that was converted from externally managed to Snowflake managed.
- Streams:
	- On Iceberg v2 tables, deletes or updates that result in copy-on-write or merge-on-read operations can cause standard streams to represent an updated or relocated row as a DELETE record followed by an INSERT record for the same row.
- Fine-grained access control policies:
	- Writing to tables that have fine-grained access control policies or tags isn’t supported.

**Native App Framework**

> You can share Iceberg tables with consumers through the [Snowflake Native App Framework](https://docs.snowflake.com/developer-guide/native-apps/native-apps-about). Be aware of the following restrictions:
> 
> - Iceberg tables shared through a Native App are read-only for consumers.
> - Cross-Cloud Auto-Fulfillment is not supported for apps that share Iceberg tables.
> - Consumers must explicitly enable the `EXTERNAL_DATA` restricted feature to the app before it can resolve Iceberg tables. For more information, see [Request access to external and Apache Iceberg™ tables](https://docs.snowflake.com/developer-guide/native-apps/requesting-external-tables).

**Unsupported features**

> The following Snowflake features aren’t currently supported for all Iceberg tables:
> 
> - [Collation](https://docs.snowflake.com/sql-reference/collation)
> - [Fail-safe](https://docs.snowflake.com/user-guide/data-failsafe)
> - [Hybrid tables](https://docs.snowflake.com/user-guide/tables-hybrid)
> - Snowflake encryption
> - [Snowflake schema evolution](https://docs.snowflake.com/user-guide/data-load-schema-evolution)
> - [Tagging](https://docs.snowflake.com/user-guide/object-tagging/introduction) using the [ASSOCIATE\_SEMANTIC\_CATEGORY\_TAGS](https://docs.snowflake.com/sql-reference/stored-procedures/associate_semantic_category_tags) stored procedure
> - [Temporary and transient tables](https://docs.snowflake.com/user-guide/tables-temp-transient)
> 
> The following features aren’t supported for externally managed Iceberg tables:
> 
> - [Cloning](https://docs.snowflake.com/user-guide/tables-storage-considerations#label-cloning-tables)
> - [Clustering](https://docs.snowflake.com/user-guide/tables-clustering-micropartitions)
> - Standard and append-only [streams](https://docs.snowflake.com/user-guide/streams-intro). Insert-only streams are supported.
> - [Replication](https://docs.snowflake.com/user-guide/account-replication-intro) of Iceberg tables, external volumes, or catalog integrations