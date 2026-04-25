---
id: p01_kc_cex_lp01_knowledge
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP01 Knowledge — What the LLM Knows (6 Types of Distilled Memory)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp01, knowledge, inject, knowledge-card, rag, embedding]
tldr: "P01 Knowledge groups 6 types of distilled memory that feed the LLM context via the INJECT function"
when_to_use: "Classify knowledge artifacts or understand the role of P01 in the CEX taxonomy"
keywords: [knowledge-card, rag-source, few-shot, embedding, context-doc, glossary]
long_tails:
  - "What types of knowledge exist in CEX"
  - "Difference between knowledge_card and context_doc in CEX"
axioms:
  - "ALWAYS version knowledge_cards (knowledge changes)"
  - "NEVER inject knowledge without a verifiable source"
linked_artifacts:
  primary: p01_kc_cex_function_inject
  related: [p01_kc_cex_lp03_prompt, p01_kc_cex_lp02_model]
density_score: 1.0
data_source: "https://arxiv.org/abs/2005.11401"
related:
  - p01_kc_cex_function_inject
  - p01_kc_cex_lp04_tools
  - rag-source-builder
  - p06_bp_knowledge_card
  - p01_kc_context_doc
  - p01_kc_cex_lp10_memory
  - embedding-config-builder
  - bld_architecture_embedding_config
  - bld_architecture_rag_source
  - context-doc-builder
---

## Quick Reference

topic: LP01 Knowledge | scope: 6 artifact types | criticality: high
llm_function: INJECT | analogy: long-term memory

## Key Concepts

- P01 answers: "what knowledge is available?"
- knowledge_card is the core type (dense atomic fact)
- Dominant function INJECT: data enters LLM context
- 6 types: kc, rag_source, glossary, context_doc, emb, fse
- Without P01 the LLM improvises; with P01 it operates with assets
- knowledge_card has density gate >= 0.8 and max 5120 bytes
- few_shot_example is an input/output pair for in-context learning
- rag_source is a pointer to an external source (URL + freshness)
- glossary_entry defines a domain term (max 3 lines, 512B)
- context_doc hydrates prompts with broad context (up to 2048B)
- embedding_config specifies the vector model and chunk_size
- KC is a graph: linked_artifacts connect knowledge nodes
- title + tldr are the primary fields for BM25 ranking
- Each ## header defines an embedding chunk in the index
- Valid KC: 13 required fields + body 200-5120 bytes

## Phases

1. Research: collect data from verifiable sources
2. Distillation: condense into atomic format (KC or glossary)
3. Validation: quality gate (density, completeness, accuracy)
4. Indexing: embedding + knowledge_index for retrieval
5. Injection: INJECT into the LLM context via RAG or direct

## Golden Rules

- ALWAYS include data_source in factual KCs
- ALWAYS maintain density >= 0.8 (no filler)
- NEVER duplicate KC and context_doc (KC is dense, ctx is broad)
- NEVER self-assign quality (external validation)
- ALWAYS use tags as a list, never a single string

## Comparison

| Type | Purpose | Size | Core |
|------|---------|------|------|
| knowledge_card | Dense atomic fact | <= 5120B | yes |
| rag_source | Indexable external pointer | <= 1024B | no |
| glossary_entry | Term definition | <= 512B | no |
| context_doc | Domain context | <= 2048B | no |
| embedding_config | Vector model config | <= 512B | no |
| few_shot_example | Input/output pair | <= 1024B | yes |

## Flow

```
[Source] -> [Distillation] -> [KC/Glossary/CtxDoc]
                                    |
                            [Embedding + Index]
                                    |
                            [INJECT into LLM]
                                    |
                            [Informed output]
```

## References

- source: https://arxiv.org/abs/2005.11401
- source: https://arxiv.org/abs/2312.10997
- deepens: p01_kc_cex_function_inject
- related: p01_kc_cex_lp03_prompt


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_inject]] | sibling | 0.34 |
| [[p01_kc_cex_lp04_tools]] | sibling | 0.25 |
| [[rag-source-builder]] | related | 0.25 |
| [[p06_bp_knowledge_card]] | downstream | 0.25 |
| [[p01_kc_context_doc]] | sibling | 0.25 |
| [[p01_kc_cex_lp10_memory]] | sibling | 0.25 |
| [[embedding-config-builder]] | related | 0.25 |
| [[bld_architecture_embedding_config]] | downstream | 0.23 |
| [[bld_architecture_rag_source]] | downstream | 0.23 |
| [[context-doc-builder]] | related | 0.23 |
