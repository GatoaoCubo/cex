---
id: p12_mission_bootstrap_2026q1
kind: dag
8f: F8_collaborate
pillar: P12
title: "Mission: CEX Self-Bootstrap — Q1 2026"
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n07_orchestrator
pipeline: bootstrap_full
domain: orchestration
quality: 9.1
tags: [mission, bootstrap, dag, orchestration, N07, critical]
tldr: "4-phase plan for CEX self-bootstrap: validate tools, N03 rebuilds N07, fix WARNs, N03 sequential rebuilds N01-N06."
node_count: 16
edge_count: 15
estimated_duration: "5-7h total"
density_score: 0.96
related:
  - index
  - p10_bi_intelligence_outputs
  - p12_sig_admin_orchestration
  - p08_ac_admin_orchestrator
  - p02_nd_n01.md
  - p12_ho_admin_template
  - n01_selfheal_w2_diagnosis
  - release_check_fixes_20260413
  - p01_kc_orchestration
  - bld_schema_integration_guide
---

# Mission: CEX Self-Bootstrap v2.0

## Situação

O CEX repo é um sistema tipado de conhecimento para agentes LLM.
Contém 300 kinds, 301 builders, 12 pillars, 7 nuclei, 8F pipeline.

**Primeiro boot fora do codexa-core.** O repo agora roda em pi + opus (xhigh thinking)
com inteligência suficiente para se auto-construir — SE seguir os docs como arquiteturado.

### Origem

O conhecimento destilado em `codexa-core` (C:\Users\PC\Documents\GitHub\codexa-core)
foi a oficina que produziu a arquitetura CEX. Agora o CEX é autônomo.

---

## Diagnóstico (2026-03-30 15:46 GMT-3)

### Estado por Nucleus

| Nucleus | Role | Artefatos | quality >= 9.0 | quality: null | sem field | Status |
|---------|------|-----------|----------------|---------------|-----------|--------|
| **N03** | Builder (Edison) | 34 | **33/34** | 0 | 0 | ✅ GOLDEN |
| **N07** | Orchestrator | 14 | 3 | **9** | **1** | 🔴 CRÍTICO |
| N01 | Intelligence | 12 | 0 | **11** | 0 | 🔴 REBUILD |
| N02 | Marketing | 11 | 0 | **10** | 0 | 🔴 REBUILD |
| N04 | Knowledge | 13 | 0 | **12** | 0 | 🔴 REBUILD |
| N05 | Operations | 10 | 0 | **9** | 0 | 🔴 REBUILD |
| N06 | Commercial | 10 | 0 | **9** | 0 | 🔴 REBUILD |

**Total: 61 artefatos para rebuild (9 null + 1 sem field em N07 + 51 null em N01-N06).**

### Manifesto Completo dos Artefatos NULL

#### N07 (10 artefatos — 9 null + 1 sem quality field)

| # | Kind | Path | Bytes | Status |
|---|------|------|-------|--------|
| 1 | agent | N07_admin/P02_model/agent_admin.md | 3338 | null |
| 2 | system_prompt | N07_admin/P03_prompt/system_prompt_admin.md | 2549 | null |
| 3 | knowledge_card | N07_admin/P01_knowledge/knowledge_card_admin.md | 2344 | null |
| 4 | dispatch_rule | N07_admin/P12_orchestration/dispatch_rule_admin.md | 1496 | null |
| 5 | dag | N07_admin/P12_orchestration/dag_admin.md | 1330 | null |
| 6 | workflow | N07_admin/P12_orchestration/workflow_admin.md | 2198 | null |
| 7 | handoff | N07_admin/P12_orchestration/handoff_admin.md | 1930 | null |
| 8 | quality_gate | N07_admin/P11_feedback/quality_gate_admin.md | 2177 | null |
| 9 | agent_card | N07_admin/architecture/agent_card_admin.md | 3270 | null |
| 10 | signal | N07_admin/P12_orchestration/signal_admin.md | 3281 | SEM FIELD |

#### N01 Intelligence (11 artefatos null)

| # | Kind | Path |
|---|------|------|
| 1 | agent | N01_intelligence/P02_model/agent_intelligence.md |
| 2 | agent_card | N01_intelligence/architecture/agent_card_intelligence.md |
| 3 | quality_gate | N01_intelligence/P11_feedback/quality_gate_intelligence.md |
| 4 | embedding_config | N01_intelligence/P01_knowledge/embedding_config_intelligence.md |
| 5 | knowledge_card | N01_intelligence/P01_knowledge/knowledge_card_intelligence.md |
| 6 | rag_source | N01_intelligence/P01_knowledge/rag_source_intelligence.md |
| 7 | dispatch_rule | N01_intelligence/P12_orchestration/dispatch_rule_intelligence.md |
| 8 | workflow | N01_intelligence/P12_orchestration/workflow_intelligence.md |
| 9 | prompt_template | N01_intelligence/P03_prompt/prompt_template_intelligence.md |
| 10 | system_prompt | N01_intelligence/P03_prompt/system_prompt_intelligence.md |
| 11 | scoring_rubric | N01_intelligence/quality/scoring_rubric_intelligence.md |

#### N02 Marketing (10 artefatos null)

| # | Kind | Path |
|---|------|------|
| 1 | agent | N02_marketing/P02_model/agent_marketing.md |
| 2 | agent_card | N02_marketing/architecture/agent_card_marketing.md |
| 3 | quality_gate | N02_marketing/P11_feedback/quality_gate_marketing.md |
| 4 | knowledge_card | N02_marketing/P01_knowledge/knowledge_card_marketing.md |
| 5 | dispatch_rule | N02_marketing/P12_orchestration/dispatch_rule_marketing.md |
| 6 | workflow | N02_marketing/P12_orchestration/workflow_marketing.md |
| 7 | action_prompt | N02_marketing/P03_prompt/action_prompt_marketing.md |
| 8 | prompt_template | N02_marketing/P03_prompt/prompt_template_marketing.md |
| 9 | system_prompt | N02_marketing/P03_prompt/system_prompt_marketing.md |
| 10 | scoring_rubric | N02_marketing/quality/scoring_rubric_marketing.md |

#### N04 Knowledge (12 artefatos null)

| # | Kind | Path |
|---|------|------|
| 1 | agent | N04_knowledge/P02_model/agent_knowledge.md |
| 2 | agent_card | N04_knowledge/architecture/agent_card_knowledge.md |
| 3 | quality_gate | N04_knowledge/P11_feedback/quality_gate_knowledge.md |
| 4 | chunk_strategy | N04_knowledge/P01_knowledge/chunk_strategy_knowledge.md |
| 5 | embedding_config | N04_knowledge/P01_knowledge/embedding_config_knowledge.md |
| 6 | knowledge_card | N04_knowledge/P01_knowledge/knowledge_card_knowledge.md |
| 7 | rag_source | N04_knowledge/P01_knowledge/rag_source_knowledge.md |
| 8 | retriever_config | N04_knowledge/P01_knowledge/retriever_config_knowledge.md |
| 9 | dispatch_rule | N04_knowledge/P12_orchestration/dispatch_rule_knowledge.md |
| 10 | workflow | N04_knowledge/P12_orchestration/workflow_knowledge.md |
| 11 | system_prompt | N04_knowledge/P03_prompt/system_prompt_knowledge.md |
| 12 | scoring_rubric | N04_knowledge/quality/scoring_rubric_knowledge.md |

#### N05 Operations (9 artefatos null)

| # | Kind | Path |
|---|------|------|
| 1 | agent | N05_operations/P02_model/agent_operations.md |
| 2 | agent_card | N05_operations/architecture/agent_card_operations.md |
| 3 | quality_gate | N05_operations/P11_feedback/quality_gate_operations.md |
| 4 | knowledge_card | N05_operations/P01_knowledge/knowledge_card_operations.md |
| 5 | checkpoint | N05_operations/P10_memory/checkpoint_operations.md |
| 6 | dispatch_rule | N05_operations/P12_orchestration/dispatch_rule_operations.md |
| 7 | spawn_config | N05_operations/P12_orchestration/spawn_config_operations.md |
| 8 | workflow | N05_operations/P12_orchestration/workflow_operations.md |
| 9 | system_prompt | N05_operations/P03_prompt/system_prompt_operations.md |

#### N06 Commercial (9 artefatos null)

| # | Kind | Path |
|---|------|------|
| 1 | agent | N06_commercial/P02_model/agent_commercial.md |
| 2 | agent_card | N06_commercial/architecture/agent_card_commercial.md |
| 3 | quality_gate | N06_commercial/P11_feedback/quality_gate_commercial.md |
| 4 | knowledge_card | N06_commercial/P01_knowledge/knowledge_card_commercial.md |
| 5 | dispatch_rule | N06_commercial/P12_orchestration/dispatch_rule_commercial.md |
| 6 | workflow | N06_commercial/P12_orchestration/workflow_commercial.md |
| 7 | prompt_template | N06_commercial/P03_prompt/prompt_template_commercial.md |
| 8 | system_prompt | N06_commercial/P03_prompt/system_prompt_commercial.md |
| 9 | scoring_rubric | N06_commercial/quality/scoring_rubric_commercial.md |

### Builder Archetypes

| Métrica | Valor |
|---------|-------|
| Builders | 98/99 (+ _builder-builder meta) |
| 13 ISOs por builder | ✅ 100% completo (1274 files) |
| Doctor result | 86 PASS, 12 WARN (size 1-74B over 4096B), 0 FAIL |
| KC Library | 98/300 kinds cobertos |

### Tools

| Tool | Status | Verificado |
|------|--------|-----------|
| cex_8f_motor.py | ✅ Intent → kind | Sim |
| cex_8f_runner.py | ✅ Lista 300 kinds, --dry-run, --execute | Sim |
| cex_doctor.py | ✅ Diagnostica 301 builders | Sim |
| cex_compile.py | ⬜ Aceita --all / --lp / single file | A testar |
| cex_index.py | ⬜ Aceita --query / --stats / --orphans | A testar |
| signal_writer.py | ✅ Gera signal_{nucleus}_{timestamp}.json | Sim |
| spawn_solo.ps1 | ✅ Multi-CLI, aceita n01-n06 | Sim |
| spawn_grid.ps1 | ✅ static/continuous, max 6 slots | Sim (com ressalvas) |
| spawn_monitor.ps1 | ⬜ Não testado | — |
| spawn_stop.ps1 | ⬜ Não testado | — |

---

## BUGS ENCONTRADOS NA v1.0 (CORRIGIDOS NESTA v2.0)

### 🔴 BUG 1: Grid não serve para Fase 3

**Problema**: `spawn_grid.ps1` extrai o nucleus do ÚLTIMO segmento do filename do handoff:
```powershell
# Get-NucleusFromHandoff
$parts = $base -split '_'
return $parts[-1]  # ultimo segmento
```

Se o handoff é `bootstrap_n01.md`, o grid lança `boot/n01.cmd` — que é o agente de Inteligência, NÃO o Builder.

Além disso, `$active[$nucleus]` usa nucleus como chave do dicionário. Se todos os handoffs terminam em `_n03`, apenas UMA instância N03 seria rastreada no loop de monitoramento.

**Impacto**: O grid lançaria os nuclei ERRADOS (N01, N02, N04, N05, N06) em vez de N03 para construir.

**Fix**: Fase 3 usa **spawn_solo sequencial** para N03, NÃO spawn_grid. Cada batch é um spawn_solo com handoff detalhado. Grid fica reservado para quando cada nucleus roda seu PRÓPRIO trabalho (não para cross-nucleus building).

### 🔴 BUG 2: signal_admin.md sem campo quality

**Problema**: `signal_admin.md` (3281 bytes, kind: signal) não tem campo `quality:` no frontmatter. O plano v1.0 listava apenas 9 artefatos N07 para rebuild — são **10**.

**Fix**: Incluído como artefato #10 no manifesto N07.

### 🟡 BUG 3: Contagem total errada

**Problema**: v1.0 dizia "60 artefatos para rebuild". Na verdade são **61** (60 null + 1 sem field).

**Fix**: Corrigido nesta versão.

---

## Plano de Execução (v2.0)

### Fase 0: Validar Ferramentas (10 min)

**Objetivo**: Confirmar que compile, index e runner funcionam end-to-end.

**Testes específicos**:

```bash
# Test 1: Compile um artefato golden existente
python _tools/cex_compile.py N03_engineering/P02_model/agent_engineering.md

# Test 2: Index rebuild + stats
python _tools/cex_index.py --stats

# Test 3: Runner dry-run para kind knowledge_card
python _tools/cex_8f_runner.py --kind knowledge_card --dry-run --verbose

# Test 4: Runner dry-run para kind agent
python _tools/cex_8f_runner.py --kind agent --dry-run --verbose

# Test 5: Signal writer sanity
python -c "from _tools.signal_writer import write_signal; write_signal('n07', 'test', 0.0, 'bootstrap_test')"
```

**Dispatch**: N07 executa diretamente (são testes de infra, não construção de artefatos).

**Critério de Aceite**: Todos 5 testes passam sem erro.

**Se falhar**: Corrigir a ferramenta antes de prosseguir. Sem ferramentas, sem bootstrap.

---

### Fase 1: Reconstruir N07 — O Orquestrador (1.5-2.5h)

**Objetivo**: N03 reconstrói os 10 artefatos de N07 com identidade REAL de orquestrador.

**Por que primeiro**: Sem N07 funcional, não há orchestração confiável para Fases 2-3.

**Dependência**: Fase 0 completa.

```
nodes:
  - id: f1_agent
    label: "Rebuild agent_admin.md — identidade de orquestrador multi-CLI"
    kind: agent
    priority: 1
    target: N07_admin/P02_model/agent_admin.md
    reference: N03_engineering/P02_model/agent_engineering.md (golden, 9.0)
    
  - id: f1_system_prompt
    label: "Rebuild system_prompt_admin.md — regras de dispatch, nunca construir"
    kind: system_prompt
    priority: 2
    target: N07_admin/P03_prompt/system_prompt_admin.md
    depends_on: [f1_agent]
    
  - id: f1_knowledge_card
    label: "Rebuild knowledge_card_admin.md — KC do domínio orchestration"
    kind: knowledge_card
    priority: 3
    target: N07_admin/P01_knowledge/knowledge_card_admin.md
    
  - id: f1_dispatch_rule
    label: "Rebuild dispatch_rule_admin.md — routing table N01-N06 real"
    kind: dispatch_rule
    priority: 4
    target: N07_admin/P12_orchestration/dispatch_rule_admin.md
    depends_on: [f1_agent]
    context: "Routing baseado em spawn_config_admin.md (quality 9.0)"
    
  - id: f1_dag
    label: "Rebuild dag_admin.md — DAG de orchestração com nodes reais"
    kind: dag
    priority: 5
    target: N07_admin/P12_orchestration/dag_admin.md
    
  - id: f1_workflow
    label: "Rebuild workflow_admin.md — solo/grid/monitor workflow"
    kind: workflow
    priority: 6
    target: N07_admin/P12_orchestration/workflow_admin.md
    depends_on: [f1_dispatch_rule]
    context: "Descrever os 3 modos: solo, grid static, grid continuous"
    
  - id: f1_handoff
    label: "Rebuild handoff_admin.md — template de handoff real com exemplos"
    kind: handoff
    priority: 7
    target: N07_admin/P12_orchestration/handoff_admin.md
    context: "Incluir formato markdown, campos obrigatórios, exemplo real"
    
  - id: f1_quality_gate
    label: "Rebuild quality_gate_admin.md — gates para orchestration"
    kind: quality_gate
    priority: 8
    target: N07_admin/P11_feedback/quality_gate_admin.md
    
  - id: f1_agent_card
    label: "Rebuild agent_card_admin.md — deployment spec N07"
    kind: agent_card
    priority: 9
    target: N07_admin/architecture/agent_card_admin.md
    depends_on: [f1_agent, f1_system_prompt]
    
  - id: f1_signal
    label: "Rebuild signal_admin.md — ADICIONAR frontmatter quality, enriquecer"
    kind: signal
    priority: 10
    target: N07_admin/P12_orchestration/signal_admin.md
    context: "Arquivo existe mas sem campo quality: no frontmatter. Completar."
```

**Dispatch**: `spawn_solo -nucleus n03 -task "..." -interactive`

**Handoff**: `.cex/runtime/handoffs/bootstrap_f1_n03.md` (conteúdo abaixo)

**Regras para N03**:
1. Ler N03_engineering/P02_model/agent_engineering.md como referência de quality 9.0
2. Ler N07_admin/P12_orchestration/spawn_config_admin.md (9.0) como referência de estilo N07
3. Ler N07_admin/P02_model/fallback_chain_admin.md (9.0) como referência de estilo N07
4. N07 identity = multi-CLI orchestrator, dispatch via spawn, NEVER builds directly
5. Cada artefato DEVE seguir 8F pipeline completo com builder ISOs
6. Compilar cada artefato após salvar: `python _tools/cex_compile.py PATH`
7. Commit incremental a cada 2-3 artefatos: `git add -A && git commit -m "[N03] rebuild N07 batch X"`
8. Signal ao final: `python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0, 'bootstrap_f1')"`

**Critério de Aceite**: Todos 10 artefatos quality >= 9.0. `python _tools/cex_doctor.py` sem erros em N07.

---

### Fase 2: Corrigir 12 WARNs dos Builders (30 min)

**Objetivo**: Comprimir 13 ISOs que excedem 4096B por 1-74 bytes.

**Dependência**: Nenhuma (independente). Pode rodar em paralelo com Fase 1 ou entre Fase 1 e 3.

**Recomendação**: Rodar ENTRE Fase 1 e Fase 3 como cooldown/warmup.

```
builders_warn:
  - action-prompt-builder    (bld_examples: 4102B, bld_memory: 4104B) — 2 files
  - agent-package-builder    (bld_system_prompt: 4101B)
  - benchmark-builder        (bld_memory: 4099B)
  - knowledge-index-builder      (bld_examples: 4098B)
  - dag-builder              (bld_memory: 4104B)
  - diagram-builder          (bld_examples: 4108B)
  - fallback-chain-builder   (bld_memory: 4097B)
  - feature-flag-builder     (bld_memory: 4100B)
  - hook-builder             (bld_quality_gate: 4101B)
  - mental-model-builder     (bld_examples: 4098B)
  - pattern-builder          (bld_examples: 4100B)
  - router-builder           (bld_examples: 4170B) — maior overflow: 74B
```

**Total**: 13 arquivos em 12 builders. Overflow médio: ~15B. Max: 74B (router-builder).

**Dispatch**: `spawn_solo -nucleus n03 -task "..." -interactive`

**Handoff**: `.cex/runtime/handoffs/bootstrap_f2_n03.md`

**Regras para N03**:
1. Tarefa cirúrgica: comprimir para <= 4096B sem perder informação
2. Técnicas: abreviar exemplos, remover linhas em branco redundantes, compactar tabelas
3. router-builder precisa de mais atenção (74B over = ~1 linha a remover)
4. Após comprimir: `python _tools/cex_doctor.py` para verificar 98 PASS

**Critério de Aceite**: Doctor → 98 PASS, 0 WARN, 0 FAIL.

---

### Fase 3: Rebuild Sequencial N01-N06 via N03 (3-4h)

**Objetivo**: N03 reconstrói todos os 51 artefatos quality:null dos 5 nuclei restantes.

**Dependência**: Fase 1 completa (N07 funcional). Fase 0 validada.

**⚠️ POR QUE NÃO USAR GRID (Bug #1)**:
- Grid extrai nucleus do filename e lança `boot/{nucleus}.cmd`
- Para rebuild, TODOS os artefatos precisam de N03 (o Builder)
- Grid lançaria boot/n01.cmd, boot/n02.cmd etc — agentes ERRADOS
- Grid usa `$active[$nucleus]` como chave — só rastreia 1 instância por nucleus
- Git conflicts com múltiplos N03 paralelos no mesmo repo

**Estratégia**: 5 batches sequenciais via `spawn_solo -nucleus n03`, um por nucleus alvo.

#### Batch 1: N01 Intelligence (11 artefatos)

**Handoff**: `.cex/runtime/handoffs/bootstrap_f3_batch1_n03.md`

```
Artefatos target (todos em N01_intelligence/):
1. agents/agent_intelligence.md (kind: agent)
2. architecture/agent_card_intelligence.md (kind: agent_card)
3. feedback/quality_gate_intelligence.md (kind: quality_gate)
4. knowledge/embedding_config_intelligence.md (kind: embedding_config)
5. knowledge/knowledge_card_intelligence.md (kind: knowledge_card)
6. knowledge/rag_source_intelligence.md (kind: rag_source)
7. orchestration/dispatch_rule_intelligence.md (kind: dispatch_rule)
8. orchestration/workflow_intelligence.md (kind: workflow)
9. prompts/prompt_template_intelligence.md (kind: prompt_template)
10. prompts/system_prompt_intelligence.md (kind: system_prompt)
11. quality/scoring_rubric_intelligence.md (kind: scoring_rubric)

Contexto N01: Nucleus de Inteligência. Pesquisa, análise, papers.
CLI: gemini 2.5-pro (1M context). Domínio: research, market analysis, competitive intel.
```

#### Batch 2: N02 Marketing (10 artefatos)

**Handoff**: `.cex/runtime/handoffs/bootstrap_f3_batch2_n03.md`

```
Artefatos target (todos em N02_marketing/):
1. agents/agent_marketing.md (kind: agent)
2. architecture/agent_card_marketing.md (kind: agent_card)
3. feedback/quality_gate_marketing.md (kind: quality_gate)
4. knowledge/knowledge_card_marketing.md (kind: knowledge_card)
5. orchestration/dispatch_rule_marketing.md (kind: dispatch_rule)
6. orchestration/workflow_marketing.md (kind: workflow)
7. prompts/action_prompt_marketing.md (kind: action_prompt)
8. prompts/prompt_template_marketing.md (kind: prompt_template)
9. prompts/system_prompt_marketing.md (kind: system_prompt)
10. quality/scoring_rubric_marketing.md (kind: scoring_rubric)

Contexto N02: Nucleus de Marketing. Copy, ads, conteúdo, branding.
CLI: claude sonnet. Domínio: creative writing, persuasion, brand voice.
```

#### Batch 3: N04 Knowledge (12 artefatos)

**Handoff**: `.cex/runtime/handoffs/bootstrap_f3_batch3_n03.md`

```
Artefatos target (todos em N04_knowledge/):
1. agents/agent_knowledge.md (kind: agent)
2. architecture/agent_card_knowledge.md (kind: agent_card)
3. feedback/quality_gate_knowledge.md (kind: quality_gate)
4. knowledge/chunk_strategy_knowledge.md (kind: chunk_strategy)
5. knowledge/embedding_config_knowledge.md (kind: embedding_config)
6. knowledge/knowledge_card_knowledge.md (kind: knowledge_card)
7. knowledge/rag_source_knowledge.md (kind: rag_source)
8. knowledge/retriever_config_knowledge.md (kind: retriever_config)
9. orchestration/dispatch_rule_knowledge.md (kind: dispatch_rule)
10. orchestration/workflow_knowledge.md (kind: workflow)
11. prompts/system_prompt_knowledge.md (kind: system_prompt)
12. quality/scoring_rubric_knowledge.md (kind: scoring_rubric)

Contexto N04: Nucleus de Knowledge. RAG, indexação, docs, chunking.
CLI: gemini 2.5-pro (1M context). Domínio: knowledge management, embeddings, retrieval.
```

#### Batch 4: N05 Operations (9 artefatos)

**Handoff**: `.cex/runtime/handoffs/bootstrap_f3_batch4_n03.md`

```
Artefatos target (todos em N05_operations/):
1. agents/agent_operations.md (kind: agent)
2. architecture/agent_card_operations.md (kind: agent_card)
3. feedback/quality_gate_operations.md (kind: quality_gate)
4. knowledge/knowledge_card_operations.md (kind: knowledge_card)
5. memory/checkpoint_operations.md (kind: checkpoint)
6. orchestration/dispatch_rule_operations.md (kind: dispatch_rule)
7. orchestration/spawn_config_operations.md (kind: spawn_config)
8. orchestration/workflow_operations.md (kind: workflow)
9. prompts/system_prompt_operations.md (kind: system_prompt)

Contexto N05: Nucleus de Operations. Deploy, test, debug, CI/CD.
CLI: codex GPT-5.4. Domínio: code review, testing, infrastructure.
```

#### Batch 5: N06 Commercial (9 artefatos)

**Handoff**: `.cex/runtime/handoffs/bootstrap_f3_batch5_n03.md`

```
Artefatos target (todos em N06_commercial/):
1. agents/agent_commercial.md (kind: agent)
2. architecture/agent_card_commercial.md (kind: agent_card)
3. feedback/quality_gate_commercial.md (kind: quality_gate)
4. knowledge/knowledge_card_commercial.md (kind: knowledge_card)
5. orchestration/dispatch_rule_commercial.md (kind: dispatch_rule)
6. orchestration/workflow_commercial.md (kind: workflow)
7. prompts/prompt_template_commercial.md (kind: prompt_template)
8. prompts/system_prompt_commercial.md (kind: system_prompt)
9. quality/scoring_rubric_commercial.md (kind: scoring_rubric)

Contexto N06: Nucleus Comercial. Sales, pricing, cursos, monetização.
CLI: claude sonnet. Domínio: persuasive copy, pricing strategy, sales funnels.
```

**Regras para N03 (todas as batches)**:
1. Ler os 13 ISOs do builder correspondente ao kind antes de produzir
2. Ler exemplos golden de N03_engineering/ como referência de quality 9.0
3. Cada artefato DEVE conter o contexto do nucleus TARGET (não de N03)
4. Pipeline 8F completo com trace visível para CADA artefato
5. Compilar cada artefato: `python _tools/cex_compile.py PATH`
6. Commit a cada 3-4 artefatos: `git add -A && git commit -m "[N03] rebuild {NXX} batch"`
7. Signal ao final de cada batch
8. Se quality < 8.0 em qualquer artefato: retry imediato antes de prosseguir

**Critério de Aceite**: Todos 51 artefatos quality >= 8.0 (target 9.0+).

---

## Dependências (v2.0)

```
Fase 0 ──→ Fase 1 ──→ Fase 2 ──→ Fase 3
                                    ├── Batch 1 (N01, 11 arts)
                                    ├── Batch 2 (N02, 10 arts)
                                    ├── Batch 3 (N04, 12 arts)
                                    ├── Batch 4 (N05, 9 arts)
                                    └── Batch 5 (N06, 9 arts)
```

**Fase 0 → Fase 1**: Sequencial (tools devem funcionar antes de build).
**Fase 1 → Fase 2**: Sequencial (N07 pronto antes de fix WARNs).
**Fase 2 → Fase 3**: Sequencial (Doctor limpo antes de mass rebuild).
**Batches 1-5**: Sequenciais via spawn_solo (evita git conflicts).

---

## Comandos de Dispatch (N07 executa)

### Fase 0 (N07 direto)
```bash
python _tools/cex_compile.py N03_engineering/P02_model/agent_engineering.md
python _tools/cex_index.py --stats
python _tools/cex_8f_runner.py --kind knowledge_card --dry-run --verbose
python _tools/cex_8f_runner.py --kind agent --dry-run --verbose
python -c "from _tools.signal_writer import write_signal; write_signal('n07', 'test', 0.0, 'bootstrap_test')"
```

### Fase 1 (spawn N03)
```powershell
# Escrever handoff primeiro (N07 faz), depois:
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f1_n03.md. Reconstrua os 10 artefatos de N07 listados. 8F obrigatorio. Quality 9.0+. Compile cada um. Commit e signal." -interactive
```

### Fase 2 (spawn N03)
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f2_n03.md. Comprima 13 arquivos de builders para <= 4096B. Doctor deve dar 98 PASS 0 WARN. Commit e signal." -interactive
```

### Fase 3 — Batches 1-5 (spawn N03 sequencial)
```powershell
# Batch 1: N01
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f3_batch1_n03.md. Reconstrua 11 artefatos de N01_intelligence. 8F obrigatorio. Quality 9.0+. Compile cada um. Commit e signal." -interactive

# Batch 2: N02 (após signal do Batch 1)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f3_batch2_n03.md. Reconstrua 10 artefatos de N02_marketing. 8F obrigatorio. Quality 9.0+. Compile cada um. Commit e signal." -interactive

# Batch 3: N04 (após signal do Batch 2)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f3_batch3_n03.md. Reconstrua 12 artefatos de N04_knowledge. 8F obrigatorio. Quality 9.0+. Compile cada um. Commit e signal." -interactive

# Batch 4: N05 (após signal do Batch 3)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f3_batch4_n03.md. Reconstrua 9 artefatos de N05_operations. 8F obrigatorio. Quality 9.0+. Compile cada um. Commit e signal." -interactive

# Batch 5: N06 (após signal do Batch 4)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/bootstrap_f3_batch5_n03.md. Reconstrua 9 artefatos de N06_commercial. 8F obrigatorio. Quality 9.0+. Compile cada um. Commit e signal." -interactive
```

---

## Riscos (v2.0)

| # | Risco | Prob | Impacto | Mitigação |
|---|-------|------|---------|-----------|
| 1 | Tools falham na Fase 0 | Média | Alto | Corrigir antes de prosseguir. Sem tools = sem bootstrap |
| 2 | N03 produz artefatos genéricos/placeholder | Alta | Alto | Handoff detalhado com contexto do nucleus target + exemplos golden |
| 3 | Quality < 8.0 em batch grande | Média | Médio | Retry individual via spawn_solo. Signal inclui lista de fails |
| 4 | N03 perde contexto em sessão longa (>10 arts) | Média | Médio | Batches de max 12 artefatos. Refresh de contexto no handoff |
| 5 | Git conflicts entre fases | Baixa | Alto | Sequencial. Commit + push entre fases |
| 6 | Spawn_solo falha (CLI crash) | Baixa | Médio | Re-spawn. Handoff persiste em disco |
| 7 | Builder ISOs desatualizados para kinds específicos | Baixa | Baixo | Doctor valida. KC library cobre 98/300 kinds |

---

## Timeline Estimada

| Fase | Duração | Artefatos | Acumulado |
|------|---------|-----------|-----------|
| Fase 0 | 10 min | 0 (validation) | 10 min |
| Fase 1 | 1.5-2.5h | 10 (N07) | 2-3h |
| Fase 2 | 30 min | 13 files (trim) | 2.5-3.5h |
| Fase 3 Batch 1 | 40 min | 11 (N01) | 3-4h |
| Fase 3 Batch 2 | 35 min | 10 (N02) | 3.5-4.5h |
| Fase 3 Batch 3 | 45 min | 12 (N04) | 4-5.5h |
| Fase 3 Batch 4 | 30 min | 9 (N05) | 4.5-6h |
| Fase 3 Batch 5 | 30 min | 9 (N06) | 5-7h |
| **TOTAL** | **5-7h** | **61 artefatos + 13 fixes** | |

---

## Métricas de Sucesso

| Métrica | Antes | Depois |
|---------|-------|--------|
| Artefatos quality >= 8.0 | 36/95 | 95/95 |
| Artefatos quality: null | 60 | 0 |
| Artefatos sem field quality | 1 | 0 |
| Doctor builders PASS | 86/98 | 98/98 |
| Doctor builders WARN | 12 | 0 |
| N07 identidade real | ❌ | ✅ |
| N01-N06 identidade real | ❌ | ✅ |
| Auto-bootstrap funcional | ❌ | ✅ |

---

## Checklist de Validação Final (após todas as fases)

```bash
# 1. Doctor limpo
python _tools/cex_doctor.py
# Expect: 98 PASS, 0 WARN, 0 FAIL

# 2. Zero quality null
grep -r "^quality: null" N0*/ --include="*.md" | wc -l
# Expect: 0

# 3. Index rebuild
python _tools/cex_index.py --stats
# Expect: all artifacts indexed

# 4. Git clean
git status
# Expect: nothing to commit

# 5. Compile all
python _tools/cex_compile.py --all
# Expect: no errors
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[index]] | upstream | 0.24 |
| [[p10_bi_intelligence_outputs]] | upstream | 0.22 |
| [[p12_sig_admin_orchestration]] | related | 0.21 |
| [[p08_ac_admin_orchestrator]] | upstream | 0.21 |
| [[p02_nd_n01.md]] | upstream | 0.20 |
| [[p12_ho_admin_template]] | related | 0.19 |
| [[n01_selfheal_w2_diagnosis]] | upstream | 0.18 |
| [[release_check_fixes_20260413]] | upstream | 0.18 |
| [[p01_kc_orchestration]] | upstream | 0.17 |
| [[bld_schema_integration_guide]] | upstream | 0.17 |
