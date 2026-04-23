---
id: p12_wf_cf_publish_hotmart
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Publish Course to Hotmart"
steps_count: 5
execution: sequential
agent_groups: [n02_marketing, n05_operations, n06_commercial]
timeout: 600
retry_policy: per_step
depends_on: [p03_ap_cf_generate_course]
signals: [complete, error]
spawn_configs: []
domain: "content_factory"
quality: 9.0
tags: [workflow, content_factory, hotmart, course, publish]
tldr: "Upload course modules to Hotmart, configure checkout, create landing page, and go live — 5 sequential steps"
density_score: 0.90
related:
  - p12_wf_builder_8f_pipeline
  - p12_wf_content_factory_v1
  - p12_wf_content_monetization
  - p12_wf_cf_publish_youtube
  - p12_wf_cf_email_launch
  - p12_wf_engineering_pipeline
  - p12_wf_cf_promote
  - bld_architecture_chain
  - p12_wf_orchestration_pipeline
  - p12_wf_commercial
---

## Purpose
Publishes a complete course to Hotmart from the structured output of ap_cf_generate_course.
Handles module upload, lesson sequencing, checkout configuration (pricing from N06), landing
page generation, and final go-live toggle. The workflow bridges content creation (N02) with
commercial strategy (N06) and operational execution (N05).

## Steps

### Step 1: Validate Course Structure [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Verify all modules, lessons, quizzes, and metadata are complete and properly formatted
- **Input**: course structure from ap_cf_generate_course
- **Output**: validation report (pass/fail per module, missing items list)
- **Signal**: validate_course_complete
- **Depends on**: none
- **Timeout**: 30s
- **On failure**: abort (incomplete course cannot be published)

### Step 2: Upload Modules and Lessons [n05_operations]
- **Agent**: n05_operations
- **Action**: Create course product on Hotmart, upload modules in sequence with lesson content
- **Input**: validated course structure from Step 1
- **Output**: Hotmart product ID + module IDs + upload confirmation
- **Signal**: upload_modules_complete
- **Depends on**: Step 1
- **Timeout**: 180s
- **On failure**: retry (max 2, upload timeouts)

### Step 3: Configure Checkout [n06_commercial]
- **Agent**: n06_commercial
- **Action**: Set pricing, payment methods, installment options, and guarantee period via Hotmart API
- **Input**: Hotmart product ID + pricing strategy from decision_manifest or brand_config
- **Output**: checkout configuration confirmation with payment link
- **Signal**: checkout_config_complete
- **Depends on**: Step 2
- **Timeout**: 60s
- **On failure**: retry (max 1, pricing API sensitive)

### Step 4: Generate Landing Page [n02_marketing]
- **Agent**: n02_marketing
- **Action**: Create Hotmart sales page with headline, benefits, testimonials section, and CTA
- **Input**: course metadata + lead_magnet_metadata from ap_cf_generate_course + brand_config
- **Output**: landing page HTML/template ID on Hotmart
- **Signal**: landing_page_complete
- **Depends on**: Step 2
- **Timeout**: 90s
- **On failure**: skip (course can launch with default Hotmart page)

### Step 5: Go Live [n05_operations]
- **Agent**: n05_operations
- **Action**: Toggle course status to active, verify public accessibility, test checkout flow
- **Input**: Hotmart product ID + checkout link + landing page
- **Output**: live course URL + verification status
- **Signal**: wf_cf_publish_hotmart_complete
- **Depends on**: Steps 3, 4
- **Timeout**: 60s
- **On failure**: abort (go-live failure requires manual Hotmart review)

## Dependencies
- Course structure from ap_cf_generate_course must be complete
- Hotmart API credentials in .cex/brand/api_keys
- Pricing strategy defined (decision_manifest or brand_config.pricing)
- Brand assets (logo, colors) for landing page generation

## Signals
- **On step complete**: {step_name}_complete per step
- **On workflow complete**: wf_cf_publish_hotmart_complete with course URL + payment link
- **On error**: wf_cf_publish_hotmart_error with step ID + Hotmart error code

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.38 |
| [[p12_wf_content_factory_v1]] | sibling | 0.38 |
| [[p12_wf_content_monetization]] | sibling | 0.31 |
| [[p12_wf_cf_publish_youtube]] | sibling | 0.31 |
| [[p12_wf_cf_email_launch]] | sibling | 0.31 |
| [[p12_wf_engineering_pipeline]] | sibling | 0.29 |
| [[p12_wf_cf_promote]] | sibling | 0.29 |
| [[bld_architecture_chain]] | upstream | 0.28 |
| [[p12_wf_orchestration_pipeline]] | sibling | 0.27 |
| [[p12_wf_commercial]] | sibling | 0.27 |
