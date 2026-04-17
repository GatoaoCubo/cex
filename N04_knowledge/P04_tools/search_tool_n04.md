---
id: p04_st_n04_knowledge
kind: search_tool
pillar: P04
nucleus: n04
title: "Search Tool -- N04 Knowledge Corpus Search"
version: "1.0.0"
quality: null
tags: [search_tool, n04, hybrid_search, semantic, lexical, BM25, reranker, P04]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "N04 corpus search tool: semantic + lexical hybrid search with cross-encoder reranking. Consumes input_schema_knowledge_query.md as its input contract. Returns ranked passages with source citations."
density_score: null
---

# Search Tool: N04 Knowledge Corpus Search

## Overview

The N04 search tool is the query interface to the semantic corpus. It implements
the READ PIPELINE from `memory_architecture_n04.md` layers 3-4 (semantic + procedural).

Input contract: `input_schema_knowledge_query.md` (P06)
Output: ranked passages or document references

---

## Search Modes

| Mode | Algorithm | When to Use | Latency |
|------|-----------|------------|---------|
| `dense` | cosine similarity on text-embedding-3-small | Semantic/conceptual queries | 180ms |
| `sparse` | BM25 TF-IDF (cex_retriever.py, 12K vocab) | Exact keyword, technical terms | 45ms |
| `hybrid` | RRF merge of dense + sparse (default) | Most queries | 220ms |
| `graph` | Knowledge graph traversal (Neo4j if available) | Multi-hop reasoning | 500ms+ |
| `procedural` | Exact string match on SOP index | "how to do X" queries | < 1ms |

---

## Search Pipeline

```
Query Input (conforms to input_schema_knowledge_query.md)
       |
       v
QUERY PREPROCESSING
  |-- Validate schema
  |-- Optional: query expansion (HyDE if query_expansion=true)
  |-- Optional: query rewriting (ambiguous queries)
       |
       v
PARALLEL RETRIEVAL
  |-- Dense: embed query -> cosine search -> top-20 candidates
  |-- Sparse: BM25 index search -> top-20 candidates
       |
       v
MERGE (Reciprocal Rank Fusion, k=60)
  RRF_score(d) = sum(1 / (k + rank_i(d)) for all retrieval systems i)
       |
       v
APPLY FILTERS (if provided in input)
  |-- kind, pillar, nucleus scope filters applied post-merge
       |
       v
RERANKING (if rerank=true, default)
  |-- Load top-20 merged results
  |-- Cross-encoder: score each (query, passage) pair
  |-- Re-sort by cross-encoder score
  |-- Return top_k results
       |
       v
FORMAT OUTPUT
  |-- passages: text excerpts with source + score
  |-- summaries: 1-2 sentence summaries
  |-- full_docs: complete document content
  |-- citations_only: source path + score
```

---

## Query Expansion (HyDE)

When `query_expansion=true`:

```python
def hyde_expand(query: str, llm) -> str:
    """
    Hypothetical Document Embeddings:
    Generate a hypothetical answer, embed it, use that embedding for retrieval.
    Much better zero-shot recall for obscure topics.
    """
    hypothetical = llm.generate(
        f"Write a short expert answer to: {query}\n\nAnswer:"
    )
    return hypothetical
```

Use only for multi-hop reasoning or obscure domain queries. Adds ~3x latency.

---

## Python Interface

```python
from cex_sdk.search import KnowledgeSearch

search = KnowledgeSearch(
    corpus="cex_artifacts",
    mode="hybrid",
    top_k=10,
    score_threshold=0.65,
    rerank=True
)

results = search.query(
    query_text="how does 8F pipeline work in N04",
    filters={"kind": "knowledge_card"},
    output_format="passages"
)

for result in results:
    print(f"[{result.score:.2f}] {result.source}")
    print(result.content[:200])
    print()
```

---

## CLI Interface

```bash
python _tools/cex_retriever.py \
  --query "RAG architecture for knowledge management" \
  --mode hybrid \
  --top-k 10 \
  --threshold 0.65 \
  --format passages \
  --filter-kind knowledge_card
```

---

## Result Schema

```python
@dataclass
class SearchResult:
    content: str         # retrieved text
    score: float         # 0.0-1.0 similarity score
    source: str          # relative file path
    metadata: dict       # kind, pillar, nucleus, quality
    rank: int            # position in result list (1-indexed)
```

---

## Cross-Corpus Search

When `corpus="all"`, search runs against all three namespaces:
1. `cex_artifacts` (internal CEX knowledge)
2. `external_docs` (ingested external sources)
3. `session_memory` (recent episodic summaries)

Results are merged via RRF. Scores are normalized per corpus before merging.
`session_memory` results get a recency boost: `boosted_score = score * (1 + 0.2 * recency_factor)`
where `recency_factor = max(0, 1 - days_old / 7)`.

---

## Fallback Chain

```
1. pgvector (primary) -- if Supabase available
2. ChromaDB (local fallback) -- if Supabase unavailable
3. cex_retriever.py TF-IDF (zero-dependency fallback) -- always available
4. Grep-based keyword search -- emergency fallback (no embedding needed)
```

---

## Integration

| Artifact | Role |
|---------|------|
| `input_schema_knowledge_query.md` | Input contract (query validation) |
| `retriever_n04.md` | Retriever config consumed by this tool |
| `api_reference_rag_apis.md` | pgvector and Pinecone API calls |
| `memory_benchmark_n04.md` | Baseline metrics -- regression check |
| `eval_dataset_n04.md` | Test queries for benchmark runs |
