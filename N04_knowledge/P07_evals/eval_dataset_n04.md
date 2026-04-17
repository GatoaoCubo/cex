---
id: p07_ed_n04_knowledge
kind: eval_dataset
pillar: P07
nucleus: n04
title: "Eval Dataset -- N04 RAG Evaluation Question-Answer Pairs"
version: "1.0.0"
quality: 9.1
tags: [eval_dataset, n04, rag_eval, ground_truth, retrieval, P07]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "RAG evaluation dataset for N04: 50 question-answer pairs with ground truth source references, covering factual, conceptual, multi-hop, and cross-pillar query types. Used for MRR/NDCG benchmarking."
density_score: null
---

# Eval Dataset: N04 RAG Evaluation Question-Answer Pairs

## Purpose

Evaluation without ground truth is a compass without a map. This dataset provides:
- 50 queries with known correct answers and source references
- Coverage across 4 query types
- Baseline for MRR@10 and NDCG@10 benchmarks in `memory_benchmark_n04.md`

---

## Dataset Structure

Each entry: `query` + `ground_truth_answer` + `ground_truth_sources` (1-3 files)

---

## Type A: Factual (15 queries) -- Exact-match, keyword-heavy

| ID | Query | Ground Truth Source |
|----|-------|-------------------|
| FA-01 | What embedding model does CEX use by default? | N04_knowledge/P01_knowledge/embedding_config_knowledge.md |
| FA-02 | How many artifacts does cex_retriever.py index? | N04_knowledge/P10_memory/memory_benchmark_n04.md |
| FA-03 | What is the default score threshold for retrieval? | N04_knowledge/P06_schema/input_schema_knowledge_query.md |
| FA-04 | What is the maximum tokens in N04 working memory? | N04_knowledge/P10_memory/memory_architecture_n04.md |
| FA-05 | What is the TTL for episodic memories? | N04_knowledge/P10_memory/consolidation_policy_n04.md |
| FA-06 | What BM25 k1 value does the N04 retriever use? | N04_knowledge/P04_tools/retriever_n04.md |
| FA-07 | What is the RRF k parameter? | N04_knowledge/P04_tools/retriever_n04.md |
| FA-08 | What chunking overlap does the document loader use for PDFs? | N04_knowledge/P04_tools/document_loader_n04.md |
| FA-09 | What similarity threshold triggers deduplication? | N04_knowledge/P10_memory/consolidation_policy_n04.md |
| FA-10 | How many document types are defined in the type taxonomy? | N04_knowledge/P06_schema/type_def_document_types.md |
| FA-11 | What is the pgvector table name used for CEX artifacts? | N04_knowledge/P06_schema/api_reference_rag_apis.md |
| FA-12 | What is the max fields allowed in the knowledge query filters? | N04_knowledge/P06_schema/input_schema_knowledge_query.md |
| FA-13 | What memory layer has permanent retention? | N04_knowledge/P10_memory/memory_architecture_n04.md |
| FA-14 | What retrieval mode does N04 use for multi-hop reasoning? | N04_knowledge/P04_tools/search_tool_n04.md |
| FA-15 | What is the target MRR@10 for the N04 retriever? | N04_knowledge/P10_memory/memory_benchmark_n04.md |

---

## Type B: Conceptual (15 queries) -- Semantic, no exact keyword match

| ID | Query | Ground Truth Source |
|----|-------|-------------------|
| CB-01 | How does N04 prevent memory from becoming just data hoarding? | N04_knowledge/P10_memory/consolidation_policy_n04.md |
| CB-02 | What is the difference between episodic and semantic memory in N04? | N04_knowledge/P10_memory/memory_architecture_n04.md |
| CB-03 | Why does N04 use hybrid retrieval instead of dense-only? | N04_knowledge/P10_memory/memory_benchmark_n04.md |
| CB-04 | How are knowledge types classified in N04 memory? | N04_knowledge/P10_memory/memory_type_n04.md |
| CB-05 | What makes a KnowledgeCard different from a ContextDoc? | N04_knowledge/P06_schema/type_def_document_types.md |
| CB-06 | When should N04 use query expansion (HyDE)? | N04_knowledge/P04_tools/search_tool_n04.md |
| CB-07 | How does N04 decide what to store in procedural memory? | N04_knowledge/P10_memory/memory_scope_n04.md |
| CB-08 | What is the role of memory_scope in working memory management? | N04_knowledge/P10_memory/memory_scope_n04.md |
| CB-09 | How does the self-improvement loop prevent quality stagnation? | N04_knowledge/P11_feedback/self_improvement_loop_n04.md |
| CB-10 | What happens when pgvector is unavailable? | N04_knowledge/P04_tools/retriever_n04.md |
| CB-11 | How does N04 handle near-duplicate knowledge cards? | N04_knowledge/P10_memory/consolidation_policy_n04.md |
| CB-12 | What does the document loader do with low-quality PDFs? | N04_knowledge/P04_tools/document_loader_n04.md |
| CB-13 | Why are procedural memories never deleted? | N04_knowledge/P10_memory/procedural_memory_n04.md |
| CB-14 | What is the purpose of the knowledge query input schema? | N04_knowledge/P06_schema/input_schema_knowledge_query.md |
| CB-15 | How do corrections differ from preferences in N04 memory? | N04_knowledge/P10_memory/memory_type_n04.md |

---

## Type C: Multi-hop (10 queries) -- Require combining 2+ sources

| ID | Query | Ground Truth Sources |
|----|-------|---------------------|
| CH-01 | What is the end-to-end retrieval pipeline when a user queries N04? | search_tool_n04.md + memory_architecture_n04.md |
| CH-02 | How does the RAG ingestion workflow relate to the document loader? | workflow_rag_ingestion.md + document_loader_n04.md |
| CH-03 | What are the regression check thresholds and how are they derived? | regression_check_n04.md + memory_benchmark_n04.md |
| CH-04 | How do memory types map to the 4 memory layers? | memory_type_n04.md + memory_architecture_n04.md |
| CH-05 | What triggers the self-improvement loop and what does it produce? | self_improvement_loop_n04.md + learning_record_n04.md |
| CH-06 | How does consolidation policy interact with the memory scope rules? | consolidation_policy_n04.md + memory_scope_n04.md |
| CH-07 | What is the complete fallback chain for retrieval? | retriever_n04.md + search_tool_n04.md |
| CH-08 | How does entity memory connect to the semantic corpus? | entity_memory_n04.md + memory_architecture_n04.md |
| CH-09 | What document type taxonomy applies when ingesting a code repo? | type_def_document_types.md + document_loader_n04.md |
| CH-10 | What determines the retrieval weight for an external RAGSource? | type_def_document_types.md + api_reference_rag_apis.md |

---

## Type D: Cross-Pillar (10 queries) -- Require knowledge across N04 pillars

| ID | Query | Ground Truth Sources |
|----|-------|---------------------|
| XP-01 | How does the 8F pipeline apply to N04 knowledge card creation? | P03/system_prompt_knowledge.md + P07/quality_gate_knowledge.md |
| XP-02 | What is the quality gate for N04 artifacts? | P07/quality_gate_knowledge.md + P07/scoring_rubric_knowledge.md |
| XP-03 | How does N04 signal completion to N07? | P12/dispatch_rule_knowledge.md + procedural_memory_n04.md |
| XP-04 | What schemas govern N04 RAG pipeline inputs and outputs? | P06 artifacts + P01/retriever_config_knowledge.md |
| XP-05 | How is N04 agent identity defined for external systems? | P02/agent_knowledge.md + P02/agent_profile_n04.md |
| XP-06 | What workflow orchestrates the RAG ingestion pipeline? | P12/workflow_rag_ingestion.md + P04/document_loader_n04.md |
| XP-07 | How does N04's architecture pillar relate to its memory layer? | P08/rag_pipeline_architecture.md + P10/memory_architecture_n04.md |
| XP-08 | What config governs N04 rate limits? | P09/con_rate_limit_config_n04.md + P04/document_loader_n04.md |
| XP-09 | How does N04 evaluate its own retrieval quality over time? | P07/eval_metric_n04.md + P11/regression_check_n04.md |
| XP-10 | What is the full N04 self-assembly portfolio target? | n04_task.md + spec_nucleus_self_assembly.md |

---

## Eval Execution

```bash
python _tools/cex_retriever.py --eval \
  --dataset N04_knowledge/P07_evals/eval_dataset_n04.md \
  --mode hybrid_rerank \
  --output N04_knowledge/P07_evals/eval_results_n04.md
```
