---
id: p01_ex_memory_persistence
kind: knowledge_card
pillar: P01
title: "Dual Persistence: SQLite + Chroma for LLM Agent Memory"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [memory, sqlite, chroma, vector-search, persistence, hybrid-search]
tldr: "SQLite (FTS5) + Chroma (vectors) juntos dao hybrid search com 10x economia de tokens via progressive disclosure em 3 camadas"
when_to_use: "Projetar memoria persistente para agentes LLM com busca keyword + semantica local"
keywords: [sqlite, chroma, fts5, vector-embedding, dual-persistence]
long_tails:
  - "Como combinar SQLite e Chroma para memoria de agente LLM"
  - "Qual a diferenca entre contentSessionId e memorySessionId"
axioms:
  - "SEMPRE usar contentSessionId para observations (estavel)"
  - "NUNCA usar memorySessionId para FK — ele comeca NULL"
linked_artifacts:
  primary: p01_kc_memory_session_compression
  related: [p01_kc_memory_worker_service, p01_kc_memory_privacy_controls]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
related:
  - p01_kc_memory_session_compression
  - bld_examples_vector_store
  - p10_ax_session_compression
  - bld_collaboration_search_tool
  - retriever-builder
  - search-tool-builder
  - bld_knowledge_card_knowledge_index
  - bld_knowledge_card_search_tool
  - p01_kc_bm25_search
---

## TL;DR

SQLite armazena dados estruturados (sessions, observations, summaries) com FTS5 para keyword search. Chroma adiciona embeddings vetoriais para busca semantica. Combinados: hybrid search com progressive disclosure em 3 camadas que reduz consumo de tokens em 10x.

## Conceito Central

Memoria de agente LLM exige dois tipos de busca: keyword exato (FTS5/SQLite) e similaridade semantica (Chroma/vetores). Nenhum resolve sozinho. O padrao dual persistence separa storage estruturado (SQLite) de indice semantico (Chroma), conectados por um workflow MCP de 3 camadas: search (IDs, ~50 tokens) → timeline (contexto, ~200 tokens) → get_observations (detalhes, ~1000 tokens).

## Arquitetura

```
SQLite (~/.claude-mem/claude-mem.db)
  sessions | sdk_sessions | observations (FTS5) | summaries
                    |
                    +--- hybrid search ---+
                    |                     |
              keyword match        semantic similarity
              (FTS5/BM25)          (Chroma embeddings)
                    |                     |
                    +--- 3-layer MCP -----+
              search → timeline → get_observations
```

| Tabela | Campos Chave | Funcao |
|--------|-------------|--------|
| sdk_sessions | content_session_id, memory_session_id | Tracking de sessao |
| observations | memory_session_id, tool_name, title | Dados brutos com FTS5 |
| summaries | content_session_id, summary | Narrativa comprimida |

## Patterns

| Trigger | Action |
|---------|--------|
| Busca exata por nome de tool | FTS5 no campo tool_name |
| Busca por conceito similar | Chroma semantic search |
| Context window limitado | Progressive disclosure 3 camadas |
| Nova sessao precisa de historico | Injetar summaries + observations |
| Dois session IDs disponiveis | contentSessionId para FK, memorySessionId para resume |

## Anti-Patterns

- Usar so SQLite sem Chroma (perde busca semantica)
- Usar so Chroma sem SQLite (perde queries estruturadas)
- Carregar todas observations de uma vez (estoura tokens)
- Usar memorySessionId como FK (comeca NULL, instavel)
- Ignorar FTS5 e fazer LIKE queries (10-100x mais lento)

## References

- source: https://github.com/thedotmack/claude-mem
- related: p01_kc_memory_session_compression
- related: p01_kc_memory_worker_service
- related: p01_kc_memory_privacy_controls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_session_compression]] | sibling | 0.25 |
| [[bld_examples_vector_store]] | downstream | 0.20 |
| [[p10_ax_session_compression]] | downstream | 0.20 |
| [[bld_collaboration_search_tool]] | downstream | 0.19 |
| [[retriever-builder]] | downstream | 0.18 |
| [[search-tool-builder]] | downstream | 0.17 |
| [[bld_knowledge_card_knowledge_index]] | sibling | 0.16 |
| [[bld_knowledge_card_search_tool]] | sibling | 0.15 |
| [[p01_kc_bm25_search]] | sibling | 0.15 |
