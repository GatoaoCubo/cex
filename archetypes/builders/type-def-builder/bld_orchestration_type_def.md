---
kind: collaboration
id: bld_collaboration_type_def
pillar: P06
llm_function: COLLABORATE
purpose: How type-def-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Type Def"
version: "1.0.0"
author: n03_builder
tags: [type_def, builder, examples]
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_validation_schema
  - type-def-builder
  - bld_collaboration_builder
  - bld_collaboration_validator
  - bld_collaboration_enum_def
  - bld_collaboration_output_validator
  - bld_collaboration_constraint_spec
  - bld_collaboration_system_prompt
  - bld_collaboration_quality_gate
  - bld_architecture_kind
---

# Collaboration: type-def-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the precise shape, constraint, and serialization rule for this domain type?"
I produce reusable type vocabulary — primitive, composite, union, and algebraic — that other spec-layer artifacts reference by id. I do NOT produce input contracts (validation-schema-builder), individual pass/fail rules (validator-builder), or runtime orchestration (workflow-builder).
## Crew Compositions
### Crew: "Domain Type Modeling"
```
  1. type-def-builder -> "defines costm types: shapes, constraints, serialization rules"
  2. validation-schema-builder -> "uses type_def vocabulary to build post-generation field contracts"
  3. validator-builder -> "references type_def constraints to write individual pass/fail rules"
```
### Crew: "Full Spec Layer Bootstrap"
```
  1. type-def-builder -> "establishes domain type vocabulary for the entire spec layer"
  2. system-prompt-builder -> "uses type vocabulary to define precise agent knowledge boundaries"
  3. unit-eval-builder -> "writes typed test cases against the defined type shapes"
```
## Handoff Protocol
### I Receive
- seeds: domain name, abstract type requirements, base type candidates, constraint descriptions
- optional: serialization targets (JSON/YAML/Protobuf), generic parameters, inheritance context
### I Produce
- type_def artifact (YAML, machine-parseable, max 100 lines)
- committed to: `cex/P06_schema/examples/p06_td_{domain}_{type_name}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- None. type-def-builder is the foundational spec layer — no upstream builder dependency required.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validation-schema-builder | uses type_def vocabulary to specify field types in output contracts |
| validator-builder | references type constraints when writing field-level pass/fail rules |
| system-prompt-builder | uses domain type names to set precise knowledge boundaries for agents |
| unit-eval-builder | writes typed assertions against type_def shapes in test cases |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validation_schema]] | sibling | 0.51 |
| [[type-def-builder]] | related | 0.46 |
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_validator]] | sibling | 0.40 |
| [[bld_collaboration_enum_def]] | sibling | 0.36 |
| [[bld_collaboration_output_validator]] | sibling | 0.35 |
| [[bld_collaboration_constraint_spec]] | sibling | 0.33 |
| [[bld_collaboration_system_prompt]] | sibling | 0.33 |
| [[bld_collaboration_quality_gate]] | sibling | 0.33 |
| [[bld_architecture_kind]] | downstream | 0.33 |
