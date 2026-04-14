---
kind: output_template
id: bld_output_template_product_tour
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for product_tour production
quality: null
title: "Output Template Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, output_template]
tldr: "Template with vars for product_tour production"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
title: {{title}} <!-- Product tour title -->
id: p05_pt_{{name}} <!-- Must match ^p05_pt_[a-z][a-z0-9_]+.md$ -->
pillar: P05 <!-- Always P05 -->
quality: null <!-- Always null -->
sections:
  - title: {{section1_title}} <!-- First section heading -->
    content: {{section1_content}} <!-- Markdown or code -->
    type: {{section1_type}} <!-- e.g., "description", "code" -->
  - title: {{section2_title}} <!-- Second section heading -->
    content: {{section2_content}} <!-- Markdown or code -->
    type: {{section2_type}} <!-- e.g., "table", "example" -->
---
```

| Step | Description          |
|------|----------------------|
| 1    | {{step1_description}} <!-- User onboarding step -->
| 2    | {{step2_description}} <!-- Key feature highlight -->

```python
# {{code_example_name}} <!-- Sample API call or code -->
def {{function_name}}():
    <!-- Code logic here -->
    pass
```
