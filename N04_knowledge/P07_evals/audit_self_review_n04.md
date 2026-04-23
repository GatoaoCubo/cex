---
quality: 8.2
quality: 7.8
id: audit_self_review_n04
kind: audit_report
pillar: P07
nucleus: n04
mission: SELF_AUDIT
title: "N04 Knowledge Self-Audit: P01/P10 Coverage, RAG Pipeline, Memory, KC Quality"
version: 1.0.0
tags: [self-audit, knowledge, memory, rag, kc, 8f]
date: 2026-04-18
related:
  - bld_schema_bugloop
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_context_window_config
  - bld_schema_pitch_deck
  - bld_schema_search_strategy
  - p06_schema_a11y_checklist
  - bld_schema_repo_map
density_score: 1.0
updated: "2026-04-22"
---

## P01 + P10 Coverage Matrix

### P01 Knowledge (30 kinds)

| Pillar | Kind | Builder (ISOs) | KC Exists | KC Words | N04 Artifact | Gap |
|--------|------|----------------|-----------|----------|--------------|-----|
| P01 | agentic_rag | YES (13) | YES | 217w | p01_gl_rag.md | KC thin (<300w) |
| P01 | changelog | YES (13) | YES | 130w | -- | KC thin |
| P01 | chunk_strategy | YES (13) | YES | 576w | chunk_strategy_knowledge.md | -- |
| P01 | citation | YES (13) | YES | 627w | -- | No N04 impl artifact |
| P01 | competitive_matrix | YES (13) | YES | 347w | -- | No N04 impl artifact |
| P01 | context_doc | YES (13) | YES | 420w | -- | No N04 impl artifact |
| P01 | dataset_card | YES (13) | YES | 380w | -- | No N04 impl artifact |
| P01 | discovery_questions | YES (13) | YES | 290w | -- | No N04 impl artifact |
| P01 | domain_vocabulary | YES (13) | YES | 310w | kc_knowledge_vocabulary.md | -- |
| P01 | ecommerce_vertical | YES (13) | YES | 280w | -- | No N04 impl artifact |
| P01 | edtech_vertical | YES (13) | YES | 310w | -- | No N04 impl artifact |
| P01 | embedder_provider | YES (13) | YES | 333w | kno_embedder_provider_n04.md | -- |
| P01 | embedding_config | YES (13) | YES | 542w | embedding_config_knowledge.md | -- |
| P01 | faq_entry | YES (13) | YES | 105w | -- | KC thin |
| P01 | few_shot_example | YES (13) | YES | 340w | few_shot_examples_rag_queries.md | -- |
| P01 | fintech_vertical | YES (13) | YES | 171w | -- | KC thin |
| P01 | glossary_entry | YES (13) | YES | 360w | -- | No N04 impl artifact |
| P01 | govtech_vertical | YES (13) | YES | 290w | -- | No N04 impl artifact |
| P01 | graph_rag_config | YES (13) | YES | 263w | -- | No N04 impl artifact |
| P01 | healthcare_vertical | YES (13) | YES | 295w | -- | No N04 impl artifact |
| P01 | knowledge_card | YES (13) | YES | 740w | knowledge_card_knowledge.md | -- |
| P01 | knowledge_graph | YES (13) | YES | 695w | kno_knowledge_graph_n04.md | -- |
| P01 | legal_vertical | YES (13) | YES | 305w | -- | No N04 impl artifact |
| P01 | lineage_record | YES (13) | YES | 380w | -- | No N04 impl artifact |
| P01 | ontology | YES (13) | YES | 430w | -- | No N04 impl artifact |
| P01 | rag_source | YES (13) | YES | 582w | rag_source_knowledge.md | -- |
| P01 | repo_map | YES (13) | YES | 360w | -- | No N04 impl artifact |
| P01 | reranker_config | YES (13) | YES | 103w | -- | KC thin (<150w), no N04 impl |
| P01 | retriever_config | YES (13) | YES | 1002w | retriever_config_knowledge.md | -- |
| P01 | vector_store | YES (13) | YES | 362w | kno_vector_store_n04.md | -- |

**P01 Summary**: 30/30 builders exist (100%), all 30 with 13 ISOs each. 30/30 KCs exist.
Coverage gap: 54 KCs system-wide below 200 words; within P01 scope: agentic_rag (217w), reranker_config (103w), faq_entry (105w) are thinnest.
N04-specific implementation artifacts: 12/30 P01 kinds have a dedicated N04 artifact in P01_knowledge/. 18 kinds lack a wired N04 implementation artifact.

### P10 Memory (22 kinds)

| Pillar | Kind | Builder (ISOs) | KC Exists | KC Words | N04 Artifact | Gap |
|--------|------|----------------|-----------|----------|--------------|-----|
| P10 | agent_grounding_record | -- | YES | 126w | -- | Builder MISSING; KC thin |
| P10 | c2pa_manifest | -- | YES | 164w | -- | Builder MISSING; KC thin |
| P10 | compression_config | -- | YES | 220w | -- | Builder MISSING |
| P10 | consolidation_policy | -- | YES | 151w | consolidation_policy_n04.md | Builder MISSING; KC thin |
| P10 | entity_memory | YES (13) | YES | 689w | entity_memory_n04.md | -- |
| P10 | episodic_memory | YES (13) | YES | 653w | -- | No N04 impl artifact |
| P10 | knowledge_index | YES (13) | YES | 574w | knowledge_memory_index.md | -- |
| P10 | learning_record | YES (13) | YES | 607w | mem_learning_record_n04.md | -- |
| P10 | memory_architecture | YES (13) | YES | 274w | memory_architecture_n04.md | KC thin |
| P10 | memory_summary | YES (13) | YES | 689w | memory_summary_n04.md | -- |
| P10 | memory_type | YES (13) | YES | 567w | memory_type_n04.md | -- |
| P10 | model_registry | -- | YES | 148w | -- | Builder MISSING; KC thin |
| P10 | procedural_memory | YES (13) | YES | 152w | procedural_memory_n04.md | KC thin |
| P10 | prompt_cache | YES (13) | YES | 622w | -- | Routes to N05 (correct) |
| P10 | prospective_memory | YES (13) | YES | 618w | -- | No N04 impl artifact |
| P10 | runtime_state | YES (13) | YES | 729w | mem_runtime_state_n04.md | -- |
| P10 | session_backend | -- | YES | 380w | -- | Builder MISSING |
| P10 | session_state | YES (13) | YES | 749w | session_state_n04.md | -- |
| P10 | user_model | YES (13) | YES | 878w | user_model_n04.md | -- |
| P10 | vc_credential | -- | YES | 164w | -- | Builder MISSING; KC thin |
| P10 | workflow_run_crate | -- | YES | 290w | -- | Builder MISSING |
| P10 | working_memory | YES (13) | YES | 602w | -- | No N04 impl artifact |

**P10 Summary**: 15/22 builders exist (68%), 7 kinds have no builder (agent_grounding_record, c2pa_manifest, compression_config, consolidation_policy, model_registry, session_backend, vc_credential, workflow_run_crate).
All 22 KCs exist. N04 implementation artifacts: 12/22 kinds have a dedicated N04 memory artifact.

## RAG Pipeline Wiring

| Component | Builder | Archetypes ISOs | Tool Wired | N04 Artifact | Status | Gap |
|-----------|---------|-----------------|------------|--------------|--------|-----|
| RAG source ingest | rag-source-builder | 13 | -- | rag_source_knowledge.md | PARTIAL | No ingest tool in P04 |
| Chunk strategy | chunk-strategy-builder | 13 | -- | chunk_strategy_knowledge.md | PARTIAL | Spec exists, no runtime tool |
| Embedder provider | embedder-provider-builder | 13 | embedding_batch_processor_tool.md | kno_embedder_provider_n04.md | OK | -- |
| Embedding config | embedding-config-builder | 13 | -- | embedding_config_knowledge.md | PARTIAL | Config spec only |
| Vector store | vector-store-builder | 13 | -- | kno_vector_store_n04.md (Supabase) | PARTIAL | Supabase only; no other backends |
| Retriever | retriever-config-builder | 13 | retriever_n04.md | retriever_config_knowledge.md | OK | TF-IDF only (no semantic) |
| Reranker | reranker-config-builder | 13 | -- | -- | MISSING | No N04 reranker tool |
| Graph RAG | graph-rag-config-builder | 13 | -- | -- | MISSING | No implementation |
| Agentic RAG | agentic-rag-builder | 13 | -- | p01_gl_rag.md | STUB | Guideline only |
| Document loader | -- | -- | document_loader_n04.md | -- | OK | No builder (kind not in P01) |
| Search tool | -- | -- | search_tool_n04.md | -- | OK | No builder |
| Supabase data layer | -- | -- | supabase_data_layer_tool.md | -- | OK | Postgres-only |
| KC validator | -- | -- | kc_validator_tool.md | -- | OK | -- |

**RAG Pipeline Retriever**: `cex_retriever.py` uses TF-IDF (cosine similarity, 22722-term vocab, 4992 docs indexed, built 2026-04-16). Algorithm: bag-of-words TF-IDF with English+Portuguese stopword removal, 3-char minimum token length. **No semantic/neural embeddings in production retriever** -- vector store exists as a spec but TF-IDF is the live engine.

**Critical gap**: retriever is lexical-only. No embedding pipeline is wired end-to-end (embedder_provider -> vector_store -> retrieval). The Supabase data layer exists but is not connected to the live TF-IDF retriever.

## Memory System Status

| Kind | Builder | N04 Implementation | Tool | Sub-agent (`.claude/agents/`) | Status |
|------|---------|-------------------|------|-------------------------------|--------|
| entity_memory | YES (13) | entity_memory_n04.md | cex_memory_select.py | -- | ACTIVE |
| knowledge_index | YES (13) | knowledge_memory_index.md | cex_retriever.py | -- | ACTIVE |
| learning_record | YES (13) | mem_learning_record_n04.md | cex_memory_update.py | -- | ACTIVE |
| memory_summary | YES (13) | memory_summary_n04.md | cex_memory_select.py | -- | ACTIVE |
| memory_type | YES (13) | memory_type_n04.md | cex_memory_types.py | -- | ACTIVE |
| procedural_memory | YES (13) | procedural_memory_n04.md | -- | -- | PARTIAL |
| working_memory | YES (13) | -- | -- | -- | STUB |
| episodic_memory | YES (13) | -- | -- | episodic-memory-builder.md | STUB |
| prospective_memory | YES (13) | -- | -- | prospective-memory-builder.md | STUB |
| memory_architecture | YES (13) | memory_architecture_n04.md | -- | -- | PARTIAL |
| runtime_state | YES (13) | mem_runtime_state_n04.md | -- | -- | ACTIVE |
| session_state | YES (13) | session_state_n04.md | -- | -- | ACTIVE |
| user_model | YES (13) | user_model_n04.md | -- | -- | ACTIVE |
| prompt_cache | YES (13) | -- | cex_prompt_cache.py | -- | N05 domain (correct routing) |
| agent_grounding_record | MISSING | -- | -- | -- | NOT STARTED |
| consolidation_policy | MISSING | consolidation_policy_n04.md | -- | -- | PARTIAL |
| model_registry | MISSING | -- | -- | -- | NOT STARTED |
| session_backend | MISSING | -- | -- | -- | NOT STARTED |
| working_memory_scope | YES (memory-scope-builder, 13) | memory_scope_n04.md | -- | -- | ACTIVE |

**Memory tools wired**: `cex_memory_select.py` (TF-IDF, zero-token retrieval), `cex_memory_update.py` (decay + prune: feedback=0.0, user=0.02, reference=0.03, project=0.05), `cex_memory_age.py` (freshness labels), `cex_memory_types.py` (4-type taxonomy: correction / preference / convention / context).

## KC Quality Sample

| KC File | Words | Sections (##) | Examples Refs | Score | Notes |
|---------|-------|---------------|---------------|-------|-------|
| kc_knowledge_card.md | 740 | 9 | 4 | 9.0 | Rich; covers definition, structure, use cases, anti-patterns |
| kc_rag_source.md | 582 | 9 | 1 | 7.5 | Good structure; only 1 example, needs more sample payloads |
| kc_entity_memory.md | 689 | 9 | 1 | 8.0 | Strong coverage; sparse examples |
| kc_retriever_config.md | 1002 | N/A | 5+ | 9.5 | Best in class; config tables, algorithm detail |
| kc_reranker_config.md | 103 | 1 | 1 | 2.5 | CRITICAL GAP -- single paragraph, no structure |
| kc_agentic_rag.md | 217 | 6 | 0 | 3.5 | Conceptual only; no implementation guidance |

**System-wide thin KCs**: 54 of 300 kind KCs are below 200 words (18%). P10 memory domain has high incidence of thin KCs: procedural_memory (152w), memory_architecture (274w). P01 RAG domain: reranker_config (103w), agentic_rag (217w) are critical gaps.

## Collaboration Map

| Nucleus | Direction | Knowledge Type | Mechanism |
|---------|-----------|----------------|-----------|
| N01 (Intelligence) | N01 -> N04 | Research findings, competitive intel | N01 produces knowledge_card; N04 indexes + enriches |
| N01 (Intelligence) | N04 -> N01 | Retrieved context, similar KCs | cex_retriever.py F3 INJECT injection |
| N02 (Marketing) | N04 -> N02 | Brand vocabulary, few-shot examples | F3 INJECT via domain_vocabulary + few_shot_example |
| N03 (Engineering) | N04 -> N03 | Architecture KCs, pattern KCs | F3 INJECT + knowledge_index |
| N03 (Engineering) | N03 -> N04 | Newly built artifacts | N03 saves; N04 indexes on next retriever build |
| N05 (Operations) | N04 -> N05 | Config KCs, deployment docs | F3 INJECT |
| N05 (Operations) | N05 -> N04 | prompt_cache artifacts | N05 owns P10 prompt_cache; feeds N04 index |
| N06 (Commercial) | N04 -> N06 | Vertical KCs (fintech, edtech, ecommerce) | F3 INJECT: P01 vertical KCs |
| N07 (Orchestrator) | N07 -> N04 | Handoffs, mission plans | .cex/runtime/handoffs/n04_task.md |
| N07 (Orchestrator) | N04 -> N07 | Audit reports, knowledge gaps | P07_evaluation/* + signals |
| ALL nuclei | N04 -> ALL | Builder ISOs, domain KCs | F2 BECOME + F3 INJECT at every build |

**Central role**: N04 is the read-write backbone of every nucleus's F3 INJECT step. The TF-IDF retriever (4992 docs, 22722 vocab) runs zero-token lookups for all context assembly. N04 is the only nucleus that serves knowledge TO all others without building final artifacts.

## Top 5 Knowledge Gaps

1. **Semantic retrieval not wired** (CRITICAL): `cex_retriever.py` uses TF-IDF only. The embedder_provider, embedding_config, and vector_store builders are fully specified (all 13 ISOs) and KCs exist, but no end-to-end embedding pipeline connects them. Semantic search would dramatically improve F3 INJECT relevance for abstract queries (e.g., "orchestration patterns"). Path to fix: wire `kno_embedder_provider_n04.md` + `kno_vector_store_n04.md` (Supabase) into a live embedding pipeline feeding a hybrid retriever.

2. **7 P10 builders missing** (HIGH): agent_grounding_record, c2pa_manifest, compression_config, consolidation_policy, model_registry, session_backend, vc_credential, workflow_run_crate have no builders in `archetypes/builders/`. These are fully defined kinds in `.cex/kinds_meta.json` with KCs but zero build pipeline. This means N04 cannot produce these artifacts via 8F. Path to fix: dispatch N03 to generate 13-ISO builder packages for each via `/build`.

3. **54 thin KCs (18% of library)** (MEDIUM): 54 of 300 kind KCs have fewer than 200 words -- insufficient to guide F3 INJECT for those kinds. P10 memory domain is disproportionately affected (agent_grounding_record=126w, procedural_memory=152w, consolidation_policy=151w). These thin KCs cause context-starved builds for those kinds. Path to fix: evolve KCs via `cex_evolve.py --kind procedural_memory` targeting 500+ word minimum.

4. **Episodic + working + prospective memory: stub only** (MEDIUM): Three memory types (episodic_memory, working_memory, prospective_memory) have builders and KCs but no N04 implementation artifacts. These memory types are architecturally defined but not operationalized. The gap means N04 has no working short-term memory (working_memory) or temporal recall (episodic_memory). Path to fix: produce implementation artifacts in `N04_knowledge/P10_memory/` using the 13-ISO builders.

5. **Reranker not implemented** (MEDIUM): The reranker_config builder exists (13 ISOs) but has the thinnest KC in the RAG domain (103 words, 1 section). No N04 tool or implementation artifact references reranking. Without a reranker stage, retrieval precision suffers at high top-K. Path to fix: (a) enrich `kc_reranker_config.md` to 500+ words, (b) produce a reranker tool artifact in `N04_knowledge/P04_tools/`.

## Recommendations

1. **Wire semantic retrieval** -- `N04_knowledge/P01_knowledge/kno_embedder_provider_n04.md` + `kno_vector_store_n04.md` are the spec anchors. Build a thin embedding wrapper (`_tools/cex_embed.py`) that calls the configured embedder and stores in Supabase, then add a hybrid mode to `cex_retriever.py` (BM25 + cosine) gated by `CEX_RETRIEVER_MODE=hybrid` env var.

2. **Dispatch N03 for 7 missing P10 builders** -- run `bash _spawn/dispatch.sh swarm agent_grounding_record 1 "build 13-ISO builder package"` pattern for each of the 7 missing kinds. Estimated: 1 grid wave, 7 cells, ~45 min.

3. **KC enrichment sweep for P10 thin KCs** -- run `python _tools/cex_evolve.py --pillar P10 --min-words 200 --target 500` to auto-enrich 8 thin P10 KCs. Priority order: procedural_memory, memory_architecture, consolidation_policy, agent_grounding_record.

4. **Produce working_memory + episodic_memory N04 artifacts** -- use the builder ISOs already in place. These are the missing operational pieces: `N04_knowledge/P10_memory/working_memory_n04.md` and `episodic_memory_n04.md`. Working memory should reference `cex_memory_select.py` for sub-session context injection; episodic memory should wrap `cex_memory_age.py` for decay-aware recall.

5. **Add reranker tool to N04 P04** -- produce `N04_knowledge/P04_tools/reranker_n04.md` (kind=reranker_config) using `reranker-config-builder`. Enrich `kc_reranker_config.md` from 103w to 600w with cross-encoder algorithm detail, BM25 score fusion, and MRR optimization guidance. This closes the RAG pipeline precision gap.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_bugloop]] | downstream | 0.56 |
| [[bld_schema_dataset_card]] | upstream | 0.53 |
| [[bld_schema_reranker_config]] | upstream | 0.53 |
| [[bld_schema_quickstart_guide]] | upstream | 0.52 |
| [[bld_schema_usage_report]] | upstream | 0.52 |
| [[bld_schema_context_window_config]] | upstream | 0.50 |
| [[bld_schema_pitch_deck]] | upstream | 0.50 |
| [[bld_schema_search_strategy]] | upstream | 0.49 |
| [[p06_schema_a11y_checklist]] | upstream | 0.48 |
| [[bld_schema_repo_map]] | upstream | 0.48 |
