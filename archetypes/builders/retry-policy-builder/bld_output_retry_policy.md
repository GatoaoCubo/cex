---
quality: 8.6
quality: 8.0
kind: output_template
id: bld_output_template_retry_policy
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a retry_policy artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
title: "Output Template Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, output_template]
tldr: "Fill-in template for retry_policy: backoff config, jitter, retry budget, error classification."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_examples_runtime_rule
  - p01_kc_api_rate_limiting_retry_patterns
  - p01_kc_bugloop
  - bld_output_template_schedule
  - runtime-rule-builder
  - bld_memory_runtime_rule
  - p03_sp_runtime_rule_builder
  - p11_qg_bugloop
  - p01_kc_runtime_rule
  - p01_kc_llm_output_parsing_validation
---

# Output Template: retry_policy

```yaml
id: p09_rtp_{{operation_slug}}
kind: retry_policy
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
operation: "{{operation_name}}"
max_attempts: {{integer_3_to_10}}
initial_interval: {{milliseconds_integer}}
backoff_strategy: "{{exponential|linear|fixed|decorrelated}}"
backoff_multiplier: {{float_optional_for_exponential}}
max_interval: {{milliseconds_integer}}
jitter: "{{FULL|EQUAL|DECORRELATED|NONE}}"
retry_budget: {{integer_optional}}
retryable_errors: [{{HTTP_429}}, {{HTTP_503}}, {{ConnectionError}}, {{TimeoutError}}]
non_retryable_errors: [{{HTTP_400}}, {{HTTP_401}}, {{HTTP_403}}]
quality: null
tags: [retry_policy, {{operation_slug}}, {{domain_tag}}]
tldr: "{{operation}} retry: {{max_attempts}} attempts, {{backoff_strategy}} {{initial_interval}}ms->{{max_interval}}ms, {{jitter}} jitter, retries {{list_retryable}}."
```

## Retry Behavior

| Parameter | Value | Notes |
|-----------|-------|-------|
| max_attempts | {{max_attempts}} | {{1_initial_plus_N_retries}} |
| initial_interval | {{initial_interval}}ms | {{context}} |
| backoff_strategy | {{strategy}} | {{rationale}} |
| backoff_multiplier | {{multiplier}} | {{only_for_exponential}} |
| max_interval | {{max_interval}}ms | {{cap_rationale}} |
| jitter | {{jitter}} | {{thundering_herd_prevention}} |
| retry_budget | {{budget}} | {{concurrent_retry_limit}} |

## Backoff Calculation

| Attempt | Base Delay | With {{jitter}} Jitter | Notes |
|---------|------------|----------------------|-------|
| 1 | {{initial_interval}}ms | {{jitter_range}} | After first failure |
| 2 | {{attempt_2_delay}}ms | {{jitter_range_2}} | {{backoff_note}} |
| 3 | {{attempt_3_delay}}ms | {{jitter_range_3}} | {{backoff_note}} |

## Error Classification

| Error | Action | Reason |
|-------|--------|--------|
| {{retryable_error}} | RETRY | {{why_transient}} |
| {{non_retryable_error}} | FAIL IMMEDIATELY | {{why_permanent}} |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_runtime_rule]] | downstream | 0.30 |
| [[p01_kc_api_rate_limiting_retry_patterns]] | upstream | 0.27 |
| [[p01_kc_bugloop]] | downstream | 0.22 |
| [[bld_output_template_schedule]] | sibling | 0.21 |
| [[runtime-rule-builder]] | downstream | 0.21 |
| [[bld_memory_runtime_rule]] | downstream | 0.21 |
| [[p03_sp_runtime_rule_builder]] | upstream | 0.18 |
| [[p11_qg_bugloop]] | downstream | 0.18 |
| [[p01_kc_runtime_rule]] | downstream | 0.17 |
| [[p01_kc_llm_output_parsing_validation]] | upstream | 0.17 |
