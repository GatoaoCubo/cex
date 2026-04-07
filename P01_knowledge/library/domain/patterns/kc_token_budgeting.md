---
id: p01_kc_token_budgeting
kind: knowledge_card
type: domain
pillar: P01
title: "Token Budgeting"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, token-budget, context-window, allocation, priority]
tldr: "Allocate context window like a financial budget. System prompt (never trim) > task > manifest > brand > KC > examples. Track spend, enforce limits, trim lowest priority first."
when_to_use: "When composing prompts for any model, especially multi-source prompts (ISOs + memory + context) that risk exceeding window limits."
keywords: [token-budget, context-window, allocation, priority, prompt-composition]
density_score: 0.95
---

# Token Budgeting

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Allocate context window slots by priority; trim from bottom up |
| Trigger | Every prompt composition, especially cex_crew_runner.py calls |
| Benefit | Maximum information density within model limits |
| Risk if skipped | Context overflow, lost instructions, degraded output |

## Priority Allocation

| Priority | Component | Budget Share | Trimmable? |
|----------|-----------|-------------|-----------|
| 1 (highest) | System prompt | 15–20% | **Never** |
| 2 | Current task / user message | 20–30% | **Never** |
| 3 | Decision manifest (GDP) | 5–10% | **Never** |
| 4 | Brand context | 5–8% | Last resort |
| 5 | Knowledge cards (relevant) | 10–20% | If needed |
| 6 | Memory (learning records) | 5–10% | By age/relevance |
| 7 | Examples / few-shot | 5–15% | **First to trim** |
| 8 | Conversation history | Remainder | Summarize progressively |

## Model Budget Reference

| Model | Total Window | Usable (80%) | System+Task Floor | Available for Context |
|-------|-------------|-------------|-------------------|---------------------|
| Claude Opus (1M) | 1,000,000 | 800,000 | 200,000 | 600,000 |
| Claude Sonnet (200K) | 200,000 | 160,000 | 50,000 | 110,000 |
| GPT-4o (128K) | 128,000 | 102,000 | 30,000 | 72,000 |
| Gemini Pro (1M) | 1,000,000 | 800,000 | 200,000 | 600,000 |

## Trimming Strategy

| Step | Action | Tokens Freed |
|------|--------|-------------|
| 1 | Remove few-shot examples beyond first 2 | 2K–10K |
| 2 | Summarize conversation history | 5K–50K |
| 3 | Reduce KCs to tldr-only mode | 3K–15K |
| 4 | Drop lowest-relevance memory entries | 2K–8K |
| 5 | Compress brand context to essentials | 1K–3K |
| 6 | **Never**: truncate system prompt or task | — |

## Budget Tracking

| Metric | How | Tool |
|--------|-----|------|
| Input tokens used | Count before API call | `cex_token_budget.py` |
| Output tokens expected | Estimate from task type | Heuristic (task → output ratio) |
| Budget remaining | Total – input – expected output | Calculated |
| Overspend alert | Budget remaining < 10% | Warning in compose step |

## Composition Example

```
Model: Claude Opus (1M tokens)
  System prompt:           45,000 tokens (4.5%)
  Task description:        12,000 tokens (1.2%)
  Decision manifest:        3,000 tokens (0.3%)
  Brand context:            5,000 tokens (0.5%)
  13 Builder ISOs:         85,000 tokens (8.5%)
  Relevant KCs (top 5):   20,000 tokens (2.0%)
  Memory (recent 10):      8,000 tokens (0.8%)
  Examples (2 golden):    15,000 tokens (1.5%)
  Conversation history:   40,000 tokens (4.0%)
  ─────────────────────────────────────────
  Total input:           233,000 tokens (23.3%)
  Available for output:  767,000 tokens ✓
```

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| No budget tracking | Discover overflow only when API rejects the call |
| Uniform allocation | Giving everything equal share wastes priority slots |
| Trimming system prompt | Breaks agent behavior fundamentally |
| Loading all KCs | 123 KCs × 4KB = 492KB — instant overflow |
| Ignoring output budget | Input fills window, no room for response |

## Linked Artifacts

- `p01_kc_context_overflow` — what happens when budget is exceeded
- `p01_kc_memory_management` — memory tier determines budget priority
- `p01_kc_query_decomposition` — split queries to distribute budget across sub-calls
