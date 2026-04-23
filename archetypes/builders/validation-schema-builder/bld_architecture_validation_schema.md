---
kind: architecture
id: bld_architecture_validation_schema
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of validation_schema — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Validation Schema"
version: "1.0.0"
author: n03_builder
tags: [validation_schema, builder, examples]
tldr: "Golden and anti-examples for validation schema construction, demonstrating ideal structure and common pitfalls."
domain: "validation schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_validation_schema
  - validation-schema-builder
  - p01_kc_validation_schema
  - bld_architecture_response_format
  - bld_knowledge_card_validation_schema
  - p03_sp_validation-schema-builder
  - bld_architecture_validator
  - bld_memory_validation_schema
  - bld_examples_validation_schema
  - p03_ins_validation_schema
---

# Architecture: validation_schema in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 20-field metadata header (id, kind, pillar, domain, target_kind, etc.) | validation-schema-builder | active |
| field_definitions | Named fields with types, constraints, and required/optional status | author | active |
| constraint_rules | Per-field validation (regex, range, enum, length, format) | author | active |
| on_failure_behavior | What happens when validation fails (reject, warn, auto_fix) | author | active |
| coercion_rules | Type coercion policies for mismatched but recoverable types | author | active |
| schema_version | Version of the schema for backward compatibility tracking | author | active |
## Dependency Graph
```
LLM_output       --validated_by-->  validation_schema  --produces-->  validated_output
type_def          --informs-->      validation_schema  --signals-->   validation_event
response_format   --precedes-->     validation_schema
```
| From | To | Type | Data |
|------|----|------|------|
| LLM_output | validation_schema | data_flow | generated output submitted for post-generation validation |
| type_def (P06) | validation_schema | dependency | type definitions inform field types and constraints |
| response_format (P05) | validation_schema | dependency | response format precedes validation in the pipeline |
| validation_schema | validated_output | produces | output that passed all field and constraint checks |
| validation_schema | validation_event (P12) | signals | emitted on pass, fail, or auto_fix |
| validation_schema | quality_gate (P11) | data_flow | gate may require schema validation pass |
## Boundary Table
| validation_schema IS | validation_schema IS NOT |
|----------------------|--------------------------|
| A post-generation contract the SYSTEM enforces automatically | A format instruction the LLM sees during generation (response_format P05) |
| Field-level validation with types, constraints, and coercion | An individual pass/fail rule (validator P06) |
| Applied after the LLM produces output — invisible to the LLM | A pre-generation prompt or template (prompt_template P03) |
| Includes on_failure behavior (reject, warn, auto_fix) | An input contract for what the prompt receives (input_schema P06) |
| Versioned for backward compatibility | A scoring evaluation with weighted dimensions (scoring_rubric P07) |
| Scoped to one target artifact kind | A universal validation applied to all artifact kinds |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Types | type_def, response_format | Supply type definitions and expected format |
| Schema | frontmatter, field_definitions, constraint_rules, schema_version | Define the validation contract |
| Enforcement | coercion_rules, on_failure_behavior | Handle mismatches and failures |
| Input | LLM_output | Generated output submitted for validation |
| Output | validated_output, validation_event, quality_gate | Deliver validated result and signal outcome |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validation_schema]] | upstream | 0.49 |
| [[validation-schema-builder]] | upstream | 0.47 |
| [[p01_kc_validation_schema]] | upstream | 0.46 |
| [[bld_architecture_response_format]] | sibling | 0.46 |
| [[bld_knowledge_card_validation_schema]] | upstream | 0.44 |
| [[p03_sp_validation-schema-builder]] | upstream | 0.43 |
| [[bld_architecture_validator]] | sibling | 0.38 |
| [[bld_memory_validation_schema]] | downstream | 0.36 |
| [[bld_examples_validation_schema]] | upstream | 0.36 |
| [[p03_ins_validation_schema]] | upstream | 0.34 |
