---
kind: schema
id: bld_schema_app_directory_entry
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for app_directory_entry
quality: 9.1
title: "Schema App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for app_directory_entry"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_sandbox_spec
  - bld_schema_multimodal_prompt
  - bld_schema_eval_metric
  - bld_schema_audit_log
  - bld_schema_marketplace_app_manifest
  - bld_schema_prompt_technique
  - bld_schema_faq_entry
---

## Frontmatter Fields  
### Required  
| Field     | Type   | Required | Default | Notes |  
|-----------|--------|----------|---------|-------|  
| id        | string | yes      | null    | Must match ID Pattern |  
| kind      | string | yes      | null    | Always "app_directory_entry" |  
| pillar    | string | yes      | null    | Always "P05" |  
| title     | string | yes      | null    | Human-readable name |  
| version   | string | yes      | null    | Semantic versioning (e.g., 1.0.0) |  
| created   | date   | yes      | null    | ISO 8601 format (e.g., 2023-01-01) |  
| updated   | date   | yes      | null    | ISO 8601 format (e.g., 2023-01-01) |  
| author    | string | yes      | null    | Maintainer's identifier |  
| domain    | string | yes      | null    | Application category (e.g., "wallet") |  
| quality   | null   | yes      | null    | Never self-score; peer review assigns |  
| tags      | array  | yes      | null    | Keywords (lowercase, no spaces) |  
| tldr      | string | yes      | null    | One-sentence summary |  
| app_id    | string | yes      | null    | Unique app identifier |  
| description | string | yes | null | Brief functional overview |  

### Recommended  
| Field     | Type   | Notes |  
|-----------|--------|-------|  
| license   | string | Open source license (e.g., MIT) |  
| category  | string | Subdomain classification (e.g., "decentralized") |  

## ID Pattern  
^p05_ade_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose, target users, and core features.  
2. **Technical Details**  
   - Architecture, dependencies, and API endpoints.  
3. **Usage**  
   - Installation, configuration, and example commands.  
4. **Compliance**  
   - Regulatory adherence and security audits.  
5. **Community**  
   - Support channels, governance model, and contribution guidelines.  

## Constraints  
- ID must match ^p05_ade_[a-z][a-z0-9_]+.md$ exactly.  
- Quality must be assigned by peer review; self-scoring is prohibited.  
- Version must follow semantic versioning (major.minor.patch).  
- Tags must be lowercase alphanumeric with underscores (no spaces).  
- Domain-specific fields (app_id, description) are mandatory.  
- File size must not exceed 4096 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.75 |
| [[bld_schema_benchmark_suite]] | sibling | 0.73 |
| [[bld_schema_reranker_config]] | sibling | 0.71 |
| [[bld_schema_sandbox_spec]] | sibling | 0.70 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.70 |
| [[bld_schema_eval_metric]] | sibling | 0.69 |
| [[bld_schema_audit_log]] | sibling | 0.69 |
| [[bld_schema_marketplace_app_manifest]] | sibling | 0.69 |
| [[bld_schema_prompt_technique]] | sibling | 0.68 |
| [[bld_schema_faq_entry]] | sibling | 0.67 |
