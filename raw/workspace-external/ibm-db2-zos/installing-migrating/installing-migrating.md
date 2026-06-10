---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/inst/src/tpc/db2z_installingmigratingdb2.html
vendor: ibm-db2-zos
topic: installing-migrating
fetched_at: 2026-06-10T06:35:34Z
revalidate_after: 2026-09-08T06:35:34Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Installing or migrating to Db2 12

![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/inst/delta.gif)

Start of change

## Installation and migration tools

Db2 12 provides the following tools that help you complete the process of installing or migrating to Db2 12:

Job control language (JCL) jobs

Each installation and migration JCL job helps you perform an installation or migration task.

Installation and migration command list (CLIST)

The installation and migration CLIST helps tailor the installation and migration JCL jobs. It contains the necessary code for tailoring the jobs to suit your needs.

Tip: You can capture most settings of an existing Db2 subsystem by running the DSNTIJXZ job, which invokes the DSNTXAZP tool. Running this job reduces the effort to manually compare settings in the current DSNTIJUZ job with the values that are defined in the defaults input member. For details, see [Updating the CLIST defaults input member: job DSNTIJXZ](https://www.ibm.com/docs/en/SSEPEK_12.0.0/inst/src/tpc/db2z_jobdsntijxz.html) and [DSNTXAZP tool](https://www.ibm.com/docs/en/SSEPEK_12.0.0/inst/src/tpc/db2z_dsntxazp.html).

Interactive Systems Productivity Facility (ISPF) panels

You can use a series of ISPF panels to pass parameter values to the CLIST. The CLIST uses these values to tailor the installation and migration jobs. This process is described in [Generating tailored Db2 12 installation, migration, or function level activation jobs](https://www.ibm.com/docs/en/SSEPEK_12.0.0/inst/src/tpc/db2z_tailorjobsclist.html).

Sample applications

The sample applications help you determine whether you installed or migrated Db2 correctly. Db2 provides a set of sample programs and procedures that help you determine if Db2 is operating correctly. For more information, see [Verifying successful Db2 12 installation or migration with sample applications](https://www.ibm.com/docs/en/SSEPEK_12.0.0/inst/src/tpc/db2z_verifyinstmigr.html).

All references to SYS1.PARMLIB also imply the logical PARMLIB data set that is used for Db2.

## Generating Db2 initialization code

Db2 executable parameters are prepared in a quick and simple procedure referred to as an assembly., which uses the supplied object code.

## Ability to defer decisions about Db2 characteristics

Db2 allows you to specify many subsystem characteristics during Db2 operation. You can modify initialization parameters, authorize users, define databases and tables, and tune Db2 while Db2 is running. Therefore, you can defer many decisions until after you finish installing or migrating Db2.

## Ability to update installation and migration options

During the process of installing or migrating, Db2 uses ISPF panels to prompt you for many options. Db2 allows you to update most of these options without requiring you to reinstall or remigrate. You can accept the default values for certain options and, after acquiring experience with Db2, tailor them to suit your needs.