---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: embedding-config-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p01_emb_nomic_embed_text, not p01_emb_nomic-embed-text)
3. Writing dimensions as string "768" instead of integer 768
4. Writing chunk_size as string instead of integer
5. Using invalid distance_metric (must be cosine, euclidean, or dot_product)
6. Forgetting normalize: true when using cosine distance (required for correct similarity)
7. Guessing cost instead of using null for local/free models
8. Drifting into index configuration (FAISS params belong in brain_index P10)

### Embedding Model Reference

| Model | Provider | Dims | Cost/1M | Quality (MTEB) |
|-------|----------|------|---------|----------------|
| nomic-embed-text | ollama | 768 | free | 0.52 |
| mxbai-embed-large | ollama | 1024 | free | 0.54 |
| text-embedding-3-small | openai | 1536 | $0.02 | 0.51 |
| text-embedding-3-large | openai | 3072 | $0.13 | 0.55 |
| embed-english-v3.0 | cohere | 1024 | $0.10 | 0.56 |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | dimensions lookup, cost accuracy, chunk_size tuning |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an embedding_config, update:
- New common mistake (if encountered)
- New model entry in reference table (if discovered)
- Production counter increment
