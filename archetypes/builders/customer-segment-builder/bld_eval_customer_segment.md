---
kind: quality_gate
id: p02_qg_customer_segment
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for customer_segment
quality: 9.0
title: "Quality Gate Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for customer_segment"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_customer_segment
  - p07_qg_eval_metric
  - p03_qg_prompt_technique
  - p11_qg_usage_report
  - p05_qg_pricing_page
  - p05_qg_integration_guide
  - p05_qg_user_journey
  - p05_qg_product_tour
  - p11_qg_incident_report
  - p03_qg_multimodal_prompt
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric | threshold | operator | scope |
|---|---|---|---|
| Customer Segment Definition Completeness | 100% | equals | All customer segments |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p02_cs_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field matches 'customer_segment' | Incorrect kind value |
| H04 | Firmographics defined | Missing firmographic data (e.g., industry, size) |
| H05 | Needs documented | No explicit customer needs or pain points |
| H06 | ICP alignment verified | No alignment with Ideal Customer Profile |
| H07 | Data sources cited | No references to data sources for segment definition |
| H08 | ICP scoring methodology documented | No scoring weights or ranking logic present in artifact |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Completeness of firmographics | 0.15 | 1.0 = All attributes present |
| D02 | ICP alignment | 0.20 | 1.0 = Perfect match |
| D03 | Data accuracy | 0.15 | 1.0 = Verified by 3+ sources |
| D04 | Stakeholder input | 0.10 | 1.0 = 100% stakeholder agreement |
| D05 | Use case relevance | 0.15 | 1.0 = All use cases covered |
| D06 | Market validation | 0.10 | 1.0 = 2+ third-party validations |
| D07 | Segment uniqueness | 0.15 | 1.0 = No overlapping definitions |

## Actions
(Table: Score | Action)
| Score | Action |
|---|---|
| GOLDEN (>=9.5) | Auto-publish to production |
| PUBLISH (>=8.0) | Publish with stakeholder review |
| REVIEW (>=7.0) | Require additional validation |
| REJECT (<7.0) | Reject; rework required |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Emergency release | CTO | Requires written justification and audit log |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
