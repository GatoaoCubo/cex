---
id: p01_kc_llamaindex_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "LlamaIndex Patterns — Query Engines, Node Parsers, Response Synthesizers, Workflows"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: llamaindex
origin: src_framework_taxonomy
quality: 9.1
tags: [llamaindex, query-engine, node-parser, response-synthesizer, workflow, index]
tldr: "LlamaIndex structures data as indexed nodes, queries via engines/retrievers, and synthesizes responses — optimized for RAG-first architectures"
when_to_use: "Building or mapping LlamaIndex constructs to CEX kinds"
keywords: [llamaindex, query-engine, node, index, retriever, ingestion, workflow]
long_tails:
  - "How does LlamaIndex ingestion pipeline map to CEX document_loader and chunk_strategy"
  - "Which LlamaIndex classes map to CEX retriever and knowledge_index kinds"
axioms:
  - "Document -> TextNode is the fundamental data transformation — nodes carry relationships and metadata"
  - "VectorStoreIndex is the default index; PropertyGraphIndex for relational queries"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_taxonomy, p01_kc_langchain_patterns, p01_kc_haystack_patterns]
feeds_kinds:
  - agent           # AgentWorkflow, Workflow (event-driven)
  - retriever       # BaseRetriever
  - retriever_config # VectorStoreIndex config, StorageContext
  - document_loader # SimpleDirectoryReader, IngestionPipeline
  - chunk_strategy  # NodeParser, SentenceSplitter
  - embedding_config # Embedding interface, Settings.embed_model
  - workflow        # Workflow (event-driven), IngestionPipeline
  - response_format # ResponseSynthesizer (generates coherent answers)
  - knowledge_index     # VectorStoreIndex, PropertyGraphIndex, IndexStore
  - knowledge_card  # Document, TextNode (atomic data units)
density_score: 0.90
related:
  - atom_07_llamaindex
  - p01_kc_core
  - p04_kc_core
  - retriever-config-builder
  - bld_collaboration_retriever
  - p01_kc_retriever
  - cex_llm_vocabulary_whitepaper
  - p01_kc_knowledge_index
  - knowledge-index-builder
  - bld_collaboration_agentic_rag
---

# LlamaIndex Patterns

## Quick Reference
```yaml
topic: LlamaIndex Core (llama_index.core)
scope: Data indexing, query engines, node-based RAG, agentic workflows
source: docs.llamaindex.ai
criticality: high
```

## Key Concepts

| Concept | Module | CEX Kind | Role |
|---------|--------|----------|------|
| `Document` | `llama_index.core` | knowledge_card | Generic data container from any source |
| `TextNode` | `llama_index.core.schema` | knowledge_card | Chunk with metadata + relationships |
| `NodeParser` | `llama_index.core.node_parser` | chunk_strategy | Abstract document-to-node splitter |
| `SentenceSplitter` | `llama_index.core.node_parser` | chunk_strategy | Split by sentence boundaries |
| `SimpleDirectoryReader` | `llama_index.core` | document_loader | Multi-file loader |
| `IngestionPipeline` | `llama_index.core.ingestion` | workflow | End-to-end document processing |
| `VectorStoreIndex` | `llama_index.core` | knowledge_index | Semantic search index via embeddings |
| `PropertyGraphIndex` | `llama_index.core` | knowledge_index | Graph-based relational index |
| `StorageContext` | `llama_index.core` | retriever_config | Unified storage configuration |
| `BaseRetriever` | `llama_index.core.retrievers` | retriever | Abstract retriever interface |
| `QueryEngine` | `llama_index.core.query_engine` | retriever | Process and answer queries |
| `ChatEngine` | `llama_index.core.chat_engine` | retriever | Conversational query interface |
| `ResponseSynthesizer` | `llama_index.core.response_synthesizers` | response_format | Generate coherent answers from context |
| `Embedding` | `llama_index.core.embeddings` | embedding_config | Embedding model interface |
| `Settings` | `llama_index.core` | embedding_config | Global config (llm, embed_model, chunk_size) |
| `Workflow` | `llama_index.core.workflow` | workflow | Event-driven agentic workflow |
| `AgentWorkflow` | `llama_index.core.agent` | agent | Multi-agent collaboration system |

## Patterns

| Trigger | Action |
|---------|--------|
| Ingest documents | `SimpleDirectoryReader("./data").load_data()` -> `IngestionPipeline` |
| Build RAG index | `VectorStoreIndex.from_documents(docs)` with `StorageContext` |
| Query with retrieval | `index.as_query_engine()` — auto-wires retriever + synthesizer |
| Conversational RAG | `index.as_chat_engine()` — adds message history |
| Custom retrieval | Subclass `BaseRetriever`, override `_retrieve()` |
| Agentic workflow | `Workflow` with `@step` decorators, event-driven |
| Graph-based queries | `PropertyGraphIndex` for entity-relationship traversal |

## Anti-Patterns

- Skipping `StorageContext` — losing persistence between sessions
- Using `VectorStoreIndex` for relational data (use `PropertyGraphIndex`)
- Ignoring `NodeRelationship` — losing document structure
- Calling `index.as_query_engine()` without tuning `similarity_top_k`
- Not setting `Settings.embed_model` — falls back to OpenAI default

## CEX Mapping

```text
[document_loader -> chunk_strategy] -> [embedding_config -> knowledge_index]
    -> [retriever_config -> retriever -> response_format] -> [agent/workflow]
```

## References

- source: docs.llamaindex.ai/en/stable/
- related: p01_kc_cex_taxonomy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_07_llamaindex]] | sibling | 0.45 |
| [[p01_kc_core]] | sibling | 0.28 |
| [[p04_kc_core]] | sibling | 0.24 |
| [[retriever-config-builder]] | related | 0.21 |
| [[bld_collaboration_retriever]] | downstream | 0.20 |
| [[p01_kc_retriever]] | sibling | 0.19 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.18 |
| [[p01_kc_knowledge_index]] | sibling | 0.18 |
| [[knowledge-index-builder]] | downstream | 0.18 |
| [[bld_collaboration_agentic_rag]] | downstream | 0.17 |
