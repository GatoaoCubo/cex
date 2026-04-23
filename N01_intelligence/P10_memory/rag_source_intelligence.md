---
id: n01_rs_academic_feeds
kind: rag_source
pillar: P01
title: "RAG Sources for N01 Intelligence Nucleus"
version: "1.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "N01_rebuild_8F"
domain: "intelligence, research, analysis, academic, financial"
quality: 9.1
tags: [rag, source, n01, memory, knowledge, vector, ingestion]
tldr: "Defines the primary academic and technical data sources for N01's RAG knowledge base, including arXiv, JSTOR, and SEC EDGAR."
density_score: 1.0
related:
  - n01_rs_intelligence_sources
  - p08_ac_intelligence
  - n01_emb_text_embedding_4
  - n04_kc_knowledge_management
  - p01_kc_vector_embedding_model_selection
  - p01_gl_embedding
  - p01_kc_rag_source
  - atom_21_rag_taxonomy
  - ex_research_pipeline_academic
  - p01_gl_rag
---

## Purpose
This document lists and configures the external data sources that are to be ingested, indexed, and made available for retrieval by the **N01 Intelligence Nucleus** RAG system. This forms the foundation of N01's world knowledge.

## Configuration Parameters

| Parameter | Value | Purpose |
|-----------|--------|---------|
| `chunk_size` | 1024 tokens | Optimal for academic papers with complex context |
| `chunk_overlap` | 128 tokens | Preserve cross-sentence relationships |
| `embedding_model` | `text-embedding-4` | Latest OpenAI model for technical content |
| `index_dimensions` | 3072 | Match embedding model output |
| `batch_size` | 100 documents | Balance memory usage vs throughput |
| `retry_limit` | 3 attempts | Handle API rate limits gracefully |
| `metadata_fields` | `[author, date, journal, doi, category]` | Enable filtered search |

## Ingestion & Retrieval Strategy

| Component | Method | Configuration | Purpose |
|-----------|--------|---------------|---------|
| **Source Monitoring** | Scheduled checks per `update_frequency` | Cron jobs + webhooks | Track new documents |
| **Document Ingestion** | Bulk download → chunk → vectorize | Uses `n01_emb_text_embedding_4` | Convert to searchable format |
| **Vector Storage** | Dense embeddings + metadata | Pinecone/Weaviate indexes | Enable semantic search |
| **Retrieval** | Hybrid search (vector + keyword) | Configured by `p01_retr_cfg.md` | Balance relevance + precision |
| **Freshness** | Delta updates only | Compare timestamps/hashes | Avoid duplicate processing |

---
## Primary Sources
This is a living list of high-priority sources for ingestion.

| Name | Type | Access Point | Update Frequency | Description |
|---|---|---|---|---|
| **arXiv** | Pre-print Archive | `s3://arxiv/` (bulk) | Daily | Access to the latest research in physics, mathematics, computer science, and more. Critical for state-of-the-art technical knowledge. |
| **JSTOR** | Journal Archive | `https://api.jstor.org/` | Weekly | Comprehensive archive of academic journals across a wide range of disciplines. Essential for foundational research. |
| **SEC EDGAR** | Financial Filings | `https://www.sec.gov/edgar/bulk-data` | Daily | Access to all company filings (10-K, 10-Q, 8-K), providing ground-truth for competitor and market analysis. |
| **USPTO Patents** | Patent Database | Bulk download via USPTO website | Weekly | Full text of granted patents and applications. Key for tracking innovation and intellectual property trends. |
| **PubMed Central**| Biomedical Papers | `https://ftp.ncbi.nlm.nih.gov/pub/pmc/` | Daily | Free full-text archive of biomedical and life sciences journal literature. |

---
## Future Sources
- **Semantic Scholar**: API access for citation graphs and paper recommendations.
- **DBLP**: Computer science bibliography for author and publication tracking.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_rs_intelligence_sources]] | sibling | 0.40 |
| [[p08_ac_intelligence]] | downstream | 0.27 |
| [[n01_emb_text_embedding_4]] | related | 0.26 |
| [[n04_kc_knowledge_management]] | related | 0.23 |
| [[p01_kc_vector_embedding_model_selection]] | related | 0.20 |
| [[p01_gl_embedding]] | related | 0.20 |
| [[p01_kc_rag_source]] | related | 0.20 |
| [[atom_21_rag_taxonomy]] | related | 0.19 |
| [[ex_research_pipeline_academic]] | downstream | 0.19 |
| [[p01_gl_rag]] | related | 0.18 |
