---
id: p01_kc_type_def
kind: knowledge_card
type: kind
pillar: P06
title: "Type Def — Deep Knowledge for type_def"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: type_def
quality: 9.1
tags: [type_def, P06, GOVERN, kind-kc]
tldr: "Reusable abstract data type definition specifying shape, fields, and types for system-wide consistency."
when_to_use: "Building, reviewing, or reasoning about type_def artifacts"
keywords: [type, schema, shape, reusable]
feeds_kinds: [type_def]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_input_schema
  - p01_kc_enum_def
  - p01_kc_interface
  - bld_architecture_type_def
  - p01_kc_schema_validation
  - type-def-builder
  - bld_collaboration_type_def
  - p03_sp_type-def-builder
  - bld_memory_type_def
  - bld_knowledge_card_input_schema
---

# Type Def

## Spec
```yaml
kind: type_def
pillar: P06
llm_function: GOVERN
max_bytes: 3072
naming: p06_td_{{type}}.yaml
core: true
```

## What It Is
A reusable, named data type definition that specifies the structural shape—fields, nested types, optional/required status—of a data object used across the system. Abstract and implementation-agnostic. NOT input_schema (defines calling contract for a specific agent invocation, not reusable shape). NOT interface (bilateral contract, not a standalone type). NOT enum_def (flat literals, no nested structure).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | BaseModel (Pydantic) | TypedDict or Pydantic for structured output |
| LlamaIndex | BaseModel / dataclass | Node, Document, or custom Pydantic model |
| CrewAI | Pydantic BaseModel | Agent output model class |
| DSPy | Signature type | Type annotation on Signature fields |
| Haystack | Dataclass / BaseModel | Haystack Document or custom component type |
| OpenAI | JSON Schema object | "type": "object" with properties in tool |
| Anthropic | JSON Schema object | Nested object in tool input_schema |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| fields | dict[str, FieldDef] | required | Fewer = flexible, more = predictable |
| nullable | bool | false | true = optional presence allowed |
| extends | type_def ref | null | Inheritance for shared base types |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Shared output type | Same shape used by N agents | p06_td_research_result.yaml |
| Nested composition | Complex object from simple types | p06_td_pipeline_report.yaml |
| Extension inheritance | Specializing a base type | p06_td_scored_result extends p06_td_result |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Defining types inline in schemas | Drift when type changes | Extract to type_def, reference everywhere |
| One type_def per agent | Explosion of near-duplicate types | Identify shared shapes, extract once |
| Using for enum literals | Wrong abstraction level | Use enum_def for flat string lists |

## Integration Graph
```
[enum_def] --> [type_def] --> [input_schema]
                   |-------> [interface (output)]
                   |-------> [validation_schema]
                   |-------> [response_format (P05)]
```

## Decision Tree
- IF reusable structured shape (object with fields) THEN type_def
- IF flat list of allowed literals THEN enum_def
- IF calling contract for specific invocation THEN input_schema
- IF bilateral channel shape THEN interface
- DEFAULT: type_def when same structure appears in >= 2 schemas

## Quality Criteria
- GOOD: Named clearly, all fields typed, snake_case throughout
- GREAT: Referenced by >= 2 other schemas, extends tracked, optional fields documented
- FAIL: Inline duplicated in schemas, no field types, named after implementation not domain

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_input_schema]] | sibling | 0.45 |
| [[p01_kc_enum_def]] | sibling | 0.38 |
| [[p01_kc_interface]] | sibling | 0.35 |
| [[bld_architecture_type_def]] | downstream | 0.35 |
| [[p01_kc_schema_validation]] | sibling | 0.33 |
| [[type-def-builder]] | related | 0.33 |
| [[bld_collaboration_type_def]] | related | 0.29 |
| [[p03_sp_type-def-builder]] | upstream | 0.29 |
| [[bld_memory_type_def]] | downstream | 0.28 |
| [[bld_knowledge_card_input_schema]] | sibling | 0.27 |
