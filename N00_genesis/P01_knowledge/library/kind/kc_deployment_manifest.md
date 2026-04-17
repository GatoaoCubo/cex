---
id: kc_deployment_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 8.2
tags: [kind, taxonomy, deployment_manifest, P09, config]
density_score: 1.0
updated: "2026-04-17"
---

# deployment_manifest

## Spec
```yaml
kind: deployment_manifest
pillar: P09
llm_function: COLLABORATE
max_bytes: 4096
naming: p09_dm_{{name}}.md + .yaml
core: false
```

## What It Is
A deployment_manifest specifies WHAT artifacts to deploy, WHERE (target environment), and HOW (configuration overrides, secrets references, rollback strategy). It is the contract between the build pipeline and the deployment infrastructure.

Industry analogs: Kubernetes manifest, Helm values.yaml, AWS CloudFormation template, Terraform module input.

It is NOT:
- `env_config` (runtime environment variables in isolation -- no artifact list, no rollback)
- `sandbox_spec` (ephemeral test environment definition -- not a stable deployment target)
- `canary_config` (traffic split strategy -- canary_config handles HOW traffic flows; deployment_manifest handles WHAT is deployed)

## When to Use
- Before triggering a deployment pipeline (staging, production, preview)
- To document what version of which artifacts was deployed and when
- To specify rollback plan as a pre-condition of deployment approval
- For multi-artifact deployments where artifact coordination matters

## When NOT to Use
- Defining only runtime environment variables -> use `env_config`
- Creating a test/ephemeral environment -> use `sandbox_spec`
- Configuring traffic split between versions -> use `canary_config`
- Defining a contractual SLA with an external party -> use `enterprise_sla`

## Structure
```yaml
# Required frontmatter fields
id: p09_dm_{name_slug}
kind: deployment_manifest
pillar: P09
manifest_name: "..."
target_env: staging | production | preview
artifacts_count: N
rollback_to: "prior-version-or-revision"
quality: null
```

```markdown
## Artifacts
| Name | Version | Checksum (SHA256) | Source |
...

## Target Environment
environment, namespace, region, cluster

## Config Overrides
env_vars table, secrets references (path only)

## Rollback Strategy
rollback_to, trigger condition, health_check_endpoint, auto_rollback
```

## Key Rules
1. NEVER inline secret values -- vault path or k8s secret reference only
2. NEVER use "latest" tag -- always pin to semver or SHA
3. ALWAYS include rollback_to -- no manifest ships without a recovery path
4. health_check_endpoint is required for service artifacts

## Relationships
```
[workflow] --> [deployment_manifest] --> [env_config]
                     |
                     +--> [canary_config] (traffic split)
                     +--> [slo_definition] (post-deploy success criteria)
                     +--> [signal: deploy_complete]
```

## Cross-Framework Map
| Platform | Equivalent |
|----------|-----------|
| Kubernetes | Deployment + ConfigMap + Secret manifest |
| Helm | values.yaml + Chart.yaml |
| AWS CloudFormation | Stack template |
| Terraform | Module variables + tfvars |
| Ansible | Playbook variables |

## Decision Tree
- IF deploying to production AND no rollback_to -> BLOCK: require rollback revision
- IF artifact version = "latest" -> REJECT: pin to semver or SHA
- IF secrets in env_vars values -> REJECT: use secret reference
- IF target_env is test/ephemeral -> use sandbox_spec instead
- DEFAULT: staging before production; staging manifest is template for production

## Quality Criteria
- GOOD: Artifact list with pinned versions, target env specified, rollback_to set
- GREAT: Checksums on artifacts, health_check_endpoint, auto_rollback: true
- FAIL: "latest" version, inline secrets, missing rollback_to
