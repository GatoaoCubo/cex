---
id: p01_kc_lp08_architecture
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "P08 Architecture: Como Escala"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [architecture, agent_group, pattern, law, diagram]
tldr: "P08 define 5 tipos de arquitetura (agent_card, pattern, law, diagram, component_map) que governam como o sistema escala — leis sao inviolaveis, patterns sao reutilizaveis"
when_to_use: "Quando precisar definir arquitetura, leis operacionais ou patterns de escala no CEX"
keywords: [agent_card, pattern, law, diagram, component_map]
long_tails:
  - "como definir uma lei operacional no CEX"
  - "qual a diferenca entre pattern e law em P08"
axioms:
  - "Laws sao inviolaveis — patterns sao recomendacoes, laws sao obrigacoes"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.87
related:
  - p01_kc_cex_lp08_architecture
  - diagram-builder
  - component-map-builder
  - bld_architecture_diagram
  - p01_kc_diagram
  - agent-card-builder
  - pattern-builder
  - bld_collaboration_agent_card
  - p08_diag_{{SCOPE_SLUG}}
  - bld_architecture_agent_card
---

# P08 Architecture: Como Escala

## Executive Summary
P08 governa a arquitetura do CEX com 5 tipos de artefato que definem desde agent_groups (7 no organization) ate leis operacionais inviolaveis (11 ativas). Patterns documentam solucoes reutilizaveis (continuous batching, spawn grid), laws definem restricoes absolutas, e diagrams visualizam o sistema em ASCII ou Mermaid.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 5 | agent_card, pattern, law, diagram, component_map |
| agent_card max_bytes | 4096 | Role + model + MCPs |
| pattern max_bytes | 4096 | Ex: continuous batching |
| law max_bytes | 3072 | Inviolavel, operacional |
| diagram formats | 2 | ASCII ou Mermaid |
| component_map format | YAML | What connects to what |

## Patterns
- Agent_group spec: role + model + MCPs + boot sequence em 1 artefato
- Pattern reutilizavel com nome, contexto, solucao, consequencias (GoF-like)
- Law numerada (P08_law_01..N) com enforcement automatico
- Diagram em ASCII para inline, Mermaid para rendering
- Component map em YAML mapeia dependencias entre componentes

## Anti-Patterns
- Law sem enforcement: vira recomendacao ignoravel
- Pattern sem consequencias documentadas: oculta trade-offs
- Agent_group spec sem MCPs: agent_group nasce sem ferramentas
- Diagram desatualizado: pior que nenhum diagrama

## Application
organization tem 7 agent_groups (orchestrator, research_agent, marketing_agent, builder_agent, knowledge_agent, operations_agent, commercial_agent) todos com agent_card em P08. As 11 leis ativas governam operacao autonoma. O agent_package de P02 mapeia architecture.md para P08.

## References
- P08_architecture/_schema.yaml (fonte de verdade)
- records/framework/docs/LAWS_v3_PRACTICAL.md (11 leis ativas)
- P02_model/_schema.yaml (agent_package.lp_mapping: architecture=P08)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp08_architecture]] | sibling | 0.41 |
| [[diagram-builder]] | downstream | 0.36 |
| [[component-map-builder]] | downstream | 0.32 |
| [[bld_architecture_diagram]] | downstream | 0.32 |
| [[p01_kc_diagram]] | sibling | 0.31 |
| [[agent-card-builder]] | downstream | 0.30 |
| [[pattern-builder]] | downstream | 0.29 |
| [[bld_collaboration_agent_card]] | downstream | 0.28 |
| [[p08_diag_{{SCOPE_SLUG}}]] | downstream | 0.28 |
| [[bld_architecture_agent_card]] | downstream | 0.26 |
