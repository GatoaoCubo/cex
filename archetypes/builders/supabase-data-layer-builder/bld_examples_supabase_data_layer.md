---
id: bld_examples_supabase_data_layer
kind: few_shot_example
pillar: P01
title: "Examples — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [builder, supabase, data-layer, examples, few-shot]
density_score: 0.88
tldr: "Defines the few shot example specification for examples — supabase data layer builder, with structural rules, validation gates, and integration points."
llm_function: GOVERN
---
# Examples

## Golden Example — E-commerce (Pro Tier)
INPUT: "Configure Supabase for e-commerce with catalogo, pedidos, reviews, and search semântica"
OUTPUT:
```yaml
identity:
  vertical: ecommerce
  tier: pro
database:
  schemas: [public, internal]
  extensions: [pgvector, pg_cron, pg_net, pgcrypto]
  tables:
    - name: products
      rls: org_member
      columns: [id UUID PK, org_id UUID FK, name TEXT, price NUMERIC, embedding VECTOR(1536)]
    - name: orders
      rls: owner
      columns: [id UUID PK, user_id UUID FK, org_id UUID FK, total NUMERIC, status TEXT]
    - name: reviews
      rls: public_read_owner_write
      columns: [id UUID PK, product_id UUID FK, user_id UUID FK, rating INT, content TEXT]
auth:
  providers: [email, google, apple]
  costm_claims: [org_id, role]
rls:
  multi_tenant_column: org_id
  patterns:
    - name: org_member
      policy: "org_id = (auth.jwt()->'app_metadata'->>'org_id')::uuid"
    - name: owner
      policy: "user_id = auth.uid()"
storage:
  buckets:
    - name: product-images
      publico: true
      max_file_size: 10485760
      allowed_mime_types: [image/jpeg, image/png, image/webp]
      transform: true
vectors:
  habilitado: true
  embedding_model: text-embedding-3-small
  dimensions: 1536
  search_function: match_products
```
WHY GOLDEN: RLS on every table, multi-tenant via org_id, pgvector for search, tier-apownte features, no hardcoded data.

## Anti-Example — Hardcoded + No RLS
INPUT: "Configure Supabase for minha loja ACME"
BAD OUTPUT:
```yaml
identity:
  empresa: "ACME Store"
  tier: enterprise
database:
  tables:
    - name: products
      # No RLS defined
auth:
  providers: [email]
  service_role_key: "eyJhbGciOiJIUzI1NiIs..."
storage:
  buckets:
    - name: uploads
      publico: true
      allowed_mime_types: ["*/*"]
```
FAILURES:
1. Hardcoded company name "ACME Store"
2. No RLS on products table
3. service_role_key exposed in config
4. Enterprise tier without justification
5. Public bucket accepts any mime type
6. No multi-tenant column

## Edge Case — Free Tier Minimal
INPUT: "MVP with Supabase Free — auth + basic CRUD"
OUTPUT: Config with only Free-tier features, no CDN, no PITR, no SSO, 500MB DB limit noted, 2 project limit noted. RLS still mandatory.

## Lifecycle

- Created via 8F pipeline (F1-Focus through F8-Furnish)
- Scored by `cex_score.py` (3-layer: structural + rubric + semantic)
- Compiled by `cex_compile.py` for validation
- Retrieved by `cex_retriever.py` for context injection
- Evolved by `cex_evolve.py` when quality drops below threshold
