---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: brain-index-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Invalid algorithm enum ("elasticsearch", "milvus" instead of bm25/faiss/hybrid)
3. Missing BM25 parameters when algorithm includes BM25
4. Missing FAISS parameters when algorithm includes FAISS
5. No rebuild_schedule (index staleness is a silent failure)
6. Confusing brain_index with embedding_config (index vs model)
7. Using hyphens in id slug (must be underscores: p10_bi_knowledge_pool)

## Proven Brain Index Patterns
| Corpus | Algorithm | Rebuild | Freshness |
|--------|-----------|---------|-----------|
| knowledge pool (~2000 cards) | hybrid | daily | 7 days |
| agent registry (~120 agents) | bm25 | weekly | 30 days |
| real-time market data | bm25 | hourly | 1 day |
| embedding archive (vectors) | faiss | on_change | 0 days |

## Production Counter
| Metric | Value |
|--------|-------|
| Brain indexes produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | BM25/FAISS parameter tuning; hybrid weight balance |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a brain_index, update:
- New common mistake (if encountered)
- New proven brain index pattern (if discovered)
- Production counter increment
