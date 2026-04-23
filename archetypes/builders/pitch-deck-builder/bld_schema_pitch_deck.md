---
kind: schema
id: bld_schema_pitch_deck
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for pitch_deck
quality: 9.0
title: "Schema Pitch Deck"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pitch_deck, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for pitch_deck"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_prompt_technique
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_config
  - bld_schema_contributor_guide
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes |  | Must match ID Pattern |  
| kind | string | yes | "pitch_deck" |  |  
| pillar | string | yes | "P05" |  |  
| title | string | yes |  |  |  
| version | string | yes | "1.0" |  |  
| created | datetime | yes |  | ISO 8601 format |  
| updated | datetime | yes |  | ISO 8601 format |  
| author | string | yes |  |  |  
| domain | string | yes |  |  |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes | [] |  |  
| tldr | string | yes |  |  |  
| audience | string | yes |  | Target audience |  
| investment_ask | string | yes |  | Funding request |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| summary | string | Brief overview |  
| key_metrics | list | Critical performance indicators |  

## ID Pattern  
^p05_pd_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Executive Summary**  
2. **Problem & Solution**  
3. **Market Opportunity**  
4. **Business Model**  
5. **Team**  
6. **Financials**  

## Constraints  
- File size must not exceed 6144 bytes  
- ID must match ^p05_pd_[a-z][a-z0-9_]+.md$  
- All required fields must be present  
- Quality field must be peer-reviewed, not self-assigned  
- Domain-specific fields (audience, investment_ask) must be populated  
- ASCII characters only; no markdown in body content

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.75 |
| [[bld_schema_usage_report]] | sibling | 0.75 |
| [[bld_schema_quickstart_guide]] | sibling | 0.75 |
| [[bld_schema_benchmark_suite]] | sibling | 0.73 |
| [[bld_schema_integration_guide]] | sibling | 0.72 |
| [[bld_schema_dataset_card]] | sibling | 0.71 |
| [[bld_schema_prompt_technique]] | sibling | 0.70 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.70 |
| [[bld_schema_sandbox_config]] | sibling | 0.69 |
| [[bld_schema_contributor_guide]] | sibling | 0.69 |
