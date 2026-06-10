---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/char/src/tpc/db2z_introcharconv.html
vendor: ibm-db2-zos
topic: internationalization
fetched_at: 2026-06-10T06:35:59Z
revalidate_after: 2026-09-08T06:35:59Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## International data and character conversion in Db2 for z/OS

In computers, all characters are encoded according to the rules of a particular encoding scheme and code page. If your database and applications handle data from multiple code pages, that data might be converted at certain times from one code page to another. This conversion process is called character conversion.

This situation of handling data from multiple code pages is likely if your database and applications contain international data or data from multiple character sets, such as Latin-1 and Katakana. In this situation, character conversions are likely to occur.

Important: For best results, try to avoid character conversions whenever possible, because conversions can potentially slow performance and sometimes cause data loss. The best way to avoid conversions is to use the same CCSID for all of your data. For more information, see [Possible consequences of character conversion](https://www.ibm.com/docs/en/SSEPEK_12.0.0/char/src/tpc/db2z_consequencecharconv.html).

The problem with character conversions is that they can degrade performance and potentially cause data loss. Therefore, you should avoid these conversions if possible. One way to avoid these conversions is to have all of your data in one code page. If you use multiple character sets, you might considering using the Unicode code page. This code page includes all characters. If you use Unicode for all of your data, conversions can be avoided. However, converting all of your data to Unicode is not a simple process.

This information discusses basic principles about character conversion and general recommendations that you can apply to your environment for optimal performance and storage.