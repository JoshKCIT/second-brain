---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/restserv/src/tpc/db2z_restservices.html
vendor: ibm-db2-zos
topic: rest-services
fetched_at: 2026-06-10T06:35:54Z
revalidate_after: 2026-09-08T06:35:54Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Db2 REST services

As a REST (Representational State Transfer) service provider, Db2 enables your web, mobile, and cloud applications to interact with Db2 data through a set of scalable RESTful APIs. These APIs are fully integrated in the Db2 distributed data facility (DDF). You can use the APIs to create, discover, execute, and manage user-defined services in Db2.

Db2 defines a REST service as a package. Each package contains a single static SQL statement and is stored in a user-defined SYSIBM.DSNSERVICE catalog table. When a service is created, a new row is added to the table that associates the service with its corresponding package. After the package is bound, it can be executed only as a service.

An authorized user can discover and invoke the service through a REST HTTP client, including IBM z/OS Connect Enterprise Edition or an IBM® Cloud API management solution. Db2 accepts the HTTP request, processes the request body in JSON (JavaScript Object Notation), executes the bound SQL statement, and returns any output in JSON.

![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/restserv/delta.gif) Db2 REST services supports a buffer size of up to 2GB for the combined request and reply content data for a single REST service request.![End of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/restserv/deltaend.gif)

All Db2 REST services are managed as native services. This Db2 native REST service solution leverages the existing DDF capabilities for authorization, authentication, client information management, service classification, system profiling, and service monitoring and display.