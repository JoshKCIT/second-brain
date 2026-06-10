---
source_url: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html
vendor: aws
topic: cognito-overview
fetched_at: 2026-06-10T06:24:07Z
revalidate_after: 2026-08-09T06:24:07Z
fetched_by_query: seed-vendor-docs.py stack bootstrap
domain: vendor:aws
authority: standard
ingest_mode: defuddle
---

[View a markdown version of this page](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.md)

Amazon Cognito identity pools - Amazon Cognito

An Amazon Cognito identity pool is a directory of federated identities that you can exchange for AWS credentials. Identity pools generate temporary AWS credentials for the users of your app, whether they’ve signed in or you haven’t identified them yet. With AWS Identity and Access Management (IAM) roles and policies, you can choose the level of permission that you want to grant to your users. Users can start out as guests and retrieve assets that you keep in AWS services. Then they can sign in with a third-party identity provider to unlock access to assets that you make available to registered members. The third-party identity provider can be a consumer (social) OAuth 2.0 provider like Apple or Google, a custom SAML or OIDC identity provider, or a custom authentication scheme, also called a *developer provider*, of your own design.

###### Features of Amazon Cognito identity pools

**Sign requests for AWS services**

[Sign API requests](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) to AWS services like Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB. Analyze user activity with services like Amazon Pinpoint and Amazon CloudWatch.

**Filter requests with resource-based policies**

Exercise granular control over user access to your resources. Transform user claims into [IAM session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html), and build IAM policies that grant resource access to distinct subsets of your users.

**Assign guest access**

For your users who haven’t signed in yet, configure your identity pool to generate AWS credentials with a narrow scope of access. Authenticate users through a single sign-on provider to elevate their access.

**Assign IAM roles based on user characteristics**

Assign a single IAM role to all of your authenticated users, or choose the role based on the claims of each user.

**Accept a variety of identity providers**

Exchange an ID or access token, a user pool token, a SAML assertion, or a social-provider OAuth token for AWS credentials.

**Validate your own identities**

Perform your own user validation and use your developer AWS credentials to issue credentials for your users.

You might already have an Amazon Cognito user pool that provides authentication and authorization services to your app. You can set up your user pool as an identity provider (IdP) to your identity pool. When you do, your users can authenticate through your user pool IdPs, consolidate their claims into a common OIDC identity token, and exchange that token for AWS credentials. Your user can then present their credentials in a signed request to your AWS services.

You can also present authenticated claims from any of your identity providers directly to your identity pool. Amazon Cognito customizes user claims from SAML, OAuth, and OIDC providers into an [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) API request for short-term credentials.

Amazon Cognito user pools are like OIDC identity providers to your SSO-enabled apps. Identity pools act as an *AWS* identity provider to any app with resource dependencies that work best with IAM authorization.

Amazon Cognito identity pools support the following identity providers:

- Public providers: [Setting up Login with Amazon as an identity pools IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon.html), [Setting up Facebook as an identity pools IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/facebook.html), [Setting up Google as an identity pool IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/google.html), [Setting up Sign in with Apple as an identity pool IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/apple.html), Twitter.
- [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)
- [Setting up an OIDC provider as an identity pool IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/open-id.html)
- [Setting up a SAML provider as an identity pool IdP](https://docs.aws.amazon.com/cognito/latest/developerguide/saml-identity-provider.html)
- [Developer-authenticated identities](https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html)

For information about Amazon Cognito identity pools Region availability, see [AWS Service Region Availability](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

For more information about Amazon Cognito identity pools, see the following topics.

###### Topics

- [Identity pools console overview](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)
- [Identity pools authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html)
- [IAM roles](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html)
- [Security best practices for Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools-security-best-practices.html)
- [Using attributes for access control](https://docs.aws.amazon.com/cognito/latest/developerguide/attributes-for-access-control.html)
- [Using role-based access control](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html)
- [Getting credentials](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-credentials.html)
- [Accessing AWS services with temporary credentials](https://docs.aws.amazon.com/cognito/latest/developerguide/accessing-aws-services.html)
- [Identity pools third-party identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html)
- [Developer-authenticated identities](https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html)
- [Switching unauthenticated users to authenticated users](https://docs.aws.amazon.com/cognito/latest/developerguide/switching-identities.html)