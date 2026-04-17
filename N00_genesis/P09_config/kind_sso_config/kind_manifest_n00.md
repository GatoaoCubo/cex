---
id: n00_sso_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "SSO Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, sso_config, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An sso_config defines the Single Sign-On integration with an enterprise identity provider using SAML 2.0, OIDC, or OAuth2. It enables enterprise customers to authenticate to CEX using their existing IdP (Okta, Azure AD, Google Workspace), enforces MFA requirements, and maps IdP groups to CEX RBAC roles for seamless access control.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `sso_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| protocol | enum | yes | saml2 \| oidc \| oauth2 |
| idp_name | string | yes | Identity provider name (okta, azure_ad, google) |
| entity_id | string | yes | Service provider entity ID (SP metadata URL) |
| idp_metadata_url | string | yes | IdP metadata endpoint |
| mfa_required | boolean | yes | Enforce MFA for all users |
| attribute_mappings | object | yes | IdP attribute -> CEX field mappings |
| group_to_role_map | object | no | IdP group -> CEX RBAC role assignments |
| session_duration_h | integer | no | SSO session lifetime in hours (default 8) |

## When to use
- Enabling enterprise customers to use their existing identity provider
- Configuring Okta or Azure AD integration for a white-label deployment
- Setting up OIDC for browser-based CEX companion applications

## Builder
`archetypes/builders/sso_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind sso_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sso_config_okta_enterprise
kind: sso_config
pillar: P09
nucleus: n05
title: "Okta SAML2 Enterprise SSO"
version: 1.0
quality: null
---
protocol: saml2
idp_name: okta
entity_id: https://cex.customer.com/saml/metadata
idp_metadata_url: https://customer.okta.com/app/metadata
mfa_required: true
attribute_mappings:
  email: user.email
  name: user.displayName
group_to_role_map:
  AI-Admins: orchestrator
  AI-Users: builder
session_duration_h: 8
```

## Related kinds
- `rbac_policy` (P09) -- RBAC roles that SSO group mappings point to
- `oauth_app_config` (P09) -- OAuth layer that OIDC SSO extends
- `white_label_config` (P09) -- branded SSO for white-label deployments
