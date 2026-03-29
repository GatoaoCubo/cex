---
kind: architecture
id: bld_architecture_memory_summary
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of memory_summary — inventory, dependencies, and architectural position
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
| From | To | Type | Data |
|------|----|------|------|
| source_content | compression_engine | feeds | raw turns/tokens to compress |
| retention_policy | compression_engine | constrains | what must survive in output |
| trigger | compression_engine | activates | fires pass when threshold crossed |
| source_window | compression_engine | scopes | limits input slice per pass |
| compression_engine | output_buffer | produces | compressed summary text |
| output_buffer | injection_point | consumed_by | summary prepended to LLM prompt |
| output_buffer | retrieval_index | indexed_by | summary embedded for semantic search |
| freshness_tracker | output_buffer | weights | decay reduces relevance score over time |

## Boundary Table
| memory_summary IS | memory_summary IS NOT |
|-------------------|----------------------|
| Reusable across sessions — persists in storage | Ephemeral per-run cursor (that is session_state) |
| Compressed representation of past context | Persistent learned behavioral pattern (that is learning_record) |
| Injected into context at runtime (llm_function: INJECT) | Static domain knowledge artifact (that is knowledge_card) |
| Produced by a compression pass (abstractive/extractive/hybrid/sliding_window) | Raw transcript or full session log |
| Has trigger threshold and retention policy | A real-time streaming buffer |
| Decays in relevance over time (freshness_decay) | Immutable reference document |

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
