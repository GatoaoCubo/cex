---
id: kc_roi_calculator
kind: knowledge_card
title: ROI Calculator Specification
version: 1.0.0
quality: 8.8
pillar: P01
language: en
density_score: 1.0
---

# ROI Calculator Specification

## Overview
ROI (Return on Investment) measures profitability of investments. This calculator helps economic buyers compare financial outcomes of different options using standardized formulas and TCO analysis.

## Inputs
- Initial investment cost
- Annual revenue generated
- Annual operational costs
- Time period (years)
- Discount rate (%)
- Salvage value (optional)

## Formulas
**Basic ROI**:  
`(Revenue - Costs) / Investment * 100%`

**Net Present Value (NPV)**:  
`Σ [(Cash Flow_t) / (1 + r)^t] - Initial Investment`

**Internal Rate of Return (IRR)**:  
Solve for `r` where NPV = 0

**Total Cost of Ownership (TCO)**:  
`Initial Cost + (Annual Costs × Time) - Salvage Value`

## TCO Comparison
| Category       | Fixed Costs       | Variable Costs    |
|----------------|-------------------|-------------------|
| Infrastructure | $50,000/year      | $100/unit         |
| Maintenance    | $20,000/year      | $50/unit          |
| Training       | $15,000/one-time  | $20/unit          |

## Checklist
- [ ] Verify all financial data is accurate
- [ ] Confirm time period matches business cycle
- [ ] Include salvage value for long-term projects
- [ ] Validate discount rate against market rates

## Example
Calculate ROI for a $200k project with:
- $120k annual revenue
- $60k costs
- 5-year lifespan
- 8% discount rate

## Tips
1. Use NPV for multi-year projects
2. Compare IRR with required rate of return
3. Include opportunity cost in TCO analysis
4. Adjust discount rate for risk profiles
```