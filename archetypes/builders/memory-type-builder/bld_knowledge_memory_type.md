---
kind: knowledge_card
id: bld_knowledge_card_memory_type
pillar: P01
llm_function: INJECT
quality: 9.1
title: "Knowledge Card Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_system_prompt_memory_type
  - bld_architecture_memory_type
  - p01_kc_memory_type
  - bld_examples_memory_type
  - bld_output_template_memory_type
  - bld_memory_memory_type
  - bld_tools_memory_type
  - bld_instruction_memory_type
  - p01_kc_memory_management
  - bld_schema_memory_type
---

# Knowledge Card: memory_type

## Taxonomy

| Type | Decay | Compact | Signal Words | Example |
|------|-------|---------|-------------|---------|
| correction | 0.00 | keep | "not X", "actually", "wrong", "use Y instead" | "Use YAML not JSON" |
| preference | 0.01 | keep | "I prefer", "I like", "please use" | "Prefer bullet lists" |
| convention | 0.02 | keep | "we always", "standard", "project uses" | "Black formatter" |
| context | 0.05 | drop | "today", "right now", "currently", "this session" | "Auth module today" |

## Classification Priority

| Priority | Test | Result |
|----------|------|--------|
| 1 | Contradicts previous agent output? | correction |
| 2 | Expresses subjective style choice? | preference |
| 3 | Describes repeatable project pattern? | convention |
| 4 | Time-bound or session-specific? | context |
| 5 | Ambiguous? | convention (safe default) |

## Decay Formula

```
confidence_new = max(0.0, confidence_old - decay_rate)
if confidence_new < 0.1: prune()  # MIN_CONFIDENCE
```

## Anti-Patterns

| Anti-Pattern | Why Bad | Fix |
|-------------|---------|-----|
| LLM observations as corrections | Only USER can correct | Gate: source must be user |
| Zero decay for everything | Memory bloat | Assign types strictly |
| No classification | Stale context in prompt | Use should_save() gate |
| Storing full LLM responses | Bloat bld_memory files | Store summary + type only |

## Integration Map

| Tool | Reads | Writes |
|------|-------|--------|
| cex_memory_types.py | - | MemoryType enum, should_save() |
| cex_memory_update.py | decay_rate per type | bld_memory_*.md |
| cex_memory_select.py | age + type for ranking | selection cache |
| cex_crew_runner.py | type labels + freshness | prompt injection |
| cex_memory_age.py | type-specific decay rate | freshness_score float |
| cex_8f_runner.py | memory via F3 INJECT | enriched context |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_memory_type]] | downstream | 0.47 |
| [[bld_architecture_memory_type]] | downstream | 0.42 |
| [[p01_kc_memory_type]] | sibling | 0.37 |
| [[bld_examples_memory_type]] | downstream | 0.37 |
| [[bld_output_template_memory_type]] | downstream | 0.32 |
| [[bld_memory_memory_type]] | downstream | 0.29 |
| [[bld_tools_memory_type]] | downstream | 0.28 |
| [[bld_instruction_memory_type]] | downstream | 0.27 |
| [[p01_kc_memory_management]] | sibling | 0.23 |
| [[bld_schema_memory_type]] | downstream | 0.23 |
