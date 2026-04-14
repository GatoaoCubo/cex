---
kind: output_template
id: bld_output_template_agentic_rag
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for agentic_rag production
quality: null
title: "Output Template Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, output_template]
tldr: "Template with vars for agentic_rag production"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p01_ar_{{name}}.md
name: {{name}}
kind: agentic_rag
quality: null
description: {{description}} <!-- High-level purpose of this template -->
schema: {{schema}} <!-- JSON schema for data structure -->
example_data:
  - {{field1}}: {{value1}} <!-- Sample row 1 -->
  - {{field2}}: {{value2}} <!-- Sample row 2 -->
queries:
  - {{query1}} <!-- Example query -->
  - {{query2}} <!-- Example query -->
---
| Field     | Description          |
|-----------|----------------------|
| {{field1}} | {{field1_description}} |
| {{field2}} | {{field2_description}} |

```python
# Example code block
def {{function_name}}():
    """{{function_description}}"""
    return {{return_value}} <!-- Result placeholder -->
```
