---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for embedding_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an embedding_config

## Phase 1: DISCOVER
1. Identify the embedding model: name and provider
2. Check brain_query [IF MCP] for existing embedding_configs (avoid duplicates)
3. Look up model specs: dimensions, max tokens, tokenizer
4. Determine chunk_size based on use case (RAG retrieval, classification, search)
5. Check cost: free/local or API pricing per 1M tokens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 22 fields (null OK for optional)
4. Set quality: null (NEVER self-score)
5. Write Model section: model name, provider, key specs
6. Write Chunking section: chunk_size, overlap, tokenizer strategy
7. Write Performance section: latency, throughput, cost
8. Write Integration section: how to use in RAG pipeline

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually (no automated validator yet)
2. HARD gates (all must pass): YAML parses, id matches p01_emb_ pattern, kind == embedding_config, dimensions is integer, quality == null
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: still a model config? Not drifting into index configuration? Not drifting into source indexing?
5. If score < 8.0: revise in same pass before outputting
