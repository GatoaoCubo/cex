---
id: p01_kc_cex_lp02_model
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP02 Model — Who the LLM Is (9 Types of Identity)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp02, model, become, agent, persona, identity, lens]
tldr: "P02 Model defines LLM identity via 9 types — from agent to lens — using the BECOME function before any input"
when_to_use: "Classify identity artifacts or understand how P02 configures who the LLM is"
keywords: [agent, mental-model, persona, boot-config, model-card, lens, agent-package]
long_tails:
  - "What types of identity exist in CEX"
  - "Difference between agent and persona in CEX"
axioms:
  - "ALWAYS execute BECOME before INJECT"
  - "NEVER mix identity (P02) with knowledge (P01)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_lp01_knowledge, p01_kc_cex_lp03_prompt]
density_score: 1.0
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_function_become
  - bld_architecture_agent
  - p01_kc_agent_identity
  - p01_kc_lp02_model
  - p01_kc_agent
  - agent-builder
  - bld_architecture_boot_config
  - lens-builder
  - p01_kc_cex_lp03_prompt
  - bld_architecture_mental_model
---

## Quick Reference

topic: LP02 Model | scope: 9 artifact types | criticality: high
llm_function: BECOME | analogy: DNA + personality

## Key Concepts

- P02 answers: "who is this entity?"
- agent is the core type (complete identity + capabilities)
- Dominant function BECOME: identity configured at boot
- lens is a cognitive perspective that colors all perception
- mental_model maps routing, decisions and productive biases
- agent_package is a portable agent bundle (LLM-agnostic)
- axiom is an immutable principle of deep identity
- P02 defines HOW P01 is interpreted and P05 is formatted
- boot_config initializes per provider (model, temp, MCPs)
- model_card specifies the LLM: pricing, context window, limits
- router translates task to agent_group (routing rule)
- fallback_chain sequences models A -> B -> C with timeout
- Boot order: system_prompt -> mental_model -> persona -> agent
- P02 is the most diverse LP: 9 types for identity facets
- Same task + different lens = radically different output

## Phases

1. Definition: choose role, domain and perspective (lens)
2. Composition: assemble agent with persona + mental_model + tools
3. Boot: load boot_config + model_card (infra prerequisite)
4. Activation: BECOME executes system_prompt -> mental_model -> agent
5. Operation: active identity constrains all other LPs

## Golden Rules

- ALWAYS define identity BEFORE injecting context
- ALWAYS create mental_model for agents with 5+ tools
- NEVER define identity in user prompt (volatile)
- NEVER confuse who I AM (P02) with what I KNOW (P01)
- ALWAYS use agent_package for agents that migrate between LLMs

## Comparison

| Type | Purpose | Size | Core |
|------|---------|------|------|
| agent | Complete identity + capabilities | <= 5120B | yes |
| lens | Specialized cognitive perspective | <= 2048B | no |
| mental_model | Routing and decision map | <= 2048B | yes |
| boot_config | Per-provider initialization | <= 2048B | no |
| model_card | LLM spec (pricing, limits) | <= 2048B | no |
| router | Task -> agent_group rule | <= 1024B | yes |
| fallback_chain | Fallback sequence between models | <= 512B | no |
| agent_package | Portable agent bundle | <= 4096B | yes |
| axiom | Immutable fundamental principle | <= 3072B | yes |

## Flow

```
[boot_config + model_card]
          |
    [system_prompt]
          |
    [mental_model]
          |
      [persona]
          |
       [agent]  <-- BECOME completo
          |
  [lens colors perception]
          |
  [P01/P03/P04 operate under identity]
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- deepens: p01_kc_cex_function_become
- related: p01_kc_cex_lp01_knowledge


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_become]] | sibling | 0.51 |
| [[bld_architecture_agent]] | downstream | 0.35 |
| [[p01_kc_agent_identity]] | sibling | 0.35 |
| [[p01_kc_lp02_model]] | sibling | 0.34 |
| [[p01_kc_agent]] | sibling | 0.30 |
| [[agent-builder]] | downstream | 0.30 |
| [[bld_architecture_boot_config]] | downstream | 0.29 |
| [[lens-builder]] | downstream | 0.28 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.28 |
| [[bld_architecture_mental_model]] | downstream | 0.27 |
