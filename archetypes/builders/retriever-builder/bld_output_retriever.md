---
kind: output_template
id: bld_output_template_retriever
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a retriever artifact
pattern: every field here exists in bld_schema_retriever.md
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [output_template, retriever, P05, vector-search, RAG]
density_score: 1.0
domain: "output_template artifact construction"
title: "Output Template Retriever"
related:
  - bld_instruction_retriever
  - bld_schema_retriever
  - retriever-builder
  - bld_examples_retriever
  - p03_sp_retriever_builder
  - p04_retr_pinecone
  - bld_collaboration_retriever
  - p01_kc_retriever
  - bld_examples_retriever_config
  - bld_architecture_retriever
---
# Output Template: retriever

Fill every `{{var}}` using schema constraints. Remove this header block before delivering.

```markdown
---
id: p04_retr_{{store_slug}}
kind: retriever
pillar: P04
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author}}
name: "{{Human-readable retriever name}}"
store_type: {{chroma|pinecone|faiss|qdrant|weaviate|milvus|elasticsearch|costm}}
embedding_model: {{model_name, e.g. text-embedding-3-small}}
similarity_metric: {{cosine|dot_product|euclidean|manhattan}}
top_k: {{integer >= 1, default 10}}
search_type: {{vector|keyword|hybrid}}
reranker: {{model_name or null}}
metadata_filters: [{{field1}}, {{field2}}]
namespace: {{collection_or_namespace_name, default "default"}}
quality: null
tags: [retriever, {{store_slug}}, {{search_type}}, {{additional_tag}}]
tldr: "{{One sentence <= 160 chars: what store, model, strategy, use case}}"
description: "{{Optional <= 200 chars: what documents this retriever searches}}"
---

## Overview
{{2-4 sentences: which vector store backend, which embedding model and its dimension,
primary use case, what document collection is searched.}}

## Search Strategy
{{Describe search_type (vector/keyword/hybrid) and why it was chosen for this use case.
If hybrid: specify fusion method (RRF k=60 or weighted alpha=X).
Specify similarity_metric and why it matches the embedding model.
If reranker: name the model, when it fires (after first-pass top_k), what it optimizes.}}

## Configuration
- top_k: {{value}} {{if reranking: note first-pass k vs final k}}
- metadata_filters: {{list fields and their types/values}}
- namespace: {{collection name or multi-tenant pattern}}
- score_threshold: {{minimum similarity score if applicable, else "none"}}
- chunk_size_assumption: {{expected chunk size from document_loader, e.g. 512 tokens}}

## Integration
- SDK/library: {{e.g. langchain ChromaRetriever, llama_index VectorStoreIndex, qdrant-client}}
- auth: {{API key env var name, or "none" for local}}
- connection: {{pattern without secrets, e.g. "host=localhost port=6333" or "PINECONE_INDEX_NAME env var"}}
- embedding_call: {{how query is encoded before search, e.g. OpenAIEmbeddings(model=...) }}
```

## Fill Rules
- id must equal filename stem exactly
- store_slug: snake_case, lowercase, no hyphens (chroma, pinecone_hybrid, faiss_local)
- tldr <= 160 characters — count before submitting
- body (all 4 sections) must total <= 2048 bytes
- quality: null — never fill with a number
- tags list must include "retriever" as first tag
- reranker: null if not used (do not omit the field)
- metadata_filters: empty list [] if none (do not omit the field)

## Cross-References

- **Pillar**: P05 (Output)
- **Kind**: `output template`
- **Artifact ID**: `bld_output_template_retriever`
- **Tags**: [output_template, retriever, P05, vector-search, RAG]

## Output Pipeline

| Aspect | Detail |
|--------|--------|
| Template | Defines structure for output template outputs |
| Validation | Checked against `validation_schema` |
| Post-hook | Scored by `cex_score.py` after creation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_retriever]] | upstream | 0.43 |
| [[bld_schema_retriever]] | downstream | 0.41 |
| [[retriever-builder]] | upstream | 0.40 |
| [[bld_examples_retriever]] | downstream | 0.39 |
| [[p03_sp_retriever_builder]] | upstream | 0.39 |
| [[p04_retr_pinecone]] | upstream | 0.35 |
| [[bld_collaboration_retriever]] | downstream | 0.34 |
| [[p01_kc_retriever]] | upstream | 0.34 |
| [[bld_examples_retriever_config]] | downstream | 0.33 |
| [[bld_architecture_retriever]] | downstream | 0.32 |
