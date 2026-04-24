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
tldr: "INJECT fornece contexto ao LLM via 16 tipos (21% do CEX) — fator #1 de qualidade de output"
when_to_use: "Entender como contexto e injetado em LLMs e por que INJECT e a maior funcao CEX"
keywords: [inject, context, rag, knowledge-card, few-shot, memory]
long_tails:
  - "Quais sao os 16 tipos de INJECT no CEX taxonomy"
  - "Por que contexto e mais importante que modelo para qualidade LLM"
axioms:
  - "SEMPRE injetar contexto APOS identidade (BECOME) e ANTES de raciocinio (REASON)"
  - "NUNCA confundir contexto efemero (session_state) com persistente (knowledge_card)"
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

INJECT preenche o context window com informacao relevante apos identidade e antes de raciocinio. Com 16 tipos (21% do total CEX), e a maior funcao — refletindo que qualidade de output depende mais de contexto que de capacidade generativa. Unifica conceitos fragmentados entre LangChain (5 tipos INJECT), LlamaIndex (6 tipos) e outros frameworks.

## Spec

| Tipo | LP | Funcao |
|------|-----|--------|
| knowledge_card | P01 | Conhecimento atomico destilado e versionado |
| rag_source | P01 | Ponteiro para base indexada via RAG |
| context_doc | P01 | Documento bruto nao destilado como referencia |
| few_shot_example | P01 | Par input/output demonstrativo |
| knowledge_index | P10 | Indice hibrido BM25 + embeddings |
| embedding_config | P01 | Config do modelo de embeddings |
| session_state | P10 | Historico e variaveis da sessao atual |
| runtime_state | P10 | Estado operacional: env vars, flags, results |
| glossary_entry | P01 | Termo + definicao padronizada |
| lens | P02 | Filtro cognitivo que direciona atencao |
| user_prompt | P03 | Input direto do usuario |
| pattern | P08 | Padrao arquitetural reutilizavel |
| diagram | P08 | Representacao visual de estrutura ou fluxo |
| component_map | P08 | Mapa de componentes e dependencias |
| learning_record | P10 | Registro de aprendizado com score |
| few_shot | P03 | Template com slots para exemplos |

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
| Conhecimento reutilizado entre sessoes | Criar knowledge_card destilada |
| Corpus grande demais para contexto | Configurar rag_source com retrieval |
| Instrucao textual insuficiente | Adicionar few_shot_examples |
| Agente precisa de estado entre turnos | Manter session_state |
| Busca semantica sobre corpus | Configurar knowledge_index hibrido |

## Anti-Patterns

- Dump de dados brutos como KC (destile primeiro)
- RAG sem relevance filter (polui contexto)
- Few-shot com exemplos ruins (ensina errado)
- Confundir session_state com memoria de longo prazo
- Ignorar INJECT e culpar o modelo por output ruim

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
