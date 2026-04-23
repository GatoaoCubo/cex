---
kind: quality_gate
id: p11_qg_retriever_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of retriever_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: retriever_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, retriever-config, P01]
tldr: "Pass/fail gate for retriever_config artifacts: required fields, id pattern, body sections, parameter completeness."
domain: "retrieval configuration for RAG search"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_retriever_config
  - p11_qg_chunk_strategy
  - p11_qg_memory_scope
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_constraint_spec
  - p11_qg_prompt_version
  - bld_instruction_retriever_config
  - p11_qg_effort_profile
  - p10_lr_retriever_config_builder
---

## Quality Gate

# Gate: retriever_config
## Definition
| Field | Value |
|---|---|
| metric | retriever_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: retriever_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p01_retr_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `retriever_config` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Search Strategy or ## Parameters or ## Integration |
| H08 | Body <= 2048 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Parameter completeness | 1.0 | All parameters have concrete values (no placeholders) |
| Rationale quality | 1.0 | Each parameter value has clear rationale |
| Pattern selection | 1.0 | Correct pattern chosen for the use case |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "retriever_config", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Parameters and values specific to declared domain |
| Testability | 0.5 | Configuration can be validated with known inputs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Examples

# Examples: retriever-config-builder
## Golden Example
INPUT: "Create retriever config for hybrid search over knowledge base"
OUTPUT:
```yaml
id: p01_retr_hybrid_knowledge
kind: retriever_config
pillar: P01
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Hybrid Knowledge Base Retriever"
quality: null
tags: [retriever_config, P01, retriever]
tldr: "Hybrid Knowledge Base Retriever — production-ready retriever_config configuration"
```
## Overview
Hybrid retriever combining FAISS dense search with BM25 sparse search for knowledge base queries.
Balances semantic understanding with keyword precision.

## Search Strategy
Algorithm: hybrid (reciprocal rank fusion)
Dense: FAISS cosine similarity on nomic-embed-text vectors.
Sparse: BM25 keyword matching on raw chunk text.
Fusion: RRF with k=60, dense_weight=0.7, sparse_weight=0.3.
Reranker: cross-encoder/ms-marco-MiniLM-L-6-v2 on top 15 candidates.

## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| store_type | faiss | Local, fast, no external dependency |
| top_k | 5 | Balances context window budget with recall |
| search_type | hybrid | Best F1 for mixed query types |
| hybrid_ratio | 0.7 | Dense-weighted; semantic queries dominate |
| fetch_k | 15 | 3x top_k for reranker input |
| reranker | ms-marco-MiniLM-L-6-v2 | Fast cross-encoder, <50ms latency |
| score_threshold | 0.3 | Drops irrelevant results on weak queries |

## Integration
- Input: query string + optional metadata filters
- Output: list of (Document, score) tuples, ranked by relevance
- Upstream: p01_chunk_tech_docs (chunks), p01_emb_nomic (embeddings)
- Downstream: LLM context assembly, RAG prompt injection
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_retr_ pattern (H02 pass)
- kind: retriever_config (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Search Strategy, Parameters, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "retriever_config" (S02 pass)
## Anti-Example
INPUT: "Create retriever for product search"
BAD OUTPUT:
```yaml
id: product-search
kind: retriever
quality: 9.0
tags: [retriever]
```
FAILURES:
1. id has hyphens and no p01_retr_ prefix -> H02 FAIL
2. kind: 'retriever' not 'retriever_config' -> H04 FAIL
3. Missing fields: store_type, top_k, search_type -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. No ## Search Strategy section -> H07 FAIL
6. No parameters table -> S03 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
