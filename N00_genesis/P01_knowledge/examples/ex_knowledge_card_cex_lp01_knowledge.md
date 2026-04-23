---
id: p01_kc_cex_lp01_knowledge
kind: knowledge_card
pillar: P01
title: "CEX LP01 Knowledge — O Que a LLM Sabe (6 Tipos de Memoria Destilada)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp01, knowledge, inject, knowledge-card, rag, embedding]
tldr: "P01 Knowledge agrupa 6 tipos de memoria destilada que alimentam o contexto do LLM via funcao INJECT"
when_to_use: "Classificar artefatos de conhecimento ou entender o papel de P01 na taxonomia CEX"
keywords: [knowledge-card, rag-source, few-shot, embedding, context-doc, glossary]
long_tails:
  - "Quais tipos de conhecimento existem no CEX"
  - "Diferenca entre knowledge_card e context_doc no CEX"
axioms:
  - "SEMPRE versionar knowledge_cards (conhecimento muda)"
  - "NUNCA injetar conhecimento sem fonte verificavel"
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

topic: LP01 Knowledge | scope: 6 tipos de artefato | criticality: high
funcao_llm: INJECT | analogia: memoria de longo prazo

## Conceitos Chave

- P01 responde: "que conhecimento esta disponivel?"
- knowledge_card eh o tipo core (fato atomico denso)
- Funcao dominante INJECT: dado entra no contexto LLM
- 6 tipos: kc, rag_source, glossary, context_doc, emb, fse
- Sem P01 o LLM improvisa; com P01 opera com patrimonio
- knowledge_card tem density gate >= 0.8 e max 5120 bytes
- few_shot_example eh par input/output para in-context learning
- rag_source eh ponteiro para fonte externa (URL + freshness)
- glossary_entry define termo do dominio (max 3 linhas, 512B)
- context_doc hidrata prompts com contexto amplo (ate 2048B)
- embedding_config especifica modelo vetorial e chunk_size
- KC eh grafo: linked_artifacts conectam nos de conhecimento
- title + tldr sao campos primarios de BM25 ranking
- Cada ## header define um chunk de embedding no indice
- KC valido: 13 campos required + body 200-5120 bytes

## Fases

1. Pesquisa: coletar dados de fontes verificaveis
2. Destilacao: condensar em formato atomico (KC ou glossary)
3. Validacao: quality gate (density, completeness, accuracy)
4. Indexacao: embedding + knowledge_index para retrieval
5. Injecao: INJECT no contexto do LLM via RAG ou direto

## Regras de Ouro

- SEMPRE incluir data_source em KCs factuais
- SEMPRE manter density >= 0.8 (sem filler)
- NUNCA duplicar KC e context_doc (KC eh denso, ctx eh amplo)
- NUNCA auto-atribuir quality (validacao externa)
- SEMPRE usar tags como lista, nunca string unica

## Comparativo

| Tipo | Proposito | Tamanho | Core |
|------|-----------|---------|------|
| knowledge_card | Fato atomico denso | <= 5120B | sim |
| rag_source | Ponteiro externo indexavel | <= 1024B | nao |
| glossary_entry | Definicao de termo | <= 512B | nao |
| context_doc | Contexto de dominio | <= 2048B | nao |
| embedding_config | Config modelo vetorial | <= 512B | nao |
| few_shot_example | Par input/output | <= 1024B | sim |

## Flow

```
[Fonte] -> [Destilacao] -> [KC/Glossary/CtxDoc]
                                    |
                            [Embedding + Index]
                                    |
                            [INJECT no LLM]
                                    |
                            [Output informado]
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
