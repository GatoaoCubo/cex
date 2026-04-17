---
kind: instruction
id: bld_instruction_oauth_app_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for oauth_app_config
quality: 8.8
title: "Instruction Oauth App Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [oauth_app_config, builder, instruction]
tldr: "Step-by-step production process for oauth_app_config"
domain: "oauth_app_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify partner integration requirements (scopes, redirect URIs).  
2. Document required OAuth2/PKCE flow variants (implicit, authorization code).  
3. Determine token lifetime constraints (access/refresh token durations).  
4. Analyze partner compliance with OIDC or OAuth2.0 specifications.  
5. Map refresh policy rules (e.g., sliding expiration, token rotation).  
6. Verify redirect URI formats (HTTPS, registered domains).  

## Phase 2: COMPOSE  
1. Define `client_id` and `client_secret` per partner.  
2. Enumerate `scopes` using SCHEMA.md's `scope` enum values.  
3. Specify `redirect_uris` array with exact URI strings.  
4. Set `access_token_lifetime` in seconds (min 300, max 86400).  
5. Configure `refresh_token_lifetime` (min 604800, max 2592000).  
6. Assign `refresh_policy` from SCHEMA.md's `refresh_policy` enum.  
7. Include `pkce_required` boolean flag (true for PKCE enforcement).  
8. Add `audience` field for API target identification.  
9. Finalize using OUTPUT_TEMPLATE.md structure with YAML formatting.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance checked via `jsonschema` validator.  
- [ ] ✅ All required fields (`client_id`, `scopes`, etc.) present.  
- [ ] ✅ Redirect URIs match registered domains and use HTTPS.  
- [ ] ✅ Token lifetimes within configured min/max bounds.  
- [ ] ✅ Refresh policy aligns with enum values and partner needs.
