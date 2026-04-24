---
id: n00_regression_check_manifest
kind: knowledge_card
8f: F3_inject
pillar: P07
nucleus: n00
title: "Regression Check -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, regression_check, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_regression_check
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - regression-check-builder
  - bld_schema_reranker_config
  - bld_schema_eval_metric
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_optimizer
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Regression check defines the comparison methodology for detecting quality degradation between a current system version and a stored baseline. It specifies which metrics to compare, the acceptable deviation threshold per metric, the baseline snapshot reference, and the alerting behavior on regression detection. Regression checks are the continuous quality monitoring mechanism that protects production systems from silent degradation.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `regression_check` |
| pillar | string | yes | Always `P07` |
| title | string | yes | System name + "Regression Check" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| baseline_id | string | yes | ID of the golden test or benchmark result used as baseline |
| metrics_monitored | list | yes | Metrics with acceptable deviation thresholds |
| comparison_method | enum | yes | absolute_diff / relative_diff / statistical_test |
| alert_on | enum | yes | any_regression / critical_only / threshold_breach |
| remediation_action | enum | yes | block_deploy / alert_only / auto_rollback |

## When to use
- Protecting a production model from silent quality degradation after each deployment
- Detecting capability regressions after prompt changes or model updates
- Gating a release when a benchmark result falls below the baseline

## Builder
`archetypes/builders/regression_check-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind regression_check --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations runs checks; N01 intelligence interprets results
- `{{SIN_LENS}}` -- Gating Wrath: block any regression before it reaches production
- `{{TARGET_AUDIENCE}}` -- CI/CD pipeline and release managers
- `{{DOMAIN_CONTEXT}}` -- system type, deployment cadence, acceptable drift thresholds

## Example (minimal)
```yaml
---
id: regression_check_cex_artifact_quality
kind: regression_check
pillar: P07
nucleus: n05
title: "CEX Artifact Quality Regression Check"
version: 1.0
quality: null
---
baseline_id: benchmark_cex_nucleus_quality_baseline
comparison_method: relative_diff
alert_on: threshold_breach
remediation_action: block_deploy
metrics_monitored:
  - {metric: artifact_quality_score, max_regression_pct: 5.0}
```

## Related kinds
- `golden_test` (P07) -- baseline artifact that regression checks compare against
- `benchmark` (P07) -- provides current measurements for comparison
- `experiment_tracker` (P07) -- tracks regression check results over time

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_regression_check]] | upstream | 0.47 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
| [[regression-check-builder]] | related | 0.41 |
| [[bld_schema_reranker_config]] | upstream | 0.41 |
| [[bld_schema_eval_metric]] | upstream | 0.40 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_search_strategy]] | upstream | 0.40 |
| [[bld_schema_dataset_card]] | upstream | 0.39 |
| [[bld_schema_optimizer]] | upstream | 0.39 |
