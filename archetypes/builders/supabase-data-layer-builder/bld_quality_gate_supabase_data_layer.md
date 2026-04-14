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
llm_function: GOVERN
---
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
