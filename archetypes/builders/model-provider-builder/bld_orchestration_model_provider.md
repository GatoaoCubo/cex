---
kind: collaboration
id: bld_collaboration_model_provider
pillar: P02
llm_function: COLLABORATE
purpose: How model-provider-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_model_card
  - model-provider-builder
  - bld_collaboration_boot_config
  - bld_memory_model_provider
  - bld_collaboration_embedder_provider
  - p03_sp_model_provider_builder
  - bld_collaboration_fallback_chain
  - p03_ins_model_provider
  - bld_config_model_provider
  - bld_collaboration_agent
---

# Collaboration: model-provider-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should we connect to and route between LLM providers?"
I produce connection and routing configurations for LLM APIs with tiered model selection, rate limits, fallback chains, and authentication. I do NOT handle model specs (model-card-builder), embedding configs (embedder-provider-builder), agent definitions (agent-builder), or boot configurations (boot-config-builder).
## Crew Compositions
### Crew: "Setup Multi-Provider LLM Routing"
```
  1. model-provider-builder  -> "provider connection configs for each API (Anthropic, OpenAI, Google)"
  2. model-card-builder      -> "model specs informing tier assignment and cost routing"
  3. router-builder           -> "routing rules: nucleus -> provider -> model selection"
  4. fallback-chain-builder   -> "cross-provider fallback ordering and trigger conditions"
```
### Crew: "Bootstrap New CEX Nucleus"
```
  1. model-provider-builder  -> "provider config for the nucleus's assigned LLM"
  2. model-card-builder      -> "spec for the model powering the nucleus"
  3. boot-config-builder     -> "startup config using provider connection and model params"
  4. system-prompt-builder   -> "persona adapted to assigned model capabilities"
```
### Crew: "Cost Optimization Audit"
```
  1. model-provider-builder  -> "all provider configs with current pricing"
  2. lens-builder            -> "cost/quality perspective for routing optimization"
  3. scoring-rubric-builder  -> "scores each provider-tier combo against task quality"
  4. model-card-builder      -> "capability comparison for tier reassignment"
```
## Handoff Protocol
### I Receive
- seeds: provider name, account tier (minimum required)
- optional: nucleus assignment, fallback provider preference, budget constraints
### I Produce
- model_provider artifact (YAML, 22+ frontmatter fields, tiered models, rate limits, fallback chain)
- committed to: `cex/P02_model/examples/p02_mp_{provider}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| Builder | Why |
|---------|-----|
| model-card-builder | model specs inform tier assignment (which model is fast/balanced/quality) |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| router-builder         | needs provider configs to build routing rules |
| boot-config-builder    | needs provider API and model ID for nucleus startup |
| fallback-chain-builder | needs provider health and rate limit data for fallback ordering |
| agent-builder          | references provider capabilities in agent definition |
| agent-package-builder  | includes model_provider as a deploy dependency |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_card]] | sibling | 0.61 |
| [[model-provider-builder]] | related | 0.54 |
| [[bld_collaboration_boot_config]] | sibling | 0.51 |
| [[bld_memory_model_provider]] | downstream | 0.46 |
| [[bld_collaboration_embedder_provider]] | sibling | 0.45 |
| [[p03_sp_model_provider_builder]] | downstream | 0.44 |
| [[bld_collaboration_fallback_chain]] | sibling | 0.42 |
| [[p03_ins_model_provider]] | downstream | 0.41 |
| [[bld_config_model_provider]] | downstream | 0.41 |
| [[bld_collaboration_agent]] | sibling | 0.40 |
