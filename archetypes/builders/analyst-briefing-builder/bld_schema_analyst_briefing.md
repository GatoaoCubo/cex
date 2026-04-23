---
kind: schema
id: bld_schema_analyst_briefing
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for analyst_briefing
quality: 9.1
title: "Schema Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for analyst_briefing"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_rl_algorithm
  - bld_schema_api_reference
---

## Frontmatter Fields
### Required
| Field              | Type   | Required | Default | Notes |
|--------------------|--------|----------|---------|-------|
| id                 | string | yes      |         |       |
| kind               | string | yes      |         | Must be analyst_briefing |
| pillar             | string | yes      |         | P05 |
| title              | string | yes      |         |       |
| version            | string | yes      |         |       |
| created            | date   | yes      |         |       |
| updated            | date   | yes      |         |       |
| author             | string | yes      |         |       |
| domain             | string | yes      |         |       |
| quality            | null   | yes      | null    | Never self-score |
| tags               | array  | yes      |         |       |
| tldr               | string | yes      |         |       |
| analyst_firm       | string | yes      |         | gartner, forrester, idc, or other |
| research_track     | string | yes      |         | e.g., magic-quadrant, wave, marketscape |
| briefing_date      | date   | yes      |         |       |
| vendor             | string | yes      |         | Vendor/company name being briefed |

### Recommended
| Field              | Type   | Notes |
|--------------------|--------|-------|
| embargo_flag       | bool   |       |
| proof_point_count  | int    |       |
| competitor_count   | int    |       |

## ID Pattern
^p05_ab_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Company Overview**
   - Vendor description (max 150 words), founding year, HQ, employee count, ARR.
2. **Market Position**
   - Analyst framework alignment (Gartner Magic Quadrant quadrant, Forrester Wave score, IDC MarketScape category).
3. **Product Strengths**
   - 5-7 quantified capability claims mapped to analyst evaluation criteria.
4. **Competitive Landscape**
   - Named competitors (min 2), differentiation table, win/loss summary.
5. **Roadmap**
   - 12-month priorities; embargo/NDA flag if forward-looking specifics included.
6. **Anticipated Analyst Questions**
   - 5-10 expected questions with pre-approved responses.

## Constraints
- All required fields must be present and valid.
- `id` must match the regex pattern exactly.
- `analyst_firm` must be one of: gartner, forrester, idc, gartner_peer_insights, idc_innovators, or custom.
- `briefing_date` must be a valid date in ISO format.
- `vendor` must be a non-empty string identifying the company being briefed.
- Proof points must be quantified (numeric values required for at least 3 strengths).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.66 |
| [[bld_schema_pitch_deck]] | sibling | 0.65 |
| [[bld_schema_reranker_config]] | sibling | 0.65 |
| [[bld_schema_sandbox_config]] | sibling | 0.65 |
| [[bld_schema_search_strategy]] | sibling | 0.64 |
| [[bld_schema_benchmark_suite]] | sibling | 0.64 |
| [[bld_schema_dataset_card]] | sibling | 0.63 |
| [[bld_schema_rl_algorithm]] | sibling | 0.63 |
| [[bld_schema_api_reference]] | sibling | 0.62 |
