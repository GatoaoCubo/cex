---
id: p01_kc_compression_config
kind: knowledge_card
type: kind
pillar: P10
title: "Compression Config -- Deep Knowledge for compression_config"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: compression_config
quality: 9.1
tags: [compression_config, p10, INJECT, kind-kc, memory]
tldr: "Configuration for context/memory compression -- controls how and when content is compacted to fit token budgets"
when_to_use: "Building or tuning context compaction behavior for long-running agent sessions"
keywords: [compression, compaction, token, budget, summarization, truncation]
feeds_kinds: [compression_config]
density_score: null
---

# Compression Config

## Spec
```yaml
kind: compression_config
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_cc_{{name}}.yaml
core: false
```

## Purpose

A compression config defines HOW and WHEN an agent's accumulated context is compressed to stay within token limits. Without explicit compression config, agents either crash at context limits or lose critical earlier context silently.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| strategy | Compression method | `summarize`, `truncate_oldest`, `rolling_window`, `priority_keep` |
| trigger_ratio | Context-to-limit ratio that triggers compression | `0.85` (85% of max) |
| preserve_types | Content types that survive compression | `[correction, user_decision, identity]` |
| max_summary_tokens | Token budget for compressed summary | `2048` |
| min_context_tokens | Minimum raw context to keep uncompressed | `1024` |
| decay_weights | Per-type decay multipliers | `{system: 0.0, user: 0.3, assistant: 0.5}` |

## Key Patterns

1. **Priority-based**: Tag content with priority at injection time; compression drops low-priority first
2. **Rolling window**: Keep last N turns verbatim, summarize everything before
3. **Semantic dedup**: Detect repeated information across turns, keep only latest version
4. **Tiered**: First try truncation (free), then summarization (LLM cost), then hard-drop

## Anti-Patterns

- Setting trigger_ratio too low (constant re-compression wastes tokens)
- Compressing system prompts (identity loss)
- Summarizing tool outputs (precision loss on data)
- No preserve_types list (corrections get lost)

## CEX Integration

- Wire 6 (`p04_skill_compact`) triggers at 85% context budget
- `cex_token_budget.py` provides the limit; compression_config defines the response
- Memory types from `cex_memory_types.py` map to preserve_types (CORRECTION = always keep)
