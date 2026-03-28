# CEX Crew Runner -- Builder Execution
**Builder**: `_builder-builder`
**Function**: BECOME
**Intent**: reconstroi quality-gate-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:18.974812

## Intent Context
- **Verb**: reconstroi
- **Object**: quality-gate-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_meta_manifest_builder.md
---
meta: true
file_position: 1/13
pillar: P02
llm_function: BECOME
purpose: Meta-template for generating MANIFEST.md of any kind-builder
---

# {{builder_name}}
<!-- Este meta-file gera o MANIFEST.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml do tipo-alvo, TAXONOMY_LAYERS.yaml, SEED_BANK.yaml -->

<!-- NOTA: {{builder_name}} = kebab-case do tipo. Ex: model-card-builder, signal-builder -->
<!-- NOTA: {{type_name}} = snake_case do tipo. Ex: model_card, signal, quality_gate -->
<!-- NOTA: {{lp}} = Pillar do tipo-alvo (P01-P12). Buscar em TAXONOMY_LAYERS.yaml -->
<!-- NOTA: {{lp_chief}} = {lp}-chief. Ex: p02-chief, p01-chief -->
<!-- NOTA: {{domain}} = geralmente igual a {{type_name}}, mas pode variar -->
<!-- NOTA: {{type_name_kebab}} = kebab-case do tipo. Ex: model-card, knowledge-card -->
<!-- NOTA: {{tags}} = [kind-builder, {{type_name_kebab}}, {{lp}}, specialist, ...extras] -->

```yaml
---
id: {{builder_name}}
kind: type_builder
pillar: {{lp}}
parent: {{lp_chief}} [PLANNED]
domain: {{type_name}}
llm_function: BECOME
version: 1.0.0
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: {{author}}
tags: [kind-builder, {{type_name_kebab}}, {{lp}}, specialist]
---
```

## Identity
Especialista em construir `{{type_name}}` — {{one_line_description}}.
<!-- NOTA: {{one_line_description}} = extrair de TAXONOMY_LAYERS.yaml kinds[].description ou _schema.yaml purpose -->
<!-- Acrescente 1-2 frases sobre dominio, ferramentas, e o que produz -->

## Capabilities
<!-- NOTA: 4-6 bullets descrevendo o que o builder PODE fazer -->
<!-- Padrao observado nos 4 builders existentes: -->
- Pesquisar/analisar {{domain_knowledge}} para produzir {{type_name}}
- Produzir {{type_name}} com frontmatter completo ({{field_count}} campos)
- Validar artifact contra quality gates ({{hard_count}} HARD + {{soft_count}} SOFT)
- {{capability_extra_1}}
<!-- NOTA: {{field_count}} = contar campos em _schema.yaml -->
<!-- NOTA: {{hard_count}}/{{soft_count}} = definir em QUALITY_GATES.md -->

## Routing
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}, {{keyword_4}}]
triggers: "{{trigger_phrase_1}}", "{{trigger_phrase_2}}", "{{trigger_phrase_3}}"
<!-- NOTA: keywords = 4-8 termos que ativam este builder via brain_query -->
<!-- NOTA: triggers = 2-3 frases naturais que um user diria -->

## Crew Role
In a crew, I handle {{ROLE_CAPS}}.
I answer: "{{one_question_this_builder_answers}}"
I do NOT handle: {{exclusion_1}}, {{exclusion_2}}, {{exclusion_3}}.
<!-- NOTA: {{ROLE_CAPS}} = papel em CAPS. Ex: MODEL DOCUMENTATION, KNOWLEDGE DISTILLATION -->
<!-- NOTA: {{exclusions}} = tipos vizinhos no mesmo Pillar ou frequentemente confundidos -->
<!-- Buscar confusoes em TAXONOMY_LAYERS.yaml overlaps e na _schema.yaml do Pillar -->

### bld_instruction_builder.md
---
kind: instruction
id: bld_instruction_builder
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for type_builder (meta-builder)
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a type_builder

## Phase 1: RESEARCH
1. Identify the target type: which kind from the taxonomy needs a builder
2. Read the target type's `_schema.yaml` to understand fields, constraints, and body structure
3. Read `TAXONOMY_LAYERS.yaml` to determine pillar assignment and sibling types
4. Read `SEED_BANK.yaml` for domain vocabulary and keyword candidates
5. Analyze existing builders in `archetypes/builders/` for pattern consistency
6. Identify boundary types: which sibling kinds are frequently confused with the target
7. Determine crew role: what single question does this builder answer

## Phase 2: COMPOSE
1. Read META_MANIFEST.md, META_SYSTEM_PROMPT.md, META_INSTRUCTIONS.md — meta-templates
2. Read META_OUTPUT_TEMPLATE.md — fill template following META constraints
3. Generate MANIFEST.md: id, kind (type_builder), pillar, domain, capabilities, routing, crew role
4. Generate SYSTEM_PROMPT.md: persona as domain specialist, 8-12 rules, boundary enforcement
5. Generate INSTRUCTIONS.md: 3-phase pipeline adapted to the target type's complexity
6. Generate KNOWLEDGE.md: domain theory, anti-patterns, size calibration, boundaries
7. Generate SCHEMA.md: all fields from _schema.yaml with types, required/optional, constraints
8. Generate OUTPUT_TEMPLATE.md: literal fill-in template with {{variables}}
9. Generate QUALITY_GATES.md: HARD gates (must pass) + SOFT gates (score contribution)
10. Generate remaining files: EXAMPLES.md, ARCHITECTURE.md, CONFIG.md, MEMORY.md, COLLABORATION.md, TOOLS.md
11. Set quality: null in every generated artifact (NEVER self-score)

## Phase 3: VALIDATE
1. Check each generated file against its META_ template constraints
2. HARD gates: all 13 files present, YAML parses in every frontmatter, id matches builder naming pattern, kind == type_builder, quality == null everywhere, domain matches target type
3. SOFT gates: capabilities >= 4 bullets, routing keywords >= 4, crew role has exclusions, boundary types listed
4. Cross-check: is every sibling type mentioned in boundaries? Does INSTRUCTIONS.md match SCHEMA.md body sections? Are EXAMPLES.md examples realistic?
5. If score < 8.0: revise weakest file in same pass before outputting

### bld_meta_instructions_builder.md
---
kind: meta_instructions
id: bld_meta_instructions_builder
meta: true
file_position: 4/13
pillar: P03
llm_function: REASON
purpose: Meta-template for generating INSTRUCTIONS.md of any kind-builder
---

# Instructions: How to Produce a {{type_name}}
<!-- Este meta-file gera o INSTRUCTIONS.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml + SCHEMA.md + OUTPUT_TEMPLATE.md ja gerados -->

```yaml
---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for {{type_name}}
pattern: 3-phase pipeline (research -> compose -> validate)
---
```

## Phase 1: RESEARCH
<!-- NOTA: Fase de coleta. Nome pode variar: RESEARCH, CLASSIFY, DISCOVER -->
<!-- signal usa CLASSIFY (porque eh simples); model_card usa RESEARCH (porque precisa pesquisar) -->
<!-- Escolha o nome que reflete a complexidade do tipo -->
1. Identify the {{primary_entity}}: {{what_to_identify}}
<!-- NOTA: {{primary_entity}} = "model" para model_card, "topic" para KC, "event" para signal -->
2. {{research_step_2}}
3. Gather sources: {{source_types}}
4. Check brain_query for existing {{type_name}}s (avoid duplicates)
5. {{research_step_extra}}
<!-- NOTA: Steps variam por complexidade: -->
<!-- - Simples (signal): 3-4 steps, foco em classificar o evento -->
<!-- - Medio (KC, quality_gate): 5-6 steps, foco em pesquisar dominio -->
<!-- - Complexo (model_card): 6-7 steps, foco em multiple sources + URLs -->

## Phase 2: COMPOSE
<!-- NOTA: Fase de escrita. Estrutura UNIVERSAL: -->
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: {{field_summary}}
<!-- NOTA: {{field_summary}} = "all N fields (null OK for optional)" -->
4. Set quality: null (NEVER self-score)
<!-- STEPS ESPECIFICOS DO TIPO (gerar a partir de SCHEMA.md body sections): -->
5. Write {{body_section_1}}
6. Write {{body_section_2}}
7. Write {{body_section_3}}
<!-- NOTA: Para cada secao obrigatoria em SCHEMA.md Body Structure, crie um step -->
<!-- Inclua constraints inline: ">= 5 rows", "booleans only", "Source URL required" -->

## Phase 3: VALIDATE
<!-- NOTA: Fase de validacao. Estrutura UNIVERSAL: -->
1. {{validation_tool_instruction}}
<!-- NOTA: Se validator existe (validate_kc.py para KC): "Run: python _tools/validate_kc.py <file>" -->
<!-- NOTA: Se validator planejado: "Check QUALITY_GATES.md manually" -->
2. HARD gates (all must pass): {{hard_gate_summary}}
3. SOFT gates: check each against QUALITY_GATES.md
4. Cross-check: {{cross_check_items}}
5. If score < 8.0: revise in same pass before outputting
<!-- NOTA: {{cross_check_items}} = verificacoes finais especificas do tipo -->
<!-- Ex model_card: "every Spec row has URL?" -->
<!-- Ex KC: "density >= 0.80? No filler?" -->
<!-- Ex signal: "still atomic? not drifting into handoff?" -->

### bld_knowledge_card_builder.md
---
kind: knowledge_card
id: bld_knowledge_card_builder
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for meta-builder construction — building builders themselves
sources: CEX archetype system, builder pattern literature, meta-programming patterns
---

# Domain Knowledge: _builder (meta)

## Executive Summary

The meta-builder is the factory that produces other builders. It operates one abstraction level above regular builders: while a knowledge-card-builder produces knowledge_cards, the _builder-builder produces the builders themselves. Every builder in the system was either directly generated or validated against the meta-builder's templates and quality gates.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P02 (agent/builder identity) |
| Output kind | type_builder (any) |
| Required files per builder | MANIFEST, SYSTEM_PROMPT, KNOWLEDGE, INSTRUCTIONS, SCHEMA, EXAMPLES, QUALITY_GATES, CONFIG, ARCHITECTURE, TOOLS, OUTPUT_TEMPLATE, MEMORY, COLLABORATION |
| Meta-file prefix | META_ (e.g., META_MANIFEST.md) |
| llm_function | BECOME (builders assume specialist identity) |
| Naming | {type_name}-builder (kebab-case) |
| Min builder files | 7 (MANIFEST + SYSTEM_PROMPT + KNOWLEDGE + INSTRUCTIONS + SCHEMA + EXAMPLES + QUALITY_GATES) |
| Max builder files | 13 (full complement) |

## Patterns

- **Template-driven generation**: META_ files are fill-in templates with {{variables}} that produce concrete builder files when instantiated with a target type's schema
- **Schema-first**: always read the target type's _schema.yaml before writing any builder file — the schema is the single source of truth for fields, constraints, and validation
- **Capability extraction**: derive builder capabilities directly from the target schema's field count, required fields, and validation rules
- **Boundary mapping**: every builder must explicitly name 3-5 sibling types it does NOT handle, sourced from the same pillar's taxonomy
- **Routing keywords**: 4-8 terms that a user would literally type when searching for this builder via semantic search
- **Crew role pattern**: one question the builder answers + explicit exclusion list

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Generic capabilities ("can help with anything") | No routing signal; brain search returns noise |
| Missing boundary section | Builders overlap, producing wrong artifact types |
| Copy-paste from another builder | Domain knowledge is wrong; validation gates don't match |
| Skipping schema read | Field counts, constraints, and validation rules drift from truth |
| Over-scoping (>8 capabilities) | Builder tries to do too much; split into two builders |

## Application

1. Read META_MANIFEST.md template and target type's _schema.yaml
2. Instantiate each META_ file by replacing {{variables}} with concrete values
3. Validate: field counts match schema, boundary types are real siblings, routing keywords are specific
4. Quality gate: all 13 files present, no template residue ({{...}}), density >= 0.80

## References

- CEX archetype system: archetypes/builders/_builder-builder/META_*.md (13 templates)
- Builder pattern: Gang of Four, applied to LLM artifact production
- Meta-programming: code that writes code, adapted to prompt-driven artifact systems

### bld_meta_knowledge_builder.md
---
kind: meta_knowledge
id: bld_meta_knowledge_builder
meta: true
file_position: 3/13
pillar: P01
llm_function: INJECT
purpose: Meta-template for generating KNOWLEDGE.md of any kind-builder
---

# Domain Knowledge: {{type_name}}
<!-- Este meta-file gera o KNOWLEDGE.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml do tipo-alvo, TAXONOMY_LAYERS.yaml, pesquisa de dominio -->
<!-- NOTA: Este eh o file mais variavel entre builders — requer pesquisa real -->

```yaml
---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for {{type_name}} production
sources: {{sources_used}}
---
```

## Foundational Standard/Concept
<!-- NOTA: Origem academica ou industrial do tipo -->
<!-- Padrao observado: -->
<!-- - model_card: Mitchell et al. 2019 "Model Cards for Model Reporting" -->
<!-- - knowledge_card: "Atomic searchable facts" (CEX-internal concept) -->
<!-- - signal: "Smallest coordination artifact in P12" (operational concept) -->
<!-- - quality_gate: Cooper 1990 stage-gate process -->
<!-- Se o tipo tem origem academica, cite paper + URL -->
<!-- Se o tipo eh CEX-interno, descreva o conceito fundamental -->
{{foundational_description}}

## Industry Implementations
<!-- NOTA: Tabela comparando implementacoes do conceito em ferramentas reais -->
<!-- Padrao: Source | What it defines | CEX uses -->
<!-- Se nao ha equivalente industrial direto: omitir ou adaptar como "Related Patterns" -->

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| {{source_1}} | {{what_1}} | {{cex_use_1}} |
| {{source_2}} | {{what_2}} | {{cex_use_2}} |
| {{source_3}} | {{what_3}} | {{cex_use_3}} |

## Key Patterns
<!-- NOTA: 5-8 patterns/principles que governam a producao deste tipo -->
<!-- Extrair de _schema.yaml constraints + experiencia do dominio -->
<!-- Padrao: bullet list com padroes concretos e actionable -->
- {{pattern_1}}
- {{pattern_2}}
- {{pattern_3}}

## CEX-Specific Extensions
<!-- NOTA: Campos ou regras que o CEX adiciona alem do padrao industrial -->
<!-- Padrao: tabela Field | Justification | Closest industry equivalent -->
<!-- Se todos os campos sao padrao industrial: omitir esta secao -->

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| {{field_1}} | {{why_1}} | {{equivalent_1}} |

## Boundary vs Nearby Types
<!-- NOTA: Tabela distinguindo este tipo dos vizinhos confusos -->
<!-- Padrao identico em TODOS os 4 builders existentes -->
<!-- Buscar overlaps em TAXONOMY_LAYERS.yaml -->

| Type | What it is | Why it is NOT {{type_name}} |
|------|------------|---------------------------|
| {{confused_type_1}} | {{what_it_is}} | {{why_different}} |
| {{confused_type_2}} | {{what_it_is}} | {{why_different}} |

## References
<!-- NOTA: URLs de fontes oficiais, papers, documentacao -->
- {{reference_1}}
- {{reference_2}}

### bld_meta_quality_gates_builder.md
---
kind: meta_quality_gates
id: bld_meta_quality_gates_builder
meta: true
file_position: 12/13
pillar: P11
llm_function: GOVERN
purpose: Meta-template for generating QUALITY_GATES.md of any kind-builder
---

# Quality Gates: {{type_name}}
<!-- Este meta-file gera o QUALITY_GATES.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md ja gerado (gates validam o schema) -->
<!-- NOTA: HARD gates derivam dos campos required. SOFT gates derivam de qualidade. -->

```yaml
---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for {{type_name}} validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---
```

## HARD Gates (block publish if ANY fails)
<!-- NOTA: GERAR a partir de SCHEMA.md Required Fields + Constraints -->
<!-- HARD GATES UNIVERSAIS (presentes em TODOS os 4 builders): -->

| Gate | Check | Why |
|------|-------|-----|
| H01 | {{format_parses}} | Broken {{format}} = broken artifact |
| H02 | id matches `{{id_pattern}}` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "{{type_name}}" | Type integrity |
| H05 | {{quality_gate}} | Never self-score |
| H06 | {{required_fields_check}} | Completeness |
<!-- NOTA: H01-H06 sao UNIVERSAIS (adaptar formato): -->
<!-- H01: "YAML frontmatter parses" (md) ou "JSON payload parses" (json) -->
<!-- H05: "quality == null" (md) ou "quality_score is numeric" (json/signal) -->
<!-- H06: "N required fields present" ou "core fields present" -->

<!-- HARD GATES ESPECIFICOS DO TIPO: -->
| H07 | {{hard_specific_1}} | {{why_1}} |
| H08 | {{hard_specific_2}} | {{why_2}} |
| H09 | {{hard_specific_3}} | {{why_3}} |
| H10 | {{hard_specific_4}} | {{why_4}} |
<!-- NOTA: Adicionar 2-5 gates especificos baseados em: -->
<!-- - Campos com constraints fortes (enums, ranges, formats) -->
<!-- - Boundary violations (drift para outro tipo) -->
<!-- - Padroes de erros comuns do dominio -->
<!-- Exemplos observados: -->
<!-- - model_card: provider in enum, context_window is integer, max_output is integer -->
<!-- - KC: tags is list, body 200-5120 bytes, no internal paths, author != orchestrator -->
<!-- - signal: status in enum, quality_score in range, no instruction fields, no routing fields -->
<!-- - quality_gate: scoring weights sum to 100%, Definition has numeric threshold -->

## SOFT Gates (contribute to score)
<!-- NOTA: GERAR a partir de SCHEMA.md Constraints + qualidade desejada -->
<!-- SOFT GATES UNIVERSAIS: -->

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3 | 0.5 | 10 |
<!-- NOTA: S01-S02 presentes na maioria dos tipos md -->

<!-- SOFT GATES ESPECIFICOS DO TIPO: -->
| S03 | {{soft_specific_1}} | {{weight}} | 10 |
| S04 | {{soft_specific_2}} | {{weight}} | 10 |
<!-- NOTA: Adicionar 5-18 gates baseados em: -->
<!-- - Secoes de body (cada secao obrigatoria = 1 gate) -->
<!-- - Formatacao (tabelas, code blocks, URLs, bullets) -->
<!-- - Densidade (>= 0.80 ou >= 0.85) -->
<!-- - Filler detection (no "this document", "in summary") -->
<!-- - Cross-references (linked_artifacts, data_source) -->
<!-- - Type-specific checks (pricing consistency, boolean fields, etc.) -->
<!-- Padroes de contagem observados: -->
<!-- - model_card: 15 SOFT gates (weights 0.5-1.0) -->
<!-- - KC: 20 SOFT gates (all weight 1.0) -->
<!-- - signal: 9 SOFT gates (weights 0.5-1.0) -->
<!-- - quality_gate: 7 SOFT gates (weights 0.5-1.0) -->

## Scoring Formula
<!-- NOTA: Formula UNIVERSAL (identica em todos os 4 builders): -->
```text
hard_pass = all {{hard_count}} HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```
<!-- NOTA: Thresholds sao UNIVERSAIS. Nao alterar. -->
<!-- Variacao possivel: KC adiciona ACCEPTABLE e NEEDS_WORK entre REVIEW e REJECT -->

## Automation
<!-- NOTA: Indicar estado do validador automatico -->
Primary: {{validation_command}}
<!-- Se validador existe: "python _tools/validate_kc.py <file>" -->
<!-- Se planejado: "validate_artifact.py --kind {{type_name}} [PLANNED]" -->
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
<!-- NOTA: 3-5 items de verificacao ANTES de comecar a produzir -->
- [ ] {{pre_check_1}}
- [ ] {{pre_check_2}}
- [ ] {{pre_check_3}}
<!-- Exemplos observados: -->
<!-- - model_card: "Official provider docs accessible", "No existing card for this model" -->
<!-- - KC: "Topic identified, not duplicate", "Sources gathered with URLs" -->
<!-- - signal: "filename uses p12_sig_ prefix", "no handoff drift" -->
<!-- - quality_gate: (nao tem; recomendado adicionar) -->

### bld_quality_gate_builder.md
---
id: p11_qg_builder
kind: quality_gate
pillar: P11
title: "Gate: builder"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: type_builder
quality: null
tags: [quality-gate, type-builder, builder-builder, P11, governance]
tldr: "Gates for type_builder artifacts — meta-builders that specialize in producing one kind."
density_score: 0.88
---

# Gate: builder

## Definition

| Field     | Value                                      |
|-----------|--------------------------------------------|
| metric    | structural completeness + domain specificity |
| threshold | 8.0                                        |
| operator  | >=                                         |
| scope     | all type_builder artifacts                 |

## HARD Gates

All must pass. Failure on any = final score 0.

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = broken builder |
| H02 | id matches `^[a-z][a-z0-9-]+-builder$` | Namespace compliance for builders |
| H03 | id == filename stem | Discovery relies on exact match |
| H04 | kind == "type_builder" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, domain, llm_function, version, created, updated, author, tags | Completeness |
| H07 | llm_function == "BECOME" | Builders adopt identity, never CALL or GOVERN |
| H08 | domain maps to a known kind in TAXONOMY_LAYERS.yaml | Builder must target a real kind |
| H09 | MANIFEST has Identity, Capabilities, Routing, Crew Role sections | Structure compliance |
| H10 | Crew Role includes at least one "I do NOT handle" exclusion | Boundary definition required |

## SOFT Scoring

| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, no filler | 1.0 |
| S02 | tags is list, len >= 3, includes "kind-builder" | 0.5 |
| S03 | Identity section explains what the builder produces in one tight sentence | 1.0 |
| S04 | Capabilities list has 4-6 bullets, each starts with verb | 1.0 |
| S05 | Routing keywords has >= 4 domain-specific terms | 1.0 |
| S06 | Routing triggers has >= 2 natural-language phrases | 0.5 |
| S07 | Crew Role names ROLE_CAPS (uppercase descriptor) | 0.5 |
| S08 | Crew Role answer is a single focused question | 1.0 |
| S09 | Exclusions cite specific neighboring kinds (not vague) | 1.0 |
| S10 | density_score >= 0.80 | 0.5 |
| S11 | No framework-internal jargon in user-facing fields | 1.0 |
| S12 | Capabilities reference field count or gate count from schema | 0.5 |

Weights sum: 9.5. Normalize: divide each by 9.5 before scoring.

## Actions

| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference builder |
| >= 8.0 | PUBLISH — ready for routing index |
| >= 7.0 | REVIEW — fix weakest SOFT gates before publish |
| < 7.0  | REJECT — rework Identity + Capabilities |

## Bypass

| Field | Value |
|-------|-------|
| conditions | Emergency gap-fill when no builder exists for a critical kind |
| approver | p11-chief |
| audit_trail | Log bypass reason in records/audits/ with timestamp |
| expiry | 72h — full gate pass required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

### bld_meta_schema_builder.md
---
kind: meta_schema
id: bld_meta_schema_builder
meta: true
file_position: 7/13
pillar: P06
llm_function: CONSTRAIN
purpose: Meta-template for generating SCHEMA.md of any kind-builder
---

# Schema: {{type_name}}
<!-- Este meta-file gera o SCHEMA.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml do Pillar-alvo (fonte primaria de campos) -->
<!-- REGRA: Este file eh SINGLE SOURCE OF TRUTH. TEMPLATE deriva. CONFIG restringe. -->

```yaml
---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for {{type_name}} — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---
```

## Frontmatter Fields
<!-- NOTA: GERAR esta tabela a partir de _schema.yaml -->
<!-- Separar em Required e Extended/Recommended -->
<!-- Padrao observado: -->
<!-- - model_card: 26 campos (muitos required) -->
<!-- - knowledge_card: 13 required + 6 extended = 19 -->
<!-- - quality_gate: ~13 campos -->
<!-- - signal: 4 required + 7 optional (JSON, sem frontmatter) -->

<!-- CAMPOS UNIVERSAIS (presentes em TODO tipo md): -->

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string ({{id_pattern}}) | YES | - | {{id_format_description}} |
| kind | literal "{{type_name}}" | YES | - | Type integrity |
| lp | literal "{{lp}}" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
<!-- NOTA: Alguns tipos adicionam restricao: "not STELLA" (KC H10) -->

<!-- CAMPOS ESPECIFICOS DO TIPO (gerar de _schema.yaml): -->
| {{field_name}} | {{field_type}} | {{YES/REC}} | {{default}} | {{notes}} |
<!-- NOTA: Para cada campo em _schema.yaml que nao seja universal: -->
<!-- - Determinar tipo (string, integer, boolean, enum, object, list) -->
<!-- - Determinar se required (YES) ou recommended (REC) -->
<!-- - Anotar constraints (min/max length, allowed values, regex) -->
<!-- - Referenciar fonte (Mitchell 2019, LiteLLM, CEX-internal, etc.) -->

<!-- CAMPOS UNIVERSAIS CEX (presentes na maioria dos tipos): -->
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Searchability |
| tldr | string <= 160ch | YES | - | Dense summary |

<!-- CAMPOS OPCIONAIS CEX (presentes em muitos tipos): -->
| keywords | list[string] | REC | - | Brain search terms |
| linked_artifacts | object {primary, related} | REC | - | Cross-references |
| data_source | URL or artifact ref | REC | - | Provenance |
| density_score | float 0.80-1.00 | REC | - | Content density |

## {{Complex_Object_Section}}
<!-- NOTA: Se o tipo tem objetos complexos no frontmatter, documentar aqui -->
<!-- Exemplos: -->
<!-- - model_card: Pricing Policy, Modalities Object, Features Object -->
<!-- - knowledge_card: Linked Artifacts Object -->
<!-- - signal: nenhum (campos simples) -->
<!-- - quality_gate: nenhum (campos simples) -->

```yaml
{{object_name}}:
  {{field_1}}: {{kind}}
  {{field_2}}: {{kind}}
```
<!-- NOTA: Incluir regras de preenchimento (ex: "open-weight = null, not 0") -->

## ID Pattern
<!-- NOTA: Regex de validacao do id -->
Regex: `{{id_regex}}`
Rule: id MUST equal filename stem.
<!-- Exemplos de padroes observados: -->
<!-- - model_card: ^p02_mc_[a-z][a-z0-9_]+$ -->
<!-- - knowledge_card: ^p01_kc_[a-z][a-z0-9_]+$ -->
<!-- - signal: p12_sig_{event} -->
<!-- - quality_gate: p11_qg_{slug} -->
<!-- Padrao universal: ^{{lp_lower}}_{{type_abbrev}}_[a-z][a-z0-9_]+$ -->

## Body Structure (required sections)
<!-- NOTA: Listar secoes obrigatorias do body -->
<!-- GERAR a partir de _schema.yaml ou convencoes do dominio -->
1. `## {{section_1}}` — {{section_1_description}}
2. `## {{section_2}}` — {{section_2_description}}
3. `## {{section_3}}` — {{section_3_description}}
<!-- NOTA: Numero de secoes varia: -->
<!-- - model_card: 5 secoes fixas -->
<!-- - knowledge_card: 7 (domain_kc) ou 6 (meta_kc) — 2 variantes -->
<!-- - signal: 0 (JSON puro) -->
<!-- - quality_gate: 5 secoes fixas -->
<!-- Se o tipo tem variantes de body, documentar todas -->

## Constraints
<!-- NOTA: Restricoes operacionais derivadas do schema -->
- max_bytes: {{max_body_bytes}}
<!-- Padroes observados: model_card=4096, KC=5120 (min 200), signal=4096, QG=4096 -->
- naming: {{naming_pattern}}
- id == filename stem
<!-- CONSTRAINTS ESPECIFICOS (gerar de _schema.yaml): -->
- {{constraint_1}}
- {{constraint_2}}
<!-- Exemplos: -->
<!-- - KC: "no internal paths (records/, .claude/, /home/)" -->
<!-- - KC: "bullet max 80 chars" -->
<!-- - model_card: "every Spec row MUST have Source URL" -->
<!-- - signal: "payload contains no instruction fields" -->
<!-- - quality_gate: "scoring weights MUST sum to 100%" -->

### bld_meta_examples_builder.md
---
kind: meta_examples
id: bld_meta_examples_builder
meta: true
file_position: 8/13
pillar: P07
llm_function: GOVERN
purpose: Meta-template for generating EXAMPLES.md of any kind-builder
---

# Examples: {{builder_name}}
<!-- Este meta-file gera o EXAMPLES.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md + OUTPUT_TEMPLATE.md + QUALITY_GATES.md ja gerados -->
<!-- INPUT RECOMENDADO: exemplos reais do tipo se existirem em {{lp_dir}}/examples/ -->

```yaml
---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of {{type_name}} artifacts
pattern: few-shot learning — LLM reads these before producing
---
```

## Golden Example

INPUT: "{{natural_language_request}}"
<!-- NOTA: {{natural_language_request}} = frase que um user diria para pedir este tipo -->
<!-- Exemplos observados: -->
<!-- - model_card: "Documenta o Claude Sonnet 4 pra decidir roteamento" -->
<!-- - KC: "Destila conhecimento sobre prompt caching para otimizar custos LLM" -->
<!-- - signal: "Emit completion signal for codex after finishing signal-builder" -->
<!-- - quality_gate: "Define gate pra knowledge_cards antes de publicar no pool" -->

OUTPUT:
<!-- NOTA: Produzir um artifact COMPLETO usando OUTPUT_TEMPLATE.md -->
<!-- O exemplo DEVE passar TODOS os HARD gates e >= 95% dos SOFT gates -->
<!-- Usar dados REAIS (nao inventados) sempre que possivel -->

```{{machine_format}}
{{complete_artifact_following_output_template}}
```
<!-- NOTA: {{machine_format}} = yaml (para md kinds) ou json (para signal) -->
<!-- Preencher TODOS os campos do template com valores concretos -->
<!-- Incluir body completo com todas as secoes obrigatorias -->

WHY THIS IS GOLDEN:
<!-- NOTA: Listar 6-10 razoes mapeadas para gates especificos -->
<!-- Padrao UNIVERSAL observado em todos os 4 builders: -->
- quality: null ({{hard_gate_quality}} pass)
- id matches {{id_prefix}} pattern ({{hard_gate_id}} pass)
- kind: {{type_name}} ({{hard_gate_type}} pass)
- {{required_fields_count}} required fields present ({{hard_gate_fields}} pass)
- {{soft_gate_check_1}} ({{soft_gate_id_1}} pass)
- {{soft_gate_check_2}} ({{soft_gate_id_2}} pass)
<!-- NOTA: Referenciar gate IDs (H01, S03, etc.) de QUALITY_GATES.md -->

## Anti-Example

INPUT: "{{simple_request}}"

BAD OUTPUT:
```{{machine_format}}
{{deliberately_bad_artifact}}
```
<!-- NOTA: Incluir 6-10 erros comuns para este tipo -->
<!-- Padrao UNIVERSAL observado: -->
<!-- 1. id sem prefixo correto -->
<!-- 2. lp ausente -->
<!-- 3. quality com valor (nao null) -->
<!-- 4. tipo do campo errado (string vs integer, string vs list) -->
<!-- 5. body com filler/prose ao inves de dados concretos -->
<!-- 6. secoes obrigatorias ausentes -->

FAILURES:
<!-- NOTA: Lista numerada com gate ID e descricao da falha -->
1. id: no `{{id_prefix}}` prefix -> {{hard_gate_id}} FAIL
2. lp: missing -> {{hard_gate_lp}} FAIL
3. quality: self-assigned -> {{hard_gate_quality}} FAIL
4. {{failure_4}} -> {{gate_4}} FAIL
5. {{failure_5}} -> {{gate_5}} FAIL
6. {{failure_6}} -> {{gate_6}} FAIL
<!-- NOTA: Mapear CADA falha para o gate exato (H01-H10, S01-S20) -->
<!-- Incluir falhas tanto HARD (bloqueiam) quanto SOFT (reduzem score) -->


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `_builder-builder` for pipeline function `BECOME`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
