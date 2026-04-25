---
id: p01_kc_supabase_cli
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase CLI — Migrations, Seed, Diff, Inspect, Deploy"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.2
tags: [supabase, cli, migrations, seed, diff, inspect, deploy, platform]
tldr: "Full CLI: init/link/start for local dev, migration new/push for schema, db diff/inspect for auditing, functions deploy for edge, and branching for staging"
when_to_use: "When managing Supabase via terminal (local dev, migrations, deploys)"
keywords: [supabase-cli, migrations, db-diff, functions-deploy]
long_tails:
  - How to do migrations in Supabase CLI step by step
  - Difference between supabase db push and supabase db reset
  - How to compare local vs remote schema with supabase db diff
axioms:
  - ALWAYS use versioned migrations, never direct SQL in production
  - NEVER do db push in production without testing with local db reset first
  - ALWAYS commit migrations in git together with the code
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_edge_functions]
density_score: 0.90
data_source: "https://supabase.com/docs/guides/cli"
related:
  - bld_tools_supabase_data_layer
  - p12_wf_supabase_setup
  - p01_kc_supabase_database
  - p01_kc_supabase_edge_functions
  - p01_kc_supabase_self_hosting
  - bld_manifest_supabase_data_layer
  - p12_dispatch_rule_supabase
  - p12_mission_supabase_data_layer
  - bld_instruction_supabase_data_layer
  - p04_tool_supabase_data_layer
---

# Supabase CLI

## Quick Reference
```yaml
topic: supabase_cli
scope: Local dev, migrations, deploy, inspect, branching
owner: n04_knowledge
criticality: high
install: npm install -g supabase
version: supabase --version (1.x+)
```

## Initial Setup
```bash
supabase init                      # Creates supabase/ dir with config.toml
supabase login                     # Auth with access token
supabase link --project-ref abc123 # Connects to cloud project
supabase start                     # Starts local stack (Docker)
supabase stop                      # Stops local stack
```

## Dev Local (Docker Stack)
```text
supabase start → starts all local services:
  Studio:      http://localhost:54323
  API (REST):  http://localhost:54321
  GraphQL:     http://localhost:54321/graphql/v1
  DB:          postgresql://postgres:postgres@localhost:54322/postgres
  Inbucket:    http://localhost:54324 (email testing)
  Edge:        http://localhost:54321/functions/v1/
```

## Essential Commands
| Command | Function | Frequency |
|---------|----------|-----------|
| `supabase migration new name` | Creates empty SQL migration file | Each schema change |
| `supabase db push` | Applies pending migrations to remote | Each deploy |
| `supabase db reset` | Resets local: drop + migrations + seed | Dev/test |
| `supabase db diff --schema public` | Compares local vs remote | Before deploy |
| `supabase db lint` | Checks schema issues | CI/CD |
| `supabase inspect db` | Statistics: size, locks, queries | Debug |
| `supabase functions deploy` | Deploy edge functions | Each change |
| `supabase secrets set K=V` | Sets env vars for edge functions | Config |
| `supabase gen types typescript` | Generates TypeScript types from schema | After migration |

## Migration Workflow
```text
1. supabase migration new add_products_table
   → creates supabase/migrations/20260331120000_add_products_table.sql

2. Edit the SQL:
   CREATE TABLE products (
     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
     name TEXT NOT NULL,
     price NUMERIC(10,2) NOT NULL
   );
   ALTER TABLE products ENABLE ROW LEVEL SECURITY;

3. supabase db reset     # tests local (drop + replay all migrations)
4. supabase db diff      # confirms diff between local and remote
5. supabase db push      # applies to remote
6. git add supabase/migrations/ && git commit
```

## Seed Data
```bash
# supabase/seed.sql — executed after migrations on db reset
INSERT INTO products (name, price) VALUES
  ('Widget A', 29.90),
  ('Widget B', 49.90);

# Run seed manually
supabase db reset  # includes seed automatically
```

## Inspect + Branching
| Command | Function |
|---------|----------|
| `inspect db table-sizes` | Table sizes |
| `inspect db cache-hit` | Cache hit ratio |
| `inspect db long-running-queries` | Queries >5min |
| `branches create X` | Isolated branch (Pro+) |
| `branches switch X` | Switch active branch |

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Direct SQL in prod Dashboard | Schema drift, lost migration | Always `migration new` |
| `db push` without `db reset` first | Migration fails in prod | Test locally first |
| Migrations outside git | Team desynchronized | Commit together with code |
| Ignoring `db lint` | Schema issues in prod | Run in CI |

## Golden Rules
- TEST every migration with local `db reset` before `db push`
- GENERATE types with `gen types typescript` after each migration
- VERSION entire `supabase/` in git (config + migrations + seed)
- USE `db diff` to detect manual changes on remote

## References
- Docs: https://supabase.com/docs/guides/cli
- Install: https://supabase.com/docs/guides/cli/getting-started
- Config: https://supabase.com/docs/guides/cli/config

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | downstream | 0.75 |
| [[p12_wf_supabase_setup]] | downstream | 0.45 |
| [[p01_kc_supabase_database]] | sibling | 0.45 |
| [[p01_kc_supabase_edge_functions]] | sibling | 0.41 |
| [[p01_kc_supabase_self_hosting]] | sibling | 0.41 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.40 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.38 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.37 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.36 |
| [[p04_tool_supabase_data_layer]] | downstream | 0.35 |
