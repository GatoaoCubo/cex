---
id: p03_cwc_n05_sonnet
kind: context_window_config
pillar: P03
title: "N05 Sonnet 200K Context Budget"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "context-window-config-builder"
target_model: claude-sonnet-4-6
total_tokens: 200000
system_prompt_budget: 20000
few_shot_budget: 20000
retrieved_context_budget: 33000
user_query_budget: 100000
output_reserve: 27000
overflow_strategy: compress
priority_tiers: [system, query, context, examples]
domain: operations
quality: null
tags: [context_window_config, n05, operations, token-budget]
tldr: "N05 200K: 50% working-memory, 13.5% tool-buf, 16.5% context, 10% ISOs, 10% system"
---

## Budget Allocation

| Section | Tokens | % | P |
|---|---|---|---|
| System prompt + rules | 15000 | 7.5 | 1 |
| Agent card + nucleus_def | 5000 | 2.5 | 2 |
| Builder ISOs | 20000 | 10.0 | 3 |
| Knowledge cards | 15000 | 7.5 | 4 |
| Handoff + mission context | 10000 | 5.0 | 5 |
| Vocabulary KC | 5000 | 2.5 | 6 |
| Brand config | 3000 | 1.5 | 7 |
| Working memory | 100000 | 50.0 | 8 |
| Tool results buffer | 20000 | 10.0 | 9 |
| Safety margin | 7000 | 3.5 | -- |
| **Total** | **200000** | **100** | -- |

## Priority Tiers

| P | Sections | Drop Rule |
|---|---|---|
| 1 | rules + agent card | Never -- Gating Wrath lens |
| 2 | handoff + vocab KC | Never -- task definition |
| 3 | KCs + brand + ISOs | Brand first, then lowest TF-IDF |
| 4 | working memory | Rolling summary of oldest turns |

## Overflow Rules

| Step | Trigger | Action | Freed |
|---|---|---|---|
| 1 | >= 160K | Summarize tool results > 3 turns old | ~10K |
| 2 | still over | Compress conversation > last 20 turns | ~20K |
| 3 | still over | Drop brand config | 3K |
| 4 | still over | Drop lowest TF-IDF KC | ~5K |
| HALT | tiers 1+2 at risk | Signal N07 and abort | -- |

## Model Profile

| Property | Value |
|---|---|
| Model | claude-sonnet-4-6 / 200K |
| Sin lens | Gating Wrath -- fail-closed |
| Consumers | `cex_token_budget.py` `cex_skill_loader.py` |
| Validator | `cex_compile.py` |
