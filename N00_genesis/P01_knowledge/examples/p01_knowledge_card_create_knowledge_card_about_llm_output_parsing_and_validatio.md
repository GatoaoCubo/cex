---
id: p01_kc_llm_output_parsing_validation
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "LLM Output Parsing and Validation Patterns"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "knowledge-card-builder"
domain: llm_engineering
quality: 9.2
tags: [llm-parsing, output-validation, structured-generation, json-schema, pydantic, error-handling]
tldr: "LLM output validation uses JSON Schema + retry logic, achieving 95%+ parse success with Pydantic v2, exponential backoff, and format-specific prompting"
when_to_use: "When LLM generates structured data requiring programmatic consumption and validation"
keywords: [llm-parsing, json-schema, pydantic, structured-output, validation]
long_tails:
  - How to validate LLM JSON output with retry logic
  - Pydantic v2 parsing patterns for GPT-4 structured generation
  - JSON Schema validation for Claude API responses
axioms:
  - ALWAYS validate LLM output before business logic consumption
  - NEVER trust raw LLM text for structured data without schema validation
  - IF parse fails THEN retry with error context in prompt
linked_artifacts:
  primary: null
  related: [p01_kc_prompt_engineering, p01_kc_error_handling]
density_score: 0.87
data_source: "OpenAI Structured Outputs API, Pydantic v2 docs, JSON Schema spec"
related:
  - p01_kc_parser
  - p01_kc_response_format
  - p03_cs_json_output
  - bld_knowledge_card_output_validator
  - bld_knowledge_card_input_schema
  - tpl_response_format
  - p01_kc_self_healing
  - p01_kc_function_def
  - bld_config_validation_schema
  - p01_kc_validation_schema
---
# LLM Output Parsing and Validation Patterns

## Quick Reference
```yaml
topic: llm_output_validation
scope: JSON/YAML parsing with schema validation and retry logic
owner: llm_engineering
criticality: high
```

## Key Concepts
- **JSON Schema**: RFC 7159 validation with type constraints, required fields, format patterns
- **Pydantic v2**: 5-50x faster parsing than v1, native JSON Schema export, ValidationError details
- **Structured Outputs**: OpenAI native JSON mode (gpt-4o-mini+), 100% valid JSON guaranteed
- **Parse Success Rate**: Industry standard 95%+ with retry logic, 85% single-attempt baseline
- **Error Context**: Include parse error + malformed output in retry prompt for 40% improvement

## Strategy Phases
1. **Schema Design**: Define strict Pydantic models with Field constraints and examples
2. **Prompt Engineering**: Include JSON example + format instructions + error recovery hints
3. **Parse + Validate**: Try JSON.loads() → Pydantic.model_validate() with exception capture
4. **Retry Logic**: Max 3 attempts with exponential backoff (100ms, 500ms, 2s delays)
5. **Fallback**: Graceful degradation or human review queue for persistent failures

## Golden Rules
- VALIDATE twice: JSON syntax + business schema compliance
- RETRY with context: include previous error + malformed output in next prompt
- CONSTRAIN early: use Pydantic Field() with regex, min/max, enum constraints
- LOG failures: track parse error patterns for prompt optimization
- TIMEOUT parsing: 5s max for large JSON objects (10MB+ responses)

## Flow
```text
[LLM Response] → [JSON.loads()] → [Pydantic.validate()] → [Business Logic]
                       ↓ FAIL              ↓ FAIL              
                 [Retry Prompt] ← [Error Context + Sample]
```

## Comparativo
| Approach | Parse Rate | Latency | Use Case |
|----------|-----------|---------|----------|
| Raw JSON.loads() | 70-80% | 1ms | Simple structures, high tolerance |
| Pydantic v2 | 90-95% | 10ms | Business data, strict validation |
| OpenAI Structured | 99.9% | +50ms | Critical accuracy, GPT-4o only |
| Custom Parser | 85-90% | 5ms | Domain-specific formats, legacy |

## Validation Patterns
```python
# Pydantic v2 with retry
from pydantic import BaseModel, Field, ValidationError
import json
from typing import Optional

class LLMOutput(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    confidence: float = Field(ge=0.0, le=1.0)
    tags: list[str] = Field(min_items=1, max_items=10)
    
def parse_with_retry(response: str, max_attempts: int = 3) -> Optional[LLMOutput]:
    for attempt in range(max_attempts):
        try:
            data = json.loads(response)
            return LLMOutput.model_validate(data)
        except (json.JSONDecodeError, ValidationError) as e:
            if attempt == max_attempts - 1:
                return None
            # Include error in retry prompt
            response = retry_llm_call(f"Parse error: {e}\nFix this JSON: {response}")
```

## Error Patterns
| Error Type | Frequency | Fix Strategy |
|------------|-----------|--------------|
| Trailing comma | 15% | Prompt: "no trailing commas in JSON" |
| Missing quotes | 12% | Include correct JSON example in prompt |
| Wrong data type | 8% | Use Pydantic Field() constraints |
| Extra fields | 5% | Set `model_config = {"extra": "forbid"}` |

## References
- OpenAI Structured Outputs: https://platform.openai.com/docs/guides/structured-outputs
- Pydantic v2 Performance: https://docs.pydantic.dev/latest/concepts/performance/
- JSON Schema Specification: https://json-schema.org/draft/2020-12/schema

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_parser]] | sibling | 0.33 |
| [[p01_kc_response_format]] | sibling | 0.31 |
| [[p03_cs_json_output]] | downstream | 0.30 |
| [[bld_knowledge_card_output_validator]] | sibling | 0.28 |
| [[bld_knowledge_card_input_schema]] | sibling | 0.26 |
| [[tpl_response_format]] | downstream | 0.25 |
| [[p01_kc_self_healing]] | sibling | 0.24 |
| [[p01_kc_function_def]] | sibling | 0.23 |
| [[bld_config_validation_schema]] | downstream | 0.22 |
| [[p01_kc_validation_schema]] | sibling | 0.22 |
