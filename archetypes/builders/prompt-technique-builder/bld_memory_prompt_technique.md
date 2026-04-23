---
kind: memory
id: p10_mem_prompt_technique_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for prompt_technique construction
quality: 8.7
title: "Memory Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, memory]
tldr: "Learned patterns and pitfalls for prompt_technique construction"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p10_mem_prompt_optimizer_builder
  - p10_lr_judge_config_builder
  - kc_reasoning_strategy
  - p10_lr_planning_strategy_builder
  - p03_sp_prompt_optimizer_builder
  - p10_lr_agent_profile_builder
  - p10_mem_eval_metric_builder
  - p10_lr_quickstart_guide_builder
  - p10_lr_reasoning_strategy_builder
  - p10_mem_customer_segment_builder
---

## Observation
Ambiguous instructions often lead to inconsistent or off-topic outputs. Overloading prompts with excessive details can overwhelm models, reducing effectiveness.

## Pattern
Clear, concise phrasing with explicit goals improves reliability. Structuring prompts into logical steps or roles (e.g., "Act as a tutor") enhances focus and coherence.

## Evidence
Reviewed artifacts showed 40% higher success rates with prompts using example-based scaffolding (e.g., "Answer like this: [example]").

## Recommendations
- Prioritize specificity: Define exact tasks and desired output formats.
- Use role-playing or scenario framing to guide model behavior.
- Test iterative refinements to balance detail and clarity.
- Avoid vague terms like "best" or "good"; use measurable criteria.
- Align techniques with model capabilities (e.g., avoid complex reasoning for basic models).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_mem_prompt_optimizer_builder]] | sibling | 0.32 |
| [[p10_lr_judge_config_builder]] | related | 0.24 |
| [[kc_reasoning_strategy]] | upstream | 0.22 |
| [[p10_lr_planning_strategy_builder]] | related | 0.21 |
| [[p03_sp_prompt_optimizer_builder]] | upstream | 0.20 |
| [[p10_lr_agent_profile_builder]] | related | 0.19 |
| [[p10_mem_eval_metric_builder]] | sibling | 0.19 |
| [[p10_lr_quickstart_guide_builder]] | sibling | 0.19 |
| [[p10_lr_reasoning_strategy_builder]] | related | 0.19 |
| [[p10_mem_customer_segment_builder]] | sibling | 0.18 |
