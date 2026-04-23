---
kind: architecture
id: bld_architecture_golden_test
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of golden_test — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - golden-test-builder
  - p01_kc_golden_test
  - bld_architecture_unit_eval
  - p11_qg_golden_test
  - p03_sp_golden_test_builder
  - bld_collaboration_golden_test
  - bld_architecture_scoring_rubric
  - bld_output_template_golden_test
  - bld_instruction_golden_test
  - p10_lr_golden_test_builder
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| target_kind | The artifact type this golden test calibrates (e.g., knowledge_card, formatter) | golden_test | required |
| input | The exact task request used to produce the reference artifact | golden_test | required |
| output | The reference artifact itself; must score >= 9.5 on all quality gates | golden_test | required |
| rationale | Mapping of output qualities to specific gate criteria; explains WHY it is golden | golden_test | required |
| quality_score | Verified score (>= 9.5); assigned after independent review, not self-assessed | golden_test | required |
| gate_mapping | List of quality gates from the target_kind that this test anchors | golden_test | required |
| reviewer | Identity of the independent evaluator who confirmed the score | golden_test | required |
| created_date | Date the golden test was certified; used for staleness checks | golden_test | required |
## Dependency Graph
```
scoring_rubric (P07) --produces--> golden_test
quality_gate (P11)   --depends-->  golden_test
golden_test          --produces--> unit_eval (P07)
golden_test          --produces--> benchmark (P07)
few_shot_example (P01) --depends--> golden_test
```
| From | To | Type | Data |
|------|----|------|------|
| scoring_rubric (P07) | golden_test | produces | evaluation dimensions and criteria the output must satisfy |
| quality_gate (P11) | golden_test | depends | pass/fail thresholds used to verify the 9.5+ score |
| golden_test | unit_eval (P07) | produces | ground-truth reference for test case comparison |
| golden_test | benchmark (P07) | produces | quality anchor for performance measurement baselines |
| few_shot_example (P01) | golden_test | depends | exemplary input/output pairs that may become golden candidates |
## Boundary Table
| golden_test IS | golden_test IS NOT |
|----------------|-------------------|
| A reference artifact certified at quality >= 9.5 | A test at any quality level (that is unit_eval) |
| A calibration anchor — defines what "perfect" looks like | A quick sanity check for system health (that is smoke_eval) |
| Independently reviewed; score is externally verified | A scoring rubric that defines evaluation criteria |
| Specific to one artifact type (target_kind) | An end-to-end pipeline test spanning multiple artifacts |
| A ground-truth source consumed by unit_eval and benchmark | A few-shot example used to teach format (not to measure quality) |
| Immutable once certified; changes require re-certification | A live metric updated continuously during operation |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Criteria | scoring_rubric (P07), quality_gate (P11) | Define evaluation dimensions and pass/fail thresholds |
| Certification | quality_score, reviewer, created_date | Record the verified 9.5+ score and its provenance |
| Content | input, output, target_kind | The reference artifact and the task that produced it |
| Rationale | rationale, gate_mapping | Explain which gates are satisfied and why the output qualifies |
| Consumers | unit_eval (P07), benchmark (P07) | Use the golden test as a quality calibration reference |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[golden-test-builder]] | upstream | 0.57 |
| [[p01_kc_golden_test]] | upstream | 0.47 |
| [[bld_architecture_unit_eval]] | sibling | 0.44 |
| [[p11_qg_golden_test]] | downstream | 0.43 |
| [[p03_sp_golden_test_builder]] | upstream | 0.40 |
| [[bld_collaboration_golden_test]] | downstream | 0.36 |
| [[bld_architecture_scoring_rubric]] | sibling | 0.35 |
| [[bld_output_template_golden_test]] | upstream | 0.34 |
| [[bld_instruction_golden_test]] | upstream | 0.32 |
| [[p10_lr_golden_test_builder]] | downstream | 0.30 |
