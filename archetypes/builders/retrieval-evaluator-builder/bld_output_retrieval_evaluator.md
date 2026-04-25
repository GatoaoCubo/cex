---
kind: output_template
id: bld_output_retrieval_evaluator
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a retrieval_evaluator
pattern: every field here exists in SCHEMA -- template derives, never invents
quality: null
title: "Retrieval Evaluator Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, output]
tldr: "Output template for retrieval evaluator artifacts with metric definitions, query sets, and thresholds."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_retrieval_evaluator
  - bld_eval_retrieval_evaluator
---

# Output Template: retrieval_evaluator

```yaml
id: p07_re_{{evaluator_slug}}
kind: retrieval_evaluator
pillar: P07
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_system: "{{system_being_evaluated}}"
primary_metric: "{{ndcg_or_mrr_or_map}}"
k_values: [{{k1}}, {{k2}}, {{k3}}]
judgment_scale: "{{binary_or_graded}}"
min_query_set_size: {{integer}}
baseline: "{{baseline_system}}"
domain: "{{domain_value}}"
quality: null
tags: [retrieval, evaluation, {{metric_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Metrics
`{{primary_and_secondary_metrics_with_formulas}}`

## Query Set
`{{query_set_requirements_and_construction}}`

## Judgment Protocol
`{{relevance_scale_and_annotator_guidelines}}`

## Baseline
`{{reference_system_and_expected_scores}}`

## Thresholds
`{{pass_fail_regression_criteria}}`

## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p07_re_{{name}}.md + .yaml pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 5120 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | retrieval evaluator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
