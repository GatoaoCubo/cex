---
quality: 8.3
quality: 7.9
id: bld_memory_deployment_manifest
kind: knowledge_card
pillar: P10
title: "Memory: deployment_manifest Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
tags: [memory, deployment_manifest, P09]
llm_function: INJECT
tldr: "Recalled patterns and corrections for deployment_manifest builder sessions."
density_score: null
related:
  - p03_sp_env_config_builder
  - p12_wf_auto_security
  - bld_architecture_env_config
  - p02_agent_deploy_ops
  - p03_sp_deploy_ops
  - p11_qg_env_config
  - p03_sp_quickstart_guide_builder
  - p03_sp_quality_gate_builder
  - p03_sp_golden_test_builder
  - p03_sp_path_config_builder
---

# Memory: deployment_manifest Builder

## Persistent Patterns
| Pattern | Frequency | Source |
|---------|-----------|--------|
| Always pin versions (never latest) | HIGH | Security + reproducibility requirement |
| Rollback_to must reference a known-good revision | HIGH | Recovery path mandatory |
| Secrets via reference, never inline | HIGH | Security gate H04 |
| artifacts_count must match list length | HIGH | Gate H06 |
| health_check_endpoint always required for services | MED | Gate H07 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User says "deploy latest" | Pin to current HEAD SHA or explicit semver |
| User omits rollback | Ask for prior stable version; default to N-1 |
| User writes secret value inline | Replace with vault path reference |
| User conflates with env_config | Redirect: env_config for runtime vars; deployment_manifest for what to deploy |
| User conflates with canary_config | Redirect: canary_config for traffic split; deployment_manifest for artifact spec |

## Context Injection Priority
1. bld_schema_deployment_manifest.md (always)
2. bld_examples_deployment_manifest.md (golden reference)
3. env_config KC (for config override context)
4. slo_definition KC (for post-deploy success criteria)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_env_config_builder]] | upstream | 0.22 |
| [[p12_wf_auto_security]] | downstream | 0.17 |
| [[bld_architecture_env_config]] | upstream | 0.17 |
| [[p02_agent_deploy_ops]] | upstream | 0.17 |
| [[p03_sp_deploy_ops]] | upstream | 0.16 |
| [[p11_qg_env_config]] | downstream | 0.16 |
| [[p03_sp_quickstart_guide_builder]] | upstream | 0.16 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.15 |
| [[p03_sp_golden_test_builder]] | upstream | 0.15 |
| [[p03_sp_path_config_builder]] | upstream | 0.15 |
