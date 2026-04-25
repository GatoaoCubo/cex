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
tldr: "N03 baselines (2026-03-30): Motor 99/99 resolution + 26/26 tests, Doctor 86 PASS / 12 WARN / 0 FAIL, pipeline dry-run <30ms, 232 compiled artifacts, 0 proprietary refs. Any regression blocks merge."
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

```bash
# Full benchmark suite (runs all checks)
python _tools/cex_8f_motor.py --test          # Motor resolution: expect 99/99
python _tools/cex_doctor.py                   # Builder health: expect 0 FAIL
python _tools/cex_8f_runner.py --dry-run --kind agent  # Pipeline latency: expect <50ms
python _tools/cex_kind_register.py --validate # Registry sync: expect all in sync
python _tools/cex_sanitize.py --check --scope N03_engineering/  # ASCII compliance

# Quick smoke test (30 seconds)
python _tools/cex_8f_motor.py --test && python _tools/cex_doctor.py --quick
```

## Regression Policy

Any commit that reduces Motor resolution below 99/99 or introduces doctor FAILs
must be reverted or fixed before merge. Benchmarks are checked in CI.

## Benchmark Evolution

| Date | Motor | Doctor | Compiled | Change Trigger |
|------|-------|--------|----------|---------------|
| 2026-03-30 | 99/99 | 86 PASS | 232 | Genesis session |
| 2026-04-07 | 99/99 | 118 PASS | 259 | WAVE3 builder expansion |
| 2026-04-13 | 99/99 | 259 PASS | 3647 ISOs | ISO validation sweep |
| 2026-04-25 | 300/300 | 300 PASS | 3647 ISOs | Full 300-kind coverage |

Note: Kind count grew from 99 to 300 since genesis. Benchmarks above track the
latest snapshot -- earlier baselines are superseded but preserved in git history.

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
