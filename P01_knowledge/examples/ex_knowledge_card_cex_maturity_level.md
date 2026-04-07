---
id: p01_kc_cex_maturity_level
kind: knowledge_card
pillar: P01
title: "CEX Maturity Level — LP Completeness as Capability Diagnostic"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, maturity, capability, diagnostic, lp-completeness]
tldr: "7 niveis (L0-L6) medem maturidade de entidades LLM por completude de LPs — observacao diagnostica, NAO prescricao"
when_to_use: "Diagnosticar por que uma entidade LLM falha ou avaliar sua maturidade atual"
keywords: [maturity-level, capability-maturity, diagnostic, cmm]
long_tails:
  - "Como medir maturidade de um agente LLM usando LPs do CEX"
  - "Qual a diferenca entre L0 e L5 no modelo de maturidade CEX"
axioms:
  - "NUNCA tratar niveis como prescricao (eh observacao empirica)"
  - "SEMPRE usar maturidade como diagnostico, nao como meta"
linked_artifacts:
  primary: p01_kc_cex_fractal_architecture
  related: [p01_kc_cex_boundary_concept]
density_score: null
data_source: null
---

## Summary

Maturity Level mede a completude dos 12 LPs em uma entidade LLM, de L0 (prompt, 1 LP) a L6 (ecossistema auto-evolutivo). Inspirado no CMM mas original na aplicacao a entidades LLM. Eh explicitamente uma OBSERVACAO, nao lei: "entidades mais capazes tendem a preencher mais LPs". A causalidade pode ser inversa — entidades complexas PRECISAM de mais LPs. Utilidade principal: diagnostico de falhas por LPs ausentes.

## Spec

| Nivel | LPs | Capacidade Central | Diagnostico |
|-------|-----|-------------------|-------------|
| L0 Prompt | 1/12 | Gerar texto | Stateless, sem identidade, sem tools |
| L1 Chain | 2/12 | Sequenciar outputs | Composicao basica, sem memoria |
| L2 Agent | 3-4/12 | Identidade + conhecimento | Entidade com papel e dados |
| L3 Runtime | 6/12 | Processo dedicado | Tools, hooks, monitoramento |
| L4 Agent_group | 9/12 | Autonomia departamental | Memoria, evolucao, coordenacao |
| L5 System | 12/12 | Multi-agente coordenado | Todas 8 funcoes ativas |
| L6 Ecosystem | 12/12+ | Auto-evolutivo | Gera novos tipos, LPs, funcoes |

Origem: CMM (Capability Maturity Model) com 5 niveis organizacionais. CEX adapta para 7 niveis de entidades LLM usando completude de LPs como metrica.

Natureza: observacao empirica, NAO prescricao. "Preencher mais LPs" nao causa melhoria. Mas ausencia de LPs frequentemente EXPLICA falhas. Diagnostico > receita.

## Patterns

| Trigger | Action |
|---------|--------|
| Agente falha em tarefa esperada | Verificar quais LPs estao faltando |
| Prompt precisa escalar para agente | Adicionar LPs incrementalmente |
| Avaliar capacidade de entidade | Contar LPs preenchidos vs necessarios |
| Planejar evolucao de sistema | Mapear LPs atuais, priorizar proximos |
| Comparar entidades entre projetos | Usar nivel como metrica comum |

## Anti-Patterns

- Usar niveis como meta ("precisamos ser L5" sem necessidade)
- Preencher LPs vazios com conteudo generico para subir nivel
- Assumir causalidade (mais LPs = melhor automaticamente)
- Ignorar que L0 eh suficiente para tarefas simples
- Comparar niveis entre dominios diferentes sem contexto

## References

- related: p01_kc_cex_fractal_architecture
- related: p01_kc_cex_boundary_concept
