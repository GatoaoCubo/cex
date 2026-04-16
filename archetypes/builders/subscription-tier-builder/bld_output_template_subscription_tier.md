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
