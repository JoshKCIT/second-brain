---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/sqlref/src/tpc/db2z_structuredquerylanguage.html
vendor: ibm-db2-zos
topic: sql-language
fetched_at: 2026-06-10T06:35:30Z
revalidate_after: 2026-09-08T06:35:30Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## SQL: The language of Db2

The language that you use to access the data in Db2 tables is the structured query language (SQL). SQL is a standardized language for defining and manipulating data in a relational database.

The SQL language consists of SQL statements.

By using SQL statements, you can accomplish activities in the following categories, among others:

- Define, modify, or drop data objects such as tables by using various forms of CREATE, ALTER, and DROP statements. These statements are formally categorized as SQL schema statements, and sometimes informally as Data Definition Language (DDL) statements.
- Retrieve, insert, update, or delete data in tables by using SELECT, INSERT, UPDATE, and MERGE statements. These statements are formally categorized as SQL data statements, and sometimes informally as Data Manipulation Language (DML) statements.
- ![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/sqlref/delta.gif) Authorize users to access specific resources such as tables or views by using various forms of GRANT, REVOKE, and TRANSFER OWNERSHIP statements. These statements are formally categorized as SQL schema statements, but they are also sometimes informally categorized as Data Control Language (DCL) statements.![End of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/sqlref/deltaend.gif)

For a list of supported SQL statements by category, see [Categories of SQL statements](https://www.ibm.com/docs/en/SSEPEK_12.0.0/sqlref/src/tpc/db2z_sqlstmtcategories.html).

When you write an SQL statement, you specify what you want done, not how to do it. To access data for example, you need only to name the tables and columns that contain the data. You do not need to describe how to get to the data.

In accordance with the relational model of data, the database uses these principles:

- The database is perceived as a set of tables.
- Relationships are represented by values in tables.
- Data is retrieved by using SQL to specify a result table that can be derived from one or more tables.

Db2 transforms each SQL statement, that is, the specification of a result table, into a sequence of operations that optimize data retrieval. This transformation occurs when the SQL statement is prepared. This transformation is also known as binding.

All executable SQL statements must be prepared before they can run. The result of preparation is the executable or operational form of the statement.

As the following example illustrates, SQL is generally intuitive.

![Begin general-use programming interface information.](https://www.ibm.com/docs/en/SSEPEK_12.0.0/sqlref/src/art/gupi_opn.svg)

## Example

Assume that you are shopping for shoes and you want to know what shoe styles are available in size 8. The SQL query that you need to write is similar to the question that you might ask a salesperson, "What shoe styles are available in size 8?" Just as the salesperson checks the shoe inventory and returns with an answer, Db2 retrieves information from a table (SHOES) and returns a result table. The query looks like this:
```
SELECT STYLE
  FROM SHOES
  WHERE SIZE = 8;
```

Assume that the answer to your question is that two shoe styles are available in a size 8: loafers and sandals. The result table looks like this:

```
STYLE 
=======
LOAFERS
SANDALS
```
![End general-use programming interface information.](https://www.ibm.com/docs/en/SSEPEK_12.0.0/sqlref/src/art/gupi_cls.svg)

## SQL standards

Db2 for z/OS® is developed based on industry SQL standards. For more information, see [Industry standards and Db2 for z/OS](https://www.ibm.com/docs/en/SSEPEK_12.0.0/home/src/cmn/db2z_industrystandardsdb2.html).

## Syntax diagrams for SQL statements

For more information about the conventions for syntax diagrams in the Db2 product documentation, see [How to read syntax diagrams](https://www.ibm.com/docs/en/SSEPEK_12.0.0/home/src/cmn/db2z_cmn_how2readsyntax.html).

## Where to find PDF format and online content

The following table shows where to find the PDF format and online content from this section of the Db2 for z/OS product documentation.

| PDF Manuals | Where to find the online content |
| --- | --- |
| [SQL Reference](https://www.ibm.com/docs/en/SSEPEK_12.0.0/pdf/db2z_12_sqlrefbook.pdf "(Opens a PDF file)") |