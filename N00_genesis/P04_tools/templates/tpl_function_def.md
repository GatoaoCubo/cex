---
id: p04_function_def_NAME
kind: function_def
8f: F6_produce
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
related:
  - p04_fn_content_monetization
  - p03_ch_content_pipeline
  - bld_output_template_function_def
  - p11_qg_function_def
  - bld_output_template_workflow_node
  - p03_ch_kc_to_notebooklm
  - p03_react_web_research
  - bld_examples_function_def
  - bld_examples_workflow_primitive
  - bld_knowledge_card_function_def
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_content_monetization]] | sibling | 0.32 |
| [[p03_ch_content_pipeline]] | upstream | 0.31 |
| [[bld_output_template_function_def]] | downstream | 0.31 |
| [[p11_qg_function_def]] | downstream | 0.29 |
| [[bld_output_template_workflow_node]] | downstream | 0.29 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.29 |
| [[p03_react_web_research]] | upstream | 0.29 |
| [[bld_examples_function_def]] | downstream | 0.28 |
| [[bld_examples_workflow_primitive]] | downstream | 0.27 |
| [[bld_knowledge_card_function_def]] | upstream | 0.27 |
