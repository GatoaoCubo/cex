---
id: p01_kc_supabase_cli
kind: knowledge_card
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
tldr: "CLI completo: init/link/start para dev local, migration new/push para schema, db diff/inspect para auditoria, functions deploy para edge, e branching para staging"
when_to_use: "Quando gerenciar Supabase via terminal (dev local, migrations, deploys)"
keywords: [supabase-cli, migrations, db-diff, functions-deploy]
long_tails:
  - Como fazer migration no Supabase CLI passo a passo
  - Diferenca entre supabase db push e supabase db reset
  - Como comparar schema local vs remoto com supabase db diff
axioms:
  - SEMPRE use migrations versionadas, nunca SQL direto em produção
  - NUNCA faça db push em produção sem testar com db reset local antes
  - SEMPRE commit migrations no git junto com o código
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
scope: Dev local, migrations, deploy, inspect, branching
owner: n04_knowledge
criticality: high
install: npm install -g supabase
version: supabase --version (1.x+)
```

## Setup Inicial
```bash
supabase init                      # Cria supabase/ dir com config.toml
supabase login                     # Auth com access token
supabase link --project-ref abc123 # Conecta ao projeto cloud
supabase start                     # Inicia stack local (Docker)
supabase stop                      # Para stack local
```

## Dev Local (Docker Stack)
```text
supabase start → inicia todos os serviços locais:
  Studio:      http://localhost:54323
  API (REST):  http://localhost:54321
  GraphQL:     http://localhost:54321/graphql/v1
  DB:          postgresql://postgres:postgres@localhost:54322/postgres
  Inbucket:    http://localhost:54324 (email testing)
  Edge:        http://localhost:54321/functions/v1/
```

## Comandos Essenciais
| Comando | Funcao | Frequência |
|---------|--------|------------|
| `supabase migration new nome` | Cria arquivo migration SQL vazio | Cada mudanca schema |
| `supabase db push` | Aplica migrations pendentes no remote | Cada deploy |
| `supabase db reset` | Reseta local: drop + migrations + seed | Dev/test |
| `supabase db diff --schema public` | Compara local vs remote | Antes de deploy |
| `supabase db lint` | Verifica schema issues | CI/CD |
| `supabase inspect db` | Estatísticas: tamanho, locks, queries | Debug |
| `supabase functions deploy` | Deploy edge functions | Cada mudanca |
| `supabase secrets set K=V` | Define env vars para edge functions | Config |
| `supabase gen types typescript` | Gera TypeScript types do schema | Após migration |

## Migration Workflow
```text
1. supabase migration new add_products_table
   → cria supabase/migrations/20260331120000_add_products_table.sql

2. Editar o SQL:
   CREATE TABLE products (
     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
     name TEXT NOT NULL,
     price NUMERIC(10,2) NOT NULL
   );
   ALTER TABLE products ENABLE ROW LEVEL SECURITY;

3. supabase db reset     # testa local (drop + replay all migrations)
4. supabase db diff      # confirma diff entre local e remote
5. supabase db push      # aplica no remote
6. git add supabase/migrations/ && git commit
```

## Seed Data
```bash
# supabase/seed.sql — executado após migrations no db reset
INSERT INTO products (name, price) VALUES
  ('Widget A', 29.90),
  ('Widget B', 49.90);

# Executar seed manualmente
supabase db reset  # inclui seed automaticamente
```

## Inspect + Branching
| Comando | Funcao |
|---------|--------|
| `inspect db table-sizes` | Tamanho tabelas |
| `inspect db cache-hit` | Cache hit ratio |
| `inspect db long-running-queries` | Queries >5min |
| `branches create X` | Branch isolado (Pro+) |
| `branches switch X` | Mudar branch ativo |

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| SQL direto no Dashboard prod | Schema drift, migration perdida | Sempre `migration new` |
| `db push` sem `db reset` antes | Migration falha em prod | Testar local primeiro |
| Migrations fora do git | Equipe desincronizada | Commit junto com code |
| Ignorar `db lint` | Schema issues em prod | Rodar no CI |

## Golden Rules
- TESTE toda migration com `db reset` local antes de `db push`
- GERE types com `gen types typescript` após cada migration
- VERSIONE `supabase/` inteiro no git (config + migrations + seed)
- USE `db diff` para detectar mudanças manuais no remote

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
