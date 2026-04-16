---
kind: instruction
id: bld_instruction_llm_evaluation_scenario
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for llm_evaluation_scenario
quality: 8.9
title: "Instruction LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, instruction, helm]
tldr: "Step-by-step production process for llm_evaluation_scenario"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Identify the capability under evaluation (e.g., commonsense reasoning, medical QA, code generation).
2. Map capability to HELM subject_area taxonomy (knowledge, reasoning, language, code, safety).
3. Survey existing HELM scenarios at `crfm.stanford.edu/helm/latest/` to avoid duplication.
4. Identify eval_dataset sources: source corpus, license, task format (MCQ, open-ended, classification).
5. Determine baseline adapter: instruction-following vs. few-shot, context window budget.
6. Audit IBM Enterprise HELM extensions if domain is finance/legal/climate/cybersecurity.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (scenario_id, subject_area, capability, task_instances).
2. Define task_instance schema: input format, expected output format, answer key.
3. Specify few_shot_pool: number of demonstrations (0, 1, 3, 5, 10), selection strategy (random, stratified).
4. Configure adapter parameters: prompt_template reference, max_tokens, stop_sequences, temperature.
5. Map primary metric: accuracy, F1, ROUGE, BLEU, exact_match, calibration_error, efficiency.
6. Define canonicalization rules: normalization function, case sensitivity, punctuation stripping, alias expansion.
7. Add subject_area and capability tags for HELM leaderboard indexing.
8. Estimate token cost per scenario run: num_instances * (prompt_tokens + completion_tokens).
9. Proofread for schema compliance and HELM naming conventions.

## Phase 3: VALIDATE
- [ ] scenario_id follows pattern `p07_evs_[subject]_[capability].md`
- [ ] subject_area maps to recognized HELM taxonomy (or IBM extension)
- [ ] capability is specific and testable, not a vague category
- [ ] task_instance format is consistent (all MCQ, all open-ended, not mixed)
- [ ] few_shot_pool size >= max few-shot trials configured in adapter
- [ ] canonicalization rules produce deterministic output (no randomness)
- [ ] metric mapped to HELM metric family with correct aggregation function
- [ ] token budget estimate documented and within model limits
