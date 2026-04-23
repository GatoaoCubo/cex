---
kind: meta_architecture
id: bld_meta_architecture_builder
meta: true
file_position: 9/13
pillar: P08
llm_function: CONSTRAIN
purpose: Meta-template for generating ARCHITECTURE.md of any kind-builder
quality: 9.1
title: "Meta Architecture Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_meta_manifest_builder
  - bld_meta_instructions_builder
  - bld_meta_collaboration_builder
  - bld_meta_system_prompt_builder
  - bld_meta_examples_builder
  - bld_meta_knowledge_builder
  - bld_meta_quality_gates_builder
  - bld_meta_config_builder
  - bld_meta_schema_builder
  - bld_meta_tools_builder
---

# Architecture: {{type_name}} in the CEX
<!-- This meta-file generates the ARCHITECTURE.md of any builder -->
<!-- REQUIRED INPUT: TAXONOMY_LAYERS.yaml (posicao + overlaps), _schema.yaml -->

```yaml
---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of {{type_name}} in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---
```

## Boundary
{{type_name}} IS: {{boundary_is_description}}.
<!-- NOTE: {{boundary_is_description}} = o that o type EH em uma frase dense -->
<!-- Exemplos observados: -->
<!-- - model_card: "spec tecnica de LLM (capacidades, costs, limits, status lifecycle)" -->
<!-- - KC: "atomic fact destilado, searchable, versionado, with density >= 0.80" -->
<!-- - signal: "evento runtime atomic emitido per um agent_group for informar status" -->
<!-- - quality_gate: "barrier of quality with score numerico (pass/fail + weighted dimensions)" -->

{{type_name}} IS NOT:

| Confusion | Por that NAO | Type correct |
|----------|-------------|-------------|
| {{confused_type_1}} | {{why_not_1}} | {{correct_lp}} {{correct_type_1}} |
| {{confused_type_2}} | {{why_not_2}} | {{correct_lp}} {{correct_type_2}} |
| {{confused_type_3}} | {{why_not_3}} | {{correct_lp}} {{correct_type_3}} |
<!-- NOTE: 3-5 confused types. Look up in: -->
<!-- 1. TAXONOMY_LAYERS.yaml overlaps (pares with severity high/medium) -->
<!-- 2. Tipos no MESMO Pillar (compartilham namespace) -->
<!-- 3. Tipos with names similares em OUTROS LPs -->
<!-- Padrao da frase "Por that NAO": "{confused} VERBO. {type_name} VERBO_DIFERENTE." -->

Regra: "{{decision_question}}" -> {{type_name}}.
<!-- NOTE: {{decision_question}} = pergunta that se respondida "sim" => usar this type -->
<!-- Exemplos: -->
<!-- - model_card: "o that this LLM PODE e quanto CUSTA?" -->
<!-- - KC: "qual o fact essencial about this topico?" -->
<!-- - signal: "o that aconteceu agora?" -->
<!-- - quality_gate: "o that deve passar antes de publicar?" -->

## Position in {{flow_name}}
<!-- NOTE: Diagrama ASCII mostrando where o type se encaixa no fluxo -->
<!-- {{flow_name}} varia: "Boot Flow", "Knowledge Flow", "Runtime Flow", etc. -->

```text
{{flow_diagram}}
```
<!-- NOTE: Diagram with arrows showing stages: -->
<!-- - model_card: boot_config -> model_card (layer 0) -> system_prompt -> agent -->
<!-- - KC: Raw Source -> Research -> KC -> Brain Index -> Retrieval -> Agent -->
<!-- - signal: dispatch_rule -> handoff -> execution -> signal -> monitor -->
<!-- - quality_gate: artifact produced -> quality_gate check -> publish/reject -->
<!-- Indicate WHERE in this flow the type is positioned -->

{{type_name}} is {{layer_description}}.
<!-- NOTE: Layer description: "INFRASTRUCTURE", "CONTENT LAYER", etc. -->

## Dependency Graph

```text
{{type_name}} <--{{rel_1}}-- {{dependent_1}} ({{why_1}})
{{type_name}} <--{{rel_2}}-- {{dependent_2}} ({{why_2}})
{{type_name}} --independent-- {{independent_types}}
```
<!-- NOTE: Tipos de relaction observados: -->
<!-- used_by, queried_by, injected_in, referenced_by, consumed_by -->
<!-- implements, uses_criteria, triggers, emitted_after, may_trigger -->
<!-- Buscar dependencies em TAXONOMY_LAYERS.yaml e nos outros builders -->

## Fractal Position
Pillar: {{lp}} ({{lp_description}})
Function: {{llm_function_primary}}
Scale: L0 ({{scale_description}})
<!-- NOTE: {{lp_description}} = ex: "Model — who the entity IS", "Knowledge — what the entity KNOWS" -->
<!-- NOTE: {{llm_function_primary}} = function principal do type (GOVERN, INJECT, COLLABORATE, etc.) -->
<!-- NOTE: {{scale_description}} = ex: "infrastructure artifact", "content artifact", "runtime event" -->
<!-- Incluir 1 frase about o that torna this type unico no Pillar -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_meta_manifest_builder]] | upstream | 0.47 |
| [[bld_meta_instructions_builder]] | upstream | 0.38 |
| [[bld_meta_collaboration_builder]] | downstream | 0.36 |
| [[bld_meta_system_prompt_builder]] | upstream | 0.35 |
| [[bld_meta_examples_builder]] | upstream | 0.34 |
| [[bld_meta_knowledge_builder]] | upstream | 0.34 |
| [[bld_meta_quality_gates_builder]] | downstream | 0.33 |
| [[bld_meta_config_builder]] | downstream | 0.33 |
| [[bld_meta_schema_builder]] | upstream | 0.32 |
| [[bld_meta_tools_builder]] | upstream | 0.31 |
