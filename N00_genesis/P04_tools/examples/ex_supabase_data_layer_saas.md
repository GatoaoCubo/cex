---
id: p04_ex_supabase_data_layer_saas
kind: example
8f: F3_inject
pillar: P04
title: "Example — Supabase Data Layer for SaaS B2B"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [example, supabase, data-layer, saas, multi-tenant, config]
tldr: "SaaS B2B config: users, orgs, subscriptions, feature flags, multi-tenant isolamento por org_id, SSO/MFA para enterprise"
density_score: 0.90
related:
  - p04_ex_supabase_data_layer_ecommerce
  - p04_ex_supabase_data_layer_marketplace
  - p04_ex_supabase_data_layer_content
  - bld_examples_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - p04_tpl_supabase_data_layer
  - p01_kc_supabase_multi_tenant
  - bld_instruction_supabase_data_layer
  - instance_supabase_config_template
  - bld_knowledge_card_supabase_data_layer
---

# SaaS B2B — Supabase Data Layer

## Vertical Profile
| Aspect | Value |
|--------|-------|
| Vertical | saas |
| Tier | team |
| Key tables | organizations, memberships, subscriptions, feature_flags, audit_log |
| Extensions | pg_cron (billing sync), pg_net (webhooks), pgjwt |
| Storage | documents (private per org) |
| Realtime | feature flag updates, audit events |
| Vectors | Not needed (no semantic search) |

## Config
```yaml
identidade:
  vertical: saas
  regiao: us-east-1
  tier: team

database:
  schemas: [public, billing, audit]
  extensions:
    obrigatorias: [pgcrypto, pg_graphql, pgjwt]
    opcionais: [pg_cron, pg_net, wrappers]
  tables:
    - name: organizations
      columns: [id UUID PK, name TEXT, slug TEXT UNIQUE, plan TEXT DEFAULT 'free', stripe_customer_id TEXT]
      rls: org_admin
      indexes: [slug, stripe_customer_id]
    - name: memberships
      columns: [user_id UUID FK auth.users, org_id UUID FK organizations, role TEXT CHECK owner/admin/member/viewer]
      rls: org_member
      indexes: [user_id, org_id]
    - name: subscriptions
      schema: billing
      columns: [id UUID PK, org_id UUID FK, plan TEXT, status TEXT, current_period_end TIMESTAMPTZ, stripe_subscription_id TEXT]
      rls: org_admin
    - name: feature_flags
      columns: [id UUID PK, org_id UUID FK, flag_name TEXT, enabled BOOLEAN, config JSONB]
      rls: org_member_read_admin_write
    - name: audit_log
      schema: audit
      columns: [id UUID PK, org_id UUID FK, user_id UUID, action TEXT, resource TEXT, metadata JSONB, created_at TIMESTAMPTZ]
      rls: org_admin

auth:
  providers: [email, google, microsoft]
  mfa: true
  sso: true
  custom_claims: [org_id, role, plan]
  jwt_expiry: 1800

rls:
  multi_tenant_column: org_id
  patterns:
    - nome: org_member
      policy: "org_id IN (SELECT org_id FROM memberships WHERE user_id = auth.uid())"
      tabelas: [memberships, feature_flags]
    - nome: org_admin
      policy: "org_id IN (SELECT org_id FROM memberships WHERE user_id = auth.uid() AND role IN ('owner','admin'))"
      tabelas: [organizations, subscriptions, audit_log]

storage:
  buckets:
    - nome: org-documents
      publico: false
      max_file_size: 52428800
      allowed_mime_types: [application/pdf, image/png, image/jpeg, text/csv]

realtime:
  habilitado: true
  postgres_changes:
    - tabela: feature_flags
      eventos: [UPDATE]
    - tabela: audit_log
      eventos: [INSERT]

vectors:
  habilitado: false

edge_functions:
  functions:
    - nome: stripe-webhook
      trigger: http
      secrets: [STRIPE_KEY, STRIPE_WEBHOOK_SECRET]
    - nome: sync-subscriptions
      trigger: cron
      schedule: "0 */6 * * *"
    - nome: onboard-org
      trigger: http
      secrets: [SENDGRID_KEY]
  deploy_method: github_actions

budget:
  alertas:
    - metrica: db_size
      threshold: 75
      acao: slack
    - metrica: auth_mau
      threshold: 90
      acao: email
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ex_supabase_data_layer_ecommerce]] | sibling | 0.69 |
| [[p04_ex_supabase_data_layer_marketplace]] | sibling | 0.63 |
| [[p04_ex_supabase_data_layer_content]] | sibling | 0.62 |
| [[bld_examples_supabase_data_layer]] | upstream | 0.57 |
| [[bld_output_template_supabase_data_layer]] | upstream | 0.54 |
| [[p04_tpl_supabase_data_layer]] | related | 0.49 |
| [[p01_kc_supabase_multi_tenant]] | upstream | 0.47 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.38 |
| [[instance_supabase_config_template]] | upstream | 0.37 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.34 |
