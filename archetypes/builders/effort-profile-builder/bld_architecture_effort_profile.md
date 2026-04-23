---
kind: architecture
id: bld_architecture_effort_profile
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of effort_profile — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Effort Profile"
version: "1.0.0"
author: n03_builder
tags: [effort_profile, builder, examples]
tldr: "Golden and anti-examples for effort profile construction, demonstrating ideal structure and common pitfalls."
domain: "effort profile construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - effort-profile-builder
  - p03_sp_effort_profile_builder
  - bld_examples_effort_profile
  - p01_kc_effort_profile
  - bld_output_template_effort_profile
  - p10_lr_effort_profile_builder
  - bld_instruction_effort_profile
  - p11_qg_effort_profile
  - bld_tools_effort_profile
  - bld_collaboration_model_card
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| model | LLM model to use (haiku, sonnet, opus) | effort_profile | required |
| thinking_level | Reasoning depth (low, medium, high, max) | effort_profile | required |
| target_builder | Which builder this profile applies to | effort_profile | required |
| cost_tier | Relative cost category (low, medium, high) | effort_profile | recommended |
| fallback_model | Alternative model if primary unavailable | external | optional |
| runtime_rule | Execution rules that consume this profile | P09 | consumer |
| agent | Agent definition that references this profile | P02 | consumer |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| model | effort_profile | produces | LLM model selection (haiku, sonnet, opus) |
| thinking_level | effort_profile | produces | Reasoning depth (low, medium, high, max) |
| target_builder | effort_profile | produces | Builder this profile targets |
| cost_tier | effort_profile | produces | Relative cost category |
| fallback_model | external | produces | Alternative model for failover |
| runtime_rule | P09 | depends | Execution rules that consume effort config |
| agent | P02 | depends | Agent definitions referencing model config |
## Boundary Table
| effort_profile IS | effort_profile IS NOT |
|-------------|----------------|
| Model and thinking level configuration for a builder | runtime_rule (execution rules) |
| QUAL model/thinking usar | env_config (environment vars) |
| Maps builder to model and reasoning depth | model_card (model specs) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | model, thinking_level, target_builder | Define the artifact's core parameters |
| optional | cost_tier, fallback_model | Extend with recommended fields |
| external | runtime_rule, agent | Upstream/downstream connections |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_effort_profile
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-effort-profile.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[effort-profile-builder]] | downstream | 0.51 |
| [[p03_sp_effort_profile_builder]] | downstream | 0.51 |
| [[bld_examples_effort_profile]] | upstream | 0.48 |
| [[p01_kc_effort_profile]] | downstream | 0.44 |
| [[bld_output_template_effort_profile]] | upstream | 0.42 |
| [[p10_lr_effort_profile_builder]] | downstream | 0.42 |
| [[bld_instruction_effort_profile]] | upstream | 0.40 |
| [[p11_qg_effort_profile]] | downstream | 0.38 |
| [[bld_tools_effort_profile]] | upstream | 0.36 |
| [[bld_collaboration_model_card]] | upstream | 0.35 |
