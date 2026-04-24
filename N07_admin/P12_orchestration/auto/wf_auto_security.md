---
id: p12_wf_auto_security
kind: workflow
8f: F8_collaborate
pillar: P12
title: "Auto-Security — Scan before production"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: before_production
quality: 9.1
tags: [workflow, auto, n07, security, owasp, vapt, scan]
tldr: "Security scan before any production deploy: secrets leak, dependency audit, env validation, prompt injection check."
density_score: 0.91
updated: 2026-04-07
related:
  - p12_wf_auto_health
  - p12_wf_auto_review
  - p12_wf_auto_ship
  - p12_wf_auto_hydrate
  - p12_wf_auto_rollback
  - p12_wf_auto_research
  - p06_security_validation_schema
  - self_audit_newpc
  - p01_fse_meta_builder_recipe
  - p03_ins_doing_tasks
---

# Auto-Security

## Trigger
Before any external deploy (Railway, Vercel, production push), or before publishing artifacts.

## Industry Pattern
OWASP VAPT (Vulnerability Assessment and Penetration Testing). Security gate in CI/CD.

## Checks

| # | Check | What | Tool | Severity |
|---|-------|------|------|----------|
| 1 | Secrets scan | No API keys, passwords, tokens in code | `grep -r "sk-\|STRIPE_SECRET\|password=" --include="*.py" --include="*.md"` | CRITICAL |
| 2 | Env validation | `.env` not committed, `.env.example` exists | `git ls-files .env` | HIGH |
| 3 | Dependency audit | No known vulnerabilities | `pip audit` or `npm audit` | MEDIUM |
| 4 | MCP config check | No real credentials in `.mcp-*.json` | Check for `${VAR}` pattern | HIGH |
| 5 | Brand data check | No PII in brand_config.yaml committed | Check for CPF, email, phone | MEDIUM |
| 6 | Prompt injection | No unescaped user input in system prompts | Scan `prompts/` for `{user_input}` without sanitization | HIGH |
| 7 | Git history check | No secrets in previous commits | `git log --diff-filter=A --name-only` | LOW |

## Verdicts

| Result | Action |
|--------|--------|
| All clear | Proceed with deploy |
| MEDIUM issues | Warn, proceed if user confirms |
| HIGH issues | Block deploy, show issues, suggest fix |
| CRITICAL (secrets) | Block deploy, suggest `git filter-branch` or BFG |

## Failure Mode
Security scan tool unavailable → warn user, proceed with manual checklist.


## Operational Constraints

This automated workflow operates under strict resource and safety boundaries:

- **Budget cap**: maximum token expenditure per execution enforced via runtime counter
- **Idempotency**: re-running the workflow produces no side effects if previous run succeeded
- **Rollback safe**: every state change creates a checkpoint enabling full reversal
- **Audit logged**: execution start, each step completion, and final status written to log

### Execution Trace

```yaml
# Workflow execution record
trace:
  workflow: wf_auto_security
  started: 2026-04-07T15:00:00
  status: completed
  steps_total: 4
  steps_passed: 4
  duration_seconds: 45
  token_usage: 12000
  artifacts_modified: 3
```

| Phase | Action | Gate |
|-------|--------|------|
| Pre-check | Validate inputs and prerequisites | Abort on missing dependency |
| Execute | Run core workflow logic | Monitor for errors |
| Post-check | Verify outputs meet quality threshold | Flag regressions |
| Cleanup | Archive temp files, update signals | Always runs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_health]] | sibling | 0.53 |
| [[p12_wf_auto_review]] | sibling | 0.48 |
| [[p12_wf_auto_ship]] | sibling | 0.41 |
| [[p12_wf_auto_hydrate]] | sibling | 0.39 |
| [[p12_wf_auto_rollback]] | sibling | 0.37 |
| [[p12_wf_auto_research]] | sibling | 0.34 |
| [[p06_security_validation_schema]] | upstream | 0.25 |
| [[self_audit_newpc]] | upstream | 0.24 |
| [[p01_fse_meta_builder_recipe]] | upstream | 0.23 |
| [[p03_ins_doing_tasks]] | upstream | 0.23 |
