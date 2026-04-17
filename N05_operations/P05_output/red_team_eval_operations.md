---
id: p07_red_team_eval_operations
kind: red_team_eval
pillar: P07
title: Operations Red Team Evaluation Suite
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: security-operations
quality: 9.0
tags: [red_team_eval, security, operations, N05, adversarial, penetration]
tldr: "Red team evaluation suite covering prompt injection, auth bypass, input fuzzing, rate limit evasion, env leakage, and error exploitation."
density_score: 0.96
---

# Operations Red Team Evaluation Suite

## Overview

This red team eval suite defines adversarial test scenarios for the CEX
backend infrastructure. Each scenario attempts to break security, bypass
controls, or exploit edge cases. Passing this eval means the system
withstands intentional attack vectors.

## Attack Categories

### 1. Prompt Injection

| test_id | attack | expected_defense | severity |
|---------|--------|------------------|----------|
| RT_PI01 | Inject system prompt override in user input | Input sanitized, injection ignored | critical |
| RT_PI02 | Chain prompt injection across multi-turn | Context isolation prevents leakage | critical |
| RT_PI03 | Encode injection in base64/unicode to bypass filters | Decoded and sanitized before processing | high |
| RT_PI04 | Inject via JSON field values in API request | Pydantic validation rejects malformed input | high |

### 2. Authentication Bypass

| test_id | attack | expected_defense | severity |
|---------|--------|------------------|----------|
| RT_AUTH01 | Expired token reuse | Token validation rejects expired JWT | critical |
| RT_AUTH02 | Missing auth header on protected endpoint | 401 returned, no data leakage | critical |
| RT_AUTH03 | Privilege escalation via role parameter injection | Server-side role validation, ignore client role | critical |
| RT_AUTH04 | API key from different tenant used cross-tenant | Tenant isolation enforced, 403 returned | critical |

### 3. Input Fuzzing

| test_id | attack | expected_defense | severity |
|---------|--------|------------------|----------|
| RT_FUZZ01 | Extremely long string input (100KB+) | Body size limit middleware rejects | high |
| RT_FUZZ02 | Null bytes in string fields | Input sanitization strips null bytes | high |
| RT_FUZZ03 | SQL injection via search parameter | Parameterized queries prevent injection | critical |
| RT_FUZZ04 | Path traversal in file upload name | Filename sanitization, no filesystem access | critical |
| RT_FUZZ05 | Unicode normalization attacks | Consistent normalization before processing | medium |

### 4. Rate Limit Evasion

| test_id | attack | expected_defense | severity |
|---------|--------|------------------|----------|
| RT_RL01 | Rapid-fire requests exceeding tier limit | 429 returned after limit, headers accurate | high |
| RT_RL02 | Distributed requests from multiple IPs | Tenant-level rate limiting (not just IP) | high |
| RT_RL03 | Slow drip to stay just under rate limit | Sliding window detects sustained abuse | medium |

### 5. Environment Leakage

| test_id | attack | expected_defense | severity |
|---------|--------|------------------|----------|
| RT_ENV01 | Trigger error to expose stack trace | Production error handler returns generic message | critical |
| RT_ENV02 | Access debug endpoints in production | Debug routes disabled in production | critical |
| RT_ENV03 | Inspect response headers for version info | Server header stripped or generic | medium |
| RT_ENV04 | Access /docs endpoint to map full API surface | Docs disabled in production or auth-gated | medium |

### 6. Resource Exhaustion

| test_id | attack | expected_defense | severity |
|---------|--------|------------------|----------|
| RT_RES01 | Open many connections without closing | Connection pool max enforced, cleanup timeout | high |
| RT_RES02 | Send large payloads to exhaust memory | Body size limit middleware rejects | high |
| RT_RES03 | Trigger expensive queries repeatedly | Query timeout + rate limiting | high |

## Execution Protocol

1. **Isolation**: Run against staging environment, never production
2. **Authorization**: Red team eval requires explicit authorization from repo owner
3. **Logging**: All attack attempts are logged with full request/response capture
4. **Evidence**: Pass/fail per test with actual response evidence
5. **Remediation**: Failed tests generate immediate security tickets

## Scoring

| result | meaning |
|--------|---------|
| All critical pass | Minimum security bar met |
| All high pass | Good security posture |
| All pass | Excellent — publish as security exemplar |
| Any critical fail | Deploy blocked until fixed |

## Report Format

```markdown
## Red Team Report: {date}

### Status: {PASS | PARTIAL | FAIL}

| Category | Tests | Pass | Fail | Critical Fails |
|----------|-------|------|------|----------------|

### Failed Tests
- {test_id}: {description} — {actual_response} — {remediation}

### Recommendations
- {priority-ordered security improvements}
```
