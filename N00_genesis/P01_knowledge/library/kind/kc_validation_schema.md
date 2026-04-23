---
id: p01_kc_validation_schema
kind: knowledge_card
type: kind
pillar: P06
title: "Validation Schema — Deep Knowledge for validation_schema"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: validation_schema
quality: 9.1
tags: [validation_schema, P06, GOVERN, kind-kc]
tldr: "Post-generation output contract applied by the system to validate LLM responses—LLM never sees it."
when_to_use: "Building, reviewing, or reasoning about validation_schema artifacts"
keywords: [validation, output, post-generation, system-applied]
feeds_kinds: [validation_schema]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_response_format
  - bld_knowledge_card_validation_schema
  - p03_sp_validation-schema-builder
  - p01_kc_input_schema
  - bld_architecture_response_format
  - bld_architecture_validation_schema
  - bld_collaboration_validation_schema
  - p03_ins_response_format
  - validation-schema-builder
  - bld_memory_validation_schema
---

# Validation Schema

## Spec
```yaml
kind: validation_schema
pillar: P06
llm_function: GOVERN
max_bytes: 3072
naming: p06_vs_{{scope}}.yaml
core: false
```

## What It Is
A formal contract applied by the SYSTEM after LLM generation to validate that the output meets structural and semantic requirements. The LLM is never shown this schema—it governs pipeline behavior, not LLM prompting. NOT response_format (P05), which is injected INTO the prompt so the LLM constrains its own output. NOT input_schema, which governs what enters the pipeline.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | PydanticOutputParser | Validates LLM string -> Pydantic model |
| LlamaIndex | StructuredOutput validator | Post-call Pydantic validation |
| CrewAI | output_pydantic | Validates agent final output model |
| DSPy | assert / suggest | Runtime output assertion |
| Haystack | OutputValidator component | Post-generation schema check |
| OpenAI | response_format (JSON mode) | JSON Schema in response_format (hybrid) |
| Anthropic | Tool result validation | Validates tool_result content post-call |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| strict | bool | false | true = hard fail, false = soft warn |
| coerce | bool | false | true = auto-fix types (risky) |
| error_action | enum | reject | reject/retry/fallback on failure |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Hard gate | Critical field must exist | Missing required field -> reject + retry |
| Soft coerce | Minor type mismatch tolerable | int as string -> auto-cast, log warning |
| Retry loop | Validation fail triggers re-prompt | Max 3 retries, then fallback |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Injecting into prompt | LLM tries to satisfy schema literally | Use response_format (P05) for LLM-visible |
| No error_action defined | Silent pass of invalid output | Always define reject/retry/fallback |
| Duplicate of input_schema | Two schemas for same data | validation_schema = output only |

## Integration Graph
```
[LLM output] --> [validation_schema] --> [pipeline next stage]
[type_def] -----> [validation_schema]          |
[enum_def] -----> [validation_schema]    +--> [scorer (P11)]
                                         +--> [error handler]
```

## Decision Tree
- IF constraining LLM output format within the prompt THEN response_format (P05)
- IF validating LLM output AFTER generation (system-side) THEN validation_schema
- IF specifying what caller must provide THEN input_schema
- DEFAULT: validation_schema for any output with structural requirements

## Quality Criteria
- GOOD: Covers all required output fields, error_action defined, linked to type_def
- GREAT: Retry strategy defined, coerce rules documented, unit_eval test included
- FAIL: Injected into prompt, no error action, duplicates input_schema scope

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_response_format]] | sibling | 0.40 |
| [[bld_knowledge_card_validation_schema]] | sibling | 0.39 |
| [[p03_sp_validation-schema-builder]] | upstream | 0.38 |
| [[p01_kc_input_schema]] | sibling | 0.37 |
| [[bld_architecture_response_format]] | downstream | 0.36 |
| [[bld_architecture_validation_schema]] | downstream | 0.36 |
| [[bld_collaboration_validation_schema]] | related | 0.35 |
| [[p03_ins_response_format]] | upstream | 0.35 |
| [[validation-schema-builder]] | related | 0.34 |
| [[bld_memory_validation_schema]] | downstream | 0.33 |
