---
id: p11_qg_embedding_config
kind: quality_gate
pillar: P11
title: "Gate: embedding_config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "embedding_config — vector model configuration for RAG pipelines including dimensions, chunking, and distance metrics"
quality: 9.0
tags: [quality-gate, embedding-config, vector, rag, chunking, P11]
tldr: "Gates for embedding_config artifacts: validates model spec, dimension accuracy, chunk size sanity, distance metric validity, and normalization settings."
density_score: 0.90
llm_function: GOVERN
---
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
