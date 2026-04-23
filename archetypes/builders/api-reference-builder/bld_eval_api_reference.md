---
kind: quality_gate
id: p06_qg_api_reference
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for api_reference
quality: 9.0
title: "Quality Gate Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for api_reference"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_api_reference
  - bld_instruction_api_reference
  - bld_schema_api_reference
  - p10_lr_api_reference_builder
  - kc_api_reference
  - p05_qg_integration_guide
  - p04_qg_sdk_example
  - p03_sp_api_reference_builder
  - p11_qg_client
  - p09_qg_marketplace_app_manifest
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| ID pattern | ^p06_ar_[a-z][a-z0-9_]+.md$ | matches | all files |
| endpoint count | >= 1 | gte | artifact body |
| authentication documented | true | equals | all artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML |
| H02 | ID matches ^p06_ar_[a-z][a-z0-9_]+.md$ | invalid pattern |
| H03 | kind field matches 'api_reference' | incorrect kind |
| H04 | All endpoints listed | missing endpoint |
| H05 | Parameters/responses documented | incomplete spec |
| H06 | Authentication methods specified | missing auth details |
| H07 | Examples provided for all endpoints | no examples |
| H08 | Consistent formatting (YAML/Markdown) | inconsistent syntax |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Completeness | 0.20 | 100% endpoints/params/responses |
| D02 | Clarity | 0.15 | Readable descriptions/examples |
| D03 | Consistency | 0.15 | Uniform structure/formatting |
| D04 | Examples | 0.10 | 100% endpoints with examples |
| D05 | Auth details | 0.10 | Full auth method coverage |
| D06 | Versioning | 0.10 | API version specified |
| D07 | Structure | 0.10 | Valid table/section hierarchy |
| D08 | Language | 0.10 | English/technical accuracy |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-publish to prod |
| PUBLISH >=8.0 | Review for minor edits |
| REVIEW >=7.0 | Fix critical issues |
| REJECT <7.0 | Rewrite documentation |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Senior engineer approval | CTO | Requires written justification |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
