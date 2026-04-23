---
kind: instruction
id: bld_instruction_reasoning_strategy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for reasoning_strategy
quality: 8.9
title: "Instruction Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, instruction]
tldr: "Step-by-step production process for reasoning_strategy"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - kc_reasoning_strategy
  - p03_qg_reasoning_strategy
  - bld_instruction_planning_strategy
  - p03_sp_reasoning_strategy_builder
  - bld_output_template_reasoning_strategy
  - p10_lr_reasoning_strategy_builder
  - bld_architecture_reasoning_strategy
  - bld_knowledge_card_reasoning_strategy
  - bld_instruction_benchmark_suite
  - bld_instruction_kind
---

## Phase 1: RESEARCH  

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
1. Define problem scope and target domain for reasoning tasks.  
2. Analyze existing structured reasoning frameworks (e.g., CoT, ReAct).  
3. Map gaps in current strategies for the specified domain.  
4. Identify key reasoning patterns (e.g., deduction, induction, abduction).  
5. Evaluate trade-offs between complexity and interpretability.  
6. Validate feasibility via small-scale prototype testing.  

## Phase 2: COMPOSE  
1. Outline artifact structure per SCHEMA.md (sections: purpose, steps, constraints).  
2. Draft reasoning phases with explicit input/output formats.  
3. Align language with OUTPUT_TEMPLATE.md (e.g., "Given X, infer Y via Z").  
4. Embed domain-specific examples (e.g., legal, medical, engineering).  
5. Specify constraints (e.g., data sources, computational limits).  
6. Refine steps for clarity and actionability.  
7. Add metadata: version, author, validation metrics.  
8. Cross-reference with schema to ensure completeness.  
9. Finalize artifact with consistent terminology.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema alignment: All required fields present.  
- [ ] ✅ Logical coherence: Steps produce valid inferences.  
- [ ] ✅ Example efficacy: Test cases pass domain benchmarks.  
- [ ] ✅ Clarity: No ambiguous language or missing context.  
- [ ] ✅ Robustness: Handles edge cases per constraints.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_reasoning_strategy]] | upstream | 0.28 |
| [[p03_qg_reasoning_strategy]] | downstream | 0.27 |
| [[bld_instruction_planning_strategy]] | sibling | 0.26 |
| [[p03_sp_reasoning_strategy_builder]] | related | 0.26 |
| [[bld_output_template_reasoning_strategy]] | downstream | 0.25 |
| [[p10_lr_reasoning_strategy_builder]] | downstream | 0.25 |
| [[bld_architecture_reasoning_strategy]] | downstream | 0.24 |
| [[bld_knowledge_card_reasoning_strategy]] | upstream | 0.23 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.23 |
| [[bld_instruction_kind]] | sibling | 0.22 |
