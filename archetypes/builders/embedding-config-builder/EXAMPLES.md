---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of embedding_config artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: embedding-config-builder

## Golden Example

INPUT: "Configura o nomic-embed-text para o brain index do CEX"

OUTPUT:

```yaml
---
id: p01_emb_nomic_embed_text
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
model_name: "nomic-embed-text"
provider: "ollama"
dimensions: 768
chunk_size: 512
overlap: 50
tokenizer: "nomic-bert"
distance_metric: "cosine"
batch_size: 32
normalize: true
max_tokens: 8192
cost_per_1m_tokens: null
domain: "knowledge-retrieval"
quality: null
tags: [embedding, ollama, nomic, vector, rag]
tldr: "nomic-embed-text via Ollama — 768d, 512-token chunks, cosine similarity, zero cost local."
---
```

## Model
nomic-embed-text by Nomic AI, served locally via Ollama.
768 dimensions, 8192 max input tokens. Top-tier open model on MTEB retrieval tasks.

## Chunking
512-token chunks with 50-token overlap (10%). Tokenizer: nomic-bert.
Optimized for paragraph-level retrieval in knowledge cards and documentation.

## Performance
- Latency: ~50ms per batch (32 vectors) on local GPU
- Throughput: ~1000 chunks/minute
- Cost: zero (local Ollama, no API fees)
- Quality: MTEB retrieval score ~0.52 (competitive with text-embedding-3-small)

## Integration
```python
# Ollama embedding call
ollama.embeddings(model="nomic-embed-text", prompt=chunk_text)
```
Index: FAISS IndexFlatIP (cosine with normalized vectors).
Rebuild: `python build_indexes_ollama.py --scope all`

## References
- Nomic AI nomic-embed-text model card
- MTEB Benchmark leaderboard (retrieval tasks)

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_emb_ pattern (H02 pass)
- kind: embedding_config (H04 pass)
- 22 frontmatter fields present (H06 pass)
- dimensions is integer 768 (H07 pass)
- chunk_size is integer 512 (H08 pass)
- model_name non-empty (H09 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "embedding" (S02 pass)
- All 4 body sections present (S03-S06 pass)

---

## Anti-Example

INPUT: "Configure embeddings"

BAD OUTPUT:

```yaml
---
id: embedding_setup
kind: embedding
pillar: Knowledge
model_name: Some Embedding Model
dimensions: large
chunk_size: a lot
distance_metric: similar
quality: 8.0
tags: embedding
---
```

This configures embeddings for the system. It uses a good model with large dimensions
and processes text in big chunks for optimal performance and results.

FAILURES:
1. id: no `p01_emb_` prefix -> H02 FAIL
2. kind: "embedding" not "embedding_config" -> H04 FAIL
3. pillar: "Knowledge" not "P01" -> H01 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. dimensions: "large" not integer -> H07 FAIL
6. chunk_size: "a lot" not integer -> H08 FAIL
7. distance_metric: "similar" not in enum (cosine, euclidean, dot_product) -> H10 FAIL
8. tags: string not list, len < 3 -> S02 FAIL
9. model_name: vague "Some Embedding Model" -> S05 FAIL
10. body: filler prose ("good model", "optimal performance") -> S07 FAIL
11. Missing fields: version, created, updated, author, provider, domain, tldr -> H06 FAIL
