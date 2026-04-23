---
kind: schema
id: bld_schema_prompt_optimizer
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for prompt_optimizer
quality: 9.1
title: "Schema Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for prompt_optimizer"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_config
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes |
|------------|--------|----------|---------|-------|
| id         | string | yes      |         |       |
| kind       | string | yes      |         |       |
| pillar     | string | yes      |         |       |
| title      | string | yes      |         |       |
| version    | string | yes      |         |       |
| created    | date   | yes      |         |       |
| updated    | date   | yes      |         |       |
| author     | string | yes      |         |       |
| domain     | string | yes      |         |       |
| quality    | null   | yes      | null    | Never self-score; peer review assigns |
| tags       | list   | yes      |         |       |
| tldr       | string | yes      |         |       |
| objective  | string | yes      |         |       |
| metrics    | list   | yes      |         |       |

### Recommended
| Field              | Type   | Notes |
|--------------------|--------|-------|
| example_use_case   | string |       |
| performance_baseline | string |       |

## ID Pattern
^p03_po_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Objective and Scope**
   Define the primary goal of the prompt optimizer and its application boundaries.

2. **Optimization Metrics**
   List quantifiable success criteria (e.g., accuracy, efficiency, user satisfaction).

3. **Prompt Template**
   Provide the structured template used for generating or refining prompts.

4. **Iteration Strategy**
   Describe the process for refining prompts (e.g., A/B testing, feedback loops).

5. **Example Use Case**
   Illustrate a real-world scenario where the optimizer improves outcomes.

## Constraints
- ID must match ^p03_po_[a-z][a-z0-9_]+.md$ exactly.
- All required fields must be present and non-null.
- Quality field must be assigned by peer review, not self-assessed.
- Domain-specific fields (objective, metrics) must align with the optimizer’s purpose.
- File size must not exceed 5120 bytes.
- Version must follow semantic versioning (e.g., 1.0.0).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.75 |
| [[bld_schema_benchmark_suite]] | sibling | 0.72 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_quickstart_guide]] | sibling | 0.72 |
| [[bld_schema_pitch_deck]] | sibling | 0.70 |
| [[bld_schema_integration_guide]] | sibling | 0.70 |
| [[bld_schema_search_strategy]] | sibling | 0.70 |
| [[bld_schema_dataset_card]] | sibling | 0.67 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.67 |
| [[bld_schema_sandbox_config]] | sibling | 0.67 |
