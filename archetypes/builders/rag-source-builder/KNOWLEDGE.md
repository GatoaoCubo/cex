---
pillar: P01
llm_function: INJECT
domain: rag_source
version: 1.0.0
---

# Knowledge: rag_source

## Foundational Concept
RAG (Retrieval-Augmented Generation) source indexing: a catalog of external data references used by vector search pipelines. A rag_source is a structured pointer — it records WHERE to find content, not the content itself.

## Industry Analogies
- Bookmark managers (Raindrop, Pinboard) — save URLs with metadata
- RSS feed registries — track sources for periodic refresh
- Data catalogs (Apache Atlas, DataHub) — asset discovery and lineage
- Link databases (Common Crawl seed lists) — URL inventories for crawlers

## Key Patterns

### URL-First Design
The url field is the primary key of a rag_source. Without a valid, accessible URL the artifact has no value. Validate format and reachability before committing.

### Freshness Tracking
External sources change. last_checked records when the URL was last verified. A recommended re-check interval is 30 days. Stale sources (>90 days unchecked) should be flagged.

### Reliability Scoring
| Level | Meaning |
|-------|---------|
| high | Official docs, stable APIs, institutional sources |
| medium | Community wikis, curated blogs, stable third-party |
| low | Social media, rapidly changing pages, unofficial mirrors |

### Format Awareness
Extraction strategy depends on format: html (scrape), json/api (parse), pdf (extract text), csv (tabular ingest).

## CEX Extensions
- last_checked: mandatory field (industry catalogs often omit this)
- domain: explicit binding to CEX domain taxonomy
- quality: null on creation (never self-scored)

## Critical Boundary

| Kind | Contains | Purpose |
|------|----------|---------|
| rag_source | URL + metadata | Pointer to external source |
| knowledge_card | Distilled content | Synthesized knowledge artifact |
| context_doc | Domain framing | Scoping and context for a domain |

rag_source POINTS TO content. knowledge_card HAS content. Never conflate.

## Ingestion Pipeline Position
```
External World
  -> rag_source (catalog: URL + metadata)
  -> brain_index (periodic crawl + embed)
  -> vector store (indexed chunks)
  -> retrieval (similarity search)
  -> agent (augmented generation)
```
