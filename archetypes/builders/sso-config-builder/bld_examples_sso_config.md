---
kind: examples
id: bld_examples_sso_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of sso_config artifacts
quality: 8.8
title: "Examples Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, examples]
tldr: "Golden and anti-examples of sso_config artifacts"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: sso_config
metadata:
  name: okta-saml-integration
  namespace: default
spec:
  protocol: saml
  idp:
    entity_id: "https://idp.okta.com/app/exk3h4567890abcdef1234567890abcdef/sso/saml/metadata"
    metadata_url: "https://idp.okta.com/app/exk3h4567890abcdef1234567890abcdef/sso/saml/metadata"
    acs_url: "https://app.example.com/saml/acs"
    x509_certificate: "MIID...XYZ="
  sp:
    entity_id: "https://app.example.com/saml/sp"
    assertion_consumer_service_url: "https://app.example.com/saml/acs"
```

## Anti-Example 1: Missing Required Fields
```yaml
kind: sso_config
metadata:
  name: broken-saml
spec:
  protocol: saml
  idp:
    entity_id: "https://idp.example.com/metadata"
```
## Why it fails
Missing `metadata_url`, `acs_url`, and `x509_certificate` fields required for SAML validation and communication. No SP configuration provided.

## Anti-Example 2: Protocol Mixing
```yaml
kind: sso_config
metadata:
  name: mixed-oidc-saml
spec:
  protocol: oidc
  idp:
    issuer: "https://auth0.example.com/oidc"
    client_id: "abcd1234"
    client_secret: "s3cr3t"
  saml:
    entity_id: "https://idp.okta.com/metadata"
```
## Why it fails
Mixing OIDC and SAML configurations in the same artifact. The `saml` field is invalid under OIDC protocol spec. Secret fields should be managed separately via secret_config.
