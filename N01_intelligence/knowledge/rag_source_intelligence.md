---
id: n01_rs_intelligence_sources
kind: rag_source
pillar: P01
title: "RAG Sources for N01 Intelligence Nucleus"
version: "2.0.0"
created: "2026-03-30"
updated: "2026-03-31"
author: "N07_peer_review"
domain: "intelligence, research, analysis, academic"
quality: 8.8
tags: [rag, source, n01, intelligence, research, arxiv, academic]
tldr: "Primary data sources for N01 Intelligence RAG — arXiv, JSTOR, SEC EDGAR, USPTO, and PubMed for research and competitive analysis."
density_score: 0.90
---

## Purpose

Lists and configures the external data sources ingested into the **N01 Intelligence Nucleus** RAG system. These sources form the foundation of N01's analytical capabilities across research, market, and competitive intelligence domains.

## Ingestion Strategy

| Parameter | Value |
|-----------|-------|
| Embedding model | text-embedding-004 (see `n01_emb_intelligence_config`) |
| Chunk size | 512 tokens |
| Overlap | 64 tokens |
| Retrieval | Hybrid (dense vector + keyword filter) |
| Index | Local FAISS (dev) / Pinecone (prod) |

New documents are downloaded per `update_frequency`, chunked, vectorized, and indexed. Stale sources are flagged after 2x their update frequency.

## Primary Sources

| Source | Type | Access | Frequency | Domain |
|--------|------|--------|-----------|--------|
| **arXiv** | Pre-print archive | `s3://arxiv/` bulk | Daily | CS, physics, math — state-of-the-art research |
| **JSTOR** | Journal archive | `https://api.jstor.org/` | Weekly | Cross-discipline foundational research |
| **SEC EDGAR** | Financial filings | `https://sec.gov/edgar/bulk-data` | Daily | 10-K, 10-Q, 8-K — competitor financials |
| **USPTO Patents** | Patent database | USPTO bulk download | Weekly | Innovation tracking, IP landscape |
| **PubMed Central** | Biomedical papers | `https://ftp.ncbi.nlm.nih.gov/pub/pmc/` | Daily | Life sciences, biotech research |

## Freshness Policy

| Metric | Value |
|--------|-------|
| Re-check interval | Per source frequency (daily/weekly) |
| Staleness threshold | 2x update frequency |
| Alert on stale | Signal to N07 orchestrator |
| Bulk re-index | Monthly full refresh |

## Future Sources

- **Semantic Scholar**: Citation graphs, paper recommendations, influence scores
- **DBLP**: CS bibliography for author/publication tracking
- **CrunchBase**: Startup and funding data for competitive intelligence
- **Google Scholar**: Broader academic coverage, citation metrics

## Integration

Sources feed into N01's RAG pipeline via the embedding config (`n01_emb_intelligence_config`). Retrieved chunks are ranked by relevance score and passed as context to Gemini 2.5-pro for synthesis into intelligence briefs, competitor analyses, and trend reports.
