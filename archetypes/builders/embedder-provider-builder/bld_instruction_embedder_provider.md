---
id: p03_ins_embedder_provider
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: instruction-builder
title: Embedder Provider Builder Execution Protocol
target: embedder-provider-builder agent
phases_count: 4
prerequisites:
  - Embedding provider and model are identified
  - Provider API documentation is accessible (model page, dimensions, rate limits)
  - The embedding model is not already configured in the P01 examples directory
validation_method: checklist
domain: embedder_provider
quality: 9.1
tags: [instruction, embedder-provider, P01, embedding, dimensions, normalization]
idempotent: true
atomic: false
rollback: "Discard generated artifact; no embedding index is modified"
dependencies: []
logging: true
tldr: Research and configure an embedding model's connection parameters, dimensions, normalization, and batch limits from official sources into a complete embedder_provider artifact.
density_score: 0.90
llm_function: REASON
---
## Context
The embedder-provider-builder produces `embedder_provider` artifacts (P01) — embedding model connection configurations for RAG pipelines. Configs specify the exact provider API, model identifier, embedding dimensions, normalization behavior, batch size limits, and authentication. An embedder_provider is a connection spec, not a vector database config (vector_store), not an LLM routing rule (model_provider), and not a retrieval pipeline (retriever).
**Inputs:**
- `$provider (required) - string - "One of: openai, cohere, voyage, jina, nomic, local, other"`
- `$model (required) - string - "Exact model identifier as used in the provider API (e.g. 'text-embedding-3-small', 'embed-english-v3.0', 'all-MiniLM-L6-v2')"`
- `$use_case (optional) - string - "Target use case: semantic search, clustering, classification, code search"`
- `$dimension_override (optional) - integer - "Reduced dimension count for matryoshka-capable models"`
**Output:** A single `embedder_provider` artifact with 20+ frontmatter fields and 5 body sections: Boundary, Configuration Matrix, Dimension Tradeoffs, Integration Pattern, Anti-Patterns. Body <= 4096 bytes.
## Phases
### Phase 1: Research
**Action:** Gather all embedding model specifications from official sources.
1. Identify the model: exact API name, provider, version.
2. Locate official documentation:
   - Provider embedding model page (dimensions, capabilities)
   - API reference (max tokens, batch limits, rate limits)
   - Pricing page (per-token or per-request costs)
   - MTEB benchmark results (retrieval, clustering, classification scores)
3. Extract all schema fields from official sources:
   - `dimensions`: integer, native embedding dimension
   - `max_tokens`: integer, max input tokens per request
   - `batch_size`: integer, max texts per batch request
   - `normalize`: boolean, whether output is L2-normalized
   - `truncate`: boolean or string, truncation behavior on overflow
   - `matryoshka`: boolean, supports dimension reduction via MRL
   - `sparse_support`: boolean, supports hybrid dense+sparse
   - `api_key_env`: string, environment variable name for authentication
4. Rule: if a data point is unavailable, set field to `null` — never infer.
5. Check for existing embedder_provider artifacts for the same model to avoid duplicates.
**Verification:** Every non-null field has a source URL identified. Dimensions match official documentation exactly.
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 4096-byte body limit.
1. Read SCHEMA — source of truth for all fields.
2. Read OUTPUT_TEMPLATE — fill every `{{var}}` following schema constraints.
3. Fill frontmatter: all required fields (`null` valid for optional; `quality: null` mandatory).
4. Write `## Boundary` section — what an embedder_provider IS and IS NOT.
5. Write `## Configuration Matrix` table:
   | Parameter | Value | Source |
   |-----------|-------|--------|
   Rows: provider, model, dimensions, max_tokens, batch_size, normalize, truncate, distance_metric, pricing.
6. Write `## Dimension Tradeoffs` — table comparing native vs reduced dimensions:
   | Dimensions | MTEB Score | Storage | Latency | Use Case |
   |------------|------------|---------|---------|----------|
7. Write `## Integration Pattern` — code snippet showing provider SDK initialization.
8. Write `## Anti-Patterns` — >= 4 common mistakes with this embedding model.
9. Write `## References` — >= 1 official URL.
**Verification:** Every Configuration row has Source URL. Dimensions are integers. Body <= 4096 bytes.
### Phase 3: Validate
**Action:** Run all 10 HARD gates. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches `^p01_emb_[a-z][a-z0-9_]+$` |
| H03 | `id` equals filename stem exactly |
| H04 | `kind` == literal string `"embedder_provider"` |
| H05 | `quality` == `null` |
| H06 | Required fields present: `id`, `kind`, `pillar`, `provider`, `model`, `dimensions`, `max_tokens`, `normalize` |
| H07 | `provider` matches a known enum value |
| H08 | `dimensions` is a positive integer |
| H09 | `max_tokens` is a positive integer |
| H10 | Body <= 4096 bytes |
Score all SOFT gates. If soft score < 8.0, revise in the same pass.
### Phase 4: Deliver
**Action:** Save, compile, commit, signal.
1. Save artifact to `P01_knowledge/examples/p01_emb_{provider}_{model_slug}.md`
2. Compile: `python _tools/cex_compile.py {path}`
3. Git commit with descriptive message
4. Signal: `write_signal('n03', 'complete', {score})`
