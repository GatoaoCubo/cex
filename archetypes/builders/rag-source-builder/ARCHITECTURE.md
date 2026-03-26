---
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
---

# Architecture: rag_source

## Boundary Definition

rag_source IS a pointer to an external indexable source.
rag_source IS NOT:
- knowledge_card (distilled content — HAS the information)
- context_doc (domain context — scopes a domain for agents)
- embedding_config (vector model settings — configures indexing)
- signal (state event — records what happened)

## Kind Comparison

| Kind | Contains | Layer | Purpose |
|------|----------|-------|---------|
| rag_source | URL + metadata | content | Point to external source |
| knowledge_card | Distilled synthesis | content | Store extracted knowledge |
| context_doc | Domain framing | context | Scope domain for agents |
| embedding_config | Model + chunking params | config | Configure vector indexing |

## Pipeline Position

```
External World (docs, APIs, papers, datasets)
        |
        v
  rag_source              <- THIS KIND
  (catalog: URL + freshness metadata)
        |
        v
  brain_index             <- periodic crawl job reads rag_sources
  (fetch URL, chunk, embed)
        |
        v
  vector store
  (indexed chunks, searchable)
        |
        v
  retrieval layer
  (similarity search on query)
        |
        v
  agent context
  (augmented generation)
```

## Fractal Position
- Pillar: P01 (knowledge layer — content tier)
- llm_function: INJECT (provides context to agents via retrieval)
- Layer: content ("Conhecimento destilado — criado, versionado")
- Core 24: YES (content tier, high-value for retrieval pipelines)

## Confusion Avoidance

**"Should I put the content here?"** No. Put a pointer here. Put content in knowledge_card.

**"Is this a context_doc?"** Only if it scopes a domain. rag_source scopes a retrieval source.

**"What if the URL has structured data?"** Still a pointer. The extracted/parsed content becomes a knowledge_card downstream.

## Dependency Flow
```
rag_source --[read by]--> brain_index [PLANNED]
rag_source --[informs]--> knowledge_card (content distilled from this source)
rag_source --[tagged with]--> domain (from CEX domain taxonomy)
```
