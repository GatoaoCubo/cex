---
kind: collaboration
id: bld_collaboration_prompt_cache
pillar: P12
llm_function: COLLABORATE
purpose: How prompt-cache-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: prompt-cache-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should LLM prompts be cached for cost/latency reduction?"
I do not manage sessions. I do not summarize conversations. I do not store runtime variables.
I configure caching strategies that reduce redundant LLM calls.
## Crew Compositions
### Crew: "Cost Optimization"
```
  1. context-window-config-builder -> "token budget allocation"
  2. prompt-cache-builder -> "caching strategy for repeated prompts"
  3. model-card-builder -> "model pricing and capabilities"
```
### Crew: "Multi-Agent Shared Cache"
```
  1. prompt-cache-builder -> "shared cache config (Redis backend)"
  2. agent-card-builder -> "agents configured with cache namespace"
  3. env-config-builder -> "Redis connection and deployment"
```
## Handoff Protocol
### I Receive
- seeds: workload pattern, repetition rate, freshness needs, deployment topology
- optional: provider-specific caching requirements
### I Produce
- prompt_cache artifact (.yaml, max 2KB)
- committed to: `P10_memory/examples/p10_pc_{name}.yaml`
### I Signal
- signal: complete (with quality from QUALITY_GATES)
## Builders I Depend On
| Builder | Why |
|---------|-----|
| system-prompt-builder | System prompts are primary cache candidates |
| model-card-builder | Provider-specific caching capabilities |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-card-builder | Agent deployment includes cache config |
| env-config-builder | Infrastructure for cache storage backend |
| runtime-state-builder | Cache metrics feed runtime monitoring |
