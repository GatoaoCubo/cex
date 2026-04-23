---
kind: meta_knowledge
id: bld_meta_knowledge_builder
meta: true
file_position: 3/13
pillar: P01
llm_function: INJECT
purpose: Meta-template for generating KNOWLEDGE.md of any kind-builder
quality: 9.1
title: "Meta Knowledge Builder"
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
  - bld_meta_architecture_builder
  - bld_meta_collaboration_builder
  - bld_meta_tools_builder
  - bld_meta_instructions_builder
  - bld_meta_schema_builder
  - bld_meta_system_prompt_builder
  - bld_meta_examples_builder
  - bld_meta_quality_gates_builder
  - bld_meta_memory_builder
---

# Domain Knowledge: {{type_name}}
<!-- This meta-file generates the KNOWLEDGE.md of any builder -->
<!-- REQUIRED INPUT: _schema.yaml do type-target, TAXONOMY_LAYERS.yaml, research de domain -->
<!-- NOTE: Este is o file more variable between builders — requer research real -->

```yaml
---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for {{type_name}} production
sources: {{sources_used}}
---
```

## Foundational Standard/Concept
<!-- NOTE: Origem academica or industrial do type -->
<!-- Padrao observado: -->
<!-- - model_card: Mitchell et al. 2019 "Model Cards for Model Reporting" -->
<!-- - knowledge_card: "Atomic searchable facts" (CEX-internal concept) -->
<!-- - signal: "Smallest coordination artifact in P12" (operational concept) -->
<!-- - quality_gate: Cooper 1990 stage-gate process -->
<!-- Se o type tem origem academica, cite paper + URL -->
<!-- Se o type is CEX-interno, descreva o concept fundamental -->
{{foundational_description}}

## Industry Implementations
<!-- NOTE: Tabela comparando implementactions do concept em tools reais -->
<!-- Padrao: Source | What it defines | CEX uses -->
<!-- Se not ha equivalente industrial direto: omitir or adaptar as "Related Patterns" -->

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| {{source_1}} | {{what_1}} | {{cex_use_1}} |
| {{source_2}} | {{what_2}} | {{cex_use_2}} |
| {{source_3}} | {{what_3}} | {{cex_use_3}} |

## Key Patterns
<!-- NOTE: 5-8 patterns/principles that governam a producao deste type -->
<!-- Extract de _schema.yaml constraints + experiencia do domain -->
<!-- Padrao: bullet list with patterns concrete e actionable -->
- {{pattern_1}}
- {{pattern_2}}
- {{pattern_3}}

## CEX-Specific Extensions
<!-- NOTE: Campos or rules that o CEX adiciona alem do standard industrial -->
<!-- Padrao: tabela Field | Justification | Closest industry equivalent -->
<!-- Se all os fields are standard industrial: omitir esta section -->

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| {{field_1}} | {{why_1}} | {{equivalent_1}} |

## Boundary vs Nearby Types
<!-- NOTE: Table distinguishing this type from confusing neighbors -->
<!-- Pattern identical in ALL 4 existing builders -->
<!-- Search overlaps in TAXONOMY_LAYERS.yaml -->

| Type | What it is | Why it is NOT {{type_name}} |
|------|------------|---------------------------|
| {{confused_type_1}} | {{what_it_is}} | {{why_different}} |
| {{confused_type_2}} | {{what_it_is}} | {{why_different}} |

## References
<!-- NOTE: URLs de fontes oficiais, papers, documentation -->
- {{reference_1}}
- {{reference_2}}

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_meta_manifest_builder]] | downstream | 0.35 |
| [[bld_meta_architecture_builder]] | downstream | 0.30 |
| [[bld_meta_collaboration_builder]] | downstream | 0.29 |
| [[bld_meta_tools_builder]] | downstream | 0.29 |
| [[bld_meta_instructions_builder]] | downstream | 0.28 |
| [[bld_meta_schema_builder]] | downstream | 0.27 |
| [[bld_meta_system_prompt_builder]] | downstream | 0.25 |
| [[bld_meta_examples_builder]] | downstream | 0.24 |
| [[bld_meta_quality_gates_builder]] | downstream | 0.23 |
| [[bld_meta_memory_builder]] | downstream | 0.22 |
