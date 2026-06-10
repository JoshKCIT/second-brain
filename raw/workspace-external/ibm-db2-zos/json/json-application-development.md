---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/json/src/tpc/db2z_jsonappdev.html
vendor: ibm-db2-zos
topic: json
fetched_at: 2026-06-10T06:35:53Z
revalidate_after: 2026-09-08T06:35:53Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## JSON application development for IBM data servers

In Db2, you can store and manage data that is formatted using JavaScript Object Notation (JSON). JSON provides a flexible mechanism to store and transmit data between application tiers. JSON is becoming one of the predominant technologies for rapidly changing mobile and interactive applications.

The JSON format is often used for serializing structured data and transmitting that structured data over a network connection. It is used primarily to transmit data between a server and a web application, serving as an alternative to XML. It eliminates the need for predetermined schema designs and reduces the need for data transformations.

JSON is a lightweight data exchange format that is specified in IETF RFC 4627. It is language independent and portable. As a subset of the JavaScript programming language, it is easy to implement and is easily read by humans and machines alike.

BSON is a standardized binary representation format for serializing JSON documents. It allows for fast traversal of JSON documents.

![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/json/delta.gif)

## Working with JSON documents by using SQL

You can also store and retrieve JSON values in Db2 columns without parsing or indexing on specific fields inside the JSON document, by using CLOB or VARCHAR column to hold the value. You can then query and update based on another key column in the table.

For more information about the recommended approach for working with JSON data in Db2 for z/OS®, see [Working with JSON documents by using SQL](https://www.ibm.com/docs/en/SSEPEK_12.0.0/json/src/tpc/db2z_jsonfunctions.html).

![End of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/json/deltaend.gif)

## Java API for JSON

A Java API also supports a JSON-oriented query language that is derived from the MongoDB query language.

Tip: The Java API is no longer the recommended approach for working with JSON data in Db2 for z/OS. For best results, use SQL and the built-in functions that are supplied with Db2 Accessories Suite for z/OS instead. For more information, see [Working with JSON documents by using SQL](https://www.ibm.com/docs/en/SSEPEK_12.0.0/json/src/tpc/db2z_jsonfunctions.html).

A JSON data store is a database that provides the capabilities to store, process, and manage data in JSON format. The Java API for JSON feature for Db2 enables a Db2 database to serve as a JSON data store. JSON documents in the data store are stored in a binary format, extended BSON.

For more information, see [Working with JSON documents with the Java API](https://www.ibm.com/docs/en/SSEPEK_12.0.0/json/src/tpc/db2z_jsonworkingwithdocs.html)