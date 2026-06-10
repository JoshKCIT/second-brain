---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_prepareapplication.html
vendor: ibm-db2-zos
topic: prepare-application
fetched_at: 2026-06-10T06:35:51Z
revalidate_after: 2026-09-08T06:35:51Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Preparing an application to run on Db2 for z/OS

To prepare and run applications that contain embedded static SQL statements or dynamic SQL statements, you must process, compile, link-edit, and bind the SQL statements.

## Before you begin

To avoid rework, follow these steps:

1. Test your SQL statements by using SPUFI.
2. Compile your program with no SQL statements, and resolve all compiler errors.
3. Proceed with the preparation and the Db2 precompiler or with the host compiler that supports that Db2 coprocessor.

The following types of applications require different methods of program preparation:
- Applications that contain ODBC calls
- Applications in interpreted languages, such as REXX. For information about running REXX programs, which you do not prepare for execution, see [Running a Db2 REXX application](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_runrexxapp.html#db2z_runrexxapp "You run Db2 REXX applications under TSO. You do not precompile, compile, link-edit, or bind Db2 REXX applications before you run them.").
- Java™ applications, which can contain JDBC calls or embedded SQL statements

## About this task

Before you can run an application program on Db2 for z/OS®, you need to prepare it. To prepare the program, you create a load module, possibly one or more packages, and an application plan.

If your application program includes SQL statements, you need to process those SQL statements by using either the Db2 coprocessor that is provided with a compiler or the Db2 precompiler.

Tip: ![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/delta.gif) The Db2 coprocessor is the recommended method for processing SQL statements in application programs. Compared to the Db2 precompiler, the Db2 coprocessor has fewer restrictions on SQL programs, and more fully supports the latest SQL and programming language enhancements. See [Processing SQL statements by using the Db2 coprocessor](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_processsqlstmtcoprocessor.html).![End of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/deltaend.gif)

Both the Db2 coprocessor and the Db2 precompiler perform the following actions:
- Replace the SQL statements in your source programs with calls to Db2 language interface modules
- Create a database request module (DBRM), which communicates your SQL requests to Db2 during the bind process

Db2 coprocessor

The following figure illustrates the program preparation process when you use the Db2 coprocessor. The process is similar to the process with the Db2 precompiler, except that the Db2 coprocessor does not create modified source for your application program. For more information, see [Processing SQL statements by using the Db2 coprocessor](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_processsqlstmtcoprocessor.html).

![Begin figure description. This figure shows that you precompile the SQL statements, and then you bind the DBRM to a plan or package before running the DB2 application. Alternately, the DB2 coprocessor combines the precompile and compile steps, and does not create modified source for your application program. End figure description.](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/art/db2z_applicationprep.svg)

Figure 1. Overview of the program preparation process for applications that contain embedded SQL. The Db2 coprocessor can combine the precompile and compile steps for certain languages.

Db2 precompiler

After you process SQL statements in your source program by using the Db2 precompiler, you create a load module, possibly one or more packages, and an application plan. Creating a load module involves compiling the modified source code that is produced by the precompiler into an object program, and link-editing the object program to create a load module. Creating a package or an application plan, a process unique to Db2, involves binding one or more DBRMs, which are created by the Db2 precompiler, by using the BIND PACKAGE command. For more information, see [Processing SQL statements by using the Db2 precompiler](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_processsqlprecompiler.html).

## Procedure

Complete the tasks by using one of the methods described below:
1. [Processing SQL statements for program preparation](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_processsqlstmt.html#db2z_processsqlstmt "The first step in preparing an SQL application to run is to process the SQL statements in the program. To process the statements, use the Db2 coprocessor or the Db2 precompiler. During this step, the SQL statements are replaced with calls to Db2 language interface modules, and a DBRM is created.")
2. [Compiling and link-editing an application](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_compilelinkeditapp.html#db2z_compilelinkeditapp "If you use the Db2 coprocessor, you process SQL statements as you compile your program, and the next step is the link edit the program. The purpose of the link-edit step is to produce an executable load module.")
3. [Binding application packages and plans](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_bindapp.html#db2z_bindapp "You must bind the DBRM that is produced by the SQL statement processor to a package before your Db2 application can run. The bind process establishes a relationship between an application program and its relational data.")
4. [Running an application on Db2 for z/OS](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_runapplication.html#db2z_runapplication "You can run your application after you have processed the SQL statements, compiled and link-edited the application, and bound the application.")

Binding a package is not necessary in all cases. These instructions assume that you bind some of your DBRMs into packages and include a package list in your plan.

If you use CICS®, you might need to complete additional steps. For more information, see:
- [Translating command-level statements in a CICS program](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_translatestmtcics.html#db2z_translatestmtcics "You can translate CICS applications with the CICS command language translator as a part of the program preparation process. CICS command language translators are available only for assembler, C, COBOL, and PL/I languages.")
- [Example of calling applications in a command procedure](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_xmpcallapps.html)

You can use the following methods to complete the program preparation tasks:

- **Preparing applications by using JCL procedures**
	A number of methods are available for preparing an application to run. You can:
	- Use Db2 interactive (DB2I) panels, which lead you step by step through the preparation process.
	- Submit a background job using JCL (which the program preparation panels can create for you).
	- Start the DSNH CLIST in TSO foreground or background.
	- Use TSO prompters and the DSN command processor.
	- Use JCL procedures added to your SYS1.PROCLIB (or equivalent) at Db2 installation time.
	- ![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/delta.gif)
		Start of change
		If the DBRM is generated in a HFS file, you can also use the Db2 command line processor to bind the resulting DBRM. Optionally, you can also copy the DBRM into a partitioned data set member by using the oput and oget commands and then bind it by using conventional JCL.
	This topic describes how to use JCL procedures to prepare a program. For information about using the DB2I panels, see [Preparing an application to run on Db2 for z/OS](https://www.ibm.com/docs/en/SSEPEK_12.0.0/apsg/src/tpc/db2z_prepareapplication.html#db2z_prepareapplication "To prepare and run applications that contain embedded static SQL statements or dynamic SQL statements, you must process, compile, link-edit, and bind the SQL statements.").
- **Preparing applications by the Db2 Program Preparation panels**
	If you develop programs using TSO and ISPF, you can prepare them to run by using the Db2 Program Preparation panels. These panels guide you step by step through the process of preparing your application to run. Other ways of preparing a program to run are available, but using Db2 Interactive (DB2I) is the easiest because it leads you automatically from task to task.
	Important: If your C++ program satisfies both of the following conditions, you must use a JCL procedure to prepare it:
	- The program consists of more than one data set or member.
	- More than one data set or member contains SQL statements.
	To prepare an application by using the Db2 Program Preparation panels:
	1. If you want to display or suppress message IDs during program preparation, specify one of the following commands on the ISPF command line:
		`TSO PROFILE MSGID`
		Message IDs are displayed
		`TSO PROFILE NOMSGID`
		Message IDs are supressed
	2. Open the DB2I Primary Option Menu.
	3. Select the option that corresponds to the Program Preparation panel.
	4. Complete the Program Preparation panel and any subsequent panels. After you complete each panel, DB2I automatically displays the next appropriate panel.
- **Preparation guidelines for DL/I batch programs**
	Use the following guidelines when you prepare a program to access Db2 and DL/I in a batch program: