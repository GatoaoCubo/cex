---
kind: examples
id: bld_examples_oauth_app_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of oauth_app_config artifacts
quality: 8.8
title: "Examples Oauth App Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [oauth_app_config, builder, examples]
tldr: "Golden and anti-examples of oauth_app_config artifacts"
domain: "oauth_app_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: oauth_app_config
name: github_integration
spec:
  client_id: "ghp_1234567890abcdef1234567890abcdef1234"
  client_secret: "supersecretclientsecret"
  redirect_uris:
    - "https://app.example.com/auth/callback"
  scopes:
    - "repo"
    - "user"
  token_lifetimes:
    access_token_expires_in: 3600
    refresh_token_expires_in: 86400
  refresh_policy: "rotate"
```

## Anti-Example 1: Missing Redirect URIs
```yaml
kind: oauth_app_config
name: bad_github_integration
spec:
  client_id: "ghp_0987654321abcdef0987654321abcdef0987"
  client_secret: "anothersecret"
  scopes:
    - "all"
```
## Why it fails
Lacks redirect_uris, allowing any redirect URI which creates open redirect vulnerabilities. Also uses "all" scope, granting excessive permissions.

## Anti-Example 2: Insecure Token Lifetimes
```yaml
kind: oauth_app_config
name: insecure_github_integration
spec:
  client_id: "ghp_1122334455abcdef1122334455abcdef1122"
  client_secret: "insecuresecret"
  redirect_uris:
    - "https://app.example.com/callback"
  scopes:
    - "public_repo"
  token_lifetimes:
    access_token_expires_in: 86400
    refresh_token_expires_in: 31536000
  refresh_policy: "reuse"
```
## Why it fails
Uses 1-year refresh tokens (31536000s) which is excessive and increases risk of token misuse. Refresh policy "reuse" allows tokens to be used indefinitely, violating security best practices.
