---
id: p01_kc_cex_lp11_feedback
kind: knowledge_card
pillar: P01
title: "CEX LP11 Feedback — Continuous Improvement Loop for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp11, feedback, quality-gate, bugloop, guardrail, optimizer]
tldr: "P11 define 5 tipos de melhoria continua: quality_gate, bugloop, lifecycle_rule, guardrail, optimizer"
when_to_use: "Entender como sistemas LLM implementam auto-correcao e melhoria continua"
keywords: [feedback, quality-gate, bugloop, guardrail, optimizer, lifecycle-rule]
long_tails:
  - "Como implementar self-healing em sistemas multi-agente LLM"
  - "Qual a diferenca entre guardrail P11 e permission P09 no CEX"
axioms:
  - "SEMPRE fechar o loop: detectar, corrigir, verificar"
  - "NUNCA confundir guardrail (safety) com permission (acesso)"
linked_artifacts:
  primary: p01_kc_cex_lp10_memory
  related: [p01_kc_cex_lp07_evals]
density_score: 1.0
data_source: "https://arxiv.org/abs/2303.11366"
---

## Quick Reference

topic: P11 Feedback | scope: continuous improvement | criticality: high
types: 5 | function: GOVERN + CONSTRAIN | layer: governance

## Conceitos Chave

- P11 eh a revisao do chefe: detecta, corrige, melhora
- quality_gate eh barreira com score numerico (pass/fail)
- bugloop executa ciclo automatico detect > fix > verify
- lifecycle_rule governa freshness, archive e promote
- guardrail eh boundary de seguranca (safety, nao acesso)
- optimizer mapeia metric > action para melhoria continua
- P11 fecha o loop: GOVERN detecta, P11 corrige
- Reflexion, Self-Refine e DSPy sao expressoes de P11
- SWE-Agent e Voyager demonstram self-healing automatico
- quality_gate NAO eh validator (P06) nem rubric (P07)
- bugloop NAO eh unit_eval (P07, teste manual)
- guardrail NAO eh permission (P09, controle de acesso)
- lifecycle_rule NAO eh hook (P04, codigo executavel)
- optimizer NAO eh benchmark (P07, medicao passiva)
- P11 melhora P03: feedback otimiza prompts iterativamente
- P11 atualiza P01: feedback gera novo conhecimento
- P11 utiliza P07: metricas de avaliacao sao input
- Funcao dominante: GOVERN (melhoria) + CONSTRAIN (safety)

## Fases

1. Definir quality_gates com thresholds por artefato
2. Implementar bugloops para modulos criticos (detect>fix)
3. Criar lifecycle_rules (freshness 30d, archive 90d)
4. Estabelecer guardrails de seguranca (safety boundaries)
5. Configurar optimizers com metricas e acoes automaticas
6. Conectar P07 evals como input para feedback loop

## Regras de Ouro

- SEMPRE ter quality_gate antes de promover ao pool
- NUNCA confundir guardrail com permission (safety vs acesso)
- SEMPRE verificar apos corrigir (bugloop completo)
- NUNCA auto-atribuir quality score (validator externo)
- SEMPRE documentar WHY de cada guardrail (contexto)

## Comparativo

| Tipo | Natureza | Trigger | Exemplo |
|------|----------|---------|---------|
| quality_gate | Barreira | Score < threshold | KC score >= 8.0 para pool |
| bugloop | Ciclo | Erro detectado | detect > fix > verify loop |
| lifecycle_rule | Regra | Tempo/estado | Archive KCs > 90 dias |
| guardrail | Restricao | Acao perigosa | Bloquear delete em producao |
| optimizer | Processo | Metrica baixa | Prompt rewrite se score < 7 |

## Flow

```
[P11: Feedback Layer]
         |
    +----+----+----+----+
    |    |    |    |    |
   qg   bl   lc   gr  opt
    |    |    |    |    |
    v    v    v    v    v
 [GOVERN]  [GOVERN] [CONSTRAIN]
    |         |         |
    v         v         v
 barreira   ciclo    safety
    |         |         |
    +----+----+---------+
         |
         v
  [P07 evals como input]
         |
         v
  [P01 knowledge atualizado]
         |
         v
  [P03 prompts otimizados]
```

## References

- source: https://arxiv.org/abs/2303.11366
- source: https://arxiv.org/abs/2310.11511
- related: p01_kc_cex_lp10_memory
- related: p01_kc_cex_lp07_evals


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
