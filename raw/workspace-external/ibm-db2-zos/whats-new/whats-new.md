---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_wnew.html
vendor: ibm-db2-zos
topic: whats-new
fetched_at: 2026-06-10T06:35:50Z
revalidate_after: 2026-09-08T06:35:50Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## What's new in Db2 12

Db2 12 for z/OS® takes Db2 to a new level, both extending the core capabilities and empowering the future. Db2 12 extends the core with new enhancements to scalability, reliability, efficiency, security, and availability. Db2 12 also empowers the next wave of applications in the cloud, mobile, and analytics spaces.

## Continuous delivery and function levels

Db2 12 introduces continuous delivery of new capabilities and enhancements in a single service stream as soon as they are ready. With continuous delivery, your business can take advantage of the newest capabilities and enhancements in Db2 for z/OS as soon as you are ready, without waiting for the next full release. Many enhancements become available as soon as you apply the PTF for the APAR that introduces them. Where necessary to control the adoption of new application capabilities, function levels and application compatibility levels enable your business to control the adoption and use of new-feature capabilities by applications in your Db2 for z/OS environments.

Many new features and capabilities become available as soon as you apply the PTF for the APAR that introduces them. For a list of these features, see [New-function APARs for Db2 12](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_newfunctionapars.html).

When necessary, function levels enable you to control the timing of the activation and adoption of new features, with the option to continue to apply corrective and preventative service without adopting the new-feature function.

<iframe allowfullscreen="" src="https://video.ibm.com/embed/recorded/131253317" width="720" height="405"></iframe>

For more information about function levels in Db2 and how to activate them, see:

- [Db2 12 function levels](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_db2functionlevels.html)
- [Adopting new capabilities in Db2 12 continuous delivery](https://www.ibm.com/docs/en/SSEPEK_12.0.0/wnew/src/tpc/db2z_managenewcapability.html)
- [Exploring IBM Db2 for z/OS Continuous Delivery (IBM Redpaper)](http://www.redbooks.ibm.com/abstracts/redp5469.html?Open "(Opens in a new tab or window)")

Db2 12 function levels 100 and 500 represent the initial set of new capabilities for Db2 12. In many respects, these function levels are comparable to conversion mode (which corresponds to function level 100) and new-function mode (which corresponds to function level 500) from past releases.

Tip: For the most current information, view documentation for Db2 continuous delivery and function levels in IBM® Documentation, or download the latest PDF edition from [PDF format manuals for Db2 12 for z/OS](https://www.ibm.com/docs/en/SSEPEK_12.0.0/home/src/tpc/db2z_pdfmanuals.html) .

## Availability of new features and capabilities in Db2 12

Many new capabilities in Db2 12 are introduced in Db2 12 function levels. However, some become available immediately in the Db2 12 initial release, or when you apply maintenance.

For migration from Db2 11, most new capabilities become available only after you activate function level 500 or higher.

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

Blogs for Db2 for z/OS: See the [IBM Community blog for Db2 for z/OS and its ecosystem](https://community.ibm.com/community/user/communities/community-home/recent-community-blogs?CommunityKey=621c2a2a-01f9-4b57-992f-36ed7432e3bb "(Opens in a new tab or window)") for the latest news about new capabilities and enhancements in Db2 for z/OS continuous delivery, from the IBM experts who design, build, test, and support Db2

[Subscribe today!](https://community.ibm.com/community/user/viewdocument/db2znews-blog-subscribe "(Opens in a new tab or window)")