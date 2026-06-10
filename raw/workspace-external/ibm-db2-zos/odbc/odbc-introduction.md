---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/odbc/src/tpc/db2z_hdint.html
vendor: ibm-db2-zos
topic: odbc
fetched_at: 2026-06-10T06:35:55Z
revalidate_after: 2026-09-08T06:35:55Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Introduction to Db2 ODBC

Db2 ODBC offers advantages over SQL and provides helpful extensions for application programming.

Db2 Open Database Connectivity (ODBC) is the IBM® callable SQL interface by the Db2 family of products. It is a C and C++ language application programming interface for relational database access, and it uses function calls to pass dynamic SQL statements as function arguments. It is an alternative to embedded dynamic SQL, but unlike embedded SQL, it does not require a precompiler.

Db2 ODBC is based on the Windows Open Database Connectivity (ODBC) specification, and the X/Open Call Level Interface specification. These specifications were chosen as the basis for the Db2 ODBC in an effort to follow industry standards and to provide a shorter learning curve for those application programmers familiar with either of these *data source* interfaces. In addition, some Db2 specific extensions were added to help the Db2 application programmer specifically exploit Db2 features.