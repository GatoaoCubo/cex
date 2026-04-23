---
kind: collaboration
id: bld_collaboration_sandbox_config
pillar: P12
llm_function: COLLABORATE
purpose: How sandbox_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, collaboration]
tldr: "How sandbox_config-builder works in crews with other builders"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_sandbox_spec
  - sandbox-config-builder
  - bld_collaboration_rbac_policy
  - bld_collaboration_sso_config
  - bld_collaboration_action_paradigm
  - bld_collaboration_memory_benchmark
  - p03_sp_code_executor_builder
  - bld_collaboration_oauth_app_config
  - bld_collaboration_transport_config
  - bld_collaboration_ab_test_config
---

## Crew Role  
Designs and validates sandbox isolation policies, ensuring secure resource boundaries for execution environments.  

## Receives From  
| Builder            | What                  | Format  |  
|-------------------|-----------------------|---------|  
| SecurityPolicyBuilder | Security constraints  | JSON    |  
| ResourceLimitBuilder  | CPU/Memory limits     | YAML    |  
| ComplianceChecker     | Regulatory rules      | XML     |  

## Produces For  
| Builder              | What                  | Format  |  
|---------------------|-----------------------|---------|  
| ExecutionEnvironmentBuilder | Isolated config   | JSON    |  
| MonitoringSystem      | Monitoring specs      | YAML    |  
| ConfigValidator       | Validation report     | JSON    |  

## Boundary  
Does NOT handle environment variables (env_config-builder) or execution logic (code_executor). UI/UX teams manage user-facing config interfaces.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_sandbox_spec]] | sibling | 0.35 |
| [[sandbox-config-builder]] | upstream | 0.34 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.30 |
| [[bld_collaboration_sso_config]] | sibling | 0.30 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.28 |
| [[bld_collaboration_memory_benchmark]] | sibling | 0.27 |
| [[p03_sp_code_executor_builder]] | upstream | 0.26 |
| [[bld_collaboration_oauth_app_config]] | sibling | 0.26 |
| [[bld_collaboration_transport_config]] | sibling | 0.26 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.25 |
