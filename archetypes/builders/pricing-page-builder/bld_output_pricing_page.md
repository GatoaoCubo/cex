---
kind: output_template
id: bld_output_template_pricing_page
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for pricing_page production
quality: 8.7
title: "Output Template Pricing Page"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pricing_page, builder, output_template]
tldr: "Template with vars for pricing_page production"
domain: "pricing_page construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_pricing_page
  - bld_instruction_subscription_tier
  - bld_instruction_pricing_page
  - p05_qg_pricing_page
  - pricing_optimization_memory
  - p08_pat_pricing_framework
  - bld_output_template_subscription_tier
  - bld_tools_pricing_page
  - bld_knowledge_card_pricing_page
  - subscription-tier-builder
---

```yaml
---
id: p05_pp_{{name}}.md
kind: pricing_page
pillar: P05
quality: null
title: {{title}}
description: {{description}}
pricing_model: {{flat|tiered|freemium}}
currency: {{USD|EUR|BRL}}
tags: [pricing_page, {{product_name}}, {{tier_style}}]
tldr: "{{one_sentence_summary}}"
domain: pricing_page construction
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author_name}}
---
```

<!-- GUIDANCE:
  - name: lowercase slug, e.g. "acme_saas" -> id becomes p05_pp_acme_saas.md
  - pricing_model: flat (single price), tiered (3+ tiers), freemium (free + paid)
  - currency: ISO 4217 code. Default USD for SaaS
  - Most Popular tier: mark with badge in table (see golden example)
  - CTA per tier: action-oriented verb ("Start Free", "Get Pro", "Contact Sales")
-->

<!-- Pricing Tiers Table -->
| Tier | Price ({{currency}}) | Features |
|------|----------------------|----------|
| Basic | {{basic_price}} | {{basic_features}} |
| Pro | {{pro_price}} | {{pro_features}} |
| Enterprise | {{enterprise_price}} | {{enterprise_features}} |

<!-- API Pricing Example -->
```json
{
  "endpoint": "/v1/pricing",
  "rate_limit": "{{rate_limit}}",
  "cost_per_call": "{{cost_per_call}}"
}
```

<!-- Additional Notes -->
{{notes}} <!-- Key terms, discounts, or usage policies -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pricing_page]] | downstream | 0.36 |
| [[bld_instruction_subscription_tier]] | upstream | 0.32 |
| [[bld_instruction_pricing_page]] | upstream | 0.31 |
| [[p05_qg_pricing_page]] | downstream | 0.28 |
| [[pricing_optimization_memory]] | downstream | 0.27 |
| [[p08_pat_pricing_framework]] | downstream | 0.26 |
| [[bld_output_template_subscription_tier]] | sibling | 0.26 |
| [[bld_tools_pricing_page]] | upstream | 0.25 |
| [[bld_knowledge_card_pricing_page]] | upstream | 0.24 |
| [[subscription-tier-builder]] | downstream | 0.23 |
