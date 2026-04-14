---
kind: output_template
id: bld_output_template_procedural_memory
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for procedural_memory production
quality: null
title: "Output Template Procedural Memory"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [procedural_memory, builder, output_template]
tldr: "Template with vars for procedural_memory production"
domain: "procedural_memory construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p10_pm_{{name}}.md
name: {{name}}
kind: procedural_memory
pillar: P10
quality: null
description: {{description}}
tags: [{{tag1}}, {{tag2}}]
created_at: {{created_at}}
---
```

<!-- id: Unique identifier following p10_pm_[a-z][a-z0-9_]+.md -->
<!-- name: Human-readable memory name -->
<!-- description: Brief purpose of this procedural memory -->
<!-- tags: Relevant categorization labels -->
<!-- created_at: ISO 8601 timestamp -->

## Procedural Memory Overview
| Step | Action | Outcome |
|------|--------|---------|
| 1    | {{action1}} | {{result1}} |
| 2    | {{action2}} | {{result2}} |

```python
# Example procedural workflow
def {{function_name}}():
    """{{description}}"""
    try:
        {{code_block}}
    except Exception as e:
        print(f"Error: {e}")
```

<!-- action1: First operational step -->
<!-- result1: Expected outcome of first step -->
<!-- action2: Second operational step -->
<!-- result2: Expected outcome of second step -->
<!-- function_name: CamelCase function identifier -->
<!-- description: Function purpose in 1 line -->
<!-- code_block: 1-3 lines of core implementation -->
