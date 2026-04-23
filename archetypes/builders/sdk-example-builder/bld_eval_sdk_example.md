---
kind: quality_gate
id: p04_qg_sdk_example
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sdk_example
quality: 9.0
title: "Quality Gate Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sdk_example"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_sdk_example
  - p05_qg_integration_guide
  - p04_qg_stt_provider
  - p09_qg_marketplace_app_manifest
  - p05_qg_github_issue_template
  - p11_qg_content_filter
  - p07_qg_benchmark_suite
  - p06_qg_api_reference
  - p01_qg_graph_rag_config
  - p11_qg_audit_log
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Code Example Completeness | 100% | equals | per language |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p04_sdk_[a-z][a-z0-9_]+.md$ | filename does not match schema |
| H03 | kind field matches 'sdk_example' | kind field is incorrect |
| H04 | Error handling demonstrated | no error handling examples present |
| H05 | API versioning used | missing or incorrect API versioning |
| H06 | Documentation comments present | code lacks inline documentation |
| H07 | Example covers all integration patterns | incomplete pattern coverage |
| H08 | Licensing statement included | missing or invalid license notice |
| H09 | No security vulnerabilities | code contains insecure practices |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Code clarity | 0.20 | Readable, well-structured code |
| D02 | Completeness | 0.20 | All required patterns implemented |
| D03 | Error handling | 0.20 | Robust error handling examples |
| D04 | Documentation | 0.15 | Clear inline comments and README |
| D05 | Licensing | 0.05 | Valid license notice present |
| D06 | Security | 0.10 | No insecure practices detected |
| D07 | Language support | 0.05 | Examples for all supported languages |
| D08 | API versioning | 0.05 | Correct API versioning used |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-approve and publish |
| PUBLISH >=8.0 | Manual review required before publish |
| REVIEW >=7.0 | Flag for team review |
| REJECT <7.0 | Reject and request revisions |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Approved by CTO for urgent release | CTO | CTO approval recorded in JIRA |

## Examples

## Golden Example
```yaml
title: "AWS S3 File Upload with Boto3"
language: python
vendor: Amazon Web Services
description: "Uploads a file to an S3 bucket using AWS SDK for Python (Boto3)"
```

```python
import boto3
import os

def upload_to_s3(file_path, bucket_name, object_key):
    """Upload file to S3 bucket."""
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise
```

## Anti-Example 1: Missing Error Handling
```python
import boto3

def upload_to_s3(file_path, bucket_name, object_key):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{object_key}")
```

## Why it fails
No exception handling leaves the application vulnerable to crashes from network errors, permission issues, or invalid inputs. Missing error feedback makes debugging impossible.

## Anti-Example 2: Hardcoded Credentials
```python
import boto3

def upload_to_s3(file_path, bucket_name, object_key):
    s3_client = boto3.client('s3', aws_access_key_id='AKIAXXXXXXXXXXXXXXXX',
                             aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    s3_client.upload_file(file_path, bucket_name, object_key)
```

## Why it fails
Hardcoding credentials violates security best practices. It exposes sensitive information in code repositories and increases risk of credential leakage. Proper approach uses environment variables or IAM roles.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
