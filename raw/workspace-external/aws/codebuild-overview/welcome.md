---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html
vendor: aws
topic: codebuild-overview
fetched_at: 2026-06-10T06:24:06Z
revalidate_after: 2026-08-09T06:24:06Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.md)

What is AWS CodeBuild? - AWS CodeBuild

AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers. It provides prepackaged build environments for popular programming languages and build tools such as Apache Maven, Gradle, and more. You can also customize build environments in CodeBuild to use your own build tools. CodeBuild scales automatically to meet peak build requests.

CodeBuild provides these benefits:

- **Fully managed** – CodeBuild eliminates the need to set up, patch, update, and manage your own build servers.
- **On demand** – CodeBuild scales on demand to meet your build needs. You pay only for the number of build minutes you consume.
- **Out of the box** – CodeBuild provides preconfigured build environments for the most popular programming languages. All you need to do is point to your build script to start your first build.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## How to run CodeBuild

You can use the AWS CodeBuild or AWS CodePipeline console to run CodeBuild. You can also automate the running of CodeBuild by using the AWS Command Line Interface (AWS CLI) or the AWS SDKs.

![The diagram shows how CodeBuild works with AWS CLI or AWS SDKs.](https://docs.aws.amazon.com/images/codebuild/latest/userguide/images/overview.png)

As the following diagram shows, you can add CodeBuild as a build or test action to the build or test stage of a pipeline in AWS CodePipeline. AWS CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the steps required to release your code. This includes building your code. A *pipeline* is a workflow construct that describes how code changes go through a release process.

![The diagram shows how CodeBuild works with AWS CodePipeline.](https://docs.aws.amazon.com/images/codebuild/latest/userguide/images/pipeline.png)

To use CodePipeline to create a pipeline and then add a CodeBuild build or test action, see [Use CodeBuild with CodePipeline](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html). For more information about CodePipeline, see the [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/).

The CodeBuild console also provides a way to quickly search for your resources, such as repositories, build projects, deployment applications, and pipelines. Choose **Go to resource** or press the `/` key, and then enter the name of the resource. Any matches appear in the list. Searches are case insensitive. You only see resources that you have permissions to view. For more information, see [Viewing resources in the console](https://docs.aws.amazon.com/codebuild/latest/userguide/console-resources.html).

## Pricing for CodeBuild

For information, see [CodeBuild pricing](https://aws.amazon.com/codebuild/pricing).

## How do I get started with CodeBuild?

We recommend that you complete the following steps:

1. **Learn** more about CodeBuild by reading the information in [Concepts](https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html).
2. **Experiment** with CodeBuild in an example scenario by following the instructions in [Getting started using the console](https://docs.aws.amazon.com/codebuild/latest/userguide/getting-started-overview.html#getting-started).
3. **Use** CodeBuild in your own scenarios by following the instructions in [Plan a build](https://docs.aws.amazon.com/codebuild/latest/userguide/planning.html).