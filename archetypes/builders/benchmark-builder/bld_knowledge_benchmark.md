---
kind: knowledge_card
id: bld_knowledge_card_benchmark
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for benchmark production — quantitative performance measurement
sources: Jain 1991, MLPerf, wrk2, LMSYS Chatbot Arena, Anthropic model cards
quality: 9.1
title: "Knowledge Card Benchmark"
version: "1.0.0"
author: n03_builder
tags: [benchmark, builder, examples]
tldr: "Golden and anti-examples for benchmark construction, demonstrating ideal structure and common pitfalls."
domain: "benchmark construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_benchmark_builder
  - bld_instruction_benchmark
  - benchmark-builder
  - p11_qg_benchmark
  - bld_output_template_benchmark
  - bld_examples_benchmark
  - p01_kc_benchmark
  - bld_architecture_benchmark
  - bld_schema_benchmark
  - p10_lr_benchmark-builder
---

# Domain Knowledge: benchmark
## Executive Summary
Benchmarks measure quantitative performance (latency, cost, throughput, quality scores) under controlled, reproducible conditions. They require baselines, targets, warmup periods, and statistical rigor via percentiles. Benchmarks differ from scoring rubrics (qualitative criteria), unit evals (correctness assertions), and golden tests (reference examples).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (governance/evaluation) |
| Frontmatter fields | 22 |
| Quality gates | 10 HARD + 9 SOFT |
| Statistical minimum | p50, p95, p99 percentiles |
| Min iterations | >= 30 for statistical significance |
| Warmup | 10-20% of total iterations discarded |
| Required sections | methodology, environment, baseline, target, results |
## Patterns
- **Baseline-target pair**: every benchmark defines current state (baseline) and goal (target) — without both, results are uninterpretable
- **Percentile reporting**: report p50, p95, p99 — averages hide tail latency that degrades real user experience
- **Warmup period**: discard first 10-20% of iterations for JIT, caching, and connection pool warming
- **Environment documentation**: exact hardware, model version, concurrency, date — benchmarks compare only under identical conditions
- **Cost normalization**: cost per 1K tokens or per request enables cross-model comparison
| Metric | Unit | Direction | Range |
|--------|------|-----------|-------|
| TTFT | ms | lower_is_better | 200-2000 |
| TPS | tokens/s | higher_is_better | 30-150 |
| Input cost | USD/1M tokens | lower_is_better | $0.25-$15 |
| Output cost | USD/1M tokens | lower_is_better | $1-$75 |
| Throughput | req/s | higher_is_better | 10-1000 |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Average-only reporting | Hides p99 tail; 50ms avg masks 2s spikes |
| No warmup period | Cold-start skews results; baseline is wrong |
| Missing environment spec | Not reproducible; "fast on my machine" |
| No baseline defined | Cannot tell if results are good or bad |
| One-run measurement | Statistical noise; need >= 30 iterations |
| Mixed metrics (quality + speed) | Conflates dimensions; separate benchmarks |
## Application
1. Define metric: what exactly is measured (latency, cost, throughput)?
2. Document environment: hardware, model, concurrency, date
3. Establish baseline: current performance under standard load
4. Set target: desired performance with justification
5. Run: discard warmup (10-20%), collect >= 30 iterations
6. Report: p50, p95, p99 with confidence intervals
## References
- Jain 1991: The Art of Computer Systems Performance Analysis
- MLPerf: standardized ML benchmarking methodology
- wrk2: latency-accurate HTTP benchmarking tool
- LMSYS Chatbot Arena: LLM comparison via Elo rating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_benchmark_builder]] | downstream | 0.52 |
| [[bld_instruction_benchmark]] | downstream | 0.47 |
| [[benchmark-builder]] | downstream | 0.44 |
| [[p11_qg_benchmark]] | downstream | 0.44 |
| [[bld_output_template_benchmark]] | downstream | 0.40 |
| [[bld_examples_benchmark]] | downstream | 0.40 |
| [[p01_kc_benchmark]] | sibling | 0.37 |
| [[bld_architecture_benchmark]] | downstream | 0.33 |
| [[bld_schema_benchmark]] | downstream | 0.32 |
| [[p10_lr_benchmark-builder]] | downstream | 0.32 |
