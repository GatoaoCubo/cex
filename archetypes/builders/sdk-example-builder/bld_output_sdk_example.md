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
related:
  - kc_sdk_example
  - bld_config_sdk_example
  - sdk-example-builder
  - bld_schema_sdk_example
  - bld_collaboration_sdk_example
  - bld_output_template_playground_config
  - p01_kc_api_client
  - api-client-builder
  - bld_architecture_client
  - p11_qg_client
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_sdk_example]] | upstream | 0.39 |
| [[bld_config_sdk_example]] | downstream | 0.38 |
| [[sdk-example-builder]] | upstream | 0.31 |
| [[bld_schema_sdk_example]] | downstream | 0.30 |
| [[bld_collaboration_sdk_example]] | downstream | 0.30 |
| [[bld_output_template_playground_config]] | sibling | 0.26 |
| [[p01_kc_api_client]] | upstream | 0.25 |
| [[api-client-builder]] | upstream | 0.24 |
| [[bld_architecture_client]] | downstream | 0.23 |
| [[p11_qg_client]] | downstream | 0.23 |
