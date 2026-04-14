---
kind: output_template
id: bld_output_template_customer_segment
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for customer_segment production
quality: null
title: "Output Template Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, output_template]
tldr: "Template with vars for customer_segment production"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p02_cs_{{segment_name}}.md
name: {{segment_name}}
description: {{segment_description}}
quality: null
created_at: {{created_at}}
updated_at: {{updated_at}}
---
```

<!-- id: Generated filename following p02_cs_[a-z][a-z0-9_]+.md pattern -->
<!-- name: Segment identifier (e.g., "high_net_worth") -->
<!-- description: Brief explanation of segment characteristics -->
<!-- quality: Always null for customer segments -->
<!-- created_at: ISO 8601 timestamp (e.g., "2023-09-01T12:00:00Z") -->
<!-- updated_at: ISO 8601 timestamp (e.g., "2023-09-02T14:30:00Z") -->

| Segment Name       | Description                  | Target              | Example         |
|--------------------|------------------------------|---------------------|-----------------|
| high_net_worth     | Customers with $1M+ AUM      | Institutional       | {{example_data}}|
| retail             | Individual retail clients    | Retail              | {{example_data}}|

```json
{
  "segment": "{{segment_name}}",
  "criteria": {
    "min_aum": {{min_aum}},
    "geography": ["{{region}}"],
    "assets": ["{{asset_type}}"]
  }
}
```

<!-- example_data: Replace with actual customer data examples -->
<!-- min_aum: Numeric value for minimum asset threshold -->
<!-- region: ISO 3166-1 alpha-2 country code (e.g., "US") -->
<!-- asset_type: Type of financial instrument (e.g., "equity") -->
