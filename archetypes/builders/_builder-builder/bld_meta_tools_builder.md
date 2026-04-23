---
kind: meta_tools
id: bld_meta_tools_builder
meta: true
file_position: 5/13
pillar: P04
llm_function: CALL
purpose: Meta-template for generating TOOLS.md of any kind-builder
quality: 9.0
title: "Meta Tools Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_validation_schema
  - bld_tools_validator
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_output_validator
  - bld_tools_input_schema
  - bld_tools_response_format
  - bld_tools_golden_test
  - bld_tools_function_def
  - bld_tools_cli_tool
---

# Tools: {{builder_name}}
<!-- This meta-file generates the TOOLS.md of any builder -->
<!-- REQUIRED INPUT: _schema.yaml + existing validator type -->

```yaml
---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for {{type_name}} production
---
```

## Production Tools
<!-- NOTE: Tabela UNIVERSAL presente em todos os 4 builders -->
<!-- TOOLS UNIVERSAIS (incluir em todo builder): -->

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing {{type_name}}s in pool | Phase 1 (check duplicates) | ACTIVE |
| {{validator_name}} | {{validator_purpose}} | Phase 3 | {{ACTIVE_or_PLANNED}} |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

<!-- NOTE: {{validator_name}} = validatar specific se existir -->
<!-- - knowledge_card: validate_kc.py (ACTIVE) -->
<!-- - model_card: validate_artifact.py [PLANNED] -->
<!-- - signal: nenhum specific (manual) -->
<!-- - quality_gate: nenhum specific (manual) -->
<!-- NOTE: Adicione tools specific do domain se existirem -->

## Data Sources
<!-- NOTE: Tabela de fontes de data para producao -->
<!-- Varia muito por type: -->
<!-- - model_card: APIs de providers (Anthropic, OpenAI, Google, LiteLLM, HuggingFace) -->
<!-- - knowledge_card: CEX Schema, CEX Examples, CEX Pool -->
<!-- - signal: signal_writer.py, spawn_monitor.ps1, P12 schema -->
<!-- - quality_gate: existing gates, validate_kc.py reference -->

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | {{lp_dir}}/_schema.yaml | Field definitions |
| CEX Examples | {{lp_dir}}/examples/ | Real artifacts |
| {{source_1}} | {{path_1}} | {{data_1}} |
| {{source_2}} | {{path_2}} | {{data_2}} |

<!-- NOTE: {{lp_dir}} = P01_knowledge, P02_model, P11_feedback, P12_orchestration, etc. -->

## Tool Permissions
<!-- NOTE: REQUIRED section in every bld_tools. DENIED > ALLOWED on conflict -->

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | {{allowed_tools_list}} | Explicitly permitted |
| DENIED | {{denied_tools_list}} | Explicitly blocked |
| EFFECTIVE | {{effective_tools_list}} | ALLOWED minus DENIED |

<!-- NOTE: ALLOWED = tools the builder can use -->
<!-- NOTE: DENIED = tools blocked (from bld_config.disallowed_tools) -->
<!-- NOTE: EFFECTIVE = final result. DENIED always wins on conflict -->
<!-- NOTE: If disallowed_tools = [], then DENIED = empty and EFFECTIVE = ALLOWED -->

## Interim Validation
<!-- NOTE: Fallback when the automatic validator does not exist -->
<!-- UNIVERSAL pattern: -->
{{interim_validation_text}}
<!-- Se validatar ACTIVE: "Run {validator} before committing. No manual checking needed." -->
<!-- Se validatar PLANNED: "Manually check each QUALITY_GATES.md gate against produced artifact." -->
<!-- Incluir checklist minimal para validation manual -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_validation_schema]] | related | 0.44 |
| [[bld_tools_validator]] | related | 0.41 |
| [[bld_tools_retriever_config]] | related | 0.40 |
| [[bld_tools_memory_scope]] | related | 0.40 |
| [[bld_tools_output_validator]] | related | 0.40 |
| [[bld_tools_input_schema]] | related | 0.40 |
| [[bld_tools_response_format]] | related | 0.39 |
| [[bld_tools_golden_test]] | related | 0.39 |
| [[bld_tools_function_def]] | related | 0.39 |
| [[bld_tools_cli_tool]] | related | 0.39 |
