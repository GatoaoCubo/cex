---
kind: output_template
id: bld_output_template_partner_listing
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for partner_listing production
quality: 8.9
title: "Output Template Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, output_template]
tldr: "Template with vars for partner_listing production"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_partner_listing
  - partner-listing-builder
  - bld_collaboration_partner_listing
  - bld_knowledge_card_partner_listing
  - p05_qg_partner_listing
  - bld_examples_partner_listing
  - bld_output_template_integration_guide
  - bld_schema_partner_listing
  - p03_sp_partner_listing_builder
  - bld_config_partner_listing
---

```markdown
```yaml
---
id: p05_pl_{{name}}.md
pillar: P05
partner_type: {{partner_type}} <!-- e.g., 'exchange', 'wallet' -->
description: {{description}} <!-- Partner overview (max 200 chars) -->
integration_status: {{status}} <!-- 'active', 'pending', 'suspended' -->
quality: null
---
```

## Partner Details
| Field          | Value                     |
|----------------|---------------------------|
| Name           | {{name}}                  <!-- Partner name (e.g., 'Acme Corp') -->
| Website        | {{website}}               <!-- URL (e.g., 'https://acme.com') -->
| API Endpoint   | {{api_url}}               <!-- Integration URL -->

```yaml
# Example API Config
partner:
  name: {{name}}
  keys:
    api_key: {{api_key}} <!-- Partner-provided key -->
    secret: {{secret}}   <!-- Partner-provided secret -->
```

## Integration Requirements
- ✅ KYC verification required
- 🔄 Real-time data sync
- 🔐 Mutual TLS encryption
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_partner_listing]] | upstream | 0.39 |
| [[partner-listing-builder]] | related | 0.37 |
| [[bld_collaboration_partner_listing]] | downstream | 0.33 |
| [[bld_knowledge_card_partner_listing]] | upstream | 0.31 |
| [[p05_qg_partner_listing]] | downstream | 0.27 |
| [[bld_examples_partner_listing]] | downstream | 0.27 |
| [[bld_output_template_integration_guide]] | sibling | 0.26 |
| [[bld_schema_partner_listing]] | downstream | 0.26 |
| [[p03_sp_partner_listing_builder]] | upstream | 0.26 |
| [[bld_config_partner_listing]] | downstream | 0.25 |
