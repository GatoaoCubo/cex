---
id: instance_supabase_config_template
kind: config
pillar: P02
title: "Instance Template — Supabase Data Layer Config"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [instance, template, supabase, config, placeholder]
tldr: "Company-agnostic Supabase config template — copy, fill [PLACEHOLDERS], run builder pipeline"
density_score: 0.85
related:
  - p04_tpl_supabase_data_layer
  - bld_config_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - p04_ex_supabase_data_layer_ecommerce
  - p04_ex_supabase_data_layer_content
  - p04_ex_supabase_data_layer_saas
  - p04_ex_supabase_data_layer_marketplace
  - bld_schema_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - bld_instruction_supabase_data_layer
---

# Supabase Config — Instance Template

> **Instructions**: Copy this file to `_instances/{company}/N04_knowledge/supabase_config.md`, replace ALL `[PLACEHOLDER]` values.

```yaml
# === COMPANY IDENTITY ===
identidade:
  empresa: "[EMPRESA_NOME]"
  vertical: "[ecommerce|saas|marketplace|content|custom]"
  regiao: "[sa-east-1|us-east-1|eu-west-1|ap-southeast-1]"
  tier: "[free|pro|team|enterprise]"

# === SUPABASE PROJECT ===
projeto:
  project_ref: "[PROJECT_REF_12_CHARS]"
  url: "https://[PROJECT_REF].supabase.co"

# === DATABASE ===
database:
  schemas: ["public", "[SCHEMA_EXTRA]"]
  extensions:
    obrigatorias: [pgcrypto, pg_graphql]
    opcionais: "[pgvector|pg_cron|pg_net|postgis|wrappers|plv8]"
  migrations_dir: "supabase/migrations/"
  seed_file: "supabase/seed.sql"

# === AUTH ===
auth:
  providers: "[email|google|apple|github|microsoft|discord|...]"
  mfa: "[true|false]"
  sso: "[true|false]"
  custom_claims: [org_id, role, "[CLAIM_EXTRA]"]
  redirect_urls: "[LISTA_URLS_PERMITIDOS]"
  jwt_expiry: "[SEGUNDOS]"

# === ROW LEVEL SECURITY ===
rls:
  multi_tenant_column: "[org_id|tenant_id|user_id]"
  admin_bypass: "[true|false]"
  patterns:
    - nome: "[PATTERN_NOME]"
      policy: "[SQL_POLICY]"
      tabelas: "[LISTA_TABELAS]"

# === STORAGE ===
storage:
  buckets:
    - nome: "[BUCKET_NOME]"
      publico: "[true|false]"
      max_file_size: "[BYTES]"
      allowed_mime_types: "[LISTA_MIMES]"
      transform: "[true|false]"
  cdn: "[true|false]"

# === REALTIME ===
realtime:
  habilitado: "[true|false]"
  postgres_changes:
    - tabela: "[TABELA]"
      eventos: "[INSERT|UPDATE|DELETE|*]"
      filter: "[FILTRO_OPCIONAL]"
  presence: "[true|false]"

# === VECTORS (pgvector) ===
vectors:
  habilitado: "[true|false]"
  embedding_model: "[text-embedding-3-small|nomic-embed-text|...]"
  dimensions: "[1536|768|1024|3072]"
  distance_function: "[cosine|inner_product|l2]"
  tabelas_vector:
    - nome: "[TABELA]"
      content_column: "[COLUNA]"
      embedding_column: "[COLUNA]"
      metadata_columns: "[LISTA_COLUNAS]"
  search_function: "[NOME_FUNCTION]"

# === EDGE FUNCTIONS ===
edge_functions:
  functions:
    - nome: "[FUNCTION_NOME]"
      trigger: "[http|cron|webhook]"
      schedule: "[CRON_EXPR]"
      secrets: "[LISTA_ENV_VARS]"
  deploy_method: "[cli|github_actions|manual]"

# === CEX INTEGRATION ===
integracao_cex:
  nuclei_consumers:
    - nucleo: "[N01|N02|...|N06]"
      uso: "[DESCRICAO]"
  mcp_habilitado: "[true|false]"
  mcp_tools: "[list_tables|execute_sql|apply_migration|...]"

# === BUDGET ===
budget:
  tier: "[MUST_MATCH_IDENTIDADE_TIER]"
  alertas:
    - metrica: "[db_size|bandwidth|storage|edge_invocations|auth_mau]"
      threshold: "[PERCENT]"
      acao: "[email|slack|webhook]"
```

## Validation
After filling, run:
```bash
python _tools/supabase_data_layer.py validate --config this_file.yaml
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tpl_supabase_data_layer]] | downstream | 0.77 |
| [[bld_config_supabase_data_layer]] | sibling | 0.39 |
| [[bld_output_template_supabase_data_layer]] | downstream | 0.35 |
| [[p04_ex_supabase_data_layer_ecommerce]] | downstream | 0.34 |
| [[p04_ex_supabase_data_layer_content]] | downstream | 0.34 |
| [[p04_ex_supabase_data_layer_saas]] | downstream | 0.34 |
| [[p04_ex_supabase_data_layer_marketplace]] | downstream | 0.32 |
| [[bld_schema_supabase_data_layer]] | related | 0.32 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.31 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.31 |
