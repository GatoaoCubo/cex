---
kind: schema
id: bld_schema_safety_hazard_taxonomy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for safety_hazard_taxonomy
quality: 9.2
title: "Schema Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, schema, MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template, taxonomy]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for safety_hazard_taxonomy"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_faq_entry
  - bld_schema_sandbox_config
  - bld_schema_multimodal_prompt
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | | Pattern: p11_sht_{{scope}}.md |
| kind | string | yes | | Must be: safety_hazard_taxonomy |
| pillar | string | yes | | Must be: P11 |
| title | string | yes | | Include "Safety Hazard Taxonomy" and scope |
| version | string | yes | | Taxonomy version |
| created | date | yes | | ISO 8601 |
| updated | date | yes | | ISO 8601 |
| author | string | yes | | Team responsible |
| domain | string | yes | | Deployment domain / scope |
| quality | null | yes | null | Never self-score |
| tags | array | yes | | Include: MLCommons, AILuminate, hazard-category minimum |
| tldr | string | yes | | One-line taxonomy scope description |
| taxonomy_scope | string | yes | | full-12 or subset with justification |
| source_standard | string | yes | | MLCommons AILuminate v1.0 |
| classifier_alignment | string | yes | | Llama Guard 4 (Meta, 2025) |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| deployment_context | string | Consumer API / Enterprise / Internal |
| jurisdiction | string | Regional legal context |
| categories_included | array | List if subset (taxonomy_scope != full-12) |

## ID Pattern
^p11_sht_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Taxonomy Overview** -- Scope declaration, source standards, classifier alignment, version rationale
2. **Hazard Category Definitions** -- Per category: code, Llama Guard label, definition, boundary conditions, false-positive risks
3. **Severity Level Matrix** -- Per category: 4 rows (low/medium/high/critical) with criteria and response template
4. **Response Template Catalog** -- SAFE_COMPLETE / WARN_PARTIAL / REFUSE_EXPLAIN / HARD_REFUSE definitions
5. **Cross-Category Boundaries** -- Table of adjacent category pairs with disambiguation rules
6. **Regulatory Mapping** -- Per category: applicable laws (GDPR, CSAM statutes, CBRN export controls)

## Constraints
- taxonomy_scope must declare: full-12 OR list of included categories with justification.
- All included categories must have Llama Guard 4 label mapped.
- CBRN category (S8) must include Chemical/Biological/Radiological/Nuclear sub-categories.
- Each category requires 4 severity level definitions.
- Response template: HARD_REFUSE required for critical severity on all categories.
- source_standard must reference MLCommons AILuminate v1.0 or later.
- classifier_alignment must reference Llama Guard version if specified.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.59 |
| [[bld_schema_reranker_config]] | sibling | 0.57 |
| [[bld_schema_dataset_card]] | sibling | 0.57 |
| [[bld_schema_pitch_deck]] | sibling | 0.57 |
| [[bld_schema_benchmark_suite]] | sibling | 0.57 |
| [[bld_schema_search_strategy]] | sibling | 0.57 |
| [[bld_schema_quickstart_guide]] | sibling | 0.57 |
| [[bld_schema_faq_entry]] | sibling | 0.56 |
| [[bld_schema_sandbox_config]] | sibling | 0.56 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.55 |
