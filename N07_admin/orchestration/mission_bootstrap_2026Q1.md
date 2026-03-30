---
id: p12_mission_bootstrap_2026q1
kind: dag
pillar: P12
title: "Mission: CEX Self-Bootstrap — Q1 2026"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: n07_orchestrator
pipeline: bootstrap_full
domain: orchestration
quality: 9.0
tags: [mission, bootstrap, dag, orchestration, N07, critical]
tldr: "Plano de 3 fases para o CEX se auto-construir: N03 reconstroi N07, depois grid reconstroi N01-N06."
node_count: 12
edge_count: 11
estimated_duration: "4-6h total"
density_score: 0.95
---

# Mission: CEX Self-Bootstrap

## Situação

O CEX repo é um sistema tipado de conhecimento para agentes LLM.
Contém 99 kinds, 99 builders, 12 pillars, 7 nuclei, 8F pipeline.

**Primeiro boot fora do codexa-core.** O repo agora roda em pi + opus (xhigh thinking)
com inteligência suficiente para se auto-construir — SE seguir os docs como arquiteturado.

### Origem

O conhecimento destilado em `codexa-core` (C:\Users\PC\Documents\GitHub\codexa-core)
foi a oficina que produziu a arquitetura CEX. Agora o CEX é autônomo.

---

## Diagnóstico (2026-03-30 15:26 GMT-3)

### Estado por Nucleus

| Nucleus | Role | Artefatos | quality >= 9.0 | quality: null | Status |
|---------|------|-----------|---------------|--------------|--------|
| **N03** | Builder (Edison) | 33 | **33/33** | 0 | ✅ GOLDEN |
| **N07** | Orchestrator | 13 | 2 | **9** | 🔴 CRÍTICO |
| N01 | Intelligence | 12 | 0 | **11** | 🔴 REBUILD |
| N02 | Marketing | 11 | 0 | **10** | 🔴 REBUILD |
| N04 | Knowledge | 13 | 0 | **12** | 🔴 REBUILD |
| N05 | Operations | 10 | 0 | **9** | 🔴 REBUILD |
| N06 | Commercial | 10 | 0 | **9** | 🔴 REBUILD |

**Total: 60 artefatos para rebuild. N03 é o único nucleus operacional.**

### Builder Archetypes

| Métrica | Valor |
|---------|-------|
| Builders | 98/99 (+ _builder-builder meta) |
| 13 ISOs por builder | ✅ 100% completo (1274 files) |
| Doctor result | 86 PASS, 12 WARN (size 1-74B over 4096B), 0 FAIL |
| KC Library | 98/98 kinds cobertos |

### Tools

| Tool | Status | Verificado |
|------|--------|-----------|
| cex_8f_motor.py | ✅ Resolve intent → kind | Sim |
| cex_8f_runner.py | ✅ Lista 99 kinds | Sim |
| cex_doctor.py | ✅ Diagnostica 98 builders | Sim |
| cex_compile.py | ⬜ Não testado neste boot | — |
| cex_index.py | ⬜ Não testado neste boot | — |
| spawn_solo.ps1 | ✅ Multi-CLI dispatch | Sim (lido) |
| spawn_grid.ps1 | ⬜ Não testado neste boot | — |

---

## Plano de Execução

### Fase 0: Validar Ferramentas (10 min)

**Objetivo**: Confirmar que o 8F pipeline roda end-to-end antes de escalar.

```
nodes:
  - id: f0_test_runner
    label: "Testar cex_8f_runner.py --kind knowledge_card --dry-run"
  - id: f0_test_compile
    label: "Testar cex_compile.py em artefato existente"
  - id: f0_test_index
    label: "Testar cex_index.py rebuild"
```

**Dispatch**: spawn_solo N03, tarefa: "Rodar dry-run do runner, testar compile e index. Reportar via signal."

---

### Fase 1: Reconstruir N07 — O Orquestrador (1-2h)

**Objetivo**: N03 reconstrói os 9 artefatos quality:null de N07 com identidade REAL de orquestrador.

**Por que primeiro**: Sem N07 funcional, não há orchestração confiável para a Fase 3.

```
nodes:
  - id: f1_agent
    label: "Rebuild agent_admin.md — identidade de orquestrador multi-CLI"
    priority: 1
    
  - id: f1_system_prompt
    label: "Rebuild system_prompt_admin.md — regras de dispatch, nunca construir"
    priority: 2
    depends_on: [f1_agent]
    
  - id: f1_knowledge_card
    label: "Rebuild knowledge_card_admin.md — KC do domínio orchestration"
    priority: 3
    
  - id: f1_dispatch_rule
    label: "Rebuild dispatch_rule_admin.md — routing table N01-N06"
    priority: 4
    depends_on: [f1_agent]
    
  - id: f1_dag
    label: "Rebuild dag_admin.md — substituir placeholder genérico"
    priority: 5
    
  - id: f1_workflow
    label: "Rebuild workflow_admin.md — solo/grid/monitor workflow"
    priority: 6
    depends_on: [f1_dispatch_rule]
    
  - id: f1_handoff
    label: "Rebuild handoff_admin.md — template de handoff real"
    priority: 7
    
  - id: f1_quality_gate
    label: "Rebuild quality_gate_admin.md — gates para orchestration"
    priority: 8
    
  - id: f1_agent_card
    label: "Rebuild agent_card_admin.md — deployment spec N07"
    priority: 9
    depends_on: [f1_agent, f1_system_prompt]
```

**Dispatch**: spawn_solo N03, handoff com lista dos 9 artefatos.

**Regras para N03**:
- Ler os artefatos EXISTENTES de N03_engineering/ como referência de qualidade 9.0
- Ler spawn_config_admin.md (quality 9.0) como exemplo do estilo correto para N07
- Identidade N07 = orquestrador multi-CLI, dispatch via spawn, nunca constrói
- Cada artefato deve seguir 8F pipeline completo com builder ISOs

**Critério de Aceite**: Todos 9 artefatos quality >= 9.0. Doctor PASS.

---

### Fase 2: Corrigir 12 WARNs dos Builders (30 min)

**Objetivo**: Comprimir 12 ISOs que excedem 4096B por 1-74 bytes.

```
builders_warn:
  - action-prompt-builder    (examples: 4102B, memory: 4104B)
  - agent-package-builder    (system_prompt: 4101B)
  - benchmark-builder        (memory: 4099B)
  - brain-index-builder      (examples: 4098B)
  - dag-builder              (memory: 4104B)
  - diagram-builder          (examples: 4108B)
  - fallback-chain-builder   (memory: 4097B)
  - feature-flag-builder     (memory: 4100B)
  - hook-builder             (quality_gate: 4101B)
  - mental-model-builder     (examples: 4098B)
  - pattern-builder          (examples: 4100B)
  - router-builder           (examples: 4170B)
```

**Dispatch**: spawn_solo N03, tarefa cirúrgica: "Comprimir 13 arquivos para <= 4096B sem perder informação."

**Critério de Aceite**: Doctor 98 PASS, 0 WARN, 0 FAIL.

---

### Fase 3: Grid Rebuild — N01-N06 em Paralelo (2-3h)

**Objetivo**: N03 reconstrói todos os artefatos quality:null dos 5 nuclei restantes.

**Pré-requisito**: Fase 1 completa (N07 funcional para supervisionar).

```
grid_slots:
  - slot_1: N01 Intelligence  (11 artefatos, CLI: gemini → rebuild via N03/claude)
  - slot_2: N02 Marketing     (10 artefatos, CLI: claude sonnet → rebuild via N03/claude)
  - slot_3: N04 Knowledge     (12 artefatos, CLI: gemini → rebuild via N03/claude)
  - slot_4: N05 Operations    (9 artefatos, CLI: codex → rebuild via N03/claude)
  - slot_5: N06 Commercial    (9 artefatos, CLI: claude sonnet → rebuild via N03/claude)
  - slot_6: (reserva — retry de falhas ou N07 hardening)
```

**Dispatch**: spawn_grid com mission file. Cada slot recebe handoff com lista de artefatos.

**Critério de Aceite**: Todos 51 artefatos quality >= 8.0. Preferência >= 9.0.

---

## Dependências

```
Fase 0 ──→ Fase 1 ──→ Fase 2 (paralela com Fase 3)
                  └──→ Fase 3 (depende de Fase 1)
```

## Riscos

| Risco | Mitigação |
|-------|-----------|
| N03 builder falha no 8F runner | Fase 0 valida antes de escalar |
| Artefatos N07 ficam genéricos | Handoff detalhado com exemplos de N03 como referência |
| Grid sobrecarrega | spawn_monitor.ps1 + mode continuous |
| Quality < 8.0 em batch | Fase backup com spawn_solo para retry individual |

## Métricas de Sucesso

| Métrica | Antes | Depois |
|---------|-------|--------|
| Artefatos quality >= 8.0 | 35/95 | 95/95 |
| Artefatos quality: null | 60 | 0 |
| Doctor PASS | 86/98 | 98/98 |
| N07 identidade real | ❌ | ✅ |
| Auto-bootstrap funcional | ❌ | ✅ |
