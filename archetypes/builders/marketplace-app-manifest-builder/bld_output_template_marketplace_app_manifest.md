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
