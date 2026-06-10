---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/pdf/db2z_12_secabook.pdf
vendor: ibm-db2-zos
topic: data-encryption
fetched_at: 2026-06-10T06:35:48Z
revalidate_after: 2026-09-08T06:35:48Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: manual
---

# Data encryption options for Db2 for z/OS

Db2 12 for z/OS protects sensitive data through several mechanisms. Unlike Db2 for Linux, UNIX, and Windows native encryption, **z/OS Db2 relies primarily on platform and data-set level controls** rather than a single “encrypt the database” toggle.

## z/OS DFSMS data set encryption

The primary at-rest encryption path for Db2 for z/OS is **z/OS DFSMS data set encryption**. Db2 data sets (including user data, logs, catalog, and directory data sets where applicable) can be encrypted using DFSMS policies and storage-group configuration. This integrates with z/OS key management (ICSF, key labels) rather than a Db2-internal master key store.

Typical use cases:

- Encrypt all data sets in a storage group used for Db2
- Encrypt data sets associated with a particular table or table space
- Encrypt log, catalog, and directory data sets under DFSMS control

## Db2 built-in encryption functions

Db2 for z/OS also supports **column-level encryption** using built-in functions such as:

- `ENCRYPT_TDES` — requires manual column definition and key management
- `ENCRYPT_DATAKEY` — data-key based column encryption with setup procedures documented in Managing Security

Value-level encryption is application-managed; it does not replace DFSMS data-set encryption for physical media protection.

## Network encryption

**SSL/TLS** can encrypt data in flight between clients and Db2. Configure SSL at the Db2 subsystem and client according to Managing Security.

## Utilities and encrypted data

Running utilities (`REORG`, `RUNSTATS`, `LOAD`, `UNLOAD`, `CHECK DATA`, and others) against encrypted data may require specific handling. See the Utility Guide section on the effect of utilities on encrypted data.

## Authority note

For vendor capability claims about Db2 for z/OS encryption, cite this cache and the canonical IBM Managing Security guide. Internal Confluence runbooks do not override IBM product behavior for `domain: vendor:ibm-db2-zos` claims.
