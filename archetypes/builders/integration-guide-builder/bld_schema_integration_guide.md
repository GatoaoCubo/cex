---
kind: schema
id: bld_schema_integration_guide
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for integration_guide
quality: 9.1
title: "Schema Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for integration_guide"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_spec
  - bld_schema_app_directory_entry
  - bld_schema_eval_metric
  - bld_schema_contributor_guide
  - bld_schema_audit_log
  - bld_schema_interactive_demo
  - bld_schema_multimodal_prompt
  - bld_schema_sdk_example
---

## Frontmatter Fields (integration guide schema)
### Required fields for an integration guide  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      | null    | Must match ID Pattern |  
| kind       | string | yes      | null    | Always 'integration_guide' |  
| pillar     | string | yes      | null    | Always 'P05' |  
| title      | string | yes      | null    | Descriptive title |  
| version    | string | yes      | null    | Semantic version (e.g., 1.0.0) |  
| created    | date   | yes      | null    | ISO 8601 format |  
| updated    | date   | yes      | null    | ISO 8601 format |  
| author     | string | yes      | null    | Author name |  
| domain     | string | yes      | null    | Integration domain (e.g., 'payments') |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | list   | yes      | null    | Keywords for search |  
| tldr       | string | yes      | null    | Summary (≤256 chars) |  
| integration_type | string | yes | null | Type of integration (e.g., 'API', 'SDK') |  
| api_endpoints | list | yes | null | List of required endpoints |  

### Recommended  
| Field         | Type   | Notes |  
|---------------|--------|-------|  
| reviewers     | list   | Peer reviewers |  
| dependencies  | list   | External dependencies |  

## ID Pattern  
^p05_ig_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and use cases.  
2. **Prerequisites**  
   - Software, hardware, and account requirements.  
3. **Step-by-Step Integration**  
   - Detailed instructions with code snippets.  
4. **API Reference**  
   - Endpoint descriptions, parameters, and examples.  
5. **Troubleshooting**  
   - Common errors and solutions.  
6. **Compliance**  
   - Legal, security, and audit requirements.  

## Constraints  
- Filename must match ID Pattern.  
- All required fields in frontmatter must be present.  
- Version must follow semantic versioning.  
- Quality must be assigned by peer review.  
- Total file size ≤8192 bytes.  
- ASCII-only characters; no markdown in body.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_benchmark_suite]] | sibling | 0.69 |
| [[bld_schema_sandbox_spec]] | sibling | 0.68 |
| [[bld_schema_app_directory_entry]] | sibling | 0.67 |
| [[bld_schema_eval_metric]] | sibling | 0.66 |
| [[bld_schema_contributor_guide]] | sibling | 0.66 |
| [[bld_schema_audit_log]] | sibling | 0.66 |
| [[bld_schema_interactive_demo]] | sibling | 0.65 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.65 |
| [[bld_schema_sdk_example]] | sibling | 0.65 |
