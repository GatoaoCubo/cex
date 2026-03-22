# RECORDS CODEX -- Biblia Universal de Meta-Construcao
## v1.0 | O documento que define COMO tudo eh criado | LIVING

---

## 0. PROPOSITO
DNA do Records. Hierarquia: CODEX > _schema > _generator > templates > instances

## 1. VARIAVEIS
- `{{snake_case}}` = LLM preenche na criacao
- `{{BRAND_UPPER}}` = York preenche no fork
- `${ENV_VAR}` = sistema preenche no runtime
- `__auto__` = lifecycle preenche automatico
- Nunca `[PLACEHOLDER]` (conflita Markdown)

## 2. ANATOMIA UNIVERSAL
YAML front: id, type, lp, quality, keywords(3+), long_tails(2+), bullets(3+), axioms(1+), related
MD body: title, summary 1-line, Fatos (bullets), Aplicacao (inputs/outputs)
Density >= 0.8. Max 2KB. Prosa > 3 linhas proibida.

## 3. NAMING
Pattern: `{lp}_{type}_{topic}.{ext}` Ex: `p01_kc_ecommerce_br.md`
Regras: lowercase, snake_case, ASCII, max 50 chars, dual (.md+.yaml)

## 4. PASTAS
Brain: P01-P12 (cada com _schema, _generator, _custom, templates, examples)
Satellites: satellites/{name}/P01-P12 (instances reais)
Meta: _meta/ (CODEX, GLOSSARY, MANDAMENTOS)

## 5. SCHEMAS = _schema.yaml por LP (contrato, validado pre-commit)
## 6. GENERATORS = _generator.md por LP (instrucoes passo-a-passo)
## 7. META-TEMPLATE = bootstrap (Edison cria v0, evolui durante uso)
## 8. DUAL OUTPUT = .md (humano) + .yaml (LLM) lado a lado

## 9. LIFECYCLE (CRUD autonomo)
CREATE (generator+template) > INDEX (Brain MCP) > READ (top-K) > USE > RESULTS > NEW KC > repeat
ARCHIVE: quality<7 + age>30d. PROMOTE: used>10x + quality>9 = examples/

## 10. BOOT PROVIDER-AGNOSTIC
1 template > N: CLAUDE.md, .cursorrules, AGENTS.md, .windsurfrules, copilot-instructions.md

## 11. MIGRACAO
KC>p01_kc | HOP>p03_prompt | FAT/ADW>p12_workflow | AGT>p02_agent | SKL>p04_skill
Progressiva: 1 LP por onda

## 12. ANTI-FRAGILIDADE
68 CORE fixos + _custom/ extensivel. Promocao: 10x+quality>8=CORE. Deprecacao: 90d sem uso.

## 13. MANDAMENTOS
1. Record denso max 2KB | 2. Dual output | 3. Metadata densa
4. Nunca prosa>3 linhas | 5. Nunca score<7 | 6. Scout first
7. Validar contra schema | 8. Brain read-only | 9. Satellites independentes
10. Cada ciclo melhora o anterior (flywheel)

---

## 14. TABELA COMPLETA: 68 TIPOS x 12 LPs

### CORE (peso 1.0)
P01 Knowledge (6): knowledge_card, rag_source, glossary_entry, context_doc, embedding_config, few_shot_example
P02 Model (7): agent, lens, boot_config, mental_model, model_card, router, fallback_chain
P03 Prompt (5): system_prompt, action_prompt, prompt_template, instruction, chain
P04 Tools (9): mcp_server, hook, skill, plugin, client, cli_tool, scraper, connector, daemon

### QUALITY (peso 0.8)
P05 Output (4): output_schema, parser, formatter, naming_rule
P06 Schema (5): input_schema, output_schema, type_def, validator, interface
P07 Evals (6): unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric
P11 Feedback (5): quality_gate, bugloop, lifecycle_rule, guardrail, optimizer

### SCALE (peso 0.6)
P08 Architecture (5): satellite_spec, pattern, law, diagram, component_map
P09 Config (5): env_config, path_config, permission, feature_flag, runtime_rule
P10 Memory (5): mental_model, brain_index, learning_record, session_state, axiom
P12 Orchestration (6): workflow, dag, spawn_config, signal, handoff, dispatch_rule

---

## 15. TAMANHOS POR TIPO

| Categoria | Max bytes | Tipos |
|-----------|----------|-------|
| Dense content (KC, agent, skill, prompt, workflow) | 2048 | 15 |
| Medium (hook, plugin, eval, schema, dag) | 1024 | 30 |
| Compact (config, signal, flag, naming) | 512 | 23 |

---

## 16. FONTES CONSOLIDADAS NESTE CODEX

| Fonte | O que contribuiu |
|-------|-----------------|
| META_TEMPLATE_LIBRARY.md | 8 templates existentes com {{vars}} |
| TPL_EDISON_009-020 | 12 meta-templates de tipos diferentes |
| META_CONSTRUCTION_ANALYSIS.md | Genesis chain (como Edison cria) |
| KC_PYTHA_118_DISLER_PATTERNS | Hooks-first, UV scripts, output styles |
| LAWS_v3_PRACTICAL.md | 11 leis operacionais |
| RSC_INDUSTRY_VOCABULARY.md | Naming validated by 7 frameworks |
| RSC_CHUNKING_DUALOUTPUT_SOTA.md | 2KB chunks = SOTA validated |
| GLOSSARIO_v1.md | 68 tipos classificados |
| 12 audios WhatsApp | Visao do usuario |
| 3800 artifacts existentes | Materia-prima real |

---

## 17. ROADMAP DE CONSTRUCAO (6 ondas)

Onda 1: DESTILAR golden do codexa-core > criar schemas baseados em dados reais
Onda 2: SCAFFOLD repo + primeiros templates P01
Onda 3: EXPANDIR 1 LP por iteracao (P02>P03>P04>...)
Onda 4: MIGRACAO massiva com grid (renaming + validation)
Onda 5: ANTI-FRAGILIDADE (_custom + promotion + lifecycle)
Onda 6: PRODUTO (bootstrap wizard + fork teste)

Cada onda: planeja > executa > avalia > melhora. Espiral, nao cascata.

---

*CODEX v1.0 | LIVING | 2026-03-22*