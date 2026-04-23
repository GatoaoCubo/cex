---
kind: architecture
id: bld_architecture_input_schema
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of input_schema — inventory, dependencies, and architectural position
quality: 9.0
title: "Architecture Input Schema"
version: "1.0.0"
author: n03_builder
tags: [input_schema, builder, examples]
tldr: "Golden and anti-examples for input schema construction, demonstrating ideal structure and common pitfalls."
domain: "input schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_interface
  - p01_kc_input_schema
  - p03_sp_input_schema_builder
  - bld_knowledge_card_input_schema
  - bld_instruction_input_schema
  - p01_kc_interface
  - p10_lr_input_schema_builder
  - p11_qg_input_schema
  - bld_collaboration_input_schema
  - input-schema-builder
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| field_definitions | Typed entries the caller must or may provide | author | required |
| required_flags | Which fields are mandatory vs optional | author | required |
| type_constraints | Primitive or structured type per field (string, int, enum, object) | author | required |
| default_values | Fallback values applied when optional fields are absent | author | optional |
| coercion_rules | Type casting applied silently before validation | author | optional |
| error_messages | Human-readable feedback per validation failure | author | optional |
| examples | Concrete valid input objects for documentation and testing | author | recommended |
| schema_version | Version identifier for backward compatibility tracking | author | required |
## Dependency Graph
```
interface     --references--> input_schema
input_schema  --validates_via--> validator
input_schema  --informs--> action_prompt
system_prompt --documents--> input_schema
```
| From | To | Type | Data |
|------|----|------|------|
| interface | input_schema | data_flow | method signature requiring typed input shape |
| input_schema | validator | data_flow | field definitions and constraints to check |
| input_schema | action_prompt | data_flow | input format reference for prompt construction |
| system_prompt | input_schema | data_flow | documentation of required caller data |
## Boundary Table
| input_schema IS | input_schema IS NOT |
|-----------------|---------------------|
| Unilateral contract: defines what the callee needs | Bilateral contract defining both sides |
| Design-time artifact specifying required data shape | Runtime validation execution engine |
| Concrete field-level contract for one operation | Abstract reusable type definition |
| Documents required vs optional with defaults | Output shape specification |
| Applies coercion before validation | Integration contract between two agents |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Contract declaration | field_definitions, required_flags, schema_version | Define the shape of valid input |
| Type system | type_constraints, coercion_rules | Enforce and normalize data types |
| Defaults | default_values | Handle absent optional fields gracefully |
| Feedback | error_messages, examples | Enable caller self-correction and testing |
| Consumers | validator, action_prompt, interface | Enforce and reference the schema at use time |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_interface]] | sibling | 0.42 |
| [[p01_kc_input_schema]] | upstream | 0.42 |
| [[p03_sp_input_schema_builder]] | upstream | 0.42 |
| [[bld_knowledge_card_input_schema]] | upstream | 0.39 |
| [[bld_instruction_input_schema]] | upstream | 0.36 |
| [[p01_kc_interface]] | upstream | 0.34 |
| [[p10_lr_input_schema_builder]] | downstream | 0.32 |
| [[p11_qg_input_schema]] | downstream | 0.29 |
| [[bld_collaboration_input_schema]] | downstream | 0.27 |
| [[input-schema-builder]] | upstream | 0.27 |
