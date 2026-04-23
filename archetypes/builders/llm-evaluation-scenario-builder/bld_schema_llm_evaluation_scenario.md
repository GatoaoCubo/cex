---
kind: schema
id: bld_schema_llm_evaluation_scenario
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for llm_evaluation_scenario
quality: 9.2
title: "Schema LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, schema, helm]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for llm_evaluation_scenario"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_multimodal_prompt
  - bld_schema_customer_segment
  - bld_schema_eval_metric
---

## Frontmatter Fields

### Required
| Field            | Type   | Required | Default | Notes |
|------------------|--------|----------|---------|-------|
| id               | string | yes      |         | Follows ID pattern below |
| kind             | string | yes      |         | Must be "llm_evaluation_scenario" |
| pillar           | string | yes      |         | Must be "P07" |
| title            | string | yes      |         | Human-readable scenario name |
| version          | string | yes      |         | Semver |
| created          | date   | yes      |         | ISO 8601 |
| updated          | date   | yes      |         | ISO 8601 |
| author           | string | yes      |         | Builder or nucleus ID |
| domain           | string | yes      |         | HELM subject_area value |
| quality          | null   | yes      | null    | Never self-score |
| tags             | array  | yes      |         | Includes subject_area + capability tags |
| tldr             | string | yes      |         | One-line scenario description |
| subject_area     | string | yes      |         | HELM taxonomy: knowledge/reasoning/language/code/safety/finance/legal/climate/cybersecurity |
| capability       | string | yes      |         | Specific testable function |
| task_format      | string | yes      |         | mcq/open_ended/classification/generation |
| primary_metric   | string | yes      |         | HELM metric family |

### Recommended
| Field                | Type   | Notes |
|----------------------|--------|-------|
| num_instances        | int    | Number of task instances |
| num_few_shot         | int    | Few-shot demonstrations (0,1,3,5,10) |
| adapter_ref          | string | Reference to prompt_template ISO |
| dataset_source       | string | Upstream dataset name + license |
| canonicalization_fn  | string | Normalization function reference |
| token_cost_estimate  | string | Estimated tokens per run |

## ID Pattern
`^p07_evs_[a-z][a-z0-9_]+\.md$`

Example: `p07_evs_medical_diagnosis_mcq.md`, `p07_evs_legal_contract_reasoning.md`

## Body Structure
1. **Scenario Overview** -- capability, subject area, HELM taxonomy placement
2. **Task Instance Specification** -- format, input/output schema, dataset source
3. **Few-Shot Pool** -- pool size, selection strategy, demonstration format
4. **Adapter Configuration** -- prompt template, token budget, stop sequences
5. **Metric Mapping** -- primary metric, aggregation function, HELM family
6. **Canonicalization Rules** -- normalization steps, determinism guarantee
7. **Token Cost Estimate** -- instances x (prompt + completion) tokens

## Constraints
- id MUST match the regex pattern exactly.
- subject_area MUST be one of the recognized HELM taxonomy values.
- task_format MUST be homogeneous within the scenario (no mixing).
- primary_metric MUST map to a HELM metric family.
- canonicalization_fn MUST be referenced by name (not inline code).
- num_few_shot MUST be <= len(few_shot_pool).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_benchmark_suite]] | sibling | 0.64 |
| [[bld_schema_usage_report]] | sibling | 0.63 |
| [[bld_schema_reranker_config]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.62 |
| [[bld_schema_pitch_deck]] | sibling | 0.62 |
| [[bld_schema_sandbox_config]] | sibling | 0.62 |
| [[bld_schema_quickstart_guide]] | sibling | 0.62 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.61 |
| [[bld_schema_customer_segment]] | sibling | 0.60 |
| [[bld_schema_eval_metric]] | sibling | 0.60 |
