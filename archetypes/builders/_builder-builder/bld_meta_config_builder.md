---
kind: meta_config
id: bld_meta_config_builder
meta: true
file_position: 10/13
pillar: P09
llm_function: CONSTRAIN
purpose: Meta-template for generating CONFIG.md of any kind-builder
quality: 9.1
title: "Meta Config Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_meta_schema_builder
  - bld_meta_tools_builder
  - bld_meta_manifest_builder
  - bld_meta_instructions_builder
  - bld_meta_collaboration_builder
  - bld_meta_quality_gates_builder
  - bld_meta_output_template_builder
  - bld_meta_examples_builder
  - bld_meta_system_prompt_builder
  - bld_config_model_card
---

# Config: {{type_name}} Production Rules
<!-- This meta-file generates the CONFIG.md of any builder -->
<!-- REQUIRED INPUT: SCHEMA.md ja gerado (CONFIG restringe SCHEMA) -->

```yaml
---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
```

<!-- NOTE: effort = low(haiku) | medium(sonnet) | high(opus) | max(opus+ultra) -->
<!-- NOTE: max_turns = integer 1-100, budget control per build session -->
<!-- NOTE: disallowed_tools = lista de tools NAO permitidas. [] = tudo permitido -->
<!-- NOTE: fork_context = inline | fork | null. Como the builder gerencia context -->
<!-- NOTE: hooks = lifecycle hooks. null = nenhum. Valores: script path or command -->
<!-- NOTE: permission_scope = nucleus | pillar | global | restricted -->

## Naming Convention
<!-- NOTE: Tabela UNIVERSAL presente em all os 4 builders -->

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `{{naming_pattern}}` | `{{naming_example}}` |
| Builder directory | kebab-case | `{{builder_name}}/` |
| Frontmatter fields | snake_case | `{{example_field_1}}`, `{{example_field_2}}` |
| {{scope_extra}} | {{convention_extra}} | {{example_extra}} |

<!-- NOTE: {{naming_pattern}} = id pattern with extensao -->
<!-- Padroes observados: -->
<!-- - model_card: p02_mc_{provider}_{slug}.md -->
<!-- - KC: p01_kc_{topic_slug}.md -->
<!-- - signal: p12_sig_{event}.json -->
<!-- - quality_gate: p11_qg_{slug}.md -->
<!-- Padrao universal: {lp_lower}_{type_abbrev}_{slug}.{ext} -->

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/{{lp_dir}}/examples/{{naming_pattern}}`
- Compiled: `cex/{{lp_dir}}/compiled/{{naming_compiled}}`
<!-- NOTE: {{lp_dir}} = P02_model, P01_knowledge, P12_orchestration, P11_feedback, etc. -->
<!-- {{naming_compiled}} = mesmo standard mas with extensao .yaml or .json -->

## Size Limits (aligned with SCHEMA)
<!-- NOTE: Copiar limits de SCHEMA.md Constraints -->
- Body: {{body_size_limits}}
- Total: {{total_size_limit}}
- Density: >= {{density_min}}
<!-- Padroes observados: -->
<!-- - model_card: body max 4096 bytes, total ~5300, density >= 0.85 -->
<!-- - KC: body 200-5120 bytes, total ~6500, density >= 0.80 -->
<!-- - signal: payload <= 4096 bytes (preferred <= 1024) -->
<!-- - quality_gate: body max 4096, density >= 0.80 -->

## {{Type_Specific_Constraints}}
<!-- NOTE: Restricoes that not cabem nas categorias acima -->
<!-- Exemplos observados: -->
<!-- - model_card: Provider Enum, Pricing Policy, Freshness (90 days) -->
<!-- - KC: Body Requirements (>= 4 sections, >= 3 lines each), KC Type Selection -->
<!-- - signal: Payload Restrictions, Boundary Restrictions (no instructions) -->
<!-- - quality_gate: (simples, without extras) -->
<!-- Incluir se o type tem: -->
<!-- - Enums specific (provider, status, etc.) -->
<!-- - Politicas de preenchimento (BASE TIER, null vs 0, etc.) -->
<!-- - Regras de freshness (90 days, etc.) -->
<!-- - Restricoes de body (min sections, min lines, etc.) -->
<!-- - Variantes de body structure (domain_kc vs meta_kc) -->
{{type_specific_constraint_sections}}

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_meta_schema_builder]] | upstream | 0.36 |
| [[bld_meta_tools_builder]] | upstream | 0.34 |
| [[bld_meta_manifest_builder]] | upstream | 0.34 |
| [[bld_meta_instructions_builder]] | upstream | 0.34 |
| [[bld_meta_collaboration_builder]] | downstream | 0.32 |
| [[bld_meta_quality_gates_builder]] | downstream | 0.31 |
| [[bld_meta_output_template_builder]] | upstream | 0.30 |
| [[bld_meta_examples_builder]] | upstream | 0.29 |
| [[bld_meta_system_prompt_builder]] | upstream | 0.29 |
| [[bld_config_model_card]] | related | 0.28 |
