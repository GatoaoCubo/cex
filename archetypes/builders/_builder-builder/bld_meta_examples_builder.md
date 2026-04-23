---
kind: meta_examples
id: bld_meta_examples_builder
meta: true
file_position: 8/13
pillar: P07
llm_function: GOVERN
purpose: Meta-template for generating EXAMPLES.md of any kind-builder
quality: 9.1
title: "Meta Examples Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_meta_quality_gates_builder
  - bld_meta_manifest_builder
  - bld_meta_instructions_builder
  - bld_meta_collaboration_builder
  - bld_meta_output_template_builder
  - bld_meta_config_builder
  - bld_meta_memory_builder
  - bld_meta_architecture_builder
  - bld_meta_system_prompt_builder
  - bld_meta_tools_builder
---

# Examples: {{builder_name}}
<!-- This meta-file generates the EXAMPLES.md of any builder -->
<!-- REQUIRED INPUT: SCHEMA.md + OUTPUT_TEMPLATE.md + QUALITY_GATES.md ja gerados -->
<!-- INPUT RECOMENDADO: examples reais do type se existirem em {{lp_dir}}/examples/ -->

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
<!-- NOTE: {{natural_language_request}} = frase that um user diria for pedir this type -->
<!-- Exemplos observados: -->
<!-- - model_card: "Documenta o Claude Sonnet 4 for decidir routing" -->
<!-- - KC: "Destila knowledge about prompt caching for optimize costs LLM" -->
<!-- - signal: "Emit completion signal for codex after finishing signal-builder" -->
<!-- - quality_gate: "Define gate for knowledge_cards antes de publicar no pool" -->

OUTPUT:
<!-- NOTE: Produce um artifact COMPLETO usando OUTPUT_TEMPLATE.md -->
<!-- O example DEVE passar TODOS os HARD gates e >= 95% dos SOFT gates -->
<!-- Usar data REAIS (nao inventados) sempre that possivel -->

```{{machine_format}}
{{complete_artifact_following_output_template}}
```
<!-- NOTE: {{machine_format}} = yaml (para md kinds) or json (para signal) -->
<!-- Preencher TODOS os fields do template with values concrete -->
<!-- Incluir body complete with todas as sections obrigatorias -->

WHY THIS IS GOLDEN:
<!-- NOTE: Listar 6-10 razoes mapeadas for specific gates -->
<!-- Padrao UNIVERSAL observado em all os 4 builders: -->
- quality: null ({{hard_gate_quality}} pass)
- id matches {{id_prefix}} pattern ({{hard_gate_id}} pass)
- kind: {{type_name}} ({{hard_gate_type}} pass)
- {{required_fields_count}} required fields present ({{hard_gate_fields}} pass)
- {{soft_gate_check_1}} ({{soft_gate_id_1}} pass)
- {{soft_gate_check_2}} ({{soft_gate_id_2}} pass)
<!-- NOTE: Referencesr gate IDs (H01, S03, etc.) de QUALITY_GATES.md -->

## Anti-Example

INPUT: "{{simple_request}}"

BAD OUTPUT:
```{{machine_format}}
{{deliberately_bad_artifact}}
```
<!-- NOTE: Incluir 6-10 erros comuns for this type -->
<!-- Padrao UNIVERSAL observado: -->
<!-- 1. id without prefixo correct -->
<!-- 2. lp ausente -->
<!-- 3. quality with value (nao null) -->
<!-- 4. type do field errado (string vs integer, string vs list) -->
<!-- 5. body with filler/prose ao inves de data concrete -->
<!-- 6. sections obrigatorias ausentes -->

FAILURES:
<!-- NOTE: Lista numerada with gate ID e description da fails -->
1. id: no `{{id_prefix}}` prefix -> {{hard_gate_id}} FAIL
2. lp: missing -> {{hard_gate_lp}} FAIL
3. quality: self-assigned -> {{hard_gate_quality}} FAIL
4. {{failure_4}} -> {{gate_4}} FAIL
5. {{failure_5}} -> {{gate_5}} FAIL
6. {{failure_6}} -> {{gate_6}} FAIL
<!-- NOTE: Map CADA fails for o gate exato (H01-H10, S01-S20) -->
<!-- Incluir failss tanto HARD (bloqueiam) quanto SOFT (reduzem score) -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_meta_quality_gates_builder]] | downstream | 0.37 |
| [[bld_meta_manifest_builder]] | upstream | 0.32 |
| [[bld_meta_instructions_builder]] | upstream | 0.32 |
| [[bld_meta_collaboration_builder]] | downstream | 0.31 |
| [[bld_meta_output_template_builder]] | upstream | 0.30 |
| [[bld_meta_config_builder]] | downstream | 0.30 |
| [[bld_meta_memory_builder]] | downstream | 0.29 |
| [[bld_meta_architecture_builder]] | downstream | 0.29 |
| [[bld_meta_system_prompt_builder]] | upstream | 0.29 |
| [[bld_meta_tools_builder]] | upstream | 0.29 |
