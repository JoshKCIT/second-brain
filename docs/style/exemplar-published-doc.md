---
title: "Exemplar: Historical Table Design Primer"
type: writing-style-exemplar
purpose: Quality bar for project artifacts authored by the agent chain. Reference this when authoring any wiki article or project artifact.
note: "Cleaned from a real published reference document. The original carried export-bold artifacts; those have been stripped. The technical content is preserved as-is."
---

Designing Historical Tables: Principles and Best Practices

### Historical Table Design Primer

Audience: Operational teams, software engineers, and anyone building or consuming tables that need to preserve a record of how data changes over time.
Purpose: This document explains — from the ground up — what a historical table is, why you need one, how to design and populate it, and what each required column does. It is written to be self-contained; you do not need to read any other document first.
What You’ll Learn
After reading this document, you will be able to:
Explain what a historical table is and why it matters
Identify the required columns (business key, EFCTV_TS, ACTV_CD, CRT_TS, UPDT_TS) and their purposes
Choose between event-driven and batch approaches for capturing changes
Write queries against an existing historical table (current-state lookups, point-in-time queries)
Make informed decisions about naming conventions and timestamp data types
### What This Document Does Not Cover
This document focuses on design concepts and conventions — the what and why of historical tables. It does not include hands-on implementation artifacts. For those, see the companion Implementation Guides, which cover:
DDL templates and column ordering (Guide 1)
Load process SQL — insert, update, delete detection (Guide 2)
Event-driven vs. batch decision framework (Guide 3)
Performance and table growth management (Guide 4)
Edge cases — duplicates, NULLs, concurrency, late-arriving data (Guide 5)
Validation queries and test scenarios (Guide 6)
Initial/seed load bootstrapping (Guide 7)
Transaction safety, idempotency, staging lifecycle, rollback (Guide 8)
Schema evolution — new/changed/dropped columns (Guide 9)
Current-state views, point-in-time joins, BI/dbt integration (Guide 10)
Orchestration, scheduling, multi-table coordination (Guide 11)
Operational runbook — incident response, access control, EDF registration (Guide 12)
Table of Contents
## What Is a Historical Table and Why Do You Need One?
### The Problem
Most operational (day-to-day transactional) tables store only the current state of data. When a customer changes their address, the old address is overwritten. When a contract is terminated, the row is deleted. The prior values are gone.
This is fine for running the business in the moment, but it creates a serious gap: you cannot answer questions about the past.
“What was this participant’s address six months ago?”
“When exactly was this contract terminated?”
“How many plans were active at the end of Q3 last year?”
“What did this row look like before someone changed it on Tuesday?”
If the old data was overwritten or deleted, the answer is: “We don’t know.”
The Solution: A Historical Table
A historical table (also called a history-preserving table or delta table) solves this by following one simple rule:
Never overwrite or delete a row. Instead, insert a new row every time something changes.
Each row in the historical table is a snapshot of an entity at a specific point in time. Over time, a single entity (identified by its business key) accumulates multiple rows — one for each change that occurred.
### Why You Should Always Capture History
It may be tempting to skip history tracking when the current use case doesn’t seem to need it. However, there is a critical asymmetry:
Adding history capture later is easy — you change the load process going forward.
Recovering history you didn’t capture is impossible — there is no way to reconstruct the delta changes that occurred between the time the table was built and the time you decided to start capturing them.
For this reason, the standing recommendation is: always capture history/delta changes from day one. The cost of storing the extra rows is far lower than the cost of not having the data when someone eventually needs it. This is the same pattern used in on-prem Data Warehouse (DW) tables today, and it carries forward into cloud-based data products.
## Append-Only vs. Destructive Reload Patterns
There are two fundamentally different ways to load data into a target table. Understanding the difference is essential before designing anything.
Destructive Reload (Overwrite)
In a destructive reload, the target table is emptied (truncated) and reloaded from scratch each time, or existing rows are updated in place using a MERGE or UPDATE statement.
	
Characteristic	
Detail
	
What happens to old data	
It is overwritten or deleted — gone forever
	
Row count over time	
Stays roughly the same as the source
	
When it’s acceptable	
Staging/landing tables, reference/lookup data with no audit trail requirement, throwaway intermediate tables
	
When it’s not acceptable	
Any table where you need to answer “what did this look like at time X?”
Append-Only (History-Preserving)
In an append-only pattern, the target table only ever receives INSERT statements. No existing rows are updated or deleted (with one narrow exception described in Section 12).
	
Characteristic	
Detail
	
What happens to old data	
It stays — every prior state is preserved as its own row
	
Row count over time	
Grows with every change detected in the source
	
When to use it	
Any table that needs historical fidelity — DW tables, sourced data products, analytical/reporting tables
### Decision Rule
Default to append-only for any table that will be used for reporting, analytics, auditing, or as a source for downstream curated/consumption layers. Use destructive reload only for transient tables where history has no value.
What About Snowflake Time Travel?
If you’re working in Snowflake, you may know that Time Travel lets you query data as it existed at any point within a configurable retention window (default 1 day, maximum 90 days). It’s natural to ask: “Why do I need an append-only historical table if Time Travel already gives me point-in-time access?”
The short answer: Time Travel is a recovery and debugging tool, not a history-tracking strategy. Here’s why:
	
Concern	
Snowflake Time Travel	
Append-Only Historical Table
	
Retention	
1–90 days (configurable, costs extra storage)	
Indefinite — every change is preserved permanently
	
Granularity	
Table-level snapshots at a moment in time	
Row-level deltas — you can see exactly which entity changed and when
	
Logical deletes	
A deleted row simply disappears from the current state; Time Travel shows it existed yesterday but not why it vanished	
ACTV_CD = 2 explicitly marks the deletion with a timestamp
	
Portability	
Snowflake-only feature; doesn’t travel with the data to S3, DB2, or other platforms	
The history is in the data itself — it works on any platform
	
Auditability	
No built-in way to ask “what changed on March 15?”	
Query by EFCTV_TS or CRT_TS to see exactly what changed and when
Time Travel is valuable for short-term recovery (“someone truncated the table an hour ago — restore it”) and debugging (“what did this query return yesterday?”). It complements the append-only pattern but does not replace it.
## What Is a Delta Change?
A delta change (or simply “delta”) is any change to a row in the source/operational system. There are exactly three types:
	
Delta Type	
What Happened in the Source	
What Happens in the Historical Table
	
Insert	
A brand-new row appeared (new business key)	
A new row is inserted with Active Code = 1 (active)
	
Update	
An existing row had one or more attributes modified	
A new row is inserted with all attributes (changed and unchanged), Active Code = 1
	
Delete	
An existing row was removed	
A new row is inserted that is identical to the prior row, except Active Code = 2 (not active)
The key insight: all three source-side operations become INSERTs into the historical table. The historical table itself is never updated or deleted (under normal operation). This is what makes it append-only.
## Key Terminology
These terms appear throughout this document and in related documentation. They are organized into two groups: core concepts you should understand before reading further, and organizational/platform terms you can refer back to as needed.
### Core Concepts
These are the building blocks of historical table design. Make sure you’re comfortable with each one before moving on.
	
Term	
Definition
	
Delta	
Any insert, update, or delete that occurs in the source/operational system.
	
Grain	
The level of detail a table represents. For example, a table at participant grain has one logical entity per participant; a table at contract grain has one per contract.
	
Business Key (also Natural Key, Unique Key)	
The column(s) that uniquely identify a single logical entity in the source system — e.g., a contract number, a participant ID, a plan ID. In the historical table, the business key alone is not unique (because multiple rows exist per entity over time).
	
Effective Timestamp (EFCTV_TS)	
The timestamp recording when a delta change was identified. Combined with the business key, it makes each row unique.
	
Active Code (ACTV_CD)	
A flag indicating whether a row represents an active (1) or logically-deleted (2) record.
	
Create Timestamp (CRT_TS)	
The timestamp of when the row was physically inserted into the historical table.
	
Update Timestamp (UPDT_TS)	
The timestamp of when the row was last modified in the historical table. Normally equals the create timestamp; differs only for manual corrections.
Organizational and Platform Terms
These terms describe the broader environment. You don’t need to memorize them now — refer back here when you encounter them later.
	
Term	
Definition
	
Data Warehouse (DW)	
A database layer that stores data sourced from operational systems, structured for analytical and reporting use. History is captured here.
	
Consumption Layer	
A layer built on top of the DW that is curated (transformed, denormalized/flattened) specifically for reporting and analytics.
	
Source Data Product	
In the Enterprise Data Foundation (EDF), a data product whose contents closely mirror the source system with minimal transformation. Analogous to the on-prem DW layer.
	
Curated Data Product	
A data product that has undergone significant transformation, combining and restructuring data for broader consumption. Analogous to the on-prem consumption layer.
	
MDM	
Master Data Management — a system that maintains a single, authoritative version of key business entities (e.g., customer identity).
	
PRTCP_ID (Participant ID)	
A surrogate identifier assigned to each unique combination of prefix code, contract number, and member ID. Used in place of MBR_ID (Member ID) to avoid exposing SSN.
	
Bounded Context	
The scope within which a consistent set of naming conventions, data definitions, and standards apply (e.g., a single squad’s set of tables).
	
UTC	
Coordinated Universal Time — the global time standard. Not adjusted for daylight saving time.
	
Offset	
The difference (in hours) between UTC and local time, e.g., Central Standard Time = UTC−06:00.
How to Read Abbreviated Column Names
Column names in this document (and throughout our data environment) use a consistent abbreviation pattern: full words are shortened to recognizable fragments, joined with underscores, and the last segment is a “class word” that indicates what kind of data the column holds (see Section 15 for the full list of class words).
Here are some examples to help you decode names you’ll encounter later:
	
Abbreviated Name	
Full Meaning	
### Class Word
	
PRTCP_ID	
PaRTiCiPant IDentifier	
_ID = identifier
	
CNTR_NMBR	
CoNTract NuMBeR	
_NMBR = number
	
PRFX_CD	
PReFiX CoDe	
_CD = code
	
ACTV_STAT_DM	
ACTiVe STATus DoMain (reference table)	
_DM = domain
	
EFCTV_TS	
EFfeCTiVe TimeStamp	
_TS = timestamp
Tip: When you encounter an unfamiliar abbreviation later in this document, refer back to this table or to the terminology tables above.
Relationship to Industry Terminology (SCD Type 2)
If you’ve studied data warehousing or used tools like dbt, Informatica, or Talend, you may recognize the pattern described in this document as Slowly Changing Dimension Type 2 (SCD2). That’s exactly what it is — our organization’s implementation of SCD2, with a few differences from the textbook version:
	
Aspect	
Textbook SCD2	
### Our Implementation
	
Row validity tracking	
valid_from / valid_to date range on each row	
EFCTV_TS only (no end-date column). Current state is determined by the most recent EFCTV_TS per business key.
	
Surrogate key	
An auto-increment ID column is typically added as the primary key	
No surrogate key. The composite key (business key + EFCTV_TS) serves as the primary key. See Section 9.
	
Delete tracking	
Varies — some implementations don’t track deletes	
ACTV_CD = 2 provides explicit logical delete tracking. See Section 6.
	
Current-row flag	
An is_current boolean column	
Not used. “Current” is derived by querying the most recent EFCTV_TS.
These differences are intentional. Omitting valid_to and is_current means there is no column that needs to be updated on existing rows when a new change arrives — which is what makes our tables truly append-only.
External resources: If you want to explore SCD2 further, search for “Slowly Changing Dimension Type 2” in Kimball Group resources. For tool-specific implementations, see dbt snapshots (which add dbt_valid_from / dbt_valid_to columns rather than using ACTV_CD).
## The Effective Timestamp — Your Change Indicator
### What It Is
The effective timestamp (EFCTV_TS) records when the source-system change was identified. It does not represent when the row was physically loaded into the target (that’s the create timestamp — see Section 7).
Why It’s a Key Column
The effective timestamp is part of the primary key of the historical table. Combined with the business key, it ensures that each row is unique — even when the same entity has changed many times.
Example: A participant with PRTCP_ID = 1234 might have five rows, each with a different EFCTV_TS, representing five distinct states over time.
It Is Additive, Not a Replacement
Some source tables already include a date or timestamp as part of their key — for example, a TRANSACTION_DATE column that distinguishes one day’s transactions from another. When you build a historical table from that source, you keep the source date column and add EFCTV_TS on top of it. Think of it this way: the source date tells you what the original record was about; EFCTV_TS tells you when you captured a snapshot of it.
If the source/operational data already has a date or timestamp in its key (e.g., a transaction date), the effective timestamp is in addition to that existing column — it does not replace it. The source-system key columns remain part of the business key; EFCTV_TS is appended to enable history tracking.
Event-Driven vs. Batch Granularity
The effective timestamp’s granularity depends on how changes are detected:
	
Approach	
Effective Timestamp Contains	
Trade-off
	
Event-driven (intra-day)	
The actual date/time the change occurred (down to the millisecond)	
Captures every intermediate state; more rows; higher storage
	
Batch (end-of-logical-day)	
A fixed timestamp like end-of-day (e.g., 23:59:59)	
Multiple changes within the same day collapse into one row; fewer rows; some intermediate states are lost
Both approaches are valid. The choice depends on how quickly downstream consumers need to see changes and whether intra-day intermediate states matter.
A Note on EFCTV_TS Conventions in Practice
The worked examples in Section 16 use a conceptual end-of-day value (23:59:59) to make the batch pattern easy to follow. In production SQL (see Guide 2 — Building the Load Process), batch loads typically use CURRENT_TIMESTAMP() — the actual execution time of the load job (e.g., 09:00 AM the morning after the business day). Both conventions are valid:
	
Convention	
When to Use
	
End-of-day value (e.g., 23:59:59 -0600)	
When EFCTV_TS should represent the business date the delta applies to. Requires the load process to derive the value rather than calling CURRENT_TIMESTAMP().
	
CURRENT_TIMESTAMP()	
When EFCTV_TS should represent when the load ran. Simpler — no derivation needed. This is what most Snowflake implementations use.
The key rule: pick one convention for your pipeline and document it. Mixing conventions within the same table makes point-in-time queries unreliable.
Background: What Is a Batch ETL Pipeline?
If you’re already familiar with ETL, skip ahead to the next subsection.
A batch ETL (Extract, Transform, Load) pipeline is an automated process that runs on a schedule — typically once per day, often overnight. It pulls data from the source system, compares it against what’s already in the target table, and loads any changes it finds. Because it runs on a fixed schedule rather than reacting to each individual change as it happens, there is always a delay between when a change occurs in the source and when it appears in the target. This delay is what makes the “missed-delta” scenario described below possible.
The Missed-Delta Caveat
On-prem, the effective date is typically process-generated and indicates when the row becomes effective in the DW environment. Changes are generally received the day after the delta occurs. If a delta from several days ago was missed and the load is retried, the effective date will reflect the retry date (typically CURRENT DATE − 1 DAY), not the date the change actually occurred in the source. This means the effective timestamp is a reliable indicator of when the delta was captured, but it may not always match when the change actually happened in the operational system.
### Platform Notes
	
Platform	
On-Prem DB2	
Snowflake / EDF
	
Column name	
EFCTV_DT or OCR_ON_TS	
EFCTV_TS
	
Data type	
DATE or TIMESTAMP	
TIMESTAMP_TZ (timestamp with time zone)
## Active Code — Tracking Current State and Logical Deletes
### What It Is
The active code (ACTV_CD) is a column that indicates whether a given row represents a currently active record or a record that has been logically deleted (i.e., the source system deleted it, but we preserve it in the historical table rather than actually removing it).
	
Value	
Meaning
	
1	
Active — this row represents a current or historically-valid state
	
2	
Not active — the record was deleted in the source system
Why 1 and 2 Instead of True/False or Y/N?
This convention comes from the on-prem DB2 environment, where the column is typed as SMALLINT. The values 1 and 2 align with an existing reference (domain) table ACTV_STAT_DM where 1 = ACTIVE and 2 = INACTIVE. This pattern has been carried forward for consistency.
When to Include It
The standing recommendation (established February 2013) is to include ACTV_CD in all Data Warehouse / historical tables unless there is a specific, documented reason not to. Even if deletes are rare for a given source, including the column costs almost nothing and provides a safety net.
How to Determine “Current State”
To find the current state of an entity, query for the most recent row (by effective timestamp) for a given business key:
If the most recent row has ACTV_CD = 1 → the entity is currently active; that row reflects its latest state.
If the most recent row has ACTV_CD = 2 → the entity has been deleted in the source. The data in the row reflects its state at the time of deletion.
How It Works with Deletes
When the source system deletes a row:
The historical table already contains the entity’s most recent row (with ACTV_CD = 1).
A new row is inserted that is identical to the most recent row in every attribute — except ACTV_CD is set to 2.
The effective timestamp on the new row reflects when the deletion was detected.
This preserves a clear audit trail: you can see exactly when the record became inactive and what the data looked like at that moment.
### Platform Notes
	
Platform	
On-Prem DB2	
Snowflake / EDF
	
Column name	
ACTV_CD	
ACTV_CD
	
Data type	
SMALLINT	
SMALLINT (or equivalent integer type)
	
Primary key?	
No	
No
	
Nullable?	
Not Null	
### Not Null
	
Default	
1	
1
Related: ACTV_STAT_CD
In some operational mainframe DB2 tables, a similar column called ACTV_STAT_CD is used to identify active vs. inactive rows, referencing the ACTV_STAT_DM domain table (1 = ACTIVE, 2 = INACTIVE). This is the operational-side equivalent; ACTV_CD is the DW/historical-table convention.
## Create Timestamp and Update Timestamp — Housekeeping Columns
These two columns exist for administrative and downstream-processing purposes. They are not part of the primary key.
Create Timestamp (CRT_TS)
	
Attribute	
Detail
	
Definition	
The date/time when this row was physically inserted into the historical table.
	
Value	
Always the current system timestamp at the moment of insert.
	
Key?	
No
	
Nullable?	
### Not Null
	
Purpose	
Enables downstream processes (e.g., curated data products) to detect which rows are new since the last load — a form of delta detection at the DW-to-consumption boundary.
Update Timestamp (UPDT_TS)
	
Attribute	
Detail
	
Definition	
The date/time when this row was last modified in the historical table.
	
Value on insert	
Same as CRT_TS — on initial insert, both columns are identical.
	
Value on manual update	
Updated to the current system timestamp. See Section 12.
	
Key?	
No
	
Nullable?	
### Not Null
	
Purpose	
Same as CRT_TS — delta detection for downstream consumers. The difference between CRT_TS and UPDT_TS also serves as a signal that a manual correction was applied.
### The Relationship Between Them
Under normal automated processing, CRT_TS and UPDT_TS are always equal — because every change from the source produces a brand-new INSERT, not an UPDATE to an existing row. The only time they diverge is if someone manually corrects a row directly in the historical table (a data quality fix, for example).
Rule of thumb: If CRT_TS ≠ UPDT_TS, that row was manually modified after initial load.
### Platform Notes
	
Platform	
On-Prem DB2	
Snowflake / EDF
	
Column names	
CRT_DT + CRT_TM (date and time as separate columns)	
CRT_TS (single timestamp column)
	
	
UPDT_DT + UPDT_TM	
UPDT_TS
	
Data type	
DATE + TIME	
TIMESTAMP_TZ
	
Additional column	
USER_ID — CHAR(8), hardcoded to RISDWETL for automated loads; set to the actual user ID for manual updates	
(At discretion of owning team)
Note: Whether to store date and time as separate columns or as a single timestamp is at the discretion of the owning team. The trend in cloud/EDF is toward a single TIMESTAMP_TZ column.
## Timestamp Data Type Guidance
### The Recommendation
Use TIMESTAMP WITH TIME ZONE (known as TIMESTAMP_TZ in Snowflake) for all timestamp columns. Store the value in UTC with the appropriate UTC offset.
Why
	
Reason	
Explanation
	
Avoids ambiguity	
A bare timestamp like 2024-10-03 11:15:00 is meaningless without knowing the time zone. Is that Central? UTC? Eastern? Storing the offset (-0600) removes all doubt.
	
Prevents drift during migration	
When data moves between on-prem (Central time default), AWS (UTC default), and Snowflake, a timestamp without an offset can silently shift. With an explicit offset, the value is self-describing and immune to platform defaults.
	
Immune to daylight saving time (DST)	
TIMESTAMP_TZ stores UTC + offset. It is not affected by DST transitions. In contrast, TIMESTAMP_LTZ (local time zone) is DST-aware and can produce non-deterministic results depending on the session’s time zone setting.
Why This Matters — A Concrete Example
Imagine a row is inserted on-prem at 3:00 PM Central Time (which is UTC−06:00). The timestamp is stored as 2024-10-03 15:00:00 with no offset attached. Later, that data is migrated to AWS, which defaults to UTC. Without an offset, the system reads 15:00:00 as 3:00 PM UTC — which is actually 9:00 AM Central. The row now appears six hours earlier than it actually occurred, and no one gets an error message — the shift is silent.
With TIMESTAMP_TZ, the value would be stored as 2024-10-03 15:00:00 -0600. Any system reading it knows the original moment in time, regardless of that system’s own default time zone. The offset travels with the data.
What to Avoid
	
Type	
Risk
	
TIMESTAMP_NTZ (no time zone)	
Stores “wall clock” time with no indication of time zone. If two systems interpret it differently, data corruption occurs silently. This is currently the Snowflake default — which is why explicit use of TIMESTAMP_TZ is important.
	
TIMESTAMP_LTZ (local time zone)	
Internally stores UTC but renders according to the session’s time zone. Useful when you need DST-aware calculations, but non-deterministic across sessions with different time zone settings. Use as a secondary attribute alongside TIMESTAMP_TZ when DST awareness is required.
### Handling Source Timestamps
The table below is a decision guide — find the row that matches what your source system gives you, then follow the corresponding guidance.
	
Source Provides	
Guidance
	
Timestamp only (no offset, no location)	
Do not assume a time zone. If you know with certainty it represents Central, convert to UTC and store with offset -0600. If unknown, store with offset +0000 and document the assumption.
	
Timestamp + offset	
Preserve the UTC + offset as-is in TIMESTAMP_TZ.
	
Timestamp + location (e.g., “America/Chicago”)	
Convert to UTC + offset for TIMESTAMP_TZ. Optionally, also store as TIMESTAMP_LTZ and keep location as a separate attribute if DST-aware calculations are needed.
	
Date only (no time component)	
Store as DATE, not as a timestamp with a default time of 00:00:00.
Most common case: The first row — a bare timestamp with no offset — is what you will encounter most often, especially from legacy on-prem sources. The key takeaway: never guess the time zone; confirm it with the source team or document your assumption.
Platform Defaults (Be Aware)
	
Environment	
### Default Timestamp Behavior
	
On-prem servers and DB2	
Central time
	
AWS (RDS, Lambda, logs)	
UTC
	
Snowflake account-level setting	
TIMESTAMP_NTZ (currently) — transitioning to TIMESTAMP_TZ
	
Snowflake console display	
TIMESTAMP_LTZ
## Composite Key Design
The primary key of a historical table is what makes each row unique. It consists of two parts:
Primary Key = Business Key column(s) + Effective Timestamp
### Why This Works
In the source/operational system, the business key alone uniquely identifies an entity (e.g., PRTCP_ID = 1234 refers to exactly one participant). But in the historical table, that same participant may have dozens of rows — one for each change over time. Adding the effective timestamp to the key ensures that each point-in-time snapshot is a distinct row.
Why Not Just Use a Single Auto-Increment ID?
If you’ve worked with application databases, you may be used to a single auto-incrementing integer column (id) as the primary key. That pattern works well when each row represents a distinct entity. In a historical table, however, the same entity appears in multiple rows — one per change.
An auto-increment ID would make each row unique, but it wouldn’t tell you: - Which rows belong to the same entity — you’d need a separate column for that (which is just the business key). - When each snapshot was taken — you’d need another column for that (which is just the effective timestamp).
The composite key (business key + effective timestamp) solves both problems in the key itself: it groups rows by entity and orders them chronologically. Adding a synthetic auto-increment column on top would be redundant.
When the Source Key Already Contains a Date/Timestamp
Some source systems include a date or timestamp as part of their own primary key (e.g., a transaction date). In this case:
The effective timestamp is additive — do not remove or replace the existing source-system date/timestamp.
The historical table’s key becomes:
Source Key column(s) (including any source date/timestamp) + Effective Timestamp
This ensures that both the source’s natural uniqueness and the history-tracking mechanism are preserved.
Example
	
Column	
Role
	
PRTCP_ID	
Business key — identifies the participant
	
CNTR_NMBR	
Business key — identifies the contract
	
EFCTV_TS	
History key — identifies when this snapshot was captured
Together, these three columns form the composite primary key. No two rows will share the same combination.
## Detecting Inserts, Updates, and Deletes from the Source
When loading data from the source system into the historical table, the process must compare the incoming data against what already exists and determine what type of delta occurred.
### Insert Detection
Condition: A business key exists in the incoming source data but does not exist in the historical table.
Action: Insert a new row with: - All attributes from the source - ACTV_CD = 1 - EFCTV_TS = timestamp when the insert was identified - CRT_TS = current system timestamp - UPDT_TS = current system timestamp (same as CRT_TS)
### Update Detection
Condition: A business key exists in both the source data and the historical table, but one or more non-key attributes differ between the source and the most recent row in the historical table for that key.
Action: Insert a new row with: - All attributes from the source — both the changed ones and the unchanged ones (carry forward the full row, not just the deltas) - ACTV_CD = 1 - EFCTV_TS = timestamp when the update was identified - CRT_TS = current system timestamp - UPDT_TS = current system timestamp (same as CRT_TS)
Important: Even though only one attribute may have changed, the new row contains every attribute. This makes point-in-time queries simple — each row is a complete snapshot, and consumers do not need to piece together partial changes.
### Delete Detection
Condition: A business key exists in the historical table (with the most recent row having ACTV_CD = 1) but does not exist in the incoming source data.
Action: Insert a new row that is: - Identical to the most recent row for that business key in every data attribute (nothing changed in the data itself) - ACTV_CD = 2 (not active — the record was deleted in the source) - EFCTV_TS = timestamp when the deletion was identified - CRT_TS = current system timestamp - UPDT_TS = current system timestamp (same as CRT_TS)
Summary of the Core Principle
	
Source-side operation	
Historical table operation	
ACTV_CD value
	
INSERT	
INSERT new row	
1
	
UPDATE	
INSERT new row	
1
	
DELETE	
INSERT new row	
2
The historical table only ever receives INSERTs. No existing rows are modified or removed under normal automated processing.
## Event-Driven vs. Batch Detection
There are two main approaches to detecting and recording deltas. The right choice depends on latency requirements and whether intermediate states matter.
Key infrastructure terms (for readers new to data engineering):
ETL (Extract, Transform, Load): An automated process that pulls data from a source system, optionally transforms it, and loads it into a target. Batch ETL runs on a schedule (e.g., nightly). See also the background note in Section 5.
Change Data Capture (CDC): A technique that detects individual row-level changes (inserts, updates, deletes) in a source database and streams them to a target in near-real-time. Tools such as Debezium and AWS Database Migration Service (DMS) implement CDC.
Event Streaming: A pattern where each change is published as a message (an “event”) to a streaming platform such as Apache Kafka. Downstream consumers read events as they arrive rather than waiting for a batch run.
You don’t need deep knowledge of these tools to follow this section — just know that event-driven approaches require more infrastructure than batch.
Event-Driven (Intra-Day)
Each individual change in the source system generates a row in the historical table in near-real-time. If an entity is updated three times in a single day, three separate rows are inserted, each with its own effective timestamp reflecting the actual time of the change.
Advantages: - Full granularity — every intermediate state is captured - Enables near-real-time reporting and analytics
Disadvantages: - Higher row volume and storage - More complex infrastructure (event streaming, change data capture, etc.)
Batch (End-of-Logical-Day)
Changes are compared once per day (or per batch window). If an entity changed multiple times within the same day, only the final state at the end of the batch window is captured. The effective timestamp is typically set to an end-of-day value (e.g., 23:59:59).
Advantages: - Simpler infrastructure — standard batch ETL - Fewer rows and lower storage
Disadvantages: - Intermediate states within the same batch window are lost - Latency — changes aren’t visible until the next batch run
How They Compare (Same Scenario)
Consider an entity (Unique Key = 1234) that undergoes these source-system changes: - Oct 1: Inserted - Oct 3 (morning): Attribute 2 updated - Oct 3 (afternoon): Attributes 1 & 3 updated - Oct 5: Deleted
Event-driven would produce 4 rows (one per change, each with the actual timestamp).
Batch would produce 3 rows (the two Oct 3 changes collapse into one end-of-day row reflecting only the final state).
The detailed worked examples are in Section 16.
## The Manual Update Exception
Under normal operation, no existing rows in the historical table are ever updated. There is one narrow exception.
### When It Applies
Occasionally, a row in the historical table contains incorrect data due to a data quality issue, a processing bug, or a one-time correction. In these cases, the row may be updated directly.
### What Changes
	
Column	
Behavior
	
Effective timestamp	
No change — the row still represents the same point in time
	
Active code	
No change
	
Create timestamp	
No change — the row was originally inserted at that time
	
Update timestamp	
Updated to the current system timestamp
	
Data attributes	
Updated as needed to correct the issue
How to Spot a Manual Update
If CRT_TS ≠ UPDT_TS on a row, it means the row was modified after its initial insert. This is the only scenario where these two columns differ, so it serves as a reliable indicator of manual intervention.
On-Prem Note
In on-prem DB2 environments with the USER_ID column, manual updates would set USER_ID to the actual person’s user ID (rather than the default RISDWETL used by automated ETL processes), providing an additional audit trail.
## Attribute Breadth — Think Broadly, Not Narrowly
When deciding which columns to include in the historical table, a common mistake is to include only the attributes needed for the current use case. This creates a problem:
If you add an attribute later, you can only capture its history from that point forward. All the delta changes that occurred before the attribute was added are lost.
### The Recommendation
Look at the source/operational data holistically. Include all relevant attributes from the source system, even those not immediately needed. The marginal cost of storing a few extra columns is small compared to the cost of not having the data when a future reporting or curation need arises.
This also prevents a common workaround: when a missing attribute is needed, teams sometimes create a separate table or layer just to capture the new attribute’s deltas going forward. This leads to data fragmentation and unnecessary replication. Including the attribute from the start avoids this entirely.
## Balancing Historical Fidelity, Operational Simplicity, and Reporting Needs
Designing a historical table involves balancing three concerns:
### Historical Fidelity
Default to capturing everything. The cost of storage is lower than the cost of not having data you later need.
Include all attributes (Section 13).
Always capture deletes as logical deletes via ACTV_CD = 2 rather than physically removing rows.
### Operational Simplicity
The append-only pattern is simpler than alternatives. There are no UPDATE or DELETE statements to write, no merge logic to debug, no concurrency issues on existing rows.
A single INSERT statement handles all three delta types (insert, update, delete) — only the column values differ.
This makes the load process easy to reason about, test, and troubleshoot.
### Reporting Needs
Consumers can answer the two most common reporting questions with simple filters:
	
Question	
### Query Pattern
	
“What is the current state of entity X?”	
WHERE Unique_Key = X and EFCTV_TS = (MAX for that key) and ACTV_CD = 1
	
“What did entity X look like at time T?”	
WHERE Unique_Key = X and EFCTV_TS <= T order by EFCTV_TS DESC and take the first row
	
“Which entities are currently active?”	
Get the latest row per business key, then filter ACTV_CD = 1
	
“When did entity X get deleted?”	
Find the row where ACTV_CD = 2 — its EFCTV_TS indicates when the deletion was detected
How the Layers Work Together
The DW / source layer (historical tables) feeds the curated / consumption layer:
Operational System  →  Historical Table (DW / Source)  →  Curated / Consumption Layer
    [append-only, full history]         [transformed, denormalized,
    flattened for reporting]
Keeping the historical table comprehensive and append-only makes curation simpler downstream — the curated layer can always go back to the historical table to get any data it needs, at any point in time.
## Naming Conventions and Practical Constraints
The naming rules in this section are shaped by decades of platform constraints — particularly IBM DB2 on mainframes and SAS analytics software. If you’ve only worked with modern cloud databases (where column names can be hundreds of characters long and any casing is allowed), some of these rules will feel unnecessarily restrictive. They exist because many of our tables originated on — or still live on — these older platforms, and consistency across both environments is important. Understanding the why behind the rules will help them feel less arbitrary.
### Column Naming Standard
The established convention is UPPER_CASE snake_case (words separated by underscores, all uppercase). This originates from the on-prem DB2 environment, which requires uppercase identifiers.
Abbreviations are drawn from a standard dictionary (the DATA_ABRVN DB2 table on-prem). They keep names within platform length limits and reduce keystrokes in analytical queries where column names can become long due to denormalization.
Class words are used as the last node of a column name to clarify the type of data:
_ID = identifier (e.g., CNTR_ID)
_CD = code (e.g., ACTV_CD)
_DT = date (e.g., EFCTV_DT)
_TS = timestamp (e.g., CRT_TS)
_NM = name (e.g., CNTR_NM)
_NMBR = number (e.g., CNTR_NMBR)
### Cloud Naming Considerations
For cloud-based data products, the naming convention is at the discretion of each squad, with one requirement: apply it consistently within the bounded context (the scope of tables owned by your team). Considerations include:
If the data is a copy from DB2 on-prem, keep the naming the same for traceability.
If the data will be accessed by Java applications, camelCase may be more natural.
Shared keys (PRTCP_ID, CNTR_NMBR, PRFX_CD, etc.) should use consistent naming across teams to enable joins across data products.
SAS 32-Character Limit
SAS restricts variable names to a maximum of 32 characters. If there is any possibility that a data product will be consumed by SAS:
Keep column names at or under 32 characters.
Be aware that SAS will silently truncate longer names, and if two column names share the same first 32 characters, SAS will auto-number them — causing confusion.
DB2 z/OS Length Limits
DB2 has its own length constraints that are more restrictive when certain access patterns are used:
	
Access Pattern	
Max Table Name Length	
### Max Column Name Length
	
Direct SQL	
30	
30
	
DCLGEN	
21	
25
	
DB2 I/O Module	
18	
18
This is why abbreviations are critical in DB2 environments.
What are DCLGEN and DB2 I/O Module? DCLGEN (Declarations Generator) is a DB2 utility that generates COBOL or PL/I data structure declarations from a table definition — the generated variable names must fit within the host language’s naming limits. DB2 I/O Module is a standardized access layer used by some applications to read and write DB2 tables. Both impose stricter name-length limits than direct SQL because they must comply with the host-language variable naming constraints of COBOL and PL/I.
Participant ID Over Member ID
When data is at the participant grain, use PRTCP_ID (Participant ID) — not MBR_ID (Member ID). This is required because MBR_ID may contain Social Security Numbers (SSN). PRTCP_ID is a surrogate key assigned to every unique combination of PRFX_CD (prefix code), CNTR_NMBR (contract number), and MBR_ID, stored in the PEN_MBR_PRTCP_KEY table.
Enterprise ID — Do Not Store Directly
When participant-level data needs to be joined with data products keyed by Enterprise ID (e.g., for customer name, address, etc.), do not store Enterprise ID in your data product. Instead, a dedicated crosswalk/translation data product will translate PRTCP_ID to Enterprise ID. This ensures Enterprise ID stays in sync with MDM (Master Data Management) consolidation events and avoids stale or inconsistent values across data products.
## Worked Examples
The following examples trace the same entity through a series of source-system changes, showing exactly what the historical table looks like after each change.
Scenario: An entity with Unique Key = 1234 undergoes the following operational changes: 1. Oct 1 — Inserted with Attribute 1 = “Irwin”, Attribute 2 = “Matthew”, Attribute 3 = “Fletcher” 2. Oct 3 (morning) — Attribute 2 updated from “Matthew” to “M” 3. Oct 3 (afternoon) — Attributes 1 & 3 updated from “Irwin”/”Fletcher” to “I”/”Fletch” 4. Oct 5 — Deleted from the source system
Example A: Event-Driven (Intra-Day)
Each change is captured individually as it happens. Four source-system events produce four rows in the historical table.
	
Row	
Activity	
EFCTV_TS	
ACTV_CD	
Unique Key	
Attr 1	
Attr 2	
Attr 3	
CRT_TS	
UPDT_TS
	
1	
Insert	
2024-10-01 09:00:01 −0600	
1	
1234	
Irwin	
Matthew	
Fletcher	
2024-10-01 09:01:01 −0600	
2024-10-01 09:01:01 −0600
	
2	
Update Attr 2	
2024-10-03 11:15:01 −0600	
1	
1234	
Irwin	
M	
Fletcher	
2024-10-03 11:16:01 −0600	
2024-10-03 11:16:01 −0600
	
3	
Update Attrs 1 & 3	
2024-10-03 13:30:01 −0600	
1	
1234	
I	
M	
Fletch	
2024-10-03 13:31:01 −0600	
2024-10-03 13:31:01 −0600
	
4	
Delete	
2024-10-05 17:55:01 −0600	
2	
1234	
I	
M	
Fletch	
2024-10-05 17:56:01 −0600	
2024-10-05 17:56:01 −0600
Things to notice: - Every row is an INSERT into the historical table — even the delete (Row 4). - Row 2 carries forward Attr 1 (“Irwin”) and Attr 3 (“Fletcher”) even though only Attr 2 changed. Each row is a complete snapshot. - Row 4 (delete) is identical to Row 3 in all data attributes — only ACTV_CD changed to 2. - CRT_TS and UPDT_TS are always equal (no manual corrections occurred). - The EFCTV_TS on each row reflects the actual time of the source change. The CRT_TS is slightly later (the time the row was physically loaded).
Example B: End-of-Logical-Day (Batch)
Changes are detected once per day. The same four source-system events now produce only three rows because the two Oct 3 changes are collapsed into a single end-of-day row.
	
Row	
Activity	
EFCTV_TS	
ACTV_CD	
Unique Key	
Attr 1	
Attr 2	
Attr 3	
CRT_TS	
UPDT_TS
	
1	
Insert	
2024-10-01 23:59:59 −0600	
1	
1234	
Irwin	
Matthew	
Fletcher	
2024-10-02 09:00:01 −0600	
2024-10-02 09:00:01 −0600
	
2	
Update (collapsed)	
2024-10-03 23:59:59 −0600	
1	
1234	
I	
M	
Fletch	
2024-10-04 09:00:01 −0600	
2024-10-04 09:00:01 −0600
	
3	
Delete	
2024-10-05 23:59:59 −0600	
2	
1234	
I	
M	
Fletch	
2024-10-06 09:00:01 −0600	
2024-10-06 09:00:01 −0600
Things to notice: - Row 2 represents the final state of the entity at end-of-day Oct 3. The intermediate state where Attr 2 was “M” but Attr 1 was still “Irwin” (from the morning update) is not captured — it is collapsed into the final values. - EFCTV_TS uses end-of-day 23:59:59 to indicate “as of end of this day.” - CRT_TS is the following morning at 09:00 — reflecting when the batch process ran and inserted the row. - In the event-driven example, there are 4 rows. In the batch example, there are 3. The batch approach trades granularity for simplicity.
Key Differences Side-by-Side
	
Aspect	
Event-Driven	
Batch
	
Total rows for this scenario	
4	
3
	
Intermediate Oct 3 state captured?	
Yes (Rows 2 and 3)	
No (only final state in Row 2)
	
EFCTV_TS precision	
Actual event time	
End-of-day
	
CRT_TS timing	
Shortly after the event	
Next morning (batch run time)
## Quick Reference Card
Required Columns for Every Historical Table
	
Column	
Data Type	
Key?	
Purpose
	
Business key column(s)	
(varies)	
Yes	
Identifies the entity (e.g., PRTCP_ID, CNTR_NMBR)
	
EFCTV_TS	
TIMESTAMP_TZ	
Yes	
When the delta change was identified
	
ACTV_CD	
SMALLINT	
No	
1 = active, 2 = not active (deleted)
	
CRT_TS	
TIMESTAMP_TZ	
No	
When the row was physically inserted
	
UPDT_TS	
TIMESTAMP_TZ	
No	
When the row was last modified (= CRT_TS unless manually corrected)
Column Behavior by Scenario
	
Scenario	
EFCTV_TS	
ACTV_CD	
CRT_TS	
UPDT_TS	
### Data Attributes
	
Source INSERT	
Timestamp of when insert was identified	
1	
Current timestamp	
Current timestamp	
Values from source
	
Source UPDATE	
Timestamp of when update was identified	
1	
Current timestamp	
Current timestamp	
All values from source (changed + unchanged)
	
Source DELETE	
Timestamp of when delete was identified	
2	
Current timestamp	
Current timestamp	
Same as prior row (no data changed)
	
Manual correction	
No change	
No change	
No change	
Updated to current timestamp	
Corrected values
Current-State Query Pattern
-- Get the current state of a specific entity
SELECT *
FROM historical_table
WHERE unique_key = 1234
    AND EFCTV_TS = (
    SELECT MAX(EFCTV_TS)
    FROM historical_table
    WHERE unique_key = 1234
    )
    AND ACTV_CD = 1;
Point-in-Time Query Pattern
-- Get the state of an entity as of a specific date/time
SELECT *
FROM historical_table
WHERE unique_key = 1234
  AND EFCTV_TS <= '2024-10-03 12:00:00 -0600'
ORDER BY EFCTV_TS DESC
FETCH FIRST 1 ROW ONLY;