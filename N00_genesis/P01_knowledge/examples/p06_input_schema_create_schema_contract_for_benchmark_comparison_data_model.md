---
id: p06_is_benchmark_comparison
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "benchmark comparison analysis — evaluates performance difference between baseline and candidate metric values"
fields:
  - name: "benchmark_name"
    type: "string"
    required: true
    default: null
    description: "Unique identifier for the benchmark suite or test being evaluated"
    error_message: "benchmark_name is required — provide the benchmark suite name (e.g., 'mmlu_5shot', 'latency_p95')"
  - name: "baseline_metric"
    type: "float"
    required: true
    default: null
    description: "Reference performance value from the prior version or control condition"
    error_message: "baseline_metric is required — provide a numeric reference value (e.g., 0.823)"
  - name: "comparison_metric"
    type: "float"
    required: true
    default: null
    description: "Candidate performance value from the new version or experimental condition"
    error_message: "comparison_metric is required — provide a numeric candidate value (e.g., 0.851)"
  - name: "metric_type"
    type: "string"
    required: true
    default: null
    description: "Category of metric; governs direction interpretation. Enum: accuracy, latency, throughput, cost, error_rate, custom"
    error_message: "metric_type is required — one of: accuracy, latency, throughput, cost, error_rate, custom"
  - name: "direction"
    type: "string"
    required: false
    default: "auto"
    description: "Whether improvement means higher or lower values. Enum: higher_is_better, lower_is_better, auto. 'auto' infers from metric_type."
    error_message: null
  - name: "significance_threshold"
    type: "float"
    required: false
    default: 0.05
    description: "P-value threshold for declaring a difference statistically significant. Range: 0.001–0.20."
    error_message: null
  - name: "analysis_mode"
    type: "string"
    required: false
    default: "percentage"
    description: "How to compute and report the difference. Enum: percentage, absolute, ratio, z_score."
    error_message: null
  - name: "sample_sizes"
    type: "object"
    required: false
    default: null
    description: "Optional sample counts for significance testing. Shape: {baseline: int, comparison: int}."
    error_message: null
  - name: "tags"
    type: "list"
    required: false
    default: []
    description: "Labels for grouping or filtering results (e.g., ['nightly', 'model-v3', 'regression'])."
    error_message: null
  - name: "output_format"
    type: "string"
    required: false
    default: "summary"
    description: "Format for the comparison report. Enum: summary, detailed, table, json."
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse baseline_metric and comparison_metric from numeric strings (e.g., '0.823' -> 0.823); reject non-numeric strings with error"
  - from: "integer"
    to: "float"
    rule: "Promote integer metric values to float silently (e.g., 95 -> 95.0)"
  - from: "string"
    to: "list"
    rule: "Parse comma-separated string into list for tags field (e.g., 'nightly,v3' -> ['nightly', 'v3'])"
examples:
  - benchmark_name: "mmlu_5shot"
    baseline_metric: 0.712
    comparison_metric: 0.741
    metric_type: "accuracy"
    direction: "higher_is_better"
    significance_threshold: 0.05
    analysis_mode: "percentage"
    sample_sizes: {baseline: 500, comparison: 500}
    tags: ["nightly", "model-v3"]
    output_format: "summary"
  - benchmark_name: "api_latency_p95"
    baseline_metric: 320.5
    comparison_metric: 289.1
    metric_type: "latency"
    direction: "lower_is_better"
    analysis_mode: "absolute"
    output_format: "detailed"
domain: "benchmark-analysis"
quality: 9.1
tags: [input-schema, benchmark-comparison, performance-evaluation, metrics]
tldr: "Input contract for benchmark comparison: requires benchmark name, baseline/comparison floats, metric type; optional direction, threshold, analysis mode, sample sizes."
density_score: 0.91
keywords: [benchmark, comparison, baseline, metric, performance, evaluation, significance, analysis_mode, direction, coercion]
related:
  - bld_schema_optimizer
  - bld_schema_eval_metric
  - bld_schema_benchmark
  - bld_schema_input_schema
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - p06_is_knowledge_data_model
  - p06_is_creation_data
  - bld_schema_usage_report
  - bld_schema_memory_benchmark
---
## Contract Definition

Benchmark comparison operations receive structured input specifying which benchmark is being evaluated, the baseline and candidate metric values to compare, and the metric category. The receiving system computes the performance delta, determines statistical significance if sample sizes are provided, and generates a comparison report in the requested format. Used by evaluation agents, CI regression checkers, and model assessment pipelines.

Required fields define the comparison identity (benchmark name), the data points (baseline and comparison floats), and the metric semantics (type + direction). Optional fields control analysis depth, statistical rigor, and report verbosity.

## Fields

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | benchmark_name | string | YES | — | Benchmark suite or test identifier |
| 2 | baseline_metric | float | YES | — | Reference performance value (prior version / control) |
| 3 | comparison_metric | float | YES | — | Candidate performance value (new version / experiment) |
| 4 | metric_type | string | YES | — | Metric category: accuracy, latency, throughput, cost, error_rate, custom |
| 5 | direction | string | NO | "auto" | Improvement direction: higher_is_better, lower_is_better, auto |
| 6 | significance_threshold | float | NO | 0.05 | P-value cutoff for significance declaration |
| 7 | analysis_mode | string | NO | "percentage" | Delta computation: percentage, absolute, ratio, z_score |
| 8 | sample_sizes | object | NO | null | {baseline: int, comparison: int} for significance testing |
| 9 | tags | list | NO | [] | Grouping labels for filtering and reporting |
| 10 | output_format | string | NO | "summary" | Report format: summary, detailed, table, json |

## Coercion Rules

| From | To | Field(s) | Rule |
|------|----|----------|------|
| string | float | baseline_metric, comparison_metric | Parse numeric strings; reject non-numeric with field-named error |
| integer | float | baseline_metric, comparison_metric | Silent promotion — no data loss |
| string | list | tags | Split on comma, strip whitespace from each element |

`direction: "auto"` resolves as follows: accuracy → higher_is_better; latency, cost → lower_is_better; throughput → higher_is_better; error_rate → lower_is_better; custom → caller must supply explicit direction or field is rejected.

## Examples

```json
{
  "benchmark_name": "mmlu_5shot",
  "baseline_metric": 0.712,
  "comparison_metric": 0.741,
  "metric_type": "accuracy",
  "direction": "higher_is_better",
  "significance_threshold": 0.05,
  "analysis_mode": "percentage",
  "sample_sizes": {"baseline": 500, "comparison": 500},
  "tags": ["nightly", "model-v3"],
  "output_format": "summary"
}
```

```json
{
  "benchmark_name": "api_latency_p95",
  "baseline_metric": 320.5,
  "comparison_metric": 289.1,
  "metric_type": "latency",
  "output_format": "detailed"
}
```

Invalid example (triggers errors):
```json
{
  "benchmark_name": "hellaswag",
  "baseline_metric": "not_a_number",
  "comparison_metric": 0.88
}
```
Failures: `baseline_metric` coercion fails (non-numeric string); `metric_type` missing → error: "metric_type is required".

## References
- JSON Schema draft-07: json-schema.org
- MLflow metrics API: mlflow.org/docs/latest/tracking
- OpenAI Evals framework: github.com/openai/evals

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_optimizer]] | related | 0.36 |
| [[bld_schema_eval_metric]] | related | 0.36 |
| [[bld_schema_benchmark]] | related | 0.36 |
| [[bld_schema_input_schema]] | related | 0.35 |
| [[bld_schema_benchmark_suite]] | related | 0.35 |
| [[bld_schema_reranker_config]] | related | 0.32 |
| [[p06_is_knowledge_data_model]] | sibling | 0.31 |
| [[p06_is_creation_data]] | sibling | 0.30 |
| [[bld_schema_usage_report]] | related | 0.30 |
| [[bld_schema_memory_benchmark]] | related | 0.30 |
