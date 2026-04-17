---
id: p02_memory_scope
kind: memory_scope
pillar: P02
version: 1.0.0
title: "Template — Memory Scope"
tags: [template, memory, scope, context, retention]
tldr: "Defines what an agent remembers and for how long. Controls context window budget, retention policy, and eviction strategy for different memory tiers."
quality: 9.0
domain: "model configuration"
density_score: 0.85
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
---

# Memory Scope: [SCOPE_NAME]

## Purpose
[WHAT this memory scope controls — which agent/system uses it, what decisions depend on memory]

## Tiers

| Tier | Retention | Size | Content |
|------|-----------|------|---------|
| Working | Current session | [2K-8K tokens] | Active task state, current intent |
| Short-term | [1h-24h] | [4K-16K tokens] | Recent interactions, partial results |
| Long-term | [30d-forever] | [unlimited, indexed] | Learning records, preferences, patterns |
| Episodic | Per-task | [1K-4K tokens] | Task-specific context, injected on demand |

## Context Window Budget
```yaml
total_budget: [8192 | 16384 | 32768] tokens
allocation:
  system_prompt: [500-2000] tokens   # Fixed, always present
  memory_inject: [1000-4000] tokens  # From long-term retrieval
  task_context:  [2000-8000] tokens  # Current task + history
  output_buffer: [1000-4000] tokens  # Reserved for generation
```

## Retention Policy
- **Write trigger**: [on_task_complete | on_session_end | on_quality_threshold]
- **What to store**: [learning_records | preferences | errors | all]
- **What to evict**: [oldest | lowest_relevance | lowest_quality]
- **Compression**: [summarize_after_N_entries | merge_similar | none]

## Eviction Strategy
When memory exceeds budget:
1. Score each entry by `relevance * recency * quality`
2. Evict lowest-scored entries until within budget
3. Never evict: [PROTECTED_ENTRIES — e.g., axioms, identity]
4. Log evicted entries to `.cex/learning_records/` for audit

## Injection Pattern
How memory is injected into the agent's context:
```
# MEMORY (from long-term store)
## Recent Learnings
- [LEARNING_1 — from bld_memory]
- [LEARNING_2 — from learning_records]
## Preferences
- [PREFERENCE_1 — user or domain specific]
```

## Quality Gate
- [ ] Total budget ≤ model context window
- [ ] Output buffer ≥ 1000 tokens (enough for generation)
- [ ] Retention policy defined (what and when)
- [ ] Eviction strategy handles budget overflow
- [ ] Protected entries identified
