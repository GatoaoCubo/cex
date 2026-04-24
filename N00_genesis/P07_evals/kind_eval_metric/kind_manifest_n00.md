---
id: n00_eval_metric_manifest
kind: knowledge_card
8f: F3_inject
pillar: P07
nucleus: n00
title: "Eval Metric -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, eval_metric, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_eval_metric
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_optimizer
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_multimodal_prompt
  - bld_schema_memory_benchmark
  - bld_schema_integration_guide
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Eval metric defines an individual evaluation metric with its computation formula, interpretation guidance, acceptable range, and normalization method. Eval metrics are the atomic measurement units consumed by benchmarks, scoring rubrics, and LLM judges. Each metric artifact documents not just HOW to compute the metric but WHY it matters and what threshold separates acceptable from unacceptable performance.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `eval_metric` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Metric name (human-readable) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| metric_name | string | yes | Canonical identifier (e.g., bleu, rouge_l, pass_at_1) |
| formula | string | yes | Mathematical or algorithmic definition |
| scale | object | yes | Min, max, direction (higher_better / lower_better) |
| interpretation | string | yes | What the metric measures and its limitations |
| threshold_acceptable | float | yes | Minimum acceptable value for production |

## When to use
- Adding a new quality dimension to the CEX scoring system
- Documenting the semantics of a metric before it is referenced in a benchmark
- Standardizing a metric definition across multiple eval kinds

## Builder
`archetypes/builders/eval_metric-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind eval_metric --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence defines; all nuclei reference
- `{{SIN_LENS}}` -- Analytical Envy: precise definition, unambiguous interpretation
- `{{TARGET_AUDIENCE}}` -- benchmarks, scoring rubrics, and LLM judges referencing this metric
- `{{DOMAIN_CONTEXT}}` -- metric domain, task type, comparison baseline

## Example (minimal)
```yaml
---
id: eval_metric_artifact_quality_score
kind: eval_metric
pillar: P07
nucleus: n01
title: "CEX Artifact Quality Score"
version: 1.0
quality: null
---
metric_name: artifact_quality_score
formula: "weighted_avg(structural_score*0.3, rubric_score*0.3, semantic_score*0.4)"
scale: {min: 0.0, max: 10.0, direction: higher_better}
threshold_acceptable: 8.0
interpretation: "Composite quality gate; below 8.0 blocks publication"
```

## Related kinds
- `scoring_rubric` (P07) -- composes multiple eval_metrics into a rubric
- `benchmark` (P07) -- references eval_metrics as its measurement units
- `llm_judge` (P07) -- uses eval_metrics as the scoring criteria for automated judgment

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_eval_metric]] | upstream | 0.52 |
| [[bld_schema_benchmark_suite]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.43 |
| [[bld_schema_optimizer]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.42 |
| [[bld_schema_usage_report]] | upstream | 0.42 |
| [[bld_schema_search_strategy]] | upstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.41 |
| [[bld_schema_memory_benchmark]] | upstream | 0.41 |
| [[bld_schema_integration_guide]] | upstream | 0.41 |
