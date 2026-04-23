---
kind: quality_gate
id: p11_qg_embedding_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of embedding_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: embedding_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, embedding-config, vector, rag, chunking, P11]
tldr: "Gates for embedding_config artifacts: validates model spec, dimension accuracy, chunk size sanity, distance metric validity, and normalization settings."
domain: "embedding_config — vector model configuration for RAG pipelines including dimensions, chunking, and distance metrics"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.90
related:
  - bld_examples_embedding_config
  - p03_sp_embedding_config_builder
  - bld_architecture_embedding_config
  - p11_qg_embedder_provider
  - p11_qg_dispatch_rule
  - bld_schema_embedding_config
  - p11_qg_chunk_strategy
  - p11_qg_kind_builder
  - p11_qg_batch_config
  - bld_knowledge_card_embedding_config
---

## Quality Gate

# Gate: embedding_config
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: embedding_config` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p01_emb_[a-z][a-z0-9_]+$` | "ID fails embedding_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"embedding_config"` | "Kind is not 'embedding_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, model, provider, dimensions, chunk_size, chunk_overlap, distance_metric, version, created, author, tags | "Missing required field(s)" |
| H07 | `distance_metric` is one of: `cosine`, `dot_product`, `euclidean` | "Invalid distance_metric value" |
| H08 | `chunk_overlap` < `chunk_size` (overlap must be less than full chunk) | "chunk_overlap must be less than chunk_size" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Dimension accuracy | 1.0 | `dimensions` matches documented output size of named model |
| Chunk size justification | 1.0 | chunk_size choice explained relative to model context window |
| Overlap rationale | 1.0 | Overlap percentage reasonable for retrieval quality (10-20% typical) |
| Tokenizer specified | 1.0 | Tokenizer (tiktoken, sentencepiece, etc.) named and version noted |
| Normalization setting | 1.0 | `normalize` flag specified; rationale given for cosine vs dot_product |
| Batch size documented | 0.5 | Recommended batch size for indexing performance stated |
| Provider and cost | 1.0 | Provider (Ollama, OpenAI, etc.) and per-token cost documented |
| Boundary clarity | 0.5 | Explicitly not knowledge_index (search index) or rag_source (data source) |
| Fallback model | 0.5 | Alternative model listed for when primary is unavailable |
| Performance notes | 1.0 | Latency, throughput, or memory footprint characteristics noted |
| Documentation | 0.5 | tldr captures model + key parameters in <= 160 characters |
Weight sum: 1.0+1.0+1.0+1.0+1.0+0.5+1.0+0.5+0.5+1.0+0.5 = 9.0 -> normalize to 100%
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental model evaluation where full parameter tuning is ongoing |
| approver | ML/RAG engineer approval required with written notes |
| audit_trail | Bypass logged to `records/audits/embedding_config_bypass_{date}.md` |
| expiry | 72h; config must be finalized before being wired to a production index |
| never_bypass | H01 (YAML parse failure), H05 (quality null invariant), H08 (overlap >= chunk_size causes indexing corruption) |

## Examples

# Examples: embedding-config-builder
## Golden Example
INPUT: "Configura o nomic-embed-text para o brain index do CEX"
OUTPUT:
```yaml
id: p01_emb_nomic_embed_text
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
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
quality: 8.8
tags: [embedding, ollama, nomic, vector, rag]
tldr: "nomic-embed-text via Ollama — 768d, 512-token chunks, cosine similarity, zero cost local."
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
## Anti-Example
INPUT: "Configure embeddings"
BAD OUTPUT:
```yaml
id: embedding_setup
kind: embedding
pillar: Knowledge
model_name: Some Embedding Model
dimensions: large
chunk_size: a lot
distance_metric: similar
quality: 8.0
tags: embedding
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
