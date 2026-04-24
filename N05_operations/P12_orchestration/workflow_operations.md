---
id: p12_wf_railway_superintendent
kind: workflow
8f: F8_collaborate
pillar: P12
version: 5.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
title: "Railway Backend Superintendent — Deploy Pipeline Workflow"
steps_count: 10
execution_mode: sequential_railway_deployment
error_recovery: rollback_then_checkpoint_then_escalate
max_retries: 2
timeout_ms: 7200000
spawn_delay_ms: 2000
quality: 9.0
tags: [workflow, railway, superintendent, deploy, fastapi, postgresql, rollback]
tldr: "10-step deploy pipeline: validate_toml → env → migrations → health_local → rollback_plan → railway_up → health_prod → pipeline → monitor → signal."
density_score: 0.97
agent_groups: [railway_superintendent]
signals: [toml_verified, env_validated, migrations_safe, health_local_ok, rollback_ready, deploy_complete, health_prod_ok, pipeline_ok, monitoring_active, deploy_signaled]
spawn_configs: [spawn_config_operations]
domain: railway-backend-operations
related:
  - p02_agent_deploy_ops
  - p02_agent_railway_superintendent
  - p08_ac_railway_superintendent
  - p12_wf_builder_8f_pipeline
  - p03_sp_railway_superintendent
  - p03_sp_deploy_ops
  - p05_output_deploy_checklist
  - p01_kc_deploy_paas
  - spec_n05_part2
  - KC_N05_ZERO_DOWNTIME_DEPLOY
---

# Railway Deployment Workflow

## Overview
10-step sequential deploy pipeline. On failure at any step: execute rollback plan.
Every step produces a signal. Checkpoint saved after each step for resume.

---

## Deploy Pipeline

```
validate_toml → validate_env → validate_migrations → health_local
     → create_rollback_plan → railway_up → verify_health_prod < 30s
     → verify_pipeline → monitor_logs_60s → signal_complete
```

### Step 1: validate_toml
```yaml
action: "Validate railway.toml against schema"
schema: "N05_operations/P06_schema/railway_toml_schema.md"
checks:
  - "[deploy].startCommand contains --host 0.0.0.0"
  - "[deploy].startCommand contains $PORT"
  - "[deploy].healthcheckPath is set"
  - "[deploy].restartPolicyType is ON_FAILURE"
signal: toml_verified
on_fail: ABORT ("Fix railway.toml before deploy")
```

### Step 2: validate_env
```yaml
action: "Validate environment variables against contract"
schema: "N05_operations/P06_schema/env_contract_schema.md"
checks:
  - "5 REQUIRED vars present (DATABASE_URL, PORT, ENV, SECRET_KEY, APP_URL)"
  - "63 total vars categorized (required/optional/mock)"
  - "No secrets in railway.toml [env] section"
signal: env_validated
on_fail: ABORT ("Missing required env vars")
```

### Step 3: validate_migrations
```yaml
action: "Test database migrations for safety"
checks:
  - "All UP migrations apply cleanly"
  - "All DOWN migrations roll back cleanly"
  - "No destructive DDL without explicit approval (DROP TABLE, DROP COLUMN)"
  - "Advisory lock prevents parallel migration"
signal: migrations_safe
on_fail: ABORT ("Migration safety check failed")
```

### Step 4: health_local
```yaml
action: "Verify /health returns 200 on local environment"
checks:
  - "GET /health returns 200"
  - "Response matches HealthResponse schema"
  - "database.connected = true"
  - "All 14 startup checks pass or fallback"
signal: health_local_ok
on_fail: ABORT ("Local health check failed — fix before deploying")
```

### Step 5: create_rollback_plan
```yaml
action: "Generate rollback plan for affected services"
template: "N05_operations/P05_output/rollback_plan_template.md"
covers:
  - "Which service(s) being deployed"
  - "Blast radius (dependent services, CORS impact, auth impact)"
  - "Data at risk (irreversible migrations? new data created?)"
  - "Rollback command: railway rollback --service <name>"
  - "Post-rollback verification: /health + CORS + auth flow"
  - "Communication: who to notify, estimated downtime"
signal: rollback_ready
on_fail: ABORT ("Cannot deploy without rollback plan")
```

### Step 6: railway_up
```yaml
action: "Execute deployment"
command: "railway up"
pre_check: "railway link --service <name> confirmed"
timeout: 300s
signal: deploy_complete
on_fail: "Execute rollback plan (Step 5 output)"
```

### Step 7: verify_health_prod
```yaml
action: "Wait for /health 200 in production"
max_wait: 30s
poll_interval: 3s
checks:
  - "GET https://<service>.railway.app/health returns 200"
  - "status = 'healthy' or 'degraded'"
  - "version matches deployed version"
signal: health_prod_ok
on_fail: "Execute rollback (railway rollback --service <name>)"
```

### Step 8: verify_pipeline
```yaml
action: "Check execution pipeline tiers"
endpoint: "GET /pipeline/health"
checks:
  - "available_tiers includes 'local'"
  - "If cloud keys present: 'cloud' tier available"
  - "Pipeline status != 'unhealthy'"
signal: pipeline_ok
on_fail: "Log warning, continue (degraded is acceptable)"
```

### Step 9: monitor_logs
```yaml
action: "Monitor Railway logs for 60 seconds"
command: "railway logs --tail"
duration: 60s
watch_for:
  - "ERROR or CRITICAL log levels"
  - "Unhandled exceptions"
  - "Connection pool exhaustion"
  - "Rate limit storms"
signal: monitoring_active
on_fail: "Escalate — rollback if errors > 5 in 60s"
```

### Step 10: signal_complete
```yaml
action: "Write completion signal and clean up"
signal: deploy_signaled
outputs:
  - "Signal: n05 deploy_complete q=9.0"
  - "Handoff archive"
  - "Checkpoint save (step=10, sha=<commit>, status=success)"
```

---

## Failure Recovery

```yaml
on_any_step_failure:
  1: "Log failure with step number, error, and context"
  2: "If step >= 6 (post-deploy): execute rollback plan"
  3: "If step < 6 (pre-deploy): abort with diagnostic"
  4: "Save checkpoint at failed step for resume"
  5: "Signal: n05 deploy_failed q=0"
  6: "Escalate to N07 if rollback also fails"
```

## Resume Protocol

```yaml
resume:
  checkpoint_file: "N05_operations/P10_memory/checkpoint_operations.md"
  saves: [step_number, service_name, commit_sha, rollback_plan_path]
  resume_from: "last successful step + 1"
  cleanup: "delete checkpoint after step 10 confirmed"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_deploy_ops]] | upstream | 0.38 |
| [[p02_agent_railway_superintendent]] | upstream | 0.37 |
| [[p08_ac_railway_superintendent]] | upstream | 0.37 |
| [[p12_wf_builder_8f_pipeline]] | sibling | 0.36 |
| [[p03_sp_railway_superintendent]] | upstream | 0.36 |
| [[p03_sp_deploy_ops]] | upstream | 0.36 |
| [[p05_output_deploy_checklist]] | upstream | 0.35 |
| [[p01_kc_deploy_paas]] | upstream | 0.35 |
| [[spec_n05_part2]] | upstream | 0.33 |
| [[KC_N05_ZERO_DOWNTIME_DEPLOY]] | upstream | 0.33 |
