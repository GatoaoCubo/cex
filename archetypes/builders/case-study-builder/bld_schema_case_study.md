---
kind: schema
id: bld_schema_case_study
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for case_study
quality: 9.1
title: "Schema Case Study"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for case_study. Challenge-Solution-Outcome with pullquote and ROI."
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_pitch_deck
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_multimodal_prompt
  - bld_schema_integration_guide
  - bld_schema_customer_segment
  - bld_schema_dataset_card
  - bld_schema_sandbox_config
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | | Must match ID Pattern |
| kind | string | yes | | Always "case_study" |
| pillar | string | yes | | P05 |
| title | string | yes | | "{Customer}: {Outcome Headline}" |
| version | string | yes | | Artifact version (e.g., "1.0.0") |
| created | string | yes | | ISO 8601 YYYY-MM-DD |
| updated | string | yes | | ISO 8601 YYYY-MM-DD |
| author | string | yes | | Content author username |
| domain | string | yes | | Customer industry |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | | Industry, product, case_study |
| tldr | string | yes | | One-sentence result + champion attribution |
| context | string | yes | | Challenge summary (50 words max) |
| outcome | string | yes | | Primary KPI result (e.g., "85% cost reduction") |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| champion_name | string | Named customer quote author |
| champion_title | string | Champion's job title |
| roi_headline | string | Headline ROI metric for marketing reuse |
| customer_size | string | Company size (e.g., "500-1000 employees") |

## ID Pattern
^p05_cs_[a-z][a-z0-9_]+\\.md$

## Body Structure (Challenge-Solution-Outcome)
1. **Company Snapshot** -- Industry, size, region, champion name/title
2. **The Challenge** -- Before-state, pain context, business stakes (150-200 words)
3. **The Solution** -- Named features, deployment timeline, integrations
4. **The Outcome** -- 3+ KPIs with before/after comparison table
5. **ROI Call-Out** -- Headline metric, timeframe, verified source (block element)
6. **Customer Pullquote** -- Direct quote, champion name + title (50-80 words)
7. **Lessons Learned** -- Transferable insight closing (50-100 words)

## Constraints
- ID must match ^p05_cs_[a-z][a-z0-9_]+\\.md$ exactly.
- File size must not exceed 6144 bytes.
- All required fields must be present and non-empty.
- quality field must be null (peer-reviewed only).
- Pullquote must be attributed to a named person with title.
- Outcome section must include at least 3 KPIs with before/after values.
- No unverified metrics or fabricated statistics.
- ASCII-only characters required in all fields.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pitch_deck]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_benchmark_suite]] | sibling | 0.64 |
| [[bld_schema_reranker_config]] | sibling | 0.63 |
| [[bld_schema_quickstart_guide]] | sibling | 0.63 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.63 |
| [[bld_schema_integration_guide]] | sibling | 0.62 |
| [[bld_schema_customer_segment]] | sibling | 0.62 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
| [[bld_schema_sandbox_config]] | sibling | 0.61 |
