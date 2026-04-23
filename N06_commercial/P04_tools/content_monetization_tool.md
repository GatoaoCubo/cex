---
id: p04_fn_content_monetization
title: "Content Monetization Tool"
kind: function_def
pillar: P04
version: 1.1.0
created: 2026-03-31
updated: 2026-04-07
author: n06_commercial
quality: 9.1
tags: [tool, function, content-monetization, billing, checkout, credits, N06]
tldr: "Full content monetization pipeline: pricing resolution, credit gating, PIX/Stripe/Hotmart checkout, LLM course generation, ad validation, email dispatch."
density_score: 0.93
linked_artifacts:
  primary: p12_wf_content_monetization
  related: [p12_dr_content_monetization, p01_kc_brand_monetization_models, n06_output_pricing_page]
name: monetize_content
description: "Execute the full content monetization pipeline: resolve pricing, configure credits, setup checkout, generate course content, validate ads, and send email sequences."
parameters:
  type: object
  properties:
    product:
      type: object
      description: "Product descriptor with name, category, and audience"
    pricing_tier:
      type: string
      description: "Pricing tier for this operation"
      enum: [free, pro, enterprise]
    payment_provider:
      type: string
      description: "Payment provider to use for checkout"
      enum: [stripe, mercadopago, hotmart, digistore24, mock]
    pipeline_steps:
      type: array
      description: "Explicit pipeline steps to execute; defaults to full pipeline"
      items:
        type: string
        enum: [PARSE, PRICING, CREDITS, CHECKOUT, COURSES, ADS, EMAILS, VALIDATE, DEPLOY]
    currency:
      type: string
      description: "Currency code; BRL uses centavos, EUR/USD use cents integer representation"
      enum: [BRL, USD, EUR]
    dry_run:
      type: boolean
      description: "If true, validates config without charging credits or hitting payment APIs"
  required: [product, pricing_tier, payment_provider]
returns:
  type: object
  description: "Monetization configuration with checkout URL, credit balance, course artifacts, and deployment status"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content-monetization
tags: [function_def, monetization, billing, checkout, courses, credits, N06]
tldr: "LLM-callable tool for the full 9-step content monetization pipeline — from pricing resolution to course generation to deployment."
examples:
  - input:
      product: {name: "SEO Avançado", category: "course", audience: "empreendedores digitais"}
      pricing_tier: "pro"
      payment_provider: "mercadopago"
    output:
      status: success
      checkout_url: "https://mercadopago.com.br/checkout/v1/redirect?pref_id=..."
      credits_consumed: 200
      course_outline_id: "outline_seo_avancado_v1"
      monetization_config_id: "p04_fn_content_monetization_seo"
error_types: [insufficient_credits, payment_provider_unavailable, course_generation_failed, ad_validation_failed]
related:
  - p03_ch_content_pipeline
  - p03_ch_kc_to_notebooklm
  - p04_function_def_NAME
  - n06_schema_brand_config
  - n06_input_schema_content_order
  - bld_output_template_function_def
  - p04_tpl_content_monetization
  - bld_schema_model_registry
  - bld_schema_input_schema
  - bld_schema_validation_schema
---

# Content Monetization Function Definition

## Purpose

`monetize_content` executes the full 9-step content monetization pipeline when called by an LLM agent. It orchestrates billing, credit consumption, checkout session creation, LLM-driven course generation, ad content validation, email sequence dispatch, and deployment of the final monetization config. The function is the single entry point for N06's content monetization domain.

## Schema (OpenAI/Anthropic format)

```json
{
  "name": "monetize_content",
  "description": "Execute the full content monetization pipeline: resolve pricing, configure credits, setup checkout, generate course content, validate ads, and send email sequences.",
  "parameters": {
    "type": "object",
    "properties": {
      "product": {
        "type": "object",
        "description": "Product descriptor: {name: string, category: 'course'|'ebook'|'saas'|'ecommerce', audience: string}",
        "required": ["name", "category", "audience"]
      },
      "pricing_tier": {
        "type": "string",
        "description": "Tier determines credit allowance and checkout flow",
        "enum": ["free", "pro", "enterprise"]
      },
      "payment_provider": {
        "type": "string",
        "description": "Provider for checkout session; use 'mock' for dev/CI",
        "enum": ["stripe", "mercadopago", "hotmart", "digistore24", "mock"]
      },
      "pipeline_steps": {
        "type": "array",
        "description": "Subset of pipeline steps to execute (default: all 9)",
        "items": {
          "type": "string",
          "enum": ["PARSE", "PRICING", "CREDITS", "CHECKOUT", "COURSES", "ADS", "EMAILS", "VALIDATE", "DEPLOY"]
        }
      },
      "currency": {
        "type": "string",
        "description": "BRL = centavos integer; USD/EUR = cents integer",
        "enum": ["BRL", "USD", "EUR"],
        "default": "BRL"
      },
      "dry_run": {
        "type": "boolean",
        "description": "Validate config and estimate costs without side effects",
        "default": false
      }
    },
    "required": ["product", "pricing_tier", "payment_provider"]
  }
}
```

## Parameter Reference

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| product | object | yes | — | `{name, category, audience}` — drives course outline and ad content |
| pricing_tier | string | yes | — | `free` (no checkout), `pro` (standard pack), `enterprise` (custom) |
| payment_provider | string | yes | — | `mercadopago` for BRL/PIX; `hotmart` for BR infoproducts; `digistore24` for EU/DACH; `stripe` for USD/global; `mock` for CI |
| pipeline_steps | array | no | all 9 | Subset execution — useful for partial rerun after step failure |
| currency | string | no | BRL | Determines centavos (BRL) vs cents (USD/EUR) representation |
| dry_run | boolean | no | false | Returns estimated costs and config preview without side effects |

## Return Type

```json
{
  "type": "object",
  "properties": {
    "status": {"type": "string", "enum": ["success", "partial", "error"]},
    "checkout_url": {"type": "string", "description": "Payment URL if CHECKOUT step ran"},
    "credits_consumed": {"type": "integer", "description": "Centavos consumed in this run"},
    "credits_remaining": {"type": "integer", "description": "Wallet balance after run"},
    "course_outline_id": {"type": "string", "description": "ID of generated course outline artifact"},
    "ad_validation_score": {"type": "number", "description": "Confidence score 0.0-1.0 from ad validator"},
    "emails_queued": {"type": "integer", "description": "Count of emails queued for dispatch"},
    "monetization_config_id": {"type": "string", "description": "ID of saved monetization_config artifact"},
    "steps_completed": {"type": "array", "items": {"type": "string"}},
    "steps_failed": {"type": "array", "items": {"type": "string"}},
    "error": {"type": "string", "description": "Error message if status=error"}
  }
}
```

## Pipeline Steps Detail

| Step | Agent | Action | Output |
|------|-------|--------|--------|
| PARSE | N06 | Extract product, audience, monetization goal | parsed_intent |
| PRICING | N06 | Resolve tier, estimate credit cost | pricing_config |
| CREDITS | N06 | check_sufficient → lock credits | credit_lock |
| CHECKOUT | N06 | Create payment session (PIX/Stripe) | checkout_url |
| COURSES | N06 | LLM chain: outline→module→sales_page→emails | course_artifacts |
| ADS | N06 | Validate ad content, confidence_score >= 0.7 | validated_ads |
| EMAILS | N06 | Render templates, queue dispatch | email_queue |
| VALIDATE | N06 | Gates: margin >30%, mock exists, webhook idempotent | validation_report |
| DEPLOY | N06 | Save monetization_config, signal complete | config_id |

## Error Contract

| Error | Condition | Response |
|-------|-----------|----------|
| insufficient_credits | Balance < PIPELINE_COSTS[operation] | `{"status": "error", "error": "insufficient_credits", "checkout_url": "..."}` |
| payment_provider_unavailable | API timeout or 5xx after 3 retries | `{"status": "error", "error": "payment_provider_unavailable"}` |
| course_generation_failed | LLM quota exceeded, no mock fallback | `{"status": "partial", "steps_failed": ["COURSES"]}` |
| ad_validation_failed | confidence_score < 0.7 after 2 retries | `{"status": "partial", "steps_failed": ["ADS"], "ad_validation_score": 0.4}` |

## Usage Examples

```python
# Full pipeline — course monetization with PIX
result = await monetize_content(
    product={"name": "SEO Avançado", "category": "course", "audience": "empreendedores"},
    pricing_tier="pro",
    payment_provider="mercadopago"
)
# Returns: {"status": "success", "checkout_url": "https://...", "credits_consumed": 200, ...}

# Dry run — estimate costs before charging
result = await monetize_content(
    product={"name": "E-book FB Ads", "category": "ebook", "audience": "lojistas"},
    pricing_tier="free",
    payment_provider="mock",
    dry_run=True
)
# Returns: {"status": "success", "credits_consumed": 0, "estimated_cost": 50, ...}

# Partial pipeline — only ads + emails after course already generated
result = await monetize_content(
    product={"name": "Copywriting Pro", "category": "course", "audience": "freelancers"},
    pricing_tier="pro",
    payment_provider="stripe",
    pipeline_steps=["ADS", "EMAILS", "DEPLOY"]
)
```

## Quality Gate

- [x] Description is ≤ 2 sentences (LLM context budget)
- [x] All required parameters listed with types and enums
- [x] Return type documented with all fields
- [x] Error contract covers: insufficient_credits, provider_unavailable, generation_failed, validation_failed
- [x] provider_compat covers openai + anthropic + gemini
- [x] mock mode available for all payment paths

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_content_pipeline]] | upstream | 0.41 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.39 |
| [[p04_function_def_NAME]] | sibling | 0.38 |
| [[n06_schema_brand_config]] | downstream | 0.36 |
| [[n06_input_schema_content_order]] | downstream | 0.35 |
| [[bld_output_template_function_def]] | downstream | 0.32 |
| [[p04_tpl_content_monetization]] | downstream | 0.32 |
| [[bld_schema_model_registry]] | downstream | 0.32 |
| [[bld_schema_input_schema]] | downstream | 0.32 |
| [[bld_schema_validation_schema]] | downstream | 0.31 |
