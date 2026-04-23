---
kind: schema
id: bld_schema_partner_listing
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for partner_listing
quality: 9.1
title: "Schema Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for partner_listing"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_agent_profile
  - bld_schema_pitch_deck
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_rl_algorithm
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
| tags      | array  | yes      |         |       |  
| tldr      | string | yes      |         |       |  
| partner_name | string | yes |         |       |  
| partner_type | string | yes |         |       |  
| listing_status | string | yes |         |       |  
| start_date | date | yes |         |       |  

### Recommended  
| Field        | Type   | Notes |  
|--------------|--------|-------|  
| description  | string |       |  
| website      | url    |       |  
| contact_info | string |       |  

## ID Pattern  
^p05_pl_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Summary of the partner listing purpose and scope.  
2. **Partner Details**  
   - Name, type, and key attributes of the partner.  
3. **Listing Status**  
   - Current status (e.g., active, pending, suspended).  
4. **Terms & Conditions**  
   - Legal and operational requirements for listing.  
5. **Compliance**  
   - Regulatory checks and certifications.  
6. **Additional Information**  
   - Notes, links, or supplementary data.  

## Constraints  
- All required fields must be present and valid.  
- `id` must match the regex pattern exactly.  
- `listing_status` must be one of: active, pending, suspended.  
- `start_date` must be a valid date in ISO format.  
- `partner_name` must be unique across all listings.  
- `domain` must align with the CEX's operational scope.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.74 |
| [[bld_schema_quickstart_guide]] | sibling | 0.71 |
| [[bld_schema_agent_profile]] | sibling | 0.71 |
| [[bld_schema_pitch_deck]] | sibling | 0.70 |
| [[bld_schema_search_strategy]] | sibling | 0.70 |
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_sandbox_config]] | sibling | 0.70 |
| [[bld_schema_benchmark_suite]] | sibling | 0.70 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_rl_algorithm]] | sibling | 0.68 |
