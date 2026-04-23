---
kind: output_template
id: bld_output_template_subscription_tier
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for subscription_tier production
quality: 8.7
title: "Output Template Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, output_template]
tldr: "Template with vars for subscription_tier production"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_subscription_tier
  - kc_subscription_tier
  - bld_instruction_pricing_page
  - pricing_optimization_memory
  - bld_config_subscription_tier
  - p08_pat_pricing_framework
  - bld_examples_subscription_tier
  - bld_tools_subscription_tier
  - bld_collaboration_subscription_tier
  - n06_api_access_pricing
---

```yaml
---
id: p11_st_{{name}}.yaml
name: {{subscription_tier_name}}
description: {{tier_description}}
features:
  - {{feature_1}}
  - {{feature_2}}
pricing: {{price}}
tier_level: {{level}}
quality: null
---
```

<!-- id: Generated filename following p11_st_[a-z][a-z0-9_]+.yaml pattern -->
<!-- name: Human-readable tier name (e.g., "Premium") -->
<!-- description: Brief explanation of tier benefits -->
<!-- features: Array of 2-5 bullet points describing included features -->
<!-- pricing: Numerical value or "Free" -->
<!-- tier_level: Numerical value (1=lowest, 5=highest) -->
<!-- quality: Always null -->

| Tier Name   | Features                  | Pricing  | Tier Level |
|-------------|---------------------------|----------|------------|
| Basic       | 10 API calls/day          | $9.99    | 1          |
| Pro         | 100 API calls/day, support | $49.99   | 3          |
| Enterprise  | Unlimited, dedicated team | Custom   | 5          |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_subscription_tier]] | upstream | 0.35 |
| [[kc_subscription_tier]] | upstream | 0.30 |
| [[bld_instruction_pricing_page]] | upstream | 0.26 |
| [[pricing_optimization_memory]] | downstream | 0.25 |
| [[bld_config_subscription_tier]] | downstream | 0.25 |
| [[p08_pat_pricing_framework]] | downstream | 0.25 |
| [[bld_examples_subscription_tier]] | downstream | 0.23 |
| [[bld_tools_subscription_tier]] | upstream | 0.22 |
| [[bld_collaboration_subscription_tier]] | downstream | 0.22 |
| [[n06_api_access_pricing]] | downstream | 0.21 |
