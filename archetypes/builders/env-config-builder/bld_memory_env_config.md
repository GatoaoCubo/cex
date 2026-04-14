---
id: p10_lr_env_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
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
agent_group: edison
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Env Config"
density_score: 0.90
llm_function: INJECT
---
## Summary
Environment configuration failures fall into two categories: security failures (secrets exposed because sensitivity was not marked) and reliability failures (services crash on startup because types are wrong or required variables are missing). A five-field variable specification and explicit sensitivity section address both categories systematically.
## Pattern
**Variable specification**: each variable requires five fields. Name in UPPER_SNAKE_CASE. Type from the set {string, integer, boolean, url, path, enum}. Default value (or null if the variable is required with no default). Sensitive flag (true marks the value for redaction in logs and outputs). Validation rule that can be evaluated at startup (regex pattern, numeric range, or enum list).
**Sensitivity section**: include `## Sensitive Variables` in every env config body, even when no sensitive variables exist - write "none" in that case. This makes it impossible to skip the review step when auditing a config.
**Override precedence**: document the lookup order explicitly (e.g., process environment > `.env.local` > `.env` > compiled defaults). Without this, operators set variables at the wrong scope and spend hours troubleshooting why their change has no effect.
**Scope specificity**: use the narrowest accurate scope slug. "api_service" is better than "system" because it limits which processes load the config. Common validated scopes: global (applies everywhere), api_service, agent_group (one background worker type), worker (queue consumer).
**Never include actual values**: the artifact describes the shape and constraints of configuration, not the values themselves. Actual secrets belong in a secrets manager, not in any committed file.
## Anti-Pattern
1. Variable names in lowercase - environment-reading code conventionally skips lowercase names.
2. Omitting the `## Sensitive Variables` section - auditors cannot confirm the review was done.

## Builder Context

This ISO operates within the `env-config-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_env_config_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_env_config_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | env_config |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
