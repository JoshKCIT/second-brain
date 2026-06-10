---
source_url: https://docs.informatica.com/integration-cloud/data-integration/current-version/getting-started/getting-started-with-informatica-cloud-data-integration.html
vendor: informatica
topic: cloud-data-integration-getting-started
fetched_at: 2026-05-28T00:48:49Z
revalidate_after: 2026-08-26T00:48:49Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:informatica
authority: standard
ingest_mode: defuddle
---

![](https://docs.informatica.com/etc/designs/informaticadita-com/images/h2l_bkgrnd_img.png)

## Getting Started

## Getting Started

[Back](https://docs.informatica.com/integration-cloud/data-integration/current-version/getting-started/preface.html) [Next](https://docs.informatica.com/integration-cloud/data-integration/current-version/getting-started/system-requirements.html)

## Getting Started with Informatica Cloud Data Integration

## Getting Started with Informatica Cloud Data Integration

You can create a data integration project in just a few steps.

## Step 1. Check system requirements

Be sure you're using a compatible browser when you're designing your projects, and check the

IDMC

Product Availability Matrix for operating systems, databases, and other systems that

Data Integration

supports.

## Step 2. Configure a runtime environment

A runtime environment is the execution platform for running tasks. A runtime environment consists of one or more Secure Agents. A Secure Agent is a lightweight program that runs tasks and enables secure communication across the firewall between your organization and

IDMC

. You must have at least one runtime environment in each organization so that users in the organization can run tasks.

## Step 3. Create a connection

Before you can use

Data Integration

to run data integration tasks, you need to create a connection. When you configure the connection, you specify the connector that enables the exchange of data between

Data Integration

and the source and target objects. For example, if you want to create a task that uses Salesforce data, you create a Salesforce connection. The Salesforce connection uses the Salesforce connector which enables the exchange of data between Salesforce and

Data Integration

.

## Step 4. Create your project

Organize your data integration projects in folders that contain assets such as mappings, tasks, and taskflows. Create a project folder and folders to contain the assets you need for your project.

After you set up folders, create your project assets. Assets include the following objects:
- Mappings
- Tasks
- Taskflows
- Components such as business services, mapplets, and hierarchical schemas

## Step 5. Add your project to the source control repository (optional)

If your organization is enabled for source control and the organization has read-write access to the source control repository, add your project to the repository.

Before you can add your project, your organization administrator must configure a link between the organization and source control repository, and you must specify your source control user credentials in

IDMC

.

## Step 6. Configure reference data properties (optional)

If your organization uses

Data Quality

, enter the license keys for verifier asset reference data files. You enter the license keys as runtime environment properties in

Administrator

. You do not need to take additional steps to download and install the reference data files.

When you run a mapping that uses a verifier asset, the Secure Agent checks for the presence of the reference data files that the asset reads and downloads any file that is absent in the runtime environment.

You can review and update the properties that relate to the reference data in

Administrator

.

Actions

Resources