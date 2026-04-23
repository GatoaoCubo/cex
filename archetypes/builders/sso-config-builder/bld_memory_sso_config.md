---
kind: memory
id: p10_mem_sso_config_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for sso_config construction
quality: 8.7
title: "Memory Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, memory]
tldr: "Learned patterns and pitfalls for sso_config construction"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_sso_config
  - p03_sp_sso_config_builder
  - bld_instruction_sso_config
  - kc_sso_config
  - sso-config-builder
  - bld_examples_sso_config
  - bld_output_template_sso_config
  - p10_lr_transport_config_builder
  - p10_mem_graph_rag_config_builder
  - bld_tools_sso_config
---

## Observation
Misconfigured entity IDs or mismatched SLO URLs often cause SAML/OIDC flows to fail. Overlooking attribute mapping rules can lead to incomplete user profile data post-authentication.

## Pattern
Using standardized templates for metadata alignment ensures compatibility across IdPs. Modular configuration blocks for protocol-specific settings (e.g., SAML vs. OIDC) improve maintainability.

## Evidence
Reviewed SAML configs with correct entity ID and OIDC configs referencing well-known endpoints demonstrated successful integration.

## Recommendations
- Use IdP-provided metadata to auto-populate entity IDs and endpoints.
- Validate attribute mappings against IdP schema during config generation.
- Separate protocol-specific settings into reusable configuration modules.
- Enforce SLO/SSO URL consistency across all service provider configs.
- Document IdP-specific quirks (e.g., custom attribute formats) in config comments.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_sso_config]] | upstream | 0.45 |
| [[p03_sp_sso_config_builder]] | upstream | 0.45 |
| [[bld_instruction_sso_config]] | upstream | 0.45 |
| [[kc_sso_config]] | upstream | 0.39 |
| [[sso-config-builder]] | upstream | 0.37 |
| [[bld_examples_sso_config]] | upstream | 0.35 |
| [[bld_output_template_sso_config]] | upstream | 0.25 |
| [[p10_lr_transport_config_builder]] | related | 0.24 |
| [[p10_mem_graph_rag_config_builder]] | sibling | 0.21 |
| [[bld_tools_sso_config]] | upstream | 0.20 |
