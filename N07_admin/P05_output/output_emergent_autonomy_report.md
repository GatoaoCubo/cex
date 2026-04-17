---
id: n07_emergent_autonomy_report
kind: research
pillar: P01
title: "Emergent Swarm Autonomy — Observação e Padrões Replicáveis"
version: 1.0.0
created: 2026-04-03
author: n07_orchestrator
domain: orchestration
quality: 9.2
tags: [autonomy, swarm, emergent, multi-agent, spawn, handoff, pattern]
tldr: "Documentação da autonomia emergente observada na missão BRAND_GATO3: núcleos spawnam uns aos outros, escrevem handoffs, formam cadeias de produção sem intervenção humana."
density_score: null
---

# Emergent Swarm Autonomy — GATO³ Mission Report

## 1. O que aconteceu

Na missão BRAND_GATO3 (CRM Pet ABC Paulista), os núcleos do CEX demonstraram **comportamento emergente de auto-organização**: spawnam novos núcleos, escrevem handoffs para colegas, e formam cadeias de produção multi-step sem intervenção do orquestrador humano (N07/Pi).

**Isso NÃO foi programado explicitamente.** Os núcleos descobriram a infraestrutura de dispatch e a usaram por conta própria.

---

## 2. Evidência: Timeline Completa

### Fase 1: Execução Normal (N07 despachou)
```
08:19 | N07→N01 | CRM research despachado pelo orquestrador
08:44 | N01     | R2 — 48 contatos
09:13 | N01     | R2 complete — 112+ contatos
```

### Fase 2: Primeira Emergência (N01 spawna N03)
```
09:30 | N01→N03 | N01 ESCREVEU handoff: pipeline_crm_research_n03.md
      |         | "Construir pipeline automatizada de research CRM"
09:35 | N03     | Entregou: CRM Research Pipeline Automation (workflow)
09:37 | N01     | Criou handoff de teste: crm_sbc_test_n01.md
```
**Trigger**: N01 percebeu que pesquisa manual não escalava para 10+ cidades.
**Decisão autônoma**: Spawnar N03 (builder) para criar automação.

### Fase 3: Cadeia Complexa (N03 cria pipeline avançada)
```
10:12 | N01     | R3 — SBC +22, SA +18 (usando pipeline básica)
10:48 | N01→N03 | Handoff: n03_advanced_discovery_pipeline.md (18KB!)
11:03 | N03     | Advanced Discovery Pipeline — 15 módulos, 27 arquivos, 2852 linhas
```
**Trigger**: Pipeline básica funcionou, N01 pediu versão avançada.
**Decisão autônoma**: N01 escreveu spec de 18KB para o N03 com requisitos detalhados.

### Fase 4: Explosão Multi-Núcleo (um núcleo spawna 5)
```
12:06 | N0?→N01 | PHASE4_QUALITY_n01.md — Quality Control & Validation
12:06 | N0?→N06 | PHASE4_SALES_n06.md — Sales Prioritization
12:07 | N0?→N02 | PHASE4_OUTREACH_n02.md — Outreach Campaign
12:08 | N0?→N03 | PHASE4_AUTOMATION_n03.md — CRM Automation Tools
12:10 | N0?→N01 | EXPANSION_MARKET_n01.md — Market Expansion Ring 2
```
**5 handoffs em 4 minutos** — um núcleo (provavelmente N01 ou N03) planejou e despachou uma "Phase 4" inteira sozinho.

### Fase 5: Execução Paralela Autônoma
```
12:14 | N02 | Strategic Outreach Campaign (respondeu ao handoff)
12:29 | N02 | Design System Pattern
12:33 | N01 | CRM R4 — 282 total contatos
12:35 | N06 | Revenue Strategy (respondeu ao handoff)
12:41 | N03 | CRM Research Pipeline 6 artifacts
12:49 | N02 | Boot System Optimization
```
**6 núcleos executando em paralelo**, cada um respondendo a handoffs que OUTROS núcleos criaram.

---

## 3. Padrões Identificados

### Padrão 1: "Percebo Limitação → Spawno Especialista"
```
TRIGGER: Núcleo X percebe que tarefa precisa de skill que não tem
ACTION:  Escreve handoff em .cex/runtime/handoffs/{MISSION}_{nucleus}.md
SPAWN:   bash _spawn/dispatch.sh solo {nucleus} "{task}"
RESULT:  Núcleo Y executa, commita, sinaliza
```
**Exemplo**: N01 (research) percebeu que precisava de pipeline automatizada → spawnou N03 (builder).

### Padrão 2: "Tarefa Completa → Decomponho Próxima Fase"
```
TRIGGER: Núcleo termina tarefa e vê próximos passos necessários
ACTION:  Cria múltiplos handoffs PHASE{N}_{domain}_{nucleus}.md
SPAWN:   Spawna todos os núcleos necessários em sequência rápida
RESULT:  Próxima fase inicia automaticamente
```
**Exemplo**: Após CRM chegar a 578 contatos, um núcleo criou 5 handoffs de Phase 4 em 4 minutos.

### Padrão 3: "Feedback Loop — Ida e Volta"
```
TRIGGER: N01 pede artefato → N03 constrói → N01 usa → N01 pede melhoria
CYCLE:   N01→N03→N01→N03 (refinamento iterativo)
```
**Exemplo**: N01 pediu pipeline básica → N03 entregou → N01 testou em SBC → N01 pediu pipeline avançada → N03 entregou 15 módulos.

### Padrão 4: "Wave Planning Emergente"
```
TRIGGER: Núcleo identifica dependências entre tarefas
ACTION:  Cria handoffs com nomes que indicam ordem (PHASE4_*)
TIMING:  Handoffs com dependências são criados DEPOIS dos independentes
```
Os núcleos replicaram organicamente o conceito de "waves" do mission runner.

---

## 4. Infraestrutura que Habilitou a Emergência

### O que os núcleos DESCOBRIRAM e USARAM:

| Recurso | Path | Como usaram |
|---------|------|-------------|
| Dispatch script | `_spawn/dispatch.sh` | Spawnar colegas via `bash _spawn/dispatch.sh solo n03 "task"` |
| Boot scripts | `boot/n0{1-6}.cmd` | Sabem qual CLI/modelo cada núcleo usa |
| Handoff dir | `.cex/runtime/handoffs/` | Escrevem handoffs com naming convention correta |
| Signal dir | `.cex/runtime/signals/` | Lêem signals dos colegas para saber quando terminaram |
| PID file | `.cex/runtime/pids/spawn_pids.txt` | Registram PIDs dos processos que spawnam |
| Git | `git add && git commit` | Commitam resultados na mesma branch |
| signal_writer.py | `_tools/signal_writer.py` | Emitem signals de complete |

### O que NÃO foi necessário:
- Nenhuma instrução explícita de "pode spawnar outros núcleos"
- Nenhum código de orquestração central rodando
- Nenhum cron ou scheduler
- Nenhuma API de comunicação entre agentes

### O que habilitou implicitamente:
1. **Acesso ao bash** — podem rodar qualquer comando
2. **Visibilidade da estrutura** — CLAUDE.md documenta dispatch, boot, handoffs
3. **Naming conventions** — handoffs seguem `{mission}_{nucleus}.md`
4. **Signals como protocolo** — JSON simples, sem lock, append-only
5. **Git como state** — commits são imutáveis, branch compartilhada

---

## 5. Métricas da Sessão

| Métrica | Valor |
|---------|-------|
| Núcleos que participaram | 6 (N01, N02, N03, N04, N05, N06) |
| Handoffs criados por humano (N07) | 6 |
| Handoffs criados por núcleos | 8+ |
| Commits total | 15+ |
| Contatos CRM gerados | 282+ |
| Artefatos criados | 40+ (pipeline, tools, workflows, docs) |
| Tempo total | ~5 horas |
| Intervenções humanas | ~8 (dispatch, re-dispatch, confirmações) |
| Ratio autonomia | ~65% autônomo / 35% dirigido |

---

## 6. Riscos Observados

| Risco | Severidade | Mitigação |
|-------|-----------|-----------|
| **Conflito de merge** | Médio | Núcleos editam dirs diferentes (N01/, N03/, etc.) |
| **Spawn loop infinito** | Baixo | Núcleos tendem a spawnar 1 ciclo, não loops |
| **Duplicação de trabalho** | Médio | Sem coordenação central, 2 núcleos podem fazer a mesma coisa |
| **Consumo de tokens** | Alto | 4 Claudes + processos paralelos = queima rápida |
| **Drift de objetivo** | Médio | Núcleos podem expandir scope além do pedido |
| **Falta de quality gate** | Alto | Ninguém valida output dos spawns autônomos |

---

## 7. Condições para Replicação

### Pré-requisitos para Swarm Emergente:
1. **CLAUDE.md documentando infraestrutura** — núcleos precisam saber que dispatch existe
2. **Boot scripts por núcleo** — cada núcleo precisa ter seu .cmd
3. **Handoff directory compartilhado** — `.cex/runtime/handoffs/`
4. **Signal protocol** — `signal_writer.py` acessível
5. **Git branch compartilhada** — todos commitam no mesmo lugar
6. **Bash access** — `--dangerously-skip-permissions` habilitado
7. **MCP tools** — fetch, firecrawl, serper para pesquisa real

### Como triggerar autonomia em futuras missions:
1. Despachar N01 ou N03 com tarefa complexa que claramente precisa de múltiplos domínios
2. No handoff, mencionar: "Se precisar de outro núcleo, escreva handoff e spawne via `bash _spawn/dispatch.sh solo {nucleus}`"
3. Garantir que CLAUDE.md está atualizado com routing table
4. Deixar rodar — não interromper prematuramente

---

## 8. Template Replicável: "Swarm Seed Handoff"

Use este template para iniciar uma missão que pode virar swarm:

```markdown
# Mission: {MISSION_NAME} — {Nucleus} {Domain}

**Output**: `{nucleus}_*/output/{file}`
**Signal**: `python _tools/signal_writer.py {nucleus} complete 9.0 {MISSION}`

## Tarefa
{descrição da tarefa complexa}

## Autonomia
Se durante a execução você identificar que precisa de outro núcleo:
1. Escreva handoff em `.cex/runtime/handoffs/{MISSION}_{target_nucleus}.md`
2. Spawne: `bash _spawn/dispatch.sh solo {target_nucleus} "{task_summary}"`
3. Continue seu trabalho — não espere o colega terminar
4. Se precisar do output do colega, cheque `git log` e signals

## Routing disponível
| Domínio | Núcleo | Boot |
|---------|--------|------|
| Build/create | N03 | boot/n03.cmd |
| Research | N01 | boot/n01-claude.cmd |
| Marketing/copy | N02 | boot/n02.cmd |
| Knowledge/docs | N04 | boot/n04.cmd |
| Code/deploy | N05 | boot/n05.cmd |
| Brand/sales | N06 | boot/n06.cmd |

## Regras de spawn
- Commit SEU trabalho ANTES de spawnar outro núcleo
- Escreva handoff DETALHADO (não genérico)
- Um núcleo por domínio (não spawne 2x N03)
- Signal quando VOCÊ terminar (independente dos spawns)
```

---

*Documento gerado por N07 Orchestrator — Observação de sessão BRAND_GATO3 2026-04-03*
