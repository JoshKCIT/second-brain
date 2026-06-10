---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html
vendor: aws
topic: opensearch-serverless-overview
fetched_at: 2026-06-10T06:24:17Z
revalidate_after: 2026-08-09T06:24:17Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.md)

Amazon OpenSearch Serverless - Amazon OpenSearch Service

[Benefits](#serverless-benefits)

## Amazon OpenSearch Serverless

Amazon OpenSearch Serverless is an on-demand, auto-scaling configuration for Amazon OpenSearch Service. Unlike provisioned OpenSearch domains, which require manual capacity management, an OpenSearch Serverless collection automatically scales compute resources based on your application's needs.

OpenSearch Serverless offers a cost-effective solution for workloads that are infrequent, intermittent, or unpredictable. It optimizes costs by automatically scaling compute capacity based on your application's usage. Serverless collections use the same high-capacity, distributed, and highly available storage volume as provisioned OpenSearch Service domains.

OpenSearch Serverless collections are always encrypted. You can choose the encryption key, but you can't disable encryption. For more information, see [Encryption in Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html).

## Benefits

OpenSearch Serverless has the following benefits:

- **Simpler than provisioned** – OpenSearch Serverless removes much of the complexity of managing OpenSearch clusters and capacity. It automatically sizes and tunes your clusters, and takes care of shard and index lifecycle management. It also manages service software updates and OpenSearch version upgrades. All updates and upgrades are non-disruptive.
- **Cost-effective** – When you use OpenSearch Serverless, you only pay for the resources that you consume. This removes the need for upfront provisioning and overprovisioning for peak workloads.
- **Highly available** – OpenSearch Serverless supports production workloads with redundancy to protect against Availability Zone outages and infrastructure failures.
- **Scalable** – OpenSearch Serverless automatically scales resources to maintain consistently fast data ingestion rates and query response times.