---
kind: collaboration
id: bld_collaboration_sandbox_spec
pillar: P12
llm_function: COLLABORATE
purpose: How sandbox_spec-builder works in crews with other builders
quality: 8.9
title: "Collaboration Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, collaboration]
tldr: "How sandbox_spec-builder works in crews with other builders"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_white_label_config
  - bld_collaboration_ab_test_config
  - bld_collaboration_sandbox_config
  - bld_collaboration_reranker_config
  - bld_collaboration_reward_model
  - bld_collaboration_oauth_app_config
  - sandbox-spec-builder
  - bld_collaboration_subscription_tier
  - bld_collaboration_sdk_example
  - bld_collaboration_integration_guide
---

## Crew Role  
Defines and enforces structural constraints for sandbox environments, ensuring isolation, resource limits, and compliance with team-specific policies.  

## Receives From  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Requirements  | Feature spec       | Document    |  
| Security Team | Compliance rules   | JSON        |  
| Infrastructure| Environment template | YAML       |  

## Produces For  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Dev Team      | Sandbox config     | YAML        |  
| QA Team       | Test scenarios     | JSON        |  
| Ops Team      | Deployment manifest | Terraform |  

## Boundary  
Does NOT handle interactive playground configurations (handled by `playground_config` builder) or production environment setups (handled by `env_config` builder). Does NOT manage actual deployment; only defines spec boundaries.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_white_label_config]] | sibling | 0.42 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.39 |
| [[bld_collaboration_sandbox_config]] | sibling | 0.37 |
| [[bld_collaboration_reranker_config]] | sibling | 0.37 |
| [[bld_collaboration_reward_model]] | sibling | 0.37 |
| [[bld_collaboration_oauth_app_config]] | sibling | 0.34 |
| [[sandbox-spec-builder]] | upstream | 0.32 |
| [[bld_collaboration_subscription_tier]] | sibling | 0.32 |
| [[bld_collaboration_sdk_example]] | sibling | 0.31 |
| [[bld_collaboration_integration_guide]] | sibling | 0.30 |
