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
density_score: 0.91
llm_function: CALL
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
