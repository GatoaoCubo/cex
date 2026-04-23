---
kind: output_template
id: bld_output_template_prompt_optimizer
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for prompt_optimizer production
quality: 8.8
title: "Output Template Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, output_template]
tldr: "Template with vars for prompt_optimizer production"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_prompt_technique
  - bld_examples_prompt_optimizer
  - action-prompt-builder
  - bld_output_template_playground_config
  - p11_qg_function_def
  - bld_collaboration_action_prompt
  - bld_instruction_function_def
  - bld_output_template_workflow_node
  - prompt-version-builder
  - bld_examples_prompt_version
---

```yaml
---
id: p03_po_{{name}}.md
pillar: P03
kind: prompt_optimizer
quality: null
description: {{description}} <!-- Brief purpose of this optimizer -->
parameters: {{parameters}} <!-- JSON schema for input parameters -->
examples: {{examples}} <!-- List of example use cases -->
---
```

| Technique       | Input Prompt                          | Optimized Prompt                      |
|-----------------|---------------------------------------|---------------------------------------|
| Clarity Boost | "Make this better"                    | "Refine this text for clarity and impact" |
| Conciseness   | "Please explain this in detail"       | "Summarize this concisely"            |
| Tone Adjust   | "Write a formal email"                | "Compose a professional email"          |

```python
# Example code block
def optimize_prompt(input_text):
    """Apply P03 optimization rules"""
    # {{insert_optimization_logic_here}} <!-- Add specific transformation rules -->
    return transformed_text
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_prompt_technique]] | sibling | 0.25 |
| [[bld_examples_prompt_optimizer]] | downstream | 0.25 |
| [[action-prompt-builder]] | upstream | 0.24 |
| [[bld_output_template_playground_config]] | sibling | 0.22 |
| [[p11_qg_function_def]] | downstream | 0.21 |
| [[bld_collaboration_action_prompt]] | downstream | 0.21 |
| [[bld_instruction_function_def]] | upstream | 0.20 |
| [[bld_output_template_workflow_node]] | sibling | 0.20 |
| [[prompt-version-builder]] | upstream | 0.20 |
| [[bld_examples_prompt_version]] | downstream | 0.19 |
