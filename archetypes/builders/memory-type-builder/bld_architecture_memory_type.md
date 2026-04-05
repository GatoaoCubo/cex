---
kind: architecture
id: bld_architecture_memory_type
pillar: P08
llm_function: INJECT
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
