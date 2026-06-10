---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/dshare/src/tpc/db2z_introdatasharing.html
vendor: ibm-db2-zos
topic: data-sharing
fetched_at: 2026-06-10T06:35:48Z
revalidate_after: 2026-09-08T06:35:48Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Introduction to Db2 data sharing

In Db2 data sharing, applications that reside in multiple Db2 subsystems in a Parallel Sysplex can read from and write to the same Db2 for z/OS® data concurrently, with integrity, performance, scalability, and dynamic workload balancing.

A Sysplex is a group of z/OS systems that communicate and cooperate with one another using specialized hardware and software. They are connected and synchronized through a Sysplex Timer and enterprise systems connection channels. A Parallel Sysplex is a Sysplex that uses one or more coupling facilities, which provide high-speed caching, list processing, and lock processing for any applications on the Sysplex.

A collection of one or more Db2 subsystems that share Db2 data is called a data sharing group. Db2 subsystems that access shared Db2 data must belong to a data sharing group.

A Db2 subsystem that belongs to a data sharing group is a member of that group. Each member can belong to one, and only one, data sharing group. All members of a data sharing group share the same Db2 catalog and directory, and all members must reside in the same Parallel Sysplex. The maximum number of members in a data sharing group is 32.

All members of a data sharing group can read and update the same Db2 data simultaneously. Therefore, all data that different members of the group can access must reside on shared disks.

Some capabilities described in this information can be used in both data sharing and non-data sharing environments. This information uses the term data sharing environment to describe a situation in which a data sharing group has been defined with at least one member. In a non-data sharing environment, no group is defined.