# Mission: Validation Registry - New Kinds + Smoke Tests + Recompile
**Prioridade**: MEDIA | **Estimativa**: 4-5h (2 waves) | **Nuclei**: N03 + N04
**REGRA: Commit e signal ANTES de qualquer pausa.**
**DEPENDE DE**: mission_schema_evolution.md + mission_runtime_evolution.md

---

## OBJETIVO

Fechar o ciclo: schemas criados (Spec 1), runtime ativado (Spec 2), agora:
1. Registrar novos kinds na TAXONOMY (memory_scope, hook_config, effort_profile)
2. Criar builders para os novos kinds
3. End-to-end smoke tests cobrindo o ciclo completo
4. Recompilar todos os artefatos afetados
5. Validar integridade do sistema pos-evolucao

Depois deste spec: CEX tem schemas universais + runtime ativo + kinds registrados + testes.

---

## O QUE CRIAR

### PHASE 1: Kind Registration + Builders (2.5h)

#### 1A: Register 3 new kinds in TAXONOMY_LAYERS.yaml
**Atualizar**: archetypes/TAXONOMY_LAYERS.yaml

Adicionar na layer runtime:

    - memory_scope        # P10 -- configuracao de escopo de memoria por builder
    - effort_profile      # P09 -- perfil de esforco/thinking por builder
    - hook_config         # P04 -- configuracao de hooks lifecycle por builder

Adicionar na secao overlaps:

    - pair: [memory_scope, learning_record]
      boundary: memory_scope = CONFIG de como memoria funciona; learning_record = CONTEUDO da memoria
    - pair: [effort_profile, runtime_rule]
      boundary: effort_profile = QUAL modelo/thinking usar; runtime_rule = QUANDO/COMO executar
    - pair: [hook_config, hook]
      boundary: hook_config = DECLARACAO de quais hooks; hook = IMPLEMENTACAO do hook

Atualizar count na layer runtime: +3

#### 1B: Create memory_scope builder (skeleton)
**Novo**: archetypes/builders/memory-scope-builder/

13 ISOs (skeleton pattern -- ~30KB total):
- bld_manifest_memory-scope.md
- bld_instruction_memory-scope.md
- bld_config_memory-scope.md
- bld_memory_memory-scope.md
- bld_tools_memory-scope.md
- bld_collaboration_memory-scope.md
- bld_architecture_memory-scope.md
- bld_schema_memory-scope.md
- bld_output_template_memory-scope.md
- bld_examples_memory-scope.md
- bld_quality_gate_memory-scope.md
- bld_knowledge_card_memory-scope.md
- bld_system_prompt_memory-scope.md

Domain: memory_scope | Pillar: P10 | effort: medium
Capability: produzir memory_scope configs para builders
Keywords: [memory, scope, user, project, local, observation, type, decay]

NOTA: skeleton builders (chunk-strategy, constraint-spec, etc) tem 13 files mas < 30KB.
Este builder segue o mesmo pattern.

#### 1C: Create effort_profile builder (skeleton)
**Novo**: archetypes/builders/effort-profile-builder/

13 ISOs (skeleton).
Domain: effort_profile | Pillar: P09 | effort: low
Capability: produzir effort profiles (model + thinking level) para builders
Keywords: [effort, thinking, model, haiku, sonnet, opus, low, medium, high, max]

#### 1D: Create hook_config builder (skeleton)
**Novo**: archetypes/builders/hook-config-builder/

13 ISOs (skeleton).
Domain: hook_config | Pillar: P04 | effort: medium
Capability: produzir hook configs (pre/post/error/quality) para builders
Keywords: [hook, lifecycle, pre-build, post-build, on-error, quality-fail, event]

#### 1E: Register kinds in cex_kind_register.py
**Atualizar**: _tools/cex_kind_register.py (181 ln)

Adicionar 3 kinds: memory_scope, effort_profile, hook_config
Com seus pillar assignments e schema references.

Commit: validation: register 3 new kinds + create 3 skeleton builders

---

### PHASE 2: End-to-End Tests + Recompile + Integrity (2h)

#### 2A: End-to-End Smoke Test
**Novo**: _tools/tests/test_e2e_evolution.py

Testa o CICLO COMPLETO:

Test 1: Discovery -> Builder
  Input: "monetizar curso hotmart"
  Assert: cex_query retorna content-monetization-builder com score >= 0.7
  Assert: keywords, triggers, capability_summary presentes no manifest

Test 2: Builder -> Memory Load
  Input: carregar content-monetization-builder
  Assert: bld_memory tem memory_scope + observation_types
  Assert: top-5 memorias selecionadas (ou vazio se nenhuma relevante)

Test 3: Builder -> Effort -> Model
  Input: builder com effort: high
  Assert: modelo selecionado == opus
  Input: builder com effort: low
  Assert: modelo selecionado == haiku

Test 4: Builder -> Tool Deny
  Input: research-pipeline-builder (disallowed: [Write, Edit])
  Assert: Write tool bloqueada com erro explicito

Test 5: Builder -> Hook Lifecycle
  Input: builder com hooks.pre_build == validate_inputs
  Assert: validate_inputs executado antes do builder

Test 6: Builder -> Quality -> Memory Update
  Input: builder executa, quality score = 8.5
  Assert: nova observacao appendada em bld_memory
  Assert: observacoes antigas com decay aplicado

Test 7: New Kinds Registered
  Assert: memory_scope in TAXONOMY_LAYERS.yaml
  Assert: effort_profile in TAXONOMY_LAYERS.yaml
  Assert: hook_config in TAXONOMY_LAYERS.yaml
  Assert: 3 skeleton builders existem com 13 files cada

Test 8: Schema Integrity (regression)
  Assert: 103 manifests com keywords (Schema Evo check)
  Assert: 104 memories com observation_types
  Assert: 103 configs com effort + hooks
  Assert: ZERO campos perdidos vs baseline

Test 9: Index Integrity
  Assert: index.db tem 3 new kinds indexed
  Assert: manifests com keywords_json populado
  Assert: queries retornam resultados para 10 test phrases

Test 10: Autodiscovery Pipeline
  Input: cex_query "criar agente de vendas"
  Assert: retorna agent-builder, score >= 0.6
  Assert: retorna crew recomendada
  Input: cex_intent recebe query desconhecida
  Assert: fallback para cex_query funciona

Criterio: 10/10 passam.
Commit: validation: e2e test suite (10 tests)

#### 2B: Recompile All

    python _tools/cex_compile.py --all
    python _tools/cex_index.py --rebuild

Verificar:
- Compiled YAMLs refletem novos campos
- Index.db tem todos os kinds + keywords
- Zero erros de compilacao

Commit: validation: recompile all + rebuild index

#### 2C: Integrity Report
**Novo**: _tools/tests/report_evolution_integrity.py

Gera relatorio:

    === CEX Evolution Integrity Report ===
    Schema Evolution: 12/12 criterios OK
    Runtime Evolution: 12/12 criterios OK
    Kind Registry: 3 new kinds registered
    Skeleton Builders: 3 created (39 files)
    E2E Tests: 10/10 passing
    Total builders: 107 (104 + 3 new)
    Total kinds: 102 (99 + 3 new)
    Memory fields: 104/104 hydrated
    Config fields: 106/106 hydrated (103 + 3 new)
    Index entries: [N] files indexed
    Compilation: 0 errors

Commit: validation: integrity report generator

---

## PLANO DE EXECUCAO

2 waves sequenciais.

| Wave | Phase | Toca | Estimativa |
|------|-------|------|------------|
| 1 | Kind Registration (1A-1E) | TAXONOMY + 3 builders + kind_register | 2.5h |
| 2 | E2E Tests + Recompile (2A-2C) | tests + compile + index + report | 2h |

### Dispatch

    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_validation_registry.md. Execute Phase 1 e 2. Commit cada fase. Signal ao final." -interactive

---

## CRITERIOS DE ACEITE

| # | Criterio | Validacao |
|---|----------|----------|
| 1 | 3 kinds em TAXONOMY | memory_scope + effort_profile + hook_config |
| 2 | 3 skeleton builders | 13 files cada, < 30KB cada |
| 3 | kind_register.py atualizado | 3 kinds registrados |
| 4 | 10/10 E2E tests passam | test_e2e_evolution.py |
| 5 | Compile sem erros | cex_compile.py --all |
| 6 | Index rebuilt | cex_index.py --rebuild |
| 7 | Integrity report green | report_evolution_integrity.py |
| 8 | Zero regressao | Nenhum campo/file perdido |

---

## ANTI-PATTERNS

- NAO criar builders full (>30KB) -- skeleton eh suficiente para kinds novos
- NAO alterar builders existentes (apenas novos)
- NAO pular E2E tests (eles cobrem o ciclo completo)
- NAO compilar sem rebuild de index
- NAO confundir hook_config (declaracao) com hook (implementacao)

---

## ARTEFATOS

### Output
| # | Artefato | Phase | Tipo |
|---|----------|-------|------|
| 1 | TAXONOMY_LAYERS.yaml (update) | 1A | Update |
| 2 | memory-scope-builder/ (13 files) | 1B | Novo |
| 3 | effort-profile-builder/ (13 files) | 1C | Novo |
| 4 | hook-config-builder/ (13 files) | 1D | Novo |
| 5 | cex_kind_register.py (update) | 1E | Update |
| 6 | test_e2e_evolution.py | 2A | Novo |
| 7 | .cex/index.db (rebuild) | 2B | Rebuild |
| 8 | report_evolution_integrity.py | 2C | Novo |

Total: 8 artefatos (39 skeleton files + 2 tests + 2 updates + 1 rebuild)

---

*Validation Registry v1.0 -- Close the Evolution Loop*
*Depende de: mission_schema_evolution + mission_runtime_evolution*
*Finaliza: Universal Agent Patterns trilogy*
*Resultado: CEX com 107 builders, 102 kinds, 8 universal patterns, runtime ativo*
