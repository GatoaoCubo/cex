---
id: p01_kc_haystack_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "Haystack Patterns — Pipeline, Component, DocumentStore, Generators"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: haystack
origin: src_framework_taxonomy
quality: 9.1
tags: [haystack, pipeline, component, document-store, generator, retriever]
tldr: "Haystack v2 builds NLP pipelines as directed multigraphs of typed components — connect, run, serialize, wrap as SuperComponent"
when_to_use: "Building or mapping Haystack v2 constructs to CEX kinds"
keywords: [haystack, pipeline, component, document-store, retriever, generator, embedder]
long_tails:
  - "How does Haystack Pipeline map to CEX workflow and component kinds"
  - "Which Haystack classes map to CEX retriever and knowledge_index kinds"
axioms:
  - "@component decorator + output_types = the universal Haystack building block"
  - "Pipeline is a directed multigraph — components wire via typed input/output sockets"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_taxonomy, p01_kc_langchain_patterns, p01_kc_llamaindex_patterns]
feeds_kinds:
  - workflow         # Pipeline, AsyncPipeline (directed multigraph execution)
  - function_def     # @component decorator (typed component = callable unit)
  - retriever        # Retriever component (document retrieval)
  - knowledge_index      # DocumentStore (abstract storage interface)
  - embedding_config # SentenceTransformersDocumentEmbedder, SentenceTransformersTextEmbedder
  - prompt_template  # PromptBuilder (template -> prompt)
  - knowledge_card   # Document (core data structure)
  - dispatch_rule    # ConditionalRouter (conditional pipeline branching)
  - pattern          # SuperComponent (wraps pipeline as reusable component)
  - document_loader  # DocumentWriter (writes into DocumentStore)
density_score: 0.89
related:
  - atom_10_haystack_vercel
  - bld_collaboration_component_map
  - bld_instruction_component_map
  - component-map-builder
  - p10_lr_component_map_builder
  - p03_sp_component_map_builder
  - bld_config_component_map
  - p11_qg_component_map
  - p04_comp_text_splitter
  - cex_llm_vocabulary_whitepaper
---

# Haystack Patterns

## Quick Reference
```yaml
topic: Haystack v2.x (haystack)
scope: Component-based pipelines, document stores, retrieval, generation
source: docs.haystack.deepset.ai
criticality: high
```

## Key Concepts

| Concept | Module | CEX Kind | Role |
|---------|--------|----------|------|
| `@component` | `haystack` | function_def | Decorator: marks class as pipeline component |
| `@component.output_types` | `haystack` | function_def | Declares component output schema |
| `Pipeline` | `haystack` | workflow | Directed multigraph of typed components |
| `AsyncPipeline` | `haystack` | workflow | Async parallel pipeline execution |
| `SuperComponent` | `haystack` | pattern | Wraps complete pipeline as single component |
| `Document` | `haystack` | knowledge_card | Core document data structure |
| `DocumentStore` | `haystack` | knowledge_index | Abstract document storage interface |
| `DocumentWriter` | `haystack.components.writers` | document_loader | Writes documents into a DocumentStore |
| `SentenceTransformersDocumentEmbedder` | `haystack.components.embedders` | embedding_config | Embeds documents via SentenceTransformers |
| `SentenceTransformersTextEmbedder` | `haystack.components.embedders` | embedding_config | Embeds query strings |
| `TransformerSimilarityRanker` | `haystack.components.rankers` | retriever | Ranks documents by similarity |
| `ConditionalRouter` | `haystack.components.routers` | dispatch_rule | Routes pipeline flow conditionally |
| `Retriever` | `haystack.components.retrievers` | retriever | Retrieves relevant documents |
| `PromptBuilder` | `haystack.components.builders` | prompt_template | Builds prompts from Jinja2 templates |
| `OpenAIGenerator` | `haystack.components.generators` | function_def | LLM generation via OpenAI API |
| `OpenAIChatGenerator` | `haystack.components.generators` | function_def | Chat LLM generation via OpenAI |
| `from_dict` / `to_dict` | (all components) | pattern | Serialize/deserialize any component |

## Patterns

| Trigger | Action |
|---------|--------|
| Define custom component | `@component` class with `run()` method + `@component.output_types(...)` |
| Build pipeline | `Pipeline()` -> `add_component()` -> `connect()` -> `run()` |
| Index documents | `embedder -> writer` pipeline into DocumentStore |
| RAG query | `text_embedder -> retriever -> prompt_builder -> generator` |
| Conditional routing | `ConditionalRouter(routes=[...])` — branch by condition |
| Reusable sub-pipeline | `SuperComponent` wraps pipeline as single component |
| Async execution | `AsyncPipeline` for parallel component execution |
| Serialize pipeline | `pipeline.to_dict()` -> YAML/JSON -> `Pipeline.from_dict()` |

## Anti-Patterns

- Skipping `@component.output_types` — pipeline cannot validate wiring
- Connecting mismatched types between components — runtime error
- Using `DocumentStore` without embedder — no semantic search capability
- Building monolithic components instead of composing small ones
- Ignoring `from_dict`/`to_dict` — losing pipeline reproducibility
- Not using `SuperComponent` for reusable sub-pipelines — duplicated wiring

## CEX Mapping

```text
[knowledge_card (Document)] -> [embedding_config -> knowledge_index (DocumentStore)]
    -> [retriever + dispatch_rule (ConditionalRouter)] -> [prompt_template (PromptBuilder)]
    -> [function_def (Generator)] -> [workflow (Pipeline)] -> [pattern (SuperComponent)]
```

## References

- source: docs.haystack.deepset.ai/docs/intro
- related: p01_kc_cex_taxonomy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_10_haystack_vercel]] | sibling | 0.26 |
| [[bld_collaboration_component_map]] | downstream | 0.26 |
| [[bld_instruction_component_map]] | downstream | 0.24 |
| [[component-map-builder]] | downstream | 0.22 |
| [[p10_lr_component_map_builder]] | downstream | 0.20 |
| [[p03_sp_component_map_builder]] | downstream | 0.19 |
| [[bld_config_component_map]] | related | 0.17 |
| [[p11_qg_component_map]] | downstream | 0.17 |
| [[p04_comp_text_splitter]] | downstream | 0.17 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.17 |
