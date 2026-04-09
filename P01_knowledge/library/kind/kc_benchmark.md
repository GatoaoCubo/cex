---
id: p01_kc_benchmark
kind: knowledge_card
type: kind
pillar: P07
title: "Benchmark — Deep Knowledge for benchmark"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: benchmark
quality: 9.1
tags: [benchmark, P07, GOVERN, kind-kc]
tldr: "Quantitative performance measurement of latency, cost, or quality across repeated runs with statistical rigor."
when_to_use: "Building, reviewing, or reasoning about benchmark artifacts"
keywords: [benchmark, performance, latency, cost, measurement]
feeds_kinds: [benchmark]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["performance test", "speed test", "latency benchmark", "cost benchmark", "perf measurement"]
user_says: ["benchmark this", "benchmark disso", "measure performance", "how fast is it", "what does it cost per request"]
long_tails: ["I need to measure how fast my pipeline responds under load", "track the cost per 1000 tokens across different models", "run a performance benchmark with p50/p95/p99 latency percentiles", "compare latency before and after this optimization"]
cross_provider:
  langchain: "LangSmith traces + metrics"
  llamaindex: "IngestionBenchmark / BatchEvalRunner"
  crewai: "Task execution metrics (manual)"
  dspy: "Evaluate class + metrics"
  openai: "usage stats + Evals API"
  anthropic: "usage field + custom latency tracker"
  haystack: "BenchmarkMeta / EvaluationRunOverview"
---

# Benchmark

## Spec
```yaml
kind: benchmark
pillar: P07
llm_function: GOVERN
max_bytes: 4096
naming: p07_bm_{{metric}}.md + .yaml
core: false
```

## What It Is
A repeatable measurement protocol that quantifies system performance along a specific dimension (latency p50/p95/p99, cost per 1K tokens, quality score distribution) across N runs with statistical aggregation. NOT an eval—benchmark does not test correctness or pass/fail; it measures magnitude. NOT scoring_rubric—rubric defines criteria; benchmark executes and records numeric results.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | LangSmith traces + metrics | Automated latency + cost tracking per run |
| LlamaIndex | IngestionBenchmark / BatchEvalRunner | Batch eval with aggregate metrics |
| CrewAI | Task execution metrics | Manual timing + token count logging |
| DSPy | Evaluate class + metrics | evaluate() returns aggregate score |
| Haystack | BenchmarkMeta / EvaluationRunOverview | Built-in benchmark result schema |
| OpenAI | usage stats + Evals API | Token usage, latency in API response |
| Anthropic | usage field + custom tracker | Input/output tokens, latency per request |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| n_runs | int | 100 | Higher = more confidence, higher cost |
| warm_up | int | 10 | Excludes cold-start from p50/p95 |
| percentiles | list[int] | [50,95,99] | p99 reveals tail latency |
| metric | enum | latency_ms | latency_ms/cost_usd/quality_score |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Latency benchmark | Measure response time distribution | p07_bm_latency_ms.yaml |
| Cost benchmark | Track $ per 1K tokens over dataset | p07_bm_cost_usd.yaml |
| Quality benchmark | Score distribution on eval_dataset | p07_bm_quality_score.yaml |
| Regression guard | Compare before/after optimization | p07_bm_latency_ms + regression_check |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Single-run benchmark | No statistical significance | Minimum n=30, report p50+p95 |
| Benchmarking on prod data | Contaminates prod, leaks costs | Use eval_dataset on staging |
| Confusing with correctness eval | Benchmark doesn't test right/wrong | Pair with unit_eval for correctness |

## Integration Graph
```
[eval_dataset] --> [benchmark] --> [regression_check]
[scoring_rubric] -> [benchmark]         |
                        |-----------> [quality_gate (P11)]
                        |-----------> [pipeline report]
```

## Decision Tree
- IF measuring quantitative performance (time/cost/score distribution) THEN benchmark
- IF testing correct output for given input THEN unit_eval or e2e_eval
- IF comparing current vs previous run THEN regression_check (uses benchmark output)
- DEFAULT: benchmark for any recurring performance tracking need

## Quality Criteria
- GOOD: n_runs >= 30, metric clearly defined, percentiles reported
- GREAT: Warm-up excluded, p95/p99 reported, baseline stored for regression_check
- FAIL: Single run, no percentiles, mixing correctness testing with performance measurement
