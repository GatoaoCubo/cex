---
kind: output_template
id: bld_output_template_sso_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sso_config production
quality: 9.0
title: "Output Template Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, output_template]
tldr: "Template with vars for sso_config production"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_sso_config
  - kc_sso_config
  - bld_schema_sso_config
  - p09_qg_sso_config
  - p03_sp_sso_config_builder
  - bld_knowledge_card_sso_config
  - sso-config-builder
  - bld_instruction_sso_config
  - p10_mem_sso_config_builder
  - bld_output_template_oauth_app_config
---

```yaml
---
id: p09_sso_{{name}}.yaml
kind: sso_config
pillar: P09
quality: null
provider: {{provider}}
protocol: {{protocol}}
idp_entity_id: {{idp_entity_id}}
acs_url: {{acs_url}}
slo_url: {{slo_url}}
metadata_url: {{metadata_url}}
redirect_uri: {{redirect_uri}}
---
```

<!-- id: p09_sso_[a-z][a-z0-9_]+.yaml (e.g., p09_sso_okta_saml.yaml) -->
<!-- provider: Identity provider name (e.g., "Okta", "Azure AD") -->
<!-- protocol: SAML or OIDC -->
<!-- idp_entity_id: IdP-issued entity ID URI -->
<!-- acs_url: Assertion Consumer Service URL (SAML) / redirect_uri (OIDC) -->
<!-- slo_url: Single Logout Service URL -->
<!-- metadata_url: IdP metadata endpoint URL -->
<!-- redirect_uri: Callback URL registered with provider -->
<!-- NEVER include client_secret, private keys, or credentials -- use secret_config reference instead -->

```yaml
# Example Configuration (SAML 2.0)
id: p09_sso_okta_saml.yaml
kind: sso_config
pillar: P09
quality: null
provider: Okta
protocol: SAML
idp_entity_id: "https://idp.example.okta.com"
acs_url: "https://app.example.com/sso/saml/callback"
slo_url: "https://app.example.com/sso/saml/logout"
metadata_url: "https://idp.example.okta.com/metadata"
redirect_uri: "https://app.example.com/sso/callback"
# client credentials: reference p09_secret_okta.yaml (NEVER inline)
```

| Field         | Required | Notes                                     |
|---------------|----------|-------------------------------------------|
| provider      | yes      | Okta, Azure AD, Google Workspace, Auth0   |
| protocol      | yes      | SAML or OIDC                              |
| idp_entity_id | yes      | URI from IdP metadata                     |
| acs_url       | yes      | HTTPS endpoint -- must match IdP config   |
| slo_url       | yes      | Logout endpoint                           |
| metadata_url  | yes      | IdP metadata XML endpoint                 |
| redirect_uri  | yes      | HTTPS -- registered with provider         |
| client_secret | NEVER    | Use secret_config reference instead       |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_sso_config]] | downstream | 0.55 |
| [[kc_sso_config]] | upstream | 0.43 |
| [[bld_schema_sso_config]] | downstream | 0.43 |
| [[p09_qg_sso_config]] | downstream | 0.37 |
| [[p03_sp_sso_config_builder]] | upstream | 0.36 |
| [[bld_knowledge_card_sso_config]] | upstream | 0.35 |
| [[sso-config-builder]] | downstream | 0.34 |
| [[bld_instruction_sso_config]] | upstream | 0.33 |
| [[p10_mem_sso_config_builder]] | downstream | 0.31 |
| [[bld_output_template_oauth_app_config]] | sibling | 0.30 |
