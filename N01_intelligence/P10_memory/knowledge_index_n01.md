---
id: knowledge_index_n01
kind: knowledge_index
8f: F3_inject
pillar: P10
nucleus: n01
title: "N01 Intelligence Corpus Index"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [knowledge_index, corpus_index, n01, retrieval, search, analytical_envy]
tldr: "Master index of the N01 intelligence corpus: 60+ knowledge cards, entity profiles, research outputs, and compiled artifacts. Enables retriever_n01 to perform sub-500ms corpus queries. Updated on every F8 COLLABORATE."
density_score: 0.90
updated: "2026-04-17"
related:
  - bld_collaboration_knowledge_index
  - knowledge-index-builder
  - bld_collaboration_embedding_config
  - p01_kc_knowledge_index
  - bld_architecture_knowledge_index
  - bld_instruction_knowledge_index
  - bld_examples_knowledge_index
  - n04_knowledge_memory_index
  - bld_knowledge_card_knowledge_index
  - bld_tools_knowledge_index
---

<!-- 8F: F1 constrain=P10/knowledge_index F2 become=knowledge-index-builder F3 inject=knowledge_index_intelligence+retriever_n01+entity_memory_n01+embedding_config_intelligence F4 reason=Analytical Envy = insatiable data hunger; an unindexed corpus is data you cannot use -- the index IS the intelligence F5 call=cex_compile F6 produce=knowledge_index_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P10_memory/ -->

## Purpose

N01 has 167+ artifacts. Without an index, retrieval degrades to linear scan.
This knowledge index maintains:
1. A BM25-indexed corpus for keyword search
2. A dense embedding index for semantic search
3. An entity registry pointing to `entity_memory_n01.md` profiles
4. A metadata index for pillar-filtered lookups

The index is the intelligence multiplier: same corpus, 10x faster retrieval.

## Corpus Coverage

| Pillar | Document Count | Primary Types |
|--------|---------------|---------------|
| P01 Knowledge | 60+ | knowledge_card, citation, glossary_entry |
| P04 Tools | 9+ | research_pipeline, search_strategy, browser_tool |
| P06 Schema | 11+ | input_schema, type_def, api_reference |
| P07 Evals | 23+ | eval_framework, scoring_rubric, benchmark |
| P10 Memory | 10+ | entity_memory, checkpoint, embedding_config |
| P11 Feedback | 3+ | quality_gate, bias_audit, self_improvement_loop |
| P03 Prompt | 5+ | system_prompt, reasoning_strategy, prompt_template |
| Other pillars | 45+ | varies |
| **Total** | **167+** | all kinds |

## Index Structure

### BM25 Index

| Field | Configuration |
|-------|--------------|
| Library | rank_bm25 (BM25Okapi) |
| Tokenizer | whitespace + lowercase + stop-word removal |
| Fields indexed | title + content + tags (concatenated) |
| Corpus update | on every F8 COLLABORATE (file write) |
| Index location | `.cex/cache/n01_bm25_index.pkl` |
| Cold build time | < 5s for 200 docs |

### Dense Embedding Index

| Field | Configuration |
|-------|--------------|
| Model | sentence-transformers/all-MiniLM-L6-v2 |
| Dimension | 384 |
| Similarity | cosine |
| Store | `.cex/cache/n01_embeddings.npy` + `.cex/cache/n01_doc_ids.json` |
| Cold build time | < 30s for 200 docs |
| Per-doc embedding | title + first 512 chars of content |

### Metadata Index

| Field | Type | Purpose |
|-------|------|---------|
| `doc_id` | string | relative file path |
| `kind` | string | CEX kind |
| `pillar` | string | P01-P12 |
| `title` | string | artifact title |
| `tags` | string[] | artifact tags |
| `quality` | float or null | last quality score |
| `created` | ISO8601 | creation date |
| `last_updated` | ISO8601 | last modification |
| `word_count` | int | content length signal |
| `density_score` | float | content density |

Stored at: `.cex/cache/n01_metadata_index.json`

## Entity Registry

Sub-index pointing to entity profiles:

| Entity Type | Count (est.) | Location |
|-------------|-------------|---------|
| Companies | 20+ | `P10_memory/entities/co_*.yaml` |
| People | 10+ | `P10_memory/entities/pe_*.yaml` |
| Events | 50+ | `P10_memory/events/ev_*.yaml` |

## Index Build / Update Protocol

```
on_f8_collaborate(new_file_path):
  doc = load(new_file_path)
  bm25_index.add(doc)
  embedding = embedder.encode(doc.title + " " + doc.content[:512])
  embeddings_store.add(doc.doc_id, embedding)
  metadata_index[doc.doc_id] = extract_metadata(doc)
  save_all_indexes()
```

Full rebuild:
```bash
python _tools/cex_index.py --target N01_intelligence --output .cex/cache/n01_*
```

## Query Interface

```python
# Keyword search
results = bm25_index.search(query, top_k=20)

# Semantic search
results = embedding_index.search(query, top_k=20)

# Pillar-filtered metadata lookup
results = metadata_index.filter(pillar="P01", kind="knowledge_card")

# Entity lookup
entity = entity_registry.get(name="Anthropic")
```

## Staleness Detection

| Index | Stale Condition | Rebuild Trigger |
|-------|----------------|----------------|
| BM25 | new file not in index | on F8, auto-incremental |
| Embeddings | new file not in store | on F8, auto-incremental |
| Metadata | mtime changed | on F8, auto-update |
| Entities | entity.last_updated > 90d | on competitor_monitor signal |

## Performance Targets

| Operation | Target | Alert |
|-----------|--------|-------|
| BM25 query | < 100ms | > 500ms |
| Embedding query | < 300ms | > 1s |
| Metadata filter | < 50ms | > 200ms |
| Full rebuild | < 60s | > 120s |
| Index size (200 docs) | < 50MB | > 200MB |

## Comparison vs. Alternatives

| Approach | Build Time | Query Speed | Memory | N01 Fit |
|----------|-----------|------------|--------|---------|
| Linear scan (no index) | 0 | O(n) slow | 0 | fail at 200+ docs |
| Full vector DB (Pinecone) | fast | fast | cloud cost | overkill |
| This index (local hybrid) | < 60s | < 400ms | < 50MB | optimal |
| SQLite FTS | < 30s | < 200ms | < 20MB | keyword only |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_index]] | downstream | 0.49 |
| [[knowledge-index-builder]] | related | 0.46 |
| [[bld_collaboration_embedding_config]] | downstream | 0.39 |
| [[p01_kc_knowledge_index]] | related | 0.34 |
| [[bld_architecture_knowledge_index]] | upstream | 0.30 |
| [[bld_instruction_knowledge_index]] | upstream | 0.29 |
| [[bld_examples_knowledge_index]] | upstream | 0.29 |
| [[n04_knowledge_memory_index]] | related | 0.28 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.28 |
| [[bld_tools_knowledge_index]] | upstream | 0.28 |
