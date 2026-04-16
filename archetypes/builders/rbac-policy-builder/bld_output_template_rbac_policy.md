---
kind: output_template
id: bld_output_template_rbac_policy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for rbac_policy production
quality: 8.7
title: "Output Template Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, output_template]
tldr: "Template with vars for rbac_policy production"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p09_rbac_{{policy_name}}.yaml <!-- Use pattern: p09_rbac_[a-z][a-z0-9_]+.yaml -->
name: {{policy_name}} <!-- Human-readable policy name -->
kind: rbac_policy
pillar: P09
quality: null <!-- Must remain null -->
---
```

| Role       | Resource       | Actions          |
|------------|----------------|------------------|
| admin      | /v1/*          | ["*"]            |
| viewer     | /v1/data/*     | ["GET"]          |

```yaml
rules:
  - role: {{role_name}} <!-- e.g., "admin" or "viewer" -->
    resource: {{resource_path}} <!-- e.g., "/v1/data/*" -->
    actions: <!-- List of allowed actions -->
      - {{action}} <!-- e.g., "GET", "POST", "*" -->
```
