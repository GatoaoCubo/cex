---
kind: learning_record
id: p10_lr_llm_evaluation_scenario_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for llm_evaluation_scenario construction
quality: 8.7
title: "Learning Record LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, learning_record, helm]
tldr: "Learned patterns and pitfalls for llm_evaluation_scenario construction"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_llm_evaluation_scenario_builder
  - llm-evaluation-scenario-builder
  - bld_knowledge_card_llm_evaluation_scenario
  - p07_qg_llm_evaluation_scenario
  - bld_instruction_llm_evaluation_scenario
  - bld_examples_llm_evaluation_scenario
  - bld_schema_llm_evaluation_scenario
  - bld_collaboration_llm_evaluation_scenario
  - kc_llm_evaluation_scenario
  - bld_tools_llm_evaluation_scenario
---

## Observation
HELM scenarios that omit explicit canonicalization rules produce irreproducible results across different runners. The most common failure: open-ended generation tasks without stop_sequences, where model completion bleeds into the next few-shot prompt, corrupting the evaluation context.

## Pattern
Define canonicalization as a named function (not inline lambda) before writing the scenario body. Validate the function independently with 10 sample outputs before committing the scenario. For MCQ: letter extraction + uppercase. For generation: markdown fence stripping + whitespace normalization. For code: execution sandbox spec + pass@k harness reference.

## Evidence
IBM Enterprise HELM audit (2024): 23% of submitted scenarios failed reproducibility checks due to missing or ambiguous canonicalization. Scenarios with named canonicalization functions had 0% reproducibility failures.

## Recommendations
- Define canonicalization_fn before writing task instances (not after).
- Pin dataset splits with SHA256 hash to prevent data drift between evaluation runs.
- Use num_train_trials >= 3 for statistical confidence in few-shot variance estimates.
- Validate few_shot_pool size is >= 3x num_few_shot before publishing.
- Document token cost estimate in the scenario -- prevents budget surprises in grid runs.
- Register every new scenario in `.cex/registry/helm_scenarios.yaml` on F8 completion.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_llm_evaluation_scenario_builder]] | upstream | 0.39 |
| [[llm-evaluation-scenario-builder]] | upstream | 0.37 |
| [[bld_knowledge_card_llm_evaluation_scenario]] | upstream | 0.32 |
| [[p07_qg_llm_evaluation_scenario]] | downstream | 0.29 |
| [[bld_instruction_llm_evaluation_scenario]] | upstream | 0.29 |
| [[bld_examples_llm_evaluation_scenario]] | upstream | 0.27 |
| [[bld_schema_llm_evaluation_scenario]] | upstream | 0.25 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.25 |
| [[kc_llm_evaluation_scenario]] | upstream | 0.25 |
| [[bld_tools_llm_evaluation_scenario]] | upstream | 0.24 |
