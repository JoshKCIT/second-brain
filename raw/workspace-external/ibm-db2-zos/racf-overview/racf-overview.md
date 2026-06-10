---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/racf/src/tpc/db2z_racfoverview.html
vendor: ibm-db2-zos
topic: racf-overview
fetched_at: 2026-06-10T06:35:47Z
revalidate_after: 2026-09-08T06:35:47Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Managing security with the RACF access control module

The RACF access control module allows you to use RACF in addition to Db2 authorization checking for Db2 objects, authorities, commands, and utilities.

You can activate the RACF access control module at the Db2 access control authorization exit point (DSNX@XAC), where you can replace the default Db2 exit routine.

The RACF access control module:

- Receives control from the Db2 access control authorization exit point (DSNX@XAC) to handle Db2 authorization checks
- Provides a single point of control for RACF and Db2 security administration
- Provides the ability to define security rules before a Db2 object is created
- Allows security rules to persist when a Db2 object is dropped
- Provides the ability to protect multiple Db2 objects with a single security rule using a combination of RACF generic, grouping, and member profiles
- Eliminates revocation of dependent privileges when a privilege is revoked from a Db2 user.
- Preserves Db2 privileges and administrative authorities
- Provides flexibility for multiple Db2 subsystems with a single set of RACF profiles
- Allows you to validate a user ID before giving it access to a Db2 object.

RACF support for the RACF access control module includes a set of general resource classes in the RACF module ICHRRCDX (the supplied portion of the RACF class descriptor table). These classes are used when you implement the RACF access control module using the default values.