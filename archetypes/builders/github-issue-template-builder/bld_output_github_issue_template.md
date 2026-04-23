---
kind: output_template
id: bld_output_template_github_issue_template
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for github_issue_template production
quality: 8.8
title: "Output Template Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, output_template]
tldr: "Template with vars for github_issue_template production"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_github_issue_template
  - kc_github_issue_template
  - p05_qg_github_issue_template
  - bld_instruction_github_issue_template
  - github-issue-template-builder
  - p03_sp_github_issue_template_builder
  - bld_output_template_sales_playbook
  - p10_mem_github_issue_template_builder
  - bld_knowledge_card_github_issue_template
  - bld_output_template_visual_workflow
---

```markdown
```yaml
title: "{{title}}"
description: "{{description}}"
labels: ["{{labels}}"]
assignees: ["{{assignees}}"]
milestone: "{{milestone}}"
id: "p05_git_{{name}}.md"
quality: null
```
<!-- title: Issue title -->
<!-- description: Detailed problem summary -->
<!-- labels: Comma-separated labels (e.g., bug,feature) -->
<!-- assignees: Comma-separated GitHub usernames -->
<!-- milestone: Project milestone name -->
<!-- name: Unique identifier (lowercase, underscores) -->

## Example Table
| Step | Action | Result |
|------|--------|--------|
| 1    | Click button | Error occurs |
| 2    | Reload page | Issue persists |

## Example Code
```python
def faulty_function():
    return 1 / 0  # Raises ZeroDivisionError
```
<!-- Include code blocks for errors, logs, or repro steps -->
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_github_issue_template]] | downstream | 0.35 |
| [[kc_github_issue_template]] | upstream | 0.32 |
| [[p05_qg_github_issue_template]] | downstream | 0.29 |
| [[bld_instruction_github_issue_template]] | upstream | 0.25 |
| [[github-issue-template-builder]] | related | 0.24 |
| [[p03_sp_github_issue_template_builder]] | upstream | 0.24 |
| [[bld_output_template_sales_playbook]] | sibling | 0.24 |
| [[p10_mem_github_issue_template_builder]] | downstream | 0.23 |
| [[bld_knowledge_card_github_issue_template]] | upstream | 0.23 |
| [[bld_output_template_visual_workflow]] | sibling | 0.18 |
