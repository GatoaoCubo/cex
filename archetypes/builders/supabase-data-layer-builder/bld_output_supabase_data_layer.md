---
id: bld_output_template_supabase_data_layer
kind: output_template
pillar: P03
title: "Output Template — Supabase Data Layer Config"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, output-template, config]
tldr: "Supabase Data Layer prompt: output template, formatting rules, and structure"
density_score: 0.87
llm_function: PRODUCE
related:
  - bld_instruction_supabase_data_layer
  - p04_ex_supabase_data_layer_saas
  - bld_examples_supabase_data_layer
  - p04_tpl_supabase_data_layer
  - p01_kc_supabase_multi_tenant
  - p04_tool_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - p04_ex_supabase_data_layer_ecommerce
  - p12_wf_supabase_setup
---
# Output Template

## Config YAML Structure
```yaml
# Supabase Data Layer Config — [VERTICAL] — [TIER]
identity:
  empresa: "[EMPRESA]"
  vertical: "[ecommerce|saas|marketplace|content|costm]"
  regiao: "[REGIAO]"
  tier: "[free|pro|team|enterprise]"

project:
  project_ref: "[REF]"
  url: "https://[REF].supabase.co"

database:
  schemas: [public]
  extensions: [pgvector, pg_cron]
  migrations_dir: "supabase/migrations/"

auth:
  providers: [email]
  mfa: false
  costm_claims: [org_id, role]

rls:
  multi_tenant_column: org_id
  patterns: []

storage:
  buckets: []

realtime:
  habilitado: false
  postgres_changes: []

vectors:
  habilitado: false

edge_functions:
  functions: []

integration_cex:
  mcp_habilitado: false

budget:
  alertas: []
```

## Migration SQL Template
```sql
-- Migration: [YYYYMMDD]_[description].sql
-- Vertical: [VERTICAL] | Tier: [TIER]

-- Extensions
CREATE EXTENSION IF NOT EXISTS "pgvector";
CREATE EXTENSION IF NOT EXISTS "pg_cron";

-- Core tables
CREATE TABLE IF NOT EXISTS organizations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  plan TEXT DEFAULT 'free',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS memberships (
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  org_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  role TEXT DEFAULT 'member',
  UNIQUE(user_id, org_id)
);

-- [VERTICAL-SPECIFIC TABLES HERE]

-- RLS
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE memberships ENABLE ROW LEVEL SECURITY;

-- Policies
CREATE POLICY "org_member" ON organizations
  FOR ALL USING (id = (auth.jwt()->'app_metadata'->>'org_id')::uuid);

-- Indexes
CREATE INDEX idx_memberships_user ON memberships(user_id);
CREATE INDEX idx_memberships_org ON memberships(org_id);
```

## Output Checklist
- [ ] Config YAML with ALL sections filled
- [ ] Migration SQL with RLS on every table
- [ ] Indexes on all FK + RLS columns
- [ ] Storage bucket policies defined
- [ ] Realtime publications configured (if enabled)
- [ ] Edge function scaffolds (if enabled)
- [ ] MCP config (if enabled)
- [ ] Tier limits documented in comments

## Cross-References

- **Pillar**: P03 (Prompt)
- **Kind**: `output template`
- **Artifact ID**: `bld_output_template_supabase_data_layer`
- **Tags**: [builder, supabase, data-layer, output-template, config]

## Output Pipeline

| Aspect | Detail |
|--------|--------|
| Template | Defines structure for output template outputs |
| Validation | Checked against `validation_schema` |
| Post-hook | Scored by `cex_score.py` after creation |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_supabase_data_layer]] | related | 0.48 |
| [[p04_ex_supabase_data_layer_saas]] | downstream | 0.44 |
| [[bld_examples_supabase_data_layer]] | upstream | 0.43 |
| [[p04_tpl_supabase_data_layer]] | downstream | 0.41 |
| [[p01_kc_supabase_multi_tenant]] | upstream | 0.41 |
| [[p04_tool_supabase_data_layer]] | downstream | 0.40 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.38 |
| [[bld_manifest_supabase_data_layer]] | related | 0.38 |
| [[p04_ex_supabase_data_layer_ecommerce]] | downstream | 0.37 |
| [[p12_wf_supabase_setup]] | downstream | 0.37 |
