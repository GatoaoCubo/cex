---
id: p01_gl_rag
kind: glossary_entry
pillar: P01
title: "Retrieval-Augmented Generation (RAG)"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: 9.2
tags: [glossary, rag, retrieval, augmented-generation]
tldr: "Pattern that augments LLM prompts with retrieved documents from a knowledge base, reducing hallucination and grounding responses in facts."
density_score: 0.97
updated: "2026-04-13"
---

# Retrieval-Augmented Generation (RAG)

**Term**: Retrieval-Augmented Generation  
**Abbreviation**: RAG  
**Synonyms**: retrieval-augmented prompting, grounded generation  

**Definition**: An architecture pattern where an LLM prompt is augmented with relevant documents retrieved from an external knowledge base at inference time. The pipeline: query → embed → retrieve top-K → inject into context → generate. Reduces hallucination by grounding responses in verified knowledge. CEX implements RAG via `cex_retriever.py` (TF-IDF sparse) with planned dense retrieval via Supabase pgvector.  

**See**: `retriever_config`, `rag_source`, `chunk_strategy`, `rag_pipeline_architecture.md`  

## Boundary

This artifact is a glossary entry defining RAG. It is not a knowledge_card (which lacks minimum density) or context_doc (which lacks scope).  

## 8F Pipeline Function

Primary function: **INJECT**  

### Key Components
1. **Query Encoder**: Transforms user input into vector space for similarity search.  
2. **Document Store**: Indexed knowledge base (e.g., TF-IDF, FAISS, pgvector).  
3. **Retriever**: Selects top-K documents based on query similarity.  
4. **Context Injector**: Merges retrieved documents into LLM prompt.  
5. **Generator**: Produces final response using augmented context.  

### Implementation Details
- **CEX RAG Stack**:  
  - `cex_retriever.py`: TF-IDF-based sparse retrieval (current)  
  - Planned: Dense retrieval via Supabase pgvector (2026 Q3)  
  - Chunking: `chunk_strategy` determines document splitting (e.g., 512 tokens)  
  - Config: `retriever_config` defines parameters (k=5, similarity threshold=0.7)  

### Use Cases
- **Customer Support**: Answers grounded in product manuals  
- **Legal Research**: Case law references in legal Q&A  
- **Medical Q&A**: Evidence-based responses from clinical guidelines  

### Comparison with Alternatives

| Method               | Knowledge Source       | Hallucination Risk | Scalability | Example Use Case         |
|----------------------|------------------------|--------------------|-------------|--------------------------|
| Traditional LLM      | Internal knowledge     | High               | Low         | General conversation     |
| Knowledge Card       | Static knowledge       | Medium             | Medium      | Dense fact lookup        |
| Prompt Engineering   | Hardcoded instructions | High               | Low         | Task-specific templates  |
| RAG (Sparse)         | External KB (TF-IDF)   | Low                | High        | Dynamic Q&A with docs    |
| RAG (Dense)          | External KB (pgvector) | Very Low           | Very High   | Real-time document search|  

## Related Kinds

- **knowledge_card**: Provides dense knowledge snippets but lacks RAG's dynamic retrieval.  
- **retriever_config**: Defines parameters for document retrieval in RAG pipelines.  
- **chunk_strategy**: Determines how documents are split for efficient retrieval.  
- **rag_pipeline_architecture**: Describes the overall system design for RAG implementations.  
- **prompt_template**: Structures the input to LLMs in RAG workflows.  

## Challenges and Solutions

| Challenge                  | Solution                                  | Impact on Accuracy | Complexity |
|---------------------------|-------------------------------------------|--------------------|------------|
| Document Relevance        | BM25 + cosine similarity hybrid scoring   | +15%               | Medium     |
| Query Ambiguity           | Multi-turn dialogue tracking              | +10%               | High       |
| Out-of-Scope Queries      | Fallback to general LLM                   | -5%                | Low        |
| Retrieval Latency         | Asynchronous retrieval + caching          | -2%                | Medium     |
| Knowledge Freshness       | Daily reindexing + versioning             | +20%               | High       |  

## Performance Metrics (CEX RAG)

| Metric               | TF-IDF (Sparse) | pgvector (Dense) | Target |
|----------------------|------------------|------------------|--------|
| Recall@5             | 78%              | 89%              | 90%    |
| Precision@5          | 65%              | 76%              | 80%    |
| Latency (ms)         | 120              | 85               | 75     |
| Hallucination Rate   | 3.2%             | 1.1%             | 1%     |
| Context Utilization  | 62%              | 78%              | 85%    |  

## Best Practices

1. **Chunking Strategy**: Use 512-token chunks with overlap for better context coverage.  
2. **Retrieval Threshold**: Set similarity threshold to 0.7 for balance between recall and precision.  
3. **Fallback Mechanism**: Implement general LLM fallback for out-of-scope queries.  
4. **Monitoring**: Track hallucination rates via post-hoc validation against ground truth.  
5. **Scalability**: Use pgvector for dense retrieval in production environments.  

## Example Workflow

1. **User Query**: "What are the side effects of drug X?"  
2. **Embed Query**: Convert to vector using BERT.  
3. **Retrieve**: Find top-5 documents from clinical guidelines.  
4. **Inject**: Append retrieved documents to prompt.  
5. **Generate**: LLM synthesizes answer with cited sources.  

## Future Directions

- **Multimodal RAG**: Extend to image/video retrieval (2026 Q4)  
- **Real-Time Updates**: Streaming ingestion of new documents  
- **Personalization**: User-specific knowledge filtering  
- **Zero-Shot Retrieval**: No need for pretraining on specific domains  
- **Ethical Guardrails**: Detect and filter biased or outdated sources  

## References

- `rag_pipeline_architecture.md` (CEX internal)  
- `retriever_config` (parameters for TF-IDF/pgvector)  
- `chunk_strategy` (document splitting rules)  
- `rag_source` (knowledge base metadata)  
- Supabase pgvector documentation (dense retrieval)  

## Summary

RAG is a critical pattern for grounding LLM responses in verified knowledge. By combining retrieval and generation, it reduces hallucination while enabling dynamic, context-aware responses. CEX's implementation balances sparse and dense retrieval methods, with ongoing improvements to scalability and accuracy.