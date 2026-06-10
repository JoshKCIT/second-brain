---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_managenewcapability.html
vendor: ibm-db2-zos
topic: continuous-delivery
fetched_at: 2026-06-10T06:35:49Z
revalidate_after: 2026-09-08T06:35:49Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/delta.gif)

## Adopting new capabilities in Db2 12 continuous delivery

In Db2 12, function levels and application compatibility levels control the adoption of most new capabilities by Db2 subsystems and Db2 applications.

## About this task

Function levels are specified by strings that correspond to the Db2 version, release, and maintenance value. The format is `VvvRrMmmm`, where vv is the version, r is the release, and mmm is the modification level. For example, `V12R1M510` identifies function level 510. For a list of all available function levels in Db2 12, see [Db2 12 function levels](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_db2functionlevels.html). Often function level identifiers are abbreviated. For example, function level 510 refers to V12R1M510.

Tip: ![Begin general-use programming interface information.](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/art/gupi_opn.svg) You can determine the catalog level and function level for a Db2 subsystem or data sharing group, and the code levels of individual subsystems or members, by issuing DISPLAY GROUP commands. For more information, see [Determining the Db2 code level, catalog level, and function level](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_determinefunctionlevel.html) ![End general-use programming interface information.](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/art/gupi_cls.svg)

**Continuous delivery in Db2 12**

The availability of most new-function application capabilities in Db2 12 depends on the type of enhancement, the activated function level, and the application compatibility levels of each application. For a list of all available function levels that are currently available in Db2 12, see [Db2 12 function levels](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_db2functionlevels.html).

Many new-function enhancements take effect at any function level when you apply a PTF in each Db2 subsystem or data sharing member. For more information, see [New-function APARs for Db2 12](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_newfunctionapars.html).

Virtual storage enhancements

Virtual storage enhancements become available at the activation of the function level that introduces them or higher. Activation of function level 100 introduces all virtual storage enhancements in the initial Db2 12 release. That is, activation of function level 500 introduces no virtual storage enhancements.

Subsystem parameters

New subsystem parameter settings are in effect only when the function level that introduced them or a higher function level is activated. Many subsystem parameter changes in the initial Db2 12 release take effect in function level 500. For more information about subsystem parameter changes in Db2 12, see [Subsystem parameter changes in Db2 12](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_subsysparmchanges.html).

Optimization enhancements

Optimization enhancements become available after the activation of the function level that introduces them or higher, and full prepare of the SQL statements. When a full prepare occurs depends on the statement type:
- For static SQL statements, after bind or rebind of the package
- For non-stabilized dynamic SQL statements, immediately, unless the statement is in the dynamic statement cache
- For stabilized dynamic SQL statements, after invalidation, free, or changed application compatibility level
Activation of function level 100 introduces all optimization enhancements in the initial Db2 12 release. That is, function level 500 introduces no optimization enhancements.

SQL capabilities

New SQL capabilities become available after the activation of the function level that introduces them or higher, for applications that run at the equivalent application compatibility level or higher. New SQL capabilities in the initial Db2 12 release become available in function level 500 for applications that run at the equivalent application compatibility level or higher. You can continue to run SQL statements compatibly with lower function levels, or previous Db2 releases, including Db2 11 and DB2® 10. For details, see [Application compatibility (APPLCOMPAT) levels in Db2 12](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_applicationcompatibility.html)

## Procedure

To manage the adoption of new capabilities in Db2 12, use the following overall process:

1. Apply maintenance to bring the Db2 subsystem to the required code level or higher.
	Tip: Apply the maintenance for a code level well before you tailor the catalog level or activate a function level. By doing so, you can verify that Db2 can continue run at the required code level, while you still have the opportunity to identify and remove any problematic maintenance items.
	Important: Do not attempt to start Db2 at any code level that is lower than the highest ever activated function level, even at the lower star (\*) function level. Activate a function level only after you are satisfied that Db2 can continue to run at the required code level.
2. If necessary, update the Db2 catalog.
	You can use a single CATMAINT job that specifies the target function level. If the target function level requires multiple catalog level updates, the CATMAINT job processes each update in sequential order. If a later update in the sequence fails, the previous successful updates do not roll back, and the catalog level remains at the highest level reached. If that occurs, you can correct the reason for the failure and resubmit the same CATMAINT job. Some function levels do not require catalog changes.
	Db2 12 uses the following Db2 catalog levels:
	- V12R1M509
	- V12R1M507
	- V12R1M505
	- V12R1M503
	- V12R1M502
	- V12R1M500
	Important: Do not attempt to start Db2 at a lower code level after any part of the CATMAINT job for a higher function level completes. Run the CATMAINT job only after you are satisfied that Db2 can continue to run at the necessary code level. The code to tolerate catalog changes is contained in the code level that delivers the CATMAINT job.
3. Activate the higher function level.
	Some new capabilities and enhancements become available immediately. Optimization enhancements become available after the next full prepare of the SQL statements. The application compatibility level of each application continues to control the use of new SQL capabilities.
4. When you are ready for applications, and objects such as routines or triggers, to use new SQL capabilities of the higher function level, rebind or alter them at the higher application compatibility level. Do this only after you are satisfied that Db2 12 is stable at the higher function level. You might need to adjust your applications for incompatible changes before they can run at the higher application compatibility level.
	Tip: Do not raise the default application compatibility level of the Db2 subsystem immediately after migrating or activating a new function level. Instead, wait until applications have been verified to work correctly at the higher function level, and any incompatibilities have been resolved. For details, see [Specifying the default application compatibility level](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_enableapplcompatsubsystem.html).

![End of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/deltaend.gif)