---
kind: output_template
id: bld_output_template_lifecycle_rule
pillar: P00
quality: 9.0
title: "Output Template Lifecycle Rule"
version: "1.0.0"
author: n03_builder
tags: [lifecycle_rule, builder, examples]
tldr: "Golden and anti-examples for lifecycle rule construction, demonstrating ideal structure and common pitfalls."
domain: "lifecycle rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
related:
  - bld_output_template_runtime_state
  - bld_schema_lifecycle_rule
  - p03_ins_lifecycle_rule
  - p03_sp_lifecycle_rule_builder
  - p11_qg_lifecycle_rule
  - bld_architecture_lifecycle_rule
  - bld_knowledge_card_lifecycle_rule
  - bld_manifest_lifecycle_rule
  - bld_output_template_golden_test
  - bld_memory_lifecycle_rule
---
```yaml
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for lifecycle_rule production
pattern: derives from SCHEMA.md — no extra fields
```
# Output Template: lifecycle_rule
```yaml
id: p11_lc_{{rule_slug}}
kind: lifecycle_rule
pillar: P11
title: "Lifecycle: {{rule_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_artifact_kind_this_governs}}"
freshness_days: {{integer_days_before_stale}}
review_cycle: "{{weekly_or_monthly_or_quarterly_or_yearly}}"
ownership: "{{who_is_responsible}}"
domain: "{{domain_value}}"
quality: null
tags: [lifecycle-rule, {{scope}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
notification: "{{signal_or_email_or_log_or_none}}"
automation: "{{full_or_semi_or_manual}}"
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{related_gate_or_law}}"
  related: [{{related_refs}}]
## Definition
{{what_artifact_kind_it_governs_and_why_freshness_matters}}
## States
| State | Entry Criteria | Duration | Next |
|-------|---------------|----------|------|
| {{state_1}} | {{how_artifact_enters_state}} | {{typical_duration}} | {{possible_next_states}} |
| {{state_2}} | {{how_artifact_enters_state}} | {{typical_duration}} | {{possible_next_states}} |
| {{state_3}} | {{how_artifact_enters_state}} | {{typical_duration}} | {{possible_next_states}} |
## Transitions
| From | To | Trigger | Action | Automated |
|------|----|---------|--------|-----------|
| {{state_a}} | {{state_b}} | {{what_causes_transition}} | {{what_happens}} | {{yes_or_no}} |
| {{state_b}} | {{state_c}} | {{what_causes_transition}} | {{what_happens}} | {{yes_or_no}} |
| {{state_c}} | {{state_d}} | {{what_causes_transition}} | {{what_happens}} | {{yes_or_no}} |
## Review Protocol
| Aspect | Value |
|--------|-------|
| Reviewer | {{who_reviews}} |
| Cycle | {{review_cycle_value}} |
| Checklist | {{what_reviewer_checks}} |
| Outcome | {{promote_or_archive_or_extend}} |
## Automation
| Transition | Method | Trigger |
|------------|--------|---------|
| {{auto_transition_1}} | {{cron_or_hook_or_manual}} | {{when_triggered}} |
| {{auto_transition_2}} | {{cron_or_hook_or_manual}} | {{when_triggered}} |
## References
- {{reference_1}}
- {{reference_2}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_runtime_state]] | sibling | 0.38 |
| [[bld_schema_lifecycle_rule]] | related | 0.30 |
| [[p03_ins_lifecycle_rule]] | related | 0.29 |
| [[p03_sp_lifecycle_rule_builder]] | related | 0.28 |
| [[p11_qg_lifecycle_rule]] | related | 0.28 |
| [[bld_architecture_lifecycle_rule]] | related | 0.28 |
| [[bld_knowledge_card_lifecycle_rule]] | related | 0.27 |
| [[bld_manifest_lifecycle_rule]] | related | 0.27 |
| [[bld_output_template_golden_test]] | sibling | 0.26 |
| [[bld_memory_lifecycle_rule]] | related | 0.25 |
