---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
vendor: aws
topic: waf-overview
fetched_at: 2026-06-10T06:24:25Z
revalidate_after: 2026-08-09T06:24:25Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.md)

AWS WAF - AWS WAF, AWS Firewall Manager, AWS Shield Advanced, and AWS Shield network security director

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

## AWS WAF

AWS WAF is a web application firewall that lets you monitor the HTTP(S) requests that are forwarded to your protected web application resources. You can protect the following resource types:

- Amazon CloudFront distribution
- Amazon API Gateway REST API
- Application Load Balancer
- AWS AppSync GraphQL API
- Amazon Cognito user pool
- AWS App Runner service
- AWS Verified Access instance
- AWS Amplify

AWS WAF lets you control access to your content. Based on criteria that you specify, such as the IP addresses that requests originate from or the values of query strings, the service associated with your protected resource responds to requests either with the requested content, with an HTTP 403 status code (Forbidden), or with a custom response.

###### Note

You can also use AWS WAF to protect your applications that are hosted in Amazon Elastic Container Service (Amazon ECS) containers. Amazon ECS is a highly scalable, fast container management service that makes it easy to run, stop, and manage Docker containers on a cluster. To use this option, you configure Amazon ECS to use an Application Load Balancer that is enabled for AWS WAF to route and protect HTTP(S) layer 7 traffic across the tasks in your service. For more information, see [Service Load Balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide*.

###### Topics

- [Get started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)
- [How AWS WAF works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html)
- [Configuring protection in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)
- [AWS WAF rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html)
- [AWS WAF rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html)
- [Web ACL capacity units (WCUs) in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html)
- [Oversize web request components in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-oversize-request-components.html)
- [Supported regular expression syntax in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-support.html)
- [IP sets and regex pattern sets in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)
- [Customized web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html)
- [Web request labeling in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html)
- [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections.html)
- [Data protection and logging for AWS WAF protection pack (web ACL) traffic](https://docs.aws.amazon.com/waf/latest/developerguide/waf-data-protection-and-logging.html)
- [Testing and tuning your AWS WAF protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html)
- [Using AWS WAF with Amazon CloudFront](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html)
- [Security in your use of the AWS WAF service](https://docs.aws.amazon.com/waf/latest/developerguide/security.html)
- [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html)
- [Migrating your AWS WAF Classic resources to AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html)