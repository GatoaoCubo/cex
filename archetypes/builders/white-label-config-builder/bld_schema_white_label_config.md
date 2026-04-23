---
kind: schema
id: bld_schema_white_label_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for white_label_config
quality: 9.1
title: "Schema White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for white_label_config"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_sandbox_config
  - bld_schema_playground_config
---

## Frontmatter Fields
### Required
| Field     | Type   | Required | Default | Notes |
|-----------|--------|----------|---------|-------|
| id        | string | yes      |         |       |
| kind      | string | yes      |         |       |
| pillar    | string | yes      |         |       |
| title     | string | yes      |         |       |
| version   | string | yes      |         |       |
| created   | date   | yes      |         |       |
| updated   | date   | yes      |         |       |
| author    | string | yes      |         |       |
| domain    | string | yes      |         |       |
| quality   | null   | yes      | null    | Never self-score; peer review assigns |
| tags      | list   | yes      |         |       |
| tldr      | string | yes      |         |       |
| branding  | dict   | yes      |         |       |
| customization | dict | yes |         |       |

### Recommended
| Field         | Type   | Notes |
|---------------|--------|-------|
| allowed_features | list |       |
| notes         | string |       |
| deprecated    | bool   |       |

## ID Pattern
^p09_wl_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Branding Configuration**
   Define logo, color schemes, and legal text.

2. **Customization Options**
   Specify UI/UX elements available for modification.

3. **Feature Whitelisting**
   List enabled/disabled features per tenant.

4. **Compliance Settings**
   Regional regulations and data handling rules.

## Constraints
- ID must match ^p09_wl_[a-z][a-z0-9_]+.yaml$
- Max file size: 4096 bytes
- 'quality' field must be peer-reviewed
- 'allowed_features' must reference valid feature keys
- 'branding' and 'customization' must be non-empty dicts

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.75 |
| [[bld_schema_quickstart_guide]] | sibling | 0.73 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_pitch_deck]] | sibling | 0.71 |
| [[bld_schema_integration_guide]] | sibling | 0.70 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_benchmark_suite]] | sibling | 0.69 |
| [[bld_schema_search_strategy]] | sibling | 0.69 |
| [[bld_schema_sandbox_config]] | sibling | 0.68 |
| [[bld_schema_playground_config]] | sibling | 0.66 |
