---
kind: tools
id: bld_tools_sso_config
pillar: P04
llm_function: CALL
purpose: Tools available for sso_config production
quality: 8.9
title: "Tools Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, tools]
tldr: "Tools available for sso_config production"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_rbac_policy
  - bld_tools_usage_quota
  - bld_tools_integration_guide
  - bld_tools_playground_config
  - bld_tools_churn_prevention_playbook
  - bld_tools_customer_segment
  - bld_tools_sandbox_spec
  - bld_tools_changelog
  - bld_tools_github_issue_template
  - bld_tools_pricing_page
---

## Context
These tools support sso_config artifact production -- generating SSO configuration specs
for SAML, OIDC, and SCIM-based identity providers.

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact .md to .yaml | After save |
| cex_score.py --apply | Peer review scoring (D1-D5 weighted) | Before publish |
| cex_doctor.py | Builder health check (validates all 13 ISOs) | Post-build |
| cex_hygiene.py | Artifact CRUD + 8-rule enforcement | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Validates frontmatter + kind/pillar/llm_function | CI gate |
| cex_hooks.py pre-commit | ASCII enforcement + schema check | Pre-commit |
| cex_retriever.py | TF-IDF similarity search (find similar artifacts) | F3 INJECT |

## External References
- SAML 2.0 (OASIS standard) -- metadata XML format, HTTP-POST/Redirect bindings
- OIDC 1.0 + OAuth 2.1 -- token-based federated authentication
- SCIM 2.0 (RFC 7642) -- user provisioning protocol for JIT account creation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_rbac_policy]] | sibling | 0.55 |
| [[bld_tools_usage_quota]] | sibling | 0.53 |
| [[bld_tools_integration_guide]] | sibling | 0.44 |
| [[bld_tools_playground_config]] | sibling | 0.39 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.37 |
| [[bld_tools_customer_segment]] | sibling | 0.37 |
| [[bld_tools_sandbox_spec]] | sibling | 0.36 |
| [[bld_tools_changelog]] | sibling | 0.36 |
| [[bld_tools_github_issue_template]] | sibling | 0.36 |
| [[bld_tools_pricing_page]] | sibling | 0.35 |
