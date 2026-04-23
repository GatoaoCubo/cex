---
kind: output_template
id: bld_output_template_guardrail
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for guardrail production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p11_qg_guardrail
  - p10_lr_guardrail_builder
  - bld_instruction_guardrail
  - bld_schema_guardrail
  - bld_architecture_guardrail
  - bld_config_guardrail
  - bld_knowledge_card_guardrail
  - guardrail-builder
  - bld_examples_guardrail
  - p03_sp_guardrail_builder
---

# Output Template: guardrail
```yaml
id: p11_gr_{{scope_slug}}
kind: guardrail
pillar: P11
title: "Guardrail: {{guardrail_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_this_protects}}"
severity: "{{critical_or_high_or_medium_or_low}}"
enforcement: "{{block_or_warn_or_log}}"
applies_to: [{{agent_kind_1}}, {{agent_kind_2}}]
domain: "{{domain_value}}"
quality: null
tags: [guardrail, {{scope}}, {{severity}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
bypass_approver: "{{who_can_override}}"
remediation: "{{how_to_fix_violation}}"
linked_artifacts:
  primary: "{{related_law_or_gate}}"
  related: [{{related_refs}}]
## Definition
{{what_it_protects_and_threat_model}}
## Rules
1. {{concrete_measurable_restriction_1}}
2. {{concrete_measurable_restriction_2}}
3. {{concrete_measurable_restriction_3}}
## Violations
| Violation | Severity | Example |
|-----------|----------|---------|
| {{violation_1}} | {{severity}} | {{concrete_example}} |
| {{violation_2}} | {{severity}} | {{concrete_example}} |
## Enforcement
| Check | Method | Trigger |
|-------|--------|---------|
| {{check_1}} | {{automated_or_manual}} | {{when_checked}} |
| {{check_2}} | {{automated_or_manual}} | {{when_checked}} |
## Bypass
- Conditions: {{when_bypass_is_allowed}}
- Approver: {{who_approves}}
- Audit: {{how_bypass_is_logged}}
## References
- {{reference_1}}
- {{reference_2}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_guardrail]] | downstream | 0.45 |
| [[p10_lr_guardrail_builder]] | downstream | 0.42 |
| [[bld_instruction_guardrail]] | upstream | 0.42 |
| [[bld_schema_guardrail]] | downstream | 0.41 |
| [[bld_architecture_guardrail]] | downstream | 0.41 |
| [[bld_config_guardrail]] | downstream | 0.40 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.39 |
| [[guardrail-builder]] | downstream | 0.38 |
| [[bld_examples_guardrail]] | downstream | 0.35 |
| [[p03_sp_guardrail_builder]] | upstream | 0.35 |
