---
kind: output_template
id: bld_output_template_consolidation_policy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for consolidation_policy production
quality: null
title: "Output Template Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, output_template]
tldr: "Template with vars for consolidation_policy production"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p10_cp_{{name}}.md
name: {{policy_name}}
description: {{policy_description}}
scope: {{policy_scope}}
policy_rules:
  - rule_id: {{rule_id}}
    description: {{rule_description}}
    owner: {{rule_owner}}
compliance_checklist:
  - {{checklist_item}}
effective_date: {{effective_date}}
version: {{version}}
quality: null
---
```

<!-- id: p10_cp_[a-z][a-z0-9_]+.md$ -->
<!-- name: Policy title (e.g., "Data Retention") -->
<!-- description: Brief summary of policy purpose -->
<!-- scope: Departments/regions affected (e.g., "Global") -->
<!-- rule_id: Unique identifier (e.g., "P10-DR-001") -->
<!-- rule_description: Specific requirement text -->
<!-- rule_owner: Responsible team/department -->
<!-- checklist_item: Compliance verification task -->
<!-- effective_date: YYYY-MM-DD -->
<!-- version: Policy iteration number (e.g., "1.0") -->

| Rule ID    | Description                  | Owner     |
|------------|------------------------------|-----------|
| {{rule_id}} | {{rule_description}}         | {{owner}} |

```yaml
compliance_checklist:
  - {{checklist_item}} <!-- e.g., "Verify data retention periods annually" -->
  - {{checklist_item}} <!-- e.g., "Audit access logs quarterly" -->
```
