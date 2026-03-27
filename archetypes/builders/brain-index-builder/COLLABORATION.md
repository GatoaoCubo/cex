---
pillar: P12
llm_function: COLLABORATE
purpose: How brain-index-builder works in crews
---

# Collaboration: brain-index-builder

## My Role
I define HOW content is indexed and searched for retrieval.
I do not define embedding models (embedding-config-builder).
I do not define data sources (rag-source-builder).

## Crew: "RAG Pipeline Setup"
```
  1. rag-source-builder        -> defines data sources
  2. embedding-config-builder  -> defines embedding model
  3. brain-index-builder       -> defines search index
  4. knowledge-card-builder    -> produces indexed content
```

## Crew: "Memory System Setup"
```
  1. brain-index-builder       -> defines search infrastructure
  2. runtime-state-builder     -> defines agent query context
  3. learning-record-builder   -> defines what gets indexed
```

## Handoff Protocol
### I Receive
- seeds: scope (what to index), algorithm preference, corpus size estimate
- optional: embedding_config (P01), existing rag_sources, performance requirements

### I Produce
- brain_index artifact in P10_memory/examples/
- committed to: cex/P10_memory/examples/p10_bi_{index_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
| Builder | Why |
|---------|-----|
| embedding-config-builder | Need to know embedding dimensions and model for FAISS config |
| rag-source-builder | Need to know corpus scope and update frequency |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| runtime-state-builder | Agents query brain_index; state may adapt based on search results |
