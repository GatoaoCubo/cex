---
kind: architecture
id: bld_architecture_type_def
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of type_def — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Type Def"
version: "1.0.0"
author: n03_builder
tags: [type_def, builder, examples]
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - type-def-builder
  - bld_collaboration_type_def
  - bld_knowledge_card_type_def
  - p03_sp_type-def-builder
  - bld_architecture_validator
  - bld_tools_type_def
  - bld_memory_type_def
  - p01_kc_type_def
  - p11_qg_type_def
  - p03_ins_type_def
---

# Architecture: type_def in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, base_type, nullable, etc.) | type-def-builder | active |
| base_type | Primitive or composite root type (string, integer, object, array, etc.) | author | active |
| constraints | Validation constraints (min, max, regex, enum, length, etc.) | author | active |
| composition_rules | Union, intersection, and discriminated union composition | author | active |
| generics | Type parameters for polymorphic type definitions | author | active |
| serialization_spec | Wire format rules (JSON, YAML, Protobuf) with field mappings | author | active |
| inheritance_chain | Parent type references for type hierarchy | author | active |
## Dependency Graph
```
domain_knowledge  --produces-->  type_def  --consumed_by-->  input_schema
type_def          --consumed_by-->  validator  --consumed_by-->  grammar
type_def          --signals-->      type_registration
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | type_def | data_flow | domain context informing type design |
| type_def | input_schema (P06) | consumes | input schemas reference type definitions |
| type_def | validator (P06) | consumes | validators use type constraints for checks |
| type_def | grammar (P06) | consumes | grammars reference types for parsing rules |
| type_def | prompt_template (P03) | data_flow | templates reference types for variable constraints |
| type_def | type_registration (P12) | signals | emitted when a new type is registered in the system |
## Boundary Table
| type_def IS | type_def IS NOT |
|-------------|-----------------|
| A reusable type declaration with base type, constraints, and composition | An input contract for a specific operation (input_schema P06) |
| Defines vocabulary that other artifacts reference | A validation rule with pass/fail logic (validator P06) |
| Supports union, intersection, and generics composition | An integration contract between systems (interface P06) |
| Includes serialization rules for wire formats | A response format instruction for the LLM (response_format P05) |
| Scoped to the spec layer — no runtime behavior | A parser that extracts data from output (parser P05) |
| Inheritable via inheritance chains | A naming convention for entities (naming_rule P05) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Domain | knowledge_card | Supply domain context for type design |
| Definition | frontmatter, base_type, constraints | Specify the type identity and validation rules |
| Composition | composition_rules, generics, inheritance_chain | Define how types combine and extend |
| Serialization | serialization_spec | Map types to wire formats |
| Consumers | input_schema, validator, grammar, prompt_template | Artifacts that reference the type definition |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[type-def-builder]] | upstream | 0.53 |
| [[bld_collaboration_type_def]] | upstream | 0.42 |
| [[bld_knowledge_card_type_def]] | upstream | 0.39 |
| [[p03_sp_type-def-builder]] | upstream | 0.38 |
| [[bld_architecture_validator]] | sibling | 0.37 |
| [[bld_tools_type_def]] | upstream | 0.37 |
| [[bld_memory_type_def]] | downstream | 0.37 |
| [[p01_kc_type_def]] | upstream | 0.35 |
| [[p11_qg_type_def]] | upstream | 0.34 |
| [[p03_ins_type_def]] | upstream | 0.34 |
