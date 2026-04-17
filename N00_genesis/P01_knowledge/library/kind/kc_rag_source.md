---
id: p01_kc_rag_source
kind: knowledge_card
type: kind
pillar: P01
title: "RAG Source — Deep Knowledge for rag_source"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: rag_source
quality: 9.1
tags: [rag_source, p01, INJECT, kind-kc]
tldr: "Pointer to an external indexable source — URL, freshness, and domain metadata for the RAG ingestion pipeline"
when_to_use: "Building, reviewing, or reasoning about rag_source artifacts"
keywords: [rag-source, external-data, ingestion, freshness]
feeds_kinds: [rag_source]
density_score: 0.99
linked_artifacts:
  primary: null
  related: []
---

# RAG Source

## Spec
```yaml
kind: rag_source
pillar: P01
llm_function: INJECT
max_bytes: 1024
naming: p01_rs_{{source}}.md + .yaml
core: false
```

## What It Is
A rag_source is a pointer to an external indexable document — it stores the URL, domain classification, and last-checked date but NOT the content itself. It tells the ingestion pipeline where to fetch knowledge from and when it was last validated. It is NOT the content (which becomes knowledge_cards after distillation) nor an embedding_config (which defines how content is encoded). RAG sources are the entry point of the knowledge supply chain.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `DocumentLoader` sources (URL, PDF, API) | WebBaseLoader, PyPDFLoader, etc. — source config |
| LlamaIndex | `SimpleDirectoryReader` / `download_loader` | Data connectors hub; 160+ loaders |
| CrewAI | `Tool` with search/scrape capability | SerperDevTool, ScrapeWebsiteTool, etc. |
| DSPy | Retrieval model configuration | ColBERTv2 server URL, Pinecone index ref |
| Haystack | `Fetcher` / `Converter` pipeline nodes | LinkContentFetcher, HTMLToDocument |
| OpenAI | Assistants API file uploads | Files uploaded to vector_store as sources |
| Anthropic | No native source management | External ETL pipeline feeds context |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| url | string | required | Source location; must be accessible at ingestion time |
| domain | string | required | Enables filtered retrieval by vertical |
| last_checked | date | required | Staleness detection; older = higher re-check priority |
| format | enum | auto-detect | Explicit format avoids parser errors |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Documentation source | Indexing official docs | Anthropic API docs, refreshed weekly |
| Marketplace feed | E-commerce competitive data | Mercado Livre category pages, daily scrape |
| Research paper | Academic knowledge ingestion | ArXiv papers on RAG techniques |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Storing content in rag_source | Exceeds 1KB; duplicates indexed content | Store pointer only; content goes to KCs after distillation |
| No freshness tracking | Stale sources silently poison knowledge base | Always set last_checked; automate re-validation |
| Mixing domains in one source | Retrieval precision drops | One rag_source per domain/vertical |

## Integration Graph
```
[external URLs] --> [rag_source] --> [chunk_strategy] --> [knowledge_card]
                         |
                  [embedding_config]
```

## Decision Tree
- IF content is already distilled and dense THEN knowledge_card directly
- IF pointing to external doc for future ingestion THEN rag_source
- IF source is a single term definition THEN glossary_entry directly
- IF source needs periodic refresh THEN rag_source with freshness tracking
- DEFAULT: rag_source for any external content not yet in the knowledge base

## Quality Criteria
- GOOD: URL valid; domain specified; last_checked present
- GREAT: Freshness SLA defined; format explicitly set; linked to downstream KCs it feeds
- FAIL: URL broken; no domain; content duplicated inline; last_checked missing
