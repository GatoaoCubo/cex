---
id: p06_security_validation_schema
kind: validator
8f: F7_govern
pillar: P06
title: Security Validation Schema
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: security-operations
quality: 9.0
tags: [validator, security, operations, N05, schema, validation]
tldr: "Security validation schema defining rules for secret detection, auth verification, input sanitization, and dependency auditing across the CEX codebase."
density_score: 0.96
related:
  - extraction_gate_severity
  - p07_red_team_eval_operations
  - bld_knowledge_card_guardrail
  - p10_lr_guardrail_builder
  - p12_wf_auto_security
  - p05_rf_security_audit
  - p11_qg_guardrail
  - p11_qg_security
  - p03_sp_guardrail_builder
  - bld_output_template_guardrail
---

# Security Validation Schema

## Overview

This schema defines validation rules for security-sensitive operations
across the CEX codebase. Every commit, every deploy, every code review
checks against these rules. Security is not a feature — it's a constraint.

## Validation Rules

### Secret Detection

```yaml
secret_detection:
  scope: "**/*.py, **/*.yaml, **/*.md, **/*.json, **/*.env"
  exclude: "**/*.env.example, **/test_*, **/mock_*"
  patterns:
    - name: api_key_literal
      regex: '(?i)(api[_-]?key|apikey)\s*[=:]\s*["\x27][a-zA-Z0-9]{20,}["\x27]'
      severity: critical
      action: block_commit
    - name: password_literal
      regex: '(?i)(password|passwd|pwd)\s*[=:]\s*["\x27][^\s]{8,}["\x27]'
      severity: critical
      action: block_commit
    - name: database_url_hardcoded
      regex: 'postgres(ql)?://[a-zA-Z0-9]+:[^@]+@'
      severity: critical
      action: block_commit
    - name: jwt_secret_literal
      regex: '(?i)(jwt[_-]?secret|secret[_-]?key)\s*[=:]\s*["\x27][^\s]{16,}["\x27]'
      severity: critical
      action: block_commit
    - name: private_key_block
      regex: '-----BEGIN (RSA |EC |DSA )?PRIVATE KEY-----'
      severity: critical
      action: block_commit
  remediation: "Move to environment variable. Reference via os.environ['KEY_NAME']."
```

### Auth Verification

```yaml
auth_verification:
  scope: "**/routers/*.py, **/endpoints/*.py"
  rules:
    - name: protected_endpoint_has_auth
      description: "All non-public endpoints must have auth dependency"
      check: "Depends(get_current_user) or Depends(verify_api_key)"
      exceptions: ["/health", "/docs", "/openapi.json", "/pipeline/health"]
      severity: critical
    - name: role_validation_server_side
      description: "Role checks use server-side user object, not client-sent role"
      check: "current_user.role, not request.body.role"
      severity: critical
    - name: tenant_isolation
      description: "Multi-tenant queries filter by tenant_id from auth context"
      check: "WHERE tenant_id = $tenant_id from auth, not from request"
      severity: critical
```

### Input Sanitization

```yaml
input_sanitization:
  scope: "**/models/*.py, **/schemas/*.py"
  rules:
    - name: pydantic_validation
      description: "All request bodies use Pydantic models with field validators"
      check: "BaseModel subclass with Field() constraints"
      severity: high
    - name: string_length_limits
      description: "All string fields have max_length constraint"
      check: "Field(max_length=N) or constr(max_length=N)"
      severity: high
    - name: sql_parameterized
      description: "All SQL queries use parameterized placeholders"
      check: "$1, $2 syntax, no f-string or .format() in SQL"
      severity: critical
    - name: path_traversal_prevention
      description: "File paths are validated against allowed directories"
      check: "os.path.realpath() + startswith(allowed_dir)"
      severity: critical
```

### Dependency Audit

```yaml
dependency_audit:
  tool: "pip-audit or safety"
  frequency: "every PR, weekly scheduled"
  rules:
    - name: no_critical_cves
      description: "No dependencies with critical CVE"
      severity: critical
      action: block_merge
    - name: no_high_cves
      description: "No dependencies with high CVE"
      severity: high
      action: warning
    - name: pinned_versions
      description: "All dependencies have pinned versions in requirements.txt"
      severity: high
      action: warning
    - name: no_unused_deps
      description: "No installed packages not imported in source"
      severity: low
      action: suggestion
```

## Integration Points

| integration | trigger | action |
|-------------|---------|--------|
| Pre-commit hook | `git commit` | Run secret detection on staged files |
| PR check | Pull request opened | Full security validation scan |
| Deploy gate | Before `railway up` | Auth + input + dependency audit |
| Scheduled | Weekly (Sunday 02:00) | Full dependency CVE scan |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[extraction_gate_severity]] | related | 0.27 |
| [[p07_red_team_eval_operations]] | downstream | 0.27 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.25 |
| [[p10_lr_guardrail_builder]] | downstream | 0.25 |
| [[p12_wf_auto_security]] | downstream | 0.22 |
| [[p05_rf_security_audit]] | upstream | 0.22 |
| [[p11_qg_guardrail]] | downstream | 0.21 |
| [[p11_qg_security]] | downstream | 0.21 |
| [[p03_sp_guardrail_builder]] | upstream | 0.20 |
| [[bld_output_template_guardrail]] | upstream | 0.20 |
