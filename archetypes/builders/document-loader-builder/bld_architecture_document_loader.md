---
id: bld_architecture_document_loader
kind: architecture
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: EDISON
domain: document_loader
llm_function: INJECT
quality: null
tags: [architecture, document_loader, ingestion, chunking, RAG, P04]
tldr: "Component map, dependency graph, and boundary table for document_loader artifacts."
---

# Architecture: document_loader

## Component Inventory
| Component | Role | Examples |
|---|---|---|
| source_file | Raw input: file path, URL, or byte stream | /data/doc.pdf, s3://bucket/file.html |
| encoding_detector | Detects charset before text extraction | chardet, charset-normalizer |
| parser | Extracts text + structure from raw bytes | pdfplumber, trafilatura, pandas, python-docx |
| chunker | Splits extracted text into overlapping chunks | RecursiveCharacterTextSplitter, SemanticChunker |
| metadata_extractor | Pulls provenance + format-specific fields | PDF dict, HTML meta tags, CSV headers |
| output_formatter | Wraps (text, metadata) into target document schema | LangChain Document, LlamaIndex TextNode |

## Dependency Graph
```
source_file
    |
    v
encoding_detector --> parser
                          |
                          v
                    metadata_extractor
                          |
                          v
                        chunker
                          |
                          v
                   output_formatter
                          |
                          v
              [List[Document | Node | Dict]]
                          |
                    downstream consumer
                 (retriever / vector store)
```

| From | To | Data |
|---|---|---|
| source_file | encoding_detector | raw bytes |
| encoding_detector | parser | charset + raw bytes |
| parser | metadata_extractor | structured text + format metadata |
| parser | chunker | full extracted text |
| metadata_extractor | output_formatter | metadata dict |
| chunker | output_formatter | list of text chunks |
| output_formatter | consumer | List[output_format] |

## Boundary Table
| IS | IS NOT |
|---|---|
| Reads files from disk, URL, or stream | Queries vector stores |
| Extracts text and structure from raw bytes | Performs embedding generation |
| Splits text into overlapping chunks | Searches external APIs or web |
| Preserves source provenance in metadata | Writes to databases |
| Outputs LangChain/LlamaIndex/Haystack docs | Ranks or scores documents |
| Handles encoding detection and fallback | Filters or deduplicates at retrieval time |

## Layer Map
| Layer | Input | Process | Output |
|---|---|---|---|
| Input | file path / URL / bytes | format detection, encoding detection | charset + raw bytes |
| Parsing | raw bytes | format-specific parser | extracted text + structure |
| Chunking | full text | splitter with chunk_size + overlap | text chunk list |
| Metadata | text + structure | field extraction per format | metadata dict per chunk |
| Output | chunks + metadata | schema wrapping | List[Document/Node/Dict] |
