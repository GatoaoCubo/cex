---
id: bld_config_supabase_data_layer
kind: config
pillar: P02
title: "Config — Supabase Data Layer Builder Defaults"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, config, defaults]
density_score: 0.89
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
llm_function: CONSTRAIN
related:
  - instance_supabase_config_template
  - p04_tpl_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - p01_kc_supabase_database
  - bld_schema_supabase_data_layer
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_pricing
---
# Builder Config

## Default Values
```yaml
defaults:
  tier: pro
  region: sa-east-1
  extensions:
    always: [pgcrypto, pg_graphql]
    if_vectors: [pgvector]
    if_cron: [pg_cron, pg_net]
  auth:
    jwt_expiry: 3600
    mfa: false
    sso: false
  rls:
    enabled: true
    multi_tenant_column: org_id
    admin_bypass: true
  storage:
    default_max_file_size: 52428800  # 50MB
    default_transform: true
  realtime:
    habilitado: false
  vectors:
    habilitado: false
    distance_function: cosine
    default_dimensions: 1536
  edge_functions:
    deploy_method: cli
```

## Tier Limits Reference
| Resource | Free | Pro | Team | Enterprise |
|----------|------|-----|------|------------|
| DB storage | 500 MB | 8 GB | 8 GB+ | Custom |
| File storage | 1 GB | 100 GB | 100 GB+ | Custom |
| Bandwidth | 5 GB | 250 GB | 250 GB+ | Custom |
| Edge invocations | 500K | 2M | 2M+ | Custom |
| Edge CPU | 2s | 10s | 150s | Custom |
| Auth MAU | 50K | 100K | 100K+ | Custom |
| Realtime msgs | 2M | 5M | Unlimited | Custom |
| Connections | 60 | 200 | 200+ | Custom |
| Pooler | 200 | 1500 | 3000 | Custom |
| Projects | 2 | Unlimited | Unlimited | Unlimited |

## Vertical Presets
| Vertical | Extensions | Key Tables | Storage | Realtime |
|----------|-----------|------------|---------|----------|
| ecommerce | pgvector, pg_cron | products, orders, reviews, carts | product-images | order status |
| saas | pg_cron | users, orgs, subscriptions, features | documents | feature flags |
| marketplace | pgvector, pg_cron, pg_net | sellers, listings, transactions | listing-images | bid updates |
| content | pgvector | posts, comments, media, feeds | content-media | live comments |
| costm | (per config) | (per config) | (per config) | (per config) |

## Environment Config
```yaml
environments:
  local:
    url: "http://localhost:54321"
    anon_key: "eyJ..."  # local dev key from supabase start
    db: "postgresql://postgres:postgres@localhost:54322/postgres"
  staging:
    url: "https://[staging-ref].supabase.co"
    # Keys from Supabase Dashboard > Settings > API
  production:
    url: "https://[prod-ref].supabase.co"
    # service_role_key ONLY in server .env, NEVER in client
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[instance_supabase_config_template]] | sibling | 0.38 |
| [[p04_tpl_supabase_data_layer]] | downstream | 0.36 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.34 |
| [[bld_output_template_supabase_data_layer]] | downstream | 0.31 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.31 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.27 |
| [[p01_kc_supabase_database]] | upstream | 0.26 |
| [[bld_schema_supabase_data_layer]] | related | 0.26 |
| [[bld_tools_supabase_data_layer]] | downstream | 0.25 |
| [[p01_kc_supabase_pricing]] | upstream | 0.25 |
