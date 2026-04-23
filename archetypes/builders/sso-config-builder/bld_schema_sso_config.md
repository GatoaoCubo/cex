---
kind: schema
id: bld_schema_sso_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for sso_config
quality: 9.1
title: "Schema Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for sso_config"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_oauth_app_config
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_audit_log
  - bld_schema_sandbox_spec
  - bld_schema_multimodal_prompt
  - bld_schema_app_directory_entry
  - bld_schema_eval_metric
  - bld_schema_usage_report
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID Pattern |  
| kind | string | yes | "sso_config" | CEX configuration type |  
| pillar | string | yes | "P09" | Strategic pillar classification |  
| title | string | yes | null | Human-readable configuration name |  
| version | string | yes | "1.0.0" | Schema version |  
| created | datetime | yes | null | ISO 8601 timestamp |  
| updated | datetime | yes | null | ISO 8601 timestamp |  
| author | string | yes | null | Responsible party |  
| domain | string | yes | "sso" | Configuration domain |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes | [] | Metadata keywords |  
| tldr | string | yes | null | Summary of configuration purpose |  
| provider | string | yes | null | SSO provider name (e.g., "Okta") |  
| protocol | string | yes | null | Authentication protocol (e.g., "SAML") |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| redirect_uri | string | Validated URI for SSO redirects |  
| scopes | list | Required OAuth scopes |  

## ID Pattern  
^p09_sso_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Configuration Overview**  
   - Summary of SSO integration purpose and scope  
2. **Provider Details**  
   - Metadata about the SSO provider (entity ID, endpoints)  
3. **Security Settings**  
   - Encryption, certificate paths, and authentication policies  
4. **Integration Instructions**  
   - Steps for system administrators to deploy/configure  
5. **Compliance and Auditing**  
   - Regulatory requirements and audit trails  
6. **Maintenance Schedule**  
   - Rotation timelines for secrets and certificates  

## Constraints  
- File must conform to ID Pattern and max 3072 bytes  
- `provider` must be a registered SSO entity  
- `protocol` must be a supported standard (SAML, OAuth 2.0, etc.)  
- `redirect_uri` must be HTTPS and match provider's domain  
- `scopes` must be non-empty and validated against provider's API  
- `quality` field must be assigned by peer review before deployment

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_oauth_app_config]] | sibling | 0.67 |
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_benchmark_suite]] | sibling | 0.66 |
| [[bld_schema_audit_log]] | sibling | 0.64 |
| [[bld_schema_sandbox_spec]] | sibling | 0.63 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.63 |
| [[bld_schema_app_directory_entry]] | sibling | 0.62 |
| [[bld_schema_eval_metric]] | sibling | 0.61 |
| [[bld_schema_usage_report]] | sibling | 0.61 |
