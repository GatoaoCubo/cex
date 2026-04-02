---
id: p06_is_benchmark_comparison
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "benchmark comparison analysis operation"
fields:
  - name: "benchmark_name"
    type: "string"
    required: true
    default: null
    description: "Name of the benchmark being evaluated"
    error_message: "benchmark_name is required - provide benchmark identifier"
  - name: "baseline_metric"
    type: "float"
    required: true
    default: null
    description: "Baseline performance metric value for comparison"
    error_message: "baseline_metric is required - provide numerical baseline value"
  - name: "comparison_metric"
    type: "float"
    required: true
    default: null
    description: "New performance metric value to compare against baseline"
    error_message: "comparison_metric is required - provide numerical comparison value"
  - name: "metric_type"
    type: "string"
    required: true
    default: null
    description: "Type of metric being compared (accuracy, latency, throughput, f1_score, etc.)"
    error_message: "metric_type is required - specify what metric is being measured"
  - name: "comparison_type"
    type: "string"
    required: false
    default: "relative"
    description: "Type of comparison analysis (relative, absolute, percentage)"
    error_message: null
  - name: "threshold"
    type: "float"
    required: false
    default: 0.05
    description: "Threshold for determining statistically significant difference"
    error_message: null
  - name: "metadata"
    type: "object"
    required: false
    default: null
    description: "Additional context: dataset, model_version, test_conditions, etc."
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse numeric strings to float for baseline_metric and comparison_metric"
  - from: "integer"
    to: "float"
    rule: "Convert integer metrics to float for consistent processing"
examples:
  - {benchmark_name: "llama_accuracy_test", baseline_metric: 0.85, comparison_metric: 0.87, metric_type: "accuracy", comparison_type: "relative", threshold: 0.02}
  - {benchmark_name: "response_latency", baseline_metric: 150.5, comparison_metric: 142.8, metric_type: "latency_ms", threshold: 5.0, metadata: {dataset: "eval_v2", model: "gpt-4"}}
domain: "benchmark-analysis"
quality: 8.9
tags: [input-schema, benchmark-comparison, performance-analysis, P06]
tldr: "Input contract for benchmark comparison: requires benchmark name, baseline/comparison metrics, metric type, with optional analysis parameters."
density_score: 0.88
---
# Benchmark Comparison Input Schema

## Contract Definition
This input schema defines the data contract for benchmark comparison analysis operations. The receiving system analyzes performance differences between baseline and new metric values, determining statistical significance and generating comparison reports. Used by performance evaluation agents and model assessment pipelines.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | benchmark_name | string | YES | - | Name of the benchmark being evaluated |
| 2 | baseline_metric | float | YES | - | Baseline performance metric value for comparison |
| 3 | comparison_metric | float | YES | - | New performance metric value to compare against baseline |
| 4 | metric_type | string | YES | - | Type of metric being compared (accuracy, latency, throughput, f1_score, etc.) |
| 5 | comparison_type | string | NO | "relative" | Type of comparison analysis (relative, absolute, percentage) |
| 6 | threshold | float | NO | 0.05 | Threshold for determining statistically significant difference |
| 7 | metadata | object | NO | null | Additional context: dataset, model_version, test_conditions, etc. |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | float | Parse numeric strings to float for baseline_metric and comparison_metric |
| integer | float | Convert integer metrics to float for consistent processing |

## Examples
```json
{"benchmark_name": "llama_accuracy_test", "baseline_metric": 0.85, "comparison_metric": 0.87, "metric_type": "accuracy", "comparison_type": "relative", "threshold": 0.02}
```

```json
{"benchmark_name": "response_latency", "baseline_metric": 150.5, "comparison_metric": 142.8, "metric_type": "latency_ms", "threshold": 5.0, "metadata": {"dataset": "eval_v2", "model": "gpt-4"}}
```

## Validation Constraints
- benchmark_name: non-empty string, alphanumeric with underscores
- baseline_metric, comparison_metric: positive numbers for most metrics, negative allowed for error rates
- metric_type: constrained to performance measurement types (accuracy, precision, recall, f1_score, latency_ms, throughput_ops, error_rate, memory_mb)
- comparison_type: enum values (relative, absolute, percentage, z_score)
- threshold: positive float between 0.001 and 1.0
- metadata: flat object, max 10 keys, values must be strings or numbers

## Error Handling
Required field errors specify which field is missing and expected type. Type coercion failures indicate source value and expected target type. Validation constraint violations provide acceptable range or format requirements.