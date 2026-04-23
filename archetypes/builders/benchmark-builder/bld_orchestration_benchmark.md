---
kind: collaboration
id: bld_collaboration_benchmark
pillar: P12
llm_function: COLLABORATE
purpose: How benchmark-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Benchmark"
version: "1.0.0"
author: n03_builder
tags: [benchmark, builder, examples]
tldr: "Golden and anti-examples for benchmark construction, demonstrating ideal structure and common pitfalls."
domain: "benchmark construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_golden_test
  - benchmark-builder
  - bld_collaboration_e2e_eval
  - bld_collaboration_builder
  - bld_collaboration_quality_gate
  - bld_collaboration_bugloop
  - bld_collaboration_regression_check
  - bld_collaboration_fallback_chain
  - bld_collaboration_validation_schema
  - bld_collaboration_prompt_version
---

# Collaboration: benchmark-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how fast, how cheap, and how well does this perform under load?"
I do not define quality criteria. I do not test correctness.
I measure performance quantitatively so teams can set baselines and detect regressions.
## Crew Compositions
### Crew: "Quality Pipeline"
```
  1. golden-test-builder -> "reference examples (quality calibration)"
  2. benchmark-builder -> "performance baselines (latency, cost, throughput)"
  3. e2e-eval-builder -> "end-to-end pipeline validation"
```
### Crew: "Performance Optimization"
```
  1. benchmark-builder -> "baseline measurements before optimization"
  2. bugloop-builder -> "detect-fix-verify cycle for performance regressions"
  3. benchmark-builder -> "post-optimization measurements for comparison"
```
## Handoff Protocol
### I Receive
- seeds: target system/agent name, metrics to measure (latency, cost, throughput)
- optional: baseline values, environment constraints, iteration count
### I Produce
- benchmark artifact (.md + .yaml frontmatter)
- committed to: `cex/P07/examples/p07_benchmark_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Benchmarks can be defined for any system.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| bugloop-builder | Uses benchmark thresholds as detection triggers |
| e2e-eval-builder | References benchmark baselines for pass/fail criteria |
| fallback-chain-builder | Uses latency/cost benchmarks to calibrate timeouts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_golden_test]] | sibling | 0.55 |
| [[benchmark-builder]] | upstream | 0.49 |
| [[bld_collaboration_e2e_eval]] | sibling | 0.48 |
| [[bld_collaboration_builder]] | sibling | 0.44 |
| [[bld_collaboration_quality_gate]] | sibling | 0.41 |
| [[bld_collaboration_bugloop]] | sibling | 0.41 |
| [[bld_collaboration_regression_check]] | sibling | 0.38 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.38 |
| [[bld_collaboration_validation_schema]] | sibling | 0.35 |
| [[bld_collaboration_prompt_version]] | sibling | 0.35 |
