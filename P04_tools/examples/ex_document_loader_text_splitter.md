---
id: p04_comp_text_splitter
kind: component
pillar: P04
description: "Pipeline component that splits documents into chunks for RAG indexing"
version: 1.0.0
created: 2026-03-25
author: builder_agent
quality: 9.0
tags: [component, pipeline, splitter, RAG, chunking]
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
