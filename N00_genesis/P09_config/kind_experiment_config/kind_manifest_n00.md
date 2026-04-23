---
id: n00_experiment_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Experiment Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, experiment_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_experiment_config
  - bld_schema_thinking_config
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_eval_metric
  - bld_schema_sandbox_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An experiment_config defines the parameters for A/B tests and prompt experiments: variant definitions, traffic allocation, success metrics, and evaluation criteria. It enables systematic comparison of builder approaches, model versions, or prompt strategies with statistically meaningful results stored in .cex/experiments/results.tsv.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `experiment_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable experiment name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| hypothesis | string | yes | What this experiment tests |
| variants | list | yes | A/B/n variant definitions |
| variants[].name | string | yes | Variant identifier (control, treatment_a...) |
| variants[].traffic_pct | integer | yes | Percentage of traffic for this variant |
| variants[].config | object | yes | Variant-specific configuration overrides |
| success_metric | string | yes | Primary metric to optimize (quality_score, latency_ms) |
| min_sample_size | integer | yes | Minimum samples before results are valid |
| results_path | string | no | Where to write results (default .cex/experiments/) |

## When to use
- Comparing two prompt strategies to determine which produces higher quality scores
- Testing a new model tier against the current baseline before switching
- Evaluating the impact of extended thinking on output quality vs. cost

## Builder
`archetypes/builders/experiment_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind experiment_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: exp_thinking_vs_standard
kind: experiment_config
pillar: P09
nucleus: n01
title: "Extended Thinking vs Standard Quality"
version: 1.0
quality: null
---
hypothesis: Extended thinking improves knowledge_card quality scores by >0.5
variants:
  - name: control
    traffic_pct: 50
    config: {thinking_tokens: 0}
  - name: thinking
    traffic_pct: 50
    config: {thinking_tokens: 8000}
success_metric: quality_score
min_sample_size: 30
```

## Related kinds
- `thinking_config` (P09) -- thinking settings used as variant configs
- `scoring_rubric` (P07) -- rubric that generates the success_metric values
- `feature_flag` (P09) -- flags can gate experiment variants by user segment

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_experiment_config]] | upstream | 0.49 |
| [[bld_schema_thinking_config]] | upstream | 0.48 |
| [[bld_schema_reranker_config]] | upstream | 0.48 |
| [[bld_schema_benchmark_suite]] | upstream | 0.47 |
| [[bld_schema_usage_report]] | upstream | 0.46 |
| [[bld_schema_search_strategy]] | upstream | 0.46 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.45 |
| [[bld_schema_dataset_card]] | upstream | 0.45 |
| [[bld_schema_eval_metric]] | upstream | 0.45 |
| [[bld_schema_sandbox_config]] | upstream | 0.45 |
