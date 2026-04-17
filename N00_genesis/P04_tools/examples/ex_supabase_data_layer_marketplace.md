---
id: p04_ex_supabase_data_layer_marketplace
kind: example
pillar: P04
title: "Example — Supabase Data Layer for Marketplace"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [example, supabase, data-layer, marketplace, config]
tldr: "Marketplace config: sellers, listings, transactions, disputes, ratings, busca semantica de produtos, media de listings"
density_score: 0.89
---

# Marketplace — Supabase Data Layer

## Vertical Profile
| Aspect | Value |
|--------|-------|
| Vertical | marketplace |
| Tier | pro |
| Key tables | sellers, listings, transactions, disputes, ratings |
| Extensions | pgvector (search), pg_cron (payouts), pg_net (notifications) |
| Storage | listing-images (public), kyc-documents (private) |
| Realtime | bid updates, transaction status |
| Vectors | Listing semantic search |

## Config
```yaml
identidade:
  vertical: marketplace
  regiao: sa-east-1
  tier: pro

database:
  schemas: [public, payments]
  extensions:
    obrigatorias: [pgcrypto, pg_graphql]
    opcionais: [pgvector, pg_cron, pg_net, pg_trgm]
  tables:
    - name: sellers
      columns: [id UUID PK, user_id UUID FK auth.users, org_id UUID FK, display_name TEXT, verified BOOLEAN, rating_avg NUMERIC(3,2)]
      rls: public_read_owner_write
      indexes: [user_id, org_id, verified]
    - name: listings
      columns: [id UUID PK, seller_id UUID FK, org_id UUID FK, title TEXT, description TEXT, price NUMERIC(10,2), status TEXT, embedding VECTOR(1536)]
      rls: public_read_seller_write
      indexes: [seller_id, status, price, "embedding HNSW vector_cosine_ops"]
    - name: transactions
      schema: payments
      columns: [id UUID PK, listing_id UUID FK, buyer_id UUID FK, seller_id UUID FK, amount NUMERIC(10,2), status TEXT, escrow_until TIMESTAMPTZ]
      rls: buyer_or_seller
      indexes: [buyer_id, seller_id, status]
    - name: disputes
      schema: payments
      columns: [id UUID PK, transaction_id UUID FK, opened_by UUID FK, reason TEXT, status TEXT, resolution TEXT]
      rls: dispute_parties
    - name: ratings
      columns: [id UUID PK, transaction_id UUID FK, from_user UUID FK, to_user UUID FK, score INT CHECK 1-5, comment TEXT]
      rls: public_read_buyer_write

auth:
  providers: [email, google, apple]
  mfa: false
  custom_claims: [org_id, role, seller_id]

rls:
  multi_tenant_column: org_id
  patterns:
    - nome: public_read_seller_write
      policy: "true FOR SELECT; seller_id = (auth.jwt()->'app_metadata'->>'seller_id')::uuid FOR INSERT/UPDATE"
      tabelas: [listings]
    - nome: buyer_or_seller
      policy: "buyer_id = auth.uid() OR seller_id = auth.uid()"
      tabelas: [transactions]

storage:
  buckets:
    - nome: listing-images
      publico: true
      max_file_size: 10485760
      allowed_mime_types: [image/jpeg, image/png, image/webp]
      transform: true
    - nome: kyc-documents
      publico: false
      max_file_size: 20971520
      allowed_mime_types: [application/pdf, image/jpeg, image/png]

realtime:
  habilitado: true
  postgres_changes:
    - tabela: transactions
      eventos: [UPDATE]
    - tabela: listings
      eventos: [INSERT]

vectors:
  habilitado: true
  embedding_model: text-embedding-3-small
  dimensions: 1536
  distance_function: cosine
  search_function: match_listings

edge_functions:
  functions:
    - nome: process-escrow
      trigger: cron
      schedule: "0 */4 * * *"
      secrets: [PAYMENT_GATEWAY_KEY]
    - nome: notify-seller
      trigger: webhook
      secrets: [SENDGRID_KEY]
  deploy_method: cli

budget:
  alertas:
    - metrica: db_size
      threshold: 75
      acao: email
```
