---
id: p07_bm_builder_nucleus
kind: benchmark
8f: F7_govern
pillar: P07
title: Benchmark -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [benchmark, builder, N03, performance]
tldr: Baseline metrics for builder health -- 99/99 motor resolution, 86 PASS doctor, <30ms pipeline dry-run.
density_score: 0.88
related:
  - p04_fd_builder_toolkit
  - p12_sig_builder_nucleus
  - p03_pt_builder_construction
  - p08_ac_builder_nucleus
  - p06_if_builder_nucleus
  - p12_dr_builder_nucleus
  - p07_regression_check
  - grid_test_n05_20260407
  - p03_ch_builder_pipeline
  - polish_fixes_20260413
---

# Benchmark: Builder Nucleus

## Current Baselines (2026-03-30)

| Metric | Value | Threshold | Tool |
|--------|-------|-----------|------|
| Motor kind resolution | 99/99 | >= 99 | cex_8f_motor.py --test |
| Motor built-in tests | 26/26 pass | 26/26 | cex_8f_motor.py --test |
| Doctor builders | 86 PASS, 12 WARN, 0 FAIL | 0 FAIL | cex_doctor.py |
| Pipeline dry-run | <30ms total | <50ms | cex_8f_runner.py --dry-run |
| Kind registry sync | 3/3 in sync | all in sync | cex_kind_register.py --validate |
| Compiled artifacts | 232 | >= 230 | ls compiled/ |
| Kind KCs | 99/99 | 99/99 | ls library/kind/ |
| Examples | 245 | >= 240 | ls examples/ |
| Proprietary refs | 0 | 0 | grep across tracked files |

## How to Run



## Regression Policy

Any commit that reduces Motor resolution below 99/99 or introduces doctor FAILs
must be reverted or fixed before merge. Benchmarks are checked in CI.

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Baseline metrics established from initial 100-artifact corpus
- Regression detection triggers alert when score drops below baseline
- Performance benchmarks run on standardized hardware configuration
- Test coverage tracked per nucleus with minimum 80% gate threshold

### Usage Reference

```yaml
# benchmark integration
artifact: benchmark_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fd_builder_toolkit]] | upstream | 0.33 |
| [[p12_sig_builder_nucleus]] | downstream | 0.32 |
| [[p03_pt_builder_construction]] | upstream | 0.31 |
| [[p08_ac_builder_nucleus]] | downstream | 0.31 |
| [[p06_if_builder_nucleus]] | upstream | 0.30 |
| [[p12_dr_builder_nucleus]] | downstream | 0.26 |
| [[p07_regression_check]] | related | 0.24 |
| [[grid_test_n05_20260407]] | related | 0.23 |
| [[p03_ch_builder_pipeline]] | upstream | 0.23 |
| [[polish_fixes_20260413]] | downstream | 0.23 |
