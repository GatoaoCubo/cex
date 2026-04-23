---
id: bld_collaboration_document_loader
kind: collaboration
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: COLLABORATE
quality: 9.1
tags: [collaboration, document_loader, ingestion, RAG, crew, P04]
tldr: "Crew compositions, handoff protocol, and dependency map for document_loader-builder in multi-builder pipelines."
density_score: 1.0
title: Collaboration ISO - document_loader
related:
  - bld_collaboration_retriever_config
  - bld_collaboration_retriever
  - p03_sp_document_loader_builder
  - bld_collaboration_chunk_strategy
  - bld_collaboration_builder
  - bld_collaboration_response_format
  - document_loader-builder
  - bld_architecture_kind
  - bld_collaboration_vector_store
  - kind-builder
---
# Collaboration: document_loader-builder

## My Role in Crews
**SPECIALIST — I handle FILE INGESTION AND CHUNKING**
I am always stage 1. I produce the chunk stream that every downstream RAG component depends on.
My output quality sets the ceiling for retrieval precision — no retriever can recover from
bad chunking or missing metadata.

## Crew Compositions

### RAG Pipeline Crew (most common)
| Position | Builder | Artifact | Handoff |
|---|---|---|---|
| 1 | document_loader-builder | p04_loader_{format}.md | List[Document] spec |
| 2 | retriever-builder | p04_retriever_{name}.md | Retrieval interface spec |
| 3 | search-tool-builder | p04_search_{name}.md | Tool wrapping retriever |

**Flow**: document_loader ingests -> retriever indexes and searches -> search_tool exposes to agent

### Data Ingestion Crew
| Position | Builder | Artifact | Handoff |
|---|---|---|---|
| 1 | document_loader-builder | p04_loader_{format}.md | List[Document] spec |
| 2 | db-connector-builder | p04_db_{name}.md | Storage interface |

**Flow**: document_loader parses + chunks -> db_connector stores chunks with embeddings

### Multi-Format Ingestion Crew
| Position | Builder | Artifact | Notes |
|---|---|---|---|
| 1a | document_loader-builder | p04_loader_pdf.md | PDF branch |
| 1b | document_loader-builder | p04_loader_html.md | HTML branch |
| 1c | document_loader-builder | p04_loader_csv.md | CSV branch |
| 2 | retriever-builder | p04_retriever_unified.md | Unified index over all formats |

## Handoff Protocol

### I Receive
| Input | Source | Format |
|---|---|---|
| Target file formats | Crew orchestrator | MIME types or format names |
| Chunk requirements | Downstream retriever spec | chunk_size, overlap, strategy |
| Metadata requirements | Downstream agent spec | List of required metadata keys |
| Output format | Downstream consumer | langchain_doc / llamaindex_node / etc. |

### I Produce
| Output | Format | Goes To |
|---|---|---|
| document_loader artifact | p04_loader_{slug}.md | Pool + retriever-builder |
| Chunk schema | metadata_fields list in frontmatter | retriever-builder for index mapping |
| Format limitations | ## Formats table | Orchestrator for pre-processing planning |

### I Signal
```
complete with quality score >= 7.0
artifact path: records/pool/p04_loaders/{id}.md
metadata_fields: [source, page, ...]  # for retriever-builder handoff
output_format: langchain_doc           # for downstream wiring
```

## Builders I Depend On
None — document_loader-builder is layer 0. No other builder must complete before I start.

## Builders That Depend On Me
| Builder | Why They Need Me | What They Use |
|---|---|---|
| retriever-builder | Needs chunk schema to build index mapping | metadata_fields, output_format, chunk_size |
| search-tool-builder | Needs retriever which needs my chunks | Indirect dependency via retriever |
| db-connector-builder | Stores my output chunks with embeddings | output_format schema |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_retriever_config]] | sibling | 0.46 |
| [[bld_collaboration_retriever]] | sibling | 0.45 |
| [[p03_sp_document_loader_builder]] | related | 0.40 |
| [[bld_collaboration_chunk_strategy]] | sibling | 0.37 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[bld_collaboration_response_format]] | sibling | 0.35 |
| [[document_loader-builder]] | related | 0.34 |
| [[bld_architecture_kind]] | downstream | 0.33 |
| [[bld_collaboration_vector_store]] | sibling | 0.31 |
| [[kind-builder]] | downstream | 0.31 |
