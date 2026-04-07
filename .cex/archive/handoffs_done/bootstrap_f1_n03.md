# N03 Task: Rebuild N07 Orchestrator — 10 Artefatos
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO

Você é N03 Builder. Sua missão: reconstruir os 10 artefatos do N07 (Orchestrator/Admin) que estão com quality: null ou sem campo quality. O N07 é o Orquestrador do CEX — ele NUNCA constrói artefatos, apenas despacha tarefas via spawn_solo/spawn_grid para os nuclei N01-N06.

## REFERÊNCIAS DE QUALIDADE (LEIA ANTES DE COMEÇAR)

1. **Golden agent (9.0)**: `N03_engineering/agents/agent_engineering.md` — como um agent 9.0 se parece
2. **Golden spawn_config (9.0)**: `N07_admin/orchestration/spawn_config_admin.md` — estilo N07 real
3. **Golden fallback_chain (9.0)**: `N07_admin/agents/fallback_chain_admin.md` — estilo N07 real
4. **Mission plan (contexto completo)**: `N07_admin/orchestration/mission_bootstrap_2026Q1.md`

## IDENTIDADE DO N07 (use em TODOS os artefatos)

- **Role**: Orquestrador multi-CLI do CEX
- **NUNCA constrói** artefatos — despacha para N03 via spawn
- **Dispatch**: spawn_solo.ps1 (1 builder) ou spawn_grid.ps1 (até 6 paralelos)
- **CLI**: pi + claude opus (xhigh thinking)
- **Domínio**: orchestration, dispatch, monitoring, quality validation
- **agent_group**: admin / orchestrator
- **Routing**: N01 (gemini, research), N02 (claude sonnet, marketing), N03 (claude opus, build), N04 (gemini, knowledge), N05 (codex, ops), N06 (claude sonnet, commercial)
- **Tools**: spawn_solo, spawn_grid, spawn_monitor, spawn_stop, cex_doctor, cex_feedback, signal_writer
- **Monitoring**: lê sinais em _ops/signals/, valida quality >= 8.0

## 10 ARTEFATOS PARA REBUILD

Construa na ordem abaixo. Para CADA artefato, siga o 8F pipeline completo com builder ISOs.

### 1. agent_admin.md (kind: agent)
- **Path**: `N07_admin/agents/agent_admin.md`
- **Builder**: `archetypes/builders/agent-builder/` (13 ISOs)
- **Conteúdo**: Identidade completa do N07 como orquestrador. Capabilities: dispatch, monitor, validate, route, handoff. NUNCA build.
- **Referência**: `N03_engineering/agents/agent_engineering.md`

### 2. system_prompt_admin.md (kind: system_prompt)
- **Path**: `N07_admin/prompts/system_prompt_admin.md`
- **Builder**: `archetypes/builders/system-prompt-builder/` (13 ISOs)
- **Conteúdo**: System prompt que instrui o LLM a ser o orquestrador. Regras: nunca construir, sempre dispatch, validar quality, monitorar signals.
- **Depende de**: #1 (agent)

### 3. knowledge_card_admin.md (kind: knowledge_card)
- **Path**: `N07_admin/knowledge/knowledge_card_admin.md`
- **Builder**: `archetypes/builders/knowledge-card-builder/` (13 ISOs)
- **Conteúdo**: KC destilado sobre o domínio orchestration — routing table, spawn modes, signal protocol, quality tiers.

### 4. dispatch_rule_admin.md (kind: dispatch_rule)
- **Path**: `N07_admin/orchestration/dispatch_rule_admin.md`
- **Builder**: `archetypes/builders/dispatch-rule-builder/` (13 ISOs)
- **Conteúdo**: Regras de roteamento reais. Quando usar N01 vs N02 vs N03 vs N04 vs N05 vs N06. CLI mapping. Fallback rules.
- **Depende de**: #1 (agent)
- **Referência**: `N07_admin/orchestration/spawn_config_admin.md` (routing table real)

### 5. dag_admin.md (kind: dag)
- **Path**: `N07_admin/orchestration/dag_admin.md`
- **Builder**: `archetypes/builders/dag-builder/` (13 ISOs)
- **Conteúdo**: DAG de orchestração do N07 — nodes reais (receive intent → classify → route → dispatch → monitor → validate → signal). NÃO placeholder genérico.

### 6. workflow_admin.md (kind: workflow)
- **Path**: `N07_admin/orchestration/workflow_admin.md`
- **Builder**: `archetypes/builders/workflow-builder/` (13 ISOs)
- **Conteúdo**: 3 workflows reais: (a) solo dispatch, (b) grid static, (c) grid continuous. Steps concretos com comandos.
- **Depende de**: #4 (dispatch_rule)

### 7. handoff_admin.md (kind: handoff)
- **Path**: `N07_admin/orchestration/handoff_admin.md`
- **Builder**: `archetypes/builders/handoff-builder/` (13 ISOs)
- **Conteúdo**: Template de handoff real com campos obrigatórios, exemplos concretos, regras de commit/signal.

### 8. quality_gate_admin.md (kind: quality_gate)
- **Path**: `N07_admin/feedback/quality_gate_admin.md`
- **Builder**: `archetypes/builders/quality-gate-builder/` (13 ISOs)
- **Conteúdo**: Gates de validação para orchestration: signal received, quality >= 8.0, doctor pass, compile success, git committed.

### 9. agent_card_admin.md (kind: agent_card)
- **Path**: `N07_admin/architecture/agent_card_admin.md`
- **Builder**: `archetypes/builders/agent-card-builder/` (13 ISOs)
- **Conteúdo**: Deployment spec do N07 — runtime (pi + opus xhigh), boot command, env vars, capabilities, endpoints.
- **Depende de**: #1 (agent), #2 (system_prompt)

### 10. signal_admin.md (kind: signal)
- **Path**: `N07_admin/orchestration/signal_admin.md`
- **Builder**: `archetypes/builders/signal-builder/` (13 ISOs)
- **Conteúdo**: O arquivo EXISTE mas sem campo quality: no frontmatter. Completar frontmatter (quality: null, author, domain, tags, tldr, density_score). Enriquecer corpo com exemplos reais de signals do bootstrap.

## REGRAS DE EXECUÇÃO

1. Para CADA artefato, leia os 13 ISOs do builder correspondente ANTES de produzir
2. Siga 8F pipeline: F1 CONSTRAIN → F2 BECOME → F3 INJECT → F4 REASON → F5 CALL → F6 PRODUCE → F7 GOVERN → F8 COLLABORATE
3. Mostre o trace 8F para CADA artefato produzido
4. quality: null em todos (NUNCA self-score)
5. Compile cada artefato após salvar: `python _tools/cex_compile.py PATH`
6. Commit incremental a cada 2-3 artefatos:
   ```
   git add -A && git commit -m "[N03] rebuild N07 artefatos batch X/4"
   ```
7. Se um artefato ficar abaixo do padrão, refaça antes de prosseguir

## COMMIT FINAL
```bash
git add -A && git commit -m "[N03] rebuild N07 admin - 10 artefatos quality 9.0+"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0, 'bootstrap_f1')"
```

## VALIDAÇÃO FINAL
```bash
python _tools/cex_doctor.py
grep -r "^quality: null" N07_admin/ --include="*.md" | grep -v mission_bootstrap
```
Expect: 0 null restantes (exceto mission_bootstrap que é quality: 9.0 já).
