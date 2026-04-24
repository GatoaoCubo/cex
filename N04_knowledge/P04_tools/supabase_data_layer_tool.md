---
id: p04_tool_supabase_data_layer
kind: cli_tool
8f: F5_call
pillar: P04
title: "Supabase Data Layer — N04 Provisioning Tool"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [tool, supabase, data-layer, provisioning, N04, cli]
tldr: "CLI tool para N04 provisionar data layer Supabase completo a partir de config YAML — schema, RLS, storage, realtime, vectors, edge functions"
density_score: 0.89
related:
  - p12_wf_supabase_setup
  - bld_manifest_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - bld_collaboration_supabase_data_layer
  - bld_output_template_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - p01_kc_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - p12_dispatch_rule_supabase
  - bld_architecture_supabase_data_layer
---

# Supabase Data Layer Tool

## Purpose
N04 uses this tool to transform a company config YAML into a complete Supabase data layer: migration SQL, RLS policies, storage buckets, realtime channels, vector indexes, and edge function scaffolds.

## Usage
```bash
# Generate migrations from config
python _tools/supabase_data_layer.py generate --config path/to/config.yaml --output supabase/migrations/

# Validate config against schema
python _tools/supabase_data_layer.py validate --config path/to/config.yaml

# Dry-run: show what would be created
python _tools/supabase_data_layer.py plan --config path/to/config.yaml
```

## Pipeline Stages
| Stage | Input | Output | Validation | Size |
|-------|-------|--------|------------|------|
| validate | config.yaml | schema check | JSON schema + required fields | — |
| plan | validated config | preview report | SQL syntax + naming | ~2KB |
| schema | database section | CREATE TABLE + indexes | foreign key integrity | ~5KB |
| auth | auth section | provider config | OAuth redirect URLs | ~1KB |
| rls | rls section | CREATE POLICY | policy syntax + roles | ~3KB |
| storage | storage section | bucket creation + policies | bucket names + MIME types | ~2KB |
| realtime | realtime section | ALTER PUBLICATION | table exists check | ~500B |
| vectors | vectors section | extension + match function | vector dimensions | ~4KB |
| edge_functions | edge_functions section | TypeScript scaffolds | function names + imports | ~8KB |
| mcp | integracao_cex section | MCP server config | port conflicts | ~1KB |

## Config Sections Processed
| Section | Output | File |
|---------|--------|------|
| database | CREATE TABLE + indexes | `migrations/001_schema.sql` |
| auth | Provider config | `migrations/002_auth.sql` |
| rls | CREATE POLICY statements | `migrations/003_rls.sql` |
| storage | Bucket creation + policies | `migrations/004_storage.sql` |
| realtime | ALTER PUBLICATION | `migrations/005_realtime.sql` |
| vectors | Extension + tables + indexes + match fn | `migrations/006_vectors.sql` |
| edge_functions | Function scaffolds | `functions/{name}/index.ts` |
| integracao_cex | MCP config | `.mcp.json` |

## Builder Reference
- Builder ISOs: `archetypes/builders/supabase-data-layer-builder/` (14 files)
- Template: `P04_tools/templates/tpl_supabase_data_layer.md`
- Examples: `P04_tools/examples/ex_supabase_data_layer_*.md` (4 verticals)
- Platform KCs: `P01_knowledge/library/platform/kc_supabase_*.md` (12 modules)

## Nucleus Integration
| Nucleus | What This Tool Produces For It |
|---------|-------------------------------|
| N01 | pgvector tables + match_documents() for RAG |
| N02 | Storage buckets + content tables |
| N03 | Migration files for deploy pipeline |
| N05 | pg_cron jobs + monitoring queries |
| N06 | CRM tables + RLS policies |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_supabase_setup]] | downstream | 0.48 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.46 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.36 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.35 |
| [[bld_output_template_supabase_data_layer]] | upstream | 0.34 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.32 |
| [[p01_kc_supabase_data_layer]] | related | 0.31 |
| [[bld_knowledge_card_supabase_data_layer]] | upstream | 0.31 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.29 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.28 |
