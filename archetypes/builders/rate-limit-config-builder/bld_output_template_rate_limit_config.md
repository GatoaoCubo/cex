---
kind: output_template
id: bld_output_template_rate_limit_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a rate_limit_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: rate_limit_config

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
```yaml
id: p09_rl_{{provider_slug}}
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_config_name}}"
provider: "{{provider_name}}"
rpm: {{requests_per_minute_integer}}
tpm: {{tokens_per_minute_integer}}
quality: null
tags: [rate_limit_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_this_config_governs_max_200ch}}"
budget_usd: {{monthly_budget_float}}
tier: "{{free|build|scale|enterprise}}"
rpd: {{requests_per_day_integer}}
concurrent: {{max_concurrent_integer}}
retry_after: {{seconds_after_429_integer}}
alert_threshold: {{fraction_0_to_1}}
model_overrides:
  {{model_name_1}}:
    rpm: {{model_rpm}}
    tpm: {{model_tpm}}
  {{model_name_2}}:
    rpm: {{model_rpm}}
    tpm: {{model_tpm}}
```
## Overview
`{{what_this_rate_limit_config_does_1_to_2_sentences}}`
`{{which_provider_and_tier_and_primary_use_case}}`
## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | `{{rpm}}` | Requests per minute |
| TPM | `{{tpm}}` | Tokens per minute |
| RPD | `{{rpd}}` | Requests per day |
| Concurrent | `{{concurrent}}` | Max parallel in-flight requests |
## Tier
**Tier**: `{{tier_name}}`
`{{tier_description_and_what_is_included}}`
Upgrade path: `{{how_to_upgrade_to_next_tier}}`
## Budget
Monthly cap: $`{{budget_usd}}`
Alert threshold: `{{alert_threshold_percent}}`% of limit
Overage policy: `{{what_happens_when_budget_exceeded}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | rate limit config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
