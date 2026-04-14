---
kind: output_template
id: bld_output_template_pricing_page
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for pricing_page production
quality: null
title: "Output Template Pricing Page"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pricing_page, builder, output_template]
tldr: "Template with vars for pricing_page production"
domain: "pricing_page construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p05_pp_{{name}}.md
pillar: P05
quality: null
title: {{title}}
description: {{description}}
pricing_tier: {{tier}}
currency: {{currency}}
---
```

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
