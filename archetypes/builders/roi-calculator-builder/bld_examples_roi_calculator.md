---
kind: examples
id: bld_examples_roi_calculator
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of roi_calculator artifacts
quality: 8.9
title: "Examples Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, examples]
tldr: "Golden and anti-examples of roi_calculator artifacts"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
```yaml  
title: ROI Calculator for Cloud Migration  
author: Jane Doe, Financial Analyst  
date: 2023-10-15  
inputs:  
  - Initial Investment: $5,000  
  - Monthly Cloud Cost (AWS EC2): $200  
  - Monthly Savings (vs. On-Premises): $1,000  
  - Time Horizon: 12 months  
formulas:  
  ROI: ((Monthly Savings × Time Horizon) - Initial Investment) / Initial Investment × 100  
  Payback Period: Initial Investment / Monthly Savings  
  TCO: Initial Investment + (Monthly Cloud Cost × Time Horizon)  
tco_comparison:  
  AWS: $7,400  
  Azure: $7,500  
  GCP: $7,300  
```  

## Anti-Example 1: Placeholder Names  
```yaml  
title: ROI Calculator for ProviderA  
inputs:  
  - Initial Investment: $X  
  - Monthly Cost: $Y  
formulas:  
  ROI: (Y - X) / X  
tco_comparison:  
  ProviderA: $Z  
```  
## Why it fails  
Uses generic placeholders like "ProviderA" and "$X" instead of real vendor names and concrete values, making it impossible for economic buyers to compare options or validate assumptions.  

## Anti-Example 2: Missing TCO Comparison  
```yaml  
title: ROI Calculator for AWS  
inputs:  
  - Initial Investment: $5,000  
  - Monthly Savings: $1,000  
formulas:  
  ROI: (1,000 × 12 - 5,000) / 5,000 × 100  
```  
## Why it fails  
Omits the TCO comparison section, which is critical for economic buyers to evaluate total costs across providers. Without TCO, the calculator lacks actionable insights for decision-making.
