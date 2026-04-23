---
id: n06_schema_brand_config
kind: constraint_spec
pillar: P06
title: "Brand Config Schema — 7 Sections, 41 Variables"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-config-validation
quality: 9.1
updated: 2026-04-07
tags: [schema, brand, config, validation, n06]
tldr: "Schema documentation for brand_config.yaml. 7 sections (identity, archetype, voice, audience, visual, positioning, monetization), 13 required fields, 28 optional. Validated by brand_validate.py."
density_score: 0.94
axioms:
  - "13 required fields MUST be present — brand_validate.py enforces this."
  - "NEVER add fields without updating this schema — schema IS the contract."
linked_artifacts:
  primary: n06_output_brand_config
  related: [p03_brand_config_extractor, n06_schema_brand_audit, p01_kc_brand_propagation_arch]
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_multimodal_prompt
  - bld_schema_tagline
  - bld_schema_training_method
  - bld_schema_agent_grounding_record
  - bld_schema_customer_segment
  - bld_schema_sandbox_config
  - bld_schema_model_architecture
  - bld_schema_research_pipeline
---

# Brand Config Schema

## Overview
`.cex/brand/brand_config.yaml` is the Single Source of Truth for brand identity.
N06 generates it. All nuclei read it. No hardcoded brand anywhere.

## Sections

### 1. identity (4 required, 3 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_NAME | string | ✅ | 1-100 chars |
| BRAND_TAGLINE | string | ✅ | 10-100 chars |
| BRAND_MISSION | string | ✅ | 20-500 chars |
| BRAND_VALUES | array[string] | ✅ | 3-7 items |
| BRAND_SLOGAN | string | ❌ | campaign-specific |
| BRAND_VISION | string | ❌ | future-tense aspirational |
| BRAND_STORY | string | ❌ | 200-2000 chars |

### 2. archetype (1 required, 2 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_ARCHETYPE | enum | ✅ | creator\|hero\|sage\|explorer\|rebel\|magician\|lover\|caregiver\|jester\|ruler\|innocent\|everyman |
| BRAND_ARCHETYPE_SHADOW | string | ❌ | counter-archetype to avoid |
| BRAND_PERSONALITY | array[string] | ❌ | 3-7 traits |

### 3. voice (2 required, 7 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_VOICE_TONE | string | ✅ | descriptive tone |
| BRAND_VOICE_FORMALITY | int | ✅ | 1-5 |
| BRAND_VOICE_ENTHUSIASM | int | ❌ | 1-5 |
| BRAND_VOICE_HUMOR | int | ❌ | 1-5 |
| BRAND_VOICE_WARMTH | int | ❌ | 1-5 |
| BRAND_VOICE_AUTHORITY | int | ❌ | 1-5 |
| BRAND_VOICE_DO | array[string] | ❌ | 3+ items |
| BRAND_VOICE_DONT | array[string] | ❌ | 3+ items |
| BRAND_LANGUAGE | string | ❌ | pattern: xx-XX |

### 4. audience (2 required, 6 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_ICP | string | ✅ | 20+ chars |
| BRAND_TRANSFORMATION | string | ✅ | pattern: From X to Y through Z |
| BRAND_ICP_AGE | string | ❌ | age range |
| BRAND_ICP_LOCATION | string | ❌ | geographic |
| BRAND_ICP_INCOME | string | ❌ | income class |
| BRAND_ICP_VALUES | array[string] | ❌ | |
| BRAND_ICP_FEARS | array[string] | ❌ | |
| BRAND_ICP_ASPIRATIONS | array[string] | ❌ | |

### 5. visual (1 required, 4 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_COLORS | object | ✅ | requires primary, secondary, accent (HEX #RRGGBB) |
| BRAND_FONTS | object | ❌ | heading, body, mono |
| BRAND_LOGO_URL | string | ❌ | URI |
| BRAND_FAVICON_URL | string | ❌ | URI |
| BRAND_STYLE | string | ❌ | e.g. "minimal-dark" |

### 6. positioning (2 required, 3 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_CATEGORY | string | ✅ | market category |
| BRAND_UVP | string | ✅ | 20+ chars |
| BRAND_DIFFERENTIATOR | string | ❌ | |
| BRAND_COMPETITORS | array[string] | ❌ | |
| BRAND_CONTENT_PILLARS | array[string] | ❌ | 3-7 items |

### 7. monetization (2 required, 3 optional)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| BRAND_PRICING_MODEL | enum | ✅ | subscription\|one-time\|credits\|freemium\|marketplace\|hybrid |
| BRAND_CURRENCY | string | ✅ | 3-letter ISO (BRL, USD, EUR) |
| BRAND_PRICE_ANCHOR | string | ❌ | highest tier price |
| BRAND_TIERS | array[string] | ❌ | tier names |
| BRAND_PAYMENT_PROVIDERS | array[string] | ❌ | stripe, mercadopago, hotmart |

## Validation

```bash
python _tools/brand_validate.py           # full validation
python _tools/brand_validate.py --strict  # warnings = errors
python _tools/brand_validate.py --json    # machine-readable
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | related | 0.56 |
| [[bld_schema_experiment_tracker]] | related | 0.48 |
| [[bld_schema_multimodal_prompt]] | related | 0.46 |
| [[bld_schema_tagline]] | related | 0.44 |
| [[bld_schema_training_method]] | related | 0.43 |
| [[bld_schema_agent_grounding_record]] | related | 0.40 |
| [[bld_schema_customer_segment]] | related | 0.39 |
| [[bld_schema_sandbox_config]] | related | 0.39 |
| [[bld_schema_model_architecture]] | related | 0.39 |
| [[bld_schema_research_pipeline]] | related | 0.38 |
