---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for smoke_eval production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: smoke_eval

```yaml
---
id: p07_se_{{scope_slug}}
kind: smoke_eval
pillar: P07
title: "{{eval_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_is_being_tested}}"
critical_path:
  - "{{step_1}}"
  - "{{step_2}}"
  - "{{step_3}}"
timeout: {{max_30_seconds}}
assertions:
  - check: "{{what_to_verify}}"
    expected: "{{expected_result}}"
    timeout_ms: {{milliseconds}}
fast_fail: true
prerequisites:
  - "{{prerequisite_1}}"
  - "{{prerequisite_2}}"
environment: "{{target_environment}}"
health_check: "{{health_endpoint_or_check}}"
frequency: "{{how_often}}"
alerting: "{{who_to_notify}}"
domain: "{{domain_value}}"
quality: null
tags: [smoke-eval, {{scope}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
---

## Critical Path
{{ordered_minimum_checks}}

## Assertions
{{fast_binary_checks_with_timeouts}}

## Prerequisites
{{what_must_exist_before_running}}

## On Failure
{{action_on_failure}}
```
