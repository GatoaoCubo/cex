---
kind: output_template
id: bld_output_template_visual_workflow
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for visual_workflow production
quality: 8.7
title: "Output Template Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, output_template]
tldr: "Template with vars for visual_workflow production"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
```yaml
---
id: p12_vw_{{name}}.md <!-- ^p12_vw_[a-z][a-z0-9_]+.md$ -->
title: {{title}} <!-- Workflow title -->
description: {{description}} <!-- Brief purpose -->
author: {{author}} <!-- Owner -->
version: {{version}} <!-- vX.X -->
quality: null <!-- Must be null -->
created: {{created}} <!-- YYYY-MM-DD -->
updated: {{updated}} <!-- YYYY-MM-DD -->
---
```

| Step | Action | Responsible |
|------|--------|-------------|
| 1    | Start  | {{user}}    |
| 2    | Review | {{team}}    |

```python
# Example script
def workflow_step():
    print("{{step_name}} executed by {{role}}")
```
```
