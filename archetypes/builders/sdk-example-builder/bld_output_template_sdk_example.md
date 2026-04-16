---
kind: output_template
id: bld_output_template_sdk_example
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sdk_example production
quality: 8.9
title: "Output Template Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, output_template]
tldr: "Template with vars for sdk_example production"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p04_sdk_{{name}}.md
name: {{SDK Example Name}}
description: {{Brief description of the SDK example}}
quality: null
pillar: P04
category: sdk_example
---
```

<!-- Replace {{SDK Example Name}} with the specific SDK example name -->
<!-- Describe the purpose of this SDK example in 1-2 sentences -->
<!-- Ensure ID follows p04_sdk_[a-z][a-z0-9_]+.md pattern -->

### Example Usage
```python
from {{sdk_name}} import Client

client = Client(api_key="your_key")
response = client.get_data(endpoint="/v1/example")
print(response.json())
```

### Parameter Table
| Name      | Type   | Description                  |
|-----------|--------|------------------------------|
| api_key   | string | Authentication credential    |
| endpoint  | string | API endpoint path            |
| timeout   | int    | Request timeout in seconds   |

### Sample Response
```json
{
  "status": "success",
  "data": {"example_field": "value"}
}
```
