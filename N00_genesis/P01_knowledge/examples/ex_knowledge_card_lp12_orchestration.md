---
id: p01_kc_lp12_orchestration
kind: knowledge_card
pillar: P01
title: "P12 Orchestration: Como Coordena"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [orchestration, workflow, DAG, spawn, signal, handoff]
tldr: "P12 define 6 tipos de orquestracao (workflow, dag, spawn_config, signal, handoff, dispatch_rule) que coordenam execucao multi-agente — 3 modos: solo, grid static, grid continuous"
when_to_use: "Quando precisar definir workflows, spawn configs, signals ou handoffs no CEX"
keywords: [workflow, dag, spawn_config, signal, handoff, dispatch_rule]
long_tails:
  - "como funciona o spawn grid continuous no CEX"
  - "qual a diferenca entre workflow e DAG em P12"
axioms:
  - "Todo handoff deve ter commit instruction — trabalho sem commit eh trabalho perdido"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.88
---

# P12 Orchestration: Como Coordena

## Executive Summary
P12 governa coordenacao multi-agente no CEX com 6 tipos de artefato. Workflows definem steps sequenciais/paralelos, DAGs modelam dependencias, spawn configs parametrizam lancamento de agent_groups (solo/grid/continuous), signals comunicam estado entre agentes, handoffs transferem contexto, e dispatch rules roteiam tasks por keyword.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 6 | workflow, dag, spawn_config, signal, handoff, dispatch_rule |
| workflow max_bytes | 3072 | Steps sequenciais/paralelos |
| signal format | JSON | complete, error, progress |
| handoff max_bytes | 4096 | Task + context + commit |
| spawn modes | 3 | solo, grid static, grid continuous |
| dispatch_rule format | YAML | keyword > agent_group routing |

## Patterns
1. Workflow com steps tipados: sequential (A>B>C) ou parallel (A+B+C)
2. DAG para dependencias complexas: task C depende de A e B concluirem
3. Spawn config: solo (1 sat), grid static (<=6 tasks), grid continuous (>6 tasks, auto-refill)
4. Signal protocol: {sat}_complete_{ts}.json com score para orchestrator monitorar
5. Handoff com 5 secoes: contexto, seeds, tarefas, scope fence, commit instruction
6. Dispatch rule: keyword match > agent_group routing em YAML

## Anti-Patterns
1. Handoff sem commit instruction: trabalho pode se perder
2. Signal sem timestamp: impossivel ordenar eventos
3. Spawn > 3 agent_groups simultaneos: BSOD risk no Windows
4. DAG com ciclo: deadlock garantido
5. Workflow sem error handling: falha em 1 step mata todo o pipeline

## Application
No organization, P12 manifesta como spawn_solo.ps1/spawn_grid.ps1, signal_writer.py, e .claude/handoffs/. Este proprio handoff (META3_edison.md) eh uma instancia de P12 handoff. Grid continuous testado com 1.6x speedup em 7 batches.

## References
1. P12_orchestration/_schema.yaml (fonte de verdade)
2. records/framework/powershell/spawn_*.ps1 (spawn implementations)
3. records/core/python/signal_writer.py (signal implementation)
4. .claude/handoffs/ (handoff instances)

## Retrieval

```yaml
query: "meta-construction"
kind_filter: knowledge_card
top_k: 5
threshold: 0.7
```

```bash
python _tools/cex_retriever.py "meta-construction" --top 5
```
