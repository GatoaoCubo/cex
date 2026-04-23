---
kind: schema
id: bld_schema_marketplace_app_manifest
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for marketplace_app_manifest
quality: 9.1
title: "Schema Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for marketplace_app_manifest"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_app_directory_entry
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_spec
  - bld_schema_audit_log
  - bld_schema_eval_metric
  - bld_schema_oauth_app_config
  - bld_schema_graph_rag_config
---

## Frontmatter Fields
### Required
| Field     | Type      | Required | Default | Notes                              |
|-----------|-----------|----------|---------|------------------------------------|
| id        | string    | yes      | null    | Must match ID Pattern              |
| kind      | string    | yes      | null    | Always "marketplace_app_manifest"  |
| pillar    | string    | yes      | null    | Always "P09"                       |
| title     | string    | yes      | null    | Human-readable name                |
| version   | string    | yes      | null    | Semantic version (e.g., 1.0.0)     |
| created   | timestamp | yes      | null    | ISO 8601 format                    |
| updated   | timestamp | yes      | null    | ISO 8601 format                    |
| author    | string    | yes      | null    | Creator/organization               |
| domain    | string    | yes      | null    | Marketplace domain (e.g., "appstore") |
| quality   | null      | yes      | null    | Never self-score; peer review assigns |
| tags      | array     | yes      | null    | Keywords for discovery             |
| tldr      | string    | yes      | null    | Summary of app purpose             |
| app_id    | string    | yes      | null    | Unique identifier for the app      |
| marketplace_url | string | yes      | null    | URL of marketplace listing         |

### Recommended
| Field         | Type   | Notes                          |
|---------------|--------|--------------------------------|
| description   | string | Detailed app description       |
| dependencies  | array  | Required system/applications   |
| license       | string | Legal terms for use            |
| screenshots   | array  | URLs to app interface images   |

## ID Pattern
^p09_mam_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **App Information**
   - Name, description, app_id, author, license

2. **Marketplace Integration**
   - marketplace_url, domain, tags, tldr

3. **Technical Requirements**
   - Dependencies, supported platforms, system requirements

4. **Compliance & Policies**
   - Data usage terms, privacy policy, age restrictions

5. **Pricing Model**
   - Free/subscription/one-time, pricing tiers

6. **User Support**
   - Contact details, documentation links, support channels

## Constraints
- All required fields must be present and valid
- `id` must match the exact regex pattern
- `version` must follow semantic versioning
- `marketplace_url` must be a valid HTTPS URL
- File size must not exceed 4096 bytes
- `quality` field must be assigned by peer review, not self-assigned

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_app_directory_entry]] | sibling | 0.73 |
| [[bld_schema_integration_guide]] | sibling | 0.72 |
| [[bld_schema_benchmark_suite]] | sibling | 0.70 |
| [[bld_schema_reranker_config]] | sibling | 0.69 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.68 |
| [[bld_schema_sandbox_spec]] | sibling | 0.67 |
| [[bld_schema_audit_log]] | sibling | 0.67 |
| [[bld_schema_eval_metric]] | sibling | 0.66 |
| [[bld_schema_oauth_app_config]] | sibling | 0.66 |
| [[bld_schema_graph_rag_config]] | sibling | 0.65 |
