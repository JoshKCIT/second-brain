---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/ugref/src/tpc/db2z_introutilities.html
vendor: ibm-db2-zos
topic: utilities
fetched_at: 2026-06-10T06:35:34Z
revalidate_after: 2026-09-08T06:35:34Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Db2 utilities

Use IBM® Db2 utilities to help maintain data in your Db2 for z/OS® databases.

## Online and stand-alone utilities

Most of the basic utilities, such as LOAD and COPY, are online utilities; they require Db2 to be up and running. Db2 online utilities run as standard batch jobs or stored procedures. They do not run under control of the terminal monitor program (TMP); they have their own attachment mechanism and they invoke Db2 control facility services directly. For more information about online utilities, see [Db2 online utilities](https://www.ibm.com/docs/en/SSEPEK_12.0.0/ugref/src/tpc/db2z_onlineutilities.html "Db2 online utilities run as standard batch jobs or stored procedures, and they require Db2 to be running. They do not run under control of the terminal monitor program (TMP); they have their own attachment mechanism and they invoke Db2 control facility services directly.") and [Invoking Db2 online utilities](https://www.ibm.com/docs/en/SSEPEK_12.0.0/ugref/src/tpc/db2z_invokeonlineutilities.html "To invoke Db2 online utilities, Db2 must be up and running.").

The other type of utilities is stand-alone utilities. These utilities run independently of Db2. They work directly on the data sets. You can use stand-alone utilities to do tasks such as format logs, modify the bootstrap data set (BSDS), and copy and print data sets. The stand-alone utilities run as batch jobs. The only way to run these utilities is to use JCL. For more information about stand-alone utilities, see [Db2 stand-alone utilities](https://www.ibm.com/docs/en/SSEPEK_12.0.0/ugref/src/tpc/db2z_standaloneutilities.html "The stand-alone utilities run as batch jobs that are independent of Db2. The only way to run these utilities is to use JCL.") and [Invoking stand-alone utilities](https://www.ibm.com/docs/en/SSEPEK_12.0.0/ugref/src/tpc/db2z_invokestandaloneutl.html "To invoke a stand-alone utility, you must use JCL. Some stand-alone utilities read the utility control statements from an input stream; other utilities obtain the function definitions from JCL EXEC PARM parameters.").

Exception: Some Db2 for z/OS users use the term online utilities to mean something other than what IBM means when it uses this term in the documentation. Some users use this term to refer to utilities that leave the data available while they are running. For example, when you use the REORG TABLESPACE utility to reorganize data, you can specify the level of access that other applications and processes have to that same data. If you specify the SHRLEVEL CHANGE option, the data can be changed while the utility runs. Therefore, REORG TABLESPACE SHRLEVEL CHANGE is considered by some users to be an "online utility" because the data is never taken offline. However, IBM does not use the term this way.<iframe allowfullscreen="" src="https://www.ustream.tv/embed/recorded/129358808" width="480" height="270" title="Introduction to IBM Db2 for z/OS Utilities"></iframe>