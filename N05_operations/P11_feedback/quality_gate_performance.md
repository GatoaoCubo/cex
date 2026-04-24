---
id: p11_qg_performance
kind: quality_gate
8f: F7_govern
pillar: P11
title: "Gate: Performance Validation"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: performance-operations
quality: 8.9
tags: [quality_gate, performance, operations, N05, benchmark, latency]
tldr: "Performance validation gate covering API latency, database query time, memory utilization, startup time, and throughput benchmarks."
density_score: 0.97
related:
  - p07_benchmark_api_latency
  - p11_qg_railway_superintendent
  - p11_qg_artifact
  - p11_qg_security
  - p07_regcheck_latency_baseline
  - p02_agent_railway_superintendent
  - p08_ac_railway_superintendent
  - p01_kc_api_health_monitoring
  - p03_sp_railway_superintendent
  - p06_schema_health_response
---

## Definition

| Property | Value |
|----------|-------|
| Metric | performance_validation_score |
| Threshold | 0.88 |
| Operator | >= |
| Scope | All API endpoints, database queries, startup sequences, and resource-intensive operations |

## Hard Gates

| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| PERF01 | API response latency p95 under threshold | < 500ms | true |
| PERF02 | Database query execution time p95 | < 100ms | true |
| PERF03 | Application startup time | < 30s | true |
| PERF04 | Memory utilization under Railway plan limit | < 512MB | true |
| PERF05 | No N+1 query patterns in ORM/database access | 0 violations | true |
| PERF06 | Connection pool utilization under 80% at steady state | < 80% | true |
| PERF07 | Health endpoint response time | < 50ms | true |

## Soft Gates

| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| SP01 | API latency p99 under extended threshold | 0.10 | 0.25 |
| SP02 | Throughput handles expected concurrent users | 0.10 | 0.20 |
| SP03 | No latency regression vs previous baseline | 0.10 | 0.20 |
| SP04 | Resource cleanup (no memory leaks over 1h run) | 0.10 | 0.20 |
| SP05 | Cache hit ratio for repeated queries | 0.10 | 0.15 |

## Validation Criteria

- **PERF01**: Load test with `wrk` or `hey` — p95 latency under 500ms for top 10 endpoints
- **PERF02**: `EXPLAIN ANALYZE` on top 20 queries, all under 100ms
- **PERF03**: Measure from `uvicorn` start to `/health` returning 200
- **PERF04**: Railway metrics dashboard or `railway metrics` CLI shows < 512MB
- **PERF05**: Enable query logging, scan for repeated single-row fetches in request handlers
- **PERF06**: `asyncpg` pool stats: `pool.get_size()` / `pool.get_max_size()` < 0.80
- **PERF07**: `/health` endpoint responds in < 50ms (local) or < 200ms (Railway network)

## Benchmark Baselines

| Endpoint | p50 | p95 | p99 | Method |
|----------|-----|-----|-----|--------|
| /health | 5ms | 15ms | 50ms | GET |
| /api/v1/search | 100ms | 300ms | 500ms | POST |
| /api/v1/create | 50ms | 150ms | 300ms | POST |
| /pipeline/health | 10ms | 30ms | 100ms | GET |

## Scoring Formula

`performance_score = (SP01 * 0.25) + (SP02 * 0.20) + (SP03 * 0.20) + (SP04 * 0.20) + (SP05 * 0.15)`

Pass condition: all hard gates pass AND `performance_score >= 0.85`

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Performance exemplar — publish baselines |
| >= 8.0 | PUBLISH | Ready for production |
| >= 7.0 | REVIEW | Performance optimization recommended |
| < 7.0  | REJECT | Performance rework required |

## Boundary

Barreira de qualidade com score numerico. NAO eh validator (P06, tecnico pass/fail) nem scoring_rubric (P07, define criterios).


## 8F Pipeline Function

Primary function: **GOVERN**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_benchmark_api_latency]] | upstream | 0.36 |
| [[p11_qg_railway_superintendent]] | sibling | 0.34 |
| [[p11_qg_artifact]] | sibling | 0.32 |
| [[p11_qg_security]] | sibling | 0.30 |
| [[p07_regcheck_latency_baseline]] | upstream | 0.28 |
| [[p02_agent_railway_superintendent]] | upstream | 0.26 |
| [[p08_ac_railway_superintendent]] | upstream | 0.25 |
| [[p01_kc_api_health_monitoring]] | upstream | 0.24 |
| [[p03_sp_railway_superintendent]] | upstream | 0.24 |
| [[p06_schema_health_response]] | upstream | 0.24 |
