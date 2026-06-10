---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_connectapplication.html
vendor: ibm-db2-zos
topic: connect-application
fetched_at: 2026-06-10T06:35:51Z
revalidate_after: 2026-09-08T06:35:51Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Connecting to Db2 from your application program

Application programs communicate with Db2 through an attachment facility. You must invoke an attachment facility, either implicitly or explicitly, before your program can interact with Db2.

## About this task

You can use the following attachment facilities in a z/OS® environment:

CICS® attachment facility

Use this facility to access Db2 from CICS application programs.

IMS attachment facility

Use this facility to access Db2 from IMS application programs.

Time Sharing Option (TSO) attachment facility

Use this facility in a TSO or batch environment to communicate to a local Db2 subsystem. This facility invokes the DSN command processor.

Call attachment facility (CAF)

Use this facility as an alternative to the TSO attachment facility when your application needs tight control over the session environment.

Resource Recovery Services attachment facility (RRSAF)

Use this facility for stored procedures that run in a WLM-established address space or as an alternative to the CAF. RRSAF provides support for z/OS RRS as the recovery coordinator and supports other capabilities not present in CAF

For distributed applications, use the distributed data facility (DDF).

Requirement: Ensure that any application that requests Db2 services satisfies the following environment characteristics, regardless of the attachment facility that you use:
- The application must be running in TCB mode. SRB mode is not supported.
- An application task cannot have any Enabled Unlocked Task (EUT) functional recovery routines (FRRs) active when requesting Db2 services. If an EUT FRR is active, the Db2 functional recovery can fail, and your application can receive some unpredictable abends.
- Different attachment facilities cannot be active concurrently within the same address space. Specifically, the following requirements exist:
	- An application must not use CAF or RRSAF in an CICS or IMS address space.
		- An application that runs in an address space that has a CAF connection to Db2 cannot connect to Db2 by using RRSAF.
		- An application that runs in an address space that has an RRSAF connection to Db2 cannot connect to Db2 by using CAF.
		- An application cannot invoke the z/OS AXSET macro after executing the CAF CONNECT call and before executing the CAF DISCONNECT call.
- One attachment facility cannot start another. For example, your CAF or RRSAF application cannot use DSN, and a DSN RUN subcommand cannot call your CAF or RRSAF application.
- The language interface modules for CAF and RRSAF, DSNALI and DSNRLI, are shipped with the linkage attributes AMODE(31) and RMODE(ANY). If your applications load CAF or RRSAF below the 16-MB line, you must link-edit DSNALI or DSNRLI again.