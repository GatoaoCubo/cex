---
kind: collaboration
id: bld_collaboration_multimodal_prompt
pillar: P12
llm_function: COLLABORATE
purpose: How multimodal_prompt-builder works in crews with other builders
quality: 8.9
title: "Collaboration Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, collaboration]
tldr: "How multimodal_prompt-builder works in crews with other builders"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_multimodal_prompt_builder
  - bld_collaboration_llm_evaluation_scenario
  - multimodal-prompt-builder
  - bld_collaboration_prompt_technique
  - bld_knowledge_card_multimodal_prompt
  - bld_collaboration_multi_modal_config
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_prompt_optimizer
  - bld_collaboration_capability_registry
  - bld_collaboration_gpai_technical_doc
---

## Crew Role  
Synthesizes multimodal prompts by integrating text, image, and audio inputs into cohesive instructions for AI models. Acts as a bridge between content creators and technical teams.  

## Receives From  
| Builder             | What                              | Format   |  
|---------------------|-----------------------------------|----------|  
| multi_modal_config  | Modality constraints and settings | YAML     |  
| knowledge_card      | Domain context for grounding      | Markdown |  
| embedding_config    | Token embedding specifications    | YAML     |  

## Produces For  
| Builder             | What                              | Format   |  
|---------------------|-----------------------------------|----------|  
| prompt_template     | Multimodal prompt structures      | Markdown |  
| llm_judge           | Test cases for cross-modal eval   | Markdown |  
| benchmark           | Evaluation scenarios with inputs  | Markdown |  

## Boundary  
Does NOT handle model-specific configuration (handled by `multi_modal_config`) or text-only prompt optimization (handled by `prompt_technique`).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_multimodal_prompt_builder]] | upstream | 0.31 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.30 |
| [[multimodal-prompt-builder]] | upstream | 0.29 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.26 |
| [[bld_knowledge_card_multimodal_prompt]] | upstream | 0.26 |
| [[bld_collaboration_multi_modal_config]] | sibling | 0.26 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.25 |
| [[bld_collaboration_prompt_optimizer]] | sibling | 0.24 |
| [[bld_collaboration_capability_registry]] | sibling | 0.24 |
| [[bld_collaboration_gpai_technical_doc]] | sibling | 0.24 |
