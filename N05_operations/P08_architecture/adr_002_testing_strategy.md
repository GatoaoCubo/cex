---
id: p08_adr_002_testing_strategy
kind: context_doc
pillar: P08
title: "ADR-002: CEX Testing Strategy"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: architecture-operations
quality: 9.0
tags: [context_doc, architecture, operations, N05, testing, strategy, ADR]
tldr: "Architecture decision record for the multi-layer testing strategy covering unit, e2e, smoke, regression, benchmark, golden, and red-team evaluations."
density_score: 0.96
---

# ADR-002: CEX Testing Strategy

## Status

**Accepted** — 2026-04-07

## Context

CEX has 59 tools, 125 builders, 123 kinds, and a complex multi-nucleus
architecture. Testing must cover tool correctness, artifact quality,
pipeline integrity, and deployment safety. A single test layer is
insufficient.

## Decision

Adopt a 7-layer testing pyramid owned by N05:

```
        /  Red-Team  \          ← adversarial security testing
       / E2E + Smoke  \         ← integration + deploy verification
      /   Regression    \        ← baseline comparison
     /   Golden Tests    \       ← canonical correct outputs
    /   Benchmarks        \      ← performance measurement
   /    Unit Evals         \     ← individual tool/function tests
  ━━━━━━━━━━━━━━━━━━━━━━━━━━
      Static Analysis          ← pre-commit hooks + lint
```

### Layer Responsibilities

| layer | tool | frequency | gate_type |
|-------|------|-----------|-----------|
| Static Analysis | `cex_hooks.py`, `cex_sanitize.py` | Every commit | blocking |
| Unit Evals | `cex_system_test.py` (54 tests) | Every PR | blocking |
| Benchmarks | `benchmark_api_latency.md` suite | Pre-deploy | warning |
| Golden Tests | Per-builder golden outputs | Every PR | blocking |
| Regression | `cex_quality_monitor.py --compare` | Every PR | blocking |
| E2E + Smoke | `smoke_eval_deploy.md` suite | Post-deploy | blocking (rollback) |
| Red-Team | `red_team_eval_operations.md` suite | Monthly + pre-release | blocking |

## Consequences

### Positive

- **Defense in depth**: Multiple layers catch different categories of defects
- **Fast feedback**: Static analysis and unit tests run in seconds
- **Regression confidence**: Baselines detect quality drift before users do
- **Security assurance**: Red-team evals prove adversarial resilience
- **Deploy safety**: Smoke evals catch production-specific failures

### Negative

- **Maintenance cost**: 7 test layers require ongoing maintenance
- **Baseline management**: Golden tests and baselines need updating on intentional changes
- **Execution time**: Full pyramid takes 5-10 minutes (static + unit + regression + benchmark)

### Operational Rules

1. No PR merges without static analysis + unit evals + regression green
2. No deploy without smoke eval passing within 30s budget
3. Red-team eval required before any public-facing release
4. Benchmark baselines updated quarterly or after architecture changes
5. Golden test updates require explicit justification in PR description
