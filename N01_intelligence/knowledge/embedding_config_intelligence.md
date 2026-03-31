---
id: n01_emb_intelligence_config
kind: embedding_config
pillar: P01
title: "Embedding Configuration for N01 Research Knowledge Base"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: null
tags: [embedding, config, rag, n01, research, vector]
tldr: "Specifies the advanced embedding and chunking strategy for the N01 RAG knowledge base, using a specialized model and semantic chunking for high-fidelity retrieval of research-grade content."
---

## 1. PURPOSE
This document defines the vector embedding model and the intelligent chunking strategy for all documents ingested into the **N01 Research & Intelligence Nucleus** knowledge base. This configuration is critical for the performance of N01's Retrieval-Augmented Generation (RAG) capabilities.

## 2. EMBEDDING MODEL SPECIFICATION
The model is chosen for its state-of-the-art performance on technical and academic corpora.

- **Model Provider**: `Google`
- **Model Name**: `text-embedding-005-research` (A hypothetical model tuned for scientific and technical documents)
- **Vector Dimensions**: `1024` (To capture the nuance of complex, dense information)
- **Distance Metric**: `Cosine Similarity` (Standard for normalized, high-dimensional vectors)
- **Normalization**: `Required (L2 Norm)`

## 3. CHUNKING STRATEGY: HIERARCHICAL & SEMANTIC
A static chunk size is suboptimal for the varied documents N01 processes. We employ a hierarchical, content-aware chunking strategy.

### **Level 1: Document Pre-processing**
- **Action**: Extract clean, structured text from source formats (PDF, HTML).
- **Metadata Extraction**: Automatically extract and attach document-level metadata:
  - `doc_id`
  - `title`
  - `authors`
  - `publication_year`
  - `source_type` (e.g., `academic_paper`, `market_report`, `patent`)

### **Level 2: Semantic Chunking**
Instead of fixed-size chunks, we split based on semantic boundaries to preserve context.
- **Primary Strategy**: Chunk by structural elements of the document.
  - For academic papers: Chunk by sections (`Abstract`, `Introduction`, `Methodology`, `Conclusion`). Sub-chunk oversized sections by paragraph.
  - For market reports: Chunk by section and subsection headings.
- **Chunk Size Target**: Aim for chunks between `300-600` tokens.
- **Chunk Overlap**: `~15%` of chunk size (e.g., ~75 tokens for a 500-token chunk) to ensure smooth transitions between related concepts.

### **Level 3: Metadata Enrichment**
Each chunk vector is stored with a rich set of metadata to enable powerful hybrid search (semantic + filtered).
- `chunk_id`
- `doc_id` (inherited from parent)
- `title` (inherited from parent)
- `authors` (inherited from parent)
- `publication_year` (inherited from parent)
- `source_type` (inherited from parent)
- **`chunk_summary`**: A concise, AI-generated summary of the chunk's content (approx. 1-2 sentences). This can be used for reranking or previewing search results.
- **`keywords`**: AI-generated keywords for the chunk's specific content.

## 4. VECTOR DATABASE CONFIGURATION
- **Development/Staging**: `FAISS` (local, for rapid iteration)
- **Production**: `Weaviate` or `Pinecone` (Managed, for scalability and hybrid search capabilities)
- **Index Type**: HNSW (Hierarchical Navigable Small World) for a balance of speed and recall accuracy.
