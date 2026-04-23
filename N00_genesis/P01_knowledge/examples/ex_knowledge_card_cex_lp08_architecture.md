---
id: p01_kc_cex_lp08_architecture
kind: knowledge_card
pillar: P01
title: "CEX LP08 Architecture — Structure and Scale for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp08, architecture, patterns, laws, multi-agent, scaling]
tldr: "P08 define 5 meta-artefatos que governam estrutura: agent_card, pattern, law, diagram, component_map"
when_to_use: "Entender como sistemas LLM escalam via arquitetura formal e meta-artefatos"
keywords: [architecture, agent_group, pattern, law, diagram, component-map]
long_tails:
  - "Como escalar sistema multi-agente LLM com arquitetura"
  - "Qual a diferenca entre pattern e law no CEX"
axioms:
  - "SEMPRE ter component_map antes de adicionar componentes"
  - "NUNCA violar uma law (inviolavel, diferente de instruction)"
linked_artifacts:
  primary: p01_kc_cex_lp07_evals
  related: [p01_kc_cex_lp06_schema]
density_score: 1.0
data_source: "https://arxiv.org/abs/2308.08155"
related:
  - p01_kc_lp08_architecture
  - component-map-builder
  - diagram-builder
  - pattern-builder
  - bld_architecture_component_map
  - bld_architecture_diagram
  - p01_kc_cex_lp11_feedback
  - bld_architecture_pattern
  - p01_kc_cex_lp09_config
  - invariant-builder
---

## Quick Reference

topic: P08 Architecture | scope: system structure | criticality: high
types: 5 | function: BECOME + GOVERN | layer: spec + governance

## Conceitos Chave

- P08 eh sobre ESTRUTURA, nao execucao de tarefas
- Tipos P08 sao meta-artefatos (descrevem artefatos)
- agent_card define departamento completo com MCPs
- pattern eh padrao reutilizavel (ex: continuous batching)
- law eh regra inviolavel do sistema (nao eh instruction)
- diagram visualiza arquitetura (ASCII ou Mermaid)
- component_map mapeia conexoes entre componentes
- Nenhum framework mainstream tem tipos equivalentes
- Sistemas LLM crescem sem planta — P08 eh a planta
- agent_card max 4096 bytes (spec layer, core: true)
- pattern usa llm_function INJECT (informa, nao obriga)
- law usa llm_function CONSTRAIN (obriga, inviolavel)
- P08 constrange todos os LPs: define o que eh possivel
- P08 eh informado por P07: metricas revelam gaps
- P08 evolui com P11: arquitetura adapta ao feedback
- Funcao dominante: BECOME (define) + GOVERN (governa)
- MetaGPT e CrewAI nao tem meta-artefatos formais

## Fases

1. Mapear componentes existentes via component_map
2. Definir laws inviolaveis do sistema (constraints)
3. Documentar patterns reutilizaveis emergentes
4. Especificar agent_cards por dominio funcional
5. Criar diagrams para comunicacao visual do time
6. Revisar arquitetura quando evals P07 revelam gaps

## Regras de Ouro

- SEMPRE documentar WHY de cada law (nao so WHAT)
- NUNCA criar agent_group sem agent_card formal
- SEMPRE atualizar component_map ao adicionar componente
- NUNCA tratar pattern como lei (pattern eh recomendacao)
- SEMPRE separar diagram (visual) de component_map (dados)

## Comparativo

| Tipo | Rigidez | Escopo | Exemplo |
|------|---------|--------|---------|
| law | Inviolavel | Sistema inteiro | "Nunca hardcode brand" |
| pattern | Recomendado | Reutilizavel | Continuous batching |
| agent_card | Obrigatorio | 1 departamento | research_agent research spec |
| diagram | Informativo | Visual | Mermaid do pipeline |
| component_map | Estrutural | Conexoes | Agent-to-agent graph |

## Flow

```
[P08: Architecture Layer]
         |
    +----+----+----+----+
    |    |    |    |    |
  laws  pats  sats diag cmap
    |    |    |    |    |
    v    v    v    v    v
[CONSTRAIN] [INJECT] [BECOME]
    |          |        |
    v          v        v
 governa    informa   define
    |          |        |
    +-----+----+--------+
          |
          v
   [sistema operacional]
          |
          v
   [P07 evals feedback loop]
```

## References

- source: https://arxiv.org/abs/2308.08155
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_lp07_evals
- related: p01_kc_cex_lp06_schema


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp08_architecture]] | sibling | 0.42 |
| [[component-map-builder]] | downstream | 0.35 |
| [[diagram-builder]] | downstream | 0.34 |
| [[pattern-builder]] | downstream | 0.30 |
| [[bld_architecture_component_map]] | downstream | 0.27 |
| [[bld_architecture_diagram]] | downstream | 0.26 |
| [[p01_kc_cex_lp11_feedback]] | sibling | 0.24 |
| [[bld_architecture_pattern]] | downstream | 0.24 |
| [[p01_kc_cex_lp09_config]] | sibling | 0.24 |
| [[invariant-builder]] | downstream | 0.23 |
