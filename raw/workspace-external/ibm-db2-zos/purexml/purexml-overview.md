---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/xml/src/tpc/db2z_xmldb2.html
vendor: ibm-db2-zos
topic: purexml
fetched_at: 2026-06-10T06:35:55Z
revalidate_after: 2026-09-08T06:35:55Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Overview of pureXML

pureXML is Db2 for z/OS® support for XML. pureXML lets your client applications manage XML data in Db2 tables.

You can store well-formed XML documents in their hierarchical form and retrieve all or portions of those documents.

Because the stored XML data is fully integrated into the Db2 database system, you can access and manage the XML data by leveraging Db2 functions and capabilities.

To efficiently manage traditional SQL data types and XML data, Db2 stores XML data in separate table spaces from the tables that contain XML columns. However, the underlying storage mechanism that is used for XML data is transparent to the application. The application does not need to explicitly specify which XML table spaces to use, or to manage the physical storage for XML and non-XML objects.

*XML document storage:* The XML column data type is provided for storage of XML data in Db2 tables. Most SQL statements support the XML data type. This enables you to perform many common database operations with XML data, such as creating tables with XML columns, adding XML columns to existing tables, creating indexes over XML columns, creating triggers on tables with XML columns, and inserting, updating, or deleting XML documents. You can update entire XML documents in an XML column, or update only portions of XML documents.

Alternatively, you can extract data items from an XML document and store those data items in columns of relational tables, using the SQL XMLTABLE built-in function in the INSERT via SELECT form of an INSERT statement.

*XML document retrieval:* You can use SQL to retrieve entire documents from XML columns, just as you retrieve data from any other type of column. When you need to retrieve portions of documents, you can specify XQuery expressions, through SQL with XML extensions (SQL/XML).

*XML schema validation:* XML schema validation is the process of determining whether the structure, content, and data types of an XML document are valid according to an XML schema. You can perform XML schema validation explicitly, by using the DSN\_XMLVALIDATE function, or implicitly, if the XML column into which you insert XML documents has an XML type modifier.

*Application development:* Application development support of XML enables applications to combine XML and relational data access and storage. The following programming languages support the XML data type:
- Assembler
- C or C++ (embedded SQL or Db2 ODBC)
- COBOL
- Java™ (JDBC or SQLJ)
- PL/I

*Database administration:* Db2 for z/OS database administration support for pureXML includes the following items:

XML schema repository (XSR)

The XML schema repository (XSR) is a repository for all XML schemas that are required to validate and process XML documents that are stored in XML columns.

Utility support

Db2 for z/OS utilities support the XML data type. The storage structure for XML data and indexes is similar to the storage structure for LOB data and indexes. As with LOB data, XML data is not stored in the base table space, but it is stored in separate table spaces that contain only XML data. The XML table spaces also have their own index spaces. Therefore, the implications of using utilities for manipulating, backing up, and restoring XML data and LOB data are similar.

*Performance:* Indexing support is available for data stored in XML columns. The use of indexes over XML data can improve the efficiency of queries that you issue against XML documents. An XML index differs from a relational index in that a relational index applies to an entire column, whereas an XML index applies to part of the data in a column. You indicate which parts of an XML column are indexed by specifying an XML pattern, which is a limited XPath expression.