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
