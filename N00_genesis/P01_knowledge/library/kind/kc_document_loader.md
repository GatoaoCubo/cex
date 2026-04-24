---
id: p01_kc_document_loader
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "Document Loader — Deep Knowledge for document_loader"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: document_loader
quality: 9.1
tags: [document_loader, P04, INJECT, kind-kc]
tldr: "Ingests raw files (PDF, HTML, CSV, DOCX) and converts them into chunked Document objects ready for embedding — the entry gate of any RAG pipeline"
when_to_use: "Building, reviewing, or reasoning about document_loader artifacts"
keywords: [document, loader, pdf, chunking, ingestion]
feeds_kinds: [document_loader]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - document_loader-builder
  - bld_architecture_document_loader
  - p08_dir_rag_pipeline
  - p03_sp_document_loader_builder
  - p01_kc_retriever
  - bld_collaboration_document_loader
  - bld_examples_document_loader
  - bld_architecture_retriever
  - p01_kc_chunk_strategy
  - p04_loader_pdf
---

# Document Loader

## Spec
```yaml
kind: document_loader
pillar: P04
llm_function: INJECT
max_bytes: 2048
naming: p04_loader_{{format}}.md + .yaml
core: true
```

## What It Is
A document_loader transforms raw files (PDF, HTML, CSV, DOCX, Markdown, JSON) into a list of Document objects — structured chunks with text content and metadata. Its boundary ends at producing chunks; it does NOT retrieve over those chunks (that is the retriever's job) and does NOT search external sources (that is search_tool). The loader is the mandatory entry gate to any RAG pipeline before embedding and indexing.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | BaseDocumentLoader, PyPDFLoader, CSVLoader | Returns List[Document]; pairs with TextSplitter |
| LlamaIndex | BaseReader, SimpleDirectoryReader, PDFReader | Returns List[TextNode]; built-in chunking |
| CrewAI | Tool wrapping LangChain loaders | No native kind; delegates to LC/LI |
| DSPy | dspy.Retrieve (text file variant) | Minimal; mostly in-memory string split |
| Haystack | FileConverter, MarkdownConverter | Pipeline component; outputs Document list |
| OpenAI | File upload API (Assistants) | Managed chunking; no user control |
| Anthropic | Manual file-to-string + chunk | No native; user owns parse + chunk logic |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| chunk_size | int | 512 | Larger = context; smaller = precision |
| chunk_overlap | int | 64 | Higher = continuity; lower = storage |
| formats_supported | list[str] | [pdf, md, txt] | More formats = more dependencies |
| extract_tables | bool | false | True = richer data; adds latency |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Format-specific loader | File type known at design time | PyPDFLoader for legal contracts |
| Universal loader | Mixed-format directory | SimpleDirectoryReader over /docs |
| Streaming load | Large files (> 50MB) | yield Document chunks lazily |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Load full file into one Document | Context overflow in embedding call | Apply TextSplitter after load |
| No metadata on chunks | Retriever cannot filter by source | Add source, page, chunk_index metadata |
| Reload on every query | Latency spike; unnecessary cost | Cache loaded chunks in vector store |

## Integration Graph
```
[raw_file / URL] --> [document_loader] --> [List[Document + metadata]]
                           |                        |
                   [chunk_strategy]         [retriever / embedder]
                           |
                   [metadata_extractor]
```

## Decision Tree
- IF source is external web URL THEN use search_tool
- IF need to search already-loaded chunks THEN use retriever
- IF file is structured DB rows THEN use db_connector
- DEFAULT: document_loader for any file-to-chunk ingestion pipeline

## Quality Criteria
- GOOD: format handled, chunks produced, metadata on each chunk
- GREAT: streaming, table extraction, per-chunk page reference, cache layer
- FAIL: single Document for entire file, no metadata, no error on unsupported format

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[document_loader-builder]] | downstream | 0.43 |
| [[bld_architecture_document_loader]] | downstream | 0.42 |
| [[p08_dir_rag_pipeline]] | downstream | 0.40 |
| [[p03_sp_document_loader_builder]] | downstream | 0.37 |
| [[p01_kc_retriever]] | sibling | 0.36 |
| [[bld_collaboration_document_loader]] | downstream | 0.34 |
| [[bld_examples_document_loader]] | downstream | 0.32 |
| [[bld_architecture_retriever]] | downstream | 0.31 |
| [[p01_kc_chunk_strategy]] | sibling | 0.31 |
| [[p04_loader_pdf]] | downstream | 0.31 |
