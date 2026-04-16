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
