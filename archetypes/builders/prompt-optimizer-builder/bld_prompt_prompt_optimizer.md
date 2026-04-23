---
kind: instruction
id: bld_instruction_prompt_optimizer
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prompt_optimizer
quality: 8.8
title: "Instruction Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, instruction]
tldr: "Step-by-step production process for prompt_optimizer"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_prompt_optimizer
  - bld_collaboration_prompt_version
  - action-prompt-builder
  - bld_instruction_eval_framework
  - bld_instruction_content_filter
  - prompt-version-builder
  - bld_collaboration_action_prompt
  - bld_instruction_benchmark_suite
  - bld_instruction_self_improvement_loop
  - bld_instruction_action_prompt
---

## Phase 1: RESEARCH  
1. Analyze existing prompt frameworks for common inefficiencies  
2. Identify 10+ governance-related prompt failure modes in P03 domain  
3. Study optimization techniques from NLP literature (2020-2024)  
4. Benchmark 5+ existing prompt compilation tools for performance metrics  
5. Collect user feedback on current prompt governance workflows  
6. Document schema requirements from bld_schema_prompt_optimizer.md for artifact compatibility  

## Phase 2: COMPOSE  
1. Define input/output schema using bld_schema_prompt_optimizer.md specifications  
2. Identify prompt failure modes: ambiguity, redundancy, instruction drift  
3. Apply DSPy-style systematic optimization: define signature, generate candidates, select best  
4. Develop optimization passes: clarity, specificity, constraint alignment  
5. Integrate schema validation layer from bld_output_template_prompt_optimizer.md  
6. Add governance rules engine for compliance checks  
7. Implement feedback loop for iterative prompt refinement  
8. Score variants using cex_score.py before finalizing  
9. Finalize artifact with versioning and metadata tagging  

## Phase 3: VALIDATE  
[ ] Frontmatter complete and valid YAML  
[ ] Schema compliance verified against bld_schema_prompt_optimizer.md  
[ ] At least 2 optimization passes documented  
[ ] Industry references cited (DSPy, OPRO, APE, or PromptWizard)  
[ ] Output conforms to bld_output_template_prompt_optimizer.md structure


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_prompt_optimizer]] | upstream | 0.31 |
| [[bld_collaboration_prompt_version]] | downstream | 0.27 |
| [[action-prompt-builder]] | related | 0.26 |
| [[bld_instruction_eval_framework]] | sibling | 0.25 |
| [[bld_instruction_content_filter]] | sibling | 0.24 |
| [[prompt-version-builder]] | related | 0.24 |
| [[bld_collaboration_action_prompt]] | downstream | 0.23 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.23 |
| [[bld_instruction_self_improvement_loop]] | sibling | 0.23 |
| [[bld_instruction_action_prompt]] | sibling | 0.23 |
