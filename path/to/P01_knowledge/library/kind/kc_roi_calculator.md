---
id: kc_roi_calculator
kind: knowledge_card
title: ROI Calculator Specification
version: 1.0.0
quality: null
pillar: P01
---

# ROI Calculator Specification

## Overview
This calculator quantifies return on investment for economic decision-makers. It compares net present value (NPV), internal rate of return (IRR), and total cost of ownership (TCO) across scenarios.

## Key Inputs
- Initial investment cost
- Annual revenue projections
- Variable operational costs
- Time horizon (years)
- Discount rate (for NPV)
- Maintenance cost inflation rate

## Calculation Formulas
**Net Present Value (NPV)**  
NPV = Σ [(Revenue_t - Cost_t) / (1 + r)^t]  
Where r = discount rate, t = time period

**Internal Rate of Return (IRR)**  
Solve for r where NPV = 0

**Payback Period**  
Years to recover initial investment  
= Initial Cost / Annual Net Profit

## TCO Comparison
| Scenario | Initial Cost | Annual Cost | NPV | IRR | Payback |
|---------|-------------|------------|-----|-----|---------|
| A       | $100k       | $20k       | $150k | 25% | 4 years |
| B       | $150k       | $15k       | $200k | 30% | 5 years |
| C       | $80k        | $25k       | $120k | 22% | 3 years |

## Use Cases
- SaaS platform adoption analysis
- Marketing campaign ROI evaluation
- Infrastructure modernization planning
- Product development budgeting
```