---
id: p01_gl_embedding
kind: glossary_entry
pillar: P01
title: "Embedding"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: 9.2
tags: [glossary, embedding, vector, similarity]
tldr: "A fixed-length float vector representing text semantics, enabling similarity search via cosine distance in vector stores."
density_score: 0.96
updated: "2026-04-13"
---

# Embedding

**Term**: Embedding  
**Abbreviation**: emb  
**Synonyms**: vector representation, text embedding, dense vector  

**Definition**: A fixed-length array of floating-point numbers (typically 384–3072 dimensions) that represents the semantic meaning of a text passage. Produced by embedding models (OpenAI `text-embedding-3-*`, Voyage `voyage-3`, local SBERT). Stored in vector databases (pgvector, FAISS). Retrieved via cosine similarity, dot product, or L2 distance. The numeric substrate of RAG pipelines.  

**See**: `embedding_config`, `embedder_provider`, `vector_store`  

## Boundary

An embedding is a **numeric representation** of text semantics, not a knowledge card (which contains structured metadata) or a context document (which contains full-text content). It is a **component** of RAG pipelines, not a complete system.  

## 8F Pipeline Function

Primary function: **INJECT**  
Embeddings are injected into vector stores during preprocessing, enabling downstream systems to perform similarity search. Key stages:  
1. Text input (e.g., user query, document)  
2. Model inference (e.g., OpenAI, SBERT)  
3. Vector output (e.g., 1536-dimensional float array)  
4. Storage in vector databases (e.g., FAISS, pgvector)  
5. Retrieval via similarity metrics (e.g., cosine similarity)  

**Example Use Case**:  
A customer support chatbot uses embeddings to map user queries to relevant knowledge base documents.  

## Comparison of Embedding Models

| Model Name              | Dimensions | Use Case               | Provider       | Performance Metric (Cosine Similarity) |
|------------------------|------------|------------------------|----------------|----------------------------------------|
| OpenAI `text-embedding-3-large` | 3072       | Semantic search        | OpenAI         | 0.89 (vs. BERT)                      |
| Voyage `voyage-3`       | 1536       | Cross-lingual search   | Voyage AI      | 0.92 (vs. SBERT)                     |
| SBERT (Sentence-BERT)   | 768        | Paraphrase detection   | Hugging Face   | 0.87 (vs. FastText)                  |
| BERT (Base)             | 768        | Token-level analysis   | Google         | 0.78 (vs. RoBERTa)                   |
| Sentence-T5             | 512        | Multilingual tasks     | Google         | 0.85 (vs. mBART)                     |

**Notes**:  
- Higher dimensions capture more nuance but increase storage costs.  
- Cosine similarity ranges from -1 (opposite) to +1 (identical).  

## Related Kinds

- **embedding_config**: Defines parameters (e.g., model version, dimensionality) for embedding generation.  
- **embedder_provider**: Manages access to embedding models (e.g., OpenAI, Hugging Face).  
- **vector_store**: Stores and indexes embeddings for efficient similarity search.  
- **knowledge_card**: Contains structured metadata (e.g., entity relationships), distinct from raw embeddings.  
- **rag_pipeline**: Uses embeddings for retrieval, but includes additional stages (e.g., ranking, summarization).  

## Technical Details

### Dimensionality Tradeoffs

| Dimension Count | Pros                          | Cons                          | Example Use Case               |
|------------------|-------------------------------|-------------------------------|--------------------------------|
| 384              | Low storage, fast inference   | Limited semantic resolution   | Chatbot intent classification  |
| 768              | Balanced performance          | Moderate storage cost         | Document clustering            |
| 1536             | High semantic fidelity        | Higher storage, slower queries | Legal document similarity search |
| 3072             | Maximum resolution            | Expensive, slow               | Academic research indexing     |

### Vector Database Benchmarks

| Database     | Throughput (QPS) | Latency (ms) | Storage Efficiency | Use Case               |
|--------------|------------------|--------------|--------------------|------------------------|
| FAISS        | 100,000          | 2.5          | 95%                | Large-scale search     |
| pgvector     | 50,000           | 4.0          | 85%                | Relational integration |
| Milvus       | 80,000           | 3.2          | 90%                | Hybrid search          |
| Weaviate     | 30,000           | 6.0          | 80%                | Schema-rich queries    |
| Pinecone     | 120,000          | 1.8          | 98%                | Cloud-native pipelines |

### Retrieval Metrics

| Metric         | Formula                          | Use Case                     | Example Value |
|----------------|----------------------------------|------------------------------|---------------|
| Cosine Similarity | (A·B)/(|A||B|)                 | Semantic matching            | 0.92          |
| Dot Product    | A·B                              | High-dimensional spaces      | 1200          |
| L2 Distance    | √Σ(Ai-Bi)²                       | Exact match prioritization   | 0.15          |
| Euclidean Distance | Same as L2 Distance         | Geometric similarity         | 0.22          |
| Hamming Distance | Bitwise comparison (binary)   | Binary embeddings only       | 10            |

## Implementation Considerations

### Model Selection Criteria

| Factor           | OpenAI `text-embedding-3` | SBERT | FastText |
|------------------|---------------------------|-------|----------|
| License          | Commercial                | MIT   | Apache 2 |
| Multilingual     | Yes                       | Yes   | Yes      |
| Fine-tuning      | No                        | Yes   | No       |
| Inference Speed  | Fast                      | Medium| Fast     |
| Cost per 1M tokens | $0.02                   | Free  | Free     |

### Storage Optimization

- **Quantization**: Reduce precision from 32-bit floats to 8-bit integers (e.g., FAISS' IVF-PQ).  
- **Compression**: Use product quantization (PQ) to reduce storage by 75%.  
- **Indexing**: Build hierarchical navigable small-world (HNSW) graphs for fast nearest-neighbor search.  

### Retrieval Best Practices

1. **Normalize Vectors**: Ensure all vectors have unit length to avoid bias from magnitude differences.  
2. **Batch Processing**: Process queries in batches (e.g., 100 vectors at once) to reduce latency.  
3. **Filtering**: Combine similarity scores with metadata filters (e.g., "only return documents from 2023").  
4. **Post-Processing**: Rank top 100 results by cosine similarity, then apply a threshold (e.g., >0.8).  

## Limitations and Alternatives

### Limitations of Embeddings

| Limitation               | Explanation                                  | Mitigation Strategy                  |
|--------------------------|----------------------------------------------|--------------------------------------|
| Semantic Drift           | Model updates may alter vector meanings      | Freeze model version in production   |
| Out-of-Vocabulary Words  | Rare terms may be poorly represented         | Use subword tokenization (e.g., BPE) |
| Context Window Limits    | Long documents may lose coherence            | Split into smaller chunks            |
| Domain Specificity       | General models may underperform on niche data| Fine-tune on domain-specific corpus  |

### Alternative Representations

| Representation Type | Format      | Use Case                     | Example Tool         |
|---------------------|-------------|------------------------------|----------------------|
| TF-IDF              | Sparse vector | Keyword-based search         | Elasticsearch        |
| Bag-of-Words        | Sparse vector | Basic text classification    | Scikit-learn         |
| Topic Models        | Probabilities | Document clustering          | LDA (Gensim)         |
| Knowledge Graphs    | Triplets    | Entity relationship analysis | Neo4j                |
| Image Embeddings    | Float array | Visual similarity search     | CLIP (OpenAI)        |

## Future Trends

### Emerging Technologies

| Technology           | Description                              | Impact on Embeddings               |
|----------------------|------------------------------------------|------------------------------------|
| Multimodal Embeddings | Combine text, image, and audio data      | Enable cross-modal search          |
| Neural Architecture Search | Automate model design for embeddings | Optimize for specific use cases  |
| Quantum Embeddings   | Use quantum computing for vector spaces  | Potential for exponential speedup |
| Self-Supervised Learning | Train on unlabelled data               | Improve generalization without fine-tuning |
| Embedding Compression | Reduce vector size without losing info   | Enable mobile and edge deployment  |

### Industry Adoption

| Sector       | Adoption Rate | Use Case Examples                          |
|--------------|---------------|--------------------------------------------|
| E-commerce   | 90%           | Product search, recommendation systems     |
| Healthcare   | 75%           | Medical record matching, drug discovery    |
| Legal        | 65%           | Document similarity, contract analysis     |
| Finance      | 80%           | Fraud detection, compliance monitoring     |
| Education    | 50%           | Plagiarism detection, content summarization|