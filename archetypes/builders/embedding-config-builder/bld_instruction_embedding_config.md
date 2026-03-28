---
kind: instruction
id: bld_instruction_embedding_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for embedding_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an embedding_config
## Phase 1: RESEARCH
1. Identify the use case for this embedding configuration: semantic search, clustering, classification, or retrieval-augmented generation
2. Select the embedding model and provider (name, version, and whether it is local or API-hosted)
3. Look up model specifications: output dimensions, maximum input tokens, and tokenizer family
4. Determine the distance metric that matches the use case: cosine for semantic similarity, dot product for maximum inner product search, euclidean for geometric distance
5. Define chunk size and overlap strategy based on content type: fixed-size for uniform documents, semantic boundary for prose, sentence-level for short fragments
6. Assess tokenizer compatibility with the chunking strategy — confirm chunk size in tokens does not exceed the model maximum
7. Check existing embedding_configs via brain_query [IF MCP] for the same provider — do not duplicate a config that already covers this model version
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all 20+ frontmatter fields; set `quality: null` — never self-score
4. Write **Model** section: model name, provider, version, output dimensions
5. Write **Chunking** section: chunk_size (in tokens), overlap (in tokens), chunking strategy with rationale
6. Write **Distance Metric** section: selected metric with one-sentence justification for the use case
7. Write **Tokenizer** section: tokenizer model name, maximum tokens per chunk, handling of overflow
8. Write **Batch Processing** section: batch size, concurrency limit, rate limits imposed by provider
9. Write **Normalization** section: whether L2 normalization is applied, any preprocessing steps before embedding
10. Write **Cost** section: price per 1K tokens (or free if local), estimated monthly cost at expected volume
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually — no automated validator
2. HARD gates: YAML parses, `id` matches `^p01_ec_[a-z][a-z0-9_]+$`, `kind` is the literal string `embedding_config`, model name is specified, dimensions is a numeric integer, chunk_size is defined, distance metric is selected, `quality` is null
3. SOFT gates: score each gate from QUALITY_GATES.md against the artifact
4. Cross-check: is this a model configuration? If it describes the index structure it belongs in `brain_index`. If it describes a data source being indexed it belongs in `rag_source`. If it produces content it belongs in `knowledge_card`. This artifact configures how embeddings are generated, nothing more.
5. If score < 8.0: revise in the same pass before outputting
