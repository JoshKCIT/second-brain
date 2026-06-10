---
source_url: https://docs.snowflake.com/en/sql-reference/sql/create-schema
vendor: snowflake
topic: schema
fetched_at: 2026-06-10T06:43:27Z
revalidate_after: 2026-07-10T06:43:27Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## CREATE SCHEMA

Creates a new schema in the current database.

This command supports the following variants:

- [Variant syntax](#label-create-or-alter-schema-syntax): Creates a schema if it doesn’t exist or alters an existing schema.
- [CREATE SCHEMA … CLONE](#label-create-schema-clone-syntax): Creates a clone of an existing schema, either at its current state or at a specific time/point in the past (using Time Travel). For more information about cloning a schema, see [Cloning considerations](https://docs.snowflake.com/user-guide/object-clone).
- [CREATE SCHEMA … FROM BACKUP SET](#label-create-schema-from-backup-set-syntax) (restores a schema from a backup under a new name)

See also:

[ALTER SCHEMA](https://docs.snowflake.com/sql-reference/sql/alter-schema), [DESCRIBE SCHEMA](https://docs.snowflake.com/sql-reference/sql/desc-schema), [DROP SCHEMA](https://docs.snowflake.com/sql-reference/sql/drop-schema), [SHOW SCHEMAS](https://docs.snowflake.com/sql-reference/sql/show-schemas), [UNDROP SCHEMA](https://docs.snowflake.com/sql-reference/sql/undrop-schema)

[CREATE OR ALTER <object>](https://docs.snowflake.com/sql-reference/sql/create-or-alter)

## Syntax

```
CREATE [ OR REPLACE ] [ TRANSIENT ] SCHEMA [ IF NOT EXISTS ] <name>
  [ CLONE <source_schema>
      [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> } ) ]
      [ IGNORE TABLES WITH INSUFFICIENT DATA RETENTION ]
      [ IGNORE HYBRID TABLES ] ]
  [ WITH MANAGED ACCESS ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ EXTERNAL_VOLUME = <external_volume_name> ]
  [ CATALOG = <catalog_integration_name> ]
  [ ICEBERG_VERSION_DEFAULT = <integer> ]
  [ ICEBERG_MERGE_ON_READ_BEHAVIOR = { 'AUTO' | 'ENABLED' | 'DISABLED' } ]
  [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
  [ REPLACE_INVALID_CHARACTERS = { TRUE | FALSE } ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
  [ STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED } ]
  [ CLASSIFICATION_PROFILE = '<classification_profile>' ]
  [ COMMENT = '<string_literal>' ]
  [ CATALOG_SYNC = '<snowflake_open_catalog_integration_name>' ]
  [ OBJECT_VISIBILITY = PRIVILEGED ]
  [ ENABLE_DATA_COMPACTION = { TRUE | FALSE } ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]
```

**Restored schema (from a backup)**

```
CREATE SCHEMA <name> FROM BACKUP SET <backup_set> IDENTIFIER '<backup_id>'
```

## Variant syntax

### CREATE OR ALTER SCHEMA

Creates a new schema if it doesn’t already exist, or transforms an existing schema into the schema defined in the statement. A CREATE OR ALTER SCHEMA statement follows the syntax rules of a CREATE SCHEMA statement and has the same limitations as an [ALTER SCHEMA](https://docs.snowflake.com/sql-reference/sql/alter-schema) statement.

For more information, see [CREATE OR ALTER SCHEMA usage notes](#label-create-or-alter-schema-usage-notes).

```
CREATE OR ALTER [ TRANSIENT ] SCHEMA <name>
  [ WITH MANAGED ACCESS ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ EXTERNAL_VOLUME = <external_volume_name> ]
  [ CATALOG = <catalog_integration_name> ]
  [ ICEBERG_VERSION_DEFAULT = <integer> ]
  [ ICEBERG_MERGE_ON_READ_BEHAVIOR = { 'AUTO' | 'ENABLED' | 'DISABLED' } ]
  [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
  [ REPLACE_INVALID_CHARACTERS = { TRUE | FALSE } ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
  [ LOG_LEVEL = '<log_level>' ]
  [ TRACE_LEVEL = '<trace_level>' ]
  [ STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED } ]
  [ COMMENT = '<string_literal>' ]
  [ OBJECT_VISIBILITY = PRIVILEGED ]
```

### CREATE SCHEMA … CLONE

Creates a new schema with the same parameter values:

> ```
> CREATE [ OR REPLACE ] SCHEMA [ IF NOT EXISTS ] <name> CLONE <source_schema>
>   [ ... ]
> ```

For more details, see [CREATE <object> … CLONE](https://docs.snowflake.com/sql-reference/sql/create-clone).

## Required parameters

`*name*`

Specifies the identifier for the schema; must be unique for the database in which the schema is created.

In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

For more details, see [Identifier requirements](https://docs.snowflake.com/sql-reference/identifiers-syntax).

## Optional parameters

`TRANSIENT`

Specifies a schema as transient. Transient schemas do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss. For more information, see [Understanding and viewing Fail-safe](https://docs.snowflake.com/user-guide/data-failsafe).

In addition, by definition, all tables created in a transient schema are transient. For more information about transient tables, see [CREATE TABLE](https://docs.snowflake.com/sql-reference/sql/create-table).

Default: No value (i.e. schema is permanent)

`CLONE *source_schema*`

Specifies to create a clone of the specified source schema. For more details about cloning a schema, see [CREATE <object> … CLONE](https://docs.snowflake.com/sql-reference/sql/create-clone).

`AT | BEFORE ( TIMESTAMP => *timestamp* | OFFSET => *time_difference* | STATEMENT => *id* )`

When cloning a schema, the [AT | BEFORE](https://docs.snowflake.com/sql-reference/constructs/at-before) clause specifies to use Time Travel to clone the schema at or before a specific point in the past.

`IGNORE TABLES WITH INSUFFICIENT DATA RETENTION`

> Ignore tables that no longer have historical data available in Time Travel to clone. If the time in the past specified in the AT | BEFORE clause is beyond the data retention period for any child table in a database or schema, skip the cloning operation for the child table. For more information, see [Child Objects and Data Retention Time](https://docs.snowflake.com/user-guide/object-clone#label-child-objects-and-data-retention-time).

`IGNORE HYBRID TABLES`

Ignore hybrid tables, which will not be cloned. Use this option to clone a schema that contains hybrid tables. The cloned schema includes other objects but skips hybrid tables.

If you don’t use this option and your schema contains one or more hybrid tables, the command ignores hybrid tables silently. However, the error handling for schemas that contain hybrid tables will change in an upcoming release; therefore, you may want to add this parameter to your commands preemptively.

`WITH MANAGED ACCESS`

Specifies a managed schema. Managed access schemas centralize privilege management with the schema owner.

In regular schemas, the owner of an object (i.e. the role that has the OWNERSHIP privilege on the object) can grant further privileges on their objects to other roles. In managed schemas, the schema owner manages all privilege grants, including [future grants](https://docs.snowflake.com/user-guide/security-access-control-configure#label-granting-future-privs-on-schema-objects), on objects in the schema. Object owners retain the OWNERSHIP privileges on the objects; however, only the schema owner can manage privilege grants on the objects.

`DATA_RETENTION_TIME_IN_DAYS = *integer*`

Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the default Time Travel retention time for all tables created in the schema. For more details, see [Understanding & using Time Travel](https://docs.snowflake.com/user-guide/data-time-travel).

For a detailed description of this object-level parameter, as well as more information about object parameters, see [Parameters](https://docs.snowflake.com/sql-reference/parameters). For more information about table-level retention time, see [CREATE TABLE](https://docs.snowflake.com/sql-reference/sql/create-table) and [Understanding & using Time Travel](https://docs.snowflake.com/user-guide/data-time-travel).

Values:

> - Standard Edition: `0` or `1`
> - Enterprise Edition:
> 	- `0` to `90` for permanent schemas
> 		- `0` or `1` for transient schemas

Default:

> - Standard Edition: `1`
> - Enterprise Edition (or higher): `1` (unless a different default value was specified at the database or account level)

> [!note] Note
> A value of `0` effectively disables Time Travel for the schema.

`MAX_DATA_EXTENSION_TIME_IN_DAYS = *integer*`

Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for tables in the schema to prevent streams on the tables from becoming stale.

For a detailed description of this parameter, see [MAX\_DATA\_EXTENSION\_TIME\_IN\_DAYS](https://docs.snowflake.com/sql-reference/parameters#label-max-data-extension-time-in-days).

`EXTERNAL_VOLUME = *external_volume_name*`

Object parameter that specifies the default external volume to use for [Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg).

For more information about this parameter, see [EXTERNAL\_VOLUME](https://docs.snowflake.com/sql-reference/parameters#label-external-volume).

`CATALOG = *catalog_integration_name*`

Object parameter that specifies the default catalog integration to use for [Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg).

For more information about this parameter, see [CATALOG](https://docs.snowflake.com/sql-reference/parameters#label-catalog).

`ICEBERG_VERSION_DEFAULT = integer`

Specifies the version of the Apache Iceberg™ table specification that Iceberg tables conform to.

Values:

`2`: New tables conform with Iceberg version 2.

`3`: New tables conform with Iceberg version 3.

> [!caution] Caution
> Before you use other engines to upgrade an Iceberg tables format-version in table properties to v3, ensure that the table isn’t used by engines or applications that don’t yet support v3. Downgrading format versions isn’t supported in the Apache Iceberg specification. Therefore, all readers and writers must support v3. The default version for Iceberg tables in Snowflake is v2, which can be configured to v3 if needed. Using Snowflake to perform in-place version upgrades isn’t supported at this time.

Default:

`2`

For more information about this parameter, see [ICEBERG\_VERSION\_DEFAULT](https://docs.snowflake.com/sql-reference/parameters#label-iceberg-version-default).

`ICEBERG_MERGE_ON_READ_BEHAVIOR = { 'AUTO' | 'ENABLED' | 'DISABLED' }`

Specifies how Snowflake performs row-level updates (UPDATE, DELETE, MERGE) on Apache Iceberg™ tables. Selects between merge-on-read (which writes Iceberg delete files alongside the data) and copy-on-write (which rewrites entire data files).

The parameter values are case-insensitive.

Values:

`'AUTO'`: Snowflake selects merge-on-read or copy-on-write based on the table’s Iceberg format version and management mode. For details, see [ICEBERG\_MERGE\_ON\_READ\_BEHAVIOR parameter](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-iceberg-merge-on-read-behavior).

`'ENABLED'`: Merge-on-read is enabled for all Apache Iceberg™ tables to which this parameter applies, regardless of format version or management mode.

`'DISABLED'`: Merge-on-read is disabled for all Apache Iceberg™ tables to which this parameter applies. All DML uses copy-on-write.

Default:

`'AUTO'`

For a detailed description of this parameter, see [ICEBERG\_MERGE\_ON\_READ\_BEHAVIOR parameter](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-iceberg-merge-on-read-behavior). For more information about merge-on-read and copy-on-write behavior in Snowflake, see [Use row-level deletes](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-row-level-deletes).

`ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE }`

> [!warning] Warning
> This parameter is deprecated. Use [`ICEBERG_MERGE_ON_READ_BEHAVIOR`](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-iceberg-merge-on-read-behavior) instead. The legacy parameter is still honored when `ICEBERG_MERGE_ON_READ_BEHAVIOR` is at its default (`'AUTO'`), but it will return an error in a future release.

Specifies whether to enable merge-on-read behavior for Apache Iceberg™ tables.

Values:

`TRUE`: New tables use merge-on-read behavior. For **v2** tables, Snowflake uses positional delete files for row-level deletes. For **v3** tables, Snowflake uses deletion vectors when conditions are met.

**Note:** Setting this parameter to `TRUE` does **not** enable merge-on-read for Snowflake-managed v2 Iceberg tables. When `ICEBERG_MERGE_ON_READ_BEHAVIOR` is at its default (`'AUTO'`), this setting routes through the auto matrix, which keeps Snowflake-managed v2 tables on copy-on-write. To enable merge-on-read for Snowflake-managed v2 tables, set `ICEBERG_MERGE_ON_READ_BEHAVIOR = 'ENABLED'` explicitly.

`FALSE`: New tables use copy-on-write behavior.

Default:

`TRUE`

For a detailed description of this parameter, see [Deprecated: ENABLE\_ICEBERG\_MERGE\_ON\_READ](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-enable-iceberg-merge-on-read). For more information about merge-on-read and copy-on-write behavior in Snowflake, see [Use row-level deletes](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-row-level-deletes).

`REPLACE_INVALID_CHARACTERS = { TRUE | FALSE }`

Specifies whether to replace invalid UTF-8 characters with the Unicode replacement character (�) in query results for an [Iceberg table](https://docs.snowflake.com/sql-reference/sql/create-iceberg-table). You can only set this parameter for tables that use an external Iceberg catalog.

- `TRUE` replaces invalid UTF-8 characters with the Unicode replacement character.
- `FALSE` leaves invalid UTF-8 characters unchanged. Snowflake returns a user error message when it encounters invalid UTF-8 characters in a Parquet data file.

Default: `FALSE`

`DEFAULT_DDL_COLLATION = '*collation_specification*'`

Specifies a default [collation specification](https://docs.snowflake.com/sql-reference/collation#label-collation-specification) for all tables added to the schema. The default can be overridden at the individual table level.

For more details about the parameter, see [DEFAULT\_DDL\_COLLATION](https://docs.snowflake.com/sql-reference/parameters#label-default-ddl-collation).

`LOG_LEVEL = '*log_level*'`

Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at the specified level (and at more severe levels) are ingested.

For more information about levels, see [LOG\_LEVEL](https://docs.snowflake.com/sql-reference/parameters#label-log-level). For information about setting log level, see [Setting levels for logging, metrics, and tracing](https://docs.snowflake.com/developer-guide/logging-tracing/telemetry-levels).

`TRACE_LEVEL = '*trace_level*'`

Controls how trace events are ingested into the event table.

For information about levels, see [TRACE\_LEVEL](https://docs.snowflake.com/sql-reference/parameters#label-trace-level). For information about setting trace level, see [Setting levels for logging, metrics, and tracing](https://docs.snowflake.com/developer-guide/logging-tracing/telemetry-levels).

`STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED }`

Specifies the storage serialization policy for [Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg) that use Snowflake as the catalog.

- `COMPATIBLE`: Snowflake performs encoding and compression of data files that ensures interoperability with third-party compute engines.
- `OPTIMIZED`: Snowflake performs encoding and compression of data files that ensures the best table performance within Snowflake.

Default: `OPTIMIZED`

`CLASSIFICATION_PROFILE = '*classification_profile*'`

Associates the schema with a classification profile so that sensitive data in the schema is [automatically classified](https://docs.snowflake.com/user-guide/classify-auto).

`COMMENT = '*string_literal*'`

Specifies a comment for the schema.

Default: No value

`CATALOG_SYNC = '*snowflake_open_catalog_integration_name*'`

Specifies the name of a catalog integration configured for [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview). If specified, Snowflake syncs Snowflake-managed Apache Iceberg™ tables in the schema with an external catalog in your Snowflake Open Catalog account. For more information about syncing Snowflake-managed Iceberg tables with Open Catalog, see [Sync a Snowflake-managed table with Snowflake Open Catalog](https://docs.snowflake.com/user-guide/tables-iceberg-open-catalog-sync).

For more information about this parameter, see [CATALOG\_SYNC](https://docs.snowflake.com/sql-reference/parameters#label-catalog-sync).

Default: No value

`ENABLE_DATA_COMPACTION = { TRUE | FALSE }`

Specifies whether Snowflake should enable data compaction on Snowflake-managed [Apache Iceberg™ tables](https://docs.snowflake.com/user-guide/tables-iceberg).

- `TRUE`: Snowflake performs data compaction on the tables.
- `FALSE`: Snowflake doesn’t perform data compaction on the tables.

Default: `TRUE`

For more information, see [ENABLE\_DATA\_COMPACTION](https://docs.snowflake.com/sql-reference/parameters#label-enable-data-compaction) and [Set data compaction](https://docs.snowflake.com/user-guide/tables-iceberg-manage#label-tables-iceberg-manage-set-data-compaction).

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`

Associate the new object with one or more [contacts](https://docs.snowflake.com/user-guide/contacts-using).

Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`

Specifies the [tag](https://docs.snowflake.com/user-guide/object-tagging/introduction) name and the tag string value.

The tag value is always a string, and the maximum number of characters for the tag value is 256.

For information about specifying tags in a statement, see [Tag quotas](https://docs.snowflake.com/user-guide/object-tagging/introduction#label-object-tagging-quota).

`OBJECT_VISIBILITY = PRIVILEGED`

> Specifies the visibility of objects in the account, which controls the [discoverability of the objects](https://docs.snowflake.com/user-guide/ui-snowsight/object-visibility-universal-search) and enables users without explicit access privileges to find objects and request access. For examples, see [Examples](https://docs.snowflake.com/user-guide/ui-snowsight/object-visibility-universal-search#label-object-visibility-examples).
> 
> - `PRIVILEGED`: Specifies that only roles within the current account that are granted an explicit privilege on the object can see the object. This is the default behavior in Snowflake.
> 
> For examples, see [Make database objects discoverable in Universal Search](https://docs.snowflake.com/user-guide/ui-snowsight/object-visibility-universal-search#label-object-visibility-examples).

## Backup parameters

The FROM BACKUP SET clause restores a schema from a backup. You don’t specify other schema properties because they’re all the same as in the backed-up schema.

> [!note] Note
> The FROM SNAPSHOT SET clause is deprecated. Use FROM BACKUP SET instead.

This form doesn’t have a CREATE OR REPLACE clause. You typically either restore the schema under a new name and recover any data or other objects from this new schema, or rename the original schema and then restore the schema under the original name.

> [!note] Note
> The restored schema is independent of the original schema from the backup. There isn’t any cloning relationship between the restored and original schemas. Therefore, all the micro-partitions in the restored schema are owned by that schema.
> 
> If you want to make backups of the newly restored schema, create a new backup set for it.

For more information about backups, see [Backups for disaster recovery and immutable storage](https://docs.snowflake.com/user-guide/backups).

`*backup_set*`

Specifies the name of a backup set created for a specific schema. You can use the SHOW BACKUP SETS command to locate the right backup set.

`*backup_id*`

Specifies the identifier of a specific backup within that backup set. You can use the SHOW BACKUPS IN BACKUP SET command to locate the right identifier within the backup set, based on the creation date and time for the backup.

## Access control requirements

A [role](https://docs.snowflake.com/user-guide/security-access-control-overview#label-access-control-overview-roles) used to execute this operation must have the following [privileges](https://docs.snowflake.com/user-guide/security-access-control-overview#label-access-control-overview-privileges) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SCHEMA | Database | Can create both regular and [managed access](https://docs.snowflake.com/user-guide/security-access-control-configure#label-managed-access-schemas) schemas. |
| CREATE SCHEMA … CLONE … WITH MANAGED ACCESS | Options | The required privileges depends on whether the source schema is managed or unmanaged:  - Managed: OWNERSHIP on the source schema. - Unmanaged: MANAGE GRANTS ON ACCOUNT and USAGE on the source schema. |
| USAGE | External volume, catalog integration | Required if setting the `EXTERNAL_VOLUME` or `CATALOG` object parameters, respectively. |
| MANAGE VISIBILITY | Account | Required to set the OBJECT\_VISIBILITY property. Only the SECURITYADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |
| MODIFY LOG LEVEL | Account | Required to set the LOG\_LEVEL for a schema. |
| MODIFY TRACE LEVEL | Account | Required to set the TRACE\_LEVEL for a schema. |
| OWNERSHIP | Schema | Required only when executing a [Variant syntax](#label-create-or-alter-schema-syntax) statement for an existing schema.  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](https://docs.snowflake.com/sql-reference/sql/grant-ownership) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](https://docs.snowflake.com/user-guide/security-access-control-configure#label-security-custom-role).

For general information about roles and privilege grants for performing SQL actions on [securable objects](https://docs.snowflake.com/user-guide/security-access-control-overview#label-access-control-securable-objects), see [Overview of Access Control](https://docs.snowflake.com/user-guide/security-access-control-overview).

## General usage notes

- Creating a schema automatically sets it as the active/current schema for the current session (equivalent to using the [USE SCHEMA](https://docs.snowflake.com/sql-reference/sql/use-schema) command for the schema).
- If a schema with the same name already exists in the database, an error is returned and the schema is not created, unless the optional `OR REPLACE` keyword is specified in the command.
	> [!important] Important
	> Using `OR REPLACE` is the equivalent of using [DROP SCHEMA](https://docs.snowflake.com/sql-reference/sql/drop-schema) on the existing schema and then creating a new schema with the same name; however, the dropped schema is not permanently removed from the system. Instead, it is retained in Time Travel. This is important because dropped schemas in Time Travel contribute to data storage for your account. For more information, see [Storage costs for Time Travel and Fail-safe](https://docs.snowflake.com/user-guide/data-cdp-storage-costs).

- The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
- CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

- In a managed access schema, the schema owner manages grants on the contained objects (e.g. tables or views) but has no other privileges (USAGE, SELECT, DROP, etc.) on the objects.
- In a [catalog-linked database](https://docs.snowflake.com/user-guide/tables-iceberg-catalog-linked-database), this command creates a namespace in your linked Iceberg REST catalog and a corresponding schema in your Snowflake database. For this use case, Snowflake supports only the following options:
	- CLASSIFICATION\_PROFILE
		- COMMENT
		- STORAGE\_SERIALIZATION\_POLICY
		- TAG
		- WITH CONTACT
		- WITH MANAGED ACCESS
	The CREATE OR ALTER and CLONE variants aren’t supported.
- Regarding metadata:
	> [!note] Attention
	> Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](https://docs.snowflake.com/sql-reference/metadata).

## CREATE OR ALTER SCHEMA usage notes

- All limitations of the [ALTER SCHEMA](https://docs.snowflake.com/sql-reference/sql/alter-schema) command apply.
- This command does *not* support the following:
	- Swapping schemas using the SWAP WITH parameter.
		- Renaming a schema using the RENAME TO parameter.
		- Creating a clone of a schema using the CLONE parameter.
		- Adding or changing tags and policies. Any existing tags and policies are preserved.
		- Converting a TRANSIENT schema to a non-TRANSIENT schema, or vice versa.

## Examples

Create a permanent schema:

> ```sql
> CREATE SCHEMA myschema;
> 
> SHOW SCHEMAS;
> 
> +-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+---------+----------------+
> | created_on                    | name               | is_default | is_current | database_name | owner        | comment                                                   | options | retention_time |
> |-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+---------+----------------|
> | 2018-12-10 09:34:02.127 -0800 | INFORMATION_SCHEMA | N          | N          | MYDB          |              | Views describing the contents of schemas in this database |         | 1              |
> | 2018-12-10 09:33:56.793 -0800 | MYSCHEMA           | N          | Y          | MYDB          | PUBLIC       |                                                           |         | 1              |
> | 2018-11-26 06:08:24.263 -0800 | PUBLIC             | N          | N          | MYDB          | PUBLIC       |                                                           |         | 1              |
> +-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+---------+----------------+
> ```

Create a transient schema:

> ```sql
> CREATE TRANSIENT SCHEMA tschema;
> 
> SHOW SCHEMAS;
> 
> +-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+-----------+----------------+
> | created_on                    | name               | is_default | is_current | database_name | owner        | comment                                                   | options   | retention_time |
> |-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+-----------+----------------|
> | 2018-12-10 09:34:02.127 -0800 | INFORMATION_SCHEMA | N          | N          | MYDB          |              | Views describing the contents of schemas in this database |           | 1              |
> | 2018-12-10 09:33:56.793 -0800 | MYSCHEMA           | N          | Y          | MYDB          | PUBLIC       |                                                           |           | 1              |
> | 2018-11-26 06:08:24.263 -0800 | PUBLIC             | N          | N          | MYDB          | PUBLIC       |                                                           |           | 1              |
> | 2018-12-10 09:35:32.326 -0800 | TSCHEMA            | N          | Y          | MYDB          | PUBLIC       |                                                           | TRANSIENT | 1              |
> +-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+-----------+----------------+
> ```

Create a managed access schema:

> ```sql
> CREATE SCHEMA mschema WITH MANAGED ACCESS;
> 
> SHOW SCHEMAS;
> 
> +-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+----------------+----------------+
> | created_on                    | name               | is_default | is_current | database_name | owner        | comment                                                   | options        | retention_time |
> |-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+----------------+----------------|
> | 2018-12-10 09:34:02.127 -0800 | INFORMATION_SCHEMA | N          | N          | MYDB          |              | Views describing the contents of schemas in this database |                | 1              |
> | 2018-12-10 09:36:47.738 -0800 | MSCHEMA            | N          | Y          | MYDB          | ROLE1        |                                                           | MANAGED ACCESS | 1              |
> | 2018-12-10 09:33:56.793 -0800 | MYSCHEMA           | N          | Y          | MYDB          | PUBLIC       |                                                           |                | 1              |
> | 2018-11-26 06:08:24.263 -0800 | PUBLIC             | N          | N          | MYDB          | PUBLIC       |                                                           |                | 1              |
> | 2018-12-10 09:35:32.326 -0800 | TSCHEMA            | N          | Y          | MYDB          | PUBLIC       |                                                           | TRANSIENT      | 1              |
> +-------------------------------+--------------------+------------+------------+---------------+--------------+-----------------------------------------------------------+----------------+----------------+
> ```

## CREATE OR ALTER SCHEMA examples

### Create a simple schema

Create a schema named `s1`:

```sql
CREATE OR ALTER SCHEMA s1;
```

Create or alter schema `s1` and set properties and parameters:

```sql
CREATE OR ALTER SCHEMA s1
  WITH MANAGED ACCESS
  DATA_RETENTION_TIME_IN_DAYS = 5
  DEFAULT_DDL_COLLATION = 'de';
```

### Unset a parameter previously set on schema

The [absence of a previously set parameter](https://docs.snowflake.com/sql-reference/sql/create-or-alter#label-create-or-alter-usage-notes) in the modified schema definition results in unsetting it. In the following example, turn off managed access for the schema `s1` created in the previous example:

```sql
CREATE OR ALTER SCHEMA s1
  DATA_RETENTION_TIME_IN_DAYS = 5
  DEFAULT_DDL_COLLATION = 'de';
```