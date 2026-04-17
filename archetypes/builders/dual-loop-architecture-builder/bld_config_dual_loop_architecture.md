---
kind: config
id: bld_config_dual_loop_architecture
pillar: P09
parent: dual-loop-architecture-builder
llm_function: CONSTRAIN
purpose: Naming, paths, cadence knobs, model tiers, limits for dual_loop_architecture
quality: 9.1
title: "Config Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, config, cadence, model_tier]
keywords: [tick_ms, cadence_s, inner_model, outer_model, bridge_topic, budget]
tldr: "Config: naming p08_dl_*, cadence knobs (tick_ms + cadence_s), inner/outer model tiers, bridge topics, budgets."
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

## Naming Convention

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.

Pattern: `p08_dl_{{agent_name}}.md`
Examples: `p08_dl_coding_agent.md`, `p08_dl_research_agent.md`, `p08_dl_customer_support.md`
Regex: `^p08_dl_[a-z][a-z0-9_]{2,48}\.md$`

## Paths

```
P08_architecture/
  dual_loop/
    {{agent_name}}/
      spec.md             # the dual_loop_architecture artifact
      inner_loop.yaml     # inner prompt + tools
      outer_loop.yaml     # outer prompt + critic
      bridge.yaml         # shared state schema
```

## Cadence Knobs (REQUIRED in every produced artifact)

| Key | Type | Range | Default | Notes |
|-----|------|-------|---------|-------|
| tick_ms | int | 50..5000 | 200 | Inner loop step period |
| cadence_s | int | 2..300 | 15 | Outer loop re-plan period |
| early_replan_on_regret | bool | - | true | Critic can wake outer early |
| regret_threshold | float | 0.0..1.0 | 0.6 | Above this, outer wakes now |
| max_ticks_without_plan | int | 5..1000 | 50 | Safety: halt if outer dies |

## Model Tier Defaults

| Tier | Loop | Suggested models | Why |
|------|------|------------------|-----|
| fast | inner | claude-sonnet-4-6, claude-haiku, gpt-4o-mini, llama-3-8b | Low latency, cheap, deterministic |
| reasoning | outer | claude-opus-4-6 (+ extended thinking), gpt-o1, gpt-o3, deepseek-r1 | Slow, deep, revises strategy |

## Bridge Topics

| Topic | Direction | Payload |
|-------|-----------|---------|
| plan/current | outer -> inner | Plan struct (goals, steps, guardrails) |
| trajectory/append | inner -> outer | (obs, action, reward, ts) |
| critique/regret | critic -> outer | regret score in [0,1] |
| control/halt | governor -> both | reason + resume_token |

## Limits

```yaml
max_bytes: 5120
max_turns: 10
inner_token_budget_per_tick: 2000
outer_token_budget_per_cadence: 20000
total_session_cost_usd: 5.00
```

## Hooks

```yaml
pre_build: validate_cadence_ratio   # cadence_s * 1000 >= 10 * tick_ms
post_build: compile_bridge_schema
on_error: halt_and_dump_trajectory
on_quality_fail: retry_with_opus_outer
on_budget_exhausted: freeze_plan_and_log
```
