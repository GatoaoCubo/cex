---
id: p01_kc_fallback_chain
kind: knowledge_card
type: kind
pillar: P02
title: "Fallback Chain — Deep Knowledge for fallback_chain"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: fallback_chain
quality: 9.1
tags: [fallback_chain, p02, GOVERN, kind-kc]
tldr: "Ordered model fallback sequence — when primary LLM fails or times out, cascade to next model with defined timeout per step"
when_to_use: "Building, reviewing, or reasoning about fallback_chain artifacts"
keywords: [fallback, cascade, model-routing, resilience, timeout]
feeds_kinds: [fallback_chain]
density_score: null
related:
  - fallback-chain-builder
  - p02_fb_model_cascade
  - bld_examples_fallback_chain
  - bld_architecture_fallback_chain
  - bld_instruction_fallback_chain
  - bld_collaboration_fallback_chain
  - p01_kc_model_card
  - p10_lr_fallback_chain_builder
  - bld_collaboration_model_provider
  - p03_sp_fallback_chain_builder
---

# Fallback Chain

## Spec
```yaml
kind: fallback_chain
pillar: P02
llm_function: GOVERN
max_bytes: 512
naming: p02_fb_{{chain}}.yaml
core: false
```

## What It Is
A fallback_chain defines an ordered sequence of LLM models to try when the primary model fails, times out, or returns low-confidence results. Each step has a timeout threshold. It is NOT a chain (P03, which is a sequence of prompts/steps) nor a router (which routes tasks to agent_groups based on keywords). Fallback chains answer "what model do I try next when this one fails?" — routers answer "which agent handles this task?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ChatModelWithFallbacks` / `with_fallbacks()` | Chained LLMs; first success wins |
| LlamaIndex | `MultiModal` LLM selector | Less explicit; manual fallback in code |
| CrewAI | `max_retry_limit` + model swap | Retry with same model; no native cascade |
| DSPy | `dspy.configure(lm=..., backoff=...)` | Backoff strategy; can swap LMs programmatically |
| Haystack | Pipeline branching with routers | Conditional routing based on error state |
| OpenAI | API retry with model downgrade | Manual: try gpt-4o, catch, retry gpt-4o-mini |
| Anthropic | API retry with model parameter change | Manual: opus → sonnet → haiku cascade |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| chain | list[model] | required | More steps = higher resilience but more complexity |
| timeout_per_step | int (seconds) | 30 | Lower timeout = faster failover but more false triggers |
| retry_count | int | 1 | More retries = resilience but latency compounds |
| quality_threshold | float | 0.0 | If set, triggers fallback on low-quality responses too |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Cost cascade | Budget-sensitive pipeline | opus → sonnet → haiku (try cheap first for simple tasks) |
| Quality cascade | Critical output | opus (30s) → opus retry (30s) → sonnet (fallback) |
| Speed cascade | Latency-sensitive | haiku (5s) → sonnet (10s) → opus (30s) |
| Provider cascade | Multi-cloud resilience | Anthropic → OpenAI → local Ollama |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Same model repeated | Retrying identical request; same failure mode | Vary model or temperature between steps |
| No timeout | Hangs indefinitely on unresponsive model | Always set timeout_per_step |
| Too many steps (>4) | Latency compounds; user waits minutes | Max 3 steps; escalate to error after that |

## Integration Graph
```
[model_card] --> [fallback_chain] --> [agent, boot_config]
                       |
                [router, env_config (P09)]
```

## Decision Tree
- IF system needs resilience against model outages THEN fallback_chain
- IF routing tasks to different agents THEN router (P02)
- IF sequencing prompt steps THEN chain (P03)
- IF single model with retries THEN just retry logic, not a fallback_chain
- DEFAULT: fallback_chain when >1 model in play

## Quality Criteria
- GOOD: Ordered models listed; timeout per step defined; tested failover
- GREAT: Each step has different model/provider; quality threshold triggers smart fallback; logged
- FAIL: No timeout; same model repeated; >4 steps; no logging of which step succeeded

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fallback-chain-builder]] | related | 0.43 |
| [[p02_fb_model_cascade]] | related | 0.42 |
| [[bld_examples_fallback_chain]] | downstream | 0.39 |
| [[bld_architecture_fallback_chain]] | downstream | 0.34 |
| [[bld_instruction_fallback_chain]] | downstream | 0.34 |
| [[bld_collaboration_fallback_chain]] | downstream | 0.34 |
| [[p01_kc_model_card]] | sibling | 0.34 |
| [[p10_lr_fallback_chain_builder]] | downstream | 0.33 |
| [[bld_collaboration_model_provider]] | related | 0.33 |
| [[p03_sp_fallback_chain_builder]] | downstream | 0.33 |
