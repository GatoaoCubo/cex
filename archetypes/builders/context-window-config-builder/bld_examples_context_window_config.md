---
kind: examples
id: bld_examples_context_window_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of context_window_config artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: context-window-config-builder
## Golden Example
INPUT: "Create context window config for Claude Opus 200K with RAG-heavy workload"
OUTPUT:
```yaml
---
id: p03_cwc_opus_rag_heavy
kind: context_window_config
pillar: P03
title: "Claude Opus 200K — RAG-Heavy Profile"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "context-window-config-builder"
target_model: claude-opus-4-20250514
total_tokens: 200000
system_prompt_budget: 10000
few_shot_budget: 15000
retrieved_context_budget: 100000
user_query_budget: 5000
output_reserve: 32000
overflow_strategy: truncate_lowest
priority_tiers: [system, query, context, examples]
domain: llm_engineering
quality: null
tags: [context_window_config, opus, rag, token-budget]
tldr: "Opus 200K RAG-heavy: 50% context, 16% output, 5% system — priority truncation on overflow"
---
# Budget: system 5%, examples 7.5%, context 50%, query 2.5%, output 16%
# Remaining 19% unallocated (buffer for dynamic scaling)
```
WHY THIS IS GOLDEN:
- quality: null
- Budgets sum <= total_tokens (162K of 200K, with buffer)
- output_reserve >= 2000 (32K)
- priority_tiers present and ordered
- overflow_strategy is valid enum

## Anti-Example
BAD OUTPUT:
```yaml
id: window_config
total_tokens: 999999
system_prompt_budget: 500000
output_reserve: 100
quality: 9.0
```
FAILURES:
1. id: no p03_cwc_ prefix
2. total_tokens: exceeds any real model
3. output_reserve: too small (< 2000)
4. quality: not null
5. No priority_tiers or overflow_strategy
