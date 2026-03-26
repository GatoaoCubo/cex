---
meta: true
file_position: 7/13
pillar: P06
llm_function: CONSTRAIN
purpose: Meta-template for generating SCHEMA.md of any type-builder
---

# Schema: {{type_name}}
<!-- Este meta-file gera o SCHEMA.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml do LP-alvo (fonte primaria de campos) -->
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
| type | literal "{{type_name}}" | YES | - | Type integrity |
| lp | literal "{{lp}}" | YES | - | LP assignment |
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
  {{field_1}}: {{type}}
  {{field_2}}: {{type}}
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
