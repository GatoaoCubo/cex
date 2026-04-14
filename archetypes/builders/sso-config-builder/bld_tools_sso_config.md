---
kind: tools
id: bld_tools_sso_config
pillar: P04
llm_function: CALL
purpose: Tools available for sso_config production
quality: null
title: "Tools Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, tools]
tldr: "Tools available for sso_config production"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| sso_compile.py | Compiles SSO config files into deployable formats | Pre-deployment |  
| sso_score.py | Scores config compliance with security policies | Post-validation |  
| sso_retriever.py | Fetches SSO metadata from identity providers | Config setup |  
| sso_doctor.py | Diagnoses misconfigurations in SSO setups | Troubleshooting |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| sso_linter.py | Validates syntax and structure of config files | Pre-deployment |  
| sso_policy_checker.py | Ensures config adheres to organizational policies | Compliance audits |  
| sso_simulator.py | Tests SSO flows in isolated environments | Pre-deployment |  

## External References  
- SAML 2.0 specification (identity provider integration)  
- OAuth2.0 framework (token-based authentication)  
- Ansible (config deployment automation)
