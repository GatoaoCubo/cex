---
id: p01_kc_parser
kind: knowledge_card
type: kind
pillar: P01
title: "Parser — Deep Knowledge for parser"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: parser
quality: 9.1
tags: [parser, P05, GOVERN, kind-kc, extraction]
tldr: "Extracts structured semantic data from raw LLM output using regex, JSON extraction, or Pydantic models — the bridge from unstructured generation to typed downstream data"
when_to_use: "Building, reviewing, or reasoning about parser artifacts"
keywords: [parser, extraction, pydantic, regex, structured-output]
feeds_kinds: [parser]
density_score: null
related:
  - parser-builder
  - p01_kc_response_format
  - bld_architecture_parser
  - p03_sp_parser_builder
  - bld_knowledge_card_parser
  - bld_collaboration_parser
  - p01_kc_llm_output_parsing_validation
  - p01_kc_output_validator
  - p11_qg_parser
  - bld_memory_parser
---

# Parser

## Spec
```yaml
kind: parser
pillar: P05
llm_function: GOVERN
max_bytes: 4096
naming: p05_parser_{{target}}.md + .yaml
core: false
```

## What It Is
A parser extracts structured semantic data from raw LLM text output. It applies regex patterns, JSON block extraction, XML parsing, or Pydantic model validation to convert unstructured generation into typed data structures that downstream systems can consume. Its boundary is semantic extraction — reading meaning and structure from generated text. It is NOT a formatter (which applies structural transformation without extracting meaning) nor a validator in P06 (which validates an already-parsed, already-structured object against a formal schema contract).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | BaseOutputParser, JsonOutputParser, PydanticOutputParser | .invoke(text) returns typed object |
| LlamaIndex | PydanticOutputParser, LLMTextCompletionProgram | Structured prediction via Pydantic |
| CrewAI | output_pydantic on Task | Per-task Pydantic model enforced on output |
| DSPy | TypedPredictor, Signature with typed fields | Compiler-driven extraction pipeline |
| Haystack | OutputAdapter with type casting | Component IO type coercion |
| OpenAI | structured_outputs (response_format json_schema) | Schema-enforced at model level |
| Anthropic | tool_use return block parsing | Response extracted from tool_use content |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| target_type | str | required | json / pydantic / regex / xml |
| strict | bool | false | True = raise on any missing required field |
| fallback | str | null | null / empty_model / retry |
| extract_pattern | str | null | Regex pattern for non-JSON text extraction |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Pydantic model | Typed structured output with validation | class AdCopy(BaseModel): title, body, cta |
| JSON block extraction | Free-form LLM with embedded JSON | re.search(r'\{.*?\}', text, re.DOTALL) |
| Regex field extraction | Templated outputs with known labels | re.search(r'Score:\s*(\d+\.?\d*)', text) |
| Retry on parse failure | Critical pipeline steps | Inject parse error reason into next prompt |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Parser that modifies extracted values | Conflates extraction with transformation | Use formatter after parser for reshaping |
| Greedy regex on nested JSON | Captures wrong outer block | Use json.loads() with try/except instead |
| Missing fallback strategy | Unhandled ParseError crashes pipeline | Always define fallback: empty_model or retry |
| P06 validator used as parser | Wrong layer; P06 validates parsed objects | Parser extracts; P06 validates result |

## Integration Graph
```
[raw_llm_text_output] --> [parser] --> [typed_structured_data]
                              |                   |
                    [target_type, pattern]   [downstream agent / storage]
                              |
                    [fallback, strict, retry]
```

## Decision Tree
- IF output needs structural formatting only THEN use formatter
- IF need to validate an already-parsed object THEN use validator (P06)
- IF extraction is enforced at generation time THEN use response_format (P05)
- DEFAULT: parser for any post-hoc extraction of typed data from raw LLM text

## Quality Criteria
- GOOD: target_type declared, fallback defined, handles missing optional fields gracefully
- GREAT: strict mode with Pydantic, retry on failure with error injection, parse error logged with raw text
- FAIL: no fallback, greedy regex, modifies semantic values during extraction, no error logging

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[parser-builder]] | downstream | 0.46 |
| [[p01_kc_response_format]] | sibling | 0.46 |
| [[bld_architecture_parser]] | downstream | 0.44 |
| [[p03_sp_parser_builder]] | downstream | 0.42 |
| [[bld_knowledge_card_parser]] | sibling | 0.39 |
| [[bld_collaboration_parser]] | downstream | 0.39 |
| [[p01_kc_llm_output_parsing_validation]] | sibling | 0.38 |
| [[p01_kc_output_validator]] | sibling | 0.37 |
| [[p11_qg_parser]] | downstream | 0.36 |
| [[bld_memory_parser]] | downstream | 0.36 |
