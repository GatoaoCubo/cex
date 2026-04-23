---
id: bld_architecture_document_loader
kind: architecture
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: CONSTRAIN
quality: 9.1
tags: [architecture, document_loader, ingestion, chunking, RAG, P04]
tldr: "Component map, dependency graph, and boundary table for document_loader artifacts."
density_score: 1.0
title: Architecture ISO - document_loader
related:
  - p01_kc_document_loader
  - document_loader-builder
  - p08_dir_rag_pipeline
  - p03_sp_document_loader_builder
  - bld_examples_document_loader
  - bld_architecture_retriever
  - p04_document_loader_NAME
  - bld_collaboration_document_loader
  - bld_knowledge_card_document_loader
  - p04_comp_text_splitter
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
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Search PDF for answer | document_loader | retriever | loader=ingest+chunk; retriever=search over chunks |
| Download file from URL | document_loader | api_client | api_client=API call; loader=parse+chunk file content |
| Extract data from webpage | document_loader | browser_tool | browser_tool=DOM interaction; loader=file parsing |
## Decision Tree
- Ingest file into chunks? → document_loader
- Search existing chunks? → retriever
- Navigate and scrape page? → browser_tool
- Call API endpoint? → api_client
## Neighbor Comparison
| Dimension | document_loader | retriever | Difference |
|---|---|---|---|
| Direction | Write (ingest→store) | Read (store→results) | Loader fills store; retriever queries it |
| Input | Raw files (PDF/HTML) | Query string | Different input types |
| Output | Chunked documents | Ranked results | Loader produces; retriever searches |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_document_loader]] | upstream | 0.46 |
| [[document_loader-builder]] | related | 0.42 |
| [[p08_dir_rag_pipeline]] | downstream | 0.41 |
| [[p03_sp_document_loader_builder]] | related | 0.38 |
| [[bld_examples_document_loader]] | related | 0.34 |
| [[bld_architecture_retriever]] | sibling | 0.33 |
| [[p04_document_loader_NAME]] | related | 0.33 |
| [[bld_collaboration_document_loader]] | related | 0.32 |
| [[bld_knowledge_card_document_loader]] | related | 0.32 |
| [[p04_comp_text_splitter]] | related | 0.31 |
