---
kind: output_template
id: bld_output_template_ecommerce_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for ecommerce_vertical production
quality: null
title: "Output Template Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, output_template]
tldr: "Template with vars for ecommerce_vertical production"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p01_ev_{{name}}.md
pillar: P01
kind: ecommerce_vertical
quality: null
description: {{description}} <!-- High-level purpose of this vertical -->
vertical: {{vertical}} <!-- E.g., "retail", "electronics" -->
metrics: {{metrics}} <!-- Key performance indicators -->
---
```

| Feature       | Value         | Notes                  |
|---------------|---------------|------------------------|
| Target Users  | {{user_type}} <!-- E.g., "B2C", "B2B" --> | User segmentation      |
| Revenue Model | {{revenue}}   <!-- E.g., "subscription", "transactional" --> | Monetization strategy  |

```python
# Example API endpoint
def get_product_data(vertical):
    """Fetch product catalog for {{vertical}}"""
    return {
        "category": "{{category}}", <!-- Product category -->
        "items": [{{item}}]          <!-- List of products -->
    }
```
