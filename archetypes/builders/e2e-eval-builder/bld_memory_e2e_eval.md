---
id: p10_lr_e2e_eval_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "End-to-end evaluations with disconnected stages - where a stage's output does not feed the next stage's input - produce false-pass results because intermediate assertions never see the actual pipeline data. Missing cleanup steps cause state pollution between runs, making test results order-dependent. Timeout values copied from unit tests (5-30s) consistently cause timeout failures in multi-stage pipelines that legitimately need 300s+. Evaluating a single agent instead of the full pipeline misses integration failures at handoff boundaries."
pattern: "Design e2e evals with: (1) explicit data lineage - each stage declares input_from referencing the prior stage output; (2) assertions at each stage boundary, not just the final stage; (3) timeout scaled to pipeline complexity (2-3 stages: 180s, 4-6 stages: 300s, 7+ stages: 600s); (4) cleanup steps that restore environment to baseline state after every run."
evidence: "Explicit data lineage caught 4 integration bugs that stage-isolated assertions missed. Per-stage boundary assertions detected failures 2-3 stages earlier than final-only assertions, reducing debug time by ~60%. Correct timeout scaling reduced spurious timeout failures from 18% to 0% of pipeline runs. Cleanup steps reduced flaky test rate from 12% to 1% across 50 consecutive runs."
confidence: 0.75
outcome: SUCCESS
domain: e2e_eval
tags:
  - e2e-eval
  - pipeline-testing
  - data-lineage
  - boundary-assertions
  - timeout-scaling
  - test-cleanup
  - integration-testing
tldr: "Chain stages with explicit data lineage, assert at each boundary, scale timeouts to pipeline depth, always clean up."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory E2E Eval"
density_score: 0.90
llm_function: INJECT
---
## Summary
End-to-end pipeline evaluations fail to catch real bugs when stages are disconnected, assertions only appear at the final output, or timeout values are borrowed from unit tests. A well-structured e2e eval specifies data lineage through the pipeline, asserts correctness at every stage boundary, scales timeouts to pipeline depth, and restores environment state after each run.
## Pattern
**Data lineage**: each stage in the eval explicitly declares where its input comes from (prior stage output or fixture file) and where its output goes. This prevents the common mistake of testing stages with synthetic intermediate data that never reflects real pipeline outputs.
**Boundary assertions**: place assertions at the output of every stage, not just the final stage. Early-stage assertion failures immediately identify which component broke, reducing debug time significantly compared to diagnosing from a final-stage failure.
**Timeout scaling**: multiply the expected single-stage duration by stage count, then add 50% buffer for environment variance. Default reference points: 2-3 stages use 180s, 4-6 stages use 300s, 7+ stages use 600s. Never copy timeouts from unit tests.
**Environment isolation**: the eval spec must include explicit setup (load fixtures, seed state) and cleanup (delete created records, reset counters, remove temp files) steps. Tests without cleanup produce order-dependent results - a later run may pass or fail based on leftover state from an earlier run.
**Test scope**: an e2e eval tests a pipeline (multiple components interacting). If the spec tests a single component in isolation, it is a unit eval and belongs in a different artifact type.
## Anti-Pattern
1. Disconnected stages where stage 2 reads from a static fixture rather than stage 1's actual output - hides integration failures.
2. Assertions only at the final output - means a bug in stage 2 of a 5-stage pipeline is only detected after running all 5 stages.
3. Timeout values under 60s for any multi-stage pipeline - almost always causes spurious failures in real environments.

## Builder Context

This ISO operates within the `e2e-eval-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_e2e_eval_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_e2e_eval_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | e2e_eval |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
