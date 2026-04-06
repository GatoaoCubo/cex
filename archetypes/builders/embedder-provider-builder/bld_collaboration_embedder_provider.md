---
kind: collaboration
id: bld_collaboration_embedder_provider
pillar: P02
llm_function: COLLABORATE
purpose: How embedder-provider-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: embedder-provider-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should we embed documents and queries for this RAG pipeline?"
I produce connection configurations for embedding models with provider API details, dimensions, normalization, batch limits, and pricing. I do NOT handle vector storage (vectordb-backend-builder), LLM routing (model-provider-builder), retrieval pipelines (retriever-builder), or chunking strategies (chunker-config-builder).
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
### Crew: "Multi-Provider Embedding Comparison"
```
  1. embedder-provider-builder  -> "produces configs for each candidate embedding model"
  2. benchmark-builder          -> "MTEB evaluation protocol for comparison"
  3. scoring-rubric-builder     -> "scores each model against target use case criteria"
  4. lens-builder               -> "cost/quality/latency perspective for selection"
```
## Handoff Protocol
### I Receive
- seeds: provider name, model name (minimum required)
- optional: target use case (semantic search, classification, clustering), dimension constraint
### I Produce
- embedder_provider artifact (YAML, 20+ frontmatter fields, dimension contract, normalized pricing)
- committed to: `cex/P01_knowledge/examples/p01_emb_{provider}_{slug}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None. embedder-provider-builder is INDEPENDENT (layer 0 infrastructure).
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| vectordb-backend-builder | needs dimension count to configure index and distance metric |
| retriever-builder        | needs model ID and normalization to embed queries at search time |
| chunker-config-builder   | needs max_tokens to set chunk size ceiling |
| rag-source-builder       | needs embedding model to plan ingestion batch sizes |
| agent-package-builder    | includes embedder_provider as a deploy dependency |
