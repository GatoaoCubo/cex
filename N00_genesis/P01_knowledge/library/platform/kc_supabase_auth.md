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
tldr: "Complete auth via GoTrue: 30+ providers, JWT with custom claims, MFA TOTP, SSO SAML, anonymous auth, and RLS integrated with PostgreSQL"
when_to_use: "When configuring authentication and authorization in Supabase projects"
keywords: [supabase-auth, gotrue, rls, jwt, mfa]
long_tails:
  - How to configure Google OAuth in Supabase Auth
  - Row Level Security with auth.uid() in PostgreSQL
  - Custom JWT claims for role-based access in Supabase
axioms:
  - ALWAYS enable RLS on every table with user data
  - NEVER use service_role_key on the client-side
  - ALWAYS validate JWT server-side before trusting custom claims
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
| Category | Providers |
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
| Pattern | Policy SQL | Use |
|---------|-----------|-----|
| Owner | `auth.uid() = user_id` | User sees only their data |
| Org member | `auth.uid() IN (SELECT uid FROM members WHERE org_id = t.org_id)` | Multi-tenant |
| Role-based | `(auth.jwt()->>'role')::text = 'admin'` | Admin bypass |
| Public read | `true` (SELECT only) | Public content |
| Custom claim | `(auth.jwt()->'app_metadata'->>'plan')::text = 'pro'` | Feature gating |

## MFA (Multi-Factor Auth)
| Spec | Value |
|------|-------|
| Method | TOTP (Google Authenticator, Authy) |
| Enrollment | `supabase.auth.mfa.enroll({factorType:'totp'})` |
| Verification | `supabase.auth.mfa.challengeAndVerify({factorId, code})` |
| AAL levels | aal1 (password only), aal2 (password + TOTP) |
| RLS check | `auth.jwt()->>'aal' = 'aal2'` for sensitive operations |

## Limits per Tier
| Metric | Free | Pro | Team |
|--------|------|-----|------|
| MAU (Monthly Active Users) | 50,000 | 100,000 | 100,000+ |
| Auth requests | No hard limit | No hard limit | No hard limit |
| Email confirmations | 4/hour (built-in) | Custom SMTP unlimited | Custom SMTP |
| SMS OTP | Twilio (your cost) | Twilio | Twilio |
| SSO SAML | No | Addon | Included |
| Custom domains | No | Yes | Yes |

## Session Management
- **Access token**: short-lived (1h default, configurable `jwt_expiry`)
- **Refresh token**: long-lived (automatic rotation)
- **onAuthStateChange**: client-side listener for session refresh
- **Server-side**: `getUser()` validates token on each request (do not trust `getSession()` alone)

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| RLS disabled | Any user reads/writes everything | `ALTER TABLE t ENABLE ROW LEVEL SECURITY;` |
| service_role on client | Total RLS bypass | Use server-side only |
| Trusting getSession() without getUser() | Expired token accepted | Always `getUser()` on server |
| JWT without custom claims | N+1 queries to check permissions | `app_metadata` via admin API |

## Golden Rules
- ENABLE RLS before inserting data in any table
- USE custom claims (app_metadata) for roles, not a separate table
- CONFIGURE custom SMTP on Pro+ (built-in limits 4 emails/hour)
- IMPLEMENT MFA (aal2) for sensitive operations (billing, delete)

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
