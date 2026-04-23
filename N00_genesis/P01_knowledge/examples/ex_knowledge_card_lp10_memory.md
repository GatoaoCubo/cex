---
id: p01_kc_lp10_memory
kind: knowledge_card
pillar: P01
title: "P10 Memory: O Que Lembra"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [memory, mental_model, brain, learning, axiom]
tldr: "P10 define 5 tipos de memoria (mental_model, knowledge_index, learning_record, session_state, axiom) que persistem conhecimento entre sessoes — axioms sao imutaveis"
when_to_use: "Quando precisar definir persistencia de conhecimento, learning records ou axiomas no CEX"
keywords: [mental_model, knowledge_index, learning_record, session_state, axiom]
long_tails:
  - "como funciona a memoria persistente no CEX"
  - "qual a diferenca entre learning_record e axiom em P10"
axioms:
  - "Axioms sao imutaveis e nao negociaveis — learning records evoluem, axioms persistem"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.86
related:
  - p10_bi_organization_brain
  - p01_rs_brain_faiss_index
  - learning-record-builder
  - p04_plug_brain_search
  - bld_examples_instruction
  - p01_kc_knowledge_index
  - p01_kc_cex_lp10_memory
  - bld_collaboration_learning_record
  - bld_knowledge_card_knowledge_index
  - knowledge-index-builder
---

# P10 Memory: O Que Lembra

## Executive Summary
P10 governa persistencia de conhecimento no CEX com 5 tipos que cobrem desde estado efemero (session_state) ate regras imutaveis (axiom). Mental models mapeiam routing e decisoes, brain indexes configuram busca (BM25 + FAISS), e learning records capturam o que deu certo/errado para evolucao continua.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 5 | mental_model, knowledge_index, learning_record, session_state, axiom |
| Max bytes (todos) | 3072 | Uniforme entre tipos |
| mental_model format | YAML | routing_rules + decision_tree |
| knowledge_index engines | 2 | BM25 (keyword) + FAISS (semantic) |
| session_state lifecycle | efemero | Snapshot descartavel |
| axiom lifecycle | imutavel | Nunca muda |

## Patterns
- Mental model por agente com routing_rules + decision_tree em YAML
- Brain index combina BM25 (~50% accuracy) + FAISS/Ollama (~88% hybrid)
- Learning record com score: o que deu certo (>= 8.0) e errado (< 7.0)
- Session state como snapshot — usado para handoff entre sessoes
- Axiom como regra fundamental que sobrevive a qualquer refactor

## Anti-Patterns
- Session state tratado como permanente: acumula lixo
- Learning record sem score: impossivel rankear por relevancia
- Brain index sem rebuild: embeddings ficam stale (>24h)
- Axiom mutavel: perde proposito de ser fundamento inviolavel

## Application
No organization, P10 manifesta como mental_model.yaml por agent_group, Brain MCP (BM25+FAISS), learning memory (.claude/rules/organization-learning.md), e MEMORY.md. O CEX formaliza cada tipo com schema validavel.

## References
- P10_memory/_schema.yaml (fonte de verdade)
- records/agent_groups/{sat}/mental_model.yaml (instancias reais)
- records/core/brain/ (Brain MCP implementation)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_bi_organization_brain]] | downstream | 0.38 |
| [[p01_rs_brain_faiss_index]] | related | 0.32 |
| [[learning-record-builder]] | downstream | 0.31 |
| [[p04_plug_brain_search]] | downstream | 0.30 |
| [[bld_examples_instruction]] | downstream | 0.29 |
| [[p01_kc_knowledge_index]] | sibling | 0.28 |
| [[p01_kc_cex_lp10_memory]] | sibling | 0.28 |
| [[bld_collaboration_learning_record]] | downstream | 0.26 |
| [[bld_knowledge_card_knowledge_index]] | sibling | 0.26 |
| [[knowledge-index-builder]] | downstream | 0.25 |
