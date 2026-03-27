---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for benchmark production
sources: [Google Benchmark, wrk2, MLPerf, LMSYS Chatbot Arena, CEX validate_kc.py]
---

# Domain Knowledge: benchmark

## Foundational Concepts
Benchmarking originates from performance engineering (Jain 1991 "Art of Computer Systems Performance Analysis").
In LLM systems: measuring latency (TTFT, TPS), cost (per 1M tokens), quality (judge scores), and throughput (req/s).
In CEX: quantitative measurement with baselines, targets, percentiles, and reproducible methodology.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Google Benchmark | C++ microbenchmark framework with warmup, iterations, statistics | Warmup + iterations + percentile pattern |
| wrk2 / hey | HTTP load testing with latency histograms | Percentile reporting (p50, p95, p99) |
| MLPerf | ML training/inference benchmarks with strict methodology | Environment specification, reproducibility |
| LMSYS Chatbot Arena | LLM comparison via Elo rating | Comparison subjects, A/B methodology |
| Anthropic Model Card | Latency, TPS, cost per model | Metric/unit/baseline pattern |

## Key Principles
- Warmup is MANDATORY (JIT, caching, connection pools need pre-heating)
- Percentiles over averages (p99 reveals tail latency that avg hides)
- Environment MUST be documented (CPU, RAM, OS, network, config)
- Baseline MUST be measured, not estimated
- Iterations MUST be sufficient for statistical significance (>= 10, prefer >= 30)
- Direction MUST be explicit (lower_is_better for latency, higher_is_better for throughput)
- Comparison requires same environment, same methodology, same time window
- Cold start vs warm: measure and report both

## Common LLM Benchmark Metrics
| Metric | Unit | Direction | Typical range |
|--------|------|-----------|---------------|
| TTFT (Time To First Token) | ms | lower_is_better | 200-2000ms |
| TPS (Tokens Per Second) | tokens/s | higher_is_better | 30-150 |
| Cost per 1M input tokens | USD | lower_is_better | $0.25-$15.00 |
| Cost per 1M output tokens | USD | lower_is_better | $1.00-$75.00 |
| Requests per second | req/s | higher_is_better | 10-1000 |
| Context window utilization | % | higher_is_better | 50-100% |

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| direction | Makes optimization goal explicit | wrk2: implicit from metric name |
| comparison_subjects | Enables multi-model/multi-config comparison | MLPerf: submission categories |
| percentiles as list | Flexible reporting granularity | wrk2: fixed p50/p75/p90/p99 |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| scoring_rubric (P07) | Defines multi-dimensional QUALITY criteria | Does NOT produce numbers |
| unit_eval (P07) | Tests CORRECTNESS of specific behavior | Does NOT measure speed/cost |
| golden_test (P07) | Provides REFERENCE example at 9.5+ | Does NOT provide metrics |
| quality_gate (P11) | Enforces PASS/FAIL threshold | Does NOT run measurements |

## References
- Jain 1991: The Art of Computer Systems Performance Analysis
- wrk2: https://github.com/giltene/wrk2
- MLPerf: https://mlcommons.org/benchmarks/
- LMSYS Chatbot Arena: https://chat.lmsys.org
