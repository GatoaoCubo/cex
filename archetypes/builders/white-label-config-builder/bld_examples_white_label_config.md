---
kind: examples
id: bld_examples_white_label_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of white_label_config artifacts
quality: 8.8
title: "Examples White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, examples]
tldr: "Golden and anti-examples of white_label_config artifacts"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
name: white_label_config
kind: white_label_config
description: Configuration for Acme Corp's white-label deployment on Stripe and AWS
tags:
  - reseller
  - branding
branding:
  reseller_name: "Acme Corp"
  reseller_logo_url: "https://acme.com/logo.png"
  custom_domain: "acme.stripe.com"
api_keys:
  stripe_publishable_key: "pk_live_1234567890"
  stripe_secret_key: "sk_live_0987654321"
  aws_access_key_id: "AKIAXXXXXXXXXXXXXXXX"
  aws_secret_access_key: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
reseller_settings:
  allowed_brands: ["Acme Corp", "Beta Inc"]
  support_email: "support@acme.com"
```

## Anti-Example 1: Brand identity confusion
```yaml
name: white_label_config
kind: white_label_config
branding:
  company_logo: "logo.svg"
  primary_color: "#007BFF"
  secondary_color: "#6C757D"
```
## Why it fails
Mixes brand identity configuration (colors, logos) with white-label reseller settings. White-label config should focus on reseller-specific deployment parameters, not core brand identity elements which belong in brand_config.

## Anti-Example 2: Runtime environment mixing
```yaml
name: white_label_config
kind: white_label_config
env_vars:
  DATABASE_URL: "postgres://user:pass@localhost:5432/dbname"
  API_ENDPOINT: "https://api.prod.example.com"
```
## Why it fails
Includes runtime environment variables that belong in env_config, not white-label configuration. White-label config should handle reseller branding and deployment parameters, not runtime infrastructure settings.
