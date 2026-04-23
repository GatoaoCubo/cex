---
id: bld_config_document_loader
kind: config
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: CONSTRAIN
quality: 9.0
tags: [config, document_loader, ingestion, P04]
tldr: "Production rules for document_loader: naming, paths, size limits, and enum definitions."
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
density_score: 1.0
title: Config ISO - document_loader
related:
  - bld_collaboration_document_loader
  - bld_output_template_document_loader
  - bld_instruction_document_loader
  - p03_sp_document_loader_builder
  - p11_qg_document_loader
  - bld_knowledge_card_document_loader
  - bld_config_kind
  - bld_schema_document_loader
  - bld_examples_document_loader
  - bld_tools_document_loader
---
# Config: document_loader Production Rules

## Naming Convention
| Item | Pattern | Example |
|---|---|---|
| Artifact file | p04_loader_{format_slug}.md | p04_loader_pdf.md |
| format_slug | lowercase, underscores, no hyphens | csv_tabular, html_news, pdf_legal |
| Builder dir | archetypes/builders/document_loader-builder/ | — |
| id field | must equal filename stem | id: p04_loader_pdf == p04_loader_pdf.md |
| Frontmatter key order | id, kind, pillar, version, created, updated, author, name | consistent across all artifacts |

## File Paths
| Purpose | Path |
|---|---|
| Artifact output | records/pool/p04_loaders/{id}.md |
| Compiled YAML | records/pool/p04_loaders/compiled/{id}.yaml |
| Builder builder specs | archetypes/builders/document_loader-builder/bld_*.md |
| Schema reference | archetypes/builders/document_loader-builder/bld_schema_document_loader.md |

## Size Limits
| Item | Limit | Action on Exceed |
|---|---|---|
| Body bytes | 2048 max | Trim descriptions; never remove required fields |
| tldr chars | 160 max | Truncate at word boundary |
| description chars | 200 max | Truncate at word boundary |
| formats_supported | no max, >= 1 | — |
| metadata_fields | no max | List all relevant; omit obvious duplicates |
| density | >= 0.80 | Remove filler prose; use tables over paragraphs |

## Chunk Strategy Enum
| Value | When to Use | Splitter Class |
|---|---|---|
| fixed | Uniform token batches; strict budget control | CharacterTextSplitter |
| recursive | Structured docs with headers and sections | RecursiveCharacterTextSplitter |
| semantic | Topic-aware splits; best retrieval recall | SemanticChunker (requires embeddings) |
| sentence | Narrative text; preserves sentence integrity | SentenceTransformersTokenTextSplitter |
| paragraph | Legal/academic; logical paragraph units | Unstructured partition + paragraph grouping |

## Output Format Enum
| Value | Consumer | Document Class |
|---|---|---|
| langchain_doc | LangChain retriever, vectorstore | langchain_core.documents.Document |
| llamaindex_node | LlamaIndex index, query engine | llama_index.core.schema.TextNode |
| haystack_doc | Haystack pipeline, DocumentStore | haystack.dataclasses.Document |
| raw_dict | Custom pipelines, direct serialization | dict with keys: text, metadata |

## Overlap Defaults
| Chunk Size | Recommended Overlap | Ratio |
|---|---|---|
| 256 tokens | 32 tokens | 12.5% |
| 512 tokens | 64 tokens | 12.5% |
| 1024 tokens | 128 tokens | 12.5% |
| 2048 tokens | 256 tokens | 12.5% |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_document_loader]] | related | 0.33 |
| [[bld_output_template_document_loader]] | related | 0.32 |
| [[bld_instruction_document_loader]] | related | 0.29 |
| [[p03_sp_document_loader_builder]] | related | 0.28 |
| [[p11_qg_document_loader]] | downstream | 0.27 |
| [[bld_knowledge_card_document_loader]] | related | 0.26 |
| [[bld_config_kind]] | sibling | 0.25 |
| [[bld_schema_document_loader]] | downstream | 0.25 |
| [[bld_examples_document_loader]] | related | 0.24 |
| [[bld_tools_document_loader]] | related | 0.24 |
