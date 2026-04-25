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
<!-- REQUIRED INPUT: SCHEMA.md + QUALITY_GATES.md already generated -->
<!-- NOTE: Memory starts empty and is updated after each production -->

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
<!-- NOTE: observation_types = fixed taxonomy of 4 types. NEVER change order or remove -->
<!-- Decay rules: user=0.03/day, feedback=0.00 (NEVER), project=0.05/day, reference=0.01/day -->

## Observation Format (universal)
<!-- NOTE: Each observation MUST follow this format. type: is MANDATORY -->
<!-- Valid types: user | feedback | project | reference -->

```
### Observation N (YYYY-MM-DD)
- type: user | feedback | project | reference
- observation: "what was learned"
- pattern: "generalizable rule"
- evidence: "supporting data"
- confidence: 0.0-1.0
- outcome: SUCCESS | PARTIAL | FAILURE
- session: session_id
- tags: [tag1, tag2]
```

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
<!-- NOTE: Start with 5-10 predictable errors based on SCHEMA and QUALITY_GATES -->
<!-- UNIVERSAL pattern observed across all 4 builders: -->
1. Setting quality to a number instead of null ({{hard_gate_quality}} rejects any value)
2. {{mistake_id_format}} (must follow {{id_pattern}})
<!-- NOTE: Adicionar erros specific based nos HARD gates -->
<!-- Observed examples: -->
<!-- - model_card: "Using string for context_window instead of integer" -->
<!-- - KC: "Using hyphens in id slug (must be underscores)" -->
<!-- - signal: "Using quality instead of quality_score" -->
<!-- - quality_gate: "Weights not summing to 100%" -->
3. {{mistake_type_specific_1}}
4. {{mistake_type_specific_2}}
5. {{mistake_type_specific_3}}
<!-- Include: format errors, boundary errors, field errors -->

### {{Domain_Patterns_Section}}
<!-- NOTE: Domain-specific section with accumulated data -->
<!-- Observed examples: -->
<!-- - model_card: "Pricing Sources" (Provider | URL | Last verified) -->
<!-- - KC: "Density Boosters" (techniques to increase density) -->
<!-- - signal: "Recurrent Patterns" (which optional fields are most useful) -->
<!-- - quality_gate: "Proven Gate Patterns" (Domain | HARD count | SOFT dims | Threshold) -->
<!-- Create table or list relevant to the type's domain -->
{{domain_patterns_content}}

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | {{anticipated_friction}} |
<!-- NOTE: {{anticipated_friction}} = anticipated friction points -->
<!-- Examples: "tiered pricing", "density threshold", "boundary drift" -->

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a {{type_name}}, update:
- New common mistake (if encountered)
- New {{domain_pattern_type}} (if discovered)
- Production counter increment
<!-- NOTE: This section is IDENTICAL across all builders -->

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
