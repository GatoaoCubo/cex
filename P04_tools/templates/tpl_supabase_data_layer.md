---
id: p04_tpl_supabase_data_layer
kind: template
pillar: P04
title: "Template — Supabase Data Layer Config"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [template, supabase, data-layer, config, multi-tenant]
tldr: "Generic Supabase config template covering all 12 modules — fill [PLACEHOLDERS] for any company vertical"
density_score: 0.88
---

# Supabase Data Layer — Config Template

## Usage
1. Copy this template
2. Replace all `[PLACEHOLDER]` values with company-specific data
3. Run builder pipeline (Phase 1-10)
4. Output: migration SQL + RLS policies + module configs

## Config YAML
```yaml
# === IDENTITY ===
identidade:
  empresa: "[EMPRESA_NOME]"
  vertical: "[ecommerce|saas|marketplace|content|custom]"
  regiao: "[sa-east-1|us-east-1|eu-west-1|ap-southeast-1]"
  tier: "[free|pro|team|enterprise]"

# === PROJECT ===
projeto:
  project_ref: "[PROJECT_REF]"
  url: "https://[PROJECT_REF].supabase.co"

# === DATABASE ===
database:
  schemas: ["public"]
  extensions:
    obrigatorias: [pgcrypto, pg_graphql]
    opcionais: "[pgvector|pg_cron|pg_net|postgis|wrappers]"
  migrations_dir: "supabase/migrations/"
  seed_file: "supabase/seed.sql"

# === AUTH ===
auth:
  providers: "[email|google|apple|github|microsoft|...]"
  mfa: "[true|false]"
  sso: "[true|false]"
  custom_claims: [org_id, role]
  jwt_expiry: 3600

# === RLS ===
rls:
  multi_tenant_column: "org_id"
  admin_bypass: true
  patterns:
    - nome: "org_member"
      policy: "org_id = (auth.jwt()->'app_metadata'->>'org_id')::uuid"
      tabelas: "[LISTA_TABELAS]"
    - nome: "owner"
      policy: "user_id = auth.uid()"
      tabelas: "[LISTA_TABELAS]"

# === STORAGE ===
storage:
  buckets:
    - nome: "[BUCKET_NOME]"
      publico: "[true|false]"
      max_file_size: "[BYTES]"
      allowed_mime_types: "[image/jpeg|image/png|application/pdf|...]"
      transform: "[true|false]"

# === REALTIME ===
realtime:
  habilitado: "[true|false]"
  postgres_changes:
    - tabela: "[TABELA]"
      eventos: "[INSERT|UPDATE|DELETE|*]"

# === VECTORS ===
vectors:
  habilitado: "[true|false]"
  embedding_model: "[text-embedding-3-small|nomic-embed-text|...]"
  dimensions: "[1536|768|1024|3072]"
  distance_function: "[cosine|inner_product|l2]"

# === EDGE FUNCTIONS ===
edge_functions:
  functions:
    - nome: "[FUNCTION_NOME]"
      trigger: "[http|cron|webhook]"
      schedule: "[CRON_EXPR]"
  deploy_method: "[cli|github_actions]"

# === CEX INTEGRATION ===
integracao_cex:
  nuclei_consumers:
    - nucleo: "[N01-N06]"
      uso: "[DESCRICAO]"
  mcp_habilitado: "[true|false]"

# === BUDGET ===
budget:
  alertas:
    - metrica: "[db_size|bandwidth|storage|edge_invocations]"
      threshold: "[75|90]"
      acao: "[email|slack|webhook]"
```
