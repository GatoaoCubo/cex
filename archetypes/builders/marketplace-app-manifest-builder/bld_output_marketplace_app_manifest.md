---
kind: output_template
id: bld_output_template_marketplace_app_manifest
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for marketplace_app_manifest production
quality: 8.7
title: "Output Template Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, output_template]
tldr: "Template with vars for marketplace_app_manifest production"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_marketplace_app_manifest
  - bld_config_marketplace_app_manifest
  - bld_schema_app_directory_entry
  - marketplace-app-manifest-builder
  - bld_output_template_oauth_app_config
  - p09_qg_marketplace_app_manifest
  - bld_output_template_playground_config
  - bld_collaboration_marketplace_app_manifest
  - bld_output_template_app_directory_entry
  - kc_marketplace_app_manifest
---

```yaml
---
id: p09_mam_{{app_name}}.yaml
name: {{app_name}}
version: {{version}}
description: {{short_description}}
publisher: {{publisher}}
quality: null
categories:
  - {{category_1}}
  - {{category_2}}
dependencies:
  - {{dependency_1}}
  - {{dependency_2}}
---
```

<!-- id: Unique identifier following p09_mam_[a-z][a-z0-9_]+.yaml pattern -->
<!-- name: Human-readable app name -->
<!-- version: Semantic version string (e.g., 1.0.0) -->
<!-- description: Brief app functionality summary -->
<!-- publisher: Organization/individual responsible -->
<!-- quality: MUST remain null -->
<!-- categories: Array of relevant marketplace categories -->
<!-- dependencies: Array of required system/app dependencies -->

| Feature       | Description                  |
|---------------|------------------------------|
| Pricing       | {{pricing_model}}           |
| Users         | {{target_audience}}         |
| Compliance    | {{regulatory_requirements}} |

```json
{
  "metadata": {
    "license": "{{license_type}}",
    "support": "{{support_contact}}"
  }
}
```

<!-- pricing_model: Subscription, freemium, etc. -->
<!-- target_audience: Retail, enterprise, etc. -->
<!-- regulatory_requirements: GDPR, CCPA compliance status -->
<!-- license_type: MIT, Apache 2.0, etc. -->
<!-- support_contact: Email or ticket system URL -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_marketplace_app_manifest]] | downstream | 0.33 |
| [[bld_config_marketplace_app_manifest]] | downstream | 0.24 |
| [[bld_schema_app_directory_entry]] | downstream | 0.22 |
| [[marketplace-app-manifest-builder]] | downstream | 0.20 |
| [[bld_output_template_oauth_app_config]] | sibling | 0.20 |
| [[p09_qg_marketplace_app_manifest]] | downstream | 0.20 |
| [[bld_output_template_playground_config]] | sibling | 0.19 |
| [[bld_collaboration_marketplace_app_manifest]] | downstream | 0.19 |
| [[bld_output_template_app_directory_entry]] | sibling | 0.18 |
| [[kc_marketplace_app_manifest]] | upstream | 0.18 |
