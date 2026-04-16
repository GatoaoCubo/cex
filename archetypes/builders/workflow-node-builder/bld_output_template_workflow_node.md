---
kind: output_template
id: bld_output_template_workflow_node
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for workflow_node production
quality: 8.7
title: "Output Template Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, output_template]
tldr: "Template with vars for workflow_node production"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: {{id}} <!-- ^p12_wn_[a-z][a-z0-9_]+.md$ -->
name: {{name}} <!-- Node display name -->
description: {{description}} <!-- Purpose/behavior summary -->
type: {{type}} <!-- E.g., "data_transform", "validation" -->
inputs: {{inputs}} <!-- List of required input fields -->
outputs: {{outputs}} <!-- List of generated output fields -->
parameters: {{parameters}} <!-- Configurable options -->
quality: {{quality}} <!-- MUST be: null -->
status: {{status}} <!-- "draft", "review", "production" -->
---
```

**Description**  
{{description}} <!-- Explain node's role in workflow -->

**Inputs/Outputs**  
| Name      | Type   | Description                  |
|-----------|--------|------------------------------|
| {{input1}} | {{type}} | {{purpose}}                |
| {{input2}} | {{type}} | {{purpose}}                |

**Configuration Example**  
```yaml
parameters:
  {{param1}}: {{value}} <!-- {{comment}} -->
  {{param2}}: {{value}} <!-- {{comment}} -->
```

**Parameters**  
- {{param1}}: {{description}} <!-- Configurable setting -->
- {{param2}}: {{description}} <!-- Default: {{default}} -->

**Status**  
{{status}} <!-- Current lifecycle stage -->
