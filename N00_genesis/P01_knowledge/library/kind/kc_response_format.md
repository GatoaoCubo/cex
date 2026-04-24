---
id: p01_kc_response_format
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "Response Format — Deep Knowledge for response_format"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: response_format
quality: 9.1
tags: [response_format, P05, CONSTRAIN, kind-kc, structured-output]
tldr: "Defines the output structure injected into the LLM's generation context — JSON schema, Pydantic model, or format instruction that constrains generation before it happens"
when_to_use: "Building, reviewing, or reasoning about response_format artifacts"
keywords: [response_format, structured-output, json-schema, constrain, generation]
feeds_kinds: [response_format]
density_score: null
related:
  - response-format-builder
  - bld_architecture_response_format
  - p01_kc_parser
  - p01_kc_validation_schema
  - p03_ins_response_format
  - bld_collaboration_response_format
  - p01_kc_function_def
  - p01_kc_formatter
  - bld_memory_response_format
  - p01_kc_llm_output_parsing_validation
---

# Response Format

## Spec
```yaml
kind: response_format
pillar: P05
llm_function: CONSTRAIN
max_bytes: 4096
naming: p05_rf_{{format}}.yaml
core: true
```

## What It Is
A response_format defines the output structure injected into the LLM's generation context — as a JSON schema in the API call (OpenAI structured_outputs, Anthropic tool-as-format), as a Pydantic model compiled to schema, or as a format instruction in the system prompt. It constrains generation BEFORE it happens. It is NOT a validation_schema in P06 (applied by the system AFTER generation to validate a parsed object), NOT a parser (which extracts data from already-generated text), NOT a formatter (which reshapes already-generated text).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | with_structured_output(schema), response_schemas | Bound to model; schema-constrained output |
| LlamaIndex | output_cls=PydanticModel in LLMProgram | Pydantic-driven structured prediction |
| CrewAI | output_pydantic on Task | Per-task response format via Pydantic class |
| DSPy | Signature with typed OutputField | Compiler resolves format constraint implicitly |
| Haystack | OutputAdapter with type hint | Type-coerced output spec on component |
| OpenAI | response_format: {type: json_schema, strict: true} | Strict JSON mode; schema passed in API call |
| Anthropic | Single tool schema as response format | Force tool_choice to output_tool; parse result |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| format_type | str | required | json_schema / pydantic / instruction |
| strict | bool | false | True = no extra fields; less hallucination |
| schema | object | required | JSON Schema definition or Pydantic model ref |
| inject_as | str | system_prompt | system_prompt / api_param / tool_schema |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| OpenAI strict JSON | Deterministic structured data extraction | response_format={type: json_schema, strict: true} |
| Anthropic tool-as-format | Single structured response from Claude | Define output_tool; force tool_choice to it |
| Pydantic in system prompt | Framework-agnostic across providers | Inject Pydantic schema description in system |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| JSON mode without schema | LLM invents arbitrary field names | Always provide explicit schema with properties |
| Schema too deeply nested | LLM omits required nested fields | Flatten to max 2 levels; max 5 required fields |
| Using response_format as validator | Wrong layer; format constrains; validator checks | Use output_validator or P06 for post-generation |
| Different format per call | Inconsistent pipeline output shape | Pin response_format at chain level, not per-call |

## Integration Graph
```
[response_format schema] --> [LLM generation (constrained)] --> [structured_output_text]
        |                                                                |
[schema, strict, inject_as]                               [parser / output_validator]
        |
[injected as system_prompt / api_param / tool_schema]
```

## Decision Tree
- IF extracting data from already-generated text THEN use parser
- IF validating a parsed object against schema THEN use validator (P06)
- IF transforming format of already-generated text THEN use formatter
- DEFAULT: response_format when constraining LLM generation structure at call time

## Quality Criteria
- GOOD: schema defined, inject_as specified, format_type declared, required fields listed
- GREAT: strict mode, schema validated against real LLM output examples, parser fallback if LLM deviates
- FAIL: JSON mode without schema, no required fields defined, applied post-generation as validator

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[response-format-builder]] | downstream | 0.40 |
| [[bld_architecture_response_format]] | downstream | 0.40 |
| [[p01_kc_parser]] | sibling | 0.40 |
| [[p01_kc_validation_schema]] | sibling | 0.39 |
| [[p03_ins_response_format]] | downstream | 0.38 |
| [[bld_collaboration_response_format]] | downstream | 0.37 |
| [[p01_kc_function_def]] | sibling | 0.37 |
| [[p01_kc_formatter]] | sibling | 0.33 |
| [[bld_memory_response_format]] | downstream | 0.32 |
| [[p01_kc_llm_output_parsing_validation]] | sibling | 0.31 |
