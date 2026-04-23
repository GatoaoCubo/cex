---
kind: quality_gate
id: p11_qg_env_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of env_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: env_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, env-config, environment-variables, secrets, configuration, P11]
tldr: "Gates for env_config artifacts: validates variable catalog completeness, sensitive masking, default correctness, override precedence, and scope accuracy."
domain: "env_config — environment variable specifications with scope, validation rules, and sensitive var handling"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.92
related:
  - bld_examples_env_config
  - p03_sp_env_config_builder
  - env-config-builder
  - bld_instruction_env_config
  - bld_knowledge_card_env_config
  - bld_schema_env_config
  - bld_examples_kind
  - p11_qg_prompt_template
  - p10_lr_env_config_builder
  - p11_qg_dispatch_rule
---

## Quality Gate

# Gate: env_config
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: env_config` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p09_env_[a-z][a-z0-9_]+$` | "ID fails env_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"env_config"` | "Kind is not 'env_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, scope, variables, override_precedence, version, created, author, tags | "Missing required field(s)" |
| H07 | No variable has a non-null default AND `sensitive: true` simultaneously (secrets must not have hardcoded defaults) | "Sensitive variable has hardcoded default — security violation" |
| H08 | `variables` list is non-empty (>= 1 variable defined) | "Variable catalog is empty" |
| H09 | Each variable entry contains: name, type, required, sensitive | "Variable entry missing required subfields" |
| H10 | `override_precedence` list present and contains at least: env, file, default in some order | "Override precedence chain incomplete" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Validation rules completeness | 1.0 | Each variable has regex, enum, or range validation defined |
| Sensitive variable masking | 1.0 | All sensitive vars have masking_rule (partial/full redaction) specified |
| Default value quality | 1.0 | Non-sensitive defaults are safe, functional, and documented |
| Scope accuracy | 1.0 | Scope (global/agent_group/service) correctly categorizes all variables |
| Type specificity | 0.5 | Types beyond string used where apownte (int, bool, url, path) |
| Boundary clarity | 0.5 | Explicitly not boot_config (provider startup), feature_flag (toggle), path_config |
| Variable naming convention | 1.0 | All names follow UPPER_SNAKE_CASE, no ambiguous abbreviations |
| Required vs optional clarity | 1.0 | Required field accurate; optional vars have meaningful defaults |
| Override precedence rationale | 0.5 | Precedence order (env > file > default) explained or justified |
| Change impact documented | 1.0 | Notes which services/components depend on each variable |
| Secret rotation guidance | 1.0 | Sensitive vars include rotation frequency or process reference |
| Documentation | 0.5 | tldr names the scope and number of variables cataloged |
Weight sum: 1.0+1.0+1.0+1.0+0.5+0.5+1.0+1.0+0.5+1.0+1.0+0.5 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | New service bootstrapping where full variable catalog is not yet known |
| approver | Security/infra owner approval required (written); sensitive vars never bypassed |

## Examples

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
author: "builder_agent"
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
quality: 8.9
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
