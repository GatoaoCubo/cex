---
kind: collaboration
id: bld_collaboration_context_window_config
pillar: P12
llm_function: COLLABORATE
purpose: How context-window-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Context Window Config"
version: "1.0.0"
author: n03_builder
tags: [context_window_config, builder, examples]
tldr: "Golden and anti-examples for context window config construction, demonstrating ideal structure and common pitfalls."
domain: "context window config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_model_card
  - bld_collaboration_prompt_template
  - bld_collaboration_action_prompt
  - bld_collaboration_prompt_version
  - bld_collaboration_chunk_strategy
  - bld_collaboration_context_doc
  - bld_collaboration_system_prompt
  - bld_collaboration_builder
  - bld_collaboration_retriever_config
  - bld_collaboration_model_provider
---

# Collaboration: context-window-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should the context window budget be allocated?"
I do not write prompts. I do not define agent identity. I do not specify model capabilities.
I ensure every prompt component has an allocated budget within model limits.
## Crew Compositions
### Crew: "Prompt Assembly Pipeline"
```
  1. system-prompt-builder -> "agent identity"
  2. few-shot-example-builder -> "calibration examples"
  3. context-window-config-builder -> "budget allocation for all components"
  4. prompt-template-builder -> "assembly template respecting budgets"
```
### Crew: "RAG Optimization"
```
  1. retriever-config-builder -> "retrieval parameters"
  2. context-window-config-builder -> "context budget allocation"
  3. chunk-strategy-builder -> "chunk sizes fitting budget"
```
## Handoff Protocol
### I Receive
- seeds: target model, workload profile, prompt component sizes
- optional: existing budgets to optimize, compression requirements
### I Produce
- context_window_config artifact (.yaml, max 2KB)
- committed to: `P03_prompt/examples/p03_cwc_{model}.yaml`
### I Signal
- signal: complete (with quality from QUALITY_GATES)
## Builders I Depend On
| Builder | Why |
|---------|-----|
| model-card-builder | total_tokens from model spec |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| prompt-template-builder | Template respects allocated budgets |
| agent-card-builder | Deployment uses token limits |
| chunk-strategy-builder | Chunk sizes fit context budget |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_card]] | sibling | 0.46 |
| [[bld_collaboration_prompt_template]] | sibling | 0.43 |
| [[bld_collaboration_action_prompt]] | sibling | 0.42 |
| [[bld_collaboration_prompt_version]] | sibling | 0.41 |
| [[bld_collaboration_chunk_strategy]] | sibling | 0.40 |
| [[bld_collaboration_context_doc]] | sibling | 0.39 |
| [[bld_collaboration_system_prompt]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.38 |
| [[bld_collaboration_retriever_config]] | sibling | 0.38 |
| [[bld_collaboration_model_provider]] | sibling | 0.36 |
