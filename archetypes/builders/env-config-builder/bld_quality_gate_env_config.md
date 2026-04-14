---
id: p11_qg_env_config
kind: quality_gate
pillar: P11
title: "Gate: env_config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "env_config — environment variable specifications with scope, validation rules, and sensitive var handling"
quality: 9.0
tags: [quality-gate, env-config, environment-variables, secrets, configuration, P11]
tldr: "Gates for env_config artifacts: validates variable catalog completeness, sensitive masking, default correctness, override precedence, and scope accuracy."
density_score: 0.92
llm_function: GOVERN
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
