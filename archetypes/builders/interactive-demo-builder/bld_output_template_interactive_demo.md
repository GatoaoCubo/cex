---
kind: output_template
id: bld_output_template_interactive_demo
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for interactive_demo production
quality: null
title: "Output Template Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, output_template]
tldr: "Template with vars for interactive_demo production"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
```yaml
---
title: "{{demo_title}}" <!-- Interactive demo title -->
description: "{{demo_summary}}" <!-- Brief overview of the demo -->
author: "{{author_name}}" <!-- Name of the creator -->
date: "{{creation_date}}" <!-- YYYY-MM-DD format -->
quality: null <!-- Must remain null -->
id: "p05_id_{{demo_name}}" <!-- Unique identifier per naming rules -->
---
```

## Demo Structure

| Step | Action | Outcome |
|------|--------|---------|
| 1 | Launch app | "Welcome screen displayed" |
| 2 | Click "Start" | "Tutorial begins" |

```python
# Sample code snippet
def interactive_step():
    user_input = input("Enter value: ")
    print(f"Received: {user_input}")
```

<!-- Replace {{demo_title}}, {{demo_summary}}, etc. with actual content -->
```
