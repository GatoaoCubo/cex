---
kind: output_template
id: bld_output_template_roi_calculator
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for roi_calculator production
quality: null
title: "Output Template Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, output_template]
tldr: "Template with vars for roi_calculator production"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p11_roi_{{id}}
name: {{name}}
description: {{description}}
parameters:
  - name: {{param1}}
    type: {{type1}}
  - name: {{param2}}
    type: {{type2}}
quality: null
---
```

<!-- id: Must match ^p11_roi_[a-z][a-z0-9_]+.yaml$ -->
<!-- name: Calculator name (e.g., "trading_roi") -->
<!-- description: Brief purpose explanation -->
<!-- param1: First input parameter (e.g., "initial_investment") -->
<!-- type1: Data type (e.g., "float") -->
<!-- param2: Second input parameter (e.g., "final_value") -->
<!-- type2: Data type (e.g., "float") -->

**Example Parameters Table:**
| Parameter         | Type   | Description              |
|-------------------|--------|--------------------------|
| initial_investment| float  | Starting capital         |
| final_value       | float  | Ending capital           |

**Usage Example:**
```python
def calculate_roi(initial, final):
    return (final - initial) / initial * 100
```
