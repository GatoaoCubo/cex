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
related:
  - bld_examples_workflow_node
  - bld_examples_workflow_primitive
  - p04_function_def_NAME
  - bld_output_template_playground_config
  - bld_output_template_input_schema
  - p11_qg_function_def
  - bld_examples_tts_provider
  - bld_output_template_workflow_primitive
  - bld_output_template_function_def
  - bld_output_template_sandbox_spec
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_workflow_node]] | downstream | 0.37 |
| [[bld_examples_workflow_primitive]] | downstream | 0.34 |
| [[p04_function_def_NAME]] | upstream | 0.30 |
| [[bld_output_template_playground_config]] | sibling | 0.27 |
| [[bld_output_template_input_schema]] | sibling | 0.25 |
| [[p11_qg_function_def]] | downstream | 0.25 |
| [[bld_examples_tts_provider]] | downstream | 0.23 |
| [[bld_output_template_workflow_primitive]] | sibling | 0.23 |
| [[bld_output_template_function_def]] | sibling | 0.22 |
| [[bld_output_template_sandbox_spec]] | sibling | 0.22 |
