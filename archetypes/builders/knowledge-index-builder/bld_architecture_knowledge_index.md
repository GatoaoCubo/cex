---
kind: architecture
id: bld_architecture_knowledge_index
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of knowledge_index — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - knowledge-index-builder
  - bld_collaboration_knowledge_index
  - p03_sp_knowledge_index_builder
  - bld_instruction_knowledge_index
  - p01_kc_knowledge_index
  - bld_architecture_rag_source
  - p11_qg_knowledge_index
  - bld_architecture_embedding_config
  - bld_architecture_knowledge_card
  - bld_knowledge_card_knowledge_index
---

# Architecture: knowledge_index in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, algorithm, scope, rebuild_schedule, etc.) | knowledge-index-builder | required |
| algorithm_config | Search algorithm selection: BM25, FAISS, or hybrid (BM25 + FAISS weighted blend) | author | required |
| scope_definition | Boundaries of what is indexed (which content types, pillars, or directories) | author | required |
| embedding_reference | Pointer to the embedding_config that produced the vectors in this index | embedding_config | required |
| ranking_strategy | Scoring formula: BM25 term weights, FAISS distance metric, hybrid fusion weights | author | required |
| filter_config | Pre-query filters (by pillar, type, tag, date range) to narrow retrieval scope | author | optional |
| rebuild_policy | Schedule and triggers for index refresh (time-based, content-change-based) | author | required |
| freshness_threshold | Maximum acceptable staleness before index is considered invalid | author | required |
## Dependency Graph
```
rag_source       --produces-->  knowledge_index  --queried_by-->  runtime_state
embedding_config --produces-->  knowledge_index  --indexes-->     knowledge_card
knowledge_index      --produces-->  retrieval_result
retrieval_result --produces-->  agent_context (injected via IHP)
knowledge_index      --signals-->   rebuild_trigger (when freshness_threshold exceeded)
```
| From | To | Type | Data |
|------|----|------|------|
| rag_source (P01) | knowledge_index | data_flow | raw content documents fed into the index |
| embedding_config (P01) | knowledge_index | data_flow | vector model spec (dimensions, chunk_size, model_id) |
| knowledge_index | knowledge_card (P01) | data_flow | indexed content returned as ranked retrieval results |
| knowledge_index | runtime_state (P10) | data_flow | query results that inform agent routing decisions |
| knowledge_index | retrieval_result | produces | ranked list of matching content with scores |
| retrieval_result | agent_context | data_flow | injected into prompt via IHP for grounded responses |
| freshness_threshold | rebuild_trigger | signals | staleness event triggers index rebuild job |
## Boundary Table
| knowledge_index IS | knowledge_index IS NOT |
|----------------|--------------------|
| A search infrastructure layer — configures how content is found | The content being indexed (knowledge_card) |
| A persistent index rebuilt on schedule or content change | An ephemeral session snapshot (session_state) |
| Algorithm configuration (BM25, FAISS, hybrid weights, filters) | The vector model that produces embeddings (embedding_config) |
| The mechanism for retrieval — finds ranked results from queries | The data source that provides raw content (rag_source) |
| Scoped by content type, pillar, or directory boundaries | A learning artifact that records what was learned (learning_record) |
| Infrastructure — does not store knowledge but makes it findable | An immutable fundamental rule (axiom) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Sources | rag_source, embedding_config | Feed raw content and vector representations into the index |
| Configuration | frontmatter, algorithm_config, ranking_strategy, filter_config | Define how content is indexed, scored, and filtered |
| Freshness | rebuild_policy, freshness_threshold, rebuild_trigger | Ensure index stays current with content changes |
| Query | scope_definition, embedding_reference | Constrain retrieval to relevant content with correct vector space |
| Output | retrieval_result, agent_context injection | Return ranked matches and deliver grounded context to agents |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-index-builder]] | downstream | 0.48 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.47 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.44 |
| [[bld_instruction_knowledge_index]] | upstream | 0.40 |
| [[p01_kc_knowledge_index]] | downstream | 0.40 |
| [[bld_architecture_rag_source]] | sibling | 0.39 |
| [[p11_qg_knowledge_index]] | downstream | 0.37 |
| [[bld_architecture_embedding_config]] | sibling | 0.33 |
| [[bld_architecture_knowledge_card]] | sibling | 0.32 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.32 |
