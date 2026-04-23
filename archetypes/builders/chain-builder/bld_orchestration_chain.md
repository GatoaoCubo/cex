---
kind: collaboration
id: bld_collaboration_chain
pillar: P12
llm_function: COLLABORATE
purpose: How chain-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - chain-builder
  - bld_collaboration_action_prompt
  - bld_collaboration_instruction
  - p01_kc_chain
  - p03_sp_chain_builder
  - bld_collaboration_input_schema
  - bld_collaboration_context_doc
  - p10_lr_chain_builder
  - bld_collaboration_few_shot_example
  - bld_collaboration_fallback_chain
---

# Collaboration: chain-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what prompts run in what order, and how does data flow between them?"
I do not orchestrate agents. I do not define individual task prompts.
I compose prompt pipelines so multi-step LLM tasks execute in correct sequence with typed data flow.
## Crew Compositions
### Crew: "Prompt Pipeline"
```
  1. action-prompt-builder -> "individual task prompts (steps)"
  2. chain-builder -> "sequential composition with data flow"
  3. input-schema-builder -> "typed contracts between chain steps"
```
### Crew: "Complex Task Decomposition"
```
  1. instruction-builder -> "step-by-step recipe for task"
  2. chain-builder -> "prompt chain that implements the recipe"
  3. e2e-eval-builder -> "end-to-end test of the full chain"
```
## Handoff Protocol
### I Receive
- seeds: task decomposition (list of steps), data flow description
- optional: error handling strategy, branching conditions, context passing rules
### I Produce
- chain artifact (.md + .yaml frontmatter)
- committed to: `cex/P03/examples/p03_chain_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- action-prompt-builder: provides individual step prompts composed into the chain
- input-schema-builder: provides typed contracts for inter-step data flow
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Tests the full chain from input to final output |
| dag-builder | May model chain dependencies in execution graphs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[chain-builder]] | upstream | 0.57 |
| [[bld_collaboration_action_prompt]] | sibling | 0.55 |
| [[bld_collaboration_instruction]] | sibling | 0.50 |
| [[p01_kc_chain]] | upstream | 0.44 |
| [[p03_sp_chain_builder]] | upstream | 0.41 |
| [[bld_collaboration_input_schema]] | sibling | 0.40 |
| [[bld_collaboration_context_doc]] | sibling | 0.40 |
| [[p10_lr_chain_builder]] | upstream | 0.40 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.40 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.39 |
