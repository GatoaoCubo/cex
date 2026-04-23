---
kind: architecture
id: bld_architecture_e2e_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of e2e_eval — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture E2E Eval"
version: "1.0.0"
author: n03_builder
tags: [e2e_eval, builder, examples]
tldr: "Golden and anti-examples for e2e eval construction, demonstrating ideal structure and common pitfalls."
domain: "e2e eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - e2e-eval-builder
  - p01_kc_e2e_eval
  - p03_sp_e2e_eval_builder
  - bld_collaboration_e2e_eval
  - p10_lr_e2e_eval_builder
  - bld_instruction_e2e_eval
  - p11_qg_e2e_eval
  - bld_output_template_e2e_eval
  - bld_collaboration_smoke_eval
  - bld_collaboration_unit_eval
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| pipeline_under_test | Reference to the workflow or agent chain being tested | e2e-eval-builder | required |
| stages | Ordered list of pipeline steps with agent/tool, input, and expected output | e2e-eval-builder | required |
| data_fixtures | Input datasets and environment state for the test run | e2e-eval-builder | required |
| expected_output | Final output specification: schema, content assertions, quality floor | e2e-eval-builder | required |
| intermediate_assertions | Per-stage output checks before the next stage runs | e2e-eval-builder | required |
| environment | Runtime context: model, temperature, tools enabled, external mocks | e2e-eval-builder | required |
| cleanup | Post-run teardown: reset state, delete temp files, restore mocks | e2e-eval-builder | required |
| pass_criteria | Conditions that constitute a passing run (threshold, all-stages, subset) | e2e-eval-builder | required |
| timeout | Maximum wall-clock time allowed for the full pipeline run | e2e-eval-builder | required |
| metadata | eval id, version, pillar, pipeline_id, author, created date | e2e-eval-builder | required |
## Dependency Graph
```
smoke_eval (P07) --must_pass_before--> e2e_eval (smoke gate must clear first)
unit_eval (P07) --composes_into--> e2e_eval (individual stage tests feed pipeline test)
workflow (P12) --tested_by--> e2e_eval (e2e verifies the workflow's end-to-end correctness)
e2e_eval --produces_for--> quality_gate (P11) (pass/fail result gates pipeline promotion)
e2e_eval --produces_for--> benchmark (P07) (pipeline metrics aggregated from e2e runs)
scoring_rubric (P07) --independent-- e2e_eval (rubric defines criteria; e2e applies verification)
golden_test (P07) --independent-- e2e_eval (golden tests reference single artifacts, e2e tests pipelines)
```
| From | To | Type | Data |
|------|----|------|------|
| smoke_eval | e2e_eval | depends | smoke pass is prerequisite |
| unit_eval | e2e_eval | data_flow | per-stage assertions reuse unit test patterns |
| workflow | e2e_eval | data_flow | pipeline definition drives stage structure |
| e2e_eval | quality_gate | produces | pass/fail verdict for pipeline promotion |
| e2e_eval | benchmark | produces | latency, cost, and accuracy metrics per run |
## Boundary Table
| e2e_eval IS | e2e_eval IS NOT |
|-------------|-----------------|
| An integration test: verifies the full pipeline from input to final output | A unit_eval — unit_eval tests a single agent in isolation |
| Tests multiple agents and tools interacting in sequence | A smoke_eval — smoke_eval does a quick sanity check in under 30 seconds |
| Includes intermediate assertions at each stage boundary | A benchmark — benchmark measures latency and cost, not pipeline correctness |
| Requires data fixtures and environment setup before running | A golden_test — golden_test is a quality reference for a single artifact |
| Produces a pass/fail verdict consumed by quality_gate | A scoring_rubric — rubric defines evaluation criteria, not the test execution |
| Defines cleanup to restore system state after the run | A workflow — workflow defines and executes the pipeline; e2e_eval tests it |
| Has an explicit timeout bounding the full run | A dag — dag models dependency structure, not test verification |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Prerequisites | smoke_eval, unit_eval | Must pass before e2e_eval is meaningful to run |
| Setup | data_fixtures, environment, pipeline_under_test | Prepare inputs, mocks, and runtime context |
| Execution | stages, timeout | Run each pipeline step in order within time bound |
| Verification | intermediate_assertions, expected_output, pass_criteria | Assert correctness at each stage and at final output |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[e2e-eval-builder]] | upstream | 0.62 |
| [[p01_kc_e2e_eval]] | upstream | 0.54 |
| [[p03_sp_e2e_eval_builder]] | upstream | 0.52 |
| [[bld_collaboration_e2e_eval]] | downstream | 0.50 |
| [[p10_lr_e2e_eval_builder]] | downstream | 0.46 |
| [[bld_instruction_e2e_eval]] | upstream | 0.45 |
| [[p11_qg_e2e_eval]] | downstream | 0.45 |
| [[bld_output_template_e2e_eval]] | upstream | 0.43 |
| [[bld_collaboration_smoke_eval]] | upstream | 0.43 |
| [[bld_collaboration_unit_eval]] | upstream | 0.41 |
