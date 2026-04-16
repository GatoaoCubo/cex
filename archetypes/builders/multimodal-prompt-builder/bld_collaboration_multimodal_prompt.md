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
