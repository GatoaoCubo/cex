# Generator: P12 Orchestration

## QUANDO USAR
- Documentar workflow (steps sequenciais ou paralelos)
- Criar DAG de dependencias entre tarefas
- Configurar spawn (solo, grid, continuous)
- Definir sinal entre agentes (complete, error, progress)
- Escrever handoff (task + context + commit)
- Estabelecer regra de despacho (keyword > satellite)

## TIPOS (escolher template)

### workflow
Naming: `p12_wf_{{name}}.md + .yaml` | Max: 2048 bytes
- Campos: steps[], parallel_groups[], inputs, outputs, timeout
- Exemplo: CLARIFY > ENRICH > COMPOSE > EXECUTE > MONITOR

### dag
Naming: `p12_dag_{{pipeline}}.yaml` | Max: 1024 bytes
- Campos: nodes[], edges[], root, terminal, critical_path
- Exemplo: build depende de test, deploy depende de build

### spawn_config
Naming: `p12_spawn_{{mode}}.yaml` | Max: 1024 bytes
- Campos: mode (solo/grid/continuous), satellites[], max_concurrent, delay
- Exemplo: grid 3 sats, 5s delay, max 3 concurrent

### signal
Naming: `p12_sig_{{event}}.json` | Max: 256 bytes
- Campos: satellite, status (complete/error/progress), score, timestamp
- Exemplo: edison_complete_1711100000.json

### handoff
Naming: `p12_ho_{{task}}.md` | Max: 2048 bytes
- Campos: contexto, seeds, tarefas[], scope_fence, commit_template
- Exemplo: wave dispatch com autonomia total

### dispatch_rule
Naming: `p12_dr_{{scope}}.yaml` | Max: 512 bytes
- Campos: keywords[], satellite, model, priority, fallback_sat
- Exemplo: "pesquisar, mercado" -> SHAKA (sonnet)

## PASSO A PASSO
1. SCOUT: verificar se orquestracao similar ja existe
2. CLASSIFICAR: qual dos 6 tipos? (workflow, dag, spawn, signal, handoff, dispatch)
3. Para workflow: definir steps com input/output de cada fase
4. Para dag: garantir que eh aciclico (sem loops)
5. Para spawn: definir max_concurrent e delay entre spawns
6. Para handoff: incluir scope_fence (SOMENTE/NAO TOQUE)
7. Para dispatch: incluir fallback_sat (se primario indisponivel)
8. VALIDAR contra P12/_schema.yaml
9. SALVAR no formato do tipo escolhido

## TESTE DE EXECUTABILIDADE
Cada orquestracao: um agente consegue executar sem ambiguidade?
- SIM: "spawn SHAKA sonnet, task: research [X], timeout 10min" -> mantem
- NAO: "Coordinate the satellites" -> falta: quais, como, quando

## ANTI-PATTERNS
- Workflow sem timeout (execucao infinita)
- DAG com ciclos (deadlock)
- Spawn sem max_concurrent (BSOD por RAM)
- Signal sem timestamp (nao se sabe ordem)
- Handoff sem scope_fence (satelite toca o que nao deve)
- Dispatch sem fallback (task perdida se sat indisponivel)

---
*Generator v1.0 | Evidence: STELLA dispatch + spawn_grid + 7 satellites | 2026-03-22*