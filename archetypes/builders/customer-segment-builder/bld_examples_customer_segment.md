---
kind: examples
id: bld_examples_customer_segment
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of customer_segment artifacts
quality: 8.8
title: "Examples Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, examples]
tldr: "Golden and anti-examples of customer_segment artifacts"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
title: Mid-Market Healthcare Provider ICP
kind: customer_segment
firmographics:
  industry: Healthcare
  company_size: 100-500 employees
  revenue: $10M-$50M
  location: North America, Europe
  technology_stack: Epic, Cerner, Microsoft 365
needs:
  - Streamlined patient data management
  - HIPAA-compliant analytics tools
  - Integration with existing EHR systems
  - Scalable cloud infrastructure
  - 24/7 technical support
```

## Anti-Example 1: Vague Generalization
```yaml
title: Small Businesses
kind: customer_segment
firmographics:
  industry: All industries
  company_size: 1-10 employees
needs:
  - "Basic tools"
  - "Low cost"
  - "Easy to use"
```
## Why it fails
Lacks specificity in industry, revenue, and technology stack. "Basic tools" and "low cost" are too generic to guide product development or marketing.

## Anti-Example 2: Persona Confusion
```yaml
title: Tech-Savvy Entrepreneurs
kind: customer_segment
firmographics:
  industry: All industries
  company_size: 1-10 employees
  personal_attributes:
    - Age: 25-35
    - Education: College degree
    - Tech proficiency: High
needs:
  - "Cool features"
  - "Modern UI"
  - "Social media integration"
```
## Why it fails
Mixes personal attributes (age, education) with firmographics. Focuses on user preferences rather than organizational needs, misaligning with ICP definition requirements.
