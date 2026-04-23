---
id: p01_kc_supabase_multi_tenant
kind: knowledge_card
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
tldr: "3 estrategias multi-tenant: shared schema + RLS (simples), schema per tenant (isolamento), project per tenant (maximo). RLS com org_id + JWT claims eh o padrao mais comum."
when_to_use: "Quando projetar isolamento de dados multi-tenant em Supabase"
keywords: [multi-tenant, rls-patterns, org-isolation, tenant-isolation]
long_tails:
  - Como implementar multi-tenancy com RLS no Supabase
  - Shared schema vs schema per tenant no Supabase
  - JWT custom claims para org_id no Supabase multi-tenant
axioms:
  - SEMPRE use RLS — nunca confie em filtro application-level para isolamento
  - NUNCA misture dados de tenants sem coluna org_id indexada
  - SEMPRE indexe a coluna de tenant (org_id) em toda tabela compartilhada
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
padrao_mais_comum: shared schema + RLS por org_id
```

## 3 Estratégias
| Estratégia | Isolamento | Complexidade | Custo | Quando |
|------------|-----------|--------------|-------|--------|
| Shared schema + RLS | Lógico (rows) | Baixa | 1 projeto | <100 tenants, SaaS B2B |
| Schema per tenant | Lógico (schemas) | Média | 1 projeto | 10-1000 tenants, compliance |
| Project per tenant | Físico (DB) | Alta | N projetos | Enterprise, data residency |

## Pattern 1: Shared Schema + RLS (Mais Comum)
```sql
-- Toda tabela tem org_id
CREATE TABLE orders (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  org_id UUID NOT NULL REFERENCES organizations(id),
  total NUMERIC(10,2) NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index OBRIGATÓRIO na coluna de tenant
CREATE INDEX idx_orders_org ON orders(org_id);

-- RLS: user vê só dados da sua org
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

## RLS Patterns (5 Principais)
| Pattern | Policy | Uso |
|---------|--------|-----|
| Owner | `auth.uid() = user_id` | Dados pessoais (perfil, prefs) |
| Org member | `org_id = jwt->org_id` | Dados da empresa (pedidos, prods) |
| Role-based | `jwt->role = 'admin'` | Admin vê tudo na org |
| Public read | `true` FOR SELECT | Catálogo público, landing pages |
| Hierarchical | `org_id IN (SELECT org_id FROM memberships WHERE user_id = auth.uid())` | User em múltiplas orgs |

## Outras Estratégias
| Estratégia | Como | Custo |
|------------|------|-------|
| Schema per tenant | `CREATE SCHEMA tenant_x;` + search_path por JWT | 1 projeto |
| Project per tenant | Management API provisiona projeto por tenant | USD 25/mo × N |

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
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| Filtro só no WHERE app-level | Tenant leak se bug no código | RLS obrigatório |
| Sem index em org_id | Full scan em toda query | CREATE INDEX |
| org_id hardcoded no app | Muda tenant = muda código | JWT claims dinâmicos |
| RLS com subquery lenta | Timeout em tabelas grandes | Materializar membership |
| Sem role hierarchy | Admin não consegue ver tudo | role check no policy |

## Golden Rules
- RLS é a ÚLTIMA linha de defesa — nunca dependa só do app code
- INDEXE org_id + coluna de sort em toda tabela compartilhada
- USE JWT claims (app_metadata) para org_id — não query no DB
- TESTE isolamento: login como user A, tentar acessar dados de org B
- MONITORE: EXPLAIN ANALYZE queries críticas com RLS ativo

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
