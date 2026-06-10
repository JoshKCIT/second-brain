---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/perf/src/tpc/db2z_managingdb2perf.html
vendor: ibm-db2-zos
topic: managing-performance
fetched_at: 2026-06-10T06:35:41Z
revalidate_after: 2026-09-08T06:35:41Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Managing Db2 performance

Managing the performance of Db2 is an iterative process. Periodically, or after significant changes to your system or workload, you must reexamine your objectives, and refine your monitoring and tuning strategy accordingly.

## About this task

You can avoid some performance problems completely by planning for performance when you first design your system. As you begin to plan your performance, remember the following information.

- Db2 is only a part of your overall system. Any change to the system hardware, disk subsystems, z/OS®, IMS, CICS®, TCP/IP, VTAM®, the network, WebSphere®, or distributed application platforms (such as Windows, UNIX, or Linux®) that share your enterprise IT infrastructure can affect how Db2 and its applications run.
- The recommendations for managing performance are based on current knowledge of Db2 performance for normal circumstances and typical systems. Therefore, you need to understand that this information might not necessarily be the best or appropriate advice for every specific situation. In particular, the advice on performance often approaches situations from a performance viewpoint only. Other factors of higher priority might make some of these performance recommendations inappropriate for your specific solution.
- The recommendations are general. Performance measurements are highly dependent on workload and system characteristics that are external to Db2.

## Procedure

To manage Db2 performance, use the following approaches:

1. Establish your performance objectives when you plan your system.
2. Consider performance as you design and implement your system.
3. Plan how you will monitor performance and capture performance data.
4. Analyze performance reports to decide whether the objectives have been met.
5. If performance is thoroughly satisfactory, use one of the following options:
	- Monitor less, because monitoring itself uses resources.
		- Continue monitoring to generate a history of performance to compare with future results.
6. If performance has not been satisfactory, take the following actions:
	1. Determine the major constraints in the system.
		2. Decide where you can afford to make trade-offs and which resources can bear an additional load. Nearly all tuning involves trade-offs among system resources.
		3. Tune your system by adjusting its characteristics to improve performance.
		4. Continue to monitor the system.