---
id: p07_benchmark_api_latency
kind: benchmark
pillar: P07
title: API Latency Benchmark Suite
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: performance-operations
quality: 8.9
tags: [benchmark, performance, operations, N05, latency, api, load-test]
tldr: "API latency benchmark suite with baseline targets, statistical methodology, regression detection, and reproducible load test configurations."
density_score: 0.96
related:
  - p07_regcheck_latency_baseline
  - p11_qg_performance
  - p01_kc_benchmark
  - benchmark-builder
  - kc_api_reference
  - p11_qg_benchmark
  - p03_sp_benchmark_builder
  - bld_collaboration_benchmark
  - bld_architecture_benchmark
  - bld_knowledge_card_benchmark
---

# API Latency Benchmark Suite

## Overview

This benchmark suite measures API response latency across critical endpoints
under controlled load conditions. Baselines are established, regressions are
detected, and performance budgets are enforced. No deploy ships without
passing the latency gate.

## Benchmark Targets

### Critical Endpoints

| endpoint | method | p50_target | p95_target | p99_target | concurrency |
|----------|--------|-----------|-----------|-----------|-------------|
| /health | GET | 5ms | 15ms | 50ms | 10 |
| /pipeline/health | GET | 10ms | 30ms | 100ms | 10 |
| /api/v1/auth/login | POST | 50ms | 150ms | 300ms | 20 |
| /api/v1/search | POST | 100ms | 300ms | 500ms | 50 |
| /api/v1/create | POST | 50ms | 150ms | 300ms | 20 |
| /api/v1/list | GET | 30ms | 100ms | 200ms | 50 |
| /api/v1/detail/{id} | GET | 20ms | 60ms | 150ms | 50 |

### Load Profiles

| profile | concurrent_users | ramp_up_s | duration_s | purpose |
|---------|-----------------|-----------|-----------|---------|
| smoke | 5 | 0 | 10 | Quick sanity check |
| baseline | 20 | 5 | 60 | Establish performance baseline |
| stress | 100 | 10 | 120 | Find breaking point |
| soak | 20 | 5 | 600 | Detect memory leaks and drift |

## Methodology

### Statistical Requirements

- **Minimum samples**: 1000 per endpoint per profile
- **Warm-up**: Discard first 100 requests (cold start noise)
- **Percentiles**: p50, p75, p90, p95, p99 — all reported
- **Outlier handling**: Report but do not discard — outliers are real user experience
- **Reproducibility**: Same load profile, same data fixtures, same Railway service tier

### Regression Detection

```
regression_threshold = 10%  # p95 delta vs baseline
critical_threshold  = 25%  # triggers deploy block

if current_p95 > baseline_p95 * 1.10:
    status = "REGRESSION_WARNING"
if current_p95 > baseline_p95 * 1.25:
    status = "REGRESSION_BLOCKED"
    action = "block deploy, investigate root cause"
```

## Execution

### Local Benchmark

```bash
# Using hey (Go HTTP load generator)
hey -n 1000 -c 20 -m GET http://localhost:8000/health
hey -n 1000 -c 50 -m POST -H "Content-Type: application/json" -d '{"q":"test"}' http://localhost:8000/api/v1/search
```

### Railway Benchmark

```bash
# Against production (with rate limit awareness)
hey -n 500 -c 10 -m GET https://api.example.railway.app/health
```

## Reporting Format

```markdown
## Benchmark Report: {date}_{profile}

| Endpoint | p50 | p95 | p99 | Baseline p95 | Delta | Status |
|----------|-----|-----|-----|-------------|-------|--------|

### Summary
- Total requests: {n}
- Error rate: {pct}%
- Throughput: {rps} req/s
- Regression: {yes/no}
```

## Baseline History

| date | profile | health_p95 | search_p95 | create_p95 | notes |
|------|---------|-----------|-----------|-----------|-------|
| 2026-04-07 | baseline | TBD | TBD | TBD | Initial benchmark — baselines to be established |

## Boundary

Medicao de performance quantitativa. NAO eh eval (nao testa corretude) nem scoring_rubric (nao define criterios).

## 8F Pipeline Function

Primary function: **GOVERN**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_regcheck_latency_baseline]] | related | 0.41 |
| [[p11_qg_performance]] | downstream | 0.39 |
| [[p01_kc_benchmark]] | related | 0.33 |
| [[benchmark-builder]] | related | 0.29 |
| [[kc_api_reference]] | upstream | 0.29 |
| [[p11_qg_benchmark]] | downstream | 0.28 |
| [[p03_sp_benchmark_builder]] | upstream | 0.28 |
| [[bld_collaboration_benchmark]] | downstream | 0.28 |
| [[bld_architecture_benchmark]] | downstream | 0.27 |
| [[bld_knowledge_card_benchmark]] | upstream | 0.27 |
