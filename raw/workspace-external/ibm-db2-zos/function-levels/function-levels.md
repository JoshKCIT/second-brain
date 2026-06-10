---
source_url: https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=12-db2-function-levels
vendor: ibm-db2-zos
topic: function-levels
fetched_at: 2026-06-10T06:35:32Z
revalidate_after: 2026-09-08T06:35:32Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

![Start of change](https://www.ibm.com/docs/delta.gif)

## Db2 12 function levels

New Db2 capabilities and enhancements are continuously delivered in a single maintenance stream as the code becomes ready. You can activate the new capabilities in a data sharing group or Db2 subsystem after a function level is delivered. A function level corresponds to a single PTF that enables the activation of a specific set of enhancements that shipped in previous prerequisite or co-requisite PTFs. The activation of a function level results in the activation of all lower function levels.

Blogs for Db2 for z/OS: See the [IBM® Community blog for Db2 for z/OS® and its ecosystem](https://community.ibm.com/community/user/communities/community-home/recent-community-blogs?CommunityKey=621c2a2a-01f9-4b57-992f-36ed7432e3bb "(Opens in a new tab or window)") for the latest news about new capabilities and enhancements in Db2 for z/OS continuous delivery, from the IBM experts who design, build, test, and support Db2

[Subscribe today!](https://community.ibm.com/community/user/viewdocument/db2znews-blog-subscribe "(Opens in a new tab or window)")

## About function levels in Db2 12

A function level enables a particular set of new Db2 capabilities and enhancements that were previously delivered in the single continuous stream of Db2 code. It includes code that supports new capabilities, defect fixes, and preventive service items. Before you can use the new capabilities of a function level, you must activate the function level, or a higher function level. Activation of a function level implies activation of the capabilities that are introduced by all lower function levels.

<iframe allowfullscreen="" src="https://video.ibm.com/embed/recorded/131253317" width="720" height="405"></iframe>

For more information about function levels, and how to activate them in Db2 12, see [Adopting new capabilities in Db2 12 continuous delivery](https://www.ibm.com/wnew/src/tpc/db2z_managenewcapability.html).

## Available function levels in Db2 12

The following function levels are available in Db2 12. They are listed in release order, beginning with the highest available function level.

| Function level | New-function capabilities (functional code APARs) | Catalog level | Enabling APAR | Release Date |
| --- | --- | --- | --- | --- |
| [FL 508](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m508.html) | - [Migration of multi-table table spaces to partition-by-growth universal table spaces (UTS)](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m508.html#db2z_fl_v12r1m508__e101) (PH27370, PH27658, PH27659, PH27660, PH27661, PH27662, PH27663) - [FTB support for non-unique indexes](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m508.html#db2z_fl_v12r1m508__e454) (PH30978) | V12R1M507 | [PH29392](https://www.ibm.com/support/pages/apar/PH29392 "(Opens in a new tab or window)") | 2020-10 |
| [FL 507](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m507.html) | - [Application granularity for locking limits (NUMLKUS and NUMLKTS)](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m507.html#db2z_fl_v12r1m507__application-numlk) (PH15342) - [Deletion of old statistics when using profiles](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m507.html#db2z_fl_v12r1m507__runstats) (PH16345) - [CREATE OR REPLACE for procedures](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m507.html#db2z_fl_v12r1m507__createreplace) (PH24324) - [Newly supported passthrough-only expressions with IBM Db2 Analytics Accelerator](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m507.html#db2z_fl_v12r1m507__new-passthrough) (PH23042) | V12R1M507 | [PH24371](https://www.ibm.com/support/pages/apar/PH24371 "(Opens in a new tab or window)") | 2020-06 |
| [FL 506](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m506.html) | - [Alternative function names support](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m506.html#db2z_fl_v12r1m506__e78336) (PH14712) - [Support for implicitly dropping explicitly created UTS and LOB table spaces](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m506.html#db2z_fl_v12r1m506__87272) (PH14452) | V12R1M505 | [PH16829](https://www.ibm.com/support/pages/apar/PH16829 "(Opens in a new tab or window)") | 2019-10 |
| [FL 505](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m505.html) | - [Rebind phase-in for packages that are being used for execution](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m505.html#db2z_fl_v12r1m505__82144) (PH12186) - [New built-in functions for encryption and decryption with key labels](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m505.html#db2z_fl_v12r1m505__71842) (PH09506) - [Improved support for DECFLOAT columns](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m505.html#db2z_fl_v12r1m505__82142) (PH09797) - [Improved RUNSTATS performance with automatic page sampling by default](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m505.html#db2z_fl_v12r1m505__93652) (PH07220) - [Temporal and archive transparency support for WHEN clause on triggers](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m505.html#db2z_fl_v12r1m505__81468) (PH09794) | V12R1M505 | [PH09191](https://www.ibm.com/support/pages/apar/PH09191 "(Opens in a new tab or window)") | 2019-06 |
| [FL 504](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m504.html) | - [IBM z14 Huffman compression](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m504.html#db2z_fl_v12r1m504__sect-38875) (PH04424) - [Prevent creation of new deprecated objects](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m504.html#db2z_fl_v12r1m504__sect-76110) (PH02873) - [Newly supported built-in functions with IBM Db2 Analytics Accelerator](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m504.html#db2z_fl_v12r1m504__sect-74487) (PH00224) - [New SQL syntax alternatives for special registers and NULL predicates](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m504.html#db2z_fl_v12r1m504__sect-37424) (PH02646) | V12R1M503 | [PH07672](https://www.ibm.com/support/pages/apar/PH07672 "(Opens in a new tab or window)") | 2019-04 |
| [FL 503](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m503.html) | - [Enablement for replication of system-period temporal tables and generated expression columns](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m503.html#db2z_fl_v12r1m503__41599) - [Console message for catalog level or function level change](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m503.html#db2z_fl_v12r1m503__76107) - [Temporal auditing](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m503.html#db2z_fl_v12r1m503__75440) (PI95480) | V12R1M503 | [PH00506](https://www.ibm.com/support/pages/apar/PH00506 "(Opens in a new tab or window)") | 2018-10 |
| [FL 502](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m502.html) | - [Key label management for z/OS DFSMS data set encryption](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m502.html#db2z_fl_v12r1m502__48635) (PI90288) - [Explicit casting of numeric values to GRAPHIC or VARGRAPHIC](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m502.html#db2z_fl_v12r1m502__67312) (PI88790) - [Db2 12 migration process changes](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m502.html#db2z_fl_v12r1m502__migr-changes) | V12R1M502 | [PI95511](https://www.ibm.com/support/pages/apar/PI95511 "(Opens in a new tab or window)") | 2018-05 |
| [FL 501](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m501.html) | - [The LISTAGG built-in function](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m501.html#db2z_fl_v12r1m501__listagg) | V12R1M500 | [PI70535](https://www.ibm.com/support/pages/apar/PI70535 "(Opens in a new tab or window)") | 2017-05 |
| [FL 500](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m500.html) | - [Application enablement in the Db2 12 initial release](https://www.ibm.com/wnew/src/tpc/db2z_12_appenable.html) - [Administrator function in the Db2 12 initial release](https://www.ibm.com/wnew/src/tpc/db2z_12_dba.html) - [Query performance in the Db2 12 initial release](https://www.ibm.com/wnew/src/tpc/db2z_12_qryperf.html) - [OLTP performance in the Db2 12 initial release](https://www.ibm.com/wnew/src/tpc/db2z_oltpperf.html) - [Subsystem parameter changes in function level 500](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m500.html#db2z_fl_v12r1m500__zparms500) - [Command changes in function level 500](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m500.html#db2z_fl_v12r1m500__commands500) - [SQL statement changes in Db2 12 function level 500](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m500.html#db2z_fl_v12r1m500__sql500) - [Utility changes in function level 500](https://www.ibm.com/docs/en/db2-for-zos/db2z_fl_v12r1m500.html#db2z_fl_v12r1m500__utility500) | V12R1M500 | None | 2016-10 |
| [FL 100](https://www.ibm.com/wnew/src/tpc/db2z_fl_v12r1m100.html) | V12R1M500 | None | 2016-10 |

Notes:
1. When the PTF for the APAR is applied in the Db2 subsystem or data sharing member.

![End of change](https://www.ibm.com/docs/deltaend.gif)