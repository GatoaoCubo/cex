---
kind: output_template
id: bld_output_template_audit_log
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for audit_log production
quality: 8.7
title: "Output Template Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, output_template]
tldr: "Template with vars for audit_log production"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p11_al_{{name}}.md
name: {{audit_log_name}}
description: <!-- Brief description of the audit log purpose -->
version: {{version}}
quality: null
log_type: {{log_type}}
retention_period: {{retention_days}}
sample_data:
  - timestamp: <!-- ISO 8601 date/time -->
    user: <!-- User ID or system name -->
    action: <!-- Action performed -->
    status: <!-- Success/failure indicator -->
```

| Timestamp       | User    | Action        | Status  |
|-----------------|---------|---------------|---------|
| 2023-10-01T08:00 | user123 | login         | success |
| 2023-10-01T08:05 | admin   | config_change | success |

```json
{
  "event_id": "p11_al_{{event_id}}",
  "details": {
    "resource": "{{resource_name}}",
    "operation": "{{operation_type}}"
  }
}
```
