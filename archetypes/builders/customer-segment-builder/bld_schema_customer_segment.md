---
kind: schema
id: bld_schema_customer_segment
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for customer_segment
quality: 9.1
title: "Schema Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for customer_segment"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_eval_metric
  - bld_schema_audit_log
  - bld_schema_nps_survey
  - bld_schema_prompt_technique
  - bld_schema_pitch_deck
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID Pattern |  
| kind | string | yes | "customer_segment" | Fixed value |  
| pillar | string | yes | "P02" | Fixed value |  
| title | string | yes | null | Descriptive name |  
| version | string | yes | "1.0" | Semantic versioning |  
| created | string | yes | ISO 8601 | Timestamp of creation |  
| updated | string | yes | ISO 8601 | Timestamp of last update |  
| author | string | yes | null | Owner/creator |  
| domain | string | yes | null | Business area (e.g., "retail") |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | array | yes | [] | Keywords for categorization |  
| tldr | string | yes | null | One-sentence summary |  
| customer_type | string | yes | null | E.g., "B2B", "B2C" |  
| segmentation_criteria | array | yes | [] | E.g., ["age", "purchase_frequency"] |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| use_case | string | Primary business application |  
| primary_metric | string | Key performance indicator |  

## ID Pattern  
^p02_cs_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Definition and purpose of the customer segment.  
2. **Segmentation Criteria**  
   - Detailed breakdown of attributes and filters.  
3. **Use Cases**  
   - Specific applications in product, marketing, or service.  
4. **Key Metrics**  
   - Quantitative and qualitative measures for evaluation.  
5. **Data Sources**  
   - Systems or datasets used to define the segment.  

## Constraints  
- ID must be unique and follow the regex pattern.  
- Pillar must be "P02" and cannot be modified.  
- All required fields must be populated before submission.  
- Dates must use ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).  
- Quality must be reviewed by at least two peers.  
- Tags must be lowercase and relevant to the domain.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_benchmark_suite]] | sibling | 0.74 |
| [[bld_schema_reranker_config]] | sibling | 0.73 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.71 |
| [[bld_schema_integration_guide]] | sibling | 0.71 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_eval_metric]] | sibling | 0.69 |
| [[bld_schema_audit_log]] | sibling | 0.69 |
| [[bld_schema_nps_survey]] | sibling | 0.69 |
| [[bld_schema_prompt_technique]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
