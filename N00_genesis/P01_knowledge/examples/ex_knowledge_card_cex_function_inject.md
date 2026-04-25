---
id: p01_kc_cex_function_inject
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function INJECT — Context Injection as Primary Quality Driver"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, inject, context, rag, knowledge-card, few-shot]
tldr: "INJECT provides context to the LLM via 16 types (21% of CEX) — #1 factor for output quality"
when_to_use: "Understand how context is injected into LLMs and why INJECT is the largest CEX function"
keywords: [inject, context, rag, knowledge-card, few-shot, memory]
long_tails:
  - "What are the 16 INJECT types in the CEX taxonomy"
  - "Why context is more important than model for LLM output quality"
axioms:
  - "ALWAYS inject context AFTER identity (BECOME) and BEFORE reasoning (REASON)"
  - "NEVER confuse ephemeral context (session_state) with persistent (knowledge_card)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_function_reason, p01_kc_cex_function_call]
density_score: null
data_source: "https://arxiv.org/abs/2309.07864"
related:
  - p01_kc_cex_lp10_memory
  - p01_kc_cex_lp01_knowledge
  - kc_model_context_protocol
  - context-doc-builder
  - p01_kc_context_doc
  - bld_architecture_session_state
  - p04_ct_cex_forge
  - bld_knowledge_card_context_doc
  - p01_kc_cex_taxonomy
  - p01_kc_cex_lp03_prompt
---

## Summary

INJECT fills the context window with relevant information after identity and before reasoning. With 16 types (21% of total CEX), it is the largest function — reflecting that output quality depends more on context than on generative capability. Unifies fragmented concepts across LangChain (5 INJECT types), LlamaIndex (6 types), and other frameworks.

## Spec

| Type | LP | Function |
|------|-----|----------|
| knowledge_card | P01 | Distilled and versioned atomic knowledge |
| rag_source | P01 | Pointer to indexed base via RAG |
| context_doc | P01 | Raw undistilled document as reference |
| few_shot_example | P01 | Demonstrative input/output pair |
| knowledge_index | P10 | Hybrid BM25 + embeddings index |
| embedding_config | P01 | Embeddings model config |
| session_state | P10 | Current session history and variables |
| runtime_state | P10 | Operational state: env vars, flags, results |
| glossary_entry | P01 | Term + standardized definition |
| lens | P02 | Cognitive filter that directs attention |
| user_prompt | P03 | Direct user input |
| pattern | P08 | Reusable architectural pattern |
| diagram | P08 | Visual representation of structure or flow |
| component_map | P08 | Component and dependency map |
| learning_record | P10 | Learning record with score |
| few_shot | P03 | Template with slots for examples |

## Code

<!-- lang: python | purpose: context injection pipeline -->
```python
context = []
context.append(brain_query("market research fones bluetooth"))
context.append(load_kc("p01_kc_fones_bluetooth_brasil"))
context.append(few_shot_examples("pesquisa_mercado", n=3))
context.append(session_state.get("user_constraints"))
# INJECT: 4 fontes -> context window -> REASON
agent.run(task="Pesquisar mercado", context=context)
```

## Patterns

| Trigger | Action |
|---------|--------|
| Knowledge reused across sessions | Create distilled knowledge_card |
| Corpus too large for context | Configure rag_source with retrieval |
| Textual instruction insufficient | Add few_shot_examples |
| Agent needs state between turns | Maintain session_state |
| Semantic search over corpus | Configure hybrid knowledge_index |

## Anti-Patterns

- Dumping raw data as KC (distill first)
- RAG without relevance filter (pollutes context)
- Few-shot with bad examples (teaches wrong)
- Confusing session_state with long-term memory
- Ignoring INJECT and blaming the model for bad output

## References

- source: https://arxiv.org/abs/2309.07864
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_function_become
- related: p01_kc_cex_function_reason

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp10_memory]] | sibling | 0.36 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.31 |
| [[kc_model_context_protocol]] | sibling | 0.26 |
| [[context-doc-builder]] | related | 0.24 |
| [[p01_kc_context_doc]] | sibling | 0.23 |
| [[bld_architecture_session_state]] | downstream | 0.21 |
| [[p04_ct_cex_forge]] | downstream | 0.20 |
| [[bld_knowledge_card_context_doc]] | sibling | 0.20 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.19 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.19 |
