---
kind: collaboration
id: bld_collaboration_sso_config
pillar: P12
llm_function: COLLABORATE
purpose: How sso_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, collaboration]
tldr: "How sso_config-builder works in crews with other builders"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_rbac_policy
  - bld_collaboration_oauth_app_config
  - bld_collaboration_sandbox_config
  - bld_collaboration_eval_metric
  - bld_collaboration_model_provider
  - bld_collaboration_safety_policy
  - bld_collaboration_reranker_config
  - bld_collaboration_tts_provider
  - bld_collaboration_visual_workflow
  - bld_collaboration_prompt_technique
---

## Crew Role  
Designs and maintains SSO configuration templates and policies, ensuring alignment with identity provider (IdP) and service provider (SP) requirements.  

## Receives From  
| Builder       | What                     | Format       |  
|---------------|--------------------------|--------------|  
| Identity Provider | Metadata (XML/JSON)      | XML/JSON     |  
| Service Provider  | Configuration requirements | YAML/Markdown |  
| Security Team     | Compliance guidelines    | PDF/Markdown |  

## Produces For  
| Builder       | What                     | Format       |  
|---------------|--------------------------|--------------|  
| SSO Config    | Configuration files      | XML/JSON     |  
| Documentation | Policy documentation     | Markdown/PDF |  
| Validation    | Configuration validation | CSV/JSON     |  

## Boundary  
Does NOT handle RBAC policies (rbac_policy-builder), secret management (secret_config-builder), or user authentication flows (auth_service).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_rbac_policy]] | sibling | 0.34 |
| [[bld_collaboration_oauth_app_config]] | sibling | 0.30 |
| [[bld_collaboration_sandbox_config]] | sibling | 0.30 |
| [[bld_collaboration_eval_metric]] | sibling | 0.29 |
| [[bld_collaboration_model_provider]] | sibling | 0.28 |
| [[bld_collaboration_safety_policy]] | sibling | 0.27 |
| [[bld_collaboration_reranker_config]] | sibling | 0.25 |
| [[bld_collaboration_tts_provider]] | sibling | 0.24 |
| [[bld_collaboration_visual_workflow]] | sibling | 0.23 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.23 |
