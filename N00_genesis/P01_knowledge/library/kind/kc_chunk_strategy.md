---
id: p01_kc_chunk_strategy
kind: knowledge_card
type: kind
pillar: P01
title: "Chunk Strategy — Deep Knowledge for chunk_strategy"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: chunk_strategy
quality: 9.1
tags: [chunk_strategy, p01, CONSTRAIN, kind-kc]
tldr: "Defines how raw text is split into retrieval-sized segments — the single highest-leverage knob in any RAG pipeline"
when_to_use: "Building, reviewing, or reasoning about chunk_strategy artifacts"
keywords: [chunking, text-splitting, overlap, semantic-split]
feeds_kinds: [chunk_strategy]
density_score: null
---

# Chunk Strategy

## Spec
```yaml
kind: chunk_strategy
pillar: P01
llm_function: CONSTRAIN
max_bytes: 2048
naming: p01_chunk.md
core: true
```

## What It Is
A chunk_strategy defines the method, size, and overlap used to split source documents into retrieval units. It is the primary constraint governing how knowledge enters the vector store. It is NOT an embedding_config (which defines the model that encodes chunks) nor a retriever_config (which governs search-time parameters).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `TextSplitter` (Recursive, Token, Semantic) | Most variants; `RecursiveCharacterTextSplitter` is default |
| LlamaIndex | `NodeParser` / `SentenceSplitter` | Nodes are chunks; metadata propagated automatically |
| CrewAI | Delegated to LangChain splitters | No native chunking; wraps LC |
| DSPy | Not built-in | Expects pre-chunked passages as input |
| Haystack | `DocumentSplitter` | split_by: word/sentence/passage/page |
| OpenAI | Assistants file_search auto-chunks | 800-token chunks, 400-token overlap (hardcoded) |
| Anthropic | No native chunking | Context window approach; chunking handled externally |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| chunk_size | int | 512 tokens | Larger = more context per hit but lower precision |
| chunk_overlap | int | 64 tokens | More overlap = fewer boundary losses but higher storage |
| method | enum | recursive | Semantic = better boundaries but slower indexing |
| separators | list | ["\n\n","\n"," "] | Domain-specific separators improve coherence |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Recursive character | General-purpose, markdown docs | 512 chars, 64 overlap, split on headers then paragraphs |
| Semantic splitting | Technical docs with mixed topics | Embed each sentence, split where cosine distance > threshold |
| Parent-child | Need both precision and context | Small chunks for retrieval, return parent chunk for generation |
| Fixed token | Billing-sensitive pipelines | Exact 256-token chunks for predictable API costs |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Zero overlap | Sentences split mid-thought at boundaries | Use >= 10% overlap |
| Chunk size > context window / 4 | Single chunk dominates generation | Keep chunks < 25% of model context |
| Ignoring document structure | Headers split from content, tables broken | Use structure-aware separators |

## Integration Graph
```
[embedding_config] --> [chunk_strategy] --> [retriever_config]
                            |
                     [knowledge_card, context_doc, rag_source]
```

## Decision Tree
- IF structured markdown with clear headers THEN recursive with header separators
- IF mixed-topic technical prose THEN semantic splitting
- IF Q&A or FAQ format THEN split per question-answer pair
- IF need both precision and context THEN parent-child chunking
- DEFAULT: recursive character, 512 tokens, 64 overlap

## Quality Criteria
- GOOD: Specifies method, size, overlap; tested on representative sample
- GREAT: Benchmarked chunk sizes against retrieval recall; separator hierarchy matches doc structure; overlap tuned to sentence boundaries
- FAIL: No overlap specified; chunk_size chosen arbitrarily; method mismatches document type
