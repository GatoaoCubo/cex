---
id: p01_kc_rag_chunking_strategies
kind: knowledge_card
pillar: P01
title: "RAG Chunking Strategies Comparison and Selection Guide"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: rag_engineering
quality: 8.0
tags: [rag, chunking, embedding, retrieval, semantic-search, document-processing, knowledge]
tldr: "RAG chunking strategies balance context preservation vs retrieval precision: fixed-size (256-512 tokens) for speed, semantic for coherence, sliding window for overlap, document-aware for structure"
when_to_use: "When designing RAG pipeline document preprocessing or optimizing retrieval quality vs performance trade-offs"
keywords: [chunking, rag, semantic-chunking, fixed-size, sliding-window, overlap]
long_tails:
  - How to choose optimal chunk size for RAG embedding retrieval
  - Semantic chunking vs fixed size chunking performance comparison
  - Document structure aware chunking for technical documentation
axioms:
  - ALWAYS test chunk strategy against your specific document type and query patterns
  - NEVER use fixed 1024+ token chunks without measuring retrieval degradation
  - IF documents have clear structure THEN use document-aware chunking over fixed-size
linked_artifacts:
  primary: null
  related: [p01_kc_embedding_strategies, p01_kc_vector_search_optimization]
density_score: 0.92
data_source: "https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/"

# RAG Chunking Strategies Comparison and Selection Guide

## Quick Reference
| Your Situation | Choose Strategy | Token Size | Overlap | Why |
|-----------------|----------------|------------|---------|-----|
| Speed critical, simple queries | Fixed-Size | 256-512 | 10% | Fast processing, adequate precision |
| Complex Q&A, need coherence | Semantic | Variable | 0% | Preserves topic boundaries |
| Dense content, multi-topic docs | Sliding Window | 512 | 20% | Captures cross-boundary concepts |
| Structured docs (code, manuals) | Document-Aware | Variable | 0% | Respects natural boundaries |
| Production system, high quality | Hybrid | 256-512 | 15% | Balances all factors |

## Key Concepts
| Strategy | How It Works | Boundary Logic | Context Preservation | Use Case |
|----------|--------------|----------------|---------------------|----------|
| Fixed-Size | Split every N tokens/chars | Ignores semantic meaning | Poor | Simple docs, speed critical |
| Semantic | Embed sentences, split on similarity drops | Topic shift detection | Excellent | Q&A, coherent content |
| Sliding Window | Overlapping chunks with stride | Fixed + overlap buffer | Good | Dense multi-topic docs |
| Document-Aware | Respect headers/paragraphs/code | Natural structure | Excellent | Structured content |
| Hybrid | Combine strategies with limits | Multiple rules | Balanced | Production systems |

## Strategy Implementation Phases
| Phase | Action | Key Metrics | Sample Size |
|-------|--------|-------------|-------------|
| Profile | Measure doc types, avg length, query patterns | Doc length distribution, query types | 50+ docs |
| Baseline | Start fixed 256-512 tokens | Retrieval@k, answer quality | 100+ queries |
| Optimize | Test semantic/document-aware strategies | Context coherence, precision@5 | 100+ docs |
| Tune | Adjust size, overlap, similarity thresholds | Processing speed, cost per doc | Production load |
| Monitor | Track precision, coherence, throughput | Retrieval drift, user satisfaction | Ongoing |

## Golden Rules
- CHUNK SIZE: 256-512 tokens optimal for most embedding models (1024+ degrades precision)
- OVERLAP: 10-20% for fixed-size, 0% for semantic (natural boundaries)
- CONTEXT: Preserve 2-3 sentences around chunk boundaries for coherence
- METADATA: Include source doc, section, chunk_id for result attribution

## Anti-Patterns
| What NOT To Do | Why It Fails | Instead Do |
|----------------|--------------|------------|
| Single sentence chunks | Loses context, poor retrieval | Min 2-3 sentences per chunk |
| 1024+ token chunks | Embedding model degrades | 256-512 tokens max |
| No overlap on dense content | Miss cross-boundary concepts | 10-20% sliding window |
| Ignore document structure | Break code/tables mid-block | Use document-aware parsing |
| One-size-fits-all strategy | Different docs need different chunking | Profile docs, choose strategy per type |

## Flow
```text
[Document] -> [Structure Analysis] -> [Strategy Selection]
                                            |
                            Fixed: [N tokens] -> [Chunks]
                            Semantic: [Embed] -> [Similarity] -> [Split]
                            Sliding: [N tokens + overlap] -> [Chunks]
                            Document: [Headers/Paragraphs] -> [Chunks]
                                            |
                                     [Add Metadata] -> [Vector DB]
```

## Comparison Strategy Matrix
| Strategy | Processing Speed | Context Preservation | Retrieval Precision | Best For |
|----------|-----------------|---------------------|-------------------|----------|
| Fixed-Size | Fastest (1000+ docs/sec) | Poor | Medium | Large corpus, speed critical |
| Semantic | Slow (50-100 docs/sec) | Excellent | High | Q&A, technical docs |
| Sliding Window | Medium (200+ docs/sec) | Good | High | Dense content, multi-topic docs |
| Document-Aware | Fast (500+ docs/sec) | Excellent | High | Structured docs, code repos |
| Hybrid | Medium (100+ docs/sec) | Good | Highest | Production systems |

## Performance Metrics
| Chunk Size | Embedding Dim | Retrieval@5 | Context Coherence | Processing Cost |
|------------|--------------|-------------|-------------------|-----------------|
| 128 tokens | 1536 | 0.72 | Low | $0.001/doc |
| 256 tokens | 1536 | 0.85 | Good | $0.002/doc |
| 512 tokens | 1536 | 0.89 | Excellent | $0.004/doc |
| 1024 tokens | 1536 | 0.81 | Excellent | $0.008/doc |

## Implementation Patterns
```python
# Fixed-size with metadata
def fixed_chunk(text, size=512, overlap=50):
    chunks = []
    for i in range(0, len(text), size - overlap):
        chunk = text[i:i + size]
        chunks.append({
            'content': chunk,
            'start_idx': i,
            'chunk_id': len(chunks)
        })
    return chunks

# Semantic threshold-based
def semantic_chunk(text, embed_model, threshold=0.8):
    sentences = split_sentences(text)
    embeddings = embed_model.encode(sentences)
    splits = find_similarity_drops(embeddings, threshold)
    return create_chunks_from_splits(sentences, splits)

# Sliding window with stride
def sliding_window_chunk(text, size=512, overlap=100):
    chunks = []
    stride = size - overlap
    for i in range(0, len(text), stride):
        chunk = text[i:i + size]
        if len(chunk) > overlap:  # Skip tiny chunks
            chunks.append({
                'content': chunk,
                'start_idx': i,
                'end_idx': i + len(chunk),
                'chunk_id': len(chunks)
            })
    return chunks

# Document-aware structure parsing
def document_aware_chunk(text, doc_type='markdown'):
    if doc_type == 'markdown':
        sections = split_on_headers(text)
    elif doc_type == 'code':
        sections = split_on_functions(text)
    else:
        sections = split_on_paragraphs(text)
    
    chunks = []
    for section in sections:
        if len(section) > 2048:  # Split large sections
            sub_chunks = fixed_chunk(section, size=512)
            chunks.extend(sub_chunks)
        else:
            chunks.append({'content': section})
    return chunks
```

## References
- LlamaIndex Node Parsers: https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/
- Related: p01_kc_embedding_strategies (model selection for chunking)
- Related: p01_kc_vector_search_optimization (retrieval tuning)