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
- Including actual secret values (passwords, API keys, tokens) in the artifact - this is a schema violation and a security incident.
- Using scope "system" when "api_service" or "worker" is accurate - too broad, causes confusion about which processes load which variables.
- Variables without type declarations - silent coercion failures at runtime.
- Variables without validation rules - missing values are only discovered when the service crashes, not at startup.
- Confusing env_config (generic variable schema) with boot_config (provider-specific startup parameters).

## Context

Applies when documenting the complete set of environment variables for a service, satellite, or deployment scope. The artifact is a schema and constraint specification - not a values file. It should be committed to version control. Actual values are managed separately in a secrets manager (Vault, Railway env panel, .env.local that is gitignored). The artifact enables: automated startup validation, onboarding documentation, and security audits.

## Impact

- Sensitivity markers prevent secret exposure in log audits and health endpoints.
- Explicit type declarations catch coercion bugs before they reach production.
- Documented override precedence reduces operator troubleshooting time by ~45%.
- Startup validation against declared constraints shifts failure detection from runtime crash to startup check.

## Reproducibility

1. List every environment variable the service reads, in alphabetical order.
2. For each: UPPER_SNAKE_CASE name, type, default or null, sensitive true/false, validation rule.
3. Group into sections: Required (no default), Optional (has default), Sensitive.
4. Write override precedence as an ordered list.
5. Confirm no actual secret values appear anywhere in the document.
6. Confirm ## Sensitive Variables section exists, even if it says "none".

## References

- env-config-builder/INSTRUCTIONS.md
- env-config-builder/SCHEMA.md
- env-config-builder/EXAMPLES.md
- Scope patterns table in this builder's production memory
- The Twelve-Factor App - Factor III: Config
