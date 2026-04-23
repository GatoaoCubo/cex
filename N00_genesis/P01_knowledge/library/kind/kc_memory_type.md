---
id: p01_kc_memory_type
kind: knowledge_card
type: kind
pillar: P10
title: "Memory Type -- Deep Knowledge for memory_type"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: memory_type
quality: 9.1
tags: [memory_type, P10, INJECT, kind-kc]
tldr: "Classification of persistent memory by source, confidence, and decay rate"
when_to_use: "Building, reviewing, or reasoning about memory_type artifacts"
keywords: [memory, classification, decay, confidence, persistence]
feeds_kinds: [memory_type, entity_memory, memory_scope, memory_summary]
density_score: null
related:
  - bld_system_prompt_memory_type
  - bld_knowledge_card_memory_type
  - p01_kc_memory_scope
  - bld_examples_memory_type
  - bld_schema_memory_type
  - bld_collaboration_memory_type
  - bld_output_template_memory_type
  - p01_kc_memory_management
  - bld_memory_memory_type
  - SPEC_04_memory_system
---

# Memory Type

## Spec
```yaml
kind: memory_type
pillar: P10
llm_function: INJECT
max_bytes: 2048
naming: p10_mt_{{type_name}}.yaml
core: false
```

## What It Is
A memory type defines a classification category for persistent memories with specific
decay rates, confidence thresholds, and storage policies. It is NOT an entity_memory
(a specific memory instance) nor a memory_scope (who can access memories). A memory
type answers "what KIND of memory is this and how should it age?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ChatMessageHistory` types | Different history types for different contexts |
| LlamaIndex | `BaseMemory` subclasses | Short-term vs long-term memory stores |
| CrewAI | `memory_type` in Agent config | short_term, long_term, entity types |
| AutoGen | `teachable_agent` categories | Facts, preferences, instructions |
| OpenClaude | `memoryTypes.ts` taxonomy | preference, convention, context, correction |
| MemGPT | `core_memory` vs `archival_memory` | Different persistence and access patterns |

## Taxonomy (from OpenClaude production)
| Type | Decay Rate | Priority | Save When |
|------|-----------|----------|-----------|
| correction | 0.00 (permanent) | HIGHEST | User corrects agent behavior |
| preference | 0.02 (slow) | HIGH | User states a preference |
| convention | 0.03 (moderate) | MEDIUM | Undocumented pattern discovered |
| context | 0.05 (fast) | LOW | Significant decision made |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| decay_rate | float | 0.03 | Faster decay = fresher memories but loses history |
| confidence | float | 0.5 | Higher threshold = fewer but more reliable memories |
| max_entries | int | 20 | More entries = richer context but more tokens consumed |
| save_trigger | enum | observed | explicit (user says remember) vs observed (agent infers) |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Permanent (decay=0) | Corrections, explicit user preferences | "Never use tabs, always spaces" |
| Slow decay (0.01-0.02) | User preferences, coding style | "Prefers Portuguese for comments" |
| Moderate decay (0.03) | Project conventions | "This repo uses pytest not unittest" |
| Fast decay (0.05+) | Task context, temporary decisions | "Currently refactoring the auth module" |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| All memories permanent | Context window bloat, stale info | Apply decay rates by type |
| No type classification | Cannot prioritize or prune | Classify on save |
| Saving raw tool output | Wastes tokens on noise | Save the insight, not the data |
| No deduplication | Same memory saved repeatedly | Check existing before creating |

## Integration Graph
```
[memory_type] --> [entity_memory] --> [memory_summary]
      |                                     |
      v                                     v
[memory_scope]                    [session_state]
```

## Quality Criteria
- GOOD: Type has decay rate, confidence threshold, and save trigger defined
- GREAT: Includes deduplication rules, max entries, and pruning policy
- FAIL: No decay rate, no classification criteria, saves everything

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_memory_type]] | upstream | 0.44 |
| [[bld_knowledge_card_memory_type]] | sibling | 0.40 |
| [[p01_kc_memory_scope]] | sibling | 0.35 |
| [[bld_examples_memory_type]] | upstream | 0.34 |
| [[bld_schema_memory_type]] | related | 0.32 |
| [[bld_collaboration_memory_type]] | downstream | 0.32 |
| [[bld_output_template_memory_type]] | upstream | 0.31 |
| [[p01_kc_memory_management]] | sibling | 0.30 |
| [[bld_memory_memory_type]] | related | 0.30 |
| [[SPEC_04_memory_system]] | upstream | 0.30 |
