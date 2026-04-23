---
kind: architecture
id: bld_architecture_llm_judge
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of llm_judge — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Llm Judge"
version: "1.0.0"
author: n03_builder
tags: [llm_judge, builder, examples]
tldr: "Golden and anti-examples for llm judge construction, demonstrating ideal structure and common pitfalls."
domain: "llm judge construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_llm_judge_builder
  - bld_collaboration_llm_judge
  - llm-judge-builder
  - p11_qg_llm_judge
  - p01_kc_llm_judge
  - bld_output_template_llm_judge
  - bld_instruction_llm_judge
  - bld_schema_llm_judge
  - bld_knowledge_card_llm_judge
  - bld_examples_llm_judge
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| judge_model | LLM that performs evaluation — receives prompt+response, returns score | llm_judge | required |
| criterion | Named quality dimension the judge evaluates (e.g. faithfulness, coherence) | llm_judge | required |
| scale | Scoring range with semantic anchor labels (min, max, anchors) | llm_judge | required |
| few_shot | Calibration examples that reduce judge variance and bias | llm_judge | required |
| judge_prompt | Templated instruction combining criteria, scale, and few_shot into judge input | llm_judge | derived |
| chain_of_thought | Flag requiring judge to reason before scoring (reduces position bias) | llm_judge | optional |
| aggregation | Method for combining scores across multiple criteria (mean, min, weighted_sum) | llm_judge | optional |
| pass_threshold | Score floor for downstream binary pass/fail decisions | llm_judge | optional |
| evaluated_output | The model response being scored (external, not owned by judge) | consumer | external |
| reference | Ground truth or ideal response for reference-based evaluation | consumer | external |
| framework | Eval framework that executes the judge (Braintrust, DeepEval, RAGAS, etc.) | P07 | external |
| quality_gate | Downstream artifact (P11) that reads judge score and blocks/passes pipeline | P11 | consumer |
| dataset | Eval corpus that supplies (input, output) pairs to the judge | P07 | consumer |

## Dependency Graph
```
reference        --provides-->  judge_prompt
evaluated_output --provides-->  judge_prompt
criterion        --shapes-->    judge_prompt
scale            --shapes-->    judge_prompt
few_shot         --calibrates-> judge_model
chain_of_thought --modifies-->  judge_model
judge_model      --produces-->  score
judge_model      --produces-->  rationale
aggregation      --depends-->   score (multi-criteria)
pass_threshold   --depends-->   score
quality_gate     --depends-->   score
framework        --executes-->  judge_model
```

## Boundary Table
| llm_judge IS | llm_judge IS NOT |
|-------------|-----------------|
| A judge configuration: model + criteria + scale + few_shot | A scoring rubric without a model (that is scoring_rubric) |
| Produces a numeric score on a declared scale | A pipeline blocker (that is quality_gate P11) |
| Evaluates ONE response per invocation | A benchmark comparing systems across datasets |
| Requires judge_model to be specified | A formula-based metric without LLM (that is metric) |
| Calibrated via few_shot examples | An eval dataset/corpus (that is dataset) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | judge_model, scale, chain_of_thought, temperature | Define who judges and how |
| criteria | criterion list | Define what dimensions are evaluated |
| calibration | few_shot, aggregation, pass_threshold | Reduce variance, enable downstream decisions |
| execution | framework, judge_prompt | Runtime integration and invocation |
| governance | quality_gate (P11) | Consumes judge score to block/pass pipeline |
| inputs | evaluated_output, reference, dataset | Supply what gets judged |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_llm_judge_builder]] | upstream | 0.59 |
| [[bld_collaboration_llm_judge]] | downstream | 0.59 |
| [[llm-judge-builder]] | upstream | 0.57 |
| [[p11_qg_llm_judge]] | downstream | 0.52 |
| [[p01_kc_llm_judge]] | upstream | 0.51 |
| [[bld_output_template_llm_judge]] | upstream | 0.50 |
| [[bld_instruction_llm_judge]] | upstream | 0.49 |
| [[bld_schema_llm_judge]] | upstream | 0.46 |
| [[bld_knowledge_card_llm_judge]] | upstream | 0.43 |
| [[bld_examples_llm_judge]] | upstream | 0.37 |
