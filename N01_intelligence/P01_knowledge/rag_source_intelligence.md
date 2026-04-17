---
id: n01_rs_intelligence_sources
kind: rag_source
pillar: P01
title: "RAG Source Configuration for N01 Intelligence Nucleus"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: 9.1
tags: [rag, source, knowledge, n01, research, ingestion]
tldr: "Defines the tiered data sources, ingestion policies, and update frequencies for the N01 Research Nucleus RAG knowledge base."
density_score: 0.97
---

## 1. PURPOSE
This document specifies the authoritative data sources that form the knowledge base for the N01 agent's Retrieval-Augmented Generation (RAG) capabilities. The selection, tiering, and ingestion policies are designed to maximize the relevance, accuracy, and credibility of N01's analytical outputs.

## 2. INGESTION & EMBEDDING
- **Embedding Configuration**: All sources are processed according to `n01_emb_intelligence_config`.
- **Ingestion Pipeline**: A dedicated pipeline monitors each source, downloads new/updated documents, performs semantic chunking, generates embeddings, and upserts the vectors and metadata into the production vector database.

## 3. SOURCE TIERS
Sources are categorized into tiers that reflect their credibility and intended use, directly informing the `Evidence Quality` dimension in the scoring rubric.

### **Tier 1: Foundational & High-Credibility Scientific Research**
- **Description**: The most authoritative sources for scientific and technical facts.
- **Update Frequency**: Daily
- **Sources**:
  - `arXiv`: Access to pre-print articles across STEM fields for state-of-the-art research.
  - `PubMed Central`: Comprehensive database of biomedical and life sciences journal literature.
  - `JSTOR`: Archive of foundational, peer-reviewed academic journals across multiple disciplines.

### **Tier 2: Official Corporate & Regulatory Data**
- **Description**: Primary sources for competitor intelligence, financial performance, and intellectual property.
- **Update Frequency**: Daily
- **Sources**:
  - `SEC EDGAR`: Corporate filings (10-K, 10-Q) for U.S. public companies. Critical for financial and strategic analysis.
  - `USPTO Bulk Data`: Granted patents and patent applications from the U.S. Patent and Trademark Office. Key for tracking innovation.

### **Tier 3: Reputable Market & Industry Analysis**
- **Description**: High-quality secondary sources that provide context and expert analysis on market trends. Requires careful source evaluation.
- **Update Frequency**: Weekly
- **Sources**:
  - `[INTERNAL] Market Research Subscriptions`: A placeholder for licensed reports from firms like Gartner, Forrester, etc. (Requires secure ingestion).
  - `[INTERNAL] Conference Proceedings`: Papers and presentations from top-tier industry conferences (e.g., NeurIPS, ICML).

### **Tier 4: High-Quality Web Content (Future)**
- **Description**: A planned expansion to include high-signal web data. Requires robust filtering to maintain quality.
- **Update Frequency**: Continuous (via a dedicated crawler)
- **Potential Sources**:
  - `Reputable Technical Blogs`: (e.g., AI-centric blogs from major tech companies).
  - `Select Industry News Outlets`: (e.g., Reuters, Bloomberg for tech/finance news).

## 4. SOURCE VALIDATION

| Validation Criteria | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---------------------|--------|--------|--------|--------|
| **Citation Count Threshold** | >50 (for papers) | N/A | >10 (for reports) | >5 (for articles) |
| **Publication Recency** | <5 years preferred | <1 year required | <2 years preferred | <30 days required |
| **Author Credibility Check** | PhD + institution | Official entity | Industry analyst | Verified expert |
| **Content Quality Score** | >0.85 (automated) | >0.90 (automated) | >0.80 (automated) | >0.75 (automated) |
| **Duplicate Detection** | Semantic similarity <0.8 | Exact match check | Semantic similarity <0.85 | URL + content hash |
| **Language Quality** | Native/fluent only | Official English | Professional only | Editorial standard |

**Rejection Thresholds**: Sources failing >2 criteria are automatically flagged for human review. Sources failing >3 criteria are rejected from ingestion.

## 5. FRESHNESS & RETENTION POLICY
- **Staleness Check**: The ingestion pipeline continuously monitors sources based on their defined update frequency.
- **Alerting**: If a source fails to update for more than 2x its frequency period, an alert is sent to the N05 Operations Nucleus.
- **Retention**: All versions of documents are retained. Vectors are tagged with the ingestion date to allow for time-bound queries (e.g., "summarize findings based on sources available before 2025").