# P01 Knowledge — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| LlamaIndex | RAG framework | Document, TextNode, ImageNode, NodeParser, VectorStoreIndex, SummaryIndex, KnowledgeGraphIndex, BaseRetriever |
| LangChain | LLM app framework | Document, DocumentLoader, TextSplitter (Recursive, Semantic, Character), VectorStore, Embedding, Retriever |
| Haystack | NLP pipeline | Document, DocumentStore, PreProcessor, Retriever, Reader, PromptNode |
| Chroma | Vector DB | Collection, Document, Embedding, Metadata, Where filters |
| Pinecone | Vector DB | Index, Namespace, Vector, SparseVector, Metadata, ServerlessSpec |
| Weaviate | Vector DB | Collection, Object, Property, VectorIndex (HNSW/flat), BM25, Hybrid search |
| Qdrant | Vector DB | Collection, Point, Vector (dense+sparse), Payload, Filter, Snapshot |
| RAGAS | RAG evaluation | TestsetGenerator, EvalSample, ContextPrecision, ContextRecall, Faithfulness, AnswerRelevancy |
| Unstructured | Doc processing | Element (Title, NarrativeText, Table, Image, ListItem), Partition, ChunkingStrategy |
| ColBERT | Late-interaction retrieval | Passage, Query, Token-level embedding, MaxSim, Plaid indexing |
| Cohere Rerank | Reranking API | Document, RerankResult, RelevanceScore, model selection, top_n |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Document | LlamaIndex, LangChain, Haystack, Chroma, Unstructured, Cohere, Qdrant, Pinecone, Weaviate | Raw source content with metadata before processing | 9 |
| Node/Chunk | LlamaIndex (TextNode), LangChain (TextSplitter output), Haystack (PreProcessor), Unstructured (Element) | Atomic unit after splitting — the retrieval granularity | 4 |
| Collection/Index | Chroma, Pinecone, Weaviate, Qdrant, LlamaIndex (VectorStoreIndex) | Named container of vectors with distance metric and config | 5 |
| Embedding Model Config | LlamaIndex, LangChain, Chroma, Pinecone, Weaviate, Qdrant | Model name + dimensions + distance metric | 6 |
| Chunking Strategy | LlamaIndex (NodeParser), LangChain (TextSplitter), Unstructured (ChunkingStrategy), Haystack (PreProcessor) | Method (recursive/semantic/sentence) + chunk_size + overlap | 4 |
| Retriever Config | LlamaIndex, LangChain, Haystack, Weaviate, Qdrant | top_k, similarity threshold, hybrid alpha, MMR diversity, filters | 5 |
| Reranker Config | Cohere Rerank, ColBERT, LlamaIndex (NodePostprocessor), LangChain (ContextualCompression) | Post-retrieval relevance reordering model + top_n | 4 |
| Metadata Schema | Chroma, Pinecone, Weaviate, Qdrant, LlamaIndex, LangChain, Haystack | Structured metadata fields on documents (filterable) | 7 |
| Sparse Vector | Pinecone (SparseVector), Qdrant (sparse), Weaviate (BM25) | Keyword-based complement to dense vectors for hybrid search | 3 |
| Knowledge Graph Triple | LlamaIndex (KGIndex), Weaviate (cross-references) | Entity-relation-entity for graph-based RAG | 2 |
| Few-shot Demo | RAGAS (TestsetGenerator), LangChain (FewShotPromptTemplate) | Input/output pairs for in-context learning | 2 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| knowledge_card | Node/Chunk (enriched) | 75% | CEX KC adds density scoring + quality gates — richer than industry chunks, but lacks chunk lineage (parent doc ref) |
| rag_source | Document | 65% | Industry Document carries content + loader config; CEX rag_source is pointer-only (URL, freshness). No loader/parser binding. |
| glossary_entry | (niche — implicit in embeddings) | 90% | Well-scoped. No direct industry equivalent; terms usually live inside documents. |
| context_doc | (unique to CEX) | 40% | No industry standard. CEX innovation for prompt hydration. Could be confused with LlamaIndex "context window" stuffing. |
| embedding_config | Embedding Model Config | 60% | Merges model + chunk_size into one kind; industry separates model config from chunking config. Lacks distance metric, index type. |
| few_shot_example | Few-shot Demo | 85% | Well-aligned with RAGAS test cases and LangChain few-shot patterns. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| chunk_strategy | Chunking is universally separate from embedding model. Config: method (recursive/semantic/sentence/markdown), chunk_size, chunk_overlap, separators. Current embedding_config mixes concerns. | LlamaIndex, LangChain, Unstructured, Haystack | high |
| retriever_config | Retrieval strategy (top_k, hybrid ratio, MMR lambda, reranker, filters) is the most critical RAG tuning surface. Currently has no CEX kind. Note: could live in P09 Config, but semantically belongs with knowledge retrieval. | LlamaIndex, LangChain, Haystack, Weaviate, Qdrant | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| context_doc | KEEP (with boundary clarification) | Unique to CEX. No rename needed, but boundary should clarify it is NOT a LlamaIndex "context" or RAG context window. It is domain background injected into prompts. |
| embedding_config | NARROW scope | Remove chunk_size from this kind (move to proposed chunk_strategy). Keep: model_name, dimensions, distance_metric, provider. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| knowledge_card | LlamaIndex TextNode, LangChain Document (post-split), Haystack Document — enriched with quality |
| rag_source | LlamaIndex DocumentLoader output, LangChain DocumentLoader, Haystack DocumentStore |
| glossary_entry | Weaviate schema definitions, general NLP glossaries |
| context_doc | (CEX-unique — validated by prompt hydration pattern) |
| embedding_config | Chroma embedding_function, Pinecone dimension config, Weaviate vectorizer |
| few_shot_example | RAGAS TestsetGenerator, LangChain FewShotPromptTemplate, DSPy demos |

## 7. Summary
Current: 6 kinds → Proposed: 8 kinds (+chunk_strategy, +retriever_config) | Coverage: ~69% → ~88%

Key insight: The industry universally separates **chunking** from **embedding** and treats **retrieval strategy** as a first-class config. CEX's embedding_config currently conflates model + chunking. Splitting these would align CEX with LlamaIndex/LangChain/Haystack patterns and make each kind more focused.
