---
source_url: https://docs.snowflake.com/en/sql-reference/sql/create-alert
vendor: snowflake
topic: alerts
fetched_at: 2026-06-10T06:43:52Z
revalidate_after: 2026-07-10T06:43:52Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## CREATE ALERT

Creates a new [alert](https://docs.snowflake.com/user-guide/alerts) in the current schema.

This command supports the following variants:

- [CREATE OR ALTER ALERT](#label-create-or-alter-alert-syntax): Creates an alert if it doesn’t exist or alters an existing alert.
- [CREATE ALERT … CLONE](#label-create-alert-clone-syntax): Creates a clone of an existing alert.

See also:

[ALTER ALERT](https://docs.snowflake.com/sql-reference/sql/alter-alert), [DESCRIBE ALERT](https://docs.snowflake.com/sql-reference/sql/desc-alert), [DROP ALERT](https://docs.snowflake.com/sql-reference/sql/drop-alert), [SHOW ALERTS](https://docs.snowflake.com/sql-reference/sql/show-alerts), [EXECUTE ALERT](https://docs.snowflake.com/sql-reference/sql/execute-alert)

[CREATE OR ALTER <object>](https://docs.snowflake.com/sql-reference/sql/create-or-alter)

> [!important] Important
> Newly created or cloned alerts are suspended upon creation. For information on resuming suspended alerts, see [Suspending and resuming an alert](https://docs.snowflake.com/user-guide/alerts#label-alerts-suspend-resume).

## Syntax

```
CREATE [ OR REPLACE ] ALERT [ IF NOT EXISTS ] <name>
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ SCHEDULE = '{ <num> MINUTE | USING CRON <expr> <time_zone> }' ]
  [ WAREHOUSE = <warehouse_name> ]
  [ COMMENT = '<string_literal>' ]
  [ CONFIG = '<configuration_string>' ]
  [ RUNBOOK = '<string_literal>' ]
  [ SUSPEND_ALERT_AFTER_NUM_FAILURES = <number> ]
  IF( EXISTS(
    <condition>
  ))
  THEN
    <action>
```

## Variant syntax

### CREATE OR ALTER ALERT

Creates a new alert if it doesn’t already exist, or transforms an existing alert into the alert defined in the statement. A CREATE OR ALTER ALERT statement follows the syntax rules of a CREATE ALERT statement and has the same limitations as an [ALTER ALERT](https://docs.snowflake.com/sql-reference/sql/alter-alert) statement.

For more information, see [CREATE OR ALTER ALERT usage notes](#label-create-or-alter-alert-usage-notes).

```
CREATE OR ALTER ALERT <name>
  [ SCHEDULE = '{ <num> MINUTE | USING CRON <expr> <time_zone> }' ]
  [ WAREHOUSE = <warehouse_name> ]
  [ COMMENT = '<string_literal>' ]
  [ CONFIG = '<configuration_string>' ]
  [ RUNBOOK = '<string_literal>' ]
  [ SUSPEND_ALERT_AFTER_NUM_FAILURES = <number> ]
  IF( EXISTS(
    <condition>
  ))
  THEN
    <action>
```

### CREATE ALERT … CLONE

Creates a new alert with the same parameter values:

> ```
> CREATE [ OR REPLACE ] ALERT <name> CLONE <source_alert>
>   [ ... ]
> ```

For more details, see [CREATE <object> … CLONE](https://docs.snowflake.com/sql-reference/sql/create-clone).

> [!note] Note
> When you clone an alert by using CREATE ALERT <name> CLONE or by cloning a schema or database containing the alert, the new alert has all of the properties of the original alert except for any properties that you explicitly override.

## Required parameters

`*name*`

String that specifies the identifier (i.e. name) for the alert; must be unique for the schema in which the alert is created.

In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

For more details, see [Identifier requirements](https://docs.snowflake.com/sql-reference/identifiers-syntax).

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`

Specifies the [tag](https://docs.snowflake.com/user-guide/object-tagging/introduction) name and the tag string value.

The tag value is always a string, and the maximum number of characters for the tag value is 256.

For information about specifying tags in a statement, see [Tag quotas](https://docs.snowflake.com/user-guide/object-tagging/introduction#label-object-tagging-quota).

`IF( EXISTS( *condition* ))`

The SQL statement that represents the condition for the alert. You can use the following commands:

- [SELECT](https://docs.snowflake.com/sql-reference/sql/select)
- [SHOW <objects>](https://docs.snowflake.com/sql-reference/sql/show)
- [CALL](https://docs.snowflake.com/sql-reference/sql/call)

If the statement returns one or more rows, the action for the alert is executed.

`THEN *action*`

The SQL statement that should be executed if the condition returns one or more rows.

To send a notification, you can [call the SYSTEM$SEND\_EMAIL or SYSTEM$SEND\_SNOWFLAKE\_NOTIFICATION stored procedure](https://docs.snowflake.com/user-guide/notifications/about-notifications).

## Optional parameters

`WAREHOUSE = warehouse_name`

Specifies the [virtual warehouse](https://docs.snowflake.com/user-guide/warehouses) that provides compute resources for executing this alert.

> [!note] Note
> For [serverless alerts](https://docs.snowflake.com/user-guide/alerts#label-alerts-serverless-compute), do not set this property.

`SCHEDULE ...`

Specifies the schedule for periodically evaluating the condition for the alert on a schedule.

When you create an alert, omitting this parameter or setting it to NULL creates an [alert on new data](https://docs.snowflake.com/user-guide/alerts#label-alerts-type-streaming).

For alerts on a schedule, you can specify the schedule in one of the following ways:

- `USING CRON *expr* *time_zone*`
	Specifies a cron expression and time zone for periodically evaluating the condition for the alert. Supports a subset of standard cron utility syntax.
	The cron expression consists of the following fields:
	```bash
	# __________ minute (0-59)
	# | ________ hour (0-23)
	# | | ______ day of month (1-31, or L)
	# | | | ____ month (1-12, JAN-DEC)
	# | | | | _ day of week (0-6, SUN-SAT, or L)
	# | | | | |
	# | | | | |
	  * * * * *
	```
	The following special characters are supported:
	| Special Character | Description |
	| --- | --- |
	| `*` | Wildcard. When specified for a given field, the alert runs at every unit of time for that field.  For example, `*` in the month field specifies that the alert runs every month. |
	| `L` | Stands for “last”. When used in the day-of-week field, it allows you to specify constructs such as “the last Friday” (“5L”) of a given month. In the day-of-month field, it specifies the last day of the month. |
	| `/*n*` | Indicates the `*n*` th instance of a given unit of time. Each quanta of time is computed independently.  For example, if `4/3` is specified in the month field, then the evaluation of the condition is scheduled for April, July and October (i.e. every 3 months, starting with the 4th month of the year).  The same schedule is maintained in subsequent years. That is, the condition is not scheduled to be evaluated in January (3 months after the October run). |
	> [!note] Note
	> - The cron expression currently evaluates against the specified time zone only. Altering the [TIMEZONE](https://docs.snowflake.com/sql-reference/parameters#label-timezone) parameter value for the account (or setting the value at the user or session level) does not change the time zone for the alert.
	> - The cron expression defines all valid times for the evaluation of the condition for the alert. Snowflake attempts to evaluate the condition based on this schedule; however, any valid run time is skipped if a previous run has not completed before the next valid run time starts.
	> - When both a specific day of month and day of week are included in the cron expression, then the evaluation of the condition is scheduled on days satisfying either the day of month or day of week. For example, `SCHEDULE = 'USING CRON 0 0 10-20 * TUE,THU UTC'` schedules an evaluation at 0AM on any 10th to 20th day of the month and also on any Tuesday or Thursday outside of those dates.
- `*num* MINUTE`
	Specifies an interval (in minutes) of wait time inserted between evaluations of the alert. Accepts positive integers only.
	Also supports `*num* M` syntax.
	To avoid ambiguity, a *base interval time* is set when the alert is resumed (using [ALTER ALERT … RESUME](https://docs.snowflake.com/INCLUDE/text/alter-alert)).
	The base interval time starts the interval counter from the current clock time. For example, if an alert is created with `10 MINUTE` and the alert is resumed at 9:03 AM, then the condition for the alert is evaluated at 9:13 AM, 9:23 AM, and so on. Note that we make a best effort to ensure absolute precision, but only guarantee that conditions are not evaluated before their set interval occurs (e.g. in the current example, the condition could be evaluated first at 9:14 AM but definitely not at 9:12 AM).
	> [!note] Note
	> The maximum supported value is `11520` (8 days). Alerts that have a greater `*num* MINUTE` value never have their conditions evaluated.

`COMMENT = 'string_literal'`

Specifies a comment for the alert.

`CONFIG = '*configuration_string*'`

Specifies a configuration string in valid JSON format that the alert can access at runtime by calling [SYSTEM$GET\_ALERT\_CONFIG](https://docs.snowflake.com/sql-reference/functions/system_get_alert_config).

The configuration is available in both the condition (`IF`) and action (`THEN`) blocks of the alert.

Syntax:

```
CONFIG=$${"string1": value1 [, "string2": value2, ...] }$$
```

Examples:

```sql
CONFIG=$${
  "enabled": true,
  "threshold": 10,
  "notify": "ops"
}$$
```

`RUNBOOK = '*string_literal*'`

Specifies a URL or free-text reference to a runbook for this alert. The runbook provides documentation or instructions for responding when the alert is triggered.

Maximum length: 2048 characters.

Example:

```sql
RUNBOOK='https://www.snowflake.com/alerts/my-alert-runbook'
```

`SUSPEND_ALERT_AFTER_NUM_FAILURES = *number*`

Specifies the number of consecutive failed alert runs after which the alert is suspended automatically. For more details, see [SUSPEND\_ALERT\_AFTER\_NUM\_FAILURES](https://docs.snowflake.com/sql-reference/parameters#label-suspend-alert-after-num-failures).

## Access control requirements

A [role](https://docs.snowflake.com/user-guide/security-access-control-overview#label-access-control-overview-roles) used to execute this operation must have the following [privileges](https://docs.snowflake.com/user-guide/security-access-control-overview#label-access-control-overview-privileges) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| EXECUTE MANAGED ALERT | Account | Required only for [serverless alerts](https://docs.snowflake.com/user-guide/alerts#label-alerts-serverless-compute). |
| EXECUTE ALERT | Account |  |
| CREATE ALERT | Schema |  |
| USAGE | Warehouse | Required only for [alerts that specify a warehouse to use](https://docs.snowflake.com/user-guide/alerts#label-alerts-warehouse-user-managed). |
| OWNERSHIP | Alert | Required to execute a [CREATE OR ALTER ALERT](#label-create-or-alter-alert-syntax) statement for an *existing* alert.  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](https://docs.snowflake.com/sql-reference/sql/grant-ownership) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege).  Note that in a [managed access schema](https://docs.snowflake.com/user-guide/security-access-control-configure#label-managed-access-schemas), only the schema owner (i.e. the role with the OWNERSHIP privilege on the schema) or a role with the MANAGE GRANTS privilege can grant or revoke privileges on objects in the schema, including future grants. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](https://docs.snowflake.com/user-guide/security-access-control-configure#label-security-custom-role).

For general information about roles and privilege grants for performing SQL actions on [securable objects](https://docs.snowflake.com/user-guide/security-access-control-overview#label-access-control-securable-objects), see [Overview of Access Control](https://docs.snowflake.com/user-guide/security-access-control-overview).

## Usage notes

- Alerts are executed using the privileges granted to the alert owner (i.e. the role that has the OWNERSHIP privilege on the alert). For the list of minimum required privileges to execute alerts, see [Granting the privileges to create alerts](https://docs.snowflake.com/user-guide/alerts#label-alerts-privileges-granting).
	To verify that the alert owner role has the required privileges to execute SQL statements for the condition and action, we recommend that you execute these statements using the alert owner role before specifying them in CREATE ALERT.
- When you create an alert, the alert is suspended by default.
	To make the alert active, you must execute [ALTER ALERT … RESUME](https://docs.snowflake.com/sql-reference/sql/alter-alert).
- To read configuration values at runtime, call [SYSTEM$GET\_ALERT\_CONFIG](https://docs.snowflake.com/sql-reference/functions/system_get_alert_config) in the condition or action SQL. If no configuration is set, the function returns `NULL`.

- When you execute CREATE ALERT or ALTER ALERT, some validation checks are not performed on the statements in the condition and action, including:
	- The resolution of the identifiers for objects.
		- The resolution of the data types of expressions.
		- The verification of the number and types of arguments in a function call.
	The CREATE ALERT and ALTER ALERT commands do not fail if the SQL statement for a condition or action specifies an invalid identifier, incorrect data type, incorrect number and types of function arguments, etc. Instead, the failure occurs when the alert executes.
	To check for failures in an existing alert, use the [ALERT\_HISTORY](https://docs.snowflake.com/sql-reference/functions/alert_history) table function.
	To avoid these types of failures, before you specify the conditions and actions for alerts, verify the SQL expressions and statements for those conditions and actions.

- Regarding metadata:
	> [!note] Attention
	> Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](https://docs.snowflake.com/sql-reference/metadata).

- The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
- CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## CREATE OR ALTER ALERT usage notes

- All limitations of the [ALTER ALERT](https://docs.snowflake.com/sql-reference/sql/alter-alert) command apply.
- An alert cannot be resumed or suspended using the CREATE OR ALTER ALERT command. To resume or suspend an alert, use the ALTER ALERT command.
- Setting or unsetting a tag is not supported; however, existing tags are not altered by a CREATE OR ALTER ALERT statement and remain unchanged.