---
id: p01_kc_supabase_self_hosting
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Self-Hosting — Docker Compose Stack Completo"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, self-hosting, docker, kong, gotrue, realtime, platform]
tldr: "Stack completo via Docker Compose: Kong (gateway) + GoTrue (auth) + PostgREST + Realtime + Storage + Studio + PostgreSQL 15+, totalmente open-source MIT"
when_to_use: "Quando fazer self-hosting do Supabase em infraestrutura propria"
keywords: [supabase-self-hosting, docker-compose, kong, gotrue]
long_tails:
  - Como fazer self-hosting do Supabase com Docker Compose
  - Arquitetura interna dos servicos do Supabase
  - Como configurar Kong API gateway no Supabase self-hosted
axioms:
  - SEMPRE altere TODAS as senhas e JWT secrets do .env default
  - NUNCA exponha portas internas (5432, 3000, 9999) diretamente
  - SEMPRE use reverse proxy (nginx/caddy) com HTTPS na frente do Kong
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_auth]
density_score: 0.87
data_source: "https://supabase.com/docs/guides/self-hosting"
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p01_kc_supabase_edge_functions
  - bld_manifest_supabase_data_layer
  - p01_kc_supabase_database
  - p12_mission_supabase_data_layer
  - p12_wf_supabase_setup
  - p01_kc_supabase_api
  - bld_examples_app_directory_entry
  - bld_instruction_supabase_data_layer
---

# Supabase Self-Hosting

## Quick Reference
```yaml
topic: supabase_self_hosting
scope: Docker Compose, serviços internos, configuração, segurança
owner: n04_knowledge
criticality: medium
license: MIT (totalmente open-source)
repo: github.com/supabase/supabase (docker/ dir)
```

## Arquitetura de Serviços
```text
[Internet] → [Nginx/Caddy HTTPS] → [Kong :8000 API Gateway]
                                        ├── /auth/v1      → GoTrue :9999
                                        ├── /rest/v1      → PostgREST :3000
                                        ├── /graphql/v1   → pg_graphql (via PostgREST)
                                        ├── /realtime/v1  → Realtime :4000
                                        ├── /storage/v1   → Storage API :5000
                                        └── /functions/v1 → Edge Runtime :54321
                                    
[Studio :3001] → [Meta API] → PostgreSQL :5432
                                  ├── pgvector
                                  ├── pg_graphql
                                  ├── pg_cron
                                  └── pg_net
```

## Serviços Docker Compose
| Serviço | Imagem | Porta | Funcao |
|---------|--------|-------|--------|
| kong | kong:2.8 | 8000 | API gateway, routing, rate limiting |
| auth (GoTrue) | supabase/gotrue | 9999 | Auth, JWT, OAuth providers |
| rest (PostgREST) | postgrest/postgrest | 3000 | REST API auto-gerada |
| realtime | supabase/realtime | 4000 | WebSocket channels |
| storage | supabase/storage-api | 5000 | File storage + imgproxy |
| imgproxy | darthsim/imgproxy | 5001 | Image transforms |
| edge-runtime | supabase/edge-runtime | 54321 | Deno functions |
| studio | supabase/studio | 3001 | Dashboard web |
| db | supabase/postgres | 5432 | PostgreSQL 15+ |
| analytics | supabase/logflare | 4000 | Log aggregation |

## Setup Rápido
```bash
git clone --depth 1 https://github.com/supabase/supabase.git
cd supabase/docker && cp .env.example .env
# Editar: POSTGRES_PASSWORD, JWT_SECRET, ANON_KEY, SERVICE_ROLE_KEY
docker compose up -d  # Studio: :3001, API: :8000
```

## Variáveis de Ambiente Críticas
| Variável | O Que É | Risco Se Default |
|----------|---------|------------------|
| POSTGRES_PASSWORD | Senha do DB | Acesso total ao banco |
| JWT_SECRET | Secret para assinar JWTs | Forge de tokens |
| ANON_KEY | JWT com role anon | Funciona mas inseguro |
| SERVICE_ROLE_KEY | JWT com role service | Bypass total de RLS |
| DASHBOARD_USERNAME | Login do Studio | Acesso ao dashboard |
| SITE_URL | URL da aplicação | OAuth redirects quebram |

## Cloud vs Self-Hosted
| Aspecto | Cloud | Self-Hosted |
|---------|-------|-------------|
| Setup | 2 min | 30-60 min |
| Custo | USD 25/mo (Pro) | USD 10-50/mo VPS |
| Compliance | SOC2 (Team+) | Total controle |
| Backups | Automáticos | Configurar |

## Requisitos: 4GB RAM, 2 cores, 20GB SSD, Docker 20.10+, Linux

## Anti-Patterns
| Anti-Pattern | Fix |
|-------------|-----|
| .env default em prod | Gerar todos os secrets |
| Sem reverse proxy HTTPS | Caddy + Let's Encrypt |
| Portas internas expostas | Firewall: só 80/443 |
| Sem backup automático | pg_dump + cron + S3 |

## Golden Rules
- GERE todos os secrets antes do primeiro start (JWT, passwords, keys)
- COLOQUE reverse proxy HTTPS (Caddy é o mais simples)
- CONFIGURE backups automáticos (pg_dump + cron + offsite storage)
- MONITORE com pg_stat_statements + container health checks
- ATUALIZE regularmente (docker compose pull + up -d)

## References
- Docs: https://supabase.com/docs/guides/self-hosting
- Docker: https://supabase.com/docs/guides/self-hosting/docker
- GitHub: https://github.com/supabase/supabase/tree/master/docker

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | downstream | 0.52 |
| [[p01_kc_supabase_cli]] | sibling | 0.45 |
| [[p01_kc_supabase_edge_functions]] | sibling | 0.37 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.37 |
| [[p01_kc_supabase_database]] | sibling | 0.33 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.32 |
| [[p12_wf_supabase_setup]] | downstream | 0.31 |
| [[p01_kc_supabase_api]] | sibling | 0.31 |
| [[bld_examples_app_directory_entry]] | downstream | 0.30 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.30 |
