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
related:
  - bld_schema_audit_log
  - bld_output_template_user_journey
  - bld_output_template_workflow_node
  - bld_output_template_usage_quota
  - p06_security_validation_schema
  - bld_output_template_playground_config
  - p03_sp_audit_log_builder
  - p11_qg_audit_log
  - p04_function_def_NAME
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_audit_log]] | downstream | 0.19 |
| [[bld_output_template_user_journey]] | sibling | 0.16 |
| [[bld_output_template_workflow_node]] | sibling | 0.16 |
| [[bld_output_template_usage_quota]] | sibling | 0.16 |
| [[p06_security_validation_schema]] | downstream | 0.16 |
| [[bld_output_template_playground_config]] | sibling | 0.16 |
| [[p03_sp_audit_log_builder]] | upstream | 0.15 |
| [[p11_qg_audit_log]] | downstream | 0.15 |
| [[p04_function_def_NAME]] | upstream | 0.15 |
