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
related:
  - bld_output_template_sales_playbook
  - bld_output_template_course_module
  - bld_schema_visual_workflow
  - bld_schema_integration_guide
  - bld_output_template_prompt_template
  - bld_output_template_workflow
  - bld_config_visual_workflow
  - bld_schema_audit_log
  - bld_output_template_user_journey
  - bld_output_template_quality_gate
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_sales_playbook]] | sibling | 0.26 |
| [[bld_output_template_course_module]] | sibling | 0.22 |
| [[bld_schema_visual_workflow]] | downstream | 0.20 |
| [[bld_schema_integration_guide]] | downstream | 0.20 |
| [[bld_output_template_prompt_template]] | sibling | 0.20 |
| [[bld_output_template_workflow]] | sibling | 0.20 |
| [[bld_config_visual_workflow]] | downstream | 0.19 |
| [[bld_schema_audit_log]] | downstream | 0.19 |
| [[bld_output_template_user_journey]] | sibling | 0.18 |
| [[bld_output_template_quality_gate]] | sibling | 0.18 |
