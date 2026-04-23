---
kind: schema
id: bld_schema_openapi_spec
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for openapi_spec
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 8.9
title: "Schema OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, schema]
tldr: "Schema for openapi_spec: OAS 3.x version, info, servers, paths, components, security."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_golden_test
  - bld_schema_api_reference
  - bld_schema_pitch_deck
  - bld_schema_rl_algorithm
---

# Schema: openapi_spec

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_oas_{slug}) | YES | - | Namespace compliance |
| kind | literal "openapi_spec" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact version |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| api_name | string | YES | - | Human-friendly API name |
| oas_version | enum: "3.0.3", "3.1.0" | YES | "3.1.0" | OAS spec version |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "openapi_spec" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p06_oas_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)

1. `## OpenAPI Document` -- YAML/JSON OAS 3.x document (the actual spec)
2. `## Security` -- security scheme documentation
3. `## Error Responses` -- standard error response table

## OAS Document Required Fields

| Field | Required | Notes |
|-------|----------|-------|
| openapi | YES | "3.1.0" or "3.0.3" |
| info.title | YES | API name |
| info.version | YES | API version string |
| servers | YES | At least one server URL |
| paths | YES | At least one path defined |
| components.schemas | REC | Reusable schema objects |
| components.securitySchemes | REC | If auth required |

## Constraints

- max_bytes: 8192 (body only, inline schema)
- oas_version: "3.1.0" preferred (supports JSON Schema dialect)
- quality: null always
- NOT api_reference (no prose docs), NOT api_client (no SDK code)
- Use $ref for any schema used more than once

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.65 |
| [[bld_schema_search_strategy]] | sibling | 0.64 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
| [[bld_schema_dataset_card]] | sibling | 0.63 |
| [[bld_schema_golden_test]] | sibling | 0.63 |
| [[bld_schema_api_reference]] | sibling | 0.63 |
| [[bld_schema_pitch_deck]] | sibling | 0.62 |
| [[bld_schema_rl_algorithm]] | sibling | 0.62 |
