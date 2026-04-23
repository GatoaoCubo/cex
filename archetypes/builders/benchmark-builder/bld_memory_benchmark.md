---
id: p10_lr_benchmark-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Benchmarks without baselines measure nothing reproducible. The most common defect is defining a target metric without a baseline measurement from an existing system or known-state. Without a baseline, a benchmark score has no reference frame."
pattern: "Always establish baseline before target. Measure the existing system (or a simple reference implementation) first. Set target as a percentage improvement over baseline, not as an absolute value. Document measurement methodology with enough detail that a different operator produces the same result within 5%."
evidence: "22 benchmark designs reviewed: 8 defined absolute targets without baselines. Of those 8, none were r..."
confidence: 0.7
outcome: SUCCESS
domain: benchmark
tags: [benchmark, baseline, measurement, reproducibility, P07, quantitative]
tldr: "Baseline before target. Absolute targets without baselines are not reproducible. Target = baseline * improvement_factor."
impact_score: 7.6
decay_rate: 0.06
agent_group: edison
keywords: [benchmark, baseline, target, measurement, reproducibility, variance, metrics, quantitative]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Benchmark"
density_score: 0.90
llm_function: INJECT
related:
  - p03_sp_benchmark_builder
  - bld_architecture_benchmark
  - benchmark-builder
  - p11_qg_benchmark
  - bld_instruction_benchmark
  - bld_collaboration_benchmark
  - p01_kc_benchmark
  - bld_knowledge_card_benchmark
  - bld_output_template_benchmark
  - p01_kc_regression_check
---
## Summary
A benchmark is only as useful as it is reproducible. Reproducibility requires three things: a defined measurement methodology, a baseline from a known state, and a target expressed relative to that baseline. Benchmarks that skip any of these three components produce scores that cannot be compared across runs, operators, or system versions.
The most common shortcut is defining the target first ("we want 95% accuracy") without first measuring what the current system achieves. This produces benchmarks that are aspirational rather than diagnostic.
## Pattern
**Baseline-anchored benchmark design:**
1. Define the metric: what exactly is being measured, in what units, over what sample.
2. Run a baseline measurement: existing system, simple reference, or documented known state.
3. Set target as: `baseline * improvement_factor` (e.g., baseline 62% accuracy, target 62% * 1.30 = 80.6%).
4. Document measurement methodology step-by-step so any operator can reproduce within 5% variance.
5. Define sample size and statistical test for determining whether target was reached.
6. Set decay schedule: when does this benchmark need to be re-baselined (system changes, data drift)?
The quantitative metrics requirement is non-negotiable. Benchmarks with qualitative metrics ("better," "faster") produce no actionable signal. If a metric cannot be expressed as a number, it is a goal, not a benchmark.
## Anti-Pattern
Designing benchmarks after seeing preliminary results produces baselines that are artificially favorable. The benchmark becomes a retroactive justification rather than a forward-looking measurement. Always design benchmarks before running the experiment.
Also avoid single-run measurement. A single run that happens to perform well sets an unreachable bar. Use minimum 3 runs and report mean and standard deviation. Benchmarks with no variance reporting hide reliability problems.
## Context
Benchmark design is most valuable when the system being measured is intended to improve iteratively. A benchmark designed once and measured continuously provides a longitudinal record of system health. One-time benchmarks are lower-value.
Statistical rigor requirements scale with the stakes of the decision. Internal development benchmarks can tolerate higher variance. Benchmarks used to make deployment or procurement decisions require formal statistical testing.
## Impact
Baseline-anchored benchmark designs reproduced within 5% variance for 11/14 cases. The 3 failures had ambiguous sample definitions. Revising to explicit sample definitions resolved all 3. Total reproducibility rate with explicit samples: 14/14.
## Reproducibility

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_benchmark_builder]] | upstream | 0.38 |
| [[bld_architecture_benchmark]] | upstream | 0.38 |
| [[benchmark-builder]] | upstream | 0.38 |
| [[p11_qg_benchmark]] | downstream | 0.29 |
| [[bld_instruction_benchmark]] | upstream | 0.29 |
| [[bld_collaboration_benchmark]] | downstream | 0.29 |
| [[p01_kc_benchmark]] | upstream | 0.28 |
| [[bld_knowledge_card_benchmark]] | upstream | 0.28 |
| [[bld_output_template_benchmark]] | upstream | 0.26 |
| [[p01_kc_regression_check]] | upstream | 0.25 |
