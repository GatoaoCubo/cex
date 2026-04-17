---
id: p06_vs_payload
kind: validation_schema
pillar: P06
title: "Validation Schema: Operations Payload"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "validation-schema-builder"
target_kind: "operational_payload"
format: "yaml"
fields_count: 22
on_failure: "reject"
strict: false
domain: "operations-payload"
quality: null
tags: [validation-schema, operations, payload, N05, P06, contract]
tldr: "Post-generation contract for all N05 operational payloads: frontmatter, signal, handoff, config, compile output, and git commit messages."
coercion: true
error_template: "Payload validation [{scope}]: {field} failed -- {reason}"
density_score: 0.92
linked_artifacts:
  primary: "N05_operations/P06_schema/security_validation_schema.md"
  related: ["N05_operations/P06_schema/api_response_contract.md", "N00_genesis/P06_schema/_schema.yaml"]
---

## Schema Overview

Five scopes: frontmatter (artifact integrity), signal (nucleus events),
handoff (dispatch contracts), config (runtime settings), compile + git.
Applied AFTER LLM generation, BEFORE execution. LLM never sees this.

## Fields -- Frontmatter (HARD)

| Field | Type | Required | Constraints | Error |
|-------|------|----------|-------------|-------|
| id | string | yes | `^p[0-9]{2}_[a-z][a-z0-9_]+$` | id must match pillar-prefixed snake_case |
| kind | string | yes | enum: [registered CEX kinds] | kind must be a registered CEX kind |
| pillar | string | yes | `^P(0[1-9]\|1[0-2])$` | pillar must be P01-P12 |
| version | string | yes | `^\d+\.\d+\.\d+$` | version must be valid semver |
| quality | null | yes | eq: null | quality must be null -- never self-score |

## Fields -- Signal (HARD)

| Field | Type | Required | Constraints | Error |
|-------|------|----------|-------------|-------|
| nucleus_id | string | yes | `^n0[1-7]$` | nucleus_id must be n01-n07 |
| event_type | string | yes | enum: [complete, error, timeout] | event_type must be complete/error/timeout |
| score | number | yes | min: 0.0, max: 10.0 | score must be in range 0.0-10.0 |

## Fields -- Handoff (HARD + SOFT)

| Field | Type | Required | Constraints | Error |
|-------|------|----------|-------------|-------|
| mission | string | yes | min: 3, max: 128 chars | mission must be 3-128 chars |
| nucleus | string | yes | `^n0[1-7]$` | nucleus must be n01-n07 |
| wave | integer | yes | min: 1 | wave must be >= 1 |
| priority | string | no | enum: [low, normal, high, critical] | priority must be low/normal/high/critical |
| effort | string | no | enum: [S, M, L, XL] | effort must be S/M/L/XL |

## Fields -- Config (HARD)

| Field | Type | Required | Constraints | Error |
|-------|------|----------|-------------|-------|
| env_config.env | string | yes | enum: [development, staging, production] | env must be dev/staging/prod |
| rate_limit.requests_per_minute | integer | yes | min: 1, max: 10000 | rpm must be 1-10000 |
| secret_config.provider | string | yes | enum: [env, vault, railway] | provider must be env/vault/railway |

## Fields -- Compile + Git (HARD)

| Field | Type | Required | Constraints | Error |
|-------|------|----------|-------------|-------|
| compile.output_format | string | yes | enum: [yaml, json] | compile output must be yaml or json |
| compile.valid_yaml | boolean | yes | eq: true | compiled output must parse as valid YAML |
| git.commit_message | string | yes | `^\[N0[0-7]\]` | commit message must start with [N0X] prefix |
| git.staged_files | array | yes | min_length: 1 | at least 1 file must be staged |

## Failure Handling

| Scope | on_failure | Coerce | Remediation |
|-------|-----------|--------|-------------|
| frontmatter.id | reject | no | Fix id to `^p[0-9]{2}_` prefix |
| frontmatter.quality | reject | auto_fix: null | Set quality: null |
| signal.nucleus_id | reject | auto_fix: lower | Normalize to n0X |
| signal.score | reject | auto_fix: clamp | Clamp to [0.0, 10.0] |
| handoff.priority | warn | auto_fix: normal | Default "normal" if absent |
| config.env | reject | no | Declare environment explicitly |
| git.commit_message | reject | no | Prefix with [N0X] |

## Integration

| Stage | Trigger | Applied by | Output |
|-------|---------|-----------|--------|
| post_generation | After LLM call | cex_compile.py | Validated artifact or rejection |
| pre_commit | git pre-commit hook | cex_hooks.py | Pass or block commit |
| on_dispatch | Handoff written | dispatch.sh | Proceed or abort dispatch |

## References

1. `N05_operations/P06_schema/security_validation_schema.md` -- security gate contract
2. `N00_genesis/P06_schema/_schema.yaml` -- P06 pillar schema definitions
3. `.claude/rules/8f-reasoning.md` -- F7 GOVERN gate definitions
4. `_tools/cex_compile.py` -- compile output validation reference
