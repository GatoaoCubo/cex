---
id: p07_bm_ops_pipeline
kind: benchmark
pillar: P07
title: "Benchmark: CEX Operations Pipeline"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
metric: "pipeline_latency"
unit: "s"
direction: "lower_is_better"
baseline: 2.0
target: 1.0
iterations: 20
warmup: 3
percentiles: [50, 95, 99]
environment: "Windows 11 Pro 10.0.26200, Python 3.12, bash via Git-for-Windows, Claude Max Opus"
domain: "operations_pipeline"
quality: 9.1
tags: [benchmark, latency, operations, compile, dispatch, signal, pipeline, P07]
tldr: "Ops pipeline benchmark: compile_single <2s, compile_all <60s, doctor <30s, signal_write <0.1s, dispatch_solo <10s, dispatch_grid <30s"
comparison_subjects: [baseline_target, degraded_threshold]
statistical_test: "median + p95 wall-clock"
confidence_interval: 0.95
density_score: 0.91
linked_artifacts:
  primary: "N05_operations/P07_evals/p07_e2e_n05.md"
  related:
    - "N05_operations/P07_evals/p07_efw_n05_operations.md"
    - "N00_genesis/P07_evals/_schema.yaml"
related:
  - bld_knowledge_card_benchmark
  - p02_agent_admin_orchestrator
  - bld_instruction_benchmark
  - p12_wf_auto_health
  - p12_wf_admin_orchestration
  - dispatch
  - p08_ac_orchestrator
  - p01_kc_orchestration
  - p01_kc_orchestration_best_practices
  - p03_sp_admin_orchestrator
---

## Benchmark Overview

Measures wall-clock latency for the six core CEX operations pipeline operations.
Each case maps to a routine N05 workflow: artifact compilation, health check,
inter-nucleus signaling, and nucleus dispatch (solo and grid).

Business impact: degradation in any of these directly increases feedback-loop
latency. compile_single drives the inner edit-compile-verify loop. dispatch_grid
determines how fast a 6-nucleus mission can start.

Three tiers define operational health per case:
- **baseline**: acceptable normal operating condition
- **acceptable**: tolerable; investigate if sustained
- **degraded**: block dispatch; trigger ops alert

## Methodology

- **Iterations**: 20 runs per case (cold-ish: new Python process per run)
- **Warmup**: 3 runs discarded before measurement window opens
- **Protocol**:
  1. Reset state: remove `.cex/runtime/signals/test_*.json` before each run
  2. Time each operation with `time` (bash wall-clock) or `Measure-Command` (PS fallback)
  3. Record p50, p95, p99 across 20 measured runs
  4. Compare p50 to baseline; compare p95 to acceptable threshold
- **Statistical test**: median (p50) as primary; p95 as tail indicator
- **Outlier handling**: retain all runs; p99 captures tail without discarding

## Metrics

| Case ID | Operation | Unit | Direction | Baseline | Acceptable | Degraded |
|---------|-----------|------|-----------|----------|------------|----------|
| compile_single | `cex_compile.py {file}` (1 artifact) | s | lower_is_better | 2 | 5 | >5 |
| compile_all | `cex_compile.py --all` (full repo) | s | lower_is_better | 60 | 120 | >120 |
| doctor_full | `cex_doctor.py` (full health check) | s | lower_is_better | 30 | 60 | >60 |
| signal_write | `write_signal()` call to file on disk | ms | lower_is_better | 100 | 500 | >500 |
| dispatch_solo | `dispatch.sh solo n05 task` to nucleus boot | s | lower_is_better | 10 | 30 | >30 |
| dispatch_grid | `dispatch.sh grid MISSION` (6 nuclei up) | s | lower_is_better | 30 | 60 | >60 |

## Environment

- **Hardware**: Win11 local dev machine (RTX 5070 Ti, NVMe SSD)
- **Software**: Python 3.12, bash via Git-for-Windows 2.44, claude opus-4-6
- **Config**: CEX repo on local NVMe; no network calls for compile/doctor/signal cases;
  dispatch cases require Claude Max auth (network latency included)
- **Date**: 2026-04-17

## Results Template

| Case | p50 | p95 | p99 | Status |
|------|-----|-----|-----|--------|
| compile_single | — | — | — | — |
| compile_all | — | — | — | — |
| doctor_full | — | — | — | — |
| signal_write (ms) | — | — | — | — |
| dispatch_solo | — | — | — | — |
| dispatch_grid | — | — | — | — |

Status key: `[OK]` = p50 <= baseline | `[WARN]` = p50 <= acceptable | `[FAIL]` = p50 > acceptable

## References

- `_tools/cex_compile.py` -- artifact compiler (md -> yaml)
- `_tools/cex_doctor.py` -- builder health check
- `_tools/signal_writer.py` -- inter-nucleus signal writer
- `_spawn/dispatch.sh` -- nucleus dispatch entry point
- `N05_operations/P07_evals/p07_e2e_n05.md` -- end-to-end test suite

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_benchmark]] | upstream | 0.30 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.30 |
| [[bld_instruction_benchmark]] | upstream | 0.29 |
| [[p12_wf_auto_health]] | downstream | 0.28 |
| [[p12_wf_admin_orchestration]] | downstream | 0.28 |
| [[dispatch]] | downstream | 0.28 |
| [[p08_ac_orchestrator]] | downstream | 0.28 |
| [[p01_kc_orchestration]] | upstream | 0.27 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.27 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.27 |
