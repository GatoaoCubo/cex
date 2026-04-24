---
id: p01_kc_cex_lp10_memory
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP10 Memory — Working Memory and State for LLM Agents"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp10, memory, runtime-state, knowledge-index, learning-record, session]
tldr: "P10 define 4 tipos de memoria operacional: runtime_state, knowledge_index, learning_record, session_state"
when_to_use: "Entender como agentes LLM gerenciam estado e memoria entre sessoes"
keywords: [memory, runtime-state, knowledge-index, learning-record, session-state]
long_tails:
  - "Como gerenciar memoria de trabalho em agentes LLM"
  - "Qual a diferenca entre knowledge P01 e memory P10 no CEX"
axioms:
  - "SEMPRE distinguir P01 (o que SABE) de P10 (o que LEMBRA)"
  - "NUNCA persistir session_state alem da sessao"
linked_artifacts:
  primary: p01_kc_cex_lp09_config
  related: [p01_kc_cex_lp01_knowledge]
density_score: 1.0
data_source: "https://arxiv.org/abs/2304.03442"
related:
  - p01_kc_cex_function_inject
  - p01_kc_lp10_memory
  - bld_architecture_session_state
  - bld_architecture_runtime_state
  - p01_kc_cex_lp01_knowledge
  - bld_architecture_memory_scope
  - p03_sp_memory_scope_builder
  - memory-scope-builder
  - runtime-state-builder
  - bld_architecture_learning_record
---

## Quick Reference

topic: P10 Memory | scope: agent state management | criticality: high
types: 4 | function: INJECT | layer: runtime + content

## Conceitos Chave

- P10 eh o caderno de anotacoes do agente (memoria operacional)
- P01 = o que ESTUDEI (externo, validado, persistente)
- P10 = o que VIVI (interno, acumulado, sessional)
- runtime_state guarda decisoes e routing entre sessoes
- knowledge_index configura busca semantica (BM25 + FAISS)
- learning_record registra o que funcionou e o que falhou
- session_state eh snapshot efemero (morre com a sessao)
- LangChain separa Memory (P10) de Document (P01)
- LlamaIndex separa StorageContext (P10) de Node (P01)
- MemGPT demonstra gerenciamento autonomo de memoria
- P10 consome P01: memoria referencia conhecimento
- P10 alimenta P03: contexto de sessao informa prompt
- P10 eh governado por P09: regras de retencao e limpeza
- Funcao dominante: INJECT (memoria injetada como contexto)
- runtime_state max 3072 bytes (persistente entre sessoes)
- session_state NAO eh core (efemero, descartavel)
- knowledge_index NAO eh embedding_config (P01) nem rag_source

## Fases

1. Definir quais estados persistem entre sessoes (runtime)
2. Configurar knowledge_index com BM25 + FAISS para busca
3. Iniciar learning_record para capturar padroes
4. Criar session_state para snapshot da sessao ativa
5. Implementar regras de retencao via P09 (decay, archive)
6. Alimentar P03 com contexto de sessao relevante

## Regras de Ouro

- SEMPRE separar P01 (conhecimento) de P10 (memoria)
- NUNCA tratar session_state como persistente (efemero)
- SEMPRE registrar learning_record apos execucao critica
- NUNCA duplicar knowledge (P01) como runtime_state (P10)
- SEMPRE comprimir memoria antes de overflow de contexto

## Comparativo

| Tipo | Persistencia | Layer | Exemplo |
|------|-------------|-------|---------|
| runtime_state | Entre sessoes | runtime | Routing decisions, counters |
| knowledge_index | Permanente | runtime | BM25 config, FAISS params |
| learning_record | Permanente | content | Success/failure patterns |
| session_state | Efemero | runtime | Current task snapshot |

## Flow

```
[P10: Memory Layer]
         |
    +----+----+----+
    |    |    |    |
   rs   bi   lr   ss
    |    |    |    |
    v    v    v    v
 [INJECT into context]
    |         |
    v         v
 persiste   efemero
    |         |
    +----+----+
         |
         v
  [P03 prompt enriched]
         |
         v
  [P01 knowledge referenced]
```

## References

- source: https://arxiv.org/abs/2304.03442
- source: https://arxiv.org/abs/2310.08560
- related: p01_kc_cex_lp09_config
- related: p01_kc_cex_lp01_knowledge


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_inject]] | sibling | 0.38 |
| [[p01_kc_lp10_memory]] | sibling | 0.33 |
| [[bld_architecture_session_state]] | downstream | 0.28 |
| [[bld_architecture_runtime_state]] | downstream | 0.27 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.27 |
| [[bld_architecture_memory_scope]] | downstream | 0.26 |
| [[p03_sp_memory_scope_builder]] | downstream | 0.25 |
| [[memory-scope-builder]] | downstream | 0.24 |
| [[runtime-state-builder]] | downstream | 0.23 |
| [[bld_architecture_learning_record]] | downstream | 0.23 |
