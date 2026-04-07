---
id: p04_ex_supabase_data_layer_ecommerce
kind: example
pillar: P04
title: "Example — Supabase Data Layer for E-commerce"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [example, supabase, data-layer, ecommerce, config]
tldr: "E-commerce config: catalogo, pedidos, reviews, busca semantica, media de produtos, status real-time"
density_score: 0.90
---

# E-commerce — Supabase Data Layer

## Vertical Profile
| Aspect | Value |
|--------|-------|
| Vertical | ecommerce |
| Tier | pro |
| Key tables | products, orders, reviews, carts, categories |
| Extensions | pgvector (search), pg_cron (cleanup), pg_net (webhooks) |
| Storage | product-images (public), invoices (private) |
| Realtime | order status updates |
| Vectors | product semantic search |

## Config
```yaml
identidade:
  vertical: ecommerce
  regiao: sa-east-1
  tier: pro

database:
  schemas: [public, internal]
  extensions:
    obrigatorias: [pgcrypto, pg_graphql]
    opcionais: [pgvector, pg_cron, pg_net]
  tables:
    - name: categories
      columns: [id UUID PK, org_id UUID FK, name TEXT, slug TEXT UNIQUE, parent_id UUID FK SELF]
      rls: org_member
    - name: products
      columns: [id UUID PK, org_id UUID FK, category_id UUID FK, name TEXT, description TEXT, price NUMERIC(10,2), stock INT, status TEXT, embedding VECTOR(1536)]
      rls: org_member
      indexes: [org_id, category_id, status, "embedding HNSW vector_cosine_ops"]
    - name: orders
      columns: [id UUID PK, user_id UUID FK, org_id UUID FK, total NUMERIC(10,2), status TEXT DEFAULT 'pending', items JSONB]
      rls: owner
      indexes: [user_id, org_id, status, created_at]
    - name: reviews
      columns: [id UUID PK, product_id UUID FK, user_id UUID FK, rating INT CHECK 1-5, content TEXT]
      rls: public_read_owner_write
    - name: carts
      columns: [id UUID PK, user_id UUID FK, items JSONB, expires_at TIMESTAMPTZ]
      rls: owner

auth:
  providers: [email, google, apple]
  mfa: false
  custom_claims: [org_id, role]

rls:
  multi_tenant_column: org_id
  patterns:
    - nome: org_member
      policy: "org_id = (auth.jwt()->'app_metadata'->>'org_id')::uuid"
      tabelas: [categories, products]
    - nome: owner
      policy: "user_id = auth.uid()"
      tabelas: [orders, carts]
    - nome: public_read_owner_write
      policy: "true FOR SELECT; user_id = auth.uid() FOR INSERT/UPDATE/DELETE"
      tabelas: [reviews]

storage:
  buckets:
    - nome: product-images
      publico: true
      max_file_size: 10485760
      allowed_mime_types: [image/jpeg, image/png, image/webp]
      transform: true
    - nome: invoices
      publico: false
      max_file_size: 5242880
      allowed_mime_types: [application/pdf]

realtime:
  habilitado: true
  postgres_changes:
    - tabela: orders
      eventos: [UPDATE]
      filter: "status=eq.shipped"

vectors:
  habilitado: true
  embedding_model: text-embedding-3-small
  dimensions: 1536
  distance_function: cosine
  search_function: match_products

edge_functions:
  functions:
    - nome: process-payment
      trigger: http
      secrets: [STRIPE_KEY, WEBHOOK_SECRET]
    - nome: cleanup-expired-carts
      trigger: cron
      schedule: "0 3 * * *"
  deploy_method: cli

budget:
  alertas:
    - metrica: db_size
      threshold: 75
      acao: email
    - metrica: bandwidth
      threshold: 90
      acao: email
```
