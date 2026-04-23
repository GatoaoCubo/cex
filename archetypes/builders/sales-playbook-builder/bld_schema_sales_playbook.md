---
kind: schema
id: bld_schema_sales_playbook
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for sales_playbook
quality: 9.1
title: "Schema Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for sales_playbook"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_eval_metric
  - bld_schema_usage_report
  - bld_schema_customer_segment
  - bld_schema_sandbox_spec
  - bld_schema_app_directory_entry
  - bld_schema_pitch_deck
  - bld_schema_search_strategy
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes                              |  
|------------|--------|----------|---------|------------------------------------|  
| id         | string | yes      | null    | Must match ID Pattern              |  
| kind       | string | yes      | "sales_playbook" | Fixed value                  |  
| pillar     | string | yes      | "P03"    | Fixed value                        |  
| title      | string | yes      | null    | Descriptive name                   |  
| version    | string | yes      | "1.0"   | Semantic versioning                |  
| created    | date   | yes      | null    | ISO 8601 format                    |  
| updated    | date   | yes      | null    | ISO 8601 format                    |  
| author     | string | yes      | null    | Owner of the playbook              |  
| domain     | string | yes      | null    | Business unit or product area      |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | list   | yes      | []      | Keywords for search/filter         |  
| tldr       | string | yes      | null    | One-sentence summary               |  
| target_audience | string | yes | null | Primary customer segment           |  
| key_metrics | list   | yes | [] | Success indicators                 |  

### Recommended  
| Field         | Type   | Notes                  |  
|---------------|--------|------------------------|  
| approval_date | date   | Date of peer approval  |  
| review_cycle  | string | Quarterly/Annual       |  

## ID Pattern  
^p03_sp_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Introduction**  
   - Purpose, scope, and objectives of the playbook.  
2. **Target Audience**  
   - Detailed customer personas and use cases.  
3. **Sales Strategy**  
   - Tactics, objection handling, and value propositions.  
4. **Key Metrics**  
   - Performance KPIs and success criteria.  
5. **Playbook Updates**  
   - Version history and change log.  

## Constraints  
- ID must match ^p03_sp_[a-z][a-z0-9_]+.md$ exactly.  
- All required fields must be present and valid.  
- Version must follow semantic versioning (e.g., 1.0.0).  
- Quality field must be assigned by peer review, not self-scored.  
- Domain-specific fields (target_audience, key_metrics) must align with business context.  
- File size must not exceed 8192 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.75 |
| [[bld_schema_reranker_config]] | sibling | 0.73 |
| [[bld_schema_benchmark_suite]] | sibling | 0.73 |
| [[bld_schema_eval_metric]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_customer_segment]] | sibling | 0.68 |
| [[bld_schema_sandbox_spec]] | sibling | 0.68 |
| [[bld_schema_app_directory_entry]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_search_strategy]] | sibling | 0.67 |
