---
id: bld_quality_gate_deployment_manifest
kind: quality_gate
pillar: P07
title: "Gate: deployment_manifest"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
quality: 8.7
tags: [quality_gate, deployment_manifest, P09]
llm_function: GOVERN
tldr: "Validates deployment manifests for artifact pinning, rollback strategy, secrets handling, and environment targeting."
density_score: null
related:
  - p11_qg_quality_gate
  - p11_qg_creation_artifacts
  - p02_agent_deploy_ops
  - bld_schema_model_provider
  - p11_qg_artifact
  - p11_qg_system_prompt
  - p03_sp_deploy_ops
  - n06_api_access_pricing
  - p11_qg_agent
  - bld_config_trace_config
---

## Quality Gate

## Definition
A deployment_manifest specifies what artifacts to deploy, to which environment, with what config, and how to roll back. This gate ensures every manifest is safe to hand to an automated deployment pipeline without human interpretation.

## HARD Gates
Failure on any HARD gate causes immediate REJECT.

| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p09_dm_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `deployment_manifest` |
| H04 | No inline secrets | No plaintext secret values in frontmatter or body |
| H05 | Quality is null | `quality` field is `null` |
| H06 | Artifacts list non-empty | At least 1 artifact with name + version |
| H07 | No "latest" version tags | All artifact versions are pinned (semver or SHA) |
| H08 | rollback_to is set | `rollback_to` field is non-null and non-empty |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Artifacts have checksums | 1.0 | SHA256 present per artifact |
| Target environment fully specified | 1.0 | namespace + region + cluster all present |
| Health check endpoint present | 1.0 | health_check_endpoint is non-empty |
| Config overrides documented | 0.5 | env_vars table present (even if empty) |
| Auto-rollback flag set | 0.5 | auto_rollback: true or false (not missing) |
| Tags include deployment_manifest | 0.5 | tags contains "deployment_manifest" |
| tldr <= 160 chars | 0.5 | Concise summary |

Sum of weights: 5.0. `soft_score = sum(weight * gate_score) / 5.0 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH -- safe for automated pipeline |
| >= 7.0 | REVIEW -- deploy with manual approval |
| < 7.0 | REJECT -- incomplete; do not deploy |

## Examples

# Examples: deployment_manifest

## Golden Example 1 -- CEX API Production Deploy
INPUT: "Deploy cex-api 2.1.0 and worker to production with rollback plan"
OUTPUT:
```yaml
---
id: p09_dm_cex_api_v210_prod
kind: deployment_manifest
pillar: P09
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
manifest_name: "CEX API v2.1.0 Production Deploy"
target_env: production
artifacts_count: 2
rollback_to: "v2.0.3"
domain: cex-api
quality: null
tags: [deployment_manifest, cex-api, production, P09]
tldr: "Deploy CEX API v2.1.0 and worker to prod us-east-1; rollback to v2.0.3 on health failure"
---
## Artifacts
| Name        | Version | Checksum (SHA256)              | Source                        |
|-------------|---------|-------------------------------|-------------------------------|
| cex-api     | 2.1.0   | a1b2c3d4e5f6...               | registry.cex.io/cex-api:2.1.0 |
| cex-worker  | 2.1.0   | 789xyz012abc...               | registry.cex.io/cex-worker:2.1.0|

## Target Environment
| Property   | Value         |
|------------|---------------|
| environment| production    |
| namespace  | cex-prod      |
| region     | us-east-1     |
| cluster    | prod-eks-01   |

## Config Overrides
| Key          | Value                        | Notes                    |
|--------------|------------------------------|--------------------------|
| LOG_LEVEL    | warn                         | Production log level     |
| REPLICAS     | 4                            | Up from staging default 2|
| MAX_POOL     | 20                           | DB connection pool prod  |

Secrets (vault refs -- no plaintext values):
- DATABASE_URL: vault/secret/prod/cex/db_url
- API_KEY: k8s-secret/cex-prod/api-key
- STRIPE_KEY: vault/secret/prod/cex/stripe

## Rollback Strategy
| Property               | Value              |
|------------------------|--------------------|
| rollback_to            | v2.0.3             |
| trigger                | health check fails 120s |
| health_check_endpoint  | GET /health -> 200 |
| readiness_timeout_s    | 120                |
| auto_rollback          | true               |
```
WHY THIS IS GOLDEN:
- Artifact checksums (SHA256) -- reproducible, tamper-evident
- Secrets as vault refs, not inline values (H04 security gate)
- Exact rollback_to version (not "previous")
- Config overrides table documents WHY each value differs from default
- quality: null (H05 pass)

## Golden Example 2 -- SaaS Checkout Hotfix Deploy
INPUT: "Emergency hotfix for checkout service -- payment bug in 1.4.2, deploy 1.4.3 to production NOW"
OUTPUT:
```yaml
---
id: p09_dm_checkout_hotfix_v143
kind: deployment_manifest
pillar: P09
version: 1.0.0
created: "2026-04-18"
updated: "2026-04-18"
manifest_name: "Checkout Service Hotfix v1.4.3 -- Payment Bug Fix"
target_env: production
artifacts_count: 1
rollback_to: "1.4.1"
domain: checkout-service
deploy_type: hotfix
quality: null
tags: [deployment_manifest, checkout, hotfix, payment, revenue-critical, P09]
tldr: "HOTFIX: checkout v1.4.3 to prod -- patches payment race condition in 1.4.2; rollback to 1.4.1 (last stable)"
---
## Artifacts
| Name              | Version | Checksum (SHA256)              | Source                              |
|-------------------|---------|-------------------------------|-------------------------------------|
| checkout-service  | 1.4.3   | f9e8d7c6b5a4...               | registry.company.io/checkout:1.4.3  |

## Deploy Notes (Hotfix Protocol)
- Skip: staging validation (hotfix urgency -- revenue loss active)
- Require: manual approval from VPE before deploy_cmd execution
- Verify: payment smoke test within 5 minutes of deploy
- Alert: RevOps on deploy start + completion (revenue impact tracking)

## Target Environment
| Property   | Value             |
|------------|-------------------|
| environment| production        |
| namespace  | checkout-prod     |
| region     | us-east-1         |
| cluster    | prod-eks-02       |

## Config Overrides
| Key                     | Value  | Notes                              |
|-------------------------|--------|------------------------------------|
| PAYMENT_RETRY_ENABLED   | true   | Re-enable after bug fix validates  |
| CIRCUIT_BREAKER_TIMEOUT | 5000   | Restore from emergency 30s timeout |

## Rollback Strategy
| Property               | Value                                   |
|------------------------|-----------------------------------------|
| rollback_to            | 1.4.1                                   |
| skip_1_4_2             | true (1.4.2 = bugged, do not roll to it)|
| trigger                | payment_error_rate > 0.5% in 5min       |
| health_check_endpoint  | POST /api/checkout/test -> 200          |
| readiness_timeout_s    | 60                                      |
| auto_rollback          | true                                    |
```
WHY THIS IS GOLDEN:
- deploy_type: hotfix encodes urgency context
- Skips 1.4.2 in rollback chain (explicitly notes bugged version)
- Revenue-alert integration (RevOps notification)
- 60s readiness timeout (tighter than standard 120s -- hotfix speed)
- Payment-specific smoke test named in rollback trigger

## Anti-Example 1: Inline Secret (REJECTED)
```yaml
# FAIL: plaintext credentials in manifest
DATABASE_URL: postgres://admin:SECRET123@prod-db.company.io/checkout
STRIPE_SECRET: sk_live_REAL_SECRET_KEY_HERE
image: checkout:latest  # FAIL: "latest" is non-reproducible
```
WHY REJECTED: Inline secrets in a deployment manifest will be committed to git, exposed in CI logs, and readable by anyone with repo access. Use vault paths or k8s secret refs. "latest" means each deploy may pull a different image -- breaks reproducibility and rollback.

## Anti-Example 2: Missing Rollback Target (REJECTED)
```yaml
target_env: production
artifacts:
  - name: api
    version: 3.0.0
# FAIL: no rollback_to
# FAIL: no health_check
# FAIL: no rollback trigger
rollback: true  # FAIL: "true" with no target or trigger is useless
```
WHY REJECTED: `rollback: true` with no `rollback_to`, no health check, and no trigger means the system knows rollback is desired but has zero information to execute it. On deploy failure, engineers must manually find the previous version, health check URL, and criteria -- all while the revenue impact clock is running.

## Anti-Example 3: No Artifact Checksums (REJECTED)
```yaml
artifacts:
  - name: api
    version: 2.0.0
    source: dockerhub/mycompany/api:2.0.0
# FAIL: no checksum -- anyone can push a malicious 2.0.0 tag to overwrite
# FAIL: dockerhub public registry -- no access control
```
WHY REJECTED: Without checksums, the manifest cannot verify that the artifact deployed matches what was tested. A supply chain attack or accidental tag overwrite would go undetected. Always include SHA256 checksums for production deploys.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
