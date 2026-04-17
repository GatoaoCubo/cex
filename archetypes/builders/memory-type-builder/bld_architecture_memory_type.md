---
kind: architecture
id: bld_architecture_memory_type
pillar: P08
llm_function: CONSTRAIN
quality: 9.0
title: "Architecture Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Architecture: memory_type

| Layer | Component | Role | Wire |
|-------|-----------|------|------|
| Input | cex_crew_runner.py | Produces observations from builder runs | W7 |
| Gate | cex_memory_types.should_save() | Reject duplicate/trivial, classify type | T05 |
| Store | cex_memory_update.append() | Type-aware decay + dedup filter | T05 |
| Rank | cex_memory_select._select_via_keywords() | Age*confidence*overlap scoring | T06 |
| Inject | cex_crew_runner._load_builder_memories() | Type labels + freshness caveats | T07 |
| Compact | cex_prompt_layers.check_compaction_needed() | Drop context type at 85% budget | W6 |

## Data Flow

```
obs -> should_save(obs, ctx) -> [reject | classify(correction|preference|convention|context)]
  -> append(type, decay) -> bld_memory_*.md -> select(query, age) -> prompt
```

## Invariants

| Rule | Detail |
|------|--------|
| Max types | 4 (correction/preference/convention/context) |
| Decay rates | Fixed per type: 0.00 / 0.01 / 0.02 / 0.05 |
| Compaction | correction=KEEP, preference=KEEP, convention=KEEP, context=DROP |
| Classifier | Heuristic-first (keyword), LLM-fallback (budget-aware) |
| Prune | confidence < 0.1 -> auto-remove on next update cycle |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target
