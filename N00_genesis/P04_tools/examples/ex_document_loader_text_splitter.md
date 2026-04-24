---
id: p04_comp_text_splitter
kind: component
8f: F8_collaborate
pillar: P04
description: "Pipeline component that splits documents into chunks for RAG indexing"
version: 1.0.0
created: 2026-03-25
author: builder_agent
quality: 9.0
tags: [component, pipeline, splitter, RAG, chunking]
updated: "2026-04-07"
domain: "tool integration"
title: "Document Loader Text Splitter"
density_score: 0.92
tldr: "Defines component for document loader text splitter, with validation gates and integration points."
related:
  - tpl_validation_schema
  - skill
  - research_then_build
  - bld_collaboration_skill
  - p08_dir_rag_pipeline
  - p01_rs_brain_faiss_index
  - bld_config_tagline
  - bld_schema_tagline
  - bld_architecture_document_loader
  - bld_schema_landing_page
---

# Component: Text Splitter

## Interface
```yaml
input: {document: string, metadata: object}
output: {chunks: [{text: string, metadata: object, index: int}]}
config:
  chunk_size: 512
  overlap: 50
  strategy: sentence  # sentence | token | semantic
```

## Behavior
Splits input document into overlapping chunks. Preserves sentence boundaries when possible. Attaches source metadata + chunk index to each output.

## Composition
```
[Document Loader] → [Text Splitter] → [Embedder] → [Vector Store]
```

## Why component, not skill
A **skill** (P04) is a high-level capability with multiple phases and triggers.
A **component** is a single-function building block. It does ONE thing:
receive input, transform, produce output. No phases, no triggers, no side effects.
Composable into pipelines. The atom of data processing.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `component` |
| Pillar | P04 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_validation_schema]] | downstream | 0.35 |
| [[skill]] | downstream | 0.34 |
| [[research_then_build]] | downstream | 0.31 |
| [[bld_collaboration_skill]] | downstream | 0.28 |
| [[p08_dir_rag_pipeline]] | downstream | 0.25 |
| [[p01_rs_brain_faiss_index]] | related | 0.24 |
| [[bld_config_tagline]] | downstream | 0.24 |
| [[bld_schema_tagline]] | downstream | 0.24 |
| [[bld_architecture_document_loader]] | related | 0.23 |
| [[bld_schema_landing_page]] | downstream | 0.23 |
