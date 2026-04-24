---
id: kc_sso_config
kind: knowledge_card
8f: F3_inject
title: SSO/SAML/OIDC Configuration Guide
version: 1.0.0
quality: 8.6
pillar: P01
density_score: 0.92
related:
  - bld_knowledge_card_sso_config
  - sso-config-builder
  - p03_sp_sso_config_builder
  - bld_instruction_sso_config
  - bld_examples_sso_config
  - p10_mem_sso_config_builder
  - bld_output_template_sso_config
  - bld_collaboration_sso_config
  - bld_tools_sso_config
  - bld_schema_sso_config
---

**SSO/SAML/OIDC Configuration Overview**

Single Sign-On (SSO) protocols like SAML and OIDC enable secure identity provider (IdP) integration. This guide covers configuration essentials for these standards:

1. **Core Components**
   - Identity Provider (IdP): Authenticates users (e.g., Okta, Azure AD)
   - Service Provider (SP): Receives authentication assertions (your application)
   - Security Assertion Markup Language (SAML)
   - OpenID Connect (OIDC) - OAuth 2.0 extension for identity

2. **Configuration Parameters**
   - `issuer`: IdP's unique identifier (e.g., `https://idp.example.com`)
   - `client_id`: SP's registered identifier with the IdP
   - `client_secret`: Secure credential for SP authentication
   - `redirect_uri`: SP's endpoint for IdP authentication responses
   - `signature_algorithm`: Signing method for SAML assertions (e.g., `RSA-SHA256`)
   - `encryption_algorithm`: Data encryption method (e.g., `AES256-CBC`)
   - `token_endpoint`: OIDC token endpoint URL
   - `authorization_endpoint`: OIDC authorization endpoint URL

3. **Implementation Considerations**
   - Use HTTPS for all communication
   - Validate certificate chains for IdP trust
   - Implement token introspection for OIDC
   - Set appropriate session expiration times
   - Monitor for replay attacks and CSRF vulnerabilities
   - Regularly rotate client secrets
   - Maintain audit logs of authentication events
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_sso_config]] | sibling | 0.56 |
| [[sso-config-builder]] | downstream | 0.54 |
| [[p03_sp_sso_config_builder]] | downstream | 0.52 |
| [[bld_instruction_sso_config]] | downstream | 0.51 |
| [[bld_examples_sso_config]] | downstream | 0.50 |
| [[p10_mem_sso_config_builder]] | downstream | 0.45 |
| [[bld_output_template_sso_config]] | downstream | 0.44 |
| [[bld_collaboration_sso_config]] | downstream | 0.27 |
| [[bld_tools_sso_config]] | downstream | 0.25 |
| [[bld_schema_sso_config]] | downstream | 0.24 |
