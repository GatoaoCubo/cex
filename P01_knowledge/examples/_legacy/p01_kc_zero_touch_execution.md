---
id: p01_kc_zero_touch_execution
kind: knowledge_card
pillar: P01
title: Zero-Touch Execution - Patterns para Pipelines Autonomos
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: PYTHA
domain: execution
quality: 9.0
tags: [execution, automation, pipeline, autonomy, satellite]
tldr: Patterns ZTE para pipelines CODEXA sem intervencao humana - TAC-8 lifecycle, retry exponencial, fallback chains por satellite
when_to_use: Quando projetando ou debugando pipelines autonomos de satellite dispatch
keywords: [zero-touch-execution, autonomous-pipeline, TAC-8, retry-strategy, fallback-chain]
long_tails:
  - como executar pipeline autonomo sem intervencao humana no CODEXA
  - qual o ciclo de vida de execucao de um satellite dispatch
axioms:
  - Toda step deve ser idempotente (re-executavel sem efeito colateral)
  - Falha sem log = bug silencioso (pior que crash)
linked_artifacts:
  agent: p02_agent_atlas
  skill: p04_skill_spawn_solo
density_score: 0.89
---

# Zero-Touch Execution - Patterns para Pipelines Autonomos

## Executive Summary

Zero-Touch Execution (ZTE) define como pipelines CODEXA rodam do dispatch ate completion sem intervencao humana. O TAC-8 (Total Autonomous Control, 8 stages) e o modelo padrao: cada stage tem checkpoint de estado, fallback chain definido e retry com backoff exponencial antes de escalar para humano.

## Spec Table

| Campo | Valor | Nota |
|-------|-------|------|
| Modelo | TAC-8 | 8 stages: Dispatch → Cleanup |
| Max retries | 3 tentativas | Backoff exponencial |
| Base delay | 1000ms | Dobra a cada retry |
| Max delay | 30000ms | Cap para nao bloquear pipeline |
| Dispatch | `unified_task_orchestrator.py dispatch` | Entry point padrao |
| Monitoring | `stella_auto_orchestrator.py status` | Polling de sinais |
| Signals dir | `.claude/signals/` | JSON por satellite |
| Logs dir | `.claude/symbiosis/logs/` | Audit trail completo |

## TAC-8 Lifecycle

| Stage | Nome | Descricao |
|-------|------|-----------|
| T1 | Dispatch | Task roteada ao satellite correto |
| T2 | Context | Satellite carrega contexto do pool |
| T3 | Plan | Decompoe task em steps executaveis |
| T4 | Execute | Roda steps com progress tracking |
| T5 | Validate | Verifica outputs contra quality gates |
| T6 | Persist | Escreve artifacts no pool/knowledge |
| T7 | Signal | Notifica orchestrator de completion |
| T8 | Cleanup | Libera recursos, arquiva logs |

## Patterns

- **Idempotencia**: cada step re-executavel sem side effects — permite retry seguro em qualquer ponto
- **Fallback por satellite**: SHAKA (web→cache→manual) | LILY (template→simples→draft) | EDISON (full→incremental→scaffold) | ATLAS (full tests→smoke→lint)
- **Checkpoint de estado**: estado persistido em cada stage boundary — recovery sem re-executar stages anteriores
- **Retry config YAML**:
  ```yaml
  max_attempts: 3
  backoff: exponential
  base_delay_ms: 1000
  max_delay_ms: 30000
  retryable: [timeout, rate_limit, transient_network]
  non_retryable: [auth_failure, invalid_input, permission_denied]
  ```

## Anti-Patterns

- **Infinite retry sem backoff**: loop infinito trava o pipeline inteiro — sempre use max_attempts + backoff
- **Silent failure**: swallow de erro sem log = bug indetectavel em producao — sempre logue com contexto
- **Skip de validation**: pular T5 para ganhar tempo gera garbage no pool — quality gates sao obrigatorios
- **Timeout hardcoded**: `sleep(30)` quebradicino — use configurable values com env vars

## Application

ZTE e o padrao de execucao de todos os satellites CODEXA (SHAKA, LILY, EDISON, PYTHA, ATLAS, YORK). Ao debugar pipeline travado, verificar em ordem: (1) signal file existe? (2) log de erro no symbiosis/logs? (3) qual stage do TAC-8 falhou?

## References

- `records/pool/knowledge/KC_ATLAS_005_ZERO_TOUCH_EXECUTION_PATTERNS.md` (fonte original)
- `records/framework/docs/SPAWN_PLAYBOOK.md` (dispatch protocol)
- `.claude/signals/` (signal format spec)
