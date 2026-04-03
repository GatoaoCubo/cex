---
id: skill_swarm_autonomy
kind: skill
pillar: P12
title: "Swarm Autonomy — Multi-Nucleus Self-Organization"
version: 1.0.0
created: 2026-04-03
author: n07_orchestrator
quality: null
tags: [swarm, autonomy, multi-agent, spawn, handoff, emergent]
tldr: "Skill que habilita qualquer núcleo a spawnar colegas, criando cadeias autônomas de produção. Descoberto empiricamente na missão BRAND_GATO3."
---

# Skill: Swarm Autonomy

## Quando usar

Quando uma missão é **complexa demais para um único núcleo** — envolve research + build + copy + code + brand em sequência ou paralelo.

## Pré-requisitos (checklist)

- [ ] `_spawn/dispatch.sh` existe e funciona
- [ ] `boot/n0{1-6}.cmd` configurados com CLI + modelo
- [ ] `.cex/runtime/handoffs/` acessível para escrita
- [ ] `_tools/signal_writer.py` no path
- [ ] `--dangerously-skip-permissions` habilitado em todos os boots
- [ ] `CLAUDE.md` documenta routing table (qual núcleo faz o quê)
- [ ] Git branch compartilhada (todos commitam no mesmo lugar)

## Os 4 Padrões

### P1: Perceive → Spawn
```
QUANDO: Estou fazendo tarefa X e percebo que preciso de skill Y que não tenho
ENTÃO:
  1. git add && git commit (salvar MEU progresso)
  2. Escrever handoff detalhado em .cex/runtime/handoffs/{MISSION}_{nucleus}.md
  3. bash _spawn/dispatch.sh solo {nucleus} "{task_summary}"
  4. Continuar MEU trabalho (não esperar)
```

### P2: Complete → Decompose
```
QUANDO: Terminei minha fase e vejo próximos passos que precisam de múltiplos domínios
ENTÃO:
  1. git add && git commit (entregar MEU trabalho)
  2. python _tools/signal_writer.py {me} complete 9.0 {MISSION}
  3. Escrever N handoffs para os próximos núcleos (um por domínio)
  4. Spawnar todos em sequência rápida
  5. NÃO spawnar a mim mesmo (evitar loop)
```

### P3: Feedback Loop
```
QUANDO: Preciso de algo do colega → colega entrega → preciso de refinamento
ENTÃO:
  1. Checar git log para ver se colega commitou
  2. Checar .cex/runtime/signals/ para status
  3. Se preciso de melhoria, escrever NOVO handoff (não reusar o anterior)
  4. Máximo 2 ciclos de refinamento (evitar loop infinito)
```

### P4: Wave Planning
```
QUANDO: Identifico dependências entre tarefas futuras
ENTÃO:
  1. Nomear handoffs com prefixo de fase: PHASE{N}_{domain}_{nucleus}.md
  2. Handoffs independentes: spawnar todos em paralelo
  3. Handoffs dependentes: incluir "ESPERE signal de {nucleus} antes de executar"
  4. Incluir no handoff: quais signals monitorar como pré-requisito
```

## Template: Swarm Seed Handoff

Incluir esta seção em QUALQUER handoff para habilitar autonomia:

```markdown
## 🔀 Autonomia Swarm

Este núcleo tem permissão para spawnar colegas quando necessário.

### Como spawnar outro núcleo:
1. Commitar seu trabalho atual: `git add {seus_arquivos} && git commit -m "[N0X] {msg}" --no-verify`
2. Escrever handoff detalhado: `.cex/runtime/handoffs/{MISSION}_{target_nucleus}.md`
3. Spawnar: `bash _spawn/dispatch.sh solo {nucleus} "{task}"`
4. Continuar seu trabalho — NÃO espere

### Routing table:
| Preciso de... | Spawnar | Boot |
|---------------|---------|------|
| Pesquisa de mercado, dados, validação | N01 | boot/n01-claude.cmd |
| Copy, campanhas, outreach, HTML visual | N02 | boot/n02.cmd |
| Build code, pipelines, automação | N03 | boot/n03.cmd |
| Documentação, knowledge cards | N04 | boot/n04.cmd |
| Deploy, infra, CI/CD, testes | N05 | boot/n05.cmd |
| Branding, pricing, revenue, comercial | N06 | boot/n06.cmd |

### Regras de spawn:
- ✅ Commitar ANTES de spawnar
- ✅ Handoff DETALHADO (contexto + dados + output esperado + signal)
- ✅ Um núcleo por domínio (não spawnar 2x o mesmo)
- ✅ Signal quando VOCÊ terminar (independente dos spawns)
- ❌ NÃO spawnar loops (máx 2 ciclos feedback)
- ❌ NÃO spawnar N07 (orquestrador é humano)
- ❌ NÃO spawnar mais de 4 núcleos de uma vez (resource limit)

### Como checar se colega terminou:
```bash
# Ver signals
ls .cex/runtime/signals/signal_{nucleus}_*.json
cat .cex/runtime/signals/signal_{nucleus}_*.json

# Ver commits
git log --oneline -5 | grep "\[N0X\]"

# Ver status geral
bash _spawn/dispatch.sh status
```
```

## Anti-Patterns

| ❌ Anti-pattern | ✅ Correção |
|----------------|-------------|
| Spawnar sem commitar | SEMPRE commitar antes |
| Handoff genérico ("faça algo") | Handoff com contexto, dados, output, signal |
| Spawnar 6 núcleos em paralelo | Máximo 4, priorizar os essenciais |
| Esperar colega (bloqueio) | Continuar trabalho próprio, checar depois |
| Spawnar a si mesmo | Escrever handoff e deixar N07 decidir |
| Loop infinito de refinamento | Máximo 2 ciclos feedback |
| Editar arquivo de outro núcleo | Cada um no seu diretório |

## Métricas de Sucesso

| Métrica | Threshold |
|---------|-----------|
| Autonomia ratio | > 50% commits autônomos |
| Handoff quality | Handoffs com > 2KB de contexto |
| Spawn success rate | > 80% spawns resultam em commit |
| Cycle time | < 30min por nucleus task |
| Conflict rate | < 5% merge conflicts |

## Caso de Estudo: BRAND_GATO3

| Fase | O que aconteceu | Núcleos | Resultado |
|------|-----------------|---------|-----------|
| Seed | N07 despachou N01 para CRM research | 1 | 26 contatos |
| Growth | N01 spawnou N03 para pipeline | 2 | Pipeline + 112 contatos |
| Bloom | N01 usou pipeline, spawnou N03 v2 | 2 | 202+ contatos + 27 módulos |
| Explosion | N01 decompos Phase 4: 5 handoffs | 5 | N01+N02+N03+N06 em paralelo |
| Harvest | 6 núcleos entregando simultaneamente | 6 | 282+ contatos, 40+ artefatos |

**De 1 núcleo para 6 em ~4 horas, com ~65% de autonomia.**

---

## Integração com Workflow CEX

Para usar em qualquer missão futura, basta:

1. Incluir `## 🔀 Autonomia Swarm` no handoff do primeiro núcleo
2. Garantir pré-requisitos (checklist acima)
3. Monitorar via `bash _spawn/dispatch.sh status`
4. Consolidar via N07 quando signals indicarem complete

O skill é **opt-in** — só ativa se o handoff incluir a seção de autonomia.
Sem a seção, o núcleo executa sua tarefa solo normalmente.
