---
kind: output_template
id: bld_output_template_roi_calculator
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for roi_calculator production
quality: 9.0
title: "Output Template Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, output_template]
tldr: "Template with vars for roi_calculator production"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_roi_calculator
  - kc_roi_calculator
  - bld_instruction_roi_calculator
  - bld_knowledge_card_roi_calculator
  - bld_schema_optimizer
  - roi-calculator-builder
  - p03_sp_roi_calculator_builder
  - bld_schema_reward_model
  - bld_schema_reranker_config
  - bld_examples_roi_calculator
---

```yaml
---
id: p11_roi_{{slug}}
kind: roi_calculator
pillar: P11
title: "{{title}}"
version: "1.0.0"
author: "{{author}}"
created: "{{created}}"
updated: "{{updated}}"
domain: "{{domain}}"
quality: null
tags: [{{tags}}]
tldr: "{{tldr}}"
calculation_method: "{{calculation_method}}"
input_parameters: [{{input_parameters}}]
output_metrics: [{{output_metrics}}]
---
```

<!-- slug: lowercase identifier, e.g. saas_platform_3yr or manufacturing_automation -->
<!-- title: Descriptive name, e.g. "SaaS Platform ROI - 3-Year Model" -->
<!-- domain: Industry context, e.g. "SaaS", "manufacturing", "healthcare" -->
<!-- calculation_method: Formula used, e.g. "NPV with 8% discount rate" or "Forrester TEI" -->
<!-- input_parameters: ["initial_investment", "annual_savings", "implementation_cost", "time_horizon"] -->
<!-- output_metrics: ["roi_percentage", "payback_period_months", "npv", "irr"] -->

## Input Parameters

| Parameter | Type | Unit | Description | Required |
|-----------|------|------|-------------|----------|
| initial_investment | float | USD | Total upfront cost | yes |
| annual_savings | float | USD | Yearly cost reduction | yes |
| implementation_cost | float | USD | One-time setup cost | yes |
| time_horizon | int | years | Evaluation period | yes |
| discount_rate | float | % | Cost of capital (NPV) | yes |
| annual_maintenance | float | USD | Recurring platform costs | yes |

## Output Metrics

| Metric | Formula | Threshold |
|--------|---------|-----------|
| ROI % | (Net Profit / Total Investment) * 100 | >= 15% |
| Payback Period | Total Investment / Annual Savings | <= 24 months |
| NPV | Sum(Savings / (1+r)^t) - Investment | > 0 |
| TCO Reduction | Baseline TCO - New TCO | > 20% |

## Scenario Comparison

| Scenario | Year 1 | Year 2 | Year 3 | ROI % |
|----------|--------|--------|--------|-------|
| Conservative | {{y1_cons}} | {{y2_cons}} | {{y3_cons}} | {{roi_cons}} |
| Base Case | {{y1_base}} | {{y2_base}} | {{y3_base}} | {{roi_base}} |
| Optimistic | {{y1_opt}} | {{y2_opt}} | {{y3_opt}} | {{roi_opt}} |

## Assumptions

- Discount rate: {{discount_rate}}% (WACC or cost of capital)
- Savings realization: {{ramp_months}} months ramp-up
- Maintenance growth: {{maintenance_growth}}% annually
- Source: Forrester TEI methodology / customer-validated data

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_roi_calculator]] | downstream | 0.38 |
| [[kc_roi_calculator]] | upstream | 0.37 |
| [[bld_instruction_roi_calculator]] | upstream | 0.35 |
| [[bld_knowledge_card_roi_calculator]] | upstream | 0.34 |
| [[bld_schema_optimizer]] | downstream | 0.32 |
| [[roi-calculator-builder]] | downstream | 0.31 |
| [[p03_sp_roi_calculator_builder]] | upstream | 0.31 |
| [[bld_schema_reward_model]] | downstream | 0.27 |
| [[bld_schema_reranker_config]] | downstream | 0.27 |
| [[bld_examples_roi_calculator]] | downstream | 0.27 |
