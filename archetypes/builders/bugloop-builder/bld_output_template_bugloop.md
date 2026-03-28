---
kind: output_template
id: bld_output_template_bugloop
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for bugloop production
pattern: derives from SCHEMA.md — no extra fields
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
- Trigger: {{when_detection_runs}}
- Pattern: {{what_signature_identifies_a_bug}}
- Sources: {{logs|tests|static_analysis|runtime}}
## Fix Strategy
{{describe_how_fix_is_applied}}
- Auto: {{yes_no_and_why}}
- Strategy rationale: {{why_this_strategy_for_this_domain}}
- Max attempts: {{N}} before escalation
## Verification
{{describe_how_fix_is_verified}}
- Suite: {{test_suite_name}}
- Pass criteria: {{what_must_hold_true}}
- Timeout: {{N}}s
## Escalation
{{describe_escalation_policy}}
- Triggers at cycle: {{N}}
- Target: {{human|system|queue}}
- Payload: {{what_info_is_sent}}
## Rollback
{{describe_rollback_conditions_and_procedure}}
- Enabled: {{true|false}}
- Strategy: {{git_revert|snapshot_restore|blue_green}}
- Trigger condition: {{when_rollback_fires}}
```
