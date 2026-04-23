---
kind: schema
id: bld_schema_api_reference
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for api_reference
quality: 9.1
title: "Schema Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for api_reference"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_playground_config
  - bld_schema_nps_survey
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes                          |  
|-----------|--------|----------|---------|--------------------------------|  
| id        | string | yes      |         | Must match ID Pattern          |  
| kind      | string | yes      |         | Fixed to "api_reference"       |  
| pillar    | string | yes      |         | Fixed to "P06"                 |  
| title     | string | yes      |         | Human-readable API name        |  
| version   | string | yes      |         | Semantic version (e.g., "v1.2")|  
| created   | date   | yes      |         | ISO 8601 format                |  
| updated   | date   | yes      |         | ISO 8601 format                |  
| author    | string | yes      |         | Maintainer name                |  
| domain    | string | yes      |         | API domain (e.g., "exchange")  |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | array  | yes      | []      | Keywords (e.g., ["REST", "WebSocket"]) |  
| tldr      | string | yes      |         | One-sentence API summary       |  
| endpoint  | string | yes      |         | Base URL (e.g., "https://api.example.com") |  
| authentication | string | yes |         | Method (e.g., "API Key", "OAuth2") |  

### Recommended  
| Field         | Type   | Notes                  |  
|---------------|--------|------------------------|  
| deprecated    | bool   | Mark if deprecated     |  
| example_url   | string | Example endpoint       |  
| swagger_url   | string | Swagger/OpenAPI spec   |  

## ID Pattern  
^p06_ar_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and use cases.  
2. **Authentication**  
   - Required headers, tokens, or keys.  
3. **Endpoints**  
   - List of endpoints with methods, paths, and parameters.  
4. **Rate Limiting**  
   - Throttling rules and quotas.  
5. **Versioning**  
   - Supported versions and deprecation policy.  

## Constraints  
- ID must match exact regex: ^p06_ar_[a-z][a-z0-9_]+.md$  
- All required fields must be present and non-null  
- Version must follow semantic versioning (e.g., "v1.0.0")  
- Endpoints must use absolute URLs  
- Authentication must specify a valid method  
- Rate limits must include numerical thresholds and reset intervals

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.71 |
| [[bld_schema_benchmark_suite]] | sibling | 0.70 |
| [[bld_schema_integration_guide]] | sibling | 0.70 |
| [[bld_schema_sandbox_config]] | sibling | 0.70 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_pitch_deck]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.66 |
| [[bld_schema_playground_config]] | sibling | 0.66 |
| [[bld_schema_nps_survey]] | sibling | 0.66 |
