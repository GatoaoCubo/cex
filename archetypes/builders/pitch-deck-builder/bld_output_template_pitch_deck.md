---
kind: output_template
id: bld_output_template_pitch_deck
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for pitch_deck production
quality: 9.1
title: "Output Template Pitch Deck"
version: "1.0.1"
author: n02_marketing
tags: [pitch_deck, builder, output_template]
tldr: "Template with vars for pitch_deck production"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

<!-- Pitch deck output template. 10-slide Sequoia structure. Replace all {{vars}}. -->

```markdown
---
id: p05_pd_{{name}}
kind: pitch_deck
pillar: P05
quality: null
title: {{title}}
company: {{company_name}}
stage: {{funding_stage}}
ask: {{funding_ask}}
audience: {{audience}}
---

## Slide 1: Problem
**Headline:** {{problem_headline}}

| Pain Point | Impact | Evidence |
|---|---|---|
| {{pain_1}} | {{quantified_impact_1}} | {{source_1}} |
| {{pain_2}} | {{quantified_impact_2}} | {{source_2}} |

> "{{customer_quote}}" -- {{customer_name}}, {{customer_title}}

## Slide 2: Why Now
{{why_now_narrative}}

| Catalyst | Details |
|---|---|
| {{catalyst_1}} | {{catalyst_1_detail}} |
| {{catalyst_2}} | {{catalyst_2_detail}} |

## Slide 3: Solution
**One-liner:** {{solution_one_liner}}

{{solution_description}}

**Key differentiators:**
1. {{differentiator_1}}
2. {{differentiator_2}}
3. {{differentiator_3}}

## Slide 4: Market Size
| Metric | Value | Source |
|---|---|---|
| TAM | {{tam}} | {{tam_source}} |
| SAM | {{sam}} | {{sam_source}} |
| SOM | {{som}} | {{som_source}} |
| CAGR | {{cagr}} | {{cagr_source}} |

## Slide 5: Product
{{product_description}}

**Core feature matrix:**
| Feature | Benefit | Status |
|---|---|---|
| {{feature_1}} | {{benefit_1}} | {{status_1}} |
| {{feature_2}} | {{benefit_2}} | {{status_2}} |

## Slide 6: Business Model
| Revenue Stream | Pricing | Unit Economics |
|---|---|---|
| {{stream_1}} | {{price_1}} | CAC: {{cac}} / LTV: {{ltv}} |
| {{stream_2}} | {{price_2}} | {{unit_econ_2}} |

Gross margin: {{gross_margin}}

## Slide 7: Traction
**Headline metric:** {{headline_metric}}

| KPI | Current | 3 Months Ago | Growth |
|---|---|---|---|
| {{kpi_1}} | {{current_1}} | {{prev_1}} | {{growth_1}} |
| {{kpi_2}} | {{current_2}} | {{prev_2}} | {{growth_2}} |

Notable milestones: {{milestones}}

## Slide 8: Team
| Name | Role | Relevant Background |
|---|---|---|
| {{founder_1}} | {{role_1}} | {{background_1}} |
| {{founder_2}} | {{role_2}} | {{background_2}} |
| {{advisor_1}} | Advisor | {{advisor_background}} |

## Slide 9: Financials
| Year | Revenue | Expenses | EBITDA |
|---|---|---|---|
| {{year_1}} | {{rev_1}} | {{exp_1}} | {{ebitda_1}} |
| {{year_2}} | {{rev_2}} | {{exp_2}} | {{ebitda_2}} |
| {{year_3}} | {{rev_3}} | {{exp_3}} | {{ebitda_3}} |

## Slide 10: Ask
**Raising:** {{funding_ask}} at {{valuation}} valuation

**Use of funds:**
| Category | % | Amount | Milestone |
|---|---|---|---|
| {{use_1}} | {{pct_1}} | {{amount_1}} | {{milestone_1}} |
| {{use_2}} | {{pct_2}} | {{amount_2}} | {{milestone_2}} |

**Exit horizon:** {{exit_timeline}} via {{exit_path}}
```
