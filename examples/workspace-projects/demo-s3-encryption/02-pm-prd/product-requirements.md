---
title: "S3 Bucket Encryption Baseline - Requirements"
type: project-artifact
project: "demo-s3-encryption"
stage: pm-prd
status: published
authored_by_agent: pm
domain: vendor:aws
authority: standard
sources:
  - "raw/workspace-external/aws/s3-server-side-encryption/using-server-side-encryption.md"
created: 2026-06-11
updated: 2026-06-11
---

## What this is

A minimal, worked requirements artifact showing the shape of a published
project document that cites a vendor source and clears the deterministic
align-cite gate. It is a reference for adopters, not live project state.

## Requirement

New objects written to project S3 buckets must be encrypted at rest using
server-side encryption with Amazon S3 managed keys (SSE-S3) or stronger. This is
the platform baseline; teams needing customer-managed key control may layer
SSE-KMS on top.

AWS applies this baseline automatically. As the AWS S3 user guide states:

> All new object uploads to Amazon S3 buckets are encrypted by default with server-side encryption with Amazon S3 managed keys (SSE-S3).

Because encryption is automatic, the requirement is verified by auditing that no
bucket policy disables default encryption, rather than by adding upload-time
encryption headers.

## Acceptance criteria

- Every project bucket reports default encryption enabled.
- No bucket policy removes or downgrades the SSE-S3 baseline.
- Buckets requiring audited key control use SSE-KMS with a customer-managed key.

## See Also

- [Using server-side encryption (AWS S3 user guide)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)
