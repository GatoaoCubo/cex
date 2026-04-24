---
id: p01_kc_supabase_auth
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Auth — GoTrue, 30+ Providers, RLS, MFA"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, auth, gotrue, rls, jwt, mfa, sso, platform]
tldr: "Auth completo via GoTrue: 30+ providers, JWT com custom claims, MFA TOTP, SSO SAML, anonymous auth, e RLS integrado ao PostgreSQL"
when_to_use: "Quando configurar autenticacao e autorizacao em projetos Supabase"
keywords: [supabase-auth, gotrue, rls, jwt, mfa]
long_tails:
  - Como configurar Google OAuth no Supabase Auth
  - Row Level Security com auth.uid() no PostgreSQL
  - Custom claims JWT para role-based access Supabase
axioms:
  - SEMPRE habilite RLS em toda tabela com dados de usuario
  - NUNCA use service_role_key no client-side
  - SEMPRE valide JWT server-side antes de confiar em custom claims
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_multi_tenant]
density_score: 0.90
data_source: "https://supabase.com/docs/guides/auth"
related:
  - p01_kc_supabase_multi_tenant
  - bld_instruction_supabase_data_layer
  - bld_examples_supabase_data_layer
  - p12_wf_supabase_setup
  - bld_manifest_supabase_data_layer
  - p04_tpl_supabase_data_layer
  - bld_memory_supabase_data_layer
  - bld_schema_supabase_data_layer
  - bld_system_prompt_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
---

# Supabase Auth — GoTrue + RLS

## Quick Reference
```yaml
topic: supabase_auth
scope: GoTrue server, OAuth providers, JWT, RLS, MFA, SSO
owner: n04_knowledge
criticality: high
service: gotrue (porta 9999)
```

## Auth Providers (30+)
| Categoria | Providers |
|-----------|-----------|
| Credential | Email/password, Phone/SMS (Twilio), Magic link |
| Social | Google, Apple, Facebook, Twitter/X, Discord, LinkedIn, Spotify |
| Developer | GitHub, GitLab, Bitbucket, Notion, Figma |
| Enterprise | Microsoft, Azure AD, Okta, Keycloak, WorkOS, SAML SSO |
| Other | Zoom, Kakao, Slack, Twitch, Anonymous auth |

## Auth Flow
```text
[Client] → signInWithOAuth({provider:'google'})
    → [GoTrue] → redirect OAuth provider
    → callback → [GoTrue] gera JWT
    → [Client] recebe session {access_token, refresh_token}
    → [PostgREST] valida JWT → auth.uid() disponivel em SQL
    → [RLS Policy] filtra dados por auth.uid()
```

## JWT Structure
```json
{
  "sub": "user-uuid",
  "email": "user@example.com",
  "role": "authenticated",
  "app_metadata": {"provider": "google", "org_id": "org-123"},
  "user_metadata": {"name": "User Name"},
  "exp": 1711900000
}
```

## RLS Patterns (Top 5)
| Pattern | Policy SQL | Uso |
|---------|-----------|-----|
| Owner | `auth.uid() = user_id` | User vê só seus dados |
| Org member | `auth.uid() IN (SELECT uid FROM members WHERE org_id = t.org_id)` | Multi-tenant |
| Role-based | `(auth.jwt()->>'role')::text = 'admin'` | Admin bypass |
| Public read | `true` (SELECT only) | Conteúdo público |
| Custom claim | `(auth.jwt()->'app_metadata'->>'plan')::text = 'pro'` | Feature gating |

## MFA (Multi-Factor Auth)
| Spec | Valor |
|------|-------|
| Metodo | TOTP (Google Authenticator, Authy) |
| Enrollment | `supabase.auth.mfa.enroll({factorType:'totp'})` |
| Verificacao | `supabase.auth.mfa.challengeAndVerify({factorId, code})` |
| AAL levels | aal1 (password only), aal2 (password + TOTP) |
| RLS check | `auth.jwt()->>'aal' = 'aal2'` para operacoes sensiveis |

## Limites por Tier
| Metrica | Free | Pro | Team |
|---------|------|-----|------|
| MAU (Monthly Active Users) | 50.000 | 100.000 | 100.000+ |
| Auth requests | Sem limite hard | Sem limite hard | Sem limite hard |
| Email confirmations | 4/hora (built-in) | Custom SMTP ilimitado | Custom SMTP |
| SMS OTP | Twilio (seu custo) | Twilio | Twilio |
| SSO SAML | Não | Addon | Incluido |
| Custom domains | Não | Sim | Sim |

## Session Management
- **Access token**: curto (1h default, configuravel `jwt_expiry`)
- **Refresh token**: longo (rotacao automatica)
- **onAuthStateChange**: listener client-side para session refresh
- **Server-side**: `getUser()` valida token a cada request (não confiar em `getSession()` sozinho)

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| RLS desabilitado | Qualquer user lê/escreve tudo | `ALTER TABLE t ENABLE ROW LEVEL SECURITY;` |
| service_role no client | Bypass total de RLS | Usar apenas server-side |
| Confiar em getSession() sem getUser() | Token expirado aceito | Sempre `getUser()` no server |
| JWT sem custom claims | Queries N+1 para checar permissoes | `app_metadata` via admin API |

## Golden Rules
- HABILITE RLS antes de inserir dados em qualquer tabela
- USE custom claims (app_metadata) para roles, não tabela separada
- CONFIGURE custom SMTP no Pro+ (built-in limita 4 emails/hora)
- IMPLEMENTE MFA (aal2) para operações sensíveis (billing, delete)

## References
- Docs: https://supabase.com/docs/guides/auth
- RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- GoTrue: https://github.com/supabase/gotrue

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_multi_tenant]] | sibling | 0.41 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.39 |
| [[bld_examples_supabase_data_layer]] | related | 0.35 |
| [[p12_wf_supabase_setup]] | downstream | 0.32 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.32 |
| [[p04_tpl_supabase_data_layer]] | downstream | 0.31 |
| [[bld_memory_supabase_data_layer]] | related | 0.30 |
| [[bld_schema_supabase_data_layer]] | downstream | 0.29 |
| [[bld_system_prompt_supabase_data_layer]] | downstream | 0.28 |
| [[bld_knowledge_card_supabase_data_layer]] | sibling | 0.28 |
