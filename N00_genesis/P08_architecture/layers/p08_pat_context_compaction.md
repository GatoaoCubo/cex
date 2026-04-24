---
id: p08_pat_context_compaction
kind: pattern
8f: F4_reason
pillar: P08
title: "Pattern: Context Compaction Strategy"
version: 1.0.0
quality: 9.1
tags: [pattern, context, compaction, memory, optimization]
tldr: "Architectural pattern for managing context window limits. Defines 4-level compaction strategy with preservation rules and trigger thresholds."
domain: "architecture"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.92
related:
  - p04_skill_compact
  - kc_model_context_protocol
  - p10_rs_conversation
  - p01_kc_context_overflow
  - p01_kc_memory_management
  - p01_kc_memory_summary
  - bld_memory_session_state
  - p01_kc_token_budgeting
  - bld_knowledge_card_context_doc
  - bld_schema_session_backend
---

# Context Compaction Pattern

## Problem
LLM agents accumulate context during long sessions. As the context window
fills, performance degrades and eventually the session must be compressed
or restarted. Uncontrolled compaction loses critical information.

## Solution
A 4-level progressive compaction strategy that preserves high-value
information while aggressively pruning low-value content.

## Architecture

```
Context Window [============================----] 80% threshold
                    |
                    v
            Compaction Engine
            ├── L1: Trim redundancy (10-20% savings)
            ├── L2: Summarize history (20-40% savings)
            ├── L3: Drop low-value (30-50% savings)
            └── L4: Critical-only (50-70% savings)
```

## Trigger Thresholds

| Usage | Action | Automatic? |
|-------|--------|-----------|
| < 60% | No action | -- |
| 60-80% | Monitor, warn | Yes |
| 80-90% | L1 + L2 compaction | Yes |
| 90-95% | L3 compaction | Yes |
| > 95% | L4 emergency compaction | Yes |

## Preservation Priority

1. Current task + requirements (NEVER compact)
2. Uncommitted changes (NEVER compact)
3. Active error context (NEVER compact)
4. User decisions this session (NEVER compact)
5. Recent tool results (compact after use)
6. Historical conversation (compact aggressively)
7. Exploration results (drop if superseded)

## Trade-offs

| Benefit | Cost |
|---------|------|
| Extends session lifetime | May lose useful historical context |
| Maintains performance | Summarization introduces information loss |
| Automatic operation | Requires careful priority tuning |

## Related Patterns

- Memory Extraction: persist valuable context before compaction
- Token Budget: pre-allocate context regions by function
- Prompt Cache: reuse cached prefixes to reduce context pressure

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_skill_compact]] | upstream | 0.45 |
| [[kc_model_context_protocol]] | upstream | 0.28 |
| [[p10_rs_conversation]] | downstream | 0.27 |
| [[p01_kc_context_overflow]] | upstream | 0.22 |
| [[p01_kc_memory_management]] | upstream | 0.21 |
| [[p01_kc_memory_summary]] | downstream | 0.21 |
| [[bld_memory_session_state]] | downstream | 0.20 |
| [[p01_kc_token_budgeting]] | upstream | 0.20 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.19 |
| [[bld_schema_session_backend]] | upstream | 0.19 |
