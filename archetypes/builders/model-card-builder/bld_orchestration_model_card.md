---
kind: collaboration
id: bld_collaboration_model_card
pillar: P02
llm_function: COLLABORATE
purpose: How model-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Model Card"
version: "1.0.0"
author: n03_builder
tags: [model_card, builder, examples]
tldr: "Golden and anti-examples for model card construction, demonstrating ideal structure and common pitfalls."
domain: "model card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_model_provider
  - model-card-builder
  - bld_collaboration_agent
  - bld_collaboration_agent_card
  - bld_collaboration_mental_model
  - bld_collaboration_boot_config
  - bld_collaboration_system_prompt
  - bld_collaboration_finetune_config
  - bld_collaboration_builder
  - bld_collaboration_fallback_chain
---

# Collaboration: model-card-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what can this LLM do and how much does it cost?"
I produce technical specs for LLMs with pricing, context limits, capability booleans, and provider data. I do NOT handle boot configuration (boot-config-builder), agent definitions (agent-builder), benchmark design (benchmark-builder), or routing infrastructure (router-builder).
## Crew Compositions
### Crew: "Build New Agent from Scratch"
```
  1. model-card-builder   -> "LLM spec: pricing, context window, capability booleans"
  2. mental-model-builder -> "cognitive blueprint referencing model constraints"
  3. agent-builder        -> "complete agent definition selecting the documented model"
  4. system-prompt-builder -> "persona adapted to model capabilities and context limits"
  5. boot-config-builder  -> "initialization wired to model ID, temperature, and token limits"
```
### Crew: "Bootstrap New Agent_group"
```
  1. model-card-builder    -> "spec for the model powering the agent_group"
  2. agent-card-builder -> "agent_group role, MCPs, and behavioral constraints"
  3. boot-config-builder   -> "startup configuration using model params from the card"
  4. system-prompt-builder -> "PRIME file adapted to documented model capabilities"
```
### Crew: "Model Comparison"
```
  1. model-card-builder    -> "produces cards for each candidate model"
  2. lens-builder          -> "applies cost/speed/quality perspective to compare them"
  3. scoring-rubric-builder -> "scores each model against target use case criteria"
```
## Handoff Protocol
### I Receive
- seeds: model name, provider (minimum required)
- optional: use case context (informs When to Use table), competing models to compare
### I Produce
- model_card artifact (Markdown, 26 frontmatter fields, capability booleans, normalized pricing, max 4KB)
- committed to: `cex/P02_model/examples/p02_mc_{provider}_{slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None. model-card-builder is INDEPENDENT (layer 0 infrastructure).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder          | references model limits and capabilities in agent definition |
| boot-config-builder    | needs model ID, temperature range, and context limits for initialization |
| mental-model-builder   | uses model capability data to scope routing rules and decision thresholds |
| router-builder         | uses pricing and capability data to assign tasks to the right model |
| fallback-chain-builder | needs model specs to order fallback priority by cost and capability |
| agent-package-builder    | includes model_card as a deploy dependency in the packaged artifact |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_provider]] | sibling | 0.58 |
| [[model-card-builder]] | related | 0.47 |
| [[bld_collaboration_agent]] | sibling | 0.46 |
| [[bld_collaboration_agent_card]] | sibling | 0.44 |
| [[bld_collaboration_mental_model]] | sibling | 0.43 |
| [[bld_collaboration_boot_config]] | sibling | 0.42 |
| [[bld_collaboration_system_prompt]] | sibling | 0.39 |
| [[bld_collaboration_finetune_config]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.37 |
