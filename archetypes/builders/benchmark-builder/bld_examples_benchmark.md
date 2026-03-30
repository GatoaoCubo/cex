---
kind: examples
id: bld_examples_benchmark
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of benchmark artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: benchmark-builder
## Golden Example
INPUT: "Cria benchmark de latencia TTFT comparando Sonnet 4 vs Haiku 4.5"
OUTPUT:
```yaml
id: p07_bm_ttft_sonnet4_vs_haiku45
kind: benchmark
pillar: P07
title: "Benchmark: TTFT Sonnet 4 vs Haiku 4.5"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
metric: "time_to_first_token"
unit: "ms"
direction: "lower_is_better"
baseline: 850
target: 400
iterations: 100
warmup: 10
percentiles: [50, 75, 95, 99]
environment: "Railway PRO, us-east-1, Python 3.12, httpx 0.27, 2 vCPU / 4GB RAM"
domain: "llm_inference"
quality: null
tags: [benchmark, ttft, latency, model-comparison, sonnet, haiku]
tldr: "TTFT benchmark: Sonnet 4 (850ms baseline) vs Haiku 4.5 (target 400ms), 100 iterations, p50/p95/p99 on Railway PRO"
comparison_subjects: [claude-sonnet-4-20250514, claude-haiku-4-5-20251001]
statistical_test: "Mann-Whitney U"
confidence_interval: 0.95
density_score: 0.91
linked_artifacts:
  primary: "p02_mc_anthropic_sonnet_4"
  related: [p02_mc_anthropic_haiku_45]
## Benchmark Overview
Measures Time To First Token (TTFT) for Claude Sonnet 4 vs Haiku 4.5 on identical prompts.
TTFT directly impacts perceived responsiveness in streaming UIs.
Business impact: Haiku 4.5 at <400ms enables sub-second perceived start for chat interfaces.
## Methodology
- **Iterations**: 100 runs per model
- **Warmup**: 10 runs discarded (connection pool, TLS handshake)
- **Protocol**: Send identical 500-token prompt via Anthropic API, measure time from request sent to first SSE chunk received
- **Statistical test**: Mann-Whitney U at 95% confidence (non-parametric, no normality assumption)
- **Outlier handling**: Report but do not discard; p99 captures tail
## Metrics
| Metric | Unit | Direction | Baseline (Sonnet 4) | Target (Haiku 4.5) |
|--------|------|-----------|---------------------|---------------------|
| TTFT | ms | lower_is_better | 850 | 400 |
| TTFT p95 | ms | lower_is_better | 1200 | 600 |
| TTFT p99 | ms | lower_is_better | 1800 | 900 |
## Environment
- **Hardware**: Railway PRO, us-east-1, 2 vCPU / 4GB RAM
- **Software**: Python 3.12, httpx 0.27, anthropic SDK 0.52
- **Config**: max_tokens=100, temperature=0, no system prompt, streaming=true
- **Date**: 2026-03-26
## Results Template
| Percentile | Sonnet 4 | Haiku 4.5 | Delta (ms) | Delta (%) |
|------------|----------|-----------|------------|-----------|
| p50 | — | — | — | — |
| p75 | — | — | — | — |
| p95 | — | — | — | — |
| p99 | — | — | — | — |
## References
- Anthropic API docs: https://docs.anthropic.com/en/api
- wrk2 percentile methodology: https://github.com/giltene/wrk2
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p07_bm_ pattern (H02 pass)
- kind: benchmark (H04 pass)
- 22 required fields present (H07 pass)
- iterations 100 >= 10 (H08 pass)
- warmup 10 >= 1 (H09 pass)
- percentiles include p50 and p95 (H10 pass)
- direction explicit: lower_is_better (H11 pass)
- baseline and target same unit: ms (H12 pass)
- environment specific: Railway PRO, us-east-1, exact versions (S05 pass)
- methodology reproducible with exact protocol (S04 pass)
- tldr <= 160 chars, dense (S01 pass)
## Anti-Example
INPUT: "Benchmark de performance"
BAD OUTPUT:
```yaml
id: perf_bench
kind: benchmark
title: "Performance Test"
iterations: 3
warmup: 0
percentiles: [50]
baseline: "fast"
target: "faster"
quality: 8.5
tags: benchmark
## Results
The system was tested and found to be performing well.
Average latency was acceptable.
```
FAILURES:
1. id: no p07_bm_ prefix -> H02 FAIL
2. pillar: missing -> H05 FAIL
3. quality: 8.5 (not null) -> H06 FAIL
4. iterations: 3 < 10 minimum -> H08 FAIL
5. warmup: 0 < 1 minimum -> H09 FAIL
6. percentiles: only p50, missing p95 -> H10 FAIL
7. direction: missing -> H11 FAIL
8. baseline/target: strings "fast"/"faster" not numbers -> H12 FAIL
