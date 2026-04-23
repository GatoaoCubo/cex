---
id: p01_kc_output_validator
kind: knowledge_card
type: kind
pillar: P01
title: "Output Validator — Deep Knowledge for output_validator"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: output_validator
quality: 9.1
tags: [output_validator, P05, GOVERN, kind-kc, validation]
tldr: "Post-LLM quality and safety checker applying heuristic, structural, and semantic checks before delivery — catches hallucination signals, toxicity, and format violations"
when_to_use: "Building, reviewing, or reasoning about output_validator artifacts"
keywords: [validation, output, quality, safety, hallucination]
feeds_kinds: [output_validator]
density_score: null
related:
  - bld_knowledge_card_output_validator
  - output-validator-builder
  - p01_kc_parser
  - bld_examples_output_validator
  - p03_sp_output_validator_builder
  - p10_lr_output_validator_builder
  - bld_architecture_output_validator
  - p01_kc_response_format
  - p01_kc_validation_schema
  - p01_kc_validator
---

# Output Validator

## Spec
```yaml
kind: output_validator
pillar: P05
llm_function: GOVERN
max_bytes: 2048
naming: p05_oval.md
core: true
```

## What It Is
An output_validator applies heuristic, structural, and semantic checks to LLM-generated output before it is delivered to downstream consumers or users. It checks for format compliance, toxicity, hallucination signals (fabricated citations, contradictory claims), length violations, and required field presence. It is NOT a validator in P06 (which validates a structured data object against a formal Pydantic/JSON Schema contract) — output_validator targets raw LLM text output quality and safety before any parsing.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | OutputParser with Pydantic validation | Parse + validate in one step |
| LlamaIndex | GuardrailsOutputParser, Evaluator | Guardrails.ai + LI evaluator pipeline |
| CrewAI | Guardrails on task output | No dedicated kind; callback-based |
| DSPy | Assert / Suggest decorators | Assert raises; Suggest soft-warns |
| Haystack | OutputValidator component | Explicitly named in Haystack 2.x |
| OpenAI | Moderation API (parallel check) | Safety check only; not structural |
| Anthropic | n/a (no native validator) | User-defined post-processing hook |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| checks | list[str] | [length, format] | More checks = safer; higher latency |
| on_fail | str | retry | retry / reject / warn / escalate |
| max_retries | int | 2 | Higher = quality; higher token cost |
| toxicity_threshold | float | 0.8 | Lower = stricter; more false positives |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Parse-then-validate | Structured output pipelines | Parse JSON block; validate required fields |
| Retry on fail | Critical quality-gated pipelines | Re-prompt with error context up to max_retries |
| Parallel safety check | High-risk user-facing content | Run Moderation API async alongside generation |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Validate after delivery | Too late to fix; user sees bad output | Always validate before delivery |
| Retry without modified prompt | Loops on identical failure indefinitely | Inject failure reason into retry prompt |
| Using P06 validator for raw LLM text | Wrong abstraction; P06 expects parsed object | P06 for schema; P05 output_validator for text |

## Integration Graph
```
[raw_llm_output] --> [output_validator] --> [validated_output / rejection_with_reason]
                           |
                  [checks, on_fail, max_retries]
                           |
               [formatter / delivery]  OR  [retry_loop --> LLM]
```

## Decision Tree
- IF output is already a parsed structured object THEN use validator (P06)
- IF output needs format transformation first THEN use formatter then validate
- IF need semantic field extraction THEN use parser
- DEFAULT: output_validator for any raw LLM text quality or safety gate before delivery

## Quality Criteria
- GOOD: checks defined, on_fail strategy set, failures logged with raw output context
- GREAT: retry with enriched prompt, parallel safety check, structured failure report
- FAIL: validates after delivery, no on_fail strategy, P06 schema validator used on raw text

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_output_validator]] | sibling | 0.38 |
| [[output-validator-builder]] | downstream | 0.36 |
| [[p01_kc_parser]] | sibling | 0.36 |
| [[bld_examples_output_validator]] | downstream | 0.36 |
| [[p03_sp_output_validator_builder]] | downstream | 0.34 |
| [[p10_lr_output_validator_builder]] | downstream | 0.33 |
| [[bld_architecture_output_validator]] | downstream | 0.33 |
| [[p01_kc_response_format]] | sibling | 0.33 |
| [[p01_kc_validation_schema]] | sibling | 0.32 |
| [[p01_kc_validator]] | sibling | 0.30 |
