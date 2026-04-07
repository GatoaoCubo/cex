# Mission: Schema Evolution - Universal Agent Patterns for CEX
**Prioridade**: CRITICA | **Estimativa**: 6-8h (3 waves) | **Nuclei**: N03 + N04
**REGRA: Commit e signal ANTES de qualquer pausa.**

---

## OBJETIVO

Evoluir os schemas fundamentais do CEX (bld_manifest, bld_memory, bld_config, bld_tools)
para incorporar 8 patterns universais descobertos na analise do source code do Claude Code
(1,902 files, 34MB TypeScript). Patterns provider-agnostic: Claude, GPT, Gemini, Llama.

Hoje: CEX tem profundidade absurda (13 ISOs, 212 crews, 99 kinds) mas ZERO patterns universais de runtime no schema.
Depois: Cada builder NATIVO carrega effort, permissions, hooks, memory taxonomy, scopes, discovery fields.

**NOTA**: Absorve mission_builder_autodiscovery.md Track A1 (hydrate frontmatter).
Autodiscovery spec continua valido para Tracks A2-A4, B1-B3, C1-C2.

---

## FONTE: Claude Code Agent Definition Schema

Extraido de tools/AgentTool/loadAgentsDir.ts (producao):

| CC Field | Type | CEX Equivalent | Status |
|----------|------|----------------|--------|
| agentType | string | bld_manifest.id | OK |
| whenToUse | string | ## Routing triggers | PARTIAL (body only) |
| tools | string[] | bld_tools | OK |
| disallowedTools | string[] | NADA | **GAP** |
| hooks | HooksSettings | NADA | **GAP** |
| model | string | bld_config agent_group | PARTIAL |
| effort | low/med/high/max | NADA | **GAP** |
| permissionMode | string | nucleus-level | PARTIAL |
| maxTurns | number | NADA | **GAP** |
| memory.scope | user/project/local | single scope | **GAP** |
| memory.types | 4 types | generic | **GAP** |

CC Memory types: user, feedback, project, reference
CC Memory scopes: user (~/.claude/), project (.claude/), local (.claude/local/)
CC Effort: low, medium, high, max

---

## MAPEAMENTO: 8 PATTERNS UNIVERSAIS

| # | Pattern | CEX Atual | CEX Apos | Prio |
|---|---------|-----------|----------|------|
| 1 | Discovery fields (keywords, triggers, geo_description) | Body-only 0/103 | Frontmatter todo manifest | P0 |
| 2 | Memory taxonomy (4 tipos: user/feedback/project/reference) | Generico 1 tipo | 4 tipos no bld_memory | P0 |
| 3 | Memory scoping (3 escopos: user/project/local) | Escopo unico | 3 escopos no bld_config | P0 |
| 4 | Tool deny-list (disallowedTools) | Nenhum | Campo no bld_config | P1 |
| 5 | Effort/thinking (low/medium/high/max) | Fixo | Campo no bld_config | P1 |
| 6 | Hook lifecycle (pre/post/error/quality) | cex_hooks pre/post-save | Campo no bld_config | P1 |
| 7 | Max turns (budget control) | Nenhum | Campo no bld_config | P2 |
| 8 | Fork context (inline vs clone) | Nenhum | Campo no bld_config | P2 |

P0 = cria + hydrate 104 builders | P1 = cria campo + defaults | P2 = cria campo + null

---

## O QUE CRIAR

### PHASE 1: Schema Definitions (1.5h)

#### 1A: Evolve bld_manifest -- meta template
**Atualizar**: archetypes/builders/_builder-builder/bld_meta_manifest_builder.md

Adicionar ao template YAML frontmatter (apos tags):

    keywords: [keyword_1, keyword_2, ..., keyword_8]       # 4-8 termos search/routing
    triggers: ["trigger_phrase_1", "trigger_phrase_2"]       # 2-4 frases naturais
    geo_description: >                                       # 3 camadas semanticas
      L1: O que faz. L2: Como faz. L3: Quando usar.

Atualizar ## Routing: frontmatter = canonical, body = derivado.

#### 1B: Evolve bld_memory -- meta template
**Atualizar**: archetypes/builders/_builder-builder/bld_meta_memory_builder.md

Adicionar ao frontmatter:

    memory_scope: project              # user | project | local
    observation_types: [user, feedback, project, reference]

Formato universal de observacao no body:

    ### Observation N (YYYY-MM-DD)
    - type: user | feedback | project | reference
    - observation: "o que foi aprendido"
    - pattern: "regra generalizavel"
    - evidence: "dados que suportam"
    - confidence: 0.0-1.0
    - outcome: SUCCESS | PARTIAL | FAILURE
    - session: session_id
    - tags: [tag1, tag2]

Decay rules: user=0.03/dia, feedback=0.00 (NUNCA), project=0.05/dia, reference=0.01/dia

#### 1C: Evolve bld_config -- meta template
**Atualizar**: archetypes/builders/_builder-builder/bld_meta_config_builder.md

Adicionar ao frontmatter:

    effort: medium                     # low(haiku) | medium(sonnet) | high(opus) | max(opus+ultra)
    max_turns: 25                      # integer, 1-100
    disallowed_tools: []               # tools NAO permitidas
    fork_context: null                 # inline | fork | null
    hooks:
      pre_build: null
      post_build: null
      on_error: null
      on_quality_fail: null
    permission_scope: nucleus          # nucleus | pillar | global | restricted

#### 1D: Evolve bld_tools -- meta template
**Atualizar**: archetypes/builders/_builder-builder/bld_meta_tools_builder.md

Adicionar secao ## Tool Permissions com ALLOWED/DENIED/EFFECTIVE.
REGRA: DENIED > ALLOWED quando conflito.

Commit: schema-evo: evolve 4 meta-templates with 8 universal patterns

---

### PHASE 2: Hydrate 104 Builders (3-4h)

#### 2A: Create hydration script
**Novo**: _tools/cex_schema_hydrate.py

Para cada builder em archetypes/builders/*/:

**bld_manifest**: extrair keywords/triggers de ## Routing body -> frontmatter. Gerar geo_description.
**bld_memory**: adicionar memory_scope: project + observation_types: [4 tipos]. Type cada obs existente.
**bld_config**: adicionar effort/max_turns/disallowed_tools/fork_context/hooks/permission_scope.
**bld_tools**: adicionar ## Tool Permissions section.

Preservar TUDO existente intacto em TODOS os files.

Flags: --dry-run | --apply | --builders [list] | --iso type | --stats

**Overrides nao-default (15 builders)**:

| Builder | effort | disallowed_tools | fork_context | permission_scope |
|---------|--------|-----------------|--------------|-----------------|
| _builder-builder | high | [] | null | global |
| research-pipeline-builder | high | [Write, Edit] | fork | nucleus |
| system-prompt-builder | medium | [BashTool] | inline | pillar |
| output-validator-builder | low | [Write, BashTool] | inline | restricted |
| agent-builder | high | [] | null | pillar |
| knowledge-card-builder | medium | [] | fork | nucleus |
| model-card-builder | low | [] | inline | nucleus |
| benchmark-builder | high | [] | fork | nucleus |
| content-monetization-builder | high | [] | null | nucleus |
| supabase-data-layer-builder | high | [] | null | nucleus |
| social-publisher-builder | medium | [] | null | nucleus |
| workflow-builder | high | [] | null | pillar |
| chain-builder | medium | [] | inline | pillar |
| brain-index-builder | high | [] | fork | global |
| bugloop-builder | medium | [] | fork | nucleus |

Restantes ~89: defaults (medium, 25, [], null, {nulls}, nucleus).

Validacao pos-hydrate:
- 103/103 manifests com keywords (>= 3) + triggers (>= 2) + geo_description (>= 50 chars)
- 104/104 memories com memory_scope + observation_types
- 103/103 configs com effort + max_turns + disallowed_tools + permission_scope
- 103/103 tools com ## Tool Permissions

Commit: schema-evo: create cex_schema_hydrate.py

#### 2B: Execute hydration

    python _tools/cex_schema_hydrate.py --dry-run --stats
    python _tools/cex_schema_hydrate.py --apply --stats

Commits:
- schema-evo: hydrate 103 bld_manifest with discovery fields
- schema-evo: hydrate 104 bld_memory with taxonomy + scopes
- schema-evo: hydrate 103 bld_config with runtime fields
- schema-evo: hydrate 103 bld_tools with permission sections

#### 2C: Update bld_norms.md
Adicionar 11 novas regras (items 13-23):

| # | Regra |
|---|-------|
| 13 | bld_manifest keywords: 4-8 in frontmatter |
| 14 | bld_manifest triggers: 2-4 phrases |
| 15 | bld_manifest geo_description: >= 50 chars, 3 layers |
| 16 | bld_memory memory_scope: user/project/local |
| 17 | bld_memory observation_types: all 4 types |
| 18 | bld_memory observation: EACH must have type: field |
| 19 | bld_config effort: low/medium/high/max |
| 20 | bld_config max_turns: int 1-100 |
| 21 | bld_config disallowed_tools: list (empty ok) |
| 22 | bld_config permission_scope: nucleus/pillar/global/restricted |
| 23 | bld_tools Tool Permissions: section required |

Commit: schema-evo: update bld_norms with 11 universal rules

---

### PHASE 3: Validate + Reindex (1h)

#### 3A: Validation script
**Novo**: _tools/tests/test_schema_evolution.py

15 tests:
1. 103 manifests have keywords (list, len >= 3)
2. 103 manifests have triggers (list, len >= 2)
3. 103 manifests have geo_description (str, len >= 50)
4. 104 memories have memory_scope (enum)
5. 104 memories have observation_types (list, len == 4)
6. 103 configs have effort (enum)
7. 103 configs have max_turns (int, range)
8. 103 configs have disallowed_tools (list)
9. 103 configs have permission_scope (enum)
10. 103 tools have ## Tool Permissions
11. No builder lost existing fields (regression)
12. YAML parseable in all modified files
13. 15 specific builders have non-default values
14. observation_types always == [user, feedback, project, reference]
15. geo_description has 3 layers

Criterio: 15/15 passam.
Commit: schema-evo: add test_schema_evolution.py

#### 3B: Rebuild index
    python _tools/cex_index.py --rebuild
Commit: schema-evo: rebuild index.db

#### 3C: Update _builder-builder README
Adicionar secao Universal Schema Fields v1.0.
Commit: schema-evo: update _builder-builder README

---

## PLANO DE EXECUCAO

3 waves sequenciais (dependencias).

| Wave | Phase | Toca | Estimativa |
|------|-------|------|------------|
| 1 | Schema Definitions (1) | _builder-builder/bld_meta_*.md (4 files) | 1.5h |
| 2 | Hydration (2) | cex_schema_hydrate.py + 104 builders x 4 ISOs | 3-4h |
| 3 | Validate + Reindex (3) | tests/ + index.db + README | 1h |

### Dispatch

    # Sequencial (6-8h, seguro)
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_schema_evolution.md. Execute Phase 1, 2, 3 em sequencia. Commit cada fase. Signal ao final." -interactive

    # 2 spawns
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_schema_evolution.md. SOMENTE Phase 1. Commit. Signal." -interactive
    # (apos Wave 1):
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_schema_evolution.md. Phase 2 e 3. Commit. Signal." -interactive

---

## INTERACAO COM OUTROS SPECS

| Spec | Relacao |
|------|---------|
| mission_builder_autodiscovery.md | PARCIALMENTE ABSORVIDO (Track A1). A2-A4, B1-B3, C1-C2 continuam |
| mission_content_monetization_v2.md | INDEPENDENTE |
| mission_runtime_evolution.md (Spec 2) | DEPENDE DESTE |
| mission_validation_registry.md (Spec 3) | DEPENDE DESTE |

---

## CRITERIOS DE ACEITE

| # | Criterio | Validacao |
|---|----------|----------|
| 1 | 4 meta-templates atualizados | Diff mostra novos campos |
| 2 | cex_schema_hydrate.py funcional | --dry-run + --apply |
| 3 | 103 manifests com discovery fields | keywords + triggers + geo_description |
| 4 | 104 memories com taxonomy | memory_scope + observation_types |
| 5 | 103 configs com runtime fields | effort + max_turns + disallowed_tools + hooks + permission_scope |
| 6 | 103 tools com permissions | ## Tool Permissions section |
| 7 | 15 builders non-default | Tabela de overrides respeitada |
| 8 | bld_norms atualizado | 11 novas regras (13-23) |
| 9 | 15/15 tests passam | test_schema_evolution.py |
| 10 | index.db rebuilt | keywords indexados |
| 11 | Zero regressao | Nenhum campo perdido |
| 12 | YAML parseable | Todos files modificados |

---

## ANTI-PATTERNS

- NAO alterar body dos ISOs (apenas frontmatter e novas secoes)
- NAO inventar keywords -- extrair do ## Routing existente
- NAO remover campos existentes
- NAO usar valores hardcoded de empresa
- NAO criar novos ISOs por builder
- NAO rodar hydrate sem --dry-run
- NAO confundir com runtime evolution (NAO muda cex_8f_motor.py)
- NAO alterar bld_collaboration, bld_architecture, bld_instruction
- NAO forcar observation_types != [user, feedback, project, reference]
- NAO setar effort: max como default

---

## ARTEFATOS

### Input
| Artefato | Path |
|----------|------|
| Meta-templates (4) | archetypes/builders/_builder-builder/bld_meta_*_builder.md |
| Manifests (103) | archetypes/builders/*/bld_manifest_*.md |
| Memories (104) | archetypes/builders/*/bld_memory_*.md |
| Configs (103) | archetypes/builders/*/bld_config_*.md |
| Tools (103) | archetypes/builders/*/bld_tools_*.md |
| Norms | archetypes/builders/bld_norms.md |
| Indexer | _tools/cex_index.py |
| Hooks ref | _tools/cex_hooks.py |
| Memory ref | _tools/cex_memory.py |
| Shared | _tools/cex_shared.py |

### Output
| # | Artefato | Phase | Tipo |
|---|----------|-------|------|
| 1 | 4 meta-templates (update) | 1 | Update |
| 2 | _tools/cex_schema_hydrate.py | 2A | Novo |
| 3 | ~416 ISO files (batch update) | 2B | Batch |
| 4 | bld_norms.md (update) | 2C | Update |
| 5 | _tools/tests/test_schema_evolution.py | 3A | Novo |
| 6 | .cex/index.db (rebuild) | 3B | Rebuild |
| 7 | _builder-builder/README.md (update) | 3C | Update |

Total: 7 artefatos logicos (1 script + 1 test + ~416 batch + 3 updates + 1 rebuild)

---

*Schema Evolution v1.0 -- Universal Agent Patterns*
*Absorve: mission_builder_autodiscovery Track A1*
*Pre-requisito para: mission_runtime_evolution + mission_validation_registry*
*Fonte: Claude Code source (1,902 files, BaseAgentDefinition)*
