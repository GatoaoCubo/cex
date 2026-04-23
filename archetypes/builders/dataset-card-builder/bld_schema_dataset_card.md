---
kind: schema
id: bld_schema_dataset_card
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for dataset_card
quality: 9.1
title: "Schema Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for dataset_card"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_schema_multimodal_prompt
  - bld_schema_voice_pipeline
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_search_strategy
---

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| id | string | Yes | N/A | Unique identifier |
| kind | string | Yes | dataset_card | Object type |
| pillar | string | Yes | P01 | Pillar designation |
| title | string | Yes | N/A | Display name |
| version | string | Yes | 1.0.0 | Semantic version |
| created | datetime | Yes | N/A | Creation timestamp |
| updated | datetime | Yes | N/A | Last modification |
| author | string | Yes | N/A | Data owner/creator |
| domain | string | Yes | N/A | Data domain/category |
| quality | number\|null | Yes | null | Peer-review score; null until scored (never self-assign) |
| tags | list | Yes | [] | Metadata keywords |
| tldr | string | Yes | N/A | One-sentence summary |
| license | string | Yes | MIT | Usage permissions |
| schema_ref | string | Yes | N/A | Reference to data schema |

## Recommended
| Field | Type | Default | Notes |
| :--- | :--- | :--- | :--- |
| language | string | en | Primary language |
| source | string | N/A | Data origin/URL |
| deprecated | boolean | false | Lifecycle status |

## ID Pattern
`^p01_dc_[a-z0-9_]+\.md$`

## Body Structure
1. Dataset Overview
2. Data Collection Methodology
3. Data Preprocessing & Cleaning
4. Annotation Process
5. Statistical Properties
6. Usage Limitations & Bias

## Constraints
* Max file size: 5120 bytes
* Encoding: ASCII only
* Naming: Must follow P01 convention
* Versioning: Must follow SemVer
* Structure: All 6 body sections are mandatory
* Integrity: All required frontmatter fields must be present

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.74 |
| [[bld_schema_benchmark_suite]] | sibling | 0.72 |
| [[bld_schema_reranker_config]] | sibling | 0.71 |
| [[bld_schema_pitch_deck]] | sibling | 0.69 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.69 |
| [[bld_schema_voice_pipeline]] | sibling | 0.69 |
| [[bld_schema_quickstart_guide]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.67 |
| [[bld_schema_sandbox_config]] | sibling | 0.67 |
| [[bld_schema_search_strategy]] | sibling | 0.67 |
