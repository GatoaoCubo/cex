---
id: p01_kc_supabase_edge_functions
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Edge Functions — Deno Runtime, Global Deploy"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, edge-functions, deno, serverless, typescript, platform]
tldr: "Serverless functions in Deno/TypeScript: global deploy, secrets management, configurable CORS, CPU limits 2s(free)/10s(pro)/150s(team)"
when_to_use: "When configuring serverless compute (webhooks, cron, custom API) in Supabase"
keywords: [edge-functions, deno, serverless, supabase-functions]
long_tails:
  - How to create an edge function with Supabase CLI
  - CPU and memory limits of Supabase Edge Functions
  - How to configure CORS in Supabase Edge Functions
axioms:
  - ALWAYS use Deno.env.get() for secrets, never hardcode
  - NEVER exceed the tier CPU limit — function is killed without warning
  - ALWAYS return CORS headers for browser calls
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_cli, p01_kc_supabase_database]
density_score: 0.88
data_source: "https://supabase.com/docs/guides/functions"
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - bld_manifest_supabase_data_layer
  - p12_wf_supabase_setup
  - p01_kc_supabase_self_hosting
  - bld_instruction_supabase_data_layer
  - p01_kc_supabase_data_layer
  - p01_kc_supabase_database
  - p12_mission_supabase_data_layer
  - bld_examples_app_directory_entry
---

# Supabase Edge Functions — Deno Runtime

## Quick Reference
```yaml
topic: supabase_edge_functions
scope: Deno serverless runtime, deploy, secrets, CORS
owner: n04_knowledge
criticality: high
service: edge-runtime (port 54321 local)
runtime: Deno (native TypeScript, no node_modules)
```

## Limits per Tier
| Metric | Free | Pro | Team |
|--------|------|-----|------|
| Invocations/month | 500,000 | 2,000,000 | 2,000,000+ |
| CPU time/invocation | 2s | 10s | 150s |
| Memory | 256 MB | 256 MB | 512 MB |
| Payload size | 2 MB | 6 MB | 6 MB |
| Concurrent executions | 10 | 100 | 200+ |
| Deploy regions | 1 | Global (11+ regions) | Global |

## Anatomy of an Edge Function
```typescript
// supabase/functions/hello-world/index.ts
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: corsHeaders })

  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )

  const { data, error } = await supabase.from('orders').select('*').limit(10)

  return new Response(JSON.stringify({ data, error }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    status: 200,
  })
})
```

## CLI Workflow
```text
supabase functions new hello-world       # creates scaffold
supabase functions serve                 # local dev (port 54321)
supabase secrets set API_KEY=sk-xxx      # set secrets
supabase functions deploy hello-world    # deploy to production
supabase functions deploy --no-verify-jwt # no auth required
```

## Invocation Triggers
| Trigger | How | Example |
|---------|------|---------|
| HTTP | `POST /functions/v1/fn-name` | Client SDK, fetch, webhook receiver |
| Cron | pg_cron chama via pg_net | `SELECT net.http_post(url, body)` daily |
| Database webhook | Trigger SQL → Edge Function | `AFTER INSERT ON orders` |
| Scheduled | Supabase Dashboard cron config | Every 5 minutes |

## Secrets Management
```bash
# Set secrets (not visible in code)
supabase secrets set OPENAI_KEY=sk-xxx STRIPE_KEY=sk-xxx

# List secrets (names only, no values)
supabase secrets list

# Access in function
const apiKey = Deno.env.get('OPENAI_KEY')

# Built-in (auto-available):
# SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_DB_URL
```

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Import node_modules | Deno does not use npm (except esm.sh) | Use Deno std or esm.sh |
| CPU-heavy sync code | Killed at 2s (free) without warning | Offload to background job |
| Hardcode secrets | Exposed on deploy, in git | `Deno.env.get()` + `supabase secrets set` |
| No CORS headers | Browser blocked, 403 | Always return CORS headers |
| No JWT verification | Anyone can call the function | Keep JWT verify (default) |

## Golden Rules
- ALWAYS respond to OPTIONS with CORS headers for browser clients
- USE `esm.sh` for npm packages inside Deno
- SAVE CPU for logic — use `pg_net` for async HTTP calls
- TEST locally with `supabase functions serve` before deploy

## References
- Docs: https://supabase.com/docs/guides/functions
- Examples: https://github.com/supabase/supabase/tree/master/examples/edge-functions
- Deno: https://deno.land/manual

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | downstream | 0.58 |
| [[p01_kc_supabase_cli]] | sibling | 0.46 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.39 |
| [[p12_wf_supabase_setup]] | downstream | 0.37 |
| [[p01_kc_supabase_self_hosting]] | sibling | 0.36 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.33 |
| [[p01_kc_supabase_data_layer]] | sibling | 0.30 |
| [[p01_kc_supabase_database]] | sibling | 0.29 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.29 |
| [[bld_examples_app_directory_entry]] | downstream | 0.27 |
