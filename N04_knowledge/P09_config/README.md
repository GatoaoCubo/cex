# P09 Config — N04 Knowledge

> Knowledge Gluttony · configuration for RAG, indexing, embeddings

## Scope in N04
Runtime settings for the knowledge layer: embedding model choice,
chunk strategy parameters, reranker thresholds, index rebuild
schedules, retriever top-k defaults. Gluttony drives "load
everything" — so configs here bias toward recall over precision.

## Kinds that live here
- `env_config` — env vars for embedding/vector-DB backends
- `embedding_config` — model/dimension defaults
- `retriever_config` — top-k, MMR lambda, rerank toggles
- `rate_limit_config` — throttles on external embedding APIs

## Related
- `knowledge/` — the KCs and RAG sources this config indexes
- `memory/` — entity memory and prompt cache settings overlap here
