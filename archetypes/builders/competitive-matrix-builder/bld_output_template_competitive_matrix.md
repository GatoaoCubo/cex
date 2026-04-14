---
kind: output_template
id: bld_output_template_competitive_matrix
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for competitive_matrix production
quality: null
title: "Output Template Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, output_template]
tldr: "Template with vars for competitive_matrix production"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p01_cm_{{name}}.md
name: {{matrix_name}}
pillar: P01
description: {{matrix_description}}
quality: null
last_updated: {{date}}
---
```

<!-- id: ID following p01_cm_[a-z][a-z0-9_]+.md pattern -->
<!-- name: Title of the competitive matrix -->
<!-- pillar: Always "P01" -->
<!-- description: Summary of the matrix purpose -->
<!-- quality: Must be "null" -->
<!-- last_updated: Date in YYYY-MM-DD format -->

| Competitor | Market Share | Technology | Customer Support | Pricing | Notes         |
|------------|--------------|------------|------------------|---------|---------------|
| CEX A      | 30%          | High       | 24/7             | Low     | <!-- Add details --> |
| CEX B      | 25%          | Medium     | 12/7             | Medium  | <!-- Add details --> |

```yaml
sample_data:
  competitors:
    - name: "CEX A"
      metrics:
        market_share: 30
        technology: "High"
        pricing: "Low"
```
