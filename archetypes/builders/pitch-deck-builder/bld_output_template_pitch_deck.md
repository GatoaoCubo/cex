---
kind: output_template
id: bld_output_template_pitch_deck
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for pitch_deck production
quality: null
title: "Output Template Pitch Deck"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pitch_deck, builder, output_template]
tldr: "Template with vars for pitch_deck production"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

<!-- Pitch deck output template: variables below render a complete pitch deck. -->
```markdown
---
id: p05_pd_{{name}}.md
pillar: P05
quality: null
title: {{title}}
description: {{description}}
keywords: {{keywords}}
audience: {{audience}}
---
# {{title}}

## Executive Summary
{{executive_summary}} <!-- High-level overview of the project -->

## Market Opportunity
| Metric         | Value        | Source       |
|----------------|--------------|--------------|
| Market Size    | {{market_size}} | {{source}} |
| CAGR           | {{cagr}}      | {{source}}   |

## Product
```python
# Sample API endpoint
def {{api_endpoint}}():
    return {"status": "success", "data": {{data}}}
```
<!-- Replace with actual code -->

## Financials
{{financial_summary}} <!-- 3-year revenue/expense projections -->

## Team
{{team_members}} <!-- Names, roles, and expertise -->

## Traction
{{traction_metrics}} <!-- Key milestones and KPIs -->
```
