---
source_url: https://docs.snowflake.com/en/sql-reference/functions-encryption
vendor: snowflake
topic: encryption-functions
fetched_at: 2026-06-10T06:43:54Z
revalidate_after: 2026-07-10T06:43:54Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:snowflake
authority: standard
ingest_mode: defuddle
---

## Encryption functions

Encryption functions encrypt or decrypt VARCHAR or BINARY values.

| Function | Notes |
| --- | --- |
| [ENCRYPT](https://docs.snowflake.com/sql-reference/functions/encrypt) | Encrypts VARCHAR or BINARY values using a passphrase. |
| [DECRYPT](https://docs.snowflake.com/sql-reference/functions/decrypt) | Decrypts VARCHAR or BINARY values using a passphrase. |
| [TRY\_DECRYPT](https://docs.snowflake.com/sql-reference/functions/try_decrypt) | Error-handling version of DECRYPT. |
| [ENCRYPT\_RAW](https://docs.snowflake.com/sql-reference/functions/encrypt_raw) | Encrypts BINARY values using a binary key and an initialization vector. |
| [DECRYPT\_RAW](https://docs.snowflake.com/sql-reference/functions/decrypt_raw) | Decrypts BINARY values using a binary key and an initialization vector. |
| [TRY\_DECRYPT\_RAW](https://docs.snowflake.com/sql-reference/functions/try_decrypt_raw) | Error-handling version of DECRYPT\_RAW. |