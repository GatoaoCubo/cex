---
id: p03_cs_json_output
kind: constraint_spec
pillar: P03
title: Structured JSON Output Constraint (answer + confidence)
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: constrained_generation
quality: 9.1
tags: [constraint-spec, json-schema, structured-output, instructor, openai, anthropic, google]
tldr: Constraint que forca LLM a gerar JSON valido com campos answer e confidence — compativel com OpenAI response_format, Anthropic tool_use, e Google responseSchema
when_to_use: Quando output do LLM deve ser JSON parseavel com campos obrigatorios e tipos definidos — especialmente em pipelines automatizados sem intervencao humana
---

# Constraint Spec: Structured JSON Output (answer + confidence)

## Overview
Especificacao de constraint para forcar LLMs a gerar output JSON estruturado com dois campos obrigatorios: `answer` (resposta do modelo) e `confidence` (nivel de confianca 0.0-1.0). Implementado via mecanismos nativos de cada provider para maximo enforcement — nao depende de prompt engineering sozinho.

## Schema
```json
{
  "type": "object",
  "properties": {
    "answer": {
      "type": "string",
      "description": "Resposta principal do modelo ao prompt",
      "minLength": 1,
      "maxLength": 4096
    },
    "confidence": {
      "type": "number",
      "description": "Confianca do modelo na resposta (0.0 = nenhuma, 1.0 = total)",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "reasoning": {
      "type": "string",
      "description": "Raciocinio opcional que levou a resposta"
    }
  },
  "required": ["answer", "confidence"],
  "additionalProperties": false
}
```

## Provider Implementations

### OpenAI (response_format)
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "answer_with_confidence",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "answer": {"type": "string"},
                    "confidence": {"type": "number"},
                    "reasoning": {"type": "string"}
                },
                "required": ["answer", "confidence"],
                "additionalProperties": False
            }
        }
    }
)
result = json.loads(response.choices[0].message.content)
```

### Anthropic (tool_use como structured output)
```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=[{
        "name": "structured_answer",
        "description": "Provide a structured answer with confidence score",
        "input_schema": {
            "type": "object",
            "properties": {
                "answer": {"type": "string", "description": "Resposta principal"},
                "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
                "reasoning": {"type": "string"}
            },
            "required": ["answer", "confidence"]
        }
    }],
    tool_choice={"type": "tool", "name": "structured_answer"},
    messages=[{"role": "user", "content": prompt}]
)
result = response.content[0].input  # dict com answer + confidence
```

### Google Gemini (responseSchema)
```python
import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "answer": {"type": "string"},
                "confidence": {"type": "number"},
                "reasoning": {"type": "string"}
            },
            "required": ["answer", "confidence"]
        }
    )
)
response = model.generate_content(prompt)
result = json.loads(response.text)
```

### Instructor (universal wrapper)
```python
import instructor
from pydantic import BaseModel, Field

class AnswerWithConfidence(BaseModel):
    answer: str = Field(description="Resposta principal")
    confidence: float = Field(ge=0.0, le=1.0, description="Confianca 0-1")
    reasoning: str | None = Field(default=None, description="Raciocinio opcional")

# Funciona com qualquer provider
client = instructor.from_anthropic(anthropic.Anthropic())
result = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}],
    response_model=AnswerWithConfidence,
    max_retries=2,
)
# result e uma instancia de AnswerWithConfidence, ja validada
```

## Enforcement Levels
| Level | Mechanism | Guarantee | Latency Impact |
|-------|-----------|-----------|----------------|
| Native schema | Provider response_format / tool_use | 100% valid JSON | +0ms (built-in) |
| Instructor | Pydantic validation + auto-retry | 99.9% (retry on fail) | +200ms (retry) |
| Prompt-only | "Respond in JSON with answer and confidence" | ~85% (model may deviate) | +0ms |
| Post-parse | json.loads() + jsonschema.validate() | Detect-only, no fix | +5ms |

## Validation Pipeline
```text
[LLM Output] --> [json.loads()] --> valid JSON?
                                      |
                           no --------+-------- yes
                           |                     |
                    [retry with              [Schema Validate]
                     "fix this JSON"]              |
                           |              valid schema?
                           |                |         |
                           |          no ---+--- yes -+
                           |          |               |
                           |   [retry with        [Return]
                           |    schema hint]
                           |          |
                           +----------+
                           max_retries=2 exceeded?
                                |
                         [Raise ConstraintError]
```

## When NOT to Use
- Free-form creative text (poetry, stories) — constraint mata criatividade
- Streaming responses — JSON parcial nao e parseavel ate completar
- Simple yes/no — overhead desnecessario, usar prompt constraint

## Related
- `ex_few_shot_product_extraction.md` — Few-shot com JSON output similar
- `ex_response_format_ad_copy.md` — Response format para copy (nao JSON strict)
- `ex_chain_content_pipeline.md` — Pipeline que usa JSON contracts entre steps
