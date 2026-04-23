---
kind: meta_schema
id: bld_meta_schema_builder
meta: true
file_position: 7/13
pillar: P06
llm_function: CONSTRAIN
purpose: Meta-template for generating SCHEMA.md of any kind-builder
quality: 9.0
title: "Meta Schema Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_input_schema
  - bld_schema_validation_schema
  - bld_schema_unit_eval
  - bld_schema_golden_test
  - bld_schema_retriever_config
  - bld_schema_smoke_eval
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_reranker_config
---

# Schema: {{type_name}}
<!-- This meta-file generates the SCHEMA.md of any builder -->
<!-- REQUIRED INPUT: _schema.yaml do Pillar-target (fonte primaria de fields) -->
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
<!-- NOTE: GERAR esta tabela a partir de _schema.yaml -->
<!-- Separar em Required e Extended/Recommended -->
<!-- Padrao observado: -->
<!-- - model_card: 26 fields (muitos required) -->
<!-- - knowledge_card: 13 required + 6 extended = 19 -->
<!-- - quality_gate: ~13 fields -->
<!-- - signal: 4 required + 7 optional (JSON, sem frontmatter) -->

<!-- CAMPOS UNIVERSAIS (presentes em TODO type md): -->

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string ({{id_pattern}}) | YES | - | {{id_format_description}} |
| kind | literal "{{type_name}}" | YES | - | Type integrity |
| lp | literal "{{lp}}" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
<!-- NOTE: Alguns types adicionam restriction: "not orchestrator" (KC H10) -->

<!-- CAMPOS ESPECIFICOS DO TIPO (gerar de _schema.yaml): -->
| {{field_name}} | {{field_type}} | {{YES/REC}} | {{default}} | {{notes}} |
<!-- NOTE: Para each field em _schema.yaml que nao seja universal: -->
<!-- - Determinar type (string, integer, boolean, enum, object, list) -->
<!-- - Determinar se required (YES) ou recommended (REC) -->
<!-- - Anotar constraints (min/max length, allowed values, regex) -->
<!-- - Referencesr fonte (Mitchell 2019, LiteLLM, CEX-internal, etc.) -->

<!-- CAMPOS UNIVERSAIS CEX (presentes na maioria dos types): -->
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Searchability |
| tldr | string <= 160ch | YES | - | Dense summary |

<!-- CAMPOS OPCIONAIS CEX (presentes em muitos types): -->
| keywords | list[string] | REC | - | Brain search terms |
| linked_artifacts | object {primary, related} | REC | - | Cross-references |
| data_source | URL or artifact ref | REC | - | Provenance |
| density_score | float 0.80-1.00 | REC | - | Content density |

## {{Complex_Object_Section}}
<!-- NOTE: Se o type tem objetos complex no frontmatter, documentar aqui -->
<!-- Exemplos: -->
<!-- - model_card: Pricing Policy, Modalities Object, Features Object -->
<!-- - knowledge_card: Linked Artifacts Object -->
<!-- - signal: nenhum (fields simples) -->
<!-- - quality_gate: nenhum (fields simples) -->

```yaml
{{object_name}}:
  {{field_1}}: {{kind}}
  {{field_2}}: {{kind}}
```
<!-- NOTE: Incluir rules de preenchimento (ex: "open-weight = null, not 0") -->

## ID Pattern
<!-- NOTE: Regex de validation do id -->
Regex: `{{id_regex}}`
Rule: id MUST equal filename stem.
<!-- Exemplos de padroes observados: -->
<!-- - model_card: ^p02_mc_[a-z][a-z0-9_]+$ -->
<!-- - knowledge_card: ^p01_kc_[a-z][a-z0-9_]+$ -->
<!-- - signal: p12_sig_{event} -->
<!-- - quality_gate: p11_qg_{slug} -->
<!-- Padrao universal: ^{{lp_lower}}_{{type_abbrev}}_[a-z][a-z0-9_]+$ -->

## Body Structure (required sections)
<!-- NOTE: Listar sections obrigatorias do body -->
<!-- GERAR a partir de _schema.yaml ou convencoes do domain -->
1. `## {{section_1}}` — {{section_1_description}}
2. `## {{section_2}}` — {{section_2_description}}
3. `## {{section_3}}` — {{section_3_description}}
<!-- NOTE: Numero de sections varia: -->
<!-- - model_card: 5 sections fixas -->
<!-- - knowledge_card: 7 (domain_kc) ou 6 (meta_kc) — 2 variants -->
<!-- - signal: 0 (JSON puro) -->
<!-- - quality_gate: 5 sections fixas -->
<!-- Se o type tem variants de body, documentar todas -->

## Constraints
<!-- NOTE: Restricoes operational derivadas do schema -->
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_input_schema]] | related | 0.54 |
| [[bld_schema_validation_schema]] | related | 0.50 |
| [[bld_schema_unit_eval]] | related | 0.50 |
| [[bld_schema_golden_test]] | related | 0.50 |
| [[bld_schema_retriever_config]] | related | 0.49 |
| [[bld_schema_smoke_eval]] | related | 0.49 |
| [[bld_schema_memory_scope]] | related | 0.49 |
| [[bld_schema_output_validator]] | related | 0.48 |
| [[bld_schema_handoff_protocol]] | related | 0.48 |
| [[bld_schema_reranker_config]] | related | 0.48 |
