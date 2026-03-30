---

```yaml
id: p01_retr_knowledge_nucleus
kind: retriever_config
pillar: P01
version: "1.0.0"
created: "2023-10-17"
updated: "2023-10-17"
author: "builder_agent"
name: "Knowledge Nucleus Retriever Configuration"
store_type: "hybrid_store"
top_k: 10
search_type: "hybrid"
quality: null
tags: [retriever_config, knowledge, hybrid]
tldr: "Hybrid retriever for Knowledge Nucleus integrating vector and keyword search."
```

## Overview
The Knowledge Nucleus Retriever Configuration is designed to optimize retrieval operations in the Knowledge Nucleus system. It integrates both vector and keyword search methodologies to improve retrieval precision and recall, accommodating a wide range of user queries.

## Search Strategy
This configuration employs a hybrid search strategy leveraging both vector similarity and keyword matching. The algorithm uses a Reciprocal Rank Fusion (RRF) approach with a higher weight on vector-based similarity to prioritize semantic matching. It retrieves the top 30 candidates and applies a reranking mechanism using a cross-encoder for final ranking.

## Parameters
| Parameter      | Value        | Rationale                                                     |
|----------------|--------------|---------------------------------------------------------------|
| store_type     | hybrid_store | Supports both semantic and lexical queries efficiently.       |
| top_k          | 10           | Balances between providing meaningful results and efficiency. |
| search_type    | hybrid       | Ensures robust handling of diverse query types.               |
| hybrid_ratio   | 0.6          | Favors semantic understanding while allowing keyword precision. |
| fetch_k        | 30           | Provides adequate candidate pool for reranking.               |
| reranker       | cross-encoder/ms-marco | Enhances the accuracy of the top results.             |
| score_threshold | 0.2         | Filters out less relevant results for clearer output.         |

## Integration
- **Input**: Accepts natural language queries with optional metadata constraints.
- **Output**: Returns a ranked list of documents with relevance scores.
- **Upstream**: Relies on a well-structured chunking and embedding process.
- **Downstream**: Integrates with the Knowledge Nucleus's retrieval-augmented generation processes, supporting LLM-based systems that require contextually rich inputs.

---