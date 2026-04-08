# Mission: Builder Auto-Discovery + Dynamic Memory (GEO Interno)
**Prioridade**: Alta | **Estimativa**: 4-5h | **Nuclei**: N03 (engineering)
**REGRA: Commit e signal ANTES de qualquer pausa.**

---

## OBJETIVO

Ativar duas capacidades latentes que transformam CEX de sistema navegado por humano
em sistema que se navega sozinho:

1. **Auto-Discovery**: Agente recebe tarefa -> consulta index.db -> acha builder + crew corretos
2. **Dynamic Memory**: Builders acumulam conhecimento sessao-sobre-sessao via bld_memory

Hoje: humano escolhe builder, builder esquece tudo apos execucao.
Depois: agente descobre builder sozinho, builder lembra e melhora a cada uso.

---

## CONTEXTO: O QUE JA EXISTE (Auditoria Completa)

### Sistema de Crews (CEX ja tem -- superando IndyDevDan)

| Componente | Quantidade | Onde Vive |
|------------|-----------|-----------|
| Nuclei (equivalente a "Teams" do Dan) | 7 | N01-N07 |
| Builders (equivalente a "Workers" do Dan) | 102 | archetypes/builders/*/  |
| Crew compositions nomeadas | 212 | bld_collaboration_*.md -> ### Crew: |
| Collaboration files com handoff protocol | 101 | bld_collaboration_*.md |
| Pipeline functions (8F) | 8 | CONSTRAIN>BECOME>INJECT>REASON>CALL>PRODUCE>GOVERN>COLLABORATE |
| Crew Runner (DAG executor) | 1 | _tools/cex_crew_runner.py |
| Motor 8F (intent classifier + fan-out) | 1 | _tools/cex_8f_motor.py |
| OBJECT_TO_KINDS (kind taxonomy) | 167 keywords -> 99 kinds | cex_8f_motor.py |

**Comparacao direta:**
- Dan: 3 teams, ~10 agents, 0 crew defs, 3-step pipeline (plan>build>validate)
- CEX: 7 nuclei, 102 builders, 212 crews nomeadas, 8F pipeline, DAG executor
- CEX ja tem tudo que Dan tem, com tipagem, schemas, quality gates, e reusabilidade.

### Auto-Discovery (PARCIAL -- gap critico)

| Componente | Status | Dado Real |
|------------|--------|-----------|
| Keywords no frontmatter dos manifests | 0/102 | Campo ausente em TODOS |
| Keywords no ## Routing (body) | 94/102 | Indexador NAO le body |
| index.db populado | 3112 files | 0 manifests com keywords |
| OBJECT_TO_KINDS | 167 keywords | Apenas KIND (agent, workflow). Zero DOMAIN (hotmart, supabase) |
| cex_query.py | NAO EXISTE | Nenhuma busca por dominio |
| Dispatch rules | 18 com keywords | Roteiam para nuclei, NAO para builders |

**Gap**: 102 builders com ~800 keywords invisiveis ao index. Agentes nao encontram builders.

### Dynamic Memory (SCHEMA EXISTE -- mecanismo inativo)

| Componente | Status | Dado Real |
|------------|--------|-----------|
| bld_memory_*.md | 103 files existem | Media 3.3KB, 339KB total |
| Campos no schema | observation, pattern, evidence, confidence, decay_rate, impact_score | Completo |
| Observacoes por file | 1 (criado uma vez, nunca atualizado) | Apenas 1/103 com multiplas |
| Mecanismo de update | NAO EXISTE | Nenhum hook/script atualiza |
| Load at boot | NAO EXISTE | Motor 8F nao carrega bld_memory |
| Decay rate | Campo existe | Nunca aplicado |

**Gap**: 103 memorias congeladas. Builders nao aprendem. Exatamente o oposto do IndyDevDan,
cujo killer feature eh mental models que crescem sessao-sobre-sessao.
---

## FONTES DE ANALISE

### IndyDevDan: "One Agent Is NOT ENOUGH" (34min, YouTube)

Multi-team agent system com PI harness. 3-tier: orchestrator > leads > workers.
10 patterns extraidos, 3 relevantes para CEX:

| Pattern Dan | CEX Status | Acao |
|-------------|-----------|------|
| Dynamic mental models (grows each session) | Schema existe, inativo | **ATIVAR (Track B)** |
| Domain locking (read/write per dir) | Nuclei + pillar isolation (2D, melhor) | Nenhuma |
| Skills compartilhadas | 118 skills (mais que Dan) | Nenhuma |
| Config-driven teams (YAML) | Frontmatter YAML tipado (melhor) | Nenhuma |
| Multi-perspective query | NAO existe | Prioridade futura |
| Delegate-never-execute | Dispatch rules fazem isso | Nenhuma |
| Session conversation log | .cex/runtime/ (parcial) | Prioridade baixa |
| Cost tracking per agent | NAO existe | Prioridade baixa |
| Agent expertise (curated) | 13 ISOs/builder = 1351 files (13x Dan) | Nenhuma |
| Consensus across teams | NAO existe | Prioridade futura |

**Conclusao**: CEX vence em 14/17 dimensoes. Dan vence em 3 (dynamic memory,
multi-perspective, session log). Dynamic memory eh o unico gap de alto impacto.

### inference.sh/skills: GEO Pattern (80 SKILL.md files)

Cada SKILL.md tem frontmatter com: name + description (3 camadas semanticas) + Triggers.
Claude Code le frontmatter -> auto-ativa skill. Conceito: GEO (SEO para agentes).

CEX gap encontrado: builders tem keywords no body (## Routing) mas NAO no frontmatter.
Indexador so le frontmatter -> builders invisiveis. Fix: hydrate frontmatter (Track A).

---

## ARQUITETURA DA SOLUCAO

### Track A: Auto-Discovery (3 camadas)

| Camada | Mecanismo | Exemplo |
|--------|-----------|---------|
| L0: KIND | OBJECT_TO_KINDS (167 kws, JA EXISTE) | "cria agent" -> agent-builder |
| L1: DOMAIN | index.db keywords de builders (CRIAR) | "monetizar hotmart" -> content-monetization-builder |
| L2: SEMANTIC | capabilities + scoring (CRIAR) | "quero vender curso online" -> melhor match |

    FLUXO COMPLETO:
    Agente recebe tarefa
      -> L0: OBJECT_TO_KINDS busca KIND match
      -> Se achou: usar builder (caminho atual, funciona)
      -> Se NAO achou: L1 fallback via cex_query.py
      -> cex_query.py busca index.db (keywords + triggers + capabilities)
      -> Retorna builder + crew composition recomendada
      -> Score >= 0.5: auto-carrega 13 ISOs + bld_collaboration (crew)
      -> Score < 0.5: pede clarificacao

### Track B: Dynamic Memory (ciclo de aprendizado)

    Builder executa tarefa
      -> Resultado avaliado (bld_quality_gate)
      -> Nova observacao extraida:
         {observation, pattern, evidence, confidence, outcome}
      -> Appendada em bld_memory_{builder}.md
      -> decay_rate aplicado a observacoes antigas
         confidence_new = confidence * (1 - decay_rate) ^ dias
      -> Observacoes com confidence < 0.1 prunadas
      -> Proxima execucao: Motor 8F carrega top-5 observacoes
      -> Builder melhora progressivamente

    Vantagem CEX sobre Dan:
    - Dan: texto livre, cresce infinitamente, sem pruning
    - CEX: structured observations, decay automatico, max 20 obs, quality scored
---

## O QUE CRIAR

### TRACK A: Auto-Discovery (2-2.5h)

#### A1: Hydrate Frontmatter dos Manifests (30min)

**Novo**: _tools/cex_geo_hydrate.py

Le cada bld_manifest_*.md (102 arquivos):
1. Extrai keywords e triggers do ## Routing section (body)
2. Gera capabilities de ## Identity + ## Capabilities (3 camadas semanticas)
3. Adiciona ao frontmatter YAML: keywords, triggers, capabilities
4. Preserva todo o resto do frontmatter e body intactos
5. Valida: YAML parseable, keywords nao-vazio

Formato frontmatter resultante:

    ---
    id: social-publisher-builder
    kind: type_builder
    pillar: P04
    domain: social_publisher
    tags: [kind-builder, social-publisher]
    keywords: [social-media, auto-posting, instagram, facebook, ayrshare, scheduling]
    triggers: ["create social publisher", "auto-posting system", "social media automation"]
    capabilities: >
      Sistema de auto-posting para redes sociais. Cobre pipeline de 10 passos
      com Ayrshare/Postiz/Meta Graph API, content mix, posting-time optimization.
      Use para: automatizar postagem, calendario, publicacao multi-plataforma.
    ---

Flags: --dry-run (mostra diff, nao altera) | --apply (altera files)
Validacao: 102/102 manifests com keywords + triggers + capabilities
Commit: "geo: hydrate 102 builder manifests with keywords/triggers/capabilities"

#### A2: Enhance Indexer (30min)

**Atualizar**: _tools/cex_index.py

Mudancas:
1. Novos campos no schema: triggers_json TEXT, capabilities TEXT
2. Fallback: se frontmatter nao tem keywords, parsear ## Routing do body
3. Rebuild completo + stats

Validacao: SELECT COUNT(*) FROM files WHERE path LIKE "%manifest%" AND keywords_json != "[]" == 102
Commit: "geo: enhance cex_index.py with triggers, capabilities, body fallback"

#### A3: Query Tool (45min)

**Novo**: _tools/cex_query.py

Uso:
    python _tools/cex_query.py "monetizar curso hotmart"

    RESULTS (3 matches):
      1. content-monetization-builder  score=0.92  domain=content_monetization
         matched: [hotmart, curso, monetizar]
         crew: "Content Production" (5 builders)
         path: archetypes/builders/content-monetization-builder/
      2. workflow-builder              score=0.45  domain=workflow
      3. dispatch-rule-commercial      score=0.38  domain=commercial

Algoritmo de scoring:
    keyword IN builder.keywords:        +0.30 (match exato)
    keyword IN builder.triggers:        +0.20 (match frase)
    keyword IN builder.domain:          +0.15 (match dominio)
    keyword IN builder.capabilities: +0.10 (match semantico)
    keyword IN builder.tags:            +0.05 (match tag)
    normalizado: score / len(query_keywords)

**NOVO vs versao anterior**: tambem retorna CREW recomendada.
Busca bld_collaboration do builder top-1, extrai ### Crew: sections,
sugere a crew mais relevante baseada nos keywords da query.

Flags: --top N | --json | --threshold 0.2 | --with-crew (default ON)
Commit: "geo: create cex_query.py with scoring + crew recommendation"

#### A4: Integration no Motor 8F + Intent (30min)

**Atualizar**: _tools/cex_intent.py + _tools/cex_8f_motor.py

Quando OBJECT_TO_KINDS nao encontra match (keyword desconhecido):
1. Chamar cex_query como fallback (L1/L2)
2. Score >= 0.5: usar builder encontrado + crew sugerida
3. Score < 0.5: pedir clarificacao ao usuario
4. Log match em .cex/runtime/learning/ para feedback loop

Flag --geo no cex_intent.py para ativar (default OFF ate validacao)
Commit: "geo: integrate cex_query into intent pipeline as L1/L2 fallback"
### TRACK B: Dynamic Memory (1.5-2h)

#### B1: Memory Update Mechanism (45min)

**Novo**: _tools/cex_memory_update.py

Uso (chamado apos execucao de builder):

    python _tools/cex_memory_update.py --builder agent-builder --observation "Agents with 3+ tools need explicit tool-selection guidance" --pattern "Add tool-selection criteria when tools > 3" --evidence "5 builds: 90pct correct with guidance vs 55pct without" --confidence 0.8 --outcome SUCCESS

O que faz:
1. Le bld_memory_{builder}.md existente
2. Parseia observacoes existentes (YAML blocks no body)
3. Aplica decay_rate em observacoes antigas:
   confidence_decayed = confidence * (1 - decay_rate) ^ days_since_created
4. Remove observacoes com confidence < 0.1 (auto-prune)
5. Se total observacoes > 20: remove a de menor confidence
6. Appenda nova observacao com timestamp e session_id
7. Atualiza frontmatter: observation_count, last_updated, avg_confidence
8. Salva arquivo

Schema da observacao appendada:

    ## Observation 3 (2026-03-31)
    - observation: "Agents with 3+ tools need explicit tool-selection guidance"
    - pattern: "Add tool-selection criteria in INSTRUCTIONS when tools > 3"
    - evidence: "5 builds: 90pct correct with guidance vs 55pct without"
    - confidence: 0.8
    - outcome: SUCCESS
    - session: abc123
    - tags: [agent-design, tools, guidance]

Vantagem sobre IndyDevDan:
- Dan: texto livre, sem decay, cresce infinitamente, sem quality scoring
- CEX: structured, decay automatico, max 20 obs, pruning, scored

Commit: "memory: create cex_memory_update.py with decay + append + prune"

#### B2: Memory Load at Boot (30min)

**Atualizar**: _tools/cex_8f_motor.py e _tools/cex_crew_runner.py

Ao carregar builder (fan_out ou compose_prompt):
1. Ler bld_memory_{builder}.md
2. Filtrar observacoes com confidence >= 0.3
3. Ordenar por confidence DESC, pegar top 5
4. Injetar no contexto do builder como secao extra

Formato injetado:

    ## Builder Memory (learned from 7 previous executions)
    1. [conf=0.90] Separate persona from capabilities across files (SUCCESS)
    2. [conf=0.85] Agents with 3+ tools need tool-selection criteria (SUCCESS)
    3. [conf=0.72] ISO files > 4KB cause context overflow in small models (PARTIAL)
    4. [conf=0.68] Include fallback chain when targeting multi-provider (SUCCESS)
    5. [conf=0.55] Guardrails reduce hallucination 40pct in agent outputs (SUCCESS)

Impacto: builder carrega com ~500 tokens extras de experiencia acumulada.
Com 1M context window disponivel, isso eh negligivel em custo e enorme em valor.

Commit: "memory: load bld_memory at boot in Motor 8F + Crew Runner"

#### B3: Memory Update Skill (15min)

**Novo**: archetypes/builders/_shared/skill_memory_update.md

Instrucao compartilhada (~50 linhas) que ensina builders a:
- Refletir apos execucao sobre o que funcionou/falhou
- Registrar UMA observacao estruturada por sessao
- Focar em PATTERNS reutilizaveis, nao fatos isolados
- Nao registrar obviedades ("o schema foi seguido" NAO eh insight)
- Bons exemplos: "Splitting handler into validate+process+respond reduced errors 40pct"

Referencia: IndyDevDan mental model skill (77 linhas).
CEX versao sera mais curta pois observations sao structured, nao texto livre.

Commit: "memory: create shared skill_memory_update.md for all builders"
### TRACK C: Smoke Tests + Validacao (30min)

#### C1: Auto-Discovery Tests

**Novo**: _tools/tests/test_autodiscovery.py

10 queries -> builder correto:

| # | Query | Builder Esperado | Score Min |
|---|-------|-----------------|-----------|
| 1 | "monetizar curso hotmart" | content-monetization-builder | 0.7 |
| 2 | "pesquisa de mercado concorrentes" | research-pipeline-builder | 0.7 |
| 3 | "automatizar postagem instagram" | social-publisher-builder | 0.7 |
| 4 | "criar banco de dados supabase" | supabase-data-layer-builder | 0.7 |
| 5 | "webhook para stripe" | webhook-builder | 0.6 |
| 6 | "criar agente de vendas" | agent-builder | 0.6 |
| 7 | "knowledge card sobre RAG" | knowledge-card-builder | 0.7 |
| 8 | "workflow de lancamento" | workflow-builder | 0.6 |
| 9 | "validar output do LLM" | output-validator-builder | 0.6 |
| 10 | "configurar variaveis de ambiente" | env-config-builder | 0.7 |

Bonus: queries 1, 2, 3 tambem devem retornar crew recomendada.
Criterio: 10/10 passam.

#### C2: Dynamic Memory Tests

**Novo**: _tools/tests/test_dynamic_memory.py

| # | Teste | Assertion |
|---|-------|-----------|
| 1 | Append observation | observation_count incrementa |
| 2 | Decay aplica | confidence diminui com tempo simulado |
| 3 | Prune remove velhas | obs com confidence < 0.1 removida |
| 4 | Max 20 enforced | obs 21 causa prune da menor |
| 5 | Load top-5 | retorna max 5, ordenado por confidence |

Criterio: 5/5 passam.
Commit: "test: smoke tests auto-discovery (10/10) + dynamic memory (5/5)"

---

## IMPACTO QUANTIFICADO

### Auto-Discovery

| Metrica | Antes | Depois |
|---------|-------|--------|
| Builders descobriveis por agentes | 0/102 | 102/102 |
| Keywords indexadas (builders) | 0 | ~800 |
| Keywords indexadas (total) | 335 | ~1150 |
| Queries resolvidas sem humano | ~30% (so KIND) | ~90% (KIND + DOMAIN + SEMANTIC) |
| Tempo de routing | 30-60s (humano decide) | <1s (SQL query) |
| Crew sugerida automaticamente | Nunca | Sempre (212 crews indexadas) |

### Dynamic Memory

| Metrica | Antes | Depois |
|---------|-------|--------|
| Builders com memoria ativa | 0/103 | 103/103 |
| Observacoes acumuladas | 103 (1 cada, congeladas) | Crescente por sessao |
| Decay aplicado | Nunca | Automatico (campo existente ativado) |
| Conhecimento reutilizado no boot | 0% | Top-5 obs por builder |
| Pruning de conhecimento obsoleto | Nunca | Auto (confidence < 0.1) |

### Score Geral CEX vs IndyDevDan

| Dimensao | Dan | CEX Hoje | CEX Apos |
|----------|-----|---------|----------|
| Knowledge depth (ISOs) | 3 | 9 | 9 |
| Dynamic memory | 8 | 1 | **8** |
| Auto-discovery | 2 | 3 | **9** |
| Type system (99 kinds) | 1 | 9 | 9 |
| Quality gates (Shokunin) | 2 | 9 | 9 |
| Crew system | 5 | 8 | **9** |
| Reusability (instances) | 2 | 8 | 8 |
| Multi-perspective | 7 | 0 | 0 (futuro) |
| Cost tracking | 6 | 0 | 0 (futuro) |
| TOTAL /90 | **36** | **47** | **61** |

CEX ja lidera (+30%). Apos mission: +69% advantage.
---

## PLANO DE EXECUCAO

Track A e Track B sao INDEPENDENTES. Podem rodar em paralelo.

### Opcao 1: Sequencial (1 spawn N03, ~4h)

A1 -> A2 -> A3 -> A4 -> B1 -> B2 -> B3 -> C1 -> C2

### Opcao 2: Paralelo (2 spawns N03, ~2.5h)

Spawn 1: A1 -> A2 -> A3 -> A4 -> C1
Spawn 2: B1 -> B2 -> B3 -> C2

### Dispatch (copy-paste)

Sequencial:

    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_builder_autodiscovery.md. Execute Track A (A1-A4) depois Track B (B1-B3) depois Track C (C1-C2). Commit cada fase. Signal ao final." -interactive

Paralelo spawn 1 (discovery):

    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_builder_autodiscovery.md. Execute SOMENTE Track A (A1-A4) e C1. Commit cada fase. Signal ao final." -interactive

Paralelo spawn 2 (memory):

    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_builder_autodiscovery.md. Execute SOMENTE Track B (B1-B3) e C2. Commit cada fase. Signal ao final." -interactive

---

## CRITERIOS DE ACEITE

### Track A

| Criterio | Validacao |
|----------|----------|
| Frontmatter hydrated | 102/102 manifests com keywords + triggers + capabilities |
| Index populated | 102 manifests com keywords_json != [] no index.db |
| Query tool | cex_query.py retorna resultados para qualquer query |
| Crew suggestion | Top-1 resultado inclui crew recomendada |
| Scoring | Top-1 = builder correto em 10/10 smoke tests |
| Intent fallback | cex_intent.py usa L1 quando L0 falha |
| Zero regressao | KIND queries ("cria agent") continuam funcionando |
| Dry-run safe | cex_geo_hydrate.py --dry-run nao altera nada |

### Track B

| Criterio | Validacao |
|----------|----------|
| Update | cex_memory_update.py appenda observacao corretamente |
| Decay | Observacoes antigas perdem confidence automaticamente |
| Prune | Confidence < 0.1 removida, max 20 enforced |
| Load at boot | Top-5 observacoes injetadas no contexto do builder |
| Skill | skill_memory_update.md existe em _shared/ |
| Tests | 5/5 test_dynamic_memory.py passam |

---

## ANTI-PATTERNS

- NAO alterar OBJECT_TO_KINDS com keywords de dominio (polui taxonomia, nao escala)
- NAO usar embeddings/ML para discovery (keyword match basta para 102 builders)
- NAO criar novo banco de dados (usar index.db existente)
- NAO duplicar keywords (frontmatter = source of truth, ## Routing = legacy)
- NAO alterar body dos manifests (so adicionar ao frontmatter)
- NAO deixar bld_memory crescer sem limite (max 20 observations, auto-prune)
- NAO injetar TODAS observacoes no prompt (max 5, threshold >= 0.3)
- NAO quebrar cex_intent.py existente (adicionar fallback, NAO substituir L0)
- NAO confundir com mission_geo_discovery.md (aquela eh geographic entity resolution)

---

## ARTEFATOS EXISTENTES (Input)

| Artefato | Path | Usar Como |
|----------|------|-----------|
| cex_index.py | _tools/cex_index.py (329 ln) | Base A2: adicionar campos |
| cex_intent.py | _tools/cex_intent.py | Base A4: adicionar fallback |
| cex_8f_motor.py | _tools/cex_8f_motor.py | Base B2: carregar memory. NAO alterar OBJECT_TO_KINDS |
| cex_crew_runner.py | _tools/cex_crew_runner.py | Base B2: injetar memory no compose_prompt |
| index.db | .cex/index.db (3112 files) | Adicionar campos triggers_json + capabilities |
| 102 manifests | archetypes/builders/*/bld_manifest_*.md | Input A1: hydrate frontmatter |
| 103 bld_memory | archetypes/builders/*/bld_memory_*.md | Input B1: ativar como dynamic |
| 103 bld_collaboration | archetypes/builders/*/bld_collaboration_*.md | Input A3: crew suggestions |
| 18 dispatch rules | N0*/orchestration/dispatch_rule_*.md | Referencia: ja indexados |

## ARTEFATOS CRIADOS (Output)

| # | Artefato | Track | Tipo |
|---|----------|-------|------|
| 1 | _tools/cex_geo_hydrate.py | A1 | Novo script |
| 2 | _tools/cex_index.py (atualizado) | A2 | Update |
| 3 | _tools/cex_query.py | A3 | Novo script |
| 4 | _tools/cex_intent.py (atualizado) | A4 | Update |
| 5 | _tools/cex_memory_update.py | B1 | Novo script |
| 6 | _tools/cex_8f_motor.py (atualizado) | B2 | Update |
| 7 | _tools/cex_crew_runner.py (atualizado) | B2 | Update |
| 8 | archetypes/builders/_shared/skill_memory_update.md | B3 | Novo artefato |
| 9 | _tools/tests/test_autodiscovery.py | C1 | Novo test |
| 10 | _tools/tests/test_dynamic_memory.py | C2 | Novo test |
| 11 | 102 bld_manifest_*.md (frontmatter atualizado) | A1 | Batch update |
| 12 | .cex/index.db (rebuild) | A2 | Rebuild |

---

**Total: 12 artefatos (3 novos scripts + 3 updates + 1 skill + 2 tests + 102 manifests + 1 DB rebuild)**
**Estimativa: 4-5h sequencial | 2.5h paralelo (2 spawns N03)**