---
kind: collaboration
id: bld_collaboration_vectordb_backend
pillar: P02
llm_function: COLLABORATE
purpose: How vectordb-backend-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: vectordb-backend-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should we store and index vectors for this RAG pipeline?"
I produce storage and indexing configurations for vector databases with backend connection details, dimension contracts, HNSW parameters, namespace strategies, and lifecycle operations. I do NOT handle embedding models (embedder-provider-builder), LLM routing (model-provider-builder), retrieval pipelines (retriever-builder), or chunking strategies (chunker-config-builder).
## Crew Compositions
### Crew: "Build RAG Pipeline from Scratch"
```
  1. embedder-provider-builder  -> "embedding model config: provider, dimensions, normalization"
  2. vectordb-backend-builder   -> "vector storage config: backend, index, distance metric"
  3. chunker-config-builder     -> "chunking strategy: size, overlap, splitter type"
  4. retriever-builder          -> "retrieval pipeline: query, rerank, hybrid search"
  5. rag-source-builder         -> "document source: URLs, formats, refresh schedule"
```
### Crew: "Upgrade TF-IDF to Vector Search"
```
  1. embedder-provider-builder  -> "embedding model replacing TF-IDF similarity"
  2. vectordb-backend-builder   -> "vector index replacing inverted index"
  3. retriever-builder          -> "new retrieval pipeline with vector similarity"
```
### Crew: "Scale Vector Storage"
```
  1. vectordb-backend-builder   -> "migration config from local (FAISS) to cloud (Pinecone)"
  2. lens-builder               -> "cost/performance perspective for backend selection"
  3. scoring-rubric-builder     -> "scores backends against latency, cost, scale criteria"
```
### Crew: "Multi-Domain Knowledge Base"
```
  1. vectordb-backend-builder   -> "namespace strategy for domain isolation"
  2. embedder-provider-builder  -> "shared embedding model across domains"
  3. rag-source-builder         -> "per-domain document sources"
  4. retriever-builder          -> "cross-domain or scoped retrieval"
```
## Handoff Protocol
### I Receive
- seeds: backend name, dimensions from embedder_provider (minimum required)
- optional: expected scale (vector count), deployment target (local/cloud), latency requirements
### I Produce
- vectordb_backend artifact (YAML, 22+ frontmatter fields, index config, namespace strategy)
- committed to: `cex/P01_knowledge/examples/p01_vdb_{backend}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
| Builder | Why |
|---------|-----|
| embedder-provider-builder | MUST receive dimensions and normalization flag to set dimension contract and distance metric |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| retriever-builder        | needs collection name, connection, and query interface |
| rag-source-builder       | needs collection target for document ingestion |
| agent-package-builder    | includes vectordb_backend as a deploy dependency |
