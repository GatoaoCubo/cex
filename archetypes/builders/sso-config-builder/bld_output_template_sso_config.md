---
kind: output_template
id: bld_output_template_sso_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sso_config production
quality: null
title: "Output Template Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, output_template]
tldr: "Template with vars for sso_config production"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p09_sso_{{name}}.yaml
name: {{name}}
description: {{description}}
quality: null
sso_provider: {{sso_provider}}
client_id: {{client_id}}
client_secret: {{client_secret}}
redirect_uri: {{redirect_uri}}
---
```

<!-- id: p09_sso_[a-z][a-z0-9_]+.yaml (e.g., p09_sso_azure.yaml) -->
<!-- name: Human-readable SSO config name -->
<!-- description: Brief purpose of this configuration -->
<!-- quality: MUST be null -->
<!-- sso_provider: Identity provider name (e.g., Azure AD, Okta) -->
<!-- client_id: OAuth client ID from provider -->
<!-- client_secret: OAuth client secret (sensitive) -->
<!-- redirect_uri: Callback URL registered with provider -->

```yaml
# Example Configuration
sso_provider: Azure AD
client_id: "12345-abcde-67890-fghij"
client_secret: "supersecretkey123!"
redirect_uri: "https://app.example.com/sso/callback"
```

| Field          | Required | Example Value                     |
|----------------|----------|-----------------------------------|
| sso_provider   | ✅       | Azure AD, Okta, Google Workspace  |
| client_id      | ✅       | 12345-abcde-67890-fghij          |
| client_secret  | ✅       | supersecretkey123!               |
| redirect_uri   | ✅       | https://app.example.com/sso/callback |
