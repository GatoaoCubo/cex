---
kind: examples
id: bld_examples_env_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of env_config artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: env-config-builder
## Golden Example
INPUT: "Define environment variables for the API service scope"
OUTPUT:
```yaml
id: p09_env_api_service
kind: env_config
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
scope: "api_service"
variables:
  - DATABASE_URL
  - API_PORT
  - LOG_LEVEL
  - JWT_SECRET_KEY
  - CORS_ORIGINS
  - MAX_CONNECTIONS
  - DEBUG
  - REDIS_URL
quality: null
tags: [env_config, api, service, P09, configuration]
tldr: "API service env: 8 vars (2 sensitive), port 8000, structured logging, JWT auth"
description: "Environment variables for the API service including database, auth, logging, and cache config"
environment: all
sensitive_count: 2
override: "env var > .env file > default"
validation: "type check + format validation per variable"
```
## Overview
Environment variables for the API service covering database, authentication, logging, and cache.
Consumed by FastAPI application at startup; missing required vars block boot.
## Variable Catalog
| Variable | Type | Required | Default | Sensitive | Validation |
|----------|------|----------|---------|-----------|------------|
| DATABASE_URL | url | yes | - | yes | postgresql:// prefix |
| API_PORT | integer | no | 8000 | no | range 1024-65535 |
| LOG_LEVEL | string | no | INFO | no | enum: DEBUG, INFO, WARNING, ERROR |
| JWT_SECRET_KEY | secret | yes | - | yes | min 32 chars, alphanumeric |
| CORS_ORIGINS | string | no | "*" | no | comma-separated URLs or "*" |
| MAX_CONNECTIONS | integer | no | 20 | no | range 1-100 |
| DEBUG | boolean | no | false | no | true/false only |
| REDIS_URL | url | no | - | no | redis:// prefix |
## Override Precedence
Standard 3-tier override for all variables:
1. Environment variable set in shell/container (highest priority)
2. Value in .env file (loaded by python-dotenv)
3. Default value from this spec (lowest priority)
Required variables with no default MUST be set via tier 1 or 2; missing = startup failure.
## Sensitive Variables
- DATABASE_URL: mask after `://` in logs — store in secrets manager or encrypted .env
- JWT_SECRET_KEY: never log, never commit — generate with `openssl rand -hex 32`
All sensitive vars: excluded from debug output, masked in error reports, rotatable without restart.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_env_ pattern (H02 pass)
- kind: env_config (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Variable Catalog, Override Precedence, Sensitive Variables (H07 pass)
- variables list matches catalog names exactly (S03 pass)
- No actual secret values in artifact (H09 pass)
- sensitive_count: 2 matches actual sensitive vars in catalog (S06 pass)
- tldr: 73 chars <= 160 (S01 pass)
- tags: 5 items, includes "env_config" (S02 pass)
## Anti-Example
INPUT: "Create env config for database"
BAD OUTPUT:
```yaml
id: database-env
kind: environment
pillar: config
scope: db
variables: DATABASE_URL=postgresql://admin:password123@localhost/mydb
quality: 7.5
tags: [database]
```
Database configuration.
Set DATABASE_URL to your connection string.
FAILURES:
1. id: "database-env" uses hyphens and no `p09_env_` prefix -> H02 FAIL
2. kind: "environment" not "env_config" -> H04 FAIL
3. pillar: "config" not "P09" -> H06 FAIL
4. quality: 7.5 (not null) -> H05 FAIL
5. variables contains actual secret value (password123) -> H09 FAIL
6. Missing fields: version, created, updated, author, tldr -> H06 FAIL
7. tags: only 1 item, missing "env_config" -> S02 FAIL
8. Body missing ## Variable Catalog, ## Override Precedence, ## Sensitive Variables -> H07 FAIL
9. variables is string with value, not list of names -> H06 FAIL
10. No validation rules defined for any variable -> S05 FAIL
11. DATABASE_URL not marked as sensitive -> S06 FAIL
