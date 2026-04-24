---
id: p01_kc_lp11_feedback
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "P11 Feedback: Como Melhora"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [feedback, quality_gate, bugloop, guardrail, optimizer]
tldr: "P11 define 5 tipos de feedback (quality_gate, bugloop, lifecycle_rule, guardrail, optimizer) que governam melhoria continua — bugloop eh o ciclo detect > fix > verify automatico"
when_to_use: "Quando precisar criar quality gates, ciclos de correcao ou guardrails de seguranca no CEX"
keywords: [quality_gate, bugloop, lifecycle_rule, guardrail, optimizer]
long_tails:
  - "como funciona o bugloop automatico no CEX"
  - "qual a diferenca entre quality_gate e guardrail em P11"
axioms:
  - "Quality gate eh pass/fail com score — sem zona cinza, sem 'quase passou'"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.87
related:
  - p01_kc_cex_lp11_feedback
  - bugloop-builder
  - p01_kc_feedback_loops
  - bld_architecture_bugloop
  - bld_manifest_lifecycle_rule
  - bld_collaboration_bugloop
  - p03_sp_bugloop_builder
  - bld_architecture_guardrail
  - bld_collaboration_lifecycle_rule
  - p01_kc_bugloop
---

# P11 Feedback: Como Melhora

## Executive Summary
P11 governa melhoria continua no CEX com 5 tipos de artefato. Quality gates definem barreiras pass/fail com score, bugloops automatizam detect > fix > verify, lifecycle rules controlam freshness/archive/promote, guardrails impoe limites de seguranca, e optimizers ligam metricas a acoes de melhoria.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 5 | quality_gate, bugloop, lifecycle_rule, guardrail, optimizer |
| Max bytes (todos) | 4096 | Uniforme entre tipos |
| quality_gate output | pass/fail + score | Binario com metrica |
| bugloop ciclo | detect > fix > verify | Automatico, max 3 retries |
| lifecycle states | 3 | fresh > stale > archived |
| guardrail enforcement | hard | Safety boundary inviolavel |

## Patterns
- Quality gate com score threshold: >= 9.5 golden, >= 8.0 pool, >= 7.0 learning, < 7.0 rejected
- Bugloop com max 3 tentativas: fix 1 (normal) > fix 2 (alternativo) > fix 3 (simplificado) > skip
- Lifecycle rule com freshness check: stale apos N dias, auto-archive apos M dias
- Guardrail como hard limit: seguranca, compliance, custo maximo
- Optimizer liga metrica a acao: "se latencia > 2s, reduzir context window"

## Anti-Patterns
- Quality gate sem threshold numerico: julgamento subjetivo
- Bugloop sem limite de retries: loop infinito
- Lifecycle sem freshness check: artefatos stale poluem pool
- Guardrail soft (warning only): nao previne o dano

## Application
No organization, P11 manifesta como Shokunin quality tiers (7.0/8.0/9.5), agent_group-execution retry protocol (3 tentativas), e ISO error_handling.md. O forge valida prompts contra P11 rules antes de output.

## References
- P11_feedback/_schema.yaml (fonte de verdade)
- P07_evals/_schema.yaml (scoring upstream)
- .claude/rules/agent_group-execution.md (retry protocol)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp11_feedback]] | sibling | 0.40 |
| [[bugloop-builder]] | downstream | 0.38 |
| [[p01_kc_feedback_loops]] | sibling | 0.30 |
| [[bld_architecture_bugloop]] | downstream | 0.29 |
| [[bld_manifest_lifecycle_rule]] | related | 0.29 |
| [[bld_collaboration_bugloop]] | downstream | 0.28 |
| [[p03_sp_bugloop_builder]] | downstream | 0.28 |
| [[bld_architecture_guardrail]] | downstream | 0.24 |
| [[bld_collaboration_lifecycle_rule]] | downstream | 0.24 |
| [[p01_kc_bugloop]] | sibling | 0.24 |
