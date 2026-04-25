---
id: bld_tools_supabase_data_layer
kind: tool_catalog
pillar: P04
title: "Tools — Supabase Data Layer Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [builder, supabase, data-layer, tools, cli, mcp, sdk]
tldr: "Supabase Data Layer tools: tool integrations, CLI commands, and external capabilities"
density_score: 0.91
llm_function: CALL
related:
  - p01_kc_supabase_cli
  - p01_kc_supabase_edge_functions
  - p12_wf_supabase_setup
  - p12_mission_supabase_data_layer
  - p01_kc_supabase_self_hosting
  - bld_manifest_supabase_data_layer
  - p01_kc_supabase_database
  - p12_dispatch_rule_supabase
  - bld_instruction_supabase_data_layer
  - bld_examples_app_directory_entry
---
# Tool Catalog

## Supabase CLI
| Command | Purpose | Phase |
|---------|---------|-------|
| `supabase init` | Initialize project structure | Setup |
| `supabase link --project-ref X` | Connect to cloud project | Setup |
| `supabase start` | Start local dev stack (Docker) | Dev |
| `supabase migration new NAME` | Create versioned migration | Schema |
| `supabase db reset` | Drop + replay migrations + seed | Test |
| `supabase db push` | Apply migrations to remote | Deploy |
| `supabase db diff` | Compare local vs remote schema | Audit |
| `supabase db lint` | Check schema issues | CI |
| `supabase gen types typescript` | Generate TS types from schema | Codegen |
| `supabase functions new NAME` | Scaffold edge function | Edge |
| `supabase functions serve` | Run functions locally | Dev |
| `supabase functions deploy NAME` | Deploy to production | Deploy |
| `supabase secrets set K=V` | Set edge function secrets | Config |
| `supabase inspect db table-sizes` | DB statistics | Monitor |

## MCP Servers
| Server | Package | Purpose |
|--------|---------|---------|
| Supabase | `npx -y @supabase/mcp-server-supabase --access-token sbp_xxx` | Project management, migrations, functions |
| Postgres | `npx -y @anthropic/mcp-server-postgres CONNECTION_STRING` | Direct SQL, bulk ops, EXPLAIN |

## Client SDKs
| Language | Package | Init Pattern |
|----------|---------|-------------|
| JavaScript | `@supabase/supabase-js` | `createClient(url, anonKey)` |
| Python | `supabase-py` | `create_client(url, key)` |
| Dart/Flutter | `supabase_flutter` | `Supabase.initialize(url:, anonKey:)` |
| Swift | `supabase-swift` | `SupabaseClient(supabaseURL:, supabaseKey:)` |
| Kotlin | `supabase-kt` | `createSupabaseClient(url, key)` |
| C# | `supabase-csharp` | `new Client(url, key)` |

## SQL Functions (Create in Migrations)
| Function | Purpose | Usage |
|----------|---------|-------|
| `match_documents(embedding, threshold, count)` | Semantic search via pgvector | `supabase.rpc('match_documents', {...})` |
| `handle_new_user()` | Auto-assign org on signup | Trigger on auth.users INSERT |
| `cleanup_expired()` | Delete old data | pg_cron: `SELECT cron.schedule('daily', ...)` |
| `notify_via_webhook(url, payload)` | HTTP call from SQL | pg_net: `SELECT net.http_post(...)` |

## Monitoring Tools
| Tool | Access | Purpose |
|------|--------|---------|
| Studio Dashboard | `https://supabase.com/dashboard` | Visual management |
| pg_stat_statements | SQL extension | Query performance |
| Supabase Logs | Dashboard > Logs | API, Auth, DB logs |
| Health endpoint | `GET /rest/v1/` | Uptime check |

## Integration Checklist
- [ ] CLI installed: `npm install -g supabase`
- [ ] Project linked: `supabase link --project-ref X`
- [ ] MCP configured: `.mcp.json` with supabase server
- [ ] SDK installed: language-specific package
- [ ] Types generated: `supabase gen types typescript`
- [ ] Secrets set: all edge function env vars configured

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_cli]] | upstream | 0.70 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.49 |
| [[p12_wf_supabase_setup]] | downstream | 0.47 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.46 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.43 |
| [[bld_manifest_supabase_data_layer]] | upstream | 0.42 |
| [[p01_kc_supabase_database]] | upstream | 0.41 |
| [[p12_dispatch_rule_supabase]] | downstream | 0.40 |
| [[bld_instruction_supabase_data_layer]] | upstream | 0.39 |
| [[bld_examples_app_directory_entry]] | downstream | 0.35 |
