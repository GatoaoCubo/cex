---
kind: output_template
id: bld_output_template_oauth_app_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for oauth_app_config production
quality: 8.8
title: "Output Template Oauth App Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [oauth_app_config, builder, output_template]
tldr: "Template with vars for oauth_app_config production"
domain: "oauth_app_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p09_oauth_{{name}}.yaml
name: {{app_name}} <!-- Human-readable name of the OAuth app -->
description: {{app_description}} <!-- Brief purpose of the app -->
client_id: {{client_id}} <!-- Issued by CEX during registration -->
client_secret: {{client_secret}} <!-- Confidential secret for API auth -->
redirect_uri: {{redirect_uri}} <!-- Post-authentication callback URL -->
scope: {{scope}} <!-- Permissions requested (e.g., "read write") -->
quality: null
```

| Field           | Description                          | Example                          |
|-----------------|--------------------------------------|----------------------------------|
| `id`            | Filename following naming rules      | `p09_oauth_user_dashboard.yaml`  |
| `redirect_uri`  | Must match exact URL registered      | `https://app.example.com/callback` |
| `scope`         | Space-separated permissions          | `read_balance trade_orders`      |

```bash
# Example CLI command to register app
cex-cli oauth register \
  --name "User Dashboard" \
  --redirect-uri "https://app.example.com/callback" \
  --scope "read_balance trade_orders"
```
