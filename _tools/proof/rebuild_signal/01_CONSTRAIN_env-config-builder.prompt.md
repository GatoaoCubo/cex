# CEX Crew Runner -- Builder Execution
**Builder**: `env-config-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi signal-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:33:56.783520

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_env_config.md
---
id: env-config-builder
kind: type_builder
pillar: P09
parent: null
domain: env_config
llm_function: GOVERN
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, env-config, P09, config, environment, variables]
---

# env-config-builder
## Identity
Especialista em construir env_config artifacts — especificacoes de variaveis de ambiente
do sistema. Domina scoping (global, satellite, service), sensitive var handling, defaults,
validation rules, override precedence, e a boundary entre env_config (variaveis genericas)
e boot_config (P02, per-provider) ou feature_flag (P09, on/off logico). Produz env_config
artifacts com frontmatter completo e variable catalog documentado.
## Capabilities
- Definir variaveis de ambiente com scope, tipo, default, e sensibilidade
- Especificar validation rules para cada variavel (regex, range, enum)
- Documentar override precedence (env > file > default)
- Marcar variaveis sensitive (secrets, keys) com masking rules
- Validar artifact contra quality gates (8 HARD + 11 SOFT)
- Distinguir env_config de boot_config, feature_flag, path_config, permission
## Routing
keywords: [env, environment, variable, config, secret, dotenv, envvar, settings, configuration, sensitive]
triggers: "define environment variables", "create env config", "document system variables", "specify secrets and config"
## Crew Role
In a crew, I handle ENVIRONMENT VARIABLE SPECIFICATION.
I answer: "what environment variables does this scope need, with what defaults and validation?"
I do NOT handle: boot_config (per-provider startup), feature_flag (on/off toggle),
path_config (filesystem paths), permission (access control), runtime_rule (timeouts/retries).

### bld_instruction_env_config.md
---
kind: instruction
id: bld_instruction_env_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for env_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an env_config
## Phase 1: RESEARCH
1. Identify the scope: global (applies to all services), a named satellite, or a specific service
2. Catalog all environment variables needed within that scope — include name, current or example value, and purpose
3. Classify the type of each variable: string, integer, boolean, URL, or secret
4. Classify the sensitivity of each variable: public (safe to log), internal (omit from logs), or secret (mask in all output)
5. Determine validation rules per variable: regex pattern for strings, numeric range for integers, allowed values enum for controlled sets
6. Define default values and whether each variable is required or optional — optional variables must have a usable default
7. Define override precedence: environment variable wins over config file, which wins over default
8. Check existing env_configs via brain_query [IF MCP] for the same scope — do not duplicate a config that already covers this service
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Variable Catalog** section: table with columns name, type, scope, default, required/optional, sensitive flag
5. Write **Validation Rules** section: per variable — pattern or range, allowed values, error message on failure
6. Write **Override Precedence** section: explicit ordering (env > file > default) with scope inheritance rules
7. Write **Secrets Handling** section: masking rules for each secret variable, rotation policy, storage location (vault, platform secrets manager)
8. Write **Groups** section: logical groupings such as database, API keys, feature toggles, file paths
9. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p09_ev_[a-z][a-z0-9_]+$`
4. Confirm at least one variable is defined
5. Confirm all sensitive variables have masking rules in the Secrets Handling section
6. Confirm validation rules are present for at least the required variables
7. Confirm no actual secret values appear anywhere in the artifact — only placeholders or descriptions
8. Confirm `quality` is null
9. Confirm body <= 4096 bytes
10. Cross-check: are these generic runtime variables? If this is a startup script it belongs in `boot_config`. If these are on/off toggles they belong in `feature_flag`. If this is access control it belongs in `permission`. This artifact catalogs variables, it does not toggle features or control access.
11. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_env_config.md
---
kind: knowledge_card
id: bld_knowledge_card_env_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for env_config production — environment variable specification
sources: 12-Factor App (Factor III), dotenv conventions, Kubernetes ConfigMap/Secret, OWASP
---

# Domain Knowledge: env_config
## Executive Summary
Env configs define the variable contract for a system scope — every environment variable needed with its name, type, default, sensitivity level, and validation rule. Following 12-Factor App principle III (store config in environment, not code), env configs separate deployment-varying configuration from artifacts. They differ from boot configs (provider-specific), feature flags (on/off logic), and permissions (access control).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| llm_function | GOVERN |
| Frontmatter fields | 15+ |
| Quality gates | 8 HARD + 11 SOFT |
| Override precedence | env var > config file > default |
| Scope hierarchy | global > satellite > service |
| Naming | UPPER_SNAKE_CASE, optional prefix per scope |
## Patterns
- **Variable type system**: every variable has an explicit type with validation
| Type | Validation | Example |
|------|-----------|---------|
| string | regex or enum | LOG_LEVEL, DATABASE_URL |
| integer | min/max range | PORT, MAX_RETRIES |
| boolean | true/false only | DEBUG, FEATURE_ENABLED |
| url | URL format check | API_BASE_URL, WEBHOOK_URL |
| secret | non-empty, masked | API_KEY, JWT_SECRET |
- **Scope hierarchy**: narrower scope wins — service config overrides satellite, satellite overrides global
- **Sensitivity handling**: sensitive vars (secrets, keys) NEVER logged, NEVER committed, ALWAYS masked in output
- **Required vs optional**: required vars block startup if missing; optional vars use defaults
- **Naming convention**: UPPER_SNAKE_CASE with optional prefix (CEX_, researcher_) for scope clarity
| Source | Concept | Application |
|--------|---------|-------------|
| 12-Factor (III) | Config in environment | Separate config from code |
| dotenv | Local dev variables | .env as implementation of spec |
| K8s ConfigMap/Secret | Namespaced config | Non-sensitive vs sensitive split |
| AWS SSM | Hierarchical encrypted config | SecureString for sensitive vars |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Secrets in code/config files | Committed to git; exposed in logs |
| No validation rules | Invalid values cause runtime errors |
| Missing defaults for optional vars | Startup fails unnecessarily |
| No scope prefix | Variable collisions between services |
| Logging sensitive vars | Secrets appear in plaintext in logs |
| No type declaration | String "true" treated as truthy in some languages, not others |
## Application
1. Catalog variables: name, type, required/optional, default, description
2. Classify sensitivity: public (ConfigMap) vs sensitive (Secret)
3. Define validation: regex, range, enum per variable
4. Set scope: global, satellite, or service with appropriate prefix
5. Document precedence: env var > config file > default
6. Validate: required vars have no defaults; secrets are marked sensitive
## References
- 12factor.net/config: Factor III — Config in environment
- dotenv: local development variable convention
- OWASP: Secret Management Cheat Sheet
- Kubernetes: ConfigMap and Secret best practices

### bld_quality_gate_env_config.md
---
id: p11_qg_env_config
kind: quality_gate
pillar: P11
title: "Gate: env_config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "env_config — environment variable specifications with scope, validation rules, and sensitive var handling"
quality: null
tags: [quality-gate, env-config, environment-variables, secrets, configuration, P11]
tldr: "Gates for env_config artifacts: validates variable catalog completeness, sensitive masking, default correctness, override precedence, and scope accuracy."
density_score: 0.92
---

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
| Scope accuracy | 1.0 | Scope (global/satellite/service) correctly categorizes all variables |
| Type specificity | 0.5 | Types beyond string used where appropriate (int, bool, url, path) |
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

### bld_schema_env_config.md
---
kind: schema
id: bld_schema_env_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for env_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: env_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_env_{scope_slug}) | YES | - | Namespace compliance |
| kind | literal "env_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | Config scope: global, satellite name, or service name |
| variables | list[string], len >= 1 | YES | - | Variable names defined |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "env_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this config covers |
| environment | enum: development, staging, production, all | REC | all | Target environment |
| sensitive_count | integer | REC | - | Number of sensitive vars |
| override | string | REC | - | Override precedence summary |
| validation | string | REC | - | Validation strategy summary |
## ID Pattern
Regex: `^p09_env_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what scope, why these variables, who consumes them
2. `## Variable Catalog` — table: name, type, required, default, sensitive, validation
3. `## Override Precedence` — how values are resolved (env > file > default)
4. `## Sensitive Variables` — which vars are secrets, masking rules, storage guidance
## Constraints
- max_bytes: 4096 (body only — env configs can be larger)
- naming: p09_env_{scope_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- variables list MUST match variable names in ## Variable Catalog
- quality: null always
- NEVER include actual secret values — names and validation only

### bld_examples_env_config.md
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

### bld_architecture_env_config.md
---
kind: architecture
id: bld_architecture_env_config
pillar: P08
llm_function: GOVERN
purpose: Component map of env_config — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| scope | The system boundary this config covers: global, satellite, service | env-config-builder | required |
| variables | Catalog of env vars: name, type, default, description, sensitivity | env-config-builder | required |
| validation_rules | Per-variable constraints: regex, range, enum, required flag | env-config-builder | required |
| sensitive_vars | List of secret/key vars with masking rules (never log, never expose) | env-config-builder | required |
| override_precedence | Resolution order: runtime env > .env file > hardcoded default | env-config-builder | required |
| defaults | Default values applied when var is absent from environment | env-config-builder | required |
| required_vars | Variables that must be present for the system to start (startup gate) | env-config-builder | required |
| optional_vars | Variables that enable optional features when present | env-config-builder | optional |
| metadata | config id, version, pillar, scope, author, created date | env-config-builder | required |
## Dependency Graph
```
guardrail (P11) --constrains--> env_config (security rules for sensitive var handling)
env_config --consumed_by--> boot_config (P02) (boot reads env vars at provider startup)
env_config --consumed_by--> daemon (P04) (daemon reads vars for config at launch)
env_config --consumed_by--> connector (P04) (connector reads API keys, base URLs from env)
env_config --consumed_by--> client (P04) (client reads auth tokens, endpoints from env)
env_config --consumed_by--> mcp_server (P04) (MCP server reads transport config from env)
feature_flag (P09) --independent-- env_config (feature_flag is on/off toggle logic, not var spec)
path_config (P09) --independent-- env_config (path_config covers filesystem paths specifically)
runtime_rule (P09) --independent-- env_config (runtime_rule governs behavior like timeouts/retries)
```
| From | To | Type | Data |
|------|----|------|------|
| guardrail | env_config | constrains | security rules for masking and exposure of sensitive vars |
| env_config | boot_config | consumed_by | env vars read at provider startup |
| env_config | daemon | consumed_by | config vars, secret values, paths at launch |
| env_config | connector | consumed_by | API keys, base URLs, auth credentials |
| env_config | client | consumed_by | auth tokens, endpoint URLs, timeouts |
| env_config | mcp_server | consumed_by | transport config, port, auth mode |
## Boundary Table
| env_config IS | env_config IS NOT |
|--------------|-------------------|
| A specification of environment variables: names, types, defaults, validation | A boot_config (P02) — boot_config is per-provider model startup configuration |
| Covers any variable that changes between deployment environments | A feature_flag (P09) — feature_flag is an on/off logical toggle with rollout logic |
| Follows 12-Factor App principle: config lives in environment, not code | A path_config (P09) — path_config specifies filesystem paths specifically |
| Declares sensitivity level and masking rules for secrets | A permission (P09) — permission governs access control, not variable values |
| Specifies validation rules (regex, enum, range) per variable | A runtime_rule (P09) — runtime_rule governs behavioral limits like timeouts and retries |
| Defines override precedence: runtime > file > default | A knowledge_card (P01) — KC distills domain knowledge, not system configuration |
| Has required_vars that gate system startup if absent | A connector (P04) — connector defines integration spec; env_config feeds it values |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Safety | guardrail, sensitive_vars | Enforce masking rules and prevent secret exposure |

### bld_collaboration_env_config.md
---
kind: collaboration
id: bld_collaboration_env_config
pillar: P12
llm_function: COLLABORATE
purpose: How env-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: env-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what environment variables does this scope need, with what defaults and validation?"
I do not configure provider startup. I do not define feature toggles.
I specify environment variables so deployments have correct configuration and secrets.
## Crew Compositions
### Crew: "Deployment Configuration"
```
  1. boot-config-builder -> "provider startup configuration"
  2. env-config-builder -> "environment variables (secrets, settings, paths)"
  3. feature-flag-builder -> "feature toggles for gradual rollout"
```
### Crew: "Multi-Provider Deployment"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "config per provider"
  3. env-config-builder -> "env vars per deployment target"
  4. fallback-chain-builder -> "degradation per environment"
```
## Handoff Protocol
### I Receive
- seeds: scope (global, service, agent), variable list
- optional: sensitivity flags, validation rules, override precedence, defaults
### I Produce
- env_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P09/examples/p09_env_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- boot-config-builder: reveals which variables each provider needs
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| client-builder | API clients reference env vars for credentials |
| connector-builder | Connectors reference env vars for connection settings |
| daemon-builder | Background processes read env vars at startup |

### bld_config_env_config.md
---
kind: config
id: bld_config_env_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: env_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_env_{scope_slug}.yaml` | `p09_env_api_service.yaml` |
| Builder directory | kebab-case | `env-config-builder/` |
| Frontmatter fields | snake_case | `sensitive_count`, `override` |
| Scope slug | snake_case, lowercase, no hyphens | `api_service`, `global`, `shaka` |
| Variable names | UPPER_SNAKE_CASE | `DATABASE_URL`, `API_PORT` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_env_{scope_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_env_{scope_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80 (no filler)
## Environment Enum
| Value | When to use |
|-------|-------------|
| development | Local dev only variables |
| staging | Pre-production environment |
| production | Production environment |
| all | Variables needed in all environments (default) |
## Scope Conventions
| Scope | Prefix | Example |
|-------|--------|---------|
| global | CEX_ | CEX_LOG_LEVEL, CEX_DEBUG |
| satellite | {DOMAIN}_ | RESEARCHER_API_KEY, BUILDER_MODEL |
| service | {SERVICE}_ | API_PORT, API_CORS_ORIGINS |

### bld_memory_env_config.md
---
id: p10_lr_env_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Environment configs that omit sensitivity markers for API keys and database URLs cause secrets to be logged, committed to version control, or exposed in health-check endpoints. Variables without type declarations cause silent type coercion failures when a service reads '8080' as a string and passes it where an integer is required. Missing override precedence documentation causes operators to set the wrong scope when troubleshooting, leaving environment-specific overrides silently ignored. Variables in lowercase are routinely skipped by environment-reading code that only scans UPPER_SNAKE_CASE names."
pattern: "Specify each variable with five fields: (1) name in UPPER_SNAKE_CASE; (2) type (string, integer, boolean, url, path); (3) default value or null if required; (4) sensitive: true/false; (5) validation rule (regex, range, enum). Include an explicit ## Sensitive Variables section even when empty. Document override precedence order (e.g., process env > .env.local > .env > defaults)."
evidence: "Configs with sensitivity markers prevented secret exposure in 3 of 3 log-audit reviews. Explicit type declarations caught 6 silent coercion bugs during code review that would have reached production. Documented override precedence reduced operator troubleshooting time by ~45% in 4 incident postmortems. UPPER_SNAKE_CASE enforcement eliminated 100% of variable-not-found errors in tested services."
confidence: 0.75
outcome: SUCCESS
domain: env_config
tags:
  - env-config
  - environment-variables
  - secrets-management
  - type-validation
  - sensitivity-marking
  - override-precedence
  - configuration-management
tldr: "UPPER_SNAKE_CASE names, explicit types and sensitivity markers, document override precedence, never include actual secret values."
impact_score: 7.5
decay_rate: 0.04
satellite: edison
keywords:
  - environment variables
  - env config
  - secrets
  - sensitivity
  - type validation
  - override precedence
  - UPPER_SNAKE_CASE
  - defaults
---

## Summary
Environment configuration failures fall into two categories: security failures (secrets exposed because sensitivity was not marked) and reliability failures (services crash on startup because types are wrong or required variables are missing). A five-field variable specification and explicit sensitivity section address both categories systematically.
## Pattern
**Variable specification**: each variable requires five fields. Name in UPPER_SNAKE_CASE. Type from the set {string, integer, boolean, url, path, enum}. Default value (or null if the variable is required with no default). Sensitive flag (true marks the value for redaction in logs and outputs). Validation rule that can be evaluated at startup (regex pattern, numeric range, or enum list).
**Sensitivity section**: include `## Sensitive Variables` in every env config body, even when no sensitive variables exist - write "none" in that case. This makes it impossible to skip the review step when auditing a config.
**Override precedence**: document the lookup order explicitly (e.g., process environment > `.env.local` > `.env` > compiled defaults). Without this, operators set variables at the wrong scope and spend hours troubleshooting why their change has no effect.
**Scope specificity**: use the narrowest accurate scope slug. "api_service" is better than "system" because it limits which processes load the config. Common validated scopes: global (applies everywhere), api_service, satellite (one background worker type), worker (queue consumer).
**Never include actual values**: the artifact describes the shape and constraints of configuration, not the values themselves. Actual secrets belong in a secrets manager, not in any committed file.
## Anti-Pattern
- Variable names in lowercase - environment-reading code conventionally skips lowercase names.
- Omitting the `## Sensitive Variables` section - auditors cannot confirm the review was done.


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `env-config-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
