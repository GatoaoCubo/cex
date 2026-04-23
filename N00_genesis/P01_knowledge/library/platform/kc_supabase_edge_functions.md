---
id: p01_kc_supabase_edge_functions
kind: knowledge_card
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
tldr: "Serverless functions em Deno/TypeScript: deploy global, secrets management, CORS configuravel, CPU limits 2s(free)/10s(pro)/150s(team)"
when_to_use: "Quando configurar serverless compute (webhooks, cron, API custom) em Supabase"
keywords: [edge-functions, deno, serverless, supabase-functions]
long_tails:
  - Como criar edge function com Supabase CLI
  - Limites de CPU e memoria das Edge Functions Supabase
  - Como configurar CORS em Edge Functions Supabase
axioms:
  - SEMPRE use Deno.env.get() para secrets, nunca hardcode
  - NUNCA exceda o CPU limit do tier — function é killed sem aviso
  - SEMPRE retorne headers CORS para chamadas de browser
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
service: edge-runtime (porta 54321 local)
runtime: Deno (TypeScript nativo, sem node_modules)
```

## Limites por Tier
| Metrica | Free | Pro | Team |
|---------|------|-----|------|
| Invocations/mês | 500.000 | 2.000.000 | 2.000.000+ |
| CPU time/invocation | 2s | 10s | 150s |
| Memory | 256 MB | 256 MB | 512 MB |
| Payload size | 2 MB | 6 MB | 6 MB |
| Concurrent executions | 10 | 100 | 200+ |
| Deploy regions | 1 | Global (11+ regions) | Global |

## Anatomia de uma Edge Function
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
supabase functions new hello-world       # cria scaffold
supabase functions serve                 # dev local (porta 54321)
supabase secrets set API_KEY=sk-xxx      # definir secrets
supabase functions deploy hello-world    # deploy producao
supabase functions deploy --no-verify-jwt # sem auth required
```

## Triggers de Invocacao
| Trigger | Como | Exemplo |
|---------|------|---------|
| HTTP | `POST /functions/v1/fn-name` | Client SDK, fetch, webhook receiver |
| Cron | pg_cron chama via pg_net | `SELECT net.http_post(url, body)` daily |
| Database webhook | Trigger SQL → Edge Function | `AFTER INSERT ON orders` |
| Scheduled | Supabase Dashboard cron config | Every 5 minutes |

## Secrets Management
```bash
# Set secrets (não visíveis no código)
supabase secrets set OPENAI_KEY=sk-xxx STRIPE_KEY=sk-xxx

# List secrets (nomes apenas, sem valores)
supabase secrets list

# Acessar na function
const apiKey = Deno.env.get('OPENAI_KEY')

# Built-in (auto-disponíveis):
# SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_DB_URL
```

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| Import node_modules | Deno não usa npm (exceto esm.sh) | Usar Deno std ou esm.sh |
| CPU-heavy sync code | Kill em 2s (free) sem aviso | Offload para background job |
| Hardcode secrets | Expostos no deploy, no git | `Deno.env.get()` + `supabase secrets set` |
| Sem CORS headers | Browser blocked, 403 | Sempre retornar CORS headers |
| Sem verificacao JWT | Qualquer um chama a function | Manter JWT verify (default) |

## Golden Rules
- SEMPRE responda OPTIONS com CORS headers para browser clients
- USE `esm.sh` para pacotes npm dentro de Deno
- GUARDE CPU para lógica — use `pg_net` para chamadas HTTP assíncronas
- TESTE localmente com `supabase functions serve` antes de deploy

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
