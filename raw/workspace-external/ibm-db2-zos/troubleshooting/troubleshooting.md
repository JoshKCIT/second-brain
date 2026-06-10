---
source_url: https://www.ibm.com/docs/en/SSEPEK_12.0.0/trbshoot/src/tpc/db2z_trbshoothome.html
vendor: ibm-db2-zos
topic: troubleshooting
fetched_at: 2026-06-10T06:35:44Z
revalidate_after: 2026-09-08T06:35:44Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:ibm-db2-zos
authority: standard
ingest_mode: defuddle
---

## Troubleshooting problems in Db2

The topics about troubleshooting Db2 problems provide a variety of information that can help you when you have problems associated with the Db2 for z/OS® product. IBM® Support personnel might ask you to refer to troubleshooting information when they help you with a specific problem.

Licensed diagnosis information: ![Start of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/trbshoot/delta.gif)

The Db2 Diagnosis Guide and Reference, which was available as a licensed publication for earlier Db2 releases, is not available with Db2 12. However, the content remains available:
- Most of the information from the Db2 Diagnosis Guide and Reference is now available without restriction in Troubleshooting problems in Db2 (this section) in the Db2 product documentation, or in the downloadable PDF manual, [Troubleshooting for Db2](https://www.ibm.com/docs/en/SSEPEK_12.0.0/pdf/db2z_12_trbshootbook.pdf "(Opens a PDF file)").
- The remaining information is available available in a downloadable PDF that is accessible when your IBMid is associated with an active Db2 product license. See [Db2 12 for z/OS licensed diagnosis information](https://www.ibm.com/support/pages/node/6413411 "(Opens in a new tab or window)").

![End of change](https://www.ibm.com/docs/en/SSEPEK_12.0.0/trbshoot/deltaend.gif)

Troubleshooting is a systematic approach to solving a problem. The goal of troubleshooting is to determine why something does not work as expected and how to resolve the problem.

The first step in the troubleshooting process is to describe the problem completely. Problem descriptions help you and the IBM technical-support representative know where to start to find the cause of the problem. This step includes asking yourself basic questions:
- What are the symptoms of the problem?
- Where does the problem occur?
- When does the problem occur?
- Under which conditions does the problem occur?
- Can the problem be reproduced?

The answers to these questions typically lead to a good description of the problem, which can then lead you a problem resolution.

## What are the symptoms of the problem?

When starting to describe a problem, the most obvious question is "What is the problem?" This question might seem straightforward; however, you can break it down into several more-focused questions that create a more descriptive picture of the problem. These questions can include:
- Who, or what, is reporting the problem?
- What are the error codes and messages?
- How does the system fail? For example, is it a loop, hang, crash, performance degradation, or incorrect result?

## Where does the problem occur?

Determining where the problem originates is not always easy, but it is one of the most important steps in resolving a problem. Many layers of technology can exist between the reporting and failing components. Networks, disks, and drivers are only a few of the components to consider when you are investigating problems.

The following questions help you to focus on where the problem occurs to isolate the problem layer:
- Is the problem specific to one platform or operating system, or is it common across multiple platforms or operating systems?
- Is the current environment and configuration supported?

If one layer reports the problem, the problem does not necessarily originate in that layer. Part of identifying where a problem originates is understanding the environment in which it exists. Take some time to completely describe the problem environment, including the operating system and version, all corresponding software and versions, and hardware information. Confirm that you are running within an environment that is a supported configuration; many problems can be traced back to incompatible levels of software that are not intended to run together or have not been fully tested together.

## When does the problem occur?

Develop a detailed timeline of events leading up to a failure, especially for those cases that are one-time occurrences. You can most easily develop a timeline by working backward: Start at the time an error was reported (as precisely as possible, even down to the millisecond), and work backward through the available logs and information. Sometimes, you need to look only as far as the first suspicious event that you find in a diagnostic log.

To develop a detailed timeline of events, answer these questions:
- Does the problem happen only at a certain time of day or night?
- How often does the problem happen?
- What sequence of events leads up to the time that the problem is reported?
- Does the problem happen after an environment change, such as upgrading or installing software or hardware?

Responding to these types of questions can give you a frame of reference in which to investigate the problem.

## Under which conditions does the problem occur?

Knowing which systems and applications are running at the time that a problem occurs is an important part of troubleshooting. These questions about your environment can help you to identify the root cause of the problem:
- Does the problem always occur when the same task is being performed?
- Does a certain sequence of events need to occur for the problem to surface?
- Do any other applications fail at the same time?

Answering these types of questions can help you explain the environment in which the problem occurs and correlate any dependencies. Remember that just because multiple problems might have occurred around the same time, the problems are not necessarily related.

## Can the problem be reproduced?

From a troubleshooting standpoint, the ideal problem is one that can be reproduced. Typically, when a problem can be reproduced you have a larger set of tools or procedures at your disposal to help you investigate. Consequently, problems that you can reproduce are often easier to debug and solve. However, problems that you can reproduce can have a disadvantage: If the problem is of significant business impact, you do not want it to recur. If possible, re-create the problem in a test or development environment, which typically offers you more flexibility and control during your investigation.
- Can the problem be re-created on a test system?
- Are multiple users or applications encountering the same type of problem?
- Can the problem be re-created by running a single command, a set of commands, or a particular application?