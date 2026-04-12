---
id: p06_arch_rag_pipeline
kind: context_doc
pillar: P06
title: "RAG Pipeline Architecture — N04 End-to-End Flow"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: 9.0
tags: [architecture, rag, pipeline, embedding, retrieval, n04]
tldr: "Complete RAG pipeline: ingest → chunk → embed → store → retrieve → inject. 6 stages, 8 kinds, 5 MCP servers."
density_score: 0.95
---

# RAG Pipeline Architecture

## Pipeline Stages

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ 1. INGEST│───▶│ 2. CHUNK │───▶│ 3. EMBED │───▶│ 4. STORE │───▶│5. RETRIEVE│──▶│ 6. INJECT│
│          │    │          │    │          │    │          │    │          │    │          │
│ firecrawl│    │ chunk_   │    │ embedding│    │ vector_  │    │ retriever│    │ prompt_  │
│ fetch    │    │ strategy │    │ _config  │    │ store    │    │ _config  │    │ layers   │
│ doc_load │    │          │    │ embedder │    │ supabase │    │ TF-IDF   │    │ memory_  │
│          │    │          │    │ _provider│    │ pgvector │    │ BM25     │    │ select   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

## Stage Detail

| Stage | Kind(s) | Tool(s) | MCP | Input | Output |
|-------|---------|---------|-----|-------|--------|
| **1. Ingest** | `document_loader`, `rag_source` | `cex_research.py` | firecrawl, fetch | URL, PDF, HTML, CSV | Raw text blobs |
| **2. Chunk** | `chunk_strategy` | — | — | Raw text | Sized chunks (256-2048 tokens) |
| **3. Embed** | `embedding_config`, `embedder_provider` | — | — | Text chunks | Float vectors (768-3072 dims) |
| **4. Store** | `vector_store` | `supabase_data_layer.py` | supabase, postgres | Vectors + metadata | Indexed rows in pgvector |
| **5. Retrieve** | `retriever_config` | `cex_retriever.py` | postgres | Query embedding | Top-K ranked docs |
| **6. Inject** | `knowledge_card`, `context_doc` | `cex_prompt_layers.py`, `cex_memory_select.py` | — | Retrieved docs | Hydrated prompt context |

## Chunking Strategies

| Strategy | Chunk Size | Overlap | Best For |
|----------|-----------|---------|----------|
| Fixed-window | 512 tokens | 64 tokens | General docs, KCs |
| Semantic | Variable | Section-boundary | Markdown with headers |
| Sentence-split | 3-5 sentences | 1 sentence | Dense prose, specs |
| Code-block | Function/class | None | Python tools, YAML schemas |

## Embedding Models

| Provider | Model | Dimensions | Max Tokens | Cost |
|----------|-------|-----------|------------|------|
| OpenAI | text-embedding-3-large | 3072 | 8191 | $0.13/1M |
| OpenAI | text-embedding-3-small | 1536 | 8191 | $0.02/1M |
| Voyage | voyage-3 | 1024 | 32000 | $0.06/1M |
| Local | all-MiniLM-L6-v2 | 384 | 512 | Free |

## Vector Store Backends

| Backend | Index Type | Latency | Scale | CEX Status |
|---------|-----------|---------|-------|------------|
| Supabase pgvector | IVFFlat / HNSW | 5-50ms | 10M vectors | **Active** (MCP connected) |
| FAISS | IVF + PQ | 1-5ms | 100M vectors | Planned |
| ChromaDB | HNSW | 5-20ms | 1M vectors | Not planned |

## Retrieval Modes

| Mode | Algorithm | When |
|------|-----------|------|
| Dense | Cosine similarity on embeddings | Default — semantic matching |
| Sparse | BM25 / TF-IDF | Keyword-heavy queries, exact term matching |
| Hybrid | Dense + Sparse + RRF | Best quality — combines semantic + lexical |
| MMR | Maximum Marginal Relevance | Diversity needed — avoid redundant results |

## CEX Integration Points

| N04 Artifact | Feeds | Consumer |
|--------------|-------|----------|
| `embedding_config` | Vector dimensions, model selection | `supabase_data_layer.py` |
| `chunk_strategy` | Split rules | All document processing |
| `retriever_config` | Top-K, threshold, rerank | `cex_retriever.py`, `cex_memory_select.py` |
| `rag_source` | Source URL, refresh schedule | `firecrawl`, `fetch` MCPs |
| `knowledge_card` | Final structured output | `cex_prompt_layers.py` |
| `brain_index` | Index metadata | `cex_kc_index.py` |

## Data Flow Volumes (CEX Current)

| Metric | Value |
|--------|-------|
| Total artifacts | 2,184 |
| Vocabulary size | ~12,000 terms |
| TF-IDF index | Active (`cex_retriever.py`) |
| P01 compiled library | 197 artifacts |
| Knowledge cards | 123 kind KCs + domain KCs |
| Embedding index | Not yet deployed (gap) |
