---
kind: architecture
id: bld_architecture_vectordb_backend
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of vectordb_backend — inventory, dependencies, and architectural position
---

# Architecture: vectordb_backend in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 22+ field metadata header (id, kind, backend, dimensions, index_type, etc.) | vectordb-backend-builder | active |
| connection_config | Host, port, API key, TLS settings for backend access | author | active |
| collection_config | Collection/index name, namespace strategy, domain isolation | author | active |
| dimension_contract | Exact dimension count matching upstream embedder | author | active |
| index_config | Index type (HNSW, IVF, flat), construction and search parameters | author | active |
| distance_metric | Similarity function aligned with embedding normalization | author | active |
| metadata_config | Metadata fields, filtering capabilities, payload schema | author | active |
| persistence_config | Storage durability, save/load behavior, backup strategy | author | active |
## Dependency Graph
```
embedder_provider  --constrains-->  vectordb_backend  --consumed_by-->  retriever
vectordb_backend   --consumed_by-->  cex_retriever.py (upgrade path)
vectordb_backend   --signals-->      reindex_trigger
chunker_config     --indirectly-->   vectordb_backend (chunk count affects index size)
```
| From | To | Type | Data |
|------|----|------|------|
| embedder_provider (P01) | vectordb_backend | dependency | dimension count, normalization flag -> distance metric |
| vectordb_backend | retriever (P01) | consumes | collection name, connection, query interface |
| vectordb_backend | cex_retriever.py | data_flow | vector search replacing TF-IDF (upgrade path) |
| vectordb_backend | rag_pipeline | produces | indexed vector storage for document retrieval |
| chunker_config (P01) | vectordb_backend | indirect | total chunk count determines index size and type selection |
| vectordb_backend | backup_schedule | produces | persistence and backup configuration |
## Boundary Table
| vectordb_backend IS | vectordb_backend IS NOT |
|---------------------|--------------------------|
| A storage and indexing config for vector embeddings | An embedding model configuration (embedder_provider P01) |
| Dimension contract with upstream embedder | An LLM routing configuration (model_provider P02) |
| HNSW/IVF index parameters and tuning | A retrieval pipeline definition (retriever P01) |
| Collection namespace and metadata schema | A chunking strategy (chunker_config P01) |
| Updated when backend version or index strategy changes | A static document — must track backend API changes |
| Scoped to one backend deployment | A comparison of multiple vector databases |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | backend docs, embedder_provider | Official documentation and upstream constraints |
| Connection | connection_config | Backend endpoint and authentication |
| Contract | dimension_contract, distance_metric | Agreement with upstream embedder |
| Indexing | index_config, metadata_config | Vector storage and search optimization |
| Organization | collection_config | Namespace strategy and domain isolation |
| Durability | persistence_config | Save/load, backup, and recovery |
| Consumers | retriever, cex_retriever.py, rag_pipeline | Systems that query the vector index |
