---
quality: 8.2
quality: 7.8
id: bld_architecture_deployment_manifest
kind: knowledge_card
pillar: P08
title: "Architecture: deployment_manifest Relationships"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
tags: [architecture, deployment_manifest, P09]
llm_function: CONSTRAIN
tldr: "How deployment_manifest relates to env_config, canary_config, sandbox_spec, and workflow."
density_score: null
related:
  - bld_architecture_env_config
  - p01_kc_secret_config
  - p01_kc_workflow
  - bld_architecture_workflow
  - workflow-builder
  - env-config-builder
  - bld_collaboration_workflow
  - bld_examples_kind
  - p12_wf_builder_8f_pipeline
  - p12_wf_create_orchestration_agent
---

# Architecture: deployment_manifest

## Relationship Graph
```
[workflow] --> [deployment_manifest] --> [env_config]
                     |                        |
                     +--> [canary_config]      +--> [secret_config]
                     |
                     +--> [sandbox_spec] (test only, not production)
                     |
                     +--> [slo_definition] (success criteria post-deploy)
```

## Kind Boundaries
| Kind | Relationship | Boundary |
|------|-------------|---------|
| env_config | USES | deployment_manifest references env_config; does not define runtime vars inline |
| canary_config | SIBLING | canary_config handles traffic split; deployment_manifest handles artifact list + target |
| sandbox_spec | EXCLUDES | sandbox_spec is ephemeral test env; deployment_manifest targets stable envs |
| workflow | PARENT | workflow steps may include deployment_manifest as a COLLABORATE step |
| slo_definition | POST-DEPLOY | slo_definition defines success metrics measured after deployment completes |
| secret_config | REFERENCES | secrets are referenced by path only, never inlined |

## Integration Points
- **Upstream**: workflow (F8 COLLABORATE step), handoff (triggering context)
- **Downstream**: env_config (variable injection), slo_definition (success gate), signal (deploy complete)
- **Sibling**: canary_config (traffic split), sandbox_spec (test env)

## Pillar Placement
Pillar P09 (Config) -- deployment_manifest is a configuration artifact, not a runtime executable. It specifies parameters for a deployment tool (Kubernetes, Helm, custom runner) to execute.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_env_config]] | related | 0.26 |
| [[p01_kc_secret_config]] | sibling | 0.24 |
| [[p01_kc_workflow]] | sibling | 0.22 |
| [[bld_architecture_workflow]] | related | 0.22 |
| [[workflow-builder]] | downstream | 0.21 |
| [[env-config-builder]] | downstream | 0.21 |
| [[bld_collaboration_workflow]] | downstream | 0.21 |
| [[bld_examples_kind]] | upstream | 0.20 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.19 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.19 |
