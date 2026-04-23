---
quality: 8.9
quality: 8.2
kind: schema
id: bld_schema_terminal_backend
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for terminal_backend
title: "Schema Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, schema]
tldr: "Formal schema for terminal_backend: 6 backend types, auth model, resource limits, cost model"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_benchmark_suite
  - bld_schema_oauth_app_config
  - bld_schema_app_directory_entry
  - bld_schema_sandbox_config
  - bld_schema_playground_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
---

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | Yes | - | Must match naming pattern |
| kind | string | Yes | - | Always "terminal_backend" |
| pillar | string | Yes | - | Always "P09" |
| title | string | Yes | - | Human-readable backend name |
| backend_type | enum | Yes | - | local \| docker \| ssh \| daytona \| modal \| singularity |
| serverless | bool | Yes | false | True only for modal, daytona |
| hibernation_capable | bool | Yes | false | True only for daytona |
| auth.method | enum | Yes | none | none \| ssh_key \| api_token \| oauth |
| auth.secret_ref | string | No | null | Points to secret_config id if auth.method != none |
| limits.timeout_seconds | integer | Yes | 3600 | Max session lifetime; cannot be null |
| cost_model.billing | enum | Yes | free | free \| per_second \| per_task \| subscription |
| version | string | Yes | "1.0.0" | Semantic versioning |
| quality | float\|null | Yes | null | Peer-review score; null until reviewed |
| tags | list | Yes | [] | Lowercase keywords |

### Optional
| Field | Type | Notes |
|-------|------|-------|
| limits.cpu_cores | integer | null = provider default |
| limits.memory_gb | float | null = provider default |
| cost_model.estimated_usd_per_hour | float | null if free or unknown |

## ID Pattern
`^p09_tb_[a-z0-9_-]+$`

## Backend-Specific Validation

| backend_type | auth.method allowed | serverless | hibernation_capable |
|--------------|---------------------|------------|---------------------|
| local | none | false | false |
| docker | none | false | false |
| ssh | ssh_key | false | false |
| daytona | api_token, oauth | true | true |
| modal | api_token | true | false |
| singularity | none, ssh_key | false | false |

## Body Structure
1. **Backend Overview** -- type, purpose, nucleus owner
2. **Connection** -- backend-specific connection config block
3. **Resource Limits** -- cpu, memory, timeout table
4. **Authentication** -- method and secret reference
5. **Cost Model** -- billing mode and estimated cost

## Constraints
- Max file size: 3072 bytes
- ID must match regex pattern
- `limits.timeout_seconds` is required and must be a positive integer
- `backend_type` must be one of the 6 supported values exactly
- `serverless: true` is only valid for modal and daytona
- Tags must be lowercase and unique

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.52 |
| [[bld_schema_integration_guide]] | sibling | 0.52 |
| [[bld_schema_sandbox_spec]] | sibling | 0.51 |
| [[bld_schema_benchmark_suite]] | sibling | 0.50 |
| [[bld_schema_oauth_app_config]] | sibling | 0.49 |
| [[bld_schema_app_directory_entry]] | sibling | 0.48 |
| [[bld_schema_sandbox_config]] | sibling | 0.48 |
| [[bld_schema_playground_config]] | sibling | 0.48 |
| [[bld_schema_usage_report]] | sibling | 0.48 |
| [[bld_schema_dataset_card]] | sibling | 0.47 |
