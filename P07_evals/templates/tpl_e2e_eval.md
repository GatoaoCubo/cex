---
# TEMPLATE: E2E Eval (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.e2e_eval)
# Max 4096 bytes

id: p07_e2e_[pipeline_slug]
kind: e2e_eval
pillar: P07
title: [e2e_eval_do_pipeline]
version: 1.0.0
created: [yyyy-mm-dd]
updated: [yyyy-mm-dd]
author: [agent_group_name]
quality: [8.0_to_10.0]
tags: [[tag1], [tag2], e2e, eval]
tldr: [o_que_o_pipeline_valida]
---

# E2E Eval: [pipeline_slug]

## Setup
<!-- INSTRUCAO: ambiente, seeds e dependencias externas. -->
- Environment: [local|staging|prod_clone]
- Seed data: [dataset_ou_fixture]
- Dependencies: [mcp|api|db]

## Execute
<!-- INSTRUCAO: passos fim-a-fim com checkpoints. -->
1. [acionar_pipeline]
2. [capturar_saida_intermediaria]
3. [validar_saida_final]

## Assert
<!-- INSTRUCAO: 3-5 asserts observaveis. -->
| # | Assertion | Expected |
|---|-----------|----------|
| 1 | [assert_1] | [resultado_1] |
| 2 | [assert_2] | [resultado_2] |
| 3 | [assert_3] | [resultado_3] |

## Teardown
<!-- INSTRUCAO: limpar estado para rerun seguro. -->
- [cleanup_1]
- [cleanup_2]

## Failure Signals
<!-- INSTRUCAO: erros que bloqueiam vs avisam. -->
- Blocker: [sinal_critico]
- Warning: [sinal_degradado]
