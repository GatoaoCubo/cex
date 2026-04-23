---
quality: 8.2
quality: 7.7
id: bld_instruction_deployment_manifest
kind: instruction
pillar: P09
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
title: "Deployment Manifest Builder Instructions"
target: "deployment-manifest-builder agent"
phases_count: 4
prerequisites:
  - "Target environment is identified (staging, production, etc.)"
  - "Artifact list with versions is known"
  - "Rollback revision or strategy is specified"
validation_method: checklist
domain: deployment_manifest
tags: [instruction, deployment_manifest, P09, config]
llm_function: REASON
tldr: "Build a deployment_manifest that specifies artifact list, target environment, config overrides, and rollback strategy."
density_score: null
related:
  - p03_sp_env_config_builder
  - p06_is_creation_data
  - bld_collaboration_env_config
  - bld_examples_kind
  - bld_schema_env_config
  - env-config-builder
  - bld_output_template_sandbox_spec
  - bld_instruction_golden_test
  - bld_knowledge_card_env_config
  - bld_collaboration_path_config
---
## Context
The deployment-manifest-builder produces a `deployment_manifest` artifact -- a structured specification of WHAT to deploy (artifacts + versions), WHERE (environment/target), HOW (config overrides, secrets), and what to do on failure (rollback). This is NOT env_config (runtime environment variables alone), NOT sandbox_spec (ephemeral test environment), NOT canary_config (traffic-split rollout).

**Input contract**:
- `manifest_name`: string -- kebab-case identifier
- `target_env`: string -- environment name (staging, production, canary)
- `artifacts`: list -- each with name, version, checksum
- `config_overrides`: map -- env var overrides for this deployment
- `rollback_to`: string -- revision or artifact version to revert to
- `health_check`: object -- endpoint and expected response

**Output contract**: single `deployment_manifest` YAML at `N0X_operations/P09_config/p09_dm_{name}.md`.

## Phases

### Phase 1: Enumerate Artifacts
Collect all artifacts to be deployed. Each entry needs:
- `name`: artifact id or image name
- `version`: semver or SHA
- `checksum`: SHA256 for integrity verification
- `source`: registry or path
Assert: at least 1 artifact present.

### Phase 2: Specify Target Environment
Define deployment target:
- `environment`: staging | production | preview
- `namespace`: Kubernetes namespace or equivalent
- `region`: cloud region if applicable
- `cluster`: target cluster id
Assert: environment is non-empty.

### Phase 3: Encode Config Overrides
List configuration that differs from defaults:
- `env_vars`: key/value pairs overriding base env_config
- `secrets`: list of secret refs (vault path or k8s secret name)
- `replicas`: override for scale
- `resources`: cpu/memory limits if overriding defaults

### Phase 4: Define Rollback Strategy
Specify recovery plan:
- `rollback_to`: prior revision id or artifact version
- `rollback_trigger`: health-check failure count or error threshold
- `health_check_endpoint`: URL and expected 2xx
- `readiness_timeout_seconds`: how long to wait before declaring failure

## Output Structure
Required frontmatter fields: id, kind, pillar, version, manifest_name, target_env, artifacts_count, quality: null, tags.
Required body sections: Artifacts, Target Environment, Config Overrides, Rollback Strategy.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_env_config_builder]] | upstream | 0.24 |
| [[p06_is_creation_data]] | upstream | 0.23 |
| [[bld_collaboration_env_config]] | downstream | 0.22 |
| [[bld_examples_kind]] | upstream | 0.21 |
| [[bld_schema_env_config]] | upstream | 0.21 |
| [[env-config-builder]] | related | 0.21 |
| [[bld_output_template_sandbox_spec]] | upstream | 0.20 |
| [[bld_instruction_golden_test]] | sibling | 0.19 |
| [[bld_knowledge_card_env_config]] | upstream | 0.18 |
| [[bld_collaboration_path_config]] | related | 0.18 |
