---
kind: architecture
id: bld_architecture_unit_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of unit_eval — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Unit Eval"
version: "1.0.0"
author: n03_builder
tags: [unit_eval, builder, examples]
tldr: "Golden and anti-examples for unit eval construction, demonstrating ideal structure and common pitfalls."
domain: "unit eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - unit-eval-builder
  - p01_kc_unit_eval
  - bld_knowledge_card_unit_eval
  - golden-test-builder
  - bld_architecture_golden_test
  - p03_sp_unit-eval-builder
  - p03_ins_unit_eval
  - p03_sp_e2e_eval_builder
  - p01_kc_e2e_eval
  - bld_memory_unit_eval
---

# Architecture: unit_eval in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target, assertion_count, etc.) | unit-eval-builder | active |
| test_input | Concrete input provided to the target agent or prompt | author | active |
| expected_output | The correct output that the target should produce | author | active |
| assertions | Specific conditions that must hold true for the test to pass | author | active |
| setup_teardown | Pre-test initialization and post-test cleanup procedures | author | active |
| coverage_mapping | Which capabilities or code paths this test exercises | author | active |
## Dependency Graph
```
target_agent    --tested_by-->   unit_eval  --produces-->    test_result
golden_test     --calibrates-->  unit_eval  --signals-->     eval_event
unit_eval       --depends-->     quality_gate
```
| From | To | Type | Data |
|------|----|------|------|
| target_agent/prompt | unit_eval | data_flow | target under test provides actual output |
| unit_eval | test_result | produces | pass/fail per assertion with details |
| golden_test (P07) | unit_eval | dependency | golden tests provide reference for expected output |
| unit_eval | eval_event (P12) | signals | emitted on test pass or fail |
| quality_gate (P11) | unit_eval | dependency | gate may require unit eval pass before promotion |
| scoring_rubric (P07) | unit_eval | dependency | rubric criteria may inform assertion design |
## Boundary Table
| unit_eval IS | unit_eval IS NOT |
|--------------|-----------------|
| A test of one agent or prompt in isolation with concrete I/O | A fast sanity check (< 30s) for basic health (smoke_eval P07) |
| Has explicit input, expected output, and assertions | A full pipeline test across multiple agents (e2e_eval P07) |
| Includes setup/teardown for test isolation | A reference example of ideal output (golden_test P07) |
| Maps coverage to specific capabilities or code paths | A performance measurement (benchmark P07) |
| Produces per-assertion pass/fail results | A weighted score across dimensions (scoring_rubric P07) |
| Regression-focused: catches breakage in existing behavior | A calibration tool for scoring consistency |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Setup | setup_teardown, golden_test | Initialize test environment and load reference data |
| Input | frontmatter, test_input | Define test identity and concrete input |
| Execution | target_agent/prompt | Run the target with test input |
| Verification | expected_output, assertions, coverage_mapping | Compare actual vs expected and check assertions |
| Output | test_result, eval_event | Report results and signal downstream |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[unit-eval-builder]] | upstream | 0.48 |
| [[p01_kc_unit_eval]] | upstream | 0.45 |
| [[bld_knowledge_card_unit_eval]] | upstream | 0.45 |
| [[golden-test-builder]] | upstream | 0.40 |
| [[bld_architecture_golden_test]] | sibling | 0.40 |
| [[p03_sp_unit-eval-builder]] | upstream | 0.39 |
| [[p03_ins_unit_eval]] | upstream | 0.38 |
| [[p03_sp_e2e_eval_builder]] | upstream | 0.35 |
| [[p01_kc_e2e_eval]] | upstream | 0.35 |
| [[bld_memory_unit_eval]] | downstream | 0.33 |
