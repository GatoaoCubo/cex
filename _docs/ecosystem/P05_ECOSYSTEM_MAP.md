# P05 Output — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| Instructor | Structured extraction | response_model (Pydantic), Partial streaming, Iterable, retry with validation, mode (JSON/TOOLS/MD_JSON) |
| BAML | AI function language | Function, Client, TypeBuilder, RetryPolicy, TestCase, Boundary (input→output type contract) |
| Outlines | Structured generation | Generator, JSONSchema guide, Regex guide, CFG guide, Choice, multi-model |
| Guardrails AI | Output validation | Guard, Validator (ToxicLanguage, ReadingLevel, etc.), Rail spec (XML), Reask, OnFail (fix/reask/noop) |
| Marvin | AI functions | fn() decorator, cast(), extract(), classify(), Model, Image extraction |
| TypeChat | Type-safe NLP | Translator (schema→prompt), Validator (JSON parse + type check), Program (multi-step), Sentiment |
| LangChain OutputParser | Output parsing | StrOutputParser, JsonOutputParser, PydanticOutputParser, CommaSeparatedListOutputParser, XMLOutputParser, OutputFixingParser |
| OpenAI Structured Outputs | API-native | response_format (json_schema), strict mode, function calling (strict:true), Pydantic integration |
| Anthropic JSON mode | API-native | tool_use for structured output, json prefill, XML tags, system prompt format instructions |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Response Schema/Format | OpenAI (response_format), Instructor (response_model), BAML (Function output), Outlines (JSONGuide), TypeChat (Translator schema) | Type definition that constrains LLM output shape | 7 |
| Output Parser | LangChain (OutputParser), Marvin (cast/extract), TypeChat (Validator), Guardrails (Guard) | Logic that extracts structured data from raw LLM text | 6 |
| Validation + Auto-fix | Guardrails (OnFail:fix), Instructor (retry), LangChain (OutputFixingParser), TypeChat (Validator repair) | Detect malformed output and auto-repair via re-prompting or rule | 4 |
| Streaming/Partial | Instructor (Partial), OpenAI (stream+json), BAML (streaming) | Emit partial structured output as tokens arrive | 3 |
| Output Mode | Instructor (mode: JSON/TOOLS/MD_JSON), OpenAI (response_format type), Anthropic (tool_use vs prefill) | Which API mechanism to use for structured output | 4 |
| Format Transformer | LangChain (StrOutputParser, XMLOutputParser), Marvin (cast) | Convert between formats: text→JSON, JSON→XML, etc. | 3 |
| Naming Convention | (implicit in all) | How artifacts/files/fields are named — present but not formalized as a concept in any framework | 0 |
| Classification/Enum | Marvin (classify), Outlines (Choice), Instructor (Literal types) | Constrain output to enumerated choices | 3 |
| Rail/Contract Spec | Guardrails (Rail XML), BAML (Function spec), TypeChat (schema) | Declarative output contract separate from prompt | 3 |
| Retry Policy | Instructor (max_retries), BAML (RetryPolicy), Guardrails (Reask) | How many times and how to retry on validation failure | 3 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| response_format | Response Schema/Format | 90% | Excellent match. CEX response_format aligns with OpenAI response_format, Instructor response_model. Core concept. |
| parser | Output Parser | 85% | Good match. Industry parsers are more typed (Pydantic, TypeScript). CEX parser is generic extractor. |
| formatter | Format Transformer | 75% | Reasonable match. Industry does format conversion inside parsers. CEX separates extraction from transformation — valid but less common. |
| naming_rule | (no industry match) | 20% | No framework treats naming as a formal output concept. This is a CEX governance kind, not an output kind. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| output_validator | Validation rules applied AFTER parsing: type checking, range constraints, toxicity filters, semantic checks. Distinct from P06 validator (pre-execution contracts) — this validates LLM output specifically. | Guardrails AI, Instructor, TypeChat, LangChain OutputFixingParser | high |
| retry_policy | Max retries, backoff, fix strategy (reask/fix/noop), validation error feedback template. Universal in structured output frameworks. Currently implicit in CEX. | Instructor, BAML, Guardrails AI | med |
| output_mode | Which API mechanism to use (JSON mode, tool_use, function_calling, markdown_json, prefill). Provider-specific routing for structured output. | Instructor, OpenAI, Anthropic, BAML | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| naming_rule | MOVE to P08 Architecture | Naming conventions are architectural governance, not output format. No industry framework treats naming as an output concept. Belongs alongside laws and governance rules in P08. |
| formatter | KEEP but narrow | Overlap risk with parser. Clarify: parser = extract data from text, formatter = convert between serialization formats (JSON↔YAML↔XML). Industry often merges these. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| response_format | OpenAI response_format, Instructor response_model, BAML Function output, Outlines JSONGuide, TypeChat Translator schema |
| parser | LangChain OutputParser, Marvin cast/extract, TypeChat Validator, Guardrails Guard |
| formatter | LangChain StrOutputParser/XMLOutputParser, Marvin cast (format conversion) |

## 7. Summary
Current: 4 kinds → Proposed: 6 kinds (+output_validator, +retry_policy, +output_mode, -naming_rule moved to P08) | Coverage: ~68% → ~90%

Key insight: The structured output space has exploded since 2024. **Validation-and-retry** is the dominant pattern (Instructor, Guardrails, BAML all center on it). CEX has response_format and parser but lacks the validation→retry loop that makes structured output reliable in production. Adding output_validator and retry_policy would close the biggest gap. naming_rule is a governance concern that belongs in P08, not P05.
