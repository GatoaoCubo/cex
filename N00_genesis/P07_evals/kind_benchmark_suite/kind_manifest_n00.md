---
id: n00_benchmark_suite_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Benchmark Suite -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, benchmark_suite, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Benchmark suite defines a composite evaluation package that groups multiple benchmarks into a unified test plan with shared configuration, execution order, and aggregate scoring. It enables comprehensive system evaluation covering multiple dimensions (latency, cost, quality, safety) in a single run. Suite results produce a multi-dimensional performance profile used for release gating.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `benchmark_suite` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Suite name describing scope |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| benchmarks | list | yes | Ordered list of benchmark IDs included in suite |
| execution_mode | enum | yes | sequential / parallel |
| gate_threshold | object | yes | Min scores per metric for suite to pass |
| aggregate_score_method | enum | yes | weighted_avg / min / geometric_mean |
| report_format | enum | yes | markdown / json / html |

## When to use
- Running a full pre-release quality check across all performance dimensions
- Comparing two complete system configurations (e.g., Claude vs. Ollama routing)
- Establishing the canonical performance profile for a new nucleus configuration

## Builder
`archetypes/builders/benchmark_suite-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind benchmark_suite --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence owns; N05 operations runs the harness
- `{{SIN_LENS}}` -- Analytical Envy: comprehensive coverage, no dimension left unmeasured
- `{{TARGET_AUDIENCE}}` -- release managers and architects reviewing pre-release performance
- `{{DOMAIN_CONTEXT}}` -- system scope, release criteria, benchmark dimensions

## Example (minimal)
```yaml
---
id: benchmark_suite_cex_pre_release
kind: benchmark_suite
pillar: P07
nucleus: n01
title: "CEX Pre-Release Benchmark Suite"
version: 1.0
quality: null
---
execution_mode: parallel
aggregate_score_method: weighted_avg
report_format: markdown
gate_threshold: {p99_latency_ms: 5000, quality_score: 8.0, cost_per_run_usd: 0.10}
```

## Related kinds
- `benchmark` (P07) -- individual benchmark that composes into this suite
- `eval_framework` (P07) -- integration framework that executes the suite
- `regression_check` (P07) -- compares suite results against prior release baseline
