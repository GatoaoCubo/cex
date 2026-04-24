---
id: p06_schema_env_contract
kind: input_schema
8f: F1_constrain
pillar: P06
title: Environment Variable Contract Schema
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.0
tags: [schema, environment, variables, contract, railway]
tldr: Schema for 63 environment variables contract validation covering DATABASE_URL, API keys, pool settings, and Railway service configuration.
schema_type: env_contract
validation_level: strict
related:
  - bld_schema_validation_schema
  - bld_output_template_input_schema
  - examples_prompt_template_builder
  - p10_lr_input_schema_builder
  - n06_input_schema_content_order
  - brand_override_config
  - p06_schema_health_response
  - bld_examples_workflow_primitive
  - bld_schema_content_monetization
  - bld_schema_workflow_primitive
---

# Environment Variable Contract Schema

## Purpose

Validates the complete 63-variable environment contract for Railway FastAPI
backend deployments including database, API keys, pool settings, and service configuration.

## Required Variables (63 total)

### Database & Infrastructure (8 vars)
```yaml
DATABASE_URL:
  required: true
  pattern: "^postgresql://.*"
  description: PostgreSQL connection string with SSL

DB_POOL_MIN:
  type: integer
  required: true
  minimum: 3
  default: 3

DB_POOL_MAX:
  type: integer
  required: true
  maximum: 20
  default: 20

DB_COMMAND_TIMEOUT:
  type: integer
  required: true
  default: 60

REDIS_URL:
  required: false
  pattern: "^redis://.*"

PORT:
  type: integer
  required: true
  default: 8000

ENV:
  type: string
  required: true
  enum: ["development", "staging", "production"]

RAILWAY_ENVIRONMENT_NAME:
  type: string
  required: true
```

### API Keys & Authentication (15 vars)
```yaml
ANTHROPIC_API_KEY:
  required: true
  pattern: "^sk-.*"

OPENAI_API_KEY:
  required: true
  pattern: "^sk-.*"

GROQ_API_KEY:
  required: false
  pattern: "^gsk_.*"

CEREBRAS_API_KEY:
  required: false

GEMINI_API_KEY:
  required: false

JWT_SECRET_KEY:
  required: true
  min_length: 32

BCRYPT_ROUNDS:
  type: integer
  default: 12
```

### Payment & Integration (20 vars)
```yaml
STRIPE_SECRET_KEY:
  required: false
  pattern: "^sk_(test_|live_).*"

MERCADOPAGO_ACCESS_TOKEN:
  required: false

BLING_CLIENT_ID:
  required: false

BLING_CLIENT_SECRET:
  required: false

E2B_API_KEY:
  required: false
```

### Rate Limiting & Credits (10 vars)
```yaml
RATE_LIMIT_FREE:
  type: integer
  default: 60

RATE_LIMIT_PRO:
  type: integer
  default: 120

RATE_LIMIT_BUSINESS:
  type: integer
  default: 300

CREDIT_PESQUISA_CENTAVOS:
  type: integer
  default: 75

CREDIT_ANUNCIO_CENTAVOS:
  type: integer
  default: 50

CREDIT_FOTO_CENTAVOS:
  type: integer
  default: 100

CREDIT_FULL_CENTAVOS:
  type: integer
  default: 200
```

### Communication & Notifications (10 vars)
```yaml
RESEND_API_KEY:
  required: false

WHATSAPP_TOKEN:
  required: false

SMTP_HOST:
  required: false

SMTP_PORT:
  type: integer
  default: 587
```

## Validation Rules

- DATABASE_URL must be PostgreSQL format with SSL support
- API keys must match provider-specific patterns
- Pool settings within Railway platform limits (3-20 connections)
- Rate limits configured per tier (free/pro/business)
- Credit values in BRL centavos for cost tracking

## Mock Mode Variables

For testing environments, these can be mock values:
- STRIPE_SECRET_KEY (test mode)
- MERCADOPAGO_ACCESS_TOKEN (sandbox)
- E2B_API_KEY (local execution fallback)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_validation_schema]] | related | 0.29 |
| [[bld_output_template_input_schema]] | upstream | 0.29 |
| [[examples_prompt_template_builder]] | downstream | 0.27 |
| [[p10_lr_input_schema_builder]] | downstream | 0.26 |
| [[n06_input_schema_content_order]] | sibling | 0.26 |
| [[brand_override_config]] | downstream | 0.26 |
| [[p06_schema_health_response]] | sibling | 0.25 |
| [[bld_examples_workflow_primitive]] | downstream | 0.24 |
| [[bld_schema_content_monetization]] | related | 0.24 |
| [[bld_schema_workflow_primitive]] | related | 0.22 |
