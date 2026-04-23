---
kind: quality_gate
id: p11_qg_retriever
pillar: P11
llm_function: GOVERN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [quality_gate, retriever, P11, validation, RAG, vector-search]
density_score: 1.0
domain: "examples artifact construction"
title: Quality Gate ISO - retriever
tldr: "10 HARD gates block delivery. 12 SOFT dimensions score 0-10. Threshold 7.0."
related:
  - bld_examples_retriever
  - bld_instruction_retriever
  - p03_sp_retriever_builder
  - bld_output_template_retriever
  - retriever-builder
  - bld_schema_retriever
  - bld_memory_retriever
  - bld_tools_retriever
  - bld_examples_retriever_config
  - bld_collaboration_retriever
---

## Quality Gate

# Gate: retriever

## Definition
- Metric: composite score 0-10
- Threshold: >= 7.0 to deliver
- HARD gates: block delivery regardless of score
- SOFT gates: contribute to composite score

## HARD Gates (all must pass — any failure blocks delivery)

| ID | Check | Fail Action |
|----|-------|-------------|
| H01 | YAML frontmatter parses without errors | Fix syntax |
| H02 | id matches `^p04_retr_[a-z][a-z0-9_]+$` AND equals filename stem | Fix id or rename file |
| H03 | kind == "retriever" (exact string) | Fix kind field |
| H04 | quality == null (not a number, not absent) | Remove numeric score |
| H05 | All required fields present: id, name, store_type, embedding_model, similarity_metric, top_k | Add missing fields |
| H06 | store_type is valid enum: chroma, pinecone, faiss, qdrant, weaviate, milvus, elasticsearch, costm | Fix to valid value |
| H07 | embedding_model is a non-empty string | Specify model name |
| H08 | similarity_metric is valid enum: cosine, dot_product, euclidean, manhattan | Fix to valid value |
| H09 | top_k >= 1 (integer) | Fix to positive integer |
| H10 | Body byte count <= 2048 (sections only, excludes frontmatter) | Trim content |

## SOFT Scoring (12 dimensions, each 0-1, sum * 10/12)

| ID | Dimension | Weight | Criteria |
|----|-----------|--------|----------|
| S01 | store_coverage | 1.0 | store_type matches real backend; version/tier noted if relevant |
| S02 | embedding_model_docs | 1.0 | model name, provider, dimension size documented |
| S03 | similarity_justification | 1.0 | metric choice explained relative to embedding model |
| S04 | hybrid_strategy | 0.8 | if hybrid: fusion method (RRF/weighted) and alpha specified |
| S05 | reranking_config | 0.8 | reranker null OR model named with trigger condition |
| S06 | metadata_filter_docs | 0.8 | filters listed with field names and types |
| S07 | namespace_scoping | 0.7 | namespace/collection specified or explicitly "default" |
| S08 | integration_docs | 1.0 | SDK/library named, auth pattern, connection string format |
| S09 | boundary_clarity | 1.0 | explicitly states what this is NOT (web search, ingestion, SQL) |
| S10 | domain_specificity | 0.9 | use case context clear; not generic "search documents" |
| S11 | testsbility | 0.8 | enough info to write a retrieval test (store + model + k) |
| S12 | error_handling | 0.5 | notes fallback behavior if store unavailable or score below threshold |

## Scoring Tiers

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Pool as golden artifact |
| >= 8.0 | Skilled | Pool + remember pattern |
| >= 7.0 | Learning | Deliver with notes |
| < 7.0 | Rejected | Revise before delivery |

## Bypass
No bypass for HARD gates. SOFT gate threshold may be reduced to 6.0 only when:
- Prototype/draft explicitly requested by user
- store_type is "costm" with acknowledged unknowns
Document bypass reason in artifact description field.

## Examples

# Examples: retriever-builder

## Golden Example

**INPUT**: "Create a hybrid retriever for a Qdrant store using Cohere embed-v3 embeddings
with reranking for a technical documentation RAG system."

**OUTPUT**:
```markdown
---
id: p04_retr_qdrant_hybrid_docs
kind: retriever
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: retriever-builder
name: "Qdrant Hybrid Retriever — Technical Docs"
store_type: qdrant
embedding_model: embed-english-v3.0
similarity_metric: dot_product
top_k: 50
search_type: hybrid
reranker: rerank-english-v3.0
metadata_filters: [source, version, category, language]
namespace: technical_docs
quality: null
tags: [retriever, qdrant, hybrid, cohere, reranking, technical-docs]
tldr: "Qdrant hybrid retriever using Cohere embed-v3 + BM25 with Cohere reranking for technical documentation RAG."
description: "Searches technical documentation collection using dense+sparse fusion, reranks top-50 to top-5 for precision."
---

## Overview
Qdrant vector store serving a technical documentation corpus. Uses Cohere embed-english-v3.0
(1024d, natively normalized) as the dense encoder. Designed for developer documentation RAG
where exact API names (keyword) and semantic intent (vector) both matter.

## Search Strategy
Hybrid search combining Qdrant's dense vectors with sparse BM25 index. Fusion via
Reciprocal Rank Fusion (RRF, k=60): balances semantic similarity and exact term matching
for technical queries like "list all methods of class X" or "explain async context manager."
dot_product metric used because Cohere embed-v3 vectors are natively normalized.
Cohere rerank-english-v3.0 applied after first-pass top_k=50 to return final top-5.

## Configuration
- top_k: 50 (first-pass); reranker returns top 5 for generation
- metadata_filters: source (file path), version (doc version string), category (api/guide/tutorial), language (en/pt)
- namespace: technical_docs
- score_threshold: 0.35 (discard low-confidence matches before reranking)
- chunk_size_assumption: 512 tokens from document_loader

## Integration
- SDK/library: qdrant-client + langchain QdrantVectorStore + cohere Python SDK
- auth: QDRANT_API_KEY env var (cloud) or none (local http://localhost:6333)
- connection: QDRANT_URL + QDRANT_API_KEY env vars; collection name = "technical_docs"
- embedding_call: CohereEmbeddings(model="embed-english-v3.0", input_type="search_query")
```

**WHY GOLDEN**: H01-H10 all pass. S01-S12 average ~9.4 — qdrant+Cohere+RRF+reranker+metadata+SDK all documented.

---

## Anti-Example

**INPUT**: "Create retriever"

**BAD OUTPUT**:
```markdown
---
id: retriever_1
kind: retriever
store_type: vector
embedding_model: embeddings
top_k: 100
quality: 8.5
tags: [search]
---
Searches documents using vectors.
```

**FAILURES**:
- H01: parses but H02 fails — id "retriever_1" does not match `^p04_retr_[a-z][a-z0-9_]+$`
- H03: kind == "retriever" passes but H04 fails — quality: 8.5 (must be null)
- H05: missing name, similarity_metric; pillar, version, created, updated, author, tldr all absent
- H06: store_type "vector" is not a valid enum value
- H07: embedding_model "embeddings" is too vague — no provider or model name
- H08: similarity_metric absent
- S01-S12: ~1.2/10 — no strategy, no config, no integration
- Body 1 line — missing Overview, Search Strategy, Configuration, Integration

## Cross-References

- **Pillar**: P07 (Evals)
- **Kind**: `examples`
- **Artifact ID**: `bld_examples_retriever`
- **Tags**: [examples, retriever, P07, RAG, vector-search, hybrid-search]

## Example Registry

| Aspect | Detail |
|--------|--------|
| Purpose | Few-shot exemplar for builder prompts |
| Injection | Loaded by `cex_skill_loader.py` at F3 |
| Quality | Must score 9.0+ to serve as exemplar |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
