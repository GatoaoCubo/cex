# PLANO N03: O Construtor que Constroi Construtores

**Status**: PLANEJAMENTO | **Versao**: 1.0.0 | **Data**: 2026-03-30
**Autor**: STELLA | **Executor**: EDISON (grid) | **Estimativa**: ~90 min

---

## 0. O QUE E N03

N03 nao eh mais um nucleo de engenharia. N03 eh a **fabrica**.

Enquanto N01 pesquisa, N02 escreve copy, N04 organiza conhecimento --
N03 eh o unico nucleo que **produz os artefatos que compoem TODOS os outros nucleos**.
O agent de N03 eh quem constroi agents. O workflow de N03 eh o proprio 8F pipeline.
O quality_gate de N03 valida os artefatos que ele mesmo produz.

Isso cria um **Strange Loop** (Hofstadter): N03 se auto-constroi.

### As 3 Camadas de N03

| Camada | O que eh | Estado |
|--------|---------|--------|
| L0 HARDWARE | Scripts Python (Runner, Motor, Doctor, Forge, Compiler, Indexer) | 4.908 linhas, 10 tools |
| L1 FIRMWARE | Builders (99 kinds x 13 ISOs = 1.287 arquivos) | 86 PASS, 12 WARN |
| L2 SISTEMA OP | Artefatos do nucleo (agent, workflow, system_prompt...) | 12 placeholders, precisa 26 |

**O que falta**: L0 e L1 estao 95% prontos. L2 esta em 46%. Este plano constroi L2.

---

## 1. INVENTARIO

### 1.1 Existentes (12 artefatos -- placeholder quality)

| # | Kind | Pillar | Fn | Subdir | Status |
|---|------|--------|----|--------|--------|
| 1 | agent | P02 | BECOME | agents/ | Generico |
| 2 | system_prompt | P03 | BECOME | prompts/ | Generico |
| 3 | agent_card | P08 | BECOME | architecture/ | Generico |
| 4 | knowledge_card | P01 | INJECT | knowledge/ | Generico |
| 5 | pattern | P08 | INJECT | architecture/ | Generico |
| 6 | dispatch_rule | P12 | REASON | orchestration/ | THIN |
| 7 | interface | P06 | CONSTRAIN | schemas/ | Generico |
| 8 | response_format | P05 | CONSTRAIN | output/ | Generico |
| 9 | workflow | P12 | PRODUCE | orchestration/ | Generico |
| 10 | boot_config | P02 | GOVERN | config/ | Generico |
| 11 | quality_gate | P11 | GOVERN | feedback/ | Generico |
| 12 | scoring_rubric | P07 | GOVERN | quality/ | Generico |

Todos sao generic engineering -- nenhum reflete que N03 eh o construtor-de-artefatos.

### 1.2 Faltantes (14 artefatos)

| # | Kind | Pillar | Fn | Subdir | Porque |
|---|------|--------|----|--------|--------|
| 13 | **mental_model** | P02 | BECOME | agents/ | Routing logic, decisao de builder |
| 14 | **axiom** | P02 | BECOME | agents/ | Verdades imutaveis do construtor |
| 15 | **prompt_template** | P03 | CONSTRAIN | prompts/ | Template reusavel |
| 16 | **few_shot_example** | P01 | INJECT | knowledge/ | Exemplos golden |
| 17 | **function_def** | P04 | CALL | tools/ | Definicao dos 10 tools |
| 18 | **input_schema** | P06 | CONSTRAIN | schemas/ | O que N03 aceita como input |
| 19 | **guardrail** | P11 | CONSTRAIN | feedback/ | Regras de protecao |
| 20 | **benchmark** | P07 | GOVERN | quality/ | Baseline de performance |
| 21 | **learning_record** | P10 | INJECT | memory/ | Licoes aprendidas |
| 22 | **handoff** | P12 | COLLABORATE | orchestration/ | Recebe/devolve trabalho |
| 23 | **signal** | P12 | COLLABORATE | orchestration/ | Completion/error signals |
| 24 | **spawn_config** | P12 | GOVERN | orchestration/ | Config de spawn |
| 25 | **dag** | P12 | PRODUCE | orchestration/ | 8F pipeline como DAG |
| 26 | **chain** | P03 | PRODUCE | prompts/ | Chain multi-step |

**Total pos-conclusao**: 26 artefatos, 11/12 pillars, 8/8 funcoes.

---

## 2. O STRANGE LOOP: BOOTSTRAP EM 3 FASES

**Paradoxo**: Para construir N03, precisamos do 8F pipeline. Mas o 8F pipeline EH N03.

**Solucao**: Bootstrap em 3 fases progressivas:

| Fase | Nome | O que | Quem | Tempo |
|------|------|-------|------|-------|
| 1 | GENESIS | 7 artefatos core escritos manualmente | STELLA direto | ~40min |
| 2 | AUTOPOIESIS | 12 artefatos novos via 8F Runner | 3 EDISON paralelos | ~30min |
| 3 | REWRITE | 19 artefatos reescritos com qualidade | 3 EDISON paralelos | ~20min |

**Porque 3 e nao 1**: O runner generico produz engineering generico.
N03 precisa de conteudo que sabe que eh fabrica. Fase 1 injeta essa compreensao.

---

## 3. FASE 1: GENESIS -- 7 Artefatos Core

### 3.1 agent (REWRITE)
- **Identidade**: Construtor de artefatos. Input = intencao humana, output = artefato CEX valido.
- **Capabilities**: parse intent, load builder ISOs, run 8F, compile, index, validate
- **Tools**: motor, runner, compile, doctor, forge, index, feedback, kind_register, nucleus_builder
- **Routing**: create, build, construct, design, scaffold, generate, forge
- **NOT**: deploy (N05), research (N01), market (N02), knowledge (N04)

### 3.2 system_prompt (REWRITE)
- **Core**: Voce eh o Builder Nucleus. Cada output DEVE ser artefato CEX valido.
- **Rules**: ler schema antes de produzir, verificar exemplos, nunca sem frontmatter
- **Inclui**: 8F pipeline como procedimento operacional inline

### 3.3 mental_model (NEW)
- **Decision tree**: intent > Motor > kind resolution > builder selection > 8F run
- **Routing**: simples (1 artefato) vs composta (multi-kind)
- **Temperature**: PRODUCE = higher creativity, GOVERN = deterministic
- **Cost**: haiku scaffold, sonnet conteudo, opus architecture

### 3.4 axiom (NEW)
1. Todo artefato tem frontmatter YAML com id, kind, pillar, title, version
2. Todo kind pertence a exatamente 1 dos 12 pillars
3. Todo kind exerce exatamente 1 das 8 funcoes
4. Qualidade minima para publicacao: 8.0
5. Compilados (.yaml) derivam de fontes (.md)
6. 8F pipeline sequencial: skip permitido, reorder nao
7. Builders sao 13 ISOs -- nenhum opcional
8. Nenhum artefato referencia implementacao proprietaria
9. O construtor especifica, nunca executa
10. kinds_meta.json eh fonte de verdade

### 3.5 workflow (REWRITE)
**O 8F Pipeline como workflow executavel:**

| Step | Name | Tool | Output | Signal |
|------|------|------|--------|--------|
| 1 | PARSE_INTENT | cex_8f_motor | classified_kinds | intent_parsed |
| 2 | LOAD_CONSTRAINTS | Runner.F1 | max_bytes, naming | constrained |
| 3 | LOAD_IDENTITY | Runner.F2 | system_prompt_text | identity_loaded |
| 4 | INJECT_KNOWLEDGE | Runner.F3 | knowledge_context | knowledge_injected |
| 5 | REASON_PLAN | Runner.F4 | construction_plan | plan_ready |
| 6 | LOAD_TOOLS | Runner.F5 | tools, existing | tools_ready |
| 7 | PRODUCE_ARTIFACT | Runner.F6 | artifact_md | artifact_produced |
| 8 | VALIDATE | Runner.F7 | pass/fail, score | validated |
| 9 | SAVE_COMPILE_INDEX | Runner.F8 | path, compiled | complete |

Retry: Step 7 retries 2x on quality failure.

### 3.6 quality_gate (REWRITE)

| Gate | Check | Severity |
|------|-------|----------|
| H01 | Frontmatter valid YAML, all required fields | HARD FAIL |
| H02 | Kind matches requested | HARD FAIL |
| H03 | Naming convention | WARN |
| H04 | References resolve | WARN |
| H05 | Density >= 0.80 | SOFT FAIL |
| H06 | Size <= max_bytes | SOFT FAIL |
| H07 | Schema fields present | HARD FAIL |

### 3.7 scoring_rubric (REWRITE)

| Dimension | Weight | 10 (Golden) | 5 (Review) | 1 (Reject) |
|-----------|--------|-------------|------------|------------|
| Correctness | 30% | Frontmatter valid, schema match | Minor issues | Wrong kind |
| Completeness | 25% | All sections filled | >70% | <50% |
| Density | 20% | 0.90+ ratio | 0.80 | <0.70 |
| Usefulness | 15% | Immediately usable | Needs minor edits | Needs rewrite |
| Integration | 10% | Compiles, indexes | Some broken | Won't compile |

---

## 4. FASE 2: AUTOPOIESIS -- N03 Produz o Resto

N03 agora tem identidade. Usa o 8F Runner COM identidade de N03 para gerar 12 novos.

| Wave | Artefatos | Slot |
|------|-----------|------|
| 2A (inputs) | input_schema, function_def, prompt_template, few_shot_example | EDISON-A |
| 2B (governance) | guardrail, benchmark, learning_record | EDISON-B |
| 2C (collaboration) | handoff, signal, spawn_config, dag, chain | EDISON-C |

---

## 5. FASE 3: REWRITE -- O Circulo se Fecha

N03 completo (26 artefatos) reescreve:
1. Os 12 placeholders originais (generico > especifico)
2. Os 7 core da Fase 1 (manual > pipeline-validated)

**Criterio**: quality >= 8.5 (mais alto porque N03 eh o standard-bearer).

| Wave | Artefatos | Slot |
|------|-----------|------|
| 3A (architecture) | agent_card, pattern, interface, boot_config | EDISON-A |
| 3B (runtime) | dispatch_rule, response_format, knowledge_card | EDISON-B |
| 3C (core rewrite) | agent, SP, MM, axiom, WF, QG, SR com F7 | EDISON-C |

---

## 6. EXECUCAO: GRID DISPATCH

| Wave | Quem | Slots | Tempo | Artefatos |
|------|------|-------|-------|-----------|
| 1 GENESIS | STELLA direto | 0 (manual) | ~40min | 7 core |
| 2 AUTOPOIESIS | Grid EDISON | 3 paralelos | ~30min | 12 novos |
| 3 REWRITE | Grid EDISON | 3 paralelos | ~20min | 19 rewrites |
| **TOTAL** | | | **~90min** | **26 artefatos finais** |

---

## 7. VALIDACAO FINAL

| Metrica | Threshold | Atual | Esperado |
|---------|-----------|-------|----------|
| Artefatos N03 | 26 | 12 | 26 |
| Pillars cobertos | 11/12 | 9/12 | 11/12 |
| 8F funcoes | 8/8 | 6/8 | 8/8 |
| Density media | >= 0.85 | ~0.73 | >= 0.85 |
| Quality media | >= 8.5 | ~6.0 | >= 8.5 |
| Self-build test | PASS | N/A | PASS |
| Cross-build test | PASS | N/A | PASS |

**Self-build**: N03 constroi um agent usando seus proprios artefatos.
**Cross-build**: N03 constroi um KC de outro nucleo (N04).

---

## 8. POS-N03: O QUE DESBLOQUEIA

1. **N01-N07 automaticos** -- N03 eh a fabrica que constroi todos
2. **N08+ on-demand** -- basta um seed para novo nucleo
3. **Instancias mais ricas** -- mais artefatos de referencia
4. **8F Runner com identidade** -- nao script generico, eh workflow de N03
5. **Self-improvement** -- N03 reescreve seus proprios builders

**N03 eh o Genesis. Todo o resto deriva dele.**

---

## RESUMO EXECUTIVO

| Dimensao | Hoje | Meta |
|----------|------|------|
| Artefatos | 12 placeholders | 26 especificos |
| Cobertura | 46% | 92% |
| Quality | ~6.0 | >= 8.5 |
| Self-build | N/A | PASS |

3 fases (Genesis > Autopoiesis > Rewrite), ~90 min, resultado: N03 auto-consistente.

---
*A fabrica que fabrica a fabrica. -- Hofstadter via CEX*
