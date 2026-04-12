---
id: kc_type_safe_llm_outputs
kind: knowledge_card
title: "Type-Safe LLM Output Patterns"
version: 1.0.0
quality: null
pillar: P01
language: English
---

# Type-Safe LLM Output Patterns

Structured output patterns ensure LLM responses match expected schemas. Key approaches include:

## 1. Pydantic Models
```python
from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    unit: str = "Celsius"

response = WeatherResponse.model_validate({
    "city": "Paris",
    "temperature": 19.5
})
```

## 2. Zod Schemas
```typescript
import * as z from 'zod'

const weatherSchema = z.object({
    city: z.string(),
    temperature: z.number(),
    unit: z.string().optional()
})

const result = weatherSchema.parse({
    city: "Tokyo",
    temperature: 25
})
```

## 3. JSON Schema
```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "author": {"type": "string"},
        "year": {"type": "integer"}
    }
}
```

## 4. Instructor Library
```python
from instructor import instructor

model = instructor.from_open_ai(model="gpt-3.5-turbo")
response = model.call({
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "What's the weather in London?"}],
    "response_model": WeatherResponse
})
```

## 5. Structured Generation
```python
from instructor import StructuredOutput

response = StructuredOutput(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Show me a poem about AI"}],
    response_model=PoemModel
).invoke()
```

**Validation**: All approaches include schema validation during deserialization. Pydantic and Zod provide detailed error messages for schema violations. JSON Schema validation is typically done via JSON Schema validators. The instructor library integrates validation directly into the LLM call workflow.
```