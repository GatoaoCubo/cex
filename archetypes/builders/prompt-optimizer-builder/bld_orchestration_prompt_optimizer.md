---
kind: collaboration
id: bld_collaboration_prompt_optimizer
pillar: P12
llm_function: COLLABORATE
purpose: How prompt_optimizer-builder works in crews with other builders
quality: 8.9
title: "Collaboration Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, collaboration]
tldr: "How prompt_optimizer-builder works in crews with other builders"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_prompt_technique
  - p03_sp_prompt_optimizer_builder
  - bld_architecture_prompt_compiler
  - bld_collaboration_action_paradigm
  - bld_collaboration_multimodal_prompt
  - bld_collaboration_agent_profile
  - bld_collaboration_safety_policy
  - bld_collaboration_agentic_rag
  - bld_collaboration_dataset_card
  - bld_collaboration_self_improvement_loop
---

## Crew Role  
Refines prompts for effectiveness, efficiency, and alignment with downstream tasks by iteratively testing, analyzing, and adjusting prompt structures and language.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| prompt_compiler | Raw prompts           | JSON        |  
| evaluator     | Performance metrics   | CSV         |  
| user_feedback | User input/feedback   | Text        |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| prompt_compiler | Optimized prompts     | JSON        |  
| analyst       | Optimization reports  | Markdown    |  
| template_manager | Updated prompt templates | YAML  |  

## Boundary  
Does NOT compile prompts into code (handled by prompt_compiler) or perform general optimization (handled by generic optimizer). Does NOT manage user feedback collection (handled by evaluator).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_prompt_technique]] | sibling | 0.33 |
| [[p03_sp_prompt_optimizer_builder]] | upstream | 0.29 |
| [[bld_architecture_prompt_compiler]] | upstream | 0.27 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.27 |
| [[bld_collaboration_multimodal_prompt]] | sibling | 0.26 |
| [[bld_collaboration_agent_profile]] | sibling | 0.26 |
| [[bld_collaboration_safety_policy]] | sibling | 0.26 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.26 |
| [[bld_collaboration_dataset_card]] | sibling | 0.24 |
| [[bld_collaboration_self_improvement_loop]] | sibling | 0.24 |
