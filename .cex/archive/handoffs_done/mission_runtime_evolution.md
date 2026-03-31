# Mission: Runtime Evolution - LLM Memory Retrieval + Hook Lifecycle + Fork Execution
**Prioridade**: ALTA | **Estimativa**: 8-10h (3 waves) | **Nuclei**: N03
**REGRA: Commit e signal ANTES de qualquer pausa.**
**DEPENDE DE**: mission_schema_evolution.md (campos devem existir antes do runtime)

---

## OBJETIVO

Transformar os campos universais criados no Schema Evolution em RUNTIME EXECUTAVEL.
Schema Evolution adicionou effort, hooks, memory_scope, disallowed_tools, fork_context
ao frontmatter de 104 builders. Este spec FAZ esses campos funcionarem.

Hoje: campos existem no frontmatter mas sao ignorados pelo Motor 8F e Crew Runner.
Depois: Motor 8F le effort/hooks/permissions, Crew Runner faz LLM retrieval de memoria,
        fork execution funciona, tool deny-list eh enforced.

Analogia: Schema Evolution = adicionar colunas na tabela. Runtime Evolution = queries que usam.

---

## O QUE CRIAR

### PHASE 1: LLM-Powered Memory Retrieval (3h)

O gap mais critico. Claude Code usa Sonnet como seletor de memorias relevantes.
CEX hoje: keyword match no index.db (~50% accuracy).
CEX depois: LLM seleciona top-5 memorias mais relevantes (~90% accuracy).

#### 1A: Memory Scanner
**Atualizar**: _tools/cex_memory.py (338 ln)

Adicionar funcao scan_builder_memories(builder_id) -> list[MemoryHeader]:
1. Ler bld_memory_{builder}.md
2. Parsear cada observacao: type, observation, confidence, outcome, date
3. Filtrar confidence >= 0.3 (abaixo = noise)
4. Retornar lista de headers (path, observation_preview, type, confidence, date)

Adicionar funcao scan_all_memories() -> list[MemoryHeader]:
1. Iterar todos 104 bld_memory files
2. Retornar merged list ordenada por confidence DESC

#### 1B: LLM Memory Selector
**Novo**: _tools/cex_memory_select.py

Funcao select_relevant_memories(query, memories, model=sonnet, top_k=5):
1. Receber query do usuario + lista de memory headers
2. Construir prompt de selecao (similar ao CC SELECT_MEMORIES_SYSTEM_PROMPT):
   - Lista memorias com filename, type, observation_preview, confidence
   - Pede ao LLM: selecione ate 5 memorias CLARAMENTE uteis para esta query
   - Regras: se nao tem certeza, NAO inclua. Retorne lista vazia se nenhuma aplica.
3. Chamar LLM (sonnet via API ou subprocess)
4. Parsear resposta: lista de paths selecionados
5. Ler conteudo completo das memorias selecionadas
6. Retornar lista de {path, content, type, confidence}

Fallback: se LLM nao disponivel, usar keyword match (degradacao graceful).
Cache: resultado cacheado por (query_hash, builder_id) por 5 minutos.

#### 1C: Integrate no Motor 8F
**Atualizar**: _tools/cex_8f_motor.py (1021 ln)

Na funcao fan_out (ou equivalente que carrega builder context):
1. Ler bld_memory do builder selecionado
2. Chamar select_relevant_memories(user_query, builder_memories)
3. Injetar resultado no prompt do builder como secao:

    ## Builder Memory (top-5 relevant from N observations)
    1. [type=feedback, conf=0.90] Separate persona from capabilities (SUCCESS)
    2. [type=project, conf=0.85] Agents with 3+ tools need guidance (SUCCESS)
    3. [type=reference, conf=0.72] ISO files > 4KB overflow small models (PARTIAL)

4. Impacto: ~300-500 tokens extras por builder. Negligivel em 1M context.

#### 1D: Integrate no Crew Runner
**Atualizar**: _tools/cex_crew_runner.py (665 ln)

Na funcao compose_prompt (ou equivalente):
1. Para CADA builder na crew: carregar top-5 memorias relevantes
2. Injetar no contexto individual do builder (nao no contexto geral da crew)
3. Builder A ve memorias de A, builder B ve memorias de B

Commit: runtime-evo: LLM-powered memory retrieval in Motor 8F + Crew Runner

---

### PHASE 2: Hook Lifecycle + Effort + Permissions (3h)

#### 2A: Effort-Aware Dispatch
**Atualizar**: _tools/cex_8f_motor.py

Na selecao de builder:
1. Ler bld_config.effort do builder selecionado
2. Mapear para modelo:
   low -> haiku | medium -> sonnet | high -> opus | max -> opus + extended thinking
3. Se crew_runner override existe: usar override (crew pode forcar effort)
4. Passar modelo selecionado para a chamada do LLM

Impacto de custo:
- ~89 builders em medium (sonnet): custo base
- ~10 builders em high (opus): 4x custo por builder
- ~3 builders em low (haiku): 0.05x custo
- Economia estimada: 30-40% vs usar opus para tudo

#### 2B: Tool Deny-List Enforcement
**Atualizar**: _tools/cex_8f_motor.py + _tools/cex_crew_runner.py

Ao carregar builder:
1. Ler bld_config.disallowed_tools
2. Ler bld_tools ## Tool Permissions DENIED
3. Merge: deny_set = config.disallowed + tools.denied
4. ANTES de qualquer tool call: verificar tool_name not in deny_set
5. Se tool bloqueada: retornar erro claro, NAO executar silenciosamente

Enforcement point: function que wrapa tool execution no Motor 8F.

#### 2C: Hook Lifecycle
**Atualizar**: _tools/cex_hooks.py (317 ln)

Adicionar 4 novos hook types (alem de pre-save/post-save existentes):

    pre_build(builder_id, input_data) -> {proceed: bool, modified_input}
    post_build(builder_id, output_data) -> {accept: bool, modified_output}
    on_error(builder_id, error) -> {retry: bool, fallback_builder}
    on_quality_fail(builder_id, score, gates_failed) -> {retry: bool, feedback}

Cada hook eh opcional (null = skip). Referencia funcoes Python em cex_hooks.py.

Hooks built-in disponiveis:
- validate_inputs: verifica frontmatter obrigatorio
- compile_and_index: compila artifact + rebuild index
- log_quality_failure: registra falha em .cex/learning_records/
- retry_with_feedback: re-executa builder com feedback do quality gate

**Atualizar**: _tools/cex_8f_motor.py
Na execucao de builder:
1. Ler bld_config.hooks
2. Se pre_build != null: executar antes do builder
3. Se post_build != null: executar apos builder
4. Se on_error != null: executar em caso de excecao
5. Se on_quality_fail != null: executar quando quality gate < 7.0

#### 2D: Permission Scope Enforcement
**Atualizar**: _tools/cex_8f_motor.py

Ao resolver paths para builder:
1. Ler bld_config.permission_scope
2. Filtrar paths acessiveis:
   nucleus: apenas N0X/ do builder
   pillar: qualquer N0X/ no mesmo pillar
   global: qualquer path
   restricted: apenas archetypes/builders/{builder}/
3. Se builder tenta acessar path fora do scope: bloquear + log warning

Commit: runtime-evo: effort dispatch + tool deny + hooks + permission scope

---

### PHASE 3: Fork Execution + Dynamic Memory Update + Tests (2-3h)

#### 3A: Fork Execution Context
**Atualizar**: _tools/cex_crew_runner.py

Quando builder tem fork_context: fork:
1. Em vez de executar inline na crew, criar sub-processo isolado
2. Sub-processo herda: builder ISOs + memoria selecionada + query context
3. Sub-processo NAO herda: context de outros builders na crew
4. Resultado retorna via file (output_file pattern do CC)
5. Crew runner espera resultado, injeta no proximo step

Beneficio: pesquisa paralela sem poluir context de builders subsequentes.
Custo: zero extra (reutiliza prompt cache se mesmo modelo).

Quando fork_context: inline (default):
- Builder expande no contexto atual (comportamento atual, sem mudanca)

Quando fork_context: null:
- Runtime decide: se task.complexity > 70%, usar fork. Senao, inline.

#### 3B: Dynamic Memory Update (de mission_builder_autodiscovery Track B)
**Novo/Atualizar**: _tools/cex_memory_update.py

Chamado APOS execucao de builder:

    python _tools/cex_memory_update.py \
      --builder agent-builder \
      --type feedback \
      --observation "Agents with 3+ tools need guidance" \
      --pattern "Add tool-selection criteria when tools > 3" \
      --evidence "5 builds: 90pct with vs 55pct without" \
      --confidence 0.8 \
      --outcome SUCCESS

O que faz:
1. Le bld_memory existente
2. Aplica decay em observacoes antigas (por tipo: feedback=0, project=0.05, etc)
3. Remove confidence < 0.1 (auto-prune)
4. Se total > 20: remove menor confidence
5. Appenda nova observacao com timestamp + session_id + type
6. Atualiza frontmatter: observation_count, last_updated, avg_confidence

Integration: Motor 8F chama cex_memory_update automaticamente apos quality gate.

#### 3C: Max Turns Enforcement
**Atualizar**: _tools/cex_8f_motor.py

Adicionar contador de turns por builder execution:
1. Ler bld_config.max_turns
2. Incrementar contador a cada turn agentivo
3. Se turns >= max_turns: parar, retornar resultado parcial + warning
4. Log: {builder, turns_used, max_turns, completed: bool}

#### 3D: Smoke Tests
**Novo**: _tools/tests/test_runtime_evolution.py

10 tests:
1. Memory scanner retorna headers corretos
2. LLM selector retorna top-5 (ou fallback keyword)
3. Memory injection no Motor 8F funciona
4. Effort maps to correct model
5. Tool deny-list blocks denied tool
6. Hook pre_build executa antes
7. Hook on_quality_fail triggers on low score
8. Permission scope blocks out-of-scope path
9. Fork execution produces output_file
10. Memory update appends + decays + prunes

Criterio: 10/10 passam.
Commit: runtime-evo: fork + memory update + max turns + tests

---

## PLANO DE EXECUCAO

3 waves sequenciais.

| Wave | Phase | Toca | Estimativa |
|------|-------|------|------------|
| 1 | LLM Memory (1A-1D) | cex_memory.py + cex_memory_select.py + cex_8f_motor.py + cex_crew_runner.py | 3h |
| 2 | Hooks+Effort+Perms (2A-2D) | cex_8f_motor.py + cex_hooks.py + cex_crew_runner.py | 3h |
| 3 | Fork+Update+Tests (3A-3D) | cex_crew_runner.py + cex_memory_update.py + tests | 2-3h |

### Dispatch

    # Sequencial (8-10h)
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_runtime_evolution.md. Execute Phases 1-3 em sequencia. Commit cada fase. Signal ao final." -interactive

---

## CRITERIOS DE ACEITE

| # | Criterio | Validacao |
|---|----------|----------|
| 1 | Memory scanner funciona | scan_builder_memories retorna headers |
| 2 | LLM selector funciona | top-5 relevantes para query |
| 3 | Memory injetada no prompt | Builder context inclui ## Builder Memory |
| 4 | Effort maps to model | low->haiku, medium->sonnet, high->opus |
| 5 | Deny-list enforced | Tool bloqueada retorna erro |
| 6 | Hooks executam | pre_build e post_build chamados |
| 7 | Permission scope enforced | Out-of-scope path bloqueado |
| 8 | Fork execution funciona | output_file produzido |
| 9 | Memory update funciona | Append + decay + prune |
| 10 | Max turns enforced | Para apos N turns |
| 11 | 10/10 tests passam | test_runtime_evolution.py |
| 12 | Fallback funciona | Sem LLM -> keyword match |

---

## ANTI-PATTERNS

- NAO chamar LLM selector para CADA turn (cache 5min, 1x por builder load)
- NAO usar opus para memory selection (sonnet suficiente, 4x mais barato)
- NAO bloquear tools silenciosamente (sempre retornar erro explicito)
- NAO injetar TODAS memorias (max 5, threshold >= 0.3)
- NAO fazer fork de builders inline-only (respeitar fork_context)
- NAO rodar hooks sync se forem lentos (async quando > 2s)
- NAO alterar schemas (esse spec usa os campos, nao cria)

---

## ARTEFATOS

### Input (de Schema Evolution)
| Artefato | Campos Usados |
|----------|---------------|
| bld_memory frontmatter | memory_scope, observation_types |
| bld_config frontmatter | effort, max_turns, disallowed_tools, hooks, permission_scope, fork_context |
| bld_tools body | ## Tool Permissions DENIED |

### Output
| # | Artefato | Phase | Tipo |
|---|----------|-------|------|
| 1 | _tools/cex_memory.py (update) | 1A | Update |
| 2 | _tools/cex_memory_select.py | 1B | Novo |
| 3 | _tools/cex_8f_motor.py (update) | 1C+2A-D+3C | Update |
| 4 | _tools/cex_crew_runner.py (update) | 1D+3A | Update |
| 5 | _tools/cex_hooks.py (update) | 2C | Update |
| 6 | _tools/cex_memory_update.py | 3B | Novo |
| 7 | _tools/tests/test_runtime_evolution.py | 3D | Novo |

Total: 7 artefatos (2 novos + 4 updates + 1 test)

---

*Runtime Evolution v1.0 -- Executable Universal Patterns*
*Depende de: mission_schema_evolution.md*
*Absorve: mission_builder_autodiscovery Tracks B1-B3*
*Fonte: Claude Code memdir/findRelevantMemories.ts + utils/effort.ts*
