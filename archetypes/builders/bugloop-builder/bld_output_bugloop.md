---
kind: output_template
id: bld_output_template_bugloop
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for bugloop production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.1
title: "Output Template Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_bugloop
  - bld_examples_bugloop
  - bld_config_bugloop
  - bld_schema_bugloop
  - bld_knowledge_card_bugloop
  - p03_sp_bugloop_builder
  - bugloop-builder
  - bld_architecture_bugloop
  - p11_qg_bugloop
  - p01_kc_bugloop
---

# Output Template: bugloop
```yaml
id: p11_bl_{{scope_slug}}
kind: bugloop
pillar: P11

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

domain: "{{system_or_module_monitored}}"
quality: null
tags: [bugloop, {{domain}}, {{trigger_type}}]
tldr: "{{one_sentence_what_cycle_detects_and_fixes}}"

scope: "{{what_this_bugloop_monitors}}"
detect:
  method: "{{static_analysis|runtime_trace|test_failure|log_scan}}"
  trigger: "{{on_commit|on_deploy|scheduled|continuous}}"

  pattern: "{{regex_or_failure_signature}}"
fix:
  strategy: "{{patch_and_retry|rollback_first|isolate_then_fix}}"
  auto_fix: {{true|false}}

  max_attempts: {{integer_1_to_10}}
verify:
  test_suite: "{{path_or_name_of_test_suite}}"
  assertions:

    - "{{assertion_1}}"
    - "{{assertion_2}}"
  timeout: {{seconds}}
cycle_count: {{max_iterations_before_escalation}}

auto_fix: {{true|false}}
escalation:
  threshold: {{cycle_number_that_triggers}}
  target: "{{who_or_what_receives_escalation}}"

confidence: {{0.0_to_1.0}}
test_suite: "{{canonical_path_or_name}}"
rollback:
  enabled: {{true|false}}

  strategy: "{{git_revert|snapshot_restore|blue_green}}"
## Detection
{{describe_how_bugs_are_detected}}
1. Trigger: {{when_detection_runs}}
2. Pattern: {{what_signature_identifies_a_bug}}
3. Sources: {{logs|tests|static_analysis|runtime}}
## Fix Strategy
{{describe_how_fix_is_applied}}
1. Auto: {{yes_no_and_why}}
2. Strategy rationale: {{why_this_strategy_for_this_domain}}
3. Max attempts: {{N}} before escalation
## Verification
{{describe_how_fix_is_verified}}
1. Suite: {{test_suite_name}}
2. Pass criteria: {{what_must_hold_true}}
3. Timeout: {{N}}s
## Escalation
{{describe_escalation_policy}}
1. Triggers at cycle: {{N}}
2. Target: {{human|system|queue}}
3. Payload: {{what_info_is_sent}}
## Rollback
{{describe_rollback_conditions_and_procedure}}
1. Enabled: {{true|false}}
2. Strategy: {{git_revert|snapshot_restore|blue_green}}
3. Trigger condition: {{when_rollback_fires}}
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | bugloop construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_bugloop]] | upstream | 0.52 |
| [[bld_examples_bugloop]] | downstream | 0.49 |
| [[bld_config_bugloop]] | downstream | 0.45 |
| [[bld_schema_bugloop]] | downstream | 0.40 |
| [[bld_knowledge_card_bugloop]] | upstream | 0.37 |
| [[p03_sp_bugloop_builder]] | downstream | 0.37 |
| [[bugloop-builder]] | downstream | 0.37 |
| [[bld_architecture_bugloop]] | downstream | 0.36 |
| [[p11_qg_bugloop]] | downstream | 0.35 |
| [[p01_kc_bugloop]] | downstream | 0.31 |
