---
kind: schema
id: bld_schema_playground_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for playground_config
quality: 9.1
title: "Schema Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for playground_config"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_prompt_technique
  - bld_schema_dataset_card
---

## Frontmatter Fields
### Required
| Field      | Type      | Required | Default | Notes |
|------------|-----------|----------|---------|-------|
| id         | string    | yes      |         | Must match ID Pattern |
| kind       | string    | yes      |         | Always "playground_config" |
| pillar     | string    | yes      |         | Always "P09" |
| title      | string    | yes      |         | Human-readable name |
| version    | string    | yes      | "1.0"   | Semantic versioning |
| created    | datetime  | yes      |         | ISO 8601 format |
| updated    | datetime  | yes      |         | ISO 8601 format |
| author     | string    | yes      |         | Creator's identifier |
| domain     | string    | yes      |         | Technical domain (e.g., "ml") |
| quality    | null      | yes      | null    | Never self-score; peer review assigns |
| tags       | array     | yes      | []      | Keywords for categorization |
| tldr       | string    | yes      |         | One-sentence summary |
| sandbox_enabled | bool  | yes      | false   | Enable/disable sandbox |
| resource_limits | object | yes      | {}      | CPU/Memory/Time caps |

### Recommended
| Field              | Type   | Notes |
|--------------------|--------|-------|
| description        | string | Detailed purpose |
| last_reviewed      | date   | Peer review date |
| access_level       | string | "public"/"private" |
| deprecated         | bool   | Mark for removal |

## ID Pattern
^p09_pg_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Configuration Overview**  
   - Purpose, scope, and use cases  
2. **Resource Allocation**  
   - CPU, memory, and time limits  
3. **Access Control**  
   - User roles and permissions  
4. **Sandbox Settings**  
   - Isolation level and security policies  
5. **Review History**  
   - Peer review dates and notes  

## Constraints
- ID must match ^p09_pg_[a-z][a-z0-9_]+.yaml$ exactly  
- File size must not exceed 4096 bytes  
- All required fields must be present and valid  
- Quality field must be assigned by peer review only  
- Domain-specific fields must conform to technical domain standards  
- Version must follow semantic versioning (e.g., "1.2.3")

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_sandbox_config]] | sibling | 0.73 |
| [[bld_schema_usage_report]] | sibling | 0.72 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_benchmark_suite]] | sibling | 0.71 |
| [[bld_schema_sandbox_spec]] | sibling | 0.70 |
| [[bld_schema_pitch_deck]] | sibling | 0.70 |
| [[bld_schema_integration_guide]] | sibling | 0.69 |
| [[bld_schema_quickstart_guide]] | sibling | 0.69 |
| [[bld_schema_prompt_technique]] | sibling | 0.68 |
| [[bld_schema_dataset_card]] | sibling | 0.67 |
