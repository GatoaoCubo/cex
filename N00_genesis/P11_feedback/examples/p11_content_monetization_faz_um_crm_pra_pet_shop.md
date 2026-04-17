---
id: petshop-crm
kind: content_monetization
pillar: P11
title: PetShop CRM
version: "1.0.0"
created: "2023-10-15"
author: "content-monetization-builder"
domain: petshop
quality: 8.7
tags: [content-monetization, crm, petshop]
density_score: 0.98
---
# PetShop CRM
## Pipeline (9 stages)
## Pricing Strategy
pricing:
  strategy: freemium
  floor_margin_pct: 0.33
  trial_days: 7
  tiers:
    - name: "Free"
      price_monthly: 0
      credits_monthly: 50
      features: [customer_profile, appointment_scheduling]
    - name: "Pro"
      price_monthly: 990
      price_yearly: 11880
      credits_monthly: 500
      features: [advanced_reporting, team_collaboration, pet_health_traking]

credits:
  unit_name: "PetCredit"
  pipeline_costs:
    customer_profile: 1
    appointment_scheduling: 2
    pet_health_traking: 3
  packs:
    - name: "Monthly Pro"
      credits: 500
      price: 990
    - name: "Yearly Pro"
      credits: 2000
      price: 11880
  overdraft_policy: notify_then_block
  rollover: false

checkout:
  provider: stripe
  webhook_url: https://api.petshop.com/webhooks
  webhook_secret_env: STRIPE_WEBHOOK_SECRET
  idempotency: true
  success_redirect: https://petshop.com/success
  cancel_redirect: https://petshop.com/cancel
  mock_mode: true

courses:
  enabled: false

ads:
  enabled: true
  platforms: [meta, google]
  monthly_budget: 5000
  target_cpa: 150
  pixel_env: PETSHOP_PIXEL

emails:
  provider: resend
  api_key_env: RESEND_API_KEY
  sequences:
    - name: "Onboarding"
      trigger: "signup"
      emails:
        - { delay_hours: 1, template: "welcome" }
        - { delay_hours: 24, template: "setup_guide" }
    - name: "Churn Prevention"
      trigger: "credits_low"
      emails:
        - { delay_hours: 24, template: "upgrade_prompt" }

validation:
  margin_check: true
  webhook_test: true
  mock_before_live: true
````