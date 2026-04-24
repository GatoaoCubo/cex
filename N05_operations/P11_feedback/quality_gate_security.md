---
id: p11_qg_security
kind: quality_gate
8f: F7_govern
pillar: P11
title: "Gate: Security Validation"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: security-operations
quality: 8.9
tags: [quality_gate, security, operations, N05, red-team, auth]
tldr: "Security validation gate covering secret management, auth flows, input sanitization, dependency vulnerabilities, and adversarial resilience."
density_score: 0.98
related:
  - p11_qg_artifact
  - p11_qg_railway_superintendent
  - p11_qg_performance
  - p11_gr_cyber_risk
  - bld_examples_env_config
  - p06_security_validation_schema
  - p07_red_team_eval_operations
  - p12_wf_auto_security
  - p01_kc_secret_config
  - kc_env_config
---

## Definition

| Property | Value |
|----------|-------|
| Metric | security_validation_score |
| Threshold | 0.95 |
| Operator | >= |
| Scope | All code changes touching auth, secrets, env vars, API endpoints, user input handling |

## Hard Gates

| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| SEC01 | No hardcoded secrets, API keys, or credentials in source code | 0 violations | true |
| SEC02 | Environment variables for all secrets, validated via env contract | 100% | true |
| SEC03 | Authentication middleware present and ordered correctly in stack | correct order | true |
| SEC04 | Input sanitization on all user-facing endpoints | 100% coverage | true |
| SEC05 | SQL injection prevention via parameterized queries (no string concat) | 0 violations | true |
| SEC06 | CORS origins explicitly whitelisted (no wildcard in production) | explicit list | true |
| SEC07 | Rate limiting active with appropriate thresholds per tier | headers present | true |
| SEC08 | Dependency vulnerability scan passes (no critical/high CVEs) | 0 critical | true |
| SEC09 | SSL/TLS enforced on all external connections (DATABASE_URL, APIs) | 100% | true |
| SEC10 | Error responses do not leak internal paths, stack traces, or versions | 0 leaks | true |

## Validation Criteria

- **SEC01**: `rg -i "api_key|secret|password|token" --glob "*.py" --glob "!*.env*"` returns no hardcoded values
- **SEC02**: All sensitive values reference `os.environ` or `.env` files, validated by env contract schema
- **SEC03**: Middleware stack has APIKeyMiddleware before business logic, after CORS
- **SEC04**: Pydantic models or explicit validators on all POST/PUT/PATCH endpoints
- **SEC05**: All database queries use asyncpg parameterized syntax `$1, $2` — no f-strings in SQL
- **SEC06**: CORS `allow_origins` is an explicit list, not `["*"]` in production config
- **SEC07**: X-RateLimit-Limit/Remaining/Reset headers present on responses
- **SEC08**: `pip audit` or `safety check` reports zero critical/high vulnerabilities
- **SEC09**: DATABASE_URL uses `sslmode=require`, external API calls use HTTPS
- **SEC10**: Production error handler returns generic messages, debug mode is off

## Soft Gates

| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| SS01 | Principle of least privilege in auth scopes | 0.10 | 0.25 |
| SS02 | Secret rotation readiness (no hardcoded expiry assumptions) | 0.10 | 0.20 |
| SS03 | Adversarial input resilience (fuzzing, boundary values) | 0.10 | 0.20 |
| SS04 | Audit trail for security-sensitive operations | 0.10 | 0.20 |
| SS05 | Documentation of security assumptions and threat model | 0.10 | 0.15 |

## Scoring Formula

`security_score = (SS01 * 0.25) + (SS02 * 0.20) + (SS03 * 0.20) + (SS04 * 0.20) + (SS05 * 0.15)`

Pass condition: all hard gates pass AND `security_score >= 0.90`

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as security exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Security review required |
| < 7.0  | REJECT | Security rework mandatory |

## Boundary

Barreira de qualidade com score numerico. NAO eh validator (P06, tecnico pass/fail) nem scoring_rubric (P07, define criterios).


## 8F Pipeline Function

Primary function: **GOVERN**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_artifact]] | sibling | 0.35 |
| [[p11_qg_railway_superintendent]] | sibling | 0.34 |
| [[p11_qg_performance]] | sibling | 0.28 |
| [[p11_gr_cyber_risk]] | related | 0.23 |
| [[bld_examples_env_config]] | upstream | 0.23 |
| [[p06_security_validation_schema]] | upstream | 0.23 |
| [[p07_red_team_eval_operations]] | upstream | 0.23 |
| [[p12_wf_auto_security]] | downstream | 0.23 |
| [[p01_kc_secret_config]] | upstream | 0.22 |
| [[kc_env_config]] | upstream | 0.22 |
