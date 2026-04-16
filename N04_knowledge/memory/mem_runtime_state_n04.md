---
id: mem_runtime_state_n04
kind: runtime_state
pillar: P10
nucleus: n04
title: N04 Runtime State
version: "1.0.0"
quality: null
tags: [runtime_state, n04, routing, memory, knowledge_gluttony]
agent: n04_knowledge
persistence: cross_session
domain: rag_indexing_taxonomy_memory
tldr: "Runtime routing state for N04 while it decides what to ingest, structure, vectorize, and remember."
routing_mode: hybrid
priority_count: 5
update_frequency: per_task
fallback_agent: n07_orchestrator
density_score: 0.94
constraint_count: 5
linked_artifacts:
  primary: N04_knowledge/agent_card_n04.md
  related: [kno_embedder_provider_n04, kno_knowledge_graph_n04, kno_vector_store_n04, mem_learning_record_n04]
---
<!-- 8F: F1=runtime_state/P10 F2=runtime-state-builder F3=nucleus_def_n04+agent_card_n04+kc_runtime_state+N04 configs/schemas F4=runtime decision map for knowledge routing, retrieval, and memory persistence
     F5=shell,apply_patch,cex_compile F6=author markdown artifact F7=frontmatter+routing-decision coherence+ascii+self-check F8=N04_knowledge/memory/mem_runtime_state_n04.md -->
# Agent Context
N04 operates at the point where raw repository content becomes indexed knowledge, structured relations, and durable memory.
Knowledge Gluttony at runtime means preferring to capture useful evidence, relation candidates, and retrieval hints before discarding them.
The counterweight is governance: N04 narrows aggressively by pillar, kind, provenance, and storage boundary before persisting anything.

## Routing Rules
| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| `knowledge_first` | incoming task defines facts, retrieval, graphing, chunking, or taxonomy | keep work in N04 and classify by kind | `0.95` |
| `memory_boundary` | content describes learned behavior, runtime routing, or persistence strategy | route to P10 memory artifact path | `0.93` |
| `research_boundary` | task demands external fact-finding rather than repository structuring | route outward to research owner | `0.88` |
| `build_boundary` | task is mostly code scaffold or implementation | keep references, route execution to build owner | `0.86` |
| `graph_upgrade` | flat retrieval is insufficient for relation-heavy questions | activate graph framing and hybrid retrieval | `0.90` |
| `filter_before_search` | corpus is broad or noisy | apply metadata filters before semantic expansion | `0.97` |

## Decision Tree
```text
task enters N04
  |- if asks for knowledge or memory artifact -> identify pillar and kind
  |- if asks for external research -> route to intelligence owner
  |- if asks for software implementation -> hand context to build owner
  |- if asks for retrieval architecture -> choose embedder + store + graph path
  \- otherwise -> ask whether the unit should be known, remembered, or routed away
```

## Priorities
1. Retrieval usefulness - every artifact should improve future findability, not just satisfy current wording.
2. Boundary integrity - P01 knowledge, P10 memory, and external domains must stay separable.
3. Provenance density - explicit references to local contracts and examples beat vague generality.
4. Cross-artifact coherence - embedder, vector store, graph, and memory should tell one system story.
5. Delivery discipline - exact filenames, 8F trace placement, and compile steps remain mandatory.

## Heuristics
| Heuristic | When | Confidence |
|-----------|------|------------|
| prefer the narrower kind | the request could fit multiple artifact families | `high` |
| keep one semantic stack | multiple retrieval artifacts are authored together | `high` |
| graph only when relations matter | the question is answerable by flat similarity alone | `medium` |
| preserve local terminology | repository examples provide vocabulary already | `high` |
| treat runtime notes as memory only if they should survive reuse | state looks ephemeral or session-specific | `high` |

## Tools Available
| Tool | Runtime use |
|------|-------------|
| `shell_command` | inspect local contracts, examples, and compile results |
| `apply_patch` | create or revise artifacts without unsafe editing patterns |
| `cex_compile.py` | compile authored markdown into derived outputs |
| `rg` | locate builders, kind KCs, and existing examples quickly |

## Constraints
1. Do not commit during this handoff wave.
2. Keep identifiers and code fields ASCII-safe.
3. Place the 8F trace immediately below closing frontmatter.
4. Preserve the exact output paths named by the handoff.
5. Do not confuse runtime state with mental model or session snapshot.

## State Transitions
| Trigger | From | To | Condition |
|---------|------|----|-----------|
| `new_handoff` | `idle` | `constraining` | a task arrives with mission metadata |
| `contracts_loaded` | `constraining` | `injecting` | schema, builders, and examples are available |
| `draft_plan_ready` | `injecting` | `producing` | enough local evidence exists to write safely |
| `draft_saved` | `producing` | `governing` | all target files exist |
| `compile_passed` | `governing` | `complete` | compilation succeeds or is acceptably skipped |

## Active Signals
| Signal | Meaning | Response |
|--------|---------|----------|
| `schema_gap` | builder fields and handoff naming do not line up perfectly | adapt frontmatter while preserving requested path |
| `density_risk` | body length increases but signal density drops | compress filler and expand operational tables |
| `boundary_risk` | content starts mixing knowledge and memory roles | split into P01 and P10 language immediately |
| `coherence_risk` | retrieval artifacts disagree on dimensions or backend logic | normalize around one canonical stack |

## Update Triggers
1. Update when a new builder changes section expectations for N04 kinds.
2. Update when the canonical embedder or vector backend changes.
3. Update when graph retrieval becomes first-class instead of sidecar.
4. Update when new validators enforce stronger frontmatter or byte constraints.
5. Update after any repeated reviewer comment about routing or memory boundaries.

## Fallback
If kind selection remains ambiguous after schema review, N04 defaults to the stricter interpretation and documents the boundary in the body.
If a requested filename conflicts with canonical naming patterns, N04 preserves the handoff path and makes the frontmatter internally consistent.
If compilation reveals format issues, N04 fixes the source artifact rather than loosening the runtime rules.

## References
1. `archetypes/builders/runtime-state-builder/bld_instruction_runtime_state.md`
2. `P01_knowledge/library/kind/kc_runtime_state.md`
3. `N04_knowledge/agent_card_n04.md`
4. `N04_knowledge/architecture/nucleus_def_n04.md`
5. `N04_knowledge/config/con_env_config_n04.md`

## Properties
| Property | Value |
|----------|-------|
| Kind | `runtime_state` |
| Pillar | `P10` |
| Nucleus | `n04` |
| Agent | `n04_knowledge` |
| Persistence | `cross_session` |
| Routing mode | `hybrid` |
| Priority count | `5` |
| Constraint count | `5` |
| Update frequency | `per_task` |
| Fallback agent | `n07_orchestrator` |
