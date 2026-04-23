---
kind: schema
id: bld_schema_sandbox_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for sandbox_config
quality: 9.1
title: "Schema Sandbox Config"
version: "1.0.1"
author: wave1_builder_gen
tags: [sandbox_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for sandbox_config"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-18"
last_reviewed: "2026-04-18"
density_score: 0.85
related:
  - bld_schema_sandbox_spec
  - bld_schema_usage_report
  - bld_schema_playground_config
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_api_reference
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_rl_algorithm
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | Yes      | -       | Must match ID pattern |  
| kind       | string | Yes      | -       | "sandbox_config" |  
| pillar     | string | Yes      | -       | "P09" |  
| title      | string | Yes      | -       | Human-readable name |  
| version    | string | Yes      | "1.0.0" | Semantic versioning |  
| created    | date   | Yes      | -       | ISO 8601 format |  
| updated    | date   | Yes      | -       | ISO 8601 format |  
| author     | string | Yes      | -       | Owner email |  
| domain     | string | Yes      | -       | CEX domain (e.g., "sandbox.example.com") |  
| quality    | string | Yes      | "draft" | "draft", "review", "production" |  
| tags       | list   | Yes      | []      | Keywords (lowercase) |  
| tldr       | string | Yes      | -       | Summary (max 256 chars) |  
| sandbox_type | string | Yes | - | "isolated", "shared", "hybrid" |  
| resource_limits | map | Yes | - | CPU, memory, storage limits |  

### Recommended  
| Field          | Type   | Notes |  
|----------------|--------|-------|  
| description    | string | Optional summary |  
| environment    | string | "dev", "test", "prod" |  
| dependencies   | list   | Required external services |  
| backend_type   | enum (local, docker, vm, daytona, modal, singularity) | Execution backend; daytona/modal/singularity are HERMES cloud runtimes |  

## ID Pattern  
`^p09_sb_[a-zA-Z0-9_-]+\.yaml$`  

## Body Structure  
1. **Configuration Overview**  
   - Purpose, scope, and use cases.  
2. **Resource Limits**  
   - CPU, memory, storage, and time constraints.  
3. **Access Control**  
   - Authentication, roles, and permissions.  
4. **Monitoring & Logging**  
   - Metrics, alerts, and log retention policies.  
5. **Network Isolation**  
   - Firewall rules, VPC, and egress policies.  

## Constraints  
- Max file size: 2048 bytes.  
- ID must match regex pattern.  
- Required fields must be present.  
- Version must follow semantic versioning (e.g., "1.2.3").  
- Tags must be lowercase and unique.  
- Domain must resolve to a valid CEX sandbox endpoint.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_sandbox_spec]] | sibling | 0.71 |
| [[bld_schema_usage_report]] | sibling | 0.70 |
| [[bld_schema_playground_config]] | sibling | 0.69 |
| [[bld_schema_reranker_config]] | sibling | 0.69 |
| [[bld_schema_benchmark_suite]] | sibling | 0.67 |
| [[bld_schema_pitch_deck]] | sibling | 0.67 |
| [[bld_schema_api_reference]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.66 |
| [[bld_schema_rl_algorithm]] | sibling | 0.65 |
