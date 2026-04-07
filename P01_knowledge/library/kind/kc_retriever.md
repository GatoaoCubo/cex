---
id: p01_kc_retriever
kind: knowledge_card
type: kind
pillar: P01
title: "Retriever — Deep Knowledge for retriever"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: retriever
quality: 9.1
tags: [retriever, P04, INJECT, kind-kc, RAG]
tldr: "Searches a local embedding store, keyword index, or hybrid index and returns ranked Document chunks — the core retrieval step of any RAG pipeline"
when_to_use: "Building, reviewing, or reasoning about retriever artifacts"
keywords: [retriever, vector, RAG, embedding, search]
feeds_kinds: [retriever]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Retriever

## Spec
```yaml
kind: retriever
pillar: P04
llm_function: INJECT
max_bytes: 2048
naming: p04_retr_{{store}}.md + .yaml
core: true
```

## What It Is
A retriever searches a local embedding store, keyword index, or hybrid index and returns the top-k ranked Document chunks for injection into the LLM prompt. It is the core retrieval step of any RAG pipeline. It is NOT a search_tool (which queries external web search APIs like Tavily or Serper) nor a document_loader (which ingests raw files into chunks before they can be retrieved).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | BaseRetriever, VectorStoreRetriever, BM25Retriever | .invoke(query) returns List[Document] |
| LlamaIndex | RetrieverQueryEngine, VectorIndexRetriever | Retrieves TextNode from VectorStore index |
| CrewAI | Tool wrapping LC/LI retriever | No native retriever kind |
| DSPy | dspy.Retrieve, ColBERTv2 | Typed module; signature-based retrieval |
| Haystack | InMemoryBM25Retriever, QdrantRetriever | Pipeline component with top_k param |
| OpenAI | File search (Assistants API) | Managed retriever; no external config |
| Anthropic | n/a (no native retrieval) | User-defined retriever via tool_use |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| top_k | int | 5 | Higher = recall; lower = precision |
| search_type | str | vector | vector / keyword / hybrid |
| score_threshold | float | 0.7 | Higher = quality; lower = recall |
| reranker | str | null | Reranker improves precision; adds latency |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Hybrid search | Mixed keyword + semantic queries | BM25 + FAISS merged via RRF score |
| Metadata filter | Domain-scoped retrieval | filter={pillar: "P04"} before vector search |
| Rerank post-retrieval | Precision-critical RAG pipelines | Cohere reranker after top-20 candidates |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No score threshold | Irrelevant low-quality chunks injected | Set score_threshold >= 0.6 |
| top_k too high without reranker | Context window overflow | Use reranker + keep top_k at 5 |
| Skip metadata filter | Cross-domain chunk contamination | Always filter by domain or pillar |

## Integration Graph
```
[user_query] --> [retriever] --> [List[Document] ranked by score]
                     |                       |
         [embedding_model, store]     [LLM prompt injection]
                     |
          [metadata_filter, reranker, top_k]
```

## Decision Tree
- IF searching external web THEN use search_tool
- IF ingesting new files into store THEN use document_loader first
- IF need structured SQL rows THEN use db_connector
- DEFAULT: retriever for any local vector / keyword / hybrid search over indexed data

## Quality Criteria
- GOOD: top_k set, score_threshold set, metadata on each returned result
- GREAT: hybrid search, reranker stage, domain filter, p50 latency < 200ms
- FAIL: no threshold, no metadata filtering, full collection scan without index
