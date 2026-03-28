# CEX Architecture v3.0
## Molde Inviolavel - Estrutura Fractal 7x12x78 + Engine Layer

**Status**: CONSOLIDADO | **Data**: 2026-03-28 | **Quebrar**: PROIBIDO

---

## 1. Hierarquia de 5 Niveis

| Nivel | Pattern | Conteudo | Modificavel |
|-------|---------|----------|-------------|
| L0 | `archetypes/builders/{type}-builder/` | 13 ISO files (fabrica) | Somente via review |
| L1 | `P{NN}_{lp}/` | _schema.yaml + templates/ + examples/ | Versionado, breaking = major |
| L2 | `N{XX}_{function}/` | NUCLEUS.md | Gerado por scaffold |
| L3 | `N{XX}/P{NN}_{lp}/` | _schema.yaml (inherits root) | Override: fields_add only |
| L4 | `N{XX}/P{NN}/{type}/` | examples/ + templates/ + compiled/ | Livre, validado por gates |

---

## 1.1 Camada Acima: As 8 Funcoes LLM

Os 12 pillars organizam ARTEFATOS (filesystem). As 8 funcoes descrevem o que o LLM FAZ (pipeline).
Todo sistema LLM — de prompt a satellite — executa estas funcoes nesta ordem:

| # | Funcao | Verbo | O Que Faz | pillars |
|---|--------|-------|-----------|-----|
| 1 | BECOME | Ser | Identidade, persona | P02, P03 |
| 2 | INJECT | Saber | Contexto, knowledge | P01, P10 |
| 3 | REASON | Pensar | CoT, planejamento | P03 |
| 4 | CALL | Fazer | Tools, APIs, MCPs | P04 |
| 5 | PRODUCE | Gerar | Output final | P03, P05 |
| 6 | CONSTRAIN | Restringir | Schemas, validacao | P06, P08 |
| 7 | GOVERN | Avaliar | Quality gates, evals | P07, P09, P11 |
| 8 | COLLABORATE | Coordenar | Signals, handoffs | P12 |

**Lei**: funcoes sao PIPELINE (sequencia), nao categorias (pastas).
**Spec completa**: `LLM_PIPELINE.md` (root do CEX).

---

## 2. Os 7 Nucleos

| ID | Dir | Funcao | pillars Primarios |
|----|-----|--------|---------------|
| N01 | N01_intelligence | Pesquisa | P01, P07 |
| N02 | N02_marketing | Marketing | P03, P05 |
| N03 | N03_engineering | Engenharia | P02, P04, P06 |
| N04 | N04_knowledge | Conhecimento | P01, P10 |
| N05 | N05_operations | Operacoes | P04, P12 |
| N06 | N06_commercial | Comercial | P05, P09 |
| N07 | N07_admin | Administracao | P08, P11, P12 |

**Inviolavel**: nao adicionar/remover nucleos sem revisao de arquitetura.

---

## 3. Os 12 pillars x 78 Types

| pillar | Nome | Types |
|----|------|-------|
| P01 | Knowledge | knowledge_card, rag_source, glossary_entry, context_doc, embedding_config, few_shot_example (6) |
| P02 | Model | agent, lens, boot_config, mental_model, model_card, router, fallback_chain, iso_package, axiom (9) |
| P03 | Prompt | system_prompt, user_prompt, prompt_template, few_shot, chain_of_thought, react, chain, meta_prompt, router_prompt, planner (10) |
| P04 | Tools | skill, mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon, component (10) |
| P05 | Output | response_format, parser, formatter, naming_rule (4) |
| P06 | Schema | input_schema, type_def, validator, interface, validation_schema, artifact_blueprint, grammar (7) |
| P07 | Evals | unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric (6) |
| P08 | Architecture | satellite_spec, pattern, law, diagram, component_map (5) |
| P09 | Config | env_config, path_config, permission, feature_flag, runtime_rule (5) |
| P10 | Memory | runtime_state, brain_index, learning_record, session_state (4) |
| P11 | Feedback | quality_gate, bugloop, lifecycle_rule, guardrail, optimizer (5) |
| P12 | Orchestration | workflow, dag, spawn_config, signal, handoff, dispatch_rule, crew (7) |

---

## 4. Formato Dual (Mandamento #2)

| O que | Fonte (.md) | Compiled | Quem sincroniza |
|-------|-------------|----------|-----------------|
| Artefatos (78 kinds) | YAML frontmatter + MD body | `.yaml` ou `.json` | distill.py |
| Schemas | `.yaml` only | N/A | manual |
| Builders (13 ISO) | `.md` only | N/A | manual |
| Meta-docs | `.md` only | N/A | manual |

**Regra**: todo artefato instance existe em DOIS formatos. O .md eh fonte de autoria. O compiled/ eh output de consumo.

---

## 5. Heranca de Schema

```
P{NN}_*/_schema.yaml              ROOT (fonte de verdade)
  |
  +-- N{XX}/P{NN}/_schema.yaml    NUCLEO (herda + especializa)
       inherits: root
       fields_add: {}              Campos extras deste nucleo
       constraints_override: {}    Restricoes especificas
```

**Regra**: nucleo NUNCA remove campos do root. Somente ADICIONA ou RESTRINGE.

---

## 6. Builders (L0)

13 ISO files por builder:

| # | File | pillar | Funcao |
|---|------|----|--------|
| 1 | MANIFEST.md | P02 | Identidade |
| 2 | SYSTEM_PROMPT.md | P03 | Persona |
| 3 | KNOWLEDGE.md | P01 | Domain knowledge |
| 4 | INSTRUCTIONS.md | P03 | Pipeline 3-fases |
| 5 | TOOLS.md | P04 | Ferramentas |
| 6 | OUTPUT_TEMPLATE.md | P05 | Template {{vars}} |
| 7 | SCHEMA.md | P06 | SOURCE OF TRUTH |
| 8 | EXAMPLES.md | P07 | Golden + anti |
| 9 | ARCHITECTURE.md | P08 | Boundary |
| 10 | CONFIG.md | P09 | Naming, paths |
| 11 | MEMORY.md | P10 | Patterns |
| 12 | QUALITY_GATES.md | P11 | HARD/SOFT gates |
| 13 | COLLABORATION.md | P12 | Crews |

Cross-validation obrigatoria antes de commit (ARCHETYPE_BUILDER_CHECKLIST).

---

## 7. Quality Gates

| Score | Tier | Destino |
|-------|------|---------|
| >= 9.5 | Golden | Pool referencia |
| >= 8.0 | Skilled | Publicado |
| >= 7.0 | Learning | Experimental |
| < 7.0 | Rejected | Refazer |

Density minima: 0.8. Max size: per _schema.yaml.

---

## 8. Regras Inviolaveis

1. NUNCA criar artefato fora de N{XX}/P{NN}/{type}/
2. NUNCA editar schema de nucleo sem inherits do root
3. NUNCA commitar builder sem CHECKLIST
4. NUNCA remover campo de schema (deprecate)
5. NUNCA pular quality gate (min 7.0)
6. NUNCA criar type fora de P{NN}/_schema.yaml root
7. SEMPRE dual output pra artefatos
8. SEMPRE density >= 0.8
9. SEMPRE builder constroi, humano revisa
10. SEMPRE path = endereco semantico

---

## 9. Tools Layer (L3 ENGINE)

13 scripts in `_tools/` power the CEX runtime. Built during overnight Waves 1-3.

| Category | Tools | Purpose |
|----------|-------|---------|
| **Governance** | `cex_doctor.py` v2, `validate_builder.py` v2, `setup_hooks.sh` | Naming v2.0, density, 13-file completeness, pre-commit (7 checks) |
| **Engine** | `cex_index.py`, `cex_pipeline.py`, `cex_feedback.py`, `cex_forge.py` | SQLite index, 5-stage pipeline (CAPTURE>ENVELOPE), quality tracking |
| **Product** | `cex_init.py` | CLI scaffolder: 5 questions to functional repo |
| **Compile** | `cex_compile.py`, `distill.py` | .md to .yaml compilation and sync |
| **Infra** | `bootstrap.py`, `bump_version.py`, `validate_schema.py`, `changelog_gen.py` | Setup, versioning, schema validation, changelog |

### Pipeline Stages (cex_pipeline.py)

```
CAPTURE -> DECOMPOSE -> HYDRATE -> COMPILE -> ENVELOPE
  (input)   (split)     (enrich)   (build)    (package)
```

### Quality Loop (cex_feedback.py)

```
Score >= 8.0 -> promote to published
Score >= 7.0 -> experimental (keep)
Score <  7.0 -> auto-archive
```

---

## 10. Numeros

| Metrica | Quantidade |
|---------|-----------|
| Total files | 1,839 |
| Nucleos | 7 |
| Pillars | 12 (x7 = 84) |
| Types | 78 (x7 = 546 dirs) |
| Builders (bld_*) | 932 (70 dirs x 13 files) |
| Templates (tpl_*) | 85 |
| Examples (ex_*) | 193 |
| Compiled (*.yaml) | 333 |
| Tools (_tools/) | 13 scripts |
| ISO files/builder | 13 |
| Subdirs/type | 3 (examples, templates, compiled) |
| Wikilinks | 392 |

---

*Architecture v3.0 -- Molde inviolavel. Engine built. Pipeline running.*