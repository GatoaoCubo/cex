---
kind: output_template
id: bld_output_template_model_provider
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a model_provider
pattern: every field here exists in SCHEMA — template derives, never invents
quality: 9.1
title: "Output Template Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_model_provider
  - bld_examples_model_provider
  - bld_knowledge_card_model_provider
  - model-provider-builder
  - p03_sp_model_provider_builder
  - bld_collaboration_model_provider
  - p11_qg_model_provider
  - p01_kc_model_provider
  - bld_memory_model_provider
  - bld_schema_model_provider
---

# Output Template: model_provider
```yaml
id: p02_mp_{{provider}}
kind: model_provider
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
provider: "{{anthropic|openai|google|ollama|groq|mistral|together|fireworks|deepseek|other}}"
api_key_env: "{{ENV_VAR_NAME_or_null}}"
api_base_url: {{url_or_null}}
auth_method: "{{bearer|api-key|oauth|none}}"
models:
  fast: "{{cheapest_model_id}}"
  balanced: "{{mid_tier_model_id}}"
  quality: "{{most_capable_model_id}}"
rate_limit_rpm: {{integer_or_null}}
rate_limit_tpm: {{integer_or_null}}
max_retries: {{integer}}
timeout_seconds: {{integer}}
fallback: "{{fallback_provider_or_null}}"
health_check_interval: {{integer_or_null}}
cost_aware: {{bool}}
nucleus_assignment: [{{N01_through_N07_or_null}}]
domain: llm_routing
quality: null
tags: [model-provider, {{provider}}, {{key_feature}}, {{tier}}]
tldr: "{{provider}} — {{model_range}} tiers, {{rpm}} RPM ({{tier}}), fallback to {{fallback}}, {{highlight}}"
keywords: [{{provider}}, {{model_ids}}, llm-routing]
linked_artifacts:
  primary: null
  related: [{{other_model_providers_or_null}}]
data_source: "{{provider_docs_url}}"
## Boundary
model_provider IS: connection and routing config for {{provider}} API (models, rate limits, fallback).
model_provider IS NOT: model_card, embedder_provider, agent, boot_config.
## Provider Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Provider | {{provider}} | {{url}} |
| API Base | {{base_url}} | {{url}} |
| Auth Method | {{auth_method}} | {{url}} |
| RPM ({{tier}}) | {{rpm}} | {{url}} |
| TPM ({{tier}}) | {{tpm}} | {{url}} |
| Timeout | {{timeout}}s | {{source}} |
## Model Tiers
| Tier | Model ID | Context | $/1M In | $/1M Out | Use Case |
|------|----------|---------|---------|----------|----------|
| fast | {{fast_model}} | {{ctx}} | ${{in}} | ${{out}} | {{use_case}} |
| balanced | {{balanced_model}} | {{ctx}} | ${{in}} | ${{out}} | {{use_case}} |
| quality | {{quality_model}} | {{ctx}} | ${{in}} | ${{out}} | {{use_case}} |
## Fallback Chain
1. Primary: {{provider}} ({{default_model}})
2. Fallback 1: {{fallback_1}} ({{model}}) — trigger: {{condition}}
3. Fallback 2: {{fallback_2}} ({{model}}) — trigger: {{condition}}
4. Circuit breaker: open after {{N}} consecutive failures, half-open after {{seconds}}s
## Rate Limit Strategy
- Algorithm: {{backoff_algorithm}}
- Retry: max {{max_retries}} attempts, then fallback
- RPM tracking: {{tracking_method}}
- TPM tracking: {{tracking_method}}
- 429 handling: {{429_strategy}}
## Anti-Patterns
1. {{anti_pattern_1}} — {{consequence}}
2. {{anti_pattern_2}} — {{consequence}}
3. {{anti_pattern_3}} — {{consequence}}
4. {{anti_pattern_4}} — {{consequence}}
## References
- api: {{api_docs_url}}
- rate-limits: {{rate_limits_url}}
- models: {{models_url}}
- pricing: {{pricing_url}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_model_provider]] | upstream | 0.60 |
| [[bld_examples_model_provider]] | downstream | 0.57 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.57 |
| [[model-provider-builder]] | upstream | 0.57 |
| [[p03_sp_model_provider_builder]] | upstream | 0.52 |
| [[bld_collaboration_model_provider]] | upstream | 0.51 |
| [[p11_qg_model_provider]] | downstream | 0.48 |
| [[p01_kc_model_provider]] | upstream | 0.47 |
| [[bld_memory_model_provider]] | downstream | 0.46 |
| [[bld_schema_model_provider]] | downstream | 0.46 |
