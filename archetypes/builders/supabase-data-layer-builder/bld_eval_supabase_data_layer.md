---
id: bld_quality_gate_supabase_data_layer
kind: quality_gate
pillar: P02
title: "Quality Gates — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, quality-gate, validation]
density_score: 0.92
tldr: "Defines the few shot example specification for examples — supabase data layer builder, with structural rules, validation gates, and integration points."
llm_function: GOVERN
related:
  - bld_examples_supabase_data_layer
  - p04_ex_supabase_data_layer_ecommerce
  - bld_instruction_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - p04_ex_supabase_data_layer_marketplace
  - bld_knowledge_card_supabase_data_layer
  - p01_kc_supabase_multi_tenant
  - p04_ex_supabase_data_layer_saas
  - bld_memory_supabase_data_layer
  - p04_ex_supabase_data_layer_content
---

## Quality Gate

# Quality Gates

## HARD Gates (ALL must pass)
| # | Gate | Check | Fail Action |
|---|------|-------|-------------|
| H01 | RLS everywhere | Every table with user data has `ENABLE ROW LEVEL SECURITY` | Block — add RLS |
| H02 | No hardcode | Zero company names, API keys, project_refs, URLs reais | Block — replace with [PLACEHOLDER] |
| H03 | Multi-tenant ready | `org_id` column + RLS policy on all shared tables | Block — add org isolation |
| H04 | Tier-apownte | No features above declared tier | Block — downgrade or upgrade tier |
| H05 | Migration SQL | All schema changes as versioned migration files | Block — convert to migration |
| H06 | Config completeness | All required sections present in YAML | Block — add missing sections |
| H07 | Index coverage | Every FK, RLS column, and sort column has index | Block — add indexes |
| H08 | No service_role_key | service_role_key never appears in client config | Block — remove/move to server |

## SOFT Gates (score impact)
| # | Gate | Check | Score Impact |
|---|------|-------|-------------|
| S01 | All 12 modules addressed | Config mentions all relevant modules | -0.3 per missing |
| S02 | Extensions justified | Each enabled extension has documented use case | -0.2 per unjustified |
| S03 | Bucket policies | Each storage bucket has explicit mime + size limits | -0.2 per missing |
| S04 | Realtime scoped | Postgres Changes filtered by table + event | -0.3 if wildcard |
| S05 | Vector index type | HNSW recommended for >1K rows, documented | -0.2 if missing |
| S06 | Edge CORS | Every HTTP-triggered function has CORS headers | -0.2 per missing |
| S07 | Seed data | seed.sql with test data for dev environment | -0.1 if missing |
| S08 | Backup strategy | Backup plan documented per tier | -0.2 if missing |
| S09 | Cost estimate | Monthly cost estimate for declared tier | -0.1 if missing |
| S10 | Nucleus mapping | Which N01-N06 uses which tables/modules | -0.2 if missing |

## Scoring Formula
```
score = 10.0 - (hard_fails * BLOCK) - sum(soft_penalties)
PASS: score >= 8.0
BLOCK: any hard gate fail = score 0 until fixed
```

## Checklist (Quick)
- [ ] H01: RLS on every user-data table
- [ ] H02: grep -r "sk-\|sbp_\|eyJ\|supabase.co" → 0 results
- [ ] H03: org_id + JWT claim policy
- [ ] H04: Features ⊆ tier capabilities
- [ ] H05: Only migration SQL, no manual DDL
- [ ] H06: identity + project + database + auth + rls present
- [ ] H07: Indexes on FK + RLS + ORDER BY columns
- [ ] H08: service_role_key only in server/.env, never in client

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
