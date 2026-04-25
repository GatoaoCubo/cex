---
id: p01_kc_supabase_multi_tenant
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Multi-Tenant — RLS Patterns, Org Isolation, Schema Strategies"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, multi-tenant, rls, org-isolation, schema, platform]
tldr: "3 multi-tenant strategies: shared schema + RLS (simple), schema per tenant (isolation), project per tenant (maximum). RLS with org_id + JWT claims is the most common pattern."
when_to_use: "When designing multi-tenant data isolation in Supabase"
keywords: [multi-tenant, rls-patterns, org-isolation, tenant-isolation]
long_tails:
  - How to implement multi-tenancy with RLS in Supabase
  - Shared schema vs schema per tenant in Supabase
  - JWT custom claims for org_id in Supabase multi-tenant
axioms:
  - ALWAYS use RLS — never trust application-level filtering for isolation
  - NEVER mix tenant data without an indexed org_id column
  - ALWAYS index the tenant column (org_id) in every shared table
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_auth, p01_kc_supabase_database]
density_score: 0.91
data_source: "https://supabase.com/docs/guides/database/postgres/row-level-security"
related:
  - bld_output_template_supabase_data_layer
  - p04_ex_supabase_data_layer_saas
  - bld_examples_supabase_data_layer
  - bld_memory_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - p04_ex_supabase_data_layer_ecommerce
  - p01_kc_supabase_auth
  - p12_wf_supabase_setup
  - bld_knowledge_card_supabase_data_layer
  - p01_rag_source_supabase
---

# Supabase Multi-Tenant

## Quick Reference
```yaml
topic: supabase_multi_tenant
scope: RLS patterns, org isolation, shared/separate schema, JWT claims
owner: n04_knowledge
criticality: high
most_common_pattern: shared schema + RLS by org_id
```

## 3 Strategies
| Strategy | Isolation | Complexity | Cost | When |
|----------|-----------|------------|------|------|
| Shared schema + RLS | Logical (rows) | Low | 1 project | <100 tenants, SaaS B2B |
| Schema per tenant | Logical (schemas) | Medium | 1 project | 10-1000 tenants, compliance |
| Project per tenant | Physical (DB) | High | N projects | Enterprise, data residency |

## Pattern 1: Shared Schema + RLS (Most Common)
```sql
-- Every table has org_id
CREATE TABLE orders (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  org_id UUID NOT NULL REFERENCES organizations(id),
  total NUMERIC(10,2) NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- MANDATORY index on tenant column
CREATE INDEX idx_orders_org ON orders(org_id);

-- RLS: user sees only their org's data
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY "tenant_isolation" ON orders
  FOR ALL USING (
    org_id = (auth.jwt()->'app_metadata'->>'org_id')::uuid
  );
```

## JWT Custom Claims
```sql
-- JWT: {"app_metadata": {"org_id": "uuid-da-org"}}
-- Auto-assign via trigger on auth.users INSERT
-- Setar via Admin API: supabase.auth.admin.updateUserById(uid, {app_metadata:{org_id}})
```

## RLS Patterns (Top 5)
| Pattern | Policy | Use |
|---------|--------|-----|
| Owner | `auth.uid() = user_id` | Personal data (profile, prefs) |
| Org member | `org_id = jwt->org_id` | Company data (orders, products) |
| Role-based | `jwt->role = 'admin'` | Admin sees everything in org |
| Public read | `true` FOR SELECT | Public catalog, landing pages |
| Hierarchical | `org_id IN (SELECT org_id FROM memberships WHERE user_id = auth.uid())` | User in multiple orgs |

## Other Strategies
| Strategy | How | Cost |
|----------|-----|------|
| Schema per tenant | `CREATE SCHEMA tenant_x;` + search_path per JWT | 1 project |
| Project per tenant | Management API provisions project per tenant | USD 25/mo x N |

## Membership Model
```sql
CREATE TABLE organizations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL, plan TEXT DEFAULT 'free'
);
CREATE TABLE memberships (
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  org_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  role TEXT CHECK (role IN ('owner','admin','member','viewer')),
  UNIQUE(user_id, org_id)
);
CREATE INDEX idx_memberships_user ON memberships(user_id);
CREATE INDEX idx_memberships_org ON memberships(org_id);
```

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Filter only in app-level WHERE | Tenant leak if code bug | RLS mandatory |
| No index on org_id | Full scan on every query | CREATE INDEX |
| org_id hardcoded in app | Change tenant = change code | Dynamic JWT claims |
| RLS with slow subquery | Timeout on large tables | Materialize membership |
| No role hierarchy | Admin cannot see everything | role check in policy |

## Golden Rules
- RLS is the LAST line of defense — never rely only on app code
- INDEX org_id + sort column in every shared table
- USE JWT claims (app_metadata) for org_id — do not query the DB
- TEST isolation: login as user A, try to access org B data
- MONITOR: EXPLAIN ANALYZE critical queries with RLS active

## References
- RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Multi-tenant: https://supabase.com/docs/guides/auth/row-level-security
- Management API: https://supabase.com/docs/reference/api

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_supabase_data_layer]] | downstream | 0.53 |
| [[p04_ex_supabase_data_layer_saas]] | downstream | 0.50 |
| [[bld_examples_supabase_data_layer]] | related | 0.50 |
| [[bld_memory_supabase_data_layer]] | related | 0.47 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.46 |
| [[p04_ex_supabase_data_layer_ecommerce]] | downstream | 0.42 |
| [[p01_kc_supabase_auth]] | sibling | 0.42 |
| [[p12_wf_supabase_setup]] | downstream | 0.37 |
| [[bld_knowledge_card_supabase_data_layer]] | sibling | 0.36 |
| [[p01_rag_source_supabase]] | related | 0.34 |
