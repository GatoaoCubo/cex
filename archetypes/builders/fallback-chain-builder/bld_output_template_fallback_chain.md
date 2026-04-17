---
kind: output_template
id: bld_output_template_fallback_chain
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a fallback_chain artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Fallback Chain"
version: "1.0.0"
author: n03_builder
tags: [fallback_chain, builder, examples]
tldr: "Golden and anti-examples for fallback chain construction, demonstrating ideal structure and common pitfalls."
domain: "fallback chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: fallback_chain
```yaml
id: p02_fc_{{fc_slug}}
kind: fallback_chain
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
steps_count: {{integer_matching_table}}
timeout_per_step_ms: {{integer_ms}}
quality_threshold: {{0.0_to_10.0}}
domain: "{{chain_domain}}"
quality: null
tags: [fallback_chain, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
retry_count: {{integer}}
circuit_breaker_threshold: {{integer}}
cost_ceiling_usd: {{float_usd}}
logging_level: "{{none|errors|all}}"
alert_on_final_fallback: {{true|false}}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
```
## Chain
| Position | Model | Provider | Timeout (ms) | Quality Min | Cost/1M tokens (USD) | Retry |
|----------|-------|----------|-------------|-------------|---------------------|-------|
| 1 | `{{primary_model}}` | {{provider_1}} | {{timeout_1}} | {{quality_1}} | {{cost_1}} | `{{retry_1}}` |
| 2 | `{{fallback_model}}` | {{provider_2}} | {{timeout_2}} | {{quality_2}} | {{cost_2}} | `{{retry_2}}` |
| 3 | `{{minimum_model}}` | {{provider_3}} | {{timeout_3}} | {{quality_3}} | {{cost_3}} | `{{retry_3}}` |
## Degradation Logic
Step transition trigger: {{timeout_exceeded|quality_below_threshold|error_response|rate_limited}}
Quality evaluation: {{automatic_score|human_review|rubric_check}}
Transition behavior: {{immediate|wait_retry_then_transition}}
## Circuit Breaker
Threshold: `{{circuit_breaker_threshold}}` consecutive failures across all steps.
State when tripped: {{open_reject_all|half_open_test_primary|closed_retry_from_step_1}}
Recovery: {{automatic_after_cooldown|manual_reset|time_based}}
Cooldown: `{{cooldown_seconds}}` seconds.
## Cost Analysis
| Step | Cost/1M tokens | Expected usage | Projected cost |
|------|---------------|----------------|----------------|
| `{{step_1}}` | {{cost_1}} | {{usage_1}} | `{{projected_1}}` |
| `{{step_2}}` | {{cost_2}} | {{usage_2}} | `{{projected_2}}` |
| Total | - | - | `{{total_projected}}` |
Ceiling: `{{cost_ceiling_usd}}` USD.
## Integration
- Activated by: {{router_failure|agent_request|quality_gate_fail}}
- Provides to: `{{agent_or_service}}`
- Signals: {{degradation_event|circuit_breaker_tripped|chain_exhausted}}
## References
- `{{reference_1}}`
- `{{reference_2}}`
