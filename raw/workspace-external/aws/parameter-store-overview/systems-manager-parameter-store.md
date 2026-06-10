---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
vendor: aws
topic: parameter-store-overview
fetched_at: 2026-06-10T06:24:18Z
revalidate_after: 2026-08-09T06:24:18Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.md)

AWS Systems Manager Parameter Store - AWS Systems Manager

## AWS Systems Manager Parameter Store

Parameter Store enables you to securely store, organize, and retrieve configuration simple configuration data at scale. It is designed to simplify configuration management across environments, allowing teams to standardize how applications access critical data without hardcoding values or relying on fragmented storage solutions.

Beyond simple storage, Parameter Store provides versioning, access control through AWS Identity and Access Management (IAM), and seamless integration with other AWS services such as Amazon EC2, Lambda, and CloudFormation. This enables dynamic configuration updates without requiring code changes or redeployments, improving operational agility and reducing risk. With features like hierarchical naming, parameter policies, and change tracking, Parameter Store helps teams maintain consistency, enforce governance, and build more secure and maintainable systems.

Parameter Store supports `String`, `StringList`, and `SecureString` parameter types. `String` and `StringList` parameter values are stored as plain text. `SecureString` parameters encrypt values using AWS Key Management Service, making them a practical choice for lightweight encrypted configuration values that don't require rotation or other advanced secret lifecycle capabilities. For more information about parameter types, see [Understanding parameter types](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-a-parameter.html)

###### Note

If you manage credentials that require automatic rotation, cross-account access, or fine-grained audit logging, we recommend using [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com//secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

Here are some examples of the types of configuration data you can store and manage in Parameter Store:

- **Database connection strings (non-rotating)** – jdbc:mysql://host:3306/appdb
- **Application environment variables** – ENV=production, LOG\_LEVEL=debug
- **Service endpoint URLs** – internal microservice endpoints or third-party base URLs
- **Resource identifiers** – S3 bucket names, DynamoDB table names, ARNs
- **Application tuning parameters** – cache TTLs, batch sizes, polling intervals

###### Note

We *don't* recommend using Parameter Store for the following types of configuration data:

- Feature flags
- Operational levers like timeouts
- Allow lists and block lists
- Circuit breakers
- Dynamic configurations

For these types of configuration data, use AWS AppConfig. For more information, see [What is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html).

## Parameter Store features

Parameter Store includes the following features for managing parameters:

- **Share parameters with other accounts**
	Centralize configuration data in a single AWS account and share parameters with other accounts that need access. For more information, see [Working with shared parameters in Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html).
- **OS Patching**
	Amazon EC2 lets you specify the operating system for new instances by [referencing a parameter instead of hardcoding an AMI (AMI) ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-systems-manager-parameter-to-find-AMI.html.html). This approach ensures your instances automatically use the latest patched and updated images. AWS and operating system vendors provide [public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-finding-public-parameters.html) that track current AMI versions, so you don't have to manage updates manually. You can also define your own parameters to reference a centrally managed golden AMI, making it easier to enforce consistent, approved configurations across your organization.
- **Accessible from other AWS services**
	Other AWS services allow you to easily reference parameter values. Here are some examples:
	- Lambda functions can retrieve parameters and secrets using the [Parameters and Secrets Lambda Extension](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html).
	- Amazon Elastic Container Service and AWS Fargate allow you to [inject environmental variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.html) whose values are managed centrally in parameter store.
	- AWS CloudFormation templates can reference [parameter values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references-ssm.html).
	- AWS AppConfig enables you to create [configuration profiles that reference parameters](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-console.html), allowing you to safely deploy configuration changes using features such as gradual rollouts, alarm-based rollbacks, and built-in data validation.
	- AWS CodeBuild allows you to [define environmental variables](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) whose values are dynamically retrieved from Parameter Store at build time.
- **Parameter History**
	Parameter Store retains the 100 most recent [versions](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-versions.html) of each parameter, so you can quickly review and reconstruct previous values when investigating operational issues.
- **Events and notifications**
	Automate workflows in Parameter Store by subscribing to parameter [change events](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-cwe.html). You can also use [change events](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) to enforce expiration and receive notifications when a parameter hasn’t been rotated within a specified timeframe.
- **Organize parameters hierarchically**
	Use [parameter hierarchies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html) to group related parameters, making it easier to discover, manage, and filter them across environments and applications.

## Parameter tiers

Parameter Store offers multiple parameter tiers that affect cost, scale, and performance. You individually configure parameters to use either the standard-parameter tier (the default tier) or the advanced-parameter tier.

Use:

- Standard parameters for most configuration data and low-scale workloads
- Advanced parameters when you need higher limits, larger values, or parameter policies

###### Important

You can upgrade a parameter from standard to advanced, but you cannot downgrade it.

The following table describes the differences between parameter tiers.

| Feature | Standard | Advanced |
| --- | --- | --- |
| Maximum parameters  (per AWS account and AWS Region) | 10,000 | 100,000 |
| Maximum value size | 4 KB | 8 KB |
| Parameter policies | Not supported | Supported  For more information, see [Assigning parameter policies in Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html). |
| Share parameters across AWS accounts | Not supported | Supported  For more information, see [Working with shared parameters in Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html). |
| Cost | No additional charge | Charges apply  For more information, see [AWS Systems Manager Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store). |

For more information about parameter tiers and their features, see [Managing tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html).

For a complete list of Parameter Store quotas and limits, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#parameter-store) in the *AWS General Reference*.

## Performance and throughput

Parameter Store provides a default throughput suitable for lower scale workloads. For applications that require higher request rates, you can enable higher throughput.

- Default throughput is sufficient for typical configuration retrieval patterns.
- High-throughput mode supports significantly higher request rates for large-scale or latency-sensitive applications.
- Additional charges apply when higher throughput is enabled.

If your application retrieves parameters frequently or at scale, evaluate throughput settings early to avoid throttling. For information about enabling high-throughput, see [Changing Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html).

## How to retrieve parameters

You can retrieve parameters from Parameter Store using the AWS Management Console, AWS CLI, or AWS SDKs to call the following API actions:

- [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html)
- [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html)
- [API\_GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html)

**AWS CLI**: The following table includes sample AWS CLI commands for Parameter Store.

| Command | Usage | Best For |
| --- | --- | --- |
| get-parameter | aws ssm get-parameter --name " `name` " | Fetching one specific parameter value. |
| get-parameter | aws ssm get-parameter --name " `name` " --with-decryption | Fetching `SecureString` parameter types. Note – you must include the `--with-decryption` flag to see the plaintext value; otherwise, you will only receive the encrypted metadata. |
| get-parameters | aws ssm get-parameters --names " `name1` " " `name2` " | Fetching up to 10 specific, unrelated parameters at once. |
| get-parameters-by-path | aws ssm get-parameters-by-path --path " `/my/app/path/` " | Bulk retrieval of an entire environment's configuration. |
| get-parameter-history | aws ssm get-parameter-history --name " `name` " | Checking how a value has changed over time. |

**SDKs (e.g., Boto3 for Python)**: Use methods like `get_parameter()` or `get_parameters_by_path()` within your application code to fetch values at runtime.

**CDK and CloudFormation**:

- **AWS CDK**: Use `valueForStringParameter` or `valueFromLookup` to read values during synthesis or deployment.
- **CloudFormation**: Use dynamic references like `{{resolve:ssm:parameter-name:version}}` to inject values directly into templates.

###### Note

For most dynamic parameter references, you specify the parameter name by using the following convention:

{{ `` ssm:`parameter-name` `` }}

To get started with Parameter Store, see [Setting up Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-setting-up.html).