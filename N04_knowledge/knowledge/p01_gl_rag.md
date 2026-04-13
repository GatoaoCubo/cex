---
id: p01_gl_rag
kind: glossary_entry
pillar: P01
title: "Retrieval-Augmented Generation (RAG)"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: 8.7
tags: [glossary, rag, retrieval, augmented-generation]
tldr: "Pattern that augments LLM prompts with retrieved documents from a knowledge base, reducing hallucination and grounding responses in facts."
density_score: 0.97
updated: "2026-04-13"
---

# Retrieval-Augmented Generation (RAG)

**Term**: Retrieval-Augmented Generation
**Abbreviation**: RAG
**Synonyms**: retrieval-augmented prompting, grounded generation

**Definition**: An architecture pattern where an LLM prompt is augmented with relevant documents retrieved from an external knowledge base at inference time. The pipeline: query → embed → retrieve top-K → inject into context → generate. Reduces hallucination by grounding responses in verified knowledge. CEX implements RAG via `cex_retriever.py` (TF-IDF sparse) with planned dense retrieval via Supabase pgvector.

**See**: `retriever_config`, `rag_source`, `chunk_strategy`, `rag_pipeline_architecture.md`

## Boundary

Definicao curta de termo do dominio. NAO eh knowledge_card (sem densidade min) nem context_doc (sem escopo).


## 8F Pipeline Function

Primary function: **INJECT**
