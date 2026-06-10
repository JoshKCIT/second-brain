---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html
vendor: aws
topic: acm-overview
fetched_at: 2026-06-10T06:24:05Z
revalidate_after: 2026-08-09T06:24:05Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.md)

What is AWS Certificate Manager? - AWS Certificate Manager

[Supported Regions](#acm-regions) [Pricing](#acm-billing)

## What is AWS Certificate Manager?

AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications. You can provide certificates for your [integrated AWS services](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html) either by issuing them directly with ACM or by [importing](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) third-party certificates into the ACM management system. ACM certificates can secure singular domain names, multiple specific domain names, wildcard domains, or combinations of these. ACM wildcard certificates can protect an unlimited number of subdomains. You can also [export](https://docs.aws.amazon.com/acm/latest/userguide/export-private.html) ACM certificates signed by AWS Private CA for use anywhere in your internal PKI.

###### Note

ACM is not intended for use with a stand-alone web server. If you want to set up a stand-alone secure server on an Amazon EC2 instance, the following tutorial has instructions: [Configure SSL/TLS on Amazon Linux 2023](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2023.html).

## Supported Regions

ACM supports IPv4 and IPv6 on public endpoints. Visit [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#acm_region) in the *AWS General Reference* or the [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) to see the regional availability for ACM.

Certificates in ACM are regional resources. To use a certificate with Elastic Load Balancing for the same fully qualified domain name (FQDN) or set of FQDNs in more than one AWS region, you must request or import a certificate for each region. For certificates provided by ACM, this means you must revalidate each domain name in the certificate for each region. You cannot copy a certificate between regions.

To use an ACM certificate with Amazon CloudFront, you must request or import the certificate in the US East (N. Virginia) region. ACM certificates in this region that are associated with a CloudFront distribution are distributed to all the geographic locations configured for that distribution.

## Pricing for AWS Certificate Manager

You are not subject to an additional charge for SSL/TLS certificates that you manage with AWS Certificate Manager. You pay only for the AWS resources that you create to run your website or application. For the latest ACM pricing information, see the [AWS Certificate Manager Service Pricing](https://aws.amazon.com/certificate-manager/pricing/) page on the AWS website.