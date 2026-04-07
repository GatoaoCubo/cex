---
kind: config
id: bld_config_vector_store
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 25
disallowed_tools: []
fork_context: inline
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: vector_store Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_vdb_{backend}.yaml` | `p01_vdb_pinecone.yaml` |
| Builder directory | kebab-case | `vector-store-builder/` |
| Frontmatter fields | snake_case | `distance_metric`, `ef_construction` |
| Backend values | lowercase single word | `pinecone`, `pgvector`, `chroma`, `faiss` |
| Collection names | snake_case with domain prefix | `cex_knowledge`, `cex_marketing` |
Rule: id MUST equal filename stem (validator checks this).
## File Paths
- Output: `cex/P01_knowledge/examples/p01_vdb_{backend}.yaml`
- Compiled: `cex/P01_knowledge/compiled/p01_vdb_{backend}.yaml`
## Size Limits (aligned with SCHEMA)
- Frontmatter: ~700-1000 bytes (22+ fields)
- Body: max 4096 bytes (excl frontmatter)
- Total: max 5100 bytes
- Density: >= 0.85
## Backend Enum
Valid: pinecone, pgvector, chroma, faiss, qdrant, weaviate, milvus, other
If backend not in list: use "other" and add backend name in tags.
## Dimension Policy
- ALWAYS match upstream embedder_provider dimensions exactly
- NEVER set dimensions independently of the embedding model
- Common dimensions: 384, 512, 768, 1024, 1536, 3072
- If embedder uses matryoshka reduction: use the reduced dimension
## Distance Metric Policy
- cosine: for L2-normalized embeddings (OpenAI, most cloud providers)
- l2 (euclidean): for raw unnormalized embeddings
- dot_product: mathematically equivalent to cosine for normalized vectors, but use cosine for clarity
- inner_product: Pinecone, Milvus naming for dot product
- ALWAYS align with the upstream embedder_provider's normalization setting
## HNSW Parameter Policy
- M: 16 default (higher = better recall, more memory, slower build)
- ef_construction: 200 default (higher = better index quality, slower build)
- ef_search: 100 default (higher = better recall at query time, slower queries)
- For small datasets (<10K): use flat index, HNSW overhead not justified
- For large datasets (>1M): consider IVF-PQ for memory efficiency
## Persistence
- Pinecone: cloud-managed, automatic
- pgvector: PostgreSQL durability, automatic
- Chroma: configurable (ephemeral, persistent path, client-server)
- FAISS: IN-MEMORY ONLY — MUST explicitly save/load via faiss.write_index/read_index
- Qdrant: configurable (in-memory, on-disk, distributed)
## Freshness
- updated field must be within 90 days of current date
- Backend APIs change less frequently than LLM providers
- Reindex triggers: schema change, embedding model change, dimension change
