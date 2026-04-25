---
id: component_map_n04
kind: component_map
8f: F4_reason
pillar: P08
nucleus: n04
title: "N04 Knowledge -- Component Map"
version: 1.0.0
created: 2026-04-18
author: n07_admin
domain: knowledge-rag-architecture
quality: 8.7
tags: [component_map, n04, knowledge, rag, architecture, data_flow]
tldr: "Internal component map of N04 Knowledge nucleus: RAG pipeline, KC library, chunk strategy, entity memory, vector store, and inter-nucleus data flows."
density_score: null
related:
  - agent_card_n04
  - self_audit_n04_codex_2026_04_15
  - p01_kc_cex_project_overview
  - p02_nd_n04.md
  - p01_kc_supabase_data_layer_n04
  - spec_n01_n04_verticalization
  - p06_arch_knowledge_graph
  - bld_architecture_supabase_data_layer
  - spec_cex_system_map
  - bld_collaboration_supabase_data_layer
---

# N04 Knowledge -- Component Map

## System Overview

N04 is the knowledge management and RAG nucleus. Its primary function is
organizing, indexing, retrieving, and evolving institutional knowledge.
All artifacts flow through 8F: CONSTRAIN kind/pillar -> BECOME librarian
-> INJECT existing KCs -> REASON on gaps -> CALL indexers -> PRODUCE KC/rag_source
-> GOVERN quality -> COLLABORATE via signal.

**Sin Lens**: Knowledge Gluttony -- insatiable hunger for facts, citations,
and context. Drives N04 to always fill gaps, never leave a KC stub uncompleted.

---

## Artifact Inventory

| Pillar | Count | Primary Kinds |
|--------|------:|---------------|
| P01 Knowledge | 21 | knowledge_card, rag_source, chunk_strategy, citation, glossary_entry |
| P02 Model | 7 | agent, boot_config, model_card, nucleus_def |
| P03 Prompt | 4 | system_prompt, prompt_template, prompt_cache |
| P04 Tools | 9 | search_tool, retriever, document_loader, db_connector |
| P05 Output | 26 | knowledge_card outputs, formatter, integration_guide |
| P06 Schema | 15 | input_schema, validation_schema, ontology, type_def |
| P07 Evals | 16 | quality_gate, benchmark, scoring_rubric, llm_judge |
| P08 Architecture | 7 | component_map, decision_record, context_map, naming_rule |
| P09 Config | 6 | env_config, rate_limit_config, path_config |
| P10 Memory | 19 | entity_memory, knowledge_index, memory_summary, user_model |
| P11 Feedback | 8 | guardrail, bugloop, learning_record, curation_nudge |
| P12 Orchestration | 8 | workflow, schedule, dispatch_rule, handoff |

**Total: 151 artifacts**

---

## Internal Components

### C1 -- RAG Pipeline
```
Input query / intent
  |
  v
[C1.1] Chunk Strategy   -- token budget, overlap policy
  |
  v
[C1.2] Embedder         -- embedder_provider + embedding_config
  |
  v
[C1.3] Vector Store     -- FAISS/pgvector (vector_store kind)
  |
  v
[C1.4] Retriever        -- retriever_config: top-k, reranker
  |
  v
[C1.5] Reranker         -- reranker_config: cross-encoder re-scoring
  |
  v
Ranked chunks -> F3 INJECT context
```

### C2 -- KC Library (source: N00_genesis)
```
300 KCs in N00_genesis/P01_knowledge/library/kind/kc_{kind}.md
  |
  +-- 21 local enriched KCs in N04_knowledge/P01_knowledge/
  +-- Graph KCs: kc_sdk_coverage_gap.md, kc_f3b_persist_gap.md
  +-- Indexed via cex_retriever.py (TF-IDF, 12K vocab)
```

### C3 -- Entity Memory
```
cex_memory_update.py --observation "{fact}"
  |
  v
entity_memory artifacts (SQLite + FTS5 via cex_user_model.py)
  |
  v
cex_memory_select.py (keyword + cosine retrieval at F3 INJECT)
```

### C4 -- Knowledge Graph
```
knowledge_graph_topology.md (N04/P08)
  |
  +-- ontology.md
  +-- domain_vocabulary per pillar
  +-- Traversal: cex_kind_deps.py (depends_on graph)
```

---

## Data Flows

| Source | -> | N04 | -> | Destination |
|--------|----|----|-----|-------------|
| N01 research output | -> | KC ingest | -> | N04/P01 library |
| N07 handoff | -> | task dispatch | -> | N04 8F run |
| N04 KC | -> | F3 INJECT | -> | All nuclei via cex_retriever.py |
| N04 entity_memory | -> | persistence | -> | .cex/runtime/memory/ |
| N04 signal | -> | F8 COLLABORATE | -> | N07 consolidation |

---

## Integration Points

| System | Kind | Protocol |
|--------|------|----------|
| N01 Intelligence | knowledge_card | Read KC, enrich, re-index |
| N07 Admin | handoff | Receive task; signal on complete |
| All nuclei | F3 INJECT | Serve KCs via cex_retriever.py |
| cex_memory_update | entity_memory | Write new entities post-run |
| cex_fts5_search | knowledge_index | FTS5 full-text search |

---

## Key Tools

| Tool | Function |
|------|----------|
| `cex_retriever.py` | TF-IDF KC similarity search |
| `cex_memory_select.py` | Entity memory injection |
| `cex_memory_update.py` | F3b persist + decay |
| `cex_fts5_search.py` | FTS5 full-text search (HERMES) |
| `cex_user_model.py` | Honcho-pattern user model (HERMES) |
| `cex_mirror_audit.py` | Fractal mirror enforcement |

---

## Gaps (from SELF_AUDIT)

| Gap | Severity | Status |
|-----|----------|--------|
| No knowledge_graph builder | HIGH | Builder exists (kind registered) |
| component_map missing until this file | MEDIUM | RESOLVED |
| entity_memory auto-persist not triggered per-run | HIGH | F3b wired in hooks |
| graph_rag_config builder | MEDIUM | Registered, needs ISO set |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n04]] | upstream | 0.40 |
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.38 |
| [[p01_kc_cex_project_overview]] | upstream | 0.31 |
| [[p02_nd_n04.md]] | upstream | 0.31 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.31 |
| [[spec_n01_n04_verticalization]] | upstream | 0.31 |
| [[p06_arch_knowledge_graph]] | upstream | 0.30 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.30 |
| [[spec_cex_system_map]] | upstream | 0.30 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.30 |
