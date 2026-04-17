---
id: p04_function_def_NAME
kind: function_def
pillar: P04
version: 1.0.0
title: "Template — Function Definition"
tags: [template, function, tool-use, api, schema]
tldr: "Defines a tool function for LLM tool-use. Specifies name, description, parameters (JSON Schema), return type, and error contract for structured function calling."
quality: 9.0
domain: "tool integration"
density_score: 0.88
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
---

# Function Definition: [NAME]

## Purpose
[WHAT this function does when called by an LLM agent]

## Schema (OpenAI/Anthropic format)
```json
{
  "name": "[function_name]",
  "description": "[1-2 sentence description for the LLM]",
  "parameters": {
    "type": "object",
    "properties": {
      "param_1": {
        "type": "string",
        "description": "[What this parameter controls]"
      },
      "param_2": {
        "type": "integer",
        "description": "[What this parameter controls]",
        "default": 10
      }
    },
    "required": ["param_1"]
  }
}
```

## Parameter Reference

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| param_1 | string | yes | — | [DESCRIPTION] |
| param_2 | integer | no | 10 | [DESCRIPTION] |
| param_3 | boolean | no | false | [DESCRIPTION] |

## Return Type
```json
{
  "type": "object",
  "properties": {
    "result": { "type": "string" },
    "status": { "type": "string", "enum": ["success", "error"] },
    "metadata": { "type": "object" }
  }
}
```

## Error Contract
| Error | Condition | Response |
|-------|-----------|----------|
| ValidationError | Invalid parameters | `{"status": "error", "message": "..."}` |
| NotFoundError | Resource doesn't exist | `{"status": "error", "message": "..."}` |
| TimeoutError | Execution > timeout | `{"status": "error", "message": "..."}` |

## Usage Example
```python
# LLM generates this tool call:
result = await function_name(param_1="value", param_2=20)
# Returns: {"result": "...", "status": "success"}
```

## Quality Gate
- [ ] Description is ≤ 2 sentences (LLM context budget)
- [ ] All required parameters listed
- [ ] Return type documented
- [ ] Error contract covers validation + not_found + timeout
