---
kind: architecture
id: bld_architecture_fallback_chain
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of fallback_chain — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Fallback Chain"
version: "1.0.0"
author: n03_builder
tags: [fallback_chain, builder, examples]
tldr: "Golden and anti-examples for fallback chain construction, demonstrating ideal structure and common pitfalls."
domain: "fallback chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - fallback-chain-builder
  - bld_examples_fallback_chain
  - p03_sp_fallback_chain_builder
  - p01_kc_fallback_chain
  - p11_qg_fallback_chain
  - bld_instruction_fallback_chain
  - p10_lr_fallback_chain_builder
  - bld_collaboration_fallback_chain
  - bld_schema_fallback_chain
  - bld_knowledge_card_fallback_chain
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| step_sequence | Ordered list of model steps (primary → degraded → minimum) | fallback_chain | required |
| primary_model | First model attempted; highest capability and cost | fallback_chain | required |
| fallback_steps | Subsequent models activated on trigger; ordered A→B→C | fallback_chain | required |
| timeout_per_step | Maximum wait time before advancing to next step | fallback_chain | required |
| quality_threshold | Minimum acceptable output score; triggers step advance if not met | fallback_chain | required |
| circuit_breaker | Opens after N consecutive failures; halts chain and emits error signal | fallback_chain | required |
| cost_controls | Per-step budget caps; prevents runaway spend during degradation | fallback_chain | required |
| trigger_conditions | Conditions that activate the chain: timeout, error, low quality, cost exceeded | fallback_chain | required |
| degradation_signal | Event emitted when chain advances a step or exhausts all steps | fallback_chain | required |
## Dependency Graph
```
model_card (P02) --produces--> fallback_chain
router (P02)     --signals-->  fallback_chain
fallback_chain   --produces--> agent (P02)
fallback_chain   --produces--> boot_config (P02)
fallback_chain   --signals-->  error_signal
circuit_breaker  --depends-->  fallback_chain
```
| From | To | Type | Data |
|------|----|------|------|
| model_card (P02) | fallback_chain | data_flow | model specs (name, cost, capability) for each step |
| router (P02) | fallback_chain | signals | routing failure triggers chain activation |
| fallback_chain | agent (P02) | produces | resilient model selection for agent execution |
| fallback_chain | boot_config (P02) | produces | per-step provider configuration |
| fallback_chain | error_signal | signals | degradation events and circuit-breaker opens |
| circuit_breaker | fallback_chain | depends | reads consecutive failure count to open/close |
## Boundary Table
| fallback_chain IS | fallback_chain IS NOT |
|-------------------|-----------------------|
| A sequence of models tried in order when the primary fails | A sequence of prompts or text transformations (that is a chain) |
| Activated by timeout, error, low quality, or cost exceeded | A task router that decides which agent receives a request |
| Stateful across retries within one execution | A static config file that never activates at runtime |
| Responsible for graceful model degradation (opus → sonnet → haiku) | Responsible for orchestrating multi-step agent workflows |
| Emitter of degradation and circuit-breaker signals | A model card describing a single model's properties |
| Owner of circuit breaker logic (opens after N failures) | A boot config initializing one provider |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Trigger | trigger_conditions, router (P02) | Detect failure conditions that activate the chain |
| Sequence | step_sequence, primary_model, fallback_steps | Define the ordered model degradation path A→B→C |
| Control | timeout_per_step, quality_threshold, cost_controls | Govern when each step advances to the next |
| Safety | circuit_breaker | Halt chain after repeated failures; prevent infinite retry |
| Output | agent (P02), boot_config (P02) | Consume the selected model configuration |
| Observability | degradation_signal, error_signal | Emit events for monitoring and alerting |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fallback-chain-builder]] | upstream | 0.52 |
| [[bld_examples_fallback_chain]] | upstream | 0.47 |
| [[p03_sp_fallback_chain_builder]] | upstream | 0.46 |
| [[p01_kc_fallback_chain]] | upstream | 0.46 |
| [[p11_qg_fallback_chain]] | downstream | 0.46 |
| [[bld_instruction_fallback_chain]] | upstream | 0.38 |
| [[p10_lr_fallback_chain_builder]] | downstream | 0.35 |
| [[bld_collaboration_fallback_chain]] | downstream | 0.35 |
| [[bld_schema_fallback_chain]] | upstream | 0.33 |
| [[bld_knowledge_card_fallback_chain]] | upstream | 0.32 |
