---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/admin/src/tpc/db2z_dbdigintro.html
vendor: ibm-db2-zos
topic: database-design
fetched_at: 2026-06-10T06:35:33Z
revalidate_after: 2026-09-08T06:35:33Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Designing and implementing Db2 databases

When you are familiar with Db2 concepts, you can begin to design and implement your Db2 databases. This information explains the task of implementing your database design in a way that most new users will understand. When you actually perform the task, you might perform the steps in a different order.

The objects in a relational database are organized into sets called schemas. A schema provides a logical classification of objects in the database. The schema name is used as the qualifier of SQL objects such as tables, views, indexes, and triggers.

You define, or create, objects by executing SQL statements. This information summarizes some of the naming conventions for the various objects that you can create. Also in this information, you will see examples of the basic SQL statements and keywords that you can use to create objects in a Db2 database. (This information does not document the complete SQL syntax.)

Tip: When you create Db2 objects (such as tables, table spaces, views, and indexes), you can precede the object name with a qualifier to distinguish it from objects that other people create. (For example, MYDB.TSPACE1 is a different table space than YOURDB.TSPACE1.) When you use a qualifier, avoid using SYS as the first three characters. If you do not specify a qualifier, Db2 assigns a qualifier for the object.