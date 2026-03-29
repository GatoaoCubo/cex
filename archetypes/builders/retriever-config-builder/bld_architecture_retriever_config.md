---
kind: architecture
id: bld_architecture_retriever_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of retriever_config — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| store_type | Vector store backend (faiss, chroma, pinecone, weaviate) | retriever_config | required |
| top_k | Number of results to return | retriever_config | required |
| search_type | Search algorithm (dense, sparse, hybrid) | retriever_config | required |
| hybrid_ratio | Weight between dense and sparse (0.0-1.0) | retriever_config | optional |
| reranker | Cross-encoder model for result reranking | external | optional |
| filters | Metadata filters applied before search | retriever_config | optional |
| chunk_strategy | Chunking config that produced the indexed documents | P01 | upstream |
| embedding_config | Vector model used to encode queries | P01 | upstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| store_type | retriever_config | produces | Vector store backend (faiss, chroma, pinecone, weaviate) |
| top_k | retriever_config | produces | Number of results to return |
| search_type | retriever_config | produces | Search algorithm (dense, sparse, hybrid) |
| hybrid_ratio | retriever_config | produces | Weight between dense and sparse (0.0-1.0) |
| reranker | external | produces | Cross-encoder model for result reranking |
| filters | retriever_config | produces | Metadata filters applied before search |
| chunk_strategy | P01 | depends | Chunking config that produced the indexed documents |
| embedding_config | P01 | depends | Vector model used to encode queries |
## Boundary Table
| retriever_config IS | retriever_config IS NOT |
|-------------|----------------|
| Retrieval parameters — how to search and rank chunks from a vector/hybrid store | embedding_config (vector model) |
| Not embedding_config | embedding_config (vector model) |
| Not chunk_strategy | chunk_strategy (splitting) |
| Not knowledge_card | knowledge_card (content) |
| Not brain_index | brain_index (index infra) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | store_type, top_k, search_type | Define the artifact's core parameters |
| optional | hybrid_ratio, reranker, filters | Extend with recommended fields |
| external | chunk_strategy, embedding_config | Upstream/downstream connections |
