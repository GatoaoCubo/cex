---
id: p10_cc_rolling_window_50pct
kind: compression_config
pillar: P10
title: "Example — Rolling Window Compression (50% Token Reduction)"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
strategy: rolling_window
trigger_ratio: 0.85
preserve_types: [correction, user_decision, identity, system_prompt]
max_summary_tokens: 2048
min_context_tokens: 1024
domain: compression_config
quality: 9.1
tags: [compression-config, rolling-window, token-reduction, memory, context]
tldr: "Rolling window compression — triggers at 85% context, keeps last 10 turns verbatim, summarizes older turns, preserves corrections. ~50% token reduction."
when_to_use: "Long-running agent sessions that accumulate context beyond 50% of model limit"
keywords: [compression, rolling-window, token, budget, summarization, context]
density_score: null
related:
  - ex_context_session_memory
  - p01_kc_compression_config
  - p03_sp_compression_config_builder
  - bld_knowledge_card_compression_config
  - p10_lr_compression_config_builder
  - bld_examples_compression_config
  - p10_memory_summary
  - compression-config-builder
  - bld_collaboration_compression_config
  - bld_instruction_compression_config
---

# Compression Config: Rolling Window (50% Reduction)

## Strategy
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| strategy | rolling_window | Preserves recent context verbatim, compresses old |
| trigger_ratio | 0.85 | Triggers at 85% of context limit |
| window_size | 10 turns | Last 10 turns kept verbatim |
| max_summary_tokens | 2048 | Budget for compressed history summary |
| min_context_tokens | 1024 | Floor — never compress below this |

## Preserve Rules
| Content Type | Action | Rationale |
|-------------|--------|-----------|
| system_prompt | NEVER compress | Identity loss destroys agent behavior |
| correction | ALWAYS keep | User corrections are highest-value context |
| user_decision | ALWAYS keep | GDP decisions must persist across session |
| identity | ALWAYS keep | Agent role and boundaries |
| tool_output | SUMMARIZE | Data precision drops but gist preserved |
| assistant_reasoning | DROP first | Lowest value — conclusions matter, not process |

## Decay Weights
```yaml
decay_weights:
  system: 0.0      # never decays
  correction: 0.0  # never decays
  user: 0.3        # slow decay — user messages are reference
  assistant: 0.5   # moderate decay — reasoning is ephemeral
  tool: 0.7        # fast decay — tool outputs are re-fetchable
```

## Token Budget Example (200K context model)
| Phase | Tokens | % of Limit |
|-------|--------|-----------|
| Before compression | 170,000 | 85% (trigger) |
| System prompt (preserved) | 4,000 | 2% |
| Corrections (preserved) | 2,000 | 1% |
| Recent 10 turns (verbatim) | 40,000 | 20% |
| Older turns (summarized) | 2,048 | 1% |
| **After compression** | **48,048** | **24%** |
| **Reduction** | **~72%** | — |

## Tiered Fallback
```
1. Truncate assistant reasoning (free, ~10% reduction)
2. Summarize old turns via LLM (1 API call, ~40% reduction)
3. Hard-drop turns beyond window (free, last resort)
```

## Boundary
compression_config IS: rules for when and how to compact accumulated context to fit token budgets.
compression_config IS NOT: a memory type (what to remember), a session backend (where to store), or a token budget (how much is available).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ex_context_session_memory]] | upstream | 0.48 |
| [[p01_kc_compression_config]] | related | 0.45 |
| [[p03_sp_compression_config_builder]] | upstream | 0.41 |
| [[bld_knowledge_card_compression_config]] | upstream | 0.40 |
| [[p10_lr_compression_config_builder]] | related | 0.35 |
| [[bld_examples_compression_config]] | upstream | 0.34 |
| [[p10_memory_summary]] | related | 0.33 |
| [[compression-config-builder]] | upstream | 0.32 |
| [[bld_collaboration_compression_config]] | downstream | 0.31 |
| [[bld_instruction_compression_config]] | upstream | 0.30 |
