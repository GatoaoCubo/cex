---
kind: output_template
id: bld_output_template_sales_playbook
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sales_playbook production
quality: 8.8
title: "Output Template Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, output_template]
tldr: "Template with vars for sales_playbook production"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_visual_workflow
  - bld_output_template_sdk_example
  - bld_schema_sales_playbook
  - bld_examples_churn_prevention_playbook
  - bld_output_template_api_reference
  - bld_output_template_playground_config
  - bld_output_template_self_improvement_loop
  - bld_config_sales_playbook
  - bld_output_template_github_issue_template
  - bld_schema_few_shot_example
---

```yaml
---
id: p03_sp_{{name}}.md <!-- Filename following p03_sp_[a-z][a-z0-9_]+.md pattern -->
title: {{title}} <!-- Playbook title -->
author: {{author}} <!-- Author name -->
date: {{date}} <!-- Last updated date (YYYY-MM-DD) -->
quality: null <!-- Must remain null -->
description: {{description}} <!-- Summary of playbook purpose -->
keywords: {{keywords}} <!-- Comma-separated relevant terms -->
---
```

## Strategies

| Step | Action | Target |
|------|--------|--------|
| 1 | Identify high-value clients | {{client_segment}} <!-- Example: enterprise SaaS companies -->
| 2 | Schedule demo with CTO | {{demo_process}} <!-- Example: 30-min walkthrough -->
| 3 | Follow-up with tailored proposal | {{proposal_template}} <!-- Example: p03_sp_proposal_template.md -->

## Script Example

```python
def generate_proposal(client_name):
    # {{script_logic}} <!-- Example: Fetch client data from CRM -->
    return f"Proposal for {client_name} generated at {datetime.now()}"
```

<!-- Replace {{script_logic}} with actual code logic -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_visual_workflow]] | sibling | 0.25 |
| [[bld_output_template_sdk_example]] | sibling | 0.22 |
| [[bld_schema_sales_playbook]] | downstream | 0.21 |
| [[bld_examples_churn_prevention_playbook]] | downstream | 0.20 |
| [[bld_output_template_api_reference]] | sibling | 0.19 |
| [[bld_output_template_playground_config]] | sibling | 0.18 |
| [[bld_output_template_self_improvement_loop]] | sibling | 0.18 |
| [[bld_config_sales_playbook]] | downstream | 0.18 |
| [[bld_output_template_github_issue_template]] | sibling | 0.17 |
| [[bld_schema_few_shot_example]] | downstream | 0.17 |
