---
id: p01_kc_enum_def
kind: knowledge_card
type: kind
pillar: P06
title: "Enum Def — Deep Knowledge for enum_def"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: enum_def
quality: 9.1
tags: [enum_def, P06, CONSTRAIN, kind-kc]
tldr: "Finite named list of allowed literals that constrains LLM or system values to a closed set."
when_to_use: "Building, reviewing, or reasoning about enum_def artifacts"
keywords: [enum, literals, closed-set, constrain]
feeds_kinds: [enum_def]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - enum-def-builder
  - p03_sp_enum_def_builder
  - bld_knowledge_card_enum_def
  - p01_kc_type_def
  - p11_qg_enum_def
  - bld_collaboration_enum_def
  - bld_architecture_enum_def
  - bld_instruction_enum_def
  - p01_kc_input_schema
  - bld_schema_enum_def
---

# Enum Def

## Spec
```yaml
kind: enum_def
pillar: P06
llm_function: CONSTRAIN
max_bytes: 1024
naming: p06_enum.md
core: true
```

## What It Is
A shared, reusable list of named string constants used to constrain any field to a finite closed set. Defined once in p06_enum.md and referenced by input_schema, validation_schema, and response_format. NOT a type_def—enum_def has no structure or field hierarchy, only a flat list of literals.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | Literal[...] / Python Enum | Type annotation in structured output |
| LlamaIndex | Enum field | Pydantic Enum in node metadata |
| CrewAI | Pydantic Literal | Agent output field constraint |
| DSPy | OutputField Literal | Constrained signature field |
| Haystack | ComponentInput choices | allowed_values list |
| OpenAI | "enum": [...] | JSON Schema enum in function/tool |
| Anthropic | "enum": [...] | input_schema enum in tool_use |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| values | list[str] | required | More = less constrained, higher hallucination |
| description | str | optional | Missing = LLM guesses semantics |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Output gate | Force one of N choices in LLM response | status: [draft, review, approved, rejected] |
| Router signal | Route pipeline to next step | intent: [search, create, update, delete] |
| Quality tier | Score bucket for quality gates | tier: [gold, silver, bronze, fail] |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| >20 values | LLM recall degrades, wrong picks | Split into semantic sub-enums |
| Overlapping semantics | LLM picks inconsistently | Make values mutually exclusive |
| Using type_def instead | Adds unnecessary shape | Use enum_def for flat literals only |

## Integration Graph
```
[type_def] --> [enum_def] --> [input_schema]
                   |-------> [validation_schema]
                   |-------> [response_format (P05)]
```

## Decision Tree
- IF field has finite closed set of string literals THEN enum_def
- IF field requires shape/structure with sub-fields THEN type_def
- IF list > 20 values and has hierarchy THEN split or use type_def
- DEFAULT: enum_def for <= 20 atomic, mutually exclusive values

## Quality Criteria
- GOOD: Values snake_case, mutually exclusive, max 20 entries
- GREAT: Each value has inline description, referenced in >= 2 schemas
- FAIL: Duplicate entries, >30 values, mixed casing, no context

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[enum-def-builder]] | related | 0.44 |
| [[p03_sp_enum_def_builder]] | related | 0.41 |
| [[bld_knowledge_card_enum_def]] | sibling | 0.41 |
| [[p01_kc_type_def]] | sibling | 0.41 |
| [[p11_qg_enum_def]] | downstream | 0.40 |
| [[bld_collaboration_enum_def]] | downstream | 0.39 |
| [[bld_architecture_enum_def]] | downstream | 0.38 |
| [[bld_instruction_enum_def]] | upstream | 0.37 |
| [[p01_kc_input_schema]] | sibling | 0.36 |
| [[bld_schema_enum_def]] | related | 0.35 |
