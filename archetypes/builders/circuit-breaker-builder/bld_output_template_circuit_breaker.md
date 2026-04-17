---
kind: output_template
id: bld_output_template_circuit_breaker
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a circuit_breaker artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 7.5
title: "Output Template Circuit Breaker"
version: "1.0.0"
author: n03_builder
tags: [circuit_breaker, builder, output_template]
tldr: "Fill-in template for circuit_breaker: service, failure threshold, state machine, cooldown, probe, fallback."
domain: "circuit breaker construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Output Template: circuit_breaker

```yaml
id: p09_cb_{{service_slug}}
kind: circuit_breaker
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
service: "{{dependency_service_name}}"
failure_rate_threshold: {{integer_1_to_100}}
cooldown_duration: {{seconds_integer}}
probe_count: {{integer}}
sliding_window_type: "{{COUNT_BASED|TIME_BASED}}"
sliding_window_size: {{integer}}
minimum_number_of_calls: {{integer}}
slow_call_threshold_ms: {{integer_optional}}
fallback_response: "{{response_while_open}}"
monitored_exceptions: [{{ExceptionType1}}, {{ExceptionType2}}]
quality: null
tags: [circuit_breaker, {{service_slug}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Overview
`{{what_dependency_is_protected_and_why_1_to_2_sentences}}`

## State Machine
| State | Condition | Transitions To |
|-------|-----------|---------------|
| CLOSED | Normal operation | OPEN when failure_rate >= {{failure_rate_threshold}}% over last {{sliding_window_size}} {{calls|seconds}} |
| OPEN | Dependency disabled | HALF-OPEN after {{cooldown_duration}}s cooldown |
| HALF-OPEN | Recovery probe | CLOSED if {{probe_count}} probes succeed; OPEN if any probe fails |

## Cooldown
- Duration: {{cooldown_duration}} seconds
- Probe calls: {{probe_count}} requests allowed in HALF-OPEN
- Recovery criteria: `{{probe_count}}` consecutive successes
- Reset trigger: `{{what_triggers_reset_to_closed}}`

## Fallback
Response during OPEN state: `{{fallback_response}}`
Error code: `{{http_status_or_error_code}}`
SLA impact: `{{what_callers_experience_during_open}}`
