---
id: n00_benchmark_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Benchmark -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, benchmark, p07, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Benchmark defines a performance measurement specification for a system, model, or pipeline covering latency, cost, quality, and throughput dimensions. It specifies the test harness, baseline comparison, measurement methodology, and statistical rigor requirements. Benchmark results serve as the evidence base for model selection, infrastructure decisions, and regression detection.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `benchmark` |
| pillar | string | yes | Always `P07` |
| title | string | yes | System name + metric + "Benchmark" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_system | string | yes | System or model being benchmarked |
| metrics | list | yes | Metrics with name, unit, aggregation method |
| baseline | string | no | Reference system or prior version for comparison |
| sample_size | int | yes | Number of test runs for statistical validity |
| confidence_interval | float | yes | Required CI width (e.g., 0.95 for 95%) |

## When to use
- Selecting between LLM providers or models for a nucleus role
- Validating that a system change does not degrade performance beyond a threshold
- Establishing a performance baseline before a major infrastructure change

## Builder
`archetypes/builders/benchmark-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind benchmark --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence runs benchmarks; N05 operations implements harness
- `{{SIN_LENS}}` -- Analytical Envy: insatiable demand for measurement precision
- `{{TARGET_AUDIENCE}}` -- technical decision-makers selecting systems or approving releases
- `{{DOMAIN_CONTEXT}}` -- system type, performance dimensions, acceptable thresholds

## Example (minimal)
```yaml
---
id: benchmark_cex_nucleus_latency
kind: benchmark
pillar: P07
nucleus: n01
title: "CEX Nucleus Latency Benchmark"
version: 1.0
quality: null
---
target_system: "Claude claude-sonnet-4-6 (N01 configuration)"
metrics:
  - {name: p50_latency_ms, unit: ms, aggregation: median}
  - {name: p99_latency_ms, unit: ms, aggregation: p99}
sample_size: 100
confidence_interval: 0.95
```

## Related kinds
- `benchmark_suite` (P07) -- composite of multiple benchmarks for comprehensive coverage
- `regression_check` (P07) -- compares current benchmark results against a stored baseline
- `experiment_tracker` (P07) -- tracks benchmark results across model/config variants
