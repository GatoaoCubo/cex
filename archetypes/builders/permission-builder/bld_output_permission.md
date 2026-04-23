---
kind: output_template
id: bld_output_template_permission
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for permission production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Permission"
version: "1.0.0"
author: n03_builder
tags: [permission, builder, examples]
tldr: "Golden and anti-examples for permission construction, demonstrating ideal structure and common pitfalls."
domain: "permission construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_permission
  - bld_schema_permission
  - p11_qg_permission
  - p03_sp_permission_builder
  - bld_examples_permission
  - permission-builder
  - bld_knowledge_card_permission
  - p09_perm_{{SCOPE_SLUG}}
  - bld_collaboration_permission
  - bld_architecture_permission
---

# Output Template: permission
```yaml
id: p09_perm_{{scope_slug}}
kind: permission
pillar: P09
title: "Permission: {{permission_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_resource_controlled}}"
roles: [{{role_1}}, {{role_2}}]
read: "{{allow_or_deny_or_conditional}}"
write: "{{allow_or_deny_or_conditional}}"
execute: "{{allow_or_deny_or_conditional}}"
quality: null
tags: [permission, {{scope}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
domain: "{{domain_value}}"
density_score: {{0.80_to_1.00}}
inheritance: "{{role_hierarchy_description}}"
escalation: "{{how_to_request_elevated_access}}"
linked_artifacts:
  primary: "{{related_guardrail_or_law}}"
  related: [{{related_refs}}]
## Scope
{{what_resource_and_why_access_control_needed}}
## Access Matrix
| Role | Read | Write | Execute | Conditions |
|------|------|-------|---------|------------|
| {{role_1}} | {{allow_deny_cond}} | {{allow_deny_cond}} | {{allow_deny_cond}} | {{conditions}} |
| {{role_2}} | {{allow_deny_cond}} | {{allow_deny_cond}} | {{allow_deny_cond}} | {{conditions}} |
## Allow List
1. {{role}}: {{action}} on {{resource}} — {{justification}}
2. {{role}}: {{action}} on {{resource}} — {{justification}}
## Deny List
1. {{role}}: {{action}} on {{resource}} — {{reason_for_denial}}
2. {{role}}: {{action}} on {{resource}} — {{reason_for_denial}}
## Audit
| Event | Logged | Retention | Alert |
|-------|--------|-----------|-------|
| {{access_event_1}} | {{yes_no}} | {{duration}} | {{threshold}} |
| {{access_event_2}} | {{yes_no}} | {{duration}} | {{threshold}} |
## Escalation
- Request method: {{how_to_request}}
- Approver: {{who_approves}}
- Duration: {{temporary_or_permanent}}
- Audit: {{how_escalation_is_logged}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_permission]] | upstream | 0.42 |
| [[bld_schema_permission]] | downstream | 0.39 |
| [[p11_qg_permission]] | downstream | 0.38 |
| [[p03_sp_permission_builder]] | upstream | 0.38 |
| [[bld_examples_permission]] | downstream | 0.37 |
| [[permission-builder]] | downstream | 0.36 |
| [[bld_knowledge_card_permission]] | upstream | 0.36 |
| [[p09_perm_{{SCOPE_SLUG}}]] | downstream | 0.36 |
| [[bld_collaboration_permission]] | downstream | 0.31 |
| [[bld_architecture_permission]] | downstream | 0.30 |
