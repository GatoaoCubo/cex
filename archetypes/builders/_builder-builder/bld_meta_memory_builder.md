---
kind: meta_memory
id: bld_meta_memory_builder
meta: true
file_position: 11/13
pillar: P10
llm_function: INJECT
purpose: Meta-template for generating MEMORY.md of any kind-builder
quality: 9.1
title: "Meta Memory Builder"
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
  - bld_meta_examples_builder
  - bld_meta_manifest_builder
  - bld_meta_collaboration_builder
  - bld_meta_config_builder
  - bld_meta_instructions_builder
  - bld_meta_tools_builder
  - bld_meta_system_prompt_builder
  - bld_meta_schema_builder
  - skill_memory_update
---

# Memory: {{builder_name}}
<!-- This meta-file generates the MEMORY.md of any builder -->
<!-- REQUIRED INPUT: SCHEMA.md + QUALITY_GATES.md ja gerados -->
<!-- NOTE: Memory comeca vazio e is atualizado apos each producao -->

```yaml
---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
memory_scope: project
observation_types: [user, feedback, project, reference]
---
```

<!-- NOTE: memory_scope = user (~/.claude/) | project (.claude/) | local (.claude/local/) -->
<!-- NOTE: observation_types = taxonomia fixa de 4 types. NUNCA alterar ordem or remover -->
<!-- Decay rules: user=0.03/dia, feedback=0.00 (NUNCA), project=0.05/dia, reference=0.01/dia -->

## Observation Format (universal)
<!-- NOTE: Cada observaction DEVE seguir this format. type: is OBRIGATORIO -->
<!-- Tipos validos: user | feedback | project | reference -->

```
### Observation N (YYYY-MM-DD)
- type: user | feedback | project | reference
- observation: "o that foi aprendido"
- pattern: "rule generalizavel"
- evidence: "data that suportam"
- confidence: 0.0-1.0
- outcome: SUCCESS | PARTIAL | FAILURE
- session: session_id
- tags: [tag1, tag2]
```

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
<!-- NOTE: Iniciar with 5-10 erros previsiveis based no SCHEMA e QUALITY_GATES -->
<!-- Padrao UNIVERSAL observado em all os 4 builders: -->
1. Setting quality to a number instead of null ({{hard_gate_quality}} rejects any value)
2. {{mistake_id_format}} (must follow {{id_pattern}})
<!-- NOTE: Adicionar erros specific based nos HARD gates -->
<!-- Exemplos observados: -->
<!-- - model_card: "Using string for context_window instead of integer" -->
<!-- - KC: "Using hyphens in id slug (must be underscores)" -->
<!-- - signal: "Using quality instead of quality_score" -->
<!-- - quality_gate: "Weights not summing to 100%" -->
3. {{mistake_type_specific_1}}
4. {{mistake_type_specific_2}}
5. {{mistake_type_specific_3}}
<!-- Incluir: erros de format, erros de boundary, erros de field -->

### {{Domain_Patterns_Section}}
<!-- NOTE: Secao specifies do domain with data acumulados -->
<!-- Exemplos observados: -->
<!-- - model_card: "Pricing Sources" (Provider | URL | Last verified) -->
<!-- - KC: "Density Boosters" (techniques for aumentar density) -->
<!-- - signal: "Recurrent Patterns" (quais fields opcionais are more uteis) -->
<!-- - quality_gate: "Proven Gate Patterns" (Domain | HARD count | SOFT dims | Threshold) -->
<!-- Creater tabela or lista relevante for o domain do type -->
{{domain_patterns_content}}

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | {{anticipated_friction}} |
<!-- NOTE: {{anticipated_friction}} = pontos de atrito previstos -->
<!-- Exemplos: "tiered pricing", "density threshold", "boundary drift" -->

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a {{type_name}}, update:
- New common mistake (if encountered)
- New {{domain_pattern_type}} (if discovered)
- Production counter increment
<!-- NOTE: Esta section is IDENTICA em all os builders -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_meta_quality_gates_builder]] | downstream | 0.32 |
| [[bld_meta_examples_builder]] | upstream | 0.30 |
| [[bld_meta_manifest_builder]] | upstream | 0.30 |
| [[bld_meta_collaboration_builder]] | downstream | 0.29 |
| [[bld_meta_config_builder]] | upstream | 0.28 |
| [[bld_meta_instructions_builder]] | upstream | 0.28 |
| [[bld_meta_tools_builder]] | upstream | 0.25 |
| [[bld_meta_system_prompt_builder]] | upstream | 0.25 |
| [[bld_meta_schema_builder]] | upstream | 0.25 |
| [[skill_memory_update]] | related | 0.24 |
