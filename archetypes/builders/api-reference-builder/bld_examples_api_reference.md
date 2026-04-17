---
kind: examples
id: bld_examples_api_reference
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of api_reference artifacts
quality: 8.9
title: "Examples Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, examples]
tldr: "Golden and anti-examples of api_reference artifacts"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
title: Stripe API Reference
description: REST API for payment processing
auth: API keys (https://stripe.com/docs/api/authentication)
version: 2023-10-12
---

# Stripe API Reference

## Customers

### Create Customer
**Method**: POST
**Path**: /v1/customers
**Params**:
- `email` (required, string)
- `name` (optional, string)
- `payment_method` (optional, string)

**Responses**:
- 200: {"id": "cus_123", "email": "user@example.com"}
- 400: {"error": "Invalid email format"}

**Example**:
```bash
curl https://api.stripe.com/v1/customers \
  -u sk_test_123: \
  -d email=user@example.com
```

## Repositories

### List Repos
**Method**: GET
**Path**: /repos/{owner}/{repo}/branches
**Params**:
- `owner` (required, string)
- `repo` (required, string)

**Responses**:
- 200: [{"name": "main", "commit": {"sha": "abc123"}}]
- 404: {"error": "Repository not found"}
```

## Anti-Example 1: Missing Authentication
```markdown
# GitHub API Reference

## Repositories

### List Repos
**Method**: GET
**Path**: /user/repos
**Params**:
- `sort` (optional, string)

**Responses**:
- 200: [{"name": "repo1", "owner": "user"}]
```
## Why it fails
No authentication method specified. Developers can't securely use the API without knowing required credentials (e.g., OAuth tokens).

## Anti-Example 2: Incomplete Parameters
```markdown
# AWS S3 API Reference

## Create Bucket

**Method**: PUT
**Path**: /buckets/{bucketName}
**Params**:
- `bucketName` (required, string)

**Responses**:
- 200: {"Location": "https://s3.amazonaws.com/bucketName"}
```
## Why it fails
Missing critical parameters like region, ACL settings, and encryption options. Developers can't fully configure bucket creation without essential details.
