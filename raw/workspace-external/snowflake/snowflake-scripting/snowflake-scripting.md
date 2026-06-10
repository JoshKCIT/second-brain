---
source_url: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/index
vendor: snowflake
topic: snowflake-scripting
fetched_at: 2026-06-10T06:40:17Z
revalidate_after: 2026-07-10T06:40:17Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

Snowflake Scripting is an extension to Snowflake SQL that adds support for procedural logic. You can use Snowflake Scripting syntax in [stored procedures](https://docs.snowflake.com/developer-guide/stored-procedure/stored-procedures-overview) and [user-defined functions (UDFs)](https://docs.snowflake.com/developer-guide/udf/sql/udf-sql-procedural-functions). You can also use Snowflake Scripting syntax outside of stored procedures and UDFs and stored procedures. The next topics explain how to use Snowflake Scripting.

[Understanding blocks in Snowflake Scripting](https://docs.snowflake.com/developer-guide/snowflake-scripting/blocks)

Learn the basic structure of Snowflake Scripting code.

[Working with variables](https://docs.snowflake.com/developer-guide/snowflake-scripting/variables)

Declare and use variables.

[Returning a value](https://docs.snowflake.com/developer-guide/snowflake-scripting/return)

Return values from stored procedures and an anonymous block.

[Working with conditional logic](https://docs.snowflake.com/developer-guide/snowflake-scripting/branch)

Control flow with IF and CASE statements.

[Working with loops](https://docs.snowflake.com/developer-guide/snowflake-scripting/loops)

Control flow with FOR, WHILE, REPEAT, and LOOP.

[Working with cursors](https://docs.snowflake.com/developer-guide/snowflake-scripting/cursors)

Iterate through query results with a cursor.

[Working with RESULTSETs](https://docs.snowflake.com/developer-guide/snowflake-scripting/resultsets)

Iterate over the result set returned by a query.

[Handling exceptions](https://docs.snowflake.com/developer-guide/snowflake-scripting/exceptions)

Handle errors by handling and raising exceptions.

[Determining the number of rows affected by SQL statements](https://docs.snowflake.com/developer-guide/snowflake-scripting/dml-status)

Use global variables to determine the effect of data manipulation language (DML) commands.

[Getting the query ID of the last query](https://docs.snowflake.com/developer-guide/snowflake-scripting/query-id)

Use the global variable SQLID to get the query ID of the last query.

[Examples for common use cases of Snowflake Scripting](https://docs.snowflake.com/developer-guide/snowflake-scripting/use-cases)

Explore examples of Snowflake Scripting code for some common use cases.

[Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](https://docs.snowflake.com/developer-guide/snowflake-scripting/running-examples)

Run the Snowflake Scripting examples in SnowSQL, Snowsight and Python Connector code.