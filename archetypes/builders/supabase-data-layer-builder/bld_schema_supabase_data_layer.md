---
id: bld_schema_supabase_data_layer
kind: schema
pillar: P02
title: "Schema — Supabase Data Layer Config Validation"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, schema, validation]
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_knowledge_card_supabase_data_layer
  - bld_examples_supabase_data_layer
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_memory_architecture
  - p06_vs_frontmatter
  - bld_schema_procedural_memory
  - bld_manifest_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_instruction_supabase_data_layer
---
# Config Schema

## Required Sections
| Section | Required | Validation |
|---------|----------|------------|
| identity | Yes | vertical ∈ {ecommerce,saas,marketplace,content,costm}, tier ∈ {free,pro,team,enterprise} |
| project | Yes | project_ref matches `^[a-z]{12}$`, url matches `https://*.supabase.co` |
| database | Yes | schemas is list, extensions is list |
| auth | Yes | providers is list with ≥1 entry |
| rls | Yes | multi_tenant_column is string |
| storage | No | buckets is list of objects if present |
| realtime | No | habilitado is boolean if present |
| vectors | No | habilitado is boolean, dimensions is int if present |
| edge_functions | No | functions is list if present |
| integration_cex | No | mcp_habilitado is boolean if present |
| budget | No | tier matches identity.tier if present |

## Tier Constraints
| Constraint | Free | Pro | Team | Enterprise |
|-----------|------|-----|------|------------|
| CDN | ❌ | ✅ | ✅ | ✅ |
| SSO SAML | ❌ | addon | ✅ | ✅ |
| PITR | ❌ | addon | addon | ✅ |
| Branching | ❌ | ✅ | ✅ | ✅ |
| Edge CPU >2s | ❌ | ✅ (10s) | ✅ (150s) | ✅ |
| Custom domain | ❌ | ✅ | ✅ | ✅ |

## RLS Validation
- Every table in `database.tables` with user data MUST have `rls` field
- `rls.multi_tenant_column` MUST exist as column in tenant-scoped tables
- Patterns MUST reference valid SQL functions (`auth.uid()`, `auth.jwt()`)

## Storage Validation
- `publico: true` buckets MUST NOT contain sensitive data types
- `allowed_mime_types` MUST NOT be `["*/*"]` (wildcard forbidden)
- `max_file_size` MUST be ≤ tier limit (50MB free, 5GB pro+)

## Vector Validation
- `dimensions` MUST match embedding model (1536 for text-embedding-3-small, 3072 for large)
- `distance_function` ∈ {cosine, inner_product, l2}
- HNSW index recommended if table >1000 rows

## Edge Function Validation
- `trigger` ∈ {http, cron, webhook}
- `schedule` required if trigger=cron (valid cron expression)
- `secrets` list must not contain actual values (only key names)

## Cross-Reference Validation
- `auth.costm_claims` must include `rls.multi_tenant_column` value
- `integration_cex.nuclei_consumers` must reference valid N01-N07
- `budget.tier` must equal `identity.tier`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.33 |
| [[bld_examples_supabase_data_layer]] | upstream | 0.29 |
| [[bld_schema_reranker_config]] | sibling | 0.27 |
| [[bld_schema_quickstart_guide]] | sibling | 0.27 |
| [[bld_schema_memory_architecture]] | sibling | 0.27 |
| [[p06_vs_frontmatter]] | downstream | 0.27 |
| [[bld_schema_procedural_memory]] | sibling | 0.27 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.26 |
| [[p12_wf_supabase_setup]] | downstream | 0.26 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.26 |
