---
kind: architecture
id: bld_architecture_memory_summary
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of memory_summary — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - memory-summary-builder
  - p03_sp_memory_summary_builder
  - bld_collaboration_memory_summary
  - p11_qg_memory_summary
  - bld_instruction_memory_summary
  - bld_examples_memory_summary
  - p01_kc_memory_summary
  - bld_knowledge_card_memory_summary
  - p01_kc_memory_persistence
  - bld_schema_memory_summary
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| source_content | Raw input to be compressed (conversation turns, session log, document) | memory_summary | required |
| compression_engine | LLM or algorithm performing the compression pass | memory_summary | required |
| retention_policy | Rules declaring what survives compression (entities, decisions, actions) | memory_summary | required |
| trigger | Condition that fires the summarization pass | memory_summary | required |
| source_window | Number of turns/messages consumed per compression pass | memory_summary | required |
| output_buffer | Compressed summary text written to storage | memory_summary | required |
| freshness_tracker | Decay function reducing summary weight over time | P10 | external |
| injection_point | Runtime location where summary is prepended to LLM context | P02 | consumer |
| retrieval_index | Vector store indexing summaries for semantic lookup | P10 | consumer |
| session_state | Ephemeral cursor — separate artifact, NOT memory_summary | P10 | sibling |
| learning_record | Persistent learned pattern — separate artifact, NOT memory_summary | P10 | sibling |

## Dependency Graph
```
source_content    --feeds-->       compression_engine
retention_policy  --constrains-->  compression_engine
trigger           --activates-->   compression_engine
source_window     --scopes-->      compression_engine
compression_engine --produces-->   output_buffer
output_buffer      --consumed_by-> injection_point
output_buffer      --indexed_by->  retrieval_index
freshness_tracker  --weights-->    output_buffer
```

## Boundary Table
| memory_summary IS | memory_summary IS NOT |
|-------------------|----------------------|
| Reusable across sessions — persists in storage | Ephemeral per-run cursor (that is session_state) |
| Compressed representation of past context | Persistent learned behavioral pattern (that is learning_record) |
| Injected into context at runtime (llm_function: INJECT) | Static domain knowledge artifact (that is knowledge_card) |
| Produced by a compression pass (abstractive/extractive/hybrid/sliding_window) | Raw transcript or full session log |
| Has trigger threshold and retention policy | Immutable reference document |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| input | source_content, source_window | Define what is consumed per compression pass |
| compression | compression_engine, retention_policy | Perform reduction, enforce what survives |
| activation | trigger | Determine when compression fires |
| output | output_buffer, freshness_tracker | Store result, track relevance decay |
| consumption | injection_point, retrieval_index | Deliver summary to runtime consumers |

## Sibling Differentiation
| Artifact | Lifecycle | llm_function | Scope |
|----------|-----------|--------------|-------|
| memory_summary | Persistent, reusable | INJECT | Compressed past context |
| session_state | Ephemeral, per-run | SNAPSHOT | Current runtime cursor |
| learning_record | Permanent, immutable | TEACH | Extracted behavioral pattern |
| knowledge_card | Static, reference | INJECT | Domain facts and specs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[memory-summary-builder]] | downstream | 0.50 |
| [[p03_sp_memory_summary_builder]] | downstream | 0.49 |
| [[bld_collaboration_memory_summary]] | downstream | 0.41 |
| [[p11_qg_memory_summary]] | downstream | 0.41 |
| [[bld_instruction_memory_summary]] | upstream | 0.37 |
| [[bld_examples_memory_summary]] | upstream | 0.35 |
| [[p01_kc_memory_summary]] | downstream | 0.33 |
| [[bld_knowledge_card_memory_summary]] | upstream | 0.31 |
| [[p01_kc_memory_persistence]] | upstream | 0.30 |
| [[bld_schema_memory_summary]] | downstream | 0.28 |
