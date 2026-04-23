---
kind: knowledge_card
id: bld_knowledge_card_input_schema
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for input_schema production — unilateral entry contracts
sources: JSON Schema (draft-07), OpenAPI requestBody, Pydantic BaseModel, TypeScript params
quality: 9.1
title: "Knowledge Card Input Schema"
version: "1.0.0"
author: n03_builder
tags: [input_schema, builder, examples]
tldr: "Golden and anti-examples for input schema construction, demonstrating ideal structure and common pitfalls."
domain: "input schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_input_schema
  - p10_lr_input_schema_builder
  - p11_qg_input_schema
  - input-schema-builder
  - p03_sp_input_schema_builder
  - bld_schema_input_schema
  - bld_collaboration_input_schema
  - bld_output_template_input_schema
  - p01_kc_input_schema
  - bld_architecture_input_schema
---

# Domain Knowledge: input_schema
## Executive Summary
Input schemas are unilateral entry contracts — the receiving system declares what data it requires with types, constraints, defaults, and coercion rules. Rooted in JSON Schema and OpenAPI requestBody patterns. Input schemas differ from interfaces (bilateral contracts), validators (pass/fail rule checks), and type definitions (abstract reusable types).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (contracts/schema) |
| Frontmatter fields | 20+ |
| Quality gates | 8 HARD + 10 SOFT |
| Direction | Unilateral (receiver defines) |
| Required per field | name, type, required/optional, description |
| Optional per field | default, coercion, error_message, examples |
## Patterns
- **Field type system**: every field has an explicit type with validation
| Source | Concept | Application |
|--------|---------|-------------|
| JSON Schema | Properties, required, types, defaults | Field definitions with types |
| OpenAPI | requestBody validation | Unilateral API input contracts |
| Pydantic | Data validation with defaults | Fields + coercion + defaults |
| TypeScript | Typed function parameters | Field-level type constraints |
| GraphQL | Input types for mutations | Structured input with defaults |
- **Required vs optional**: required fields block execution if missing; optional fields MUST have defaults
- **Coercion rules**: "123" → 123 when type is integer — handle LLM-generated mixed-type data gracefully
- **Field-level error messages**: each required field has its own error text for clear LLM-friendly feedback
- **Examples mandatory**: at least one valid payload example for testing and documentation
- **Versioning**: semver for schema evolution — breaking changes require major version bump
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Optional field without default | Undefined behavior when field missing |
| No type constraints | Any value accepted; runtime type errors |
| No coercion rules | LLM sends "42" as string; integer field rejects it |
| Missing error messages | Generic "validation failed" with no field context |
| No examples | Cannot test or document expected input format |
| Bilateral contract in input_schema | That is an interface, not an input_schema |
## Application
1. Identify scope: what operation/agent receives this input?
2. Define fields: name, type, required/optional, description per field
3. Set defaults: every optional field gets a default value
4. Add coercion: rules for type conversion (string→int, string→bool)
5. Write error messages: field-level, actionable text
6. Provide examples: at least one valid payload
## References
- JSON Schema: json-schema.org (draft-07+)
- OpenAPI: requestBody specification (spec.openapis.org)
- Pydantic: data validation for Python (docs.pydantic.dev)
- GraphQL: input type specification

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_input_schema]] | downstream | 0.53 |
| [[p10_lr_input_schema_builder]] | downstream | 0.45 |
| [[p11_qg_input_schema]] | downstream | 0.45 |
| [[input-schema-builder]] | downstream | 0.40 |
| [[p03_sp_input_schema_builder]] | downstream | 0.39 |
| [[bld_schema_input_schema]] | downstream | 0.37 |
| [[bld_collaboration_input_schema]] | downstream | 0.34 |
| [[bld_output_template_input_schema]] | downstream | 0.33 |
| [[p01_kc_input_schema]] | sibling | 0.32 |
| [[bld_architecture_input_schema]] | downstream | 0.32 |
