---
id: bld_knowledge_card_document_loader
kind: knowledge_card
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: INJECT
quality: 9.1
tags: [knowledge_card, document_loader, ingestion, chunking, RAG, P04]
tldr: "Domain knowledge for document_loader: parsers, chunk strategies, metadata patterns, anti-patterns, and RAG pipeline position."
density_score: 1.0
when_to_use: "Apply when domain knowledge for document_loader: parsers, chunk strategies, metadata patterns, anti-patterns..."
keywords: [knowledge-card, spec, summary, domain, document_loader]
linked_artifacts:
  primary: null
  related: []
title: Knowledge Card ISO - document_loader
---
# Domain Knowledge: document_loader

## Executive Summary
Document loaders transform raw files into chunked, metadata-rich documents for downstream RAG.
They are stage 1 of any ingestion pipeline: raw file -> parsed text -> chunked Documents ->
embeddings -> vector store. A loader that loses source metadata or chunks poorly degrades
retrieval quality for every query downstream.

## Spec Table
| Property | Value |
|---|---|
| Pillar | P04 |
| llm_function | INJECT |
| Formats | PDF, HTML, CSV, DOCX, JSON, TXT, MD, PPTX, XLSX |
| Chunk strategies | fixed, recursive, semantic, sentence, paragraph |
| Output formats | langchain_doc, llamaindex_node, haystack_doc, raw_dict |
| Max body | 2048 bytes |
| ID pattern | p04_loader_{format_slug} |

## Patterns
| Pattern | When to Use | Library |
|---|---|---|
| Recursive chunking | Structured docs with headers (MD, HTML, DOCX) | LangChain RecursiveCharacterTextSplitter |
| Sentence splitting | Narrative text (TXT, news, books) | NLTK sent_tokenize, spaCy |
| Semantic chunking | Topic-aware splits for better retrieval recall | LangChain SemanticChunker (OpenAI embeds) |
| Fixed-size | Uniform processing, token-budget strict | LangChain CharacterTextSplitter |
| Paragraph | Legal/academic docs with logical paragraph units | Unstructured.io partition |

**Overlap rule**: always set overlap >= 10% of chunk_size. 512-token chunks -> 64-token overlap.
**Parser selection**: prefer Unstructured.io for mixed formats (auto-detects type). For
pure PDF: pdfplumber > PyPDF2 (better table/layout handling). For HTML: trafilatura > BeautifulSoup
(strips boilerplate). For DOCX: python-docx (preserves headings). For CSV: pandas (type inference).

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|---|---|---|
| Chunking without overlap | Context lost at boundaries; retrieval misses answers that span chunks | Set overlap >= 10% of chunk_size |
| Losing source metadata | Chunks untraceable to origin; citation impossible | Always include source, page, section in metadata |
| Ignoring encoding | UnicodeDecodeError on Latin-1 / UTF-16 files | Use chardet or charset-normalizer for detection |
| Treating all formats identically | PDF tables mangled as text; HTML full of nav boilerplate | Per-format parser + post-processing |
| Chunks too large | Exceeds LLM context window; dilutes retrieval score | chunk_size <= 512 tokens for most LLMs |
| No error handling for corrupt files | Silent data loss; missing documents in index | Log parse errors, emit partial doc with error metadata |

## Application
1. Identify formats -> select parsers -> confirm MIME types
2. Choose chunk_strategy based on content structure
3. Set chunk_size from target LLM context window (512 default, 256 for 4K window)
4. Set overlap = chunk_size * 0.125 minimum
5. Define metadata_fields: source always; add page/section/author per format
6. Declare output_format matching downstream consumer

## References
- LangChain document loaders: https://python.langchain.com/docs/integrations/document_loaders/
- LlamaIndex readers: https://docs.llamaindex.ai/en/stable/module_guides/loading/
- Haystack converters: https://docs.haystack.deepset.ai/docs/file-converters
- Unstructured.io: https://unstructured-io.github.io/unstructured/
- Apache Tika: https://tika.apache.org/ (JVM-based, 1000+ formats)
