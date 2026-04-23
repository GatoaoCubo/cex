---
kind: quality_gate
id: p11_qg_roi_calculator
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for roi_calculator
quality: 9.0
title: "Quality Gate Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for roi_calculator"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_roi_calculator
  - bld_instruction_roi_calculator
  - p10_mem_roi_calculator_builder
  - kc_roi_calculator
  - p03_sp_roi_calculator_builder
  - bld_knowledge_card_roi_calculator
  - roi-calculator-builder
  - bld_collaboration_roi_calculator
  - bld_output_template_roi_calculator
  - p07_qg_benchmark_suite
---

## Quality Gate

## Definition
| metric         | threshold | operator | scope          |
|----------------|-----------|----------|----------------|
| Accuracy       | 95%       | >=       | Economic buyers|
| Completeness   | 100%      | ==       | All inputs     |

## HARD Gates
| ID             | Check                          | Fail Condition                              |
|----------------|--------------------------------|---------------------------------------------|
| H01            | YAML frontmatter valid         | Missing or invalid frontmatter              |
| H02            | ID matches pattern             | ID does not match ^p11_roi_[a-z][a-z0-9_]+$ |
| H03            | kind field matches 'roi_calculator' | kind field invalid                          |
| H04            | Input parameters defined       | Missing required input fields               |
| H05            | ROI formula mathematically valid | Formula errors or undefined variables       |
| H06            | TCO comparison included        | Missing TCO comparison table                |
| H07            | Output units specified         | Missing or ambiguous output units           |

## SOFT Scoring
| Dim        | Dimension         | Weight | Scoring Guide                          |
|------------|-------------------|--------|----------------------------------------|
| D01        | Accuracy          | 0.15   | 100% = 1.0, 90% = 0.9                   |
| D02        | Completeness      | 0.15   | 100% = 1.0, 80% = 0.8                   |
| D03        | Clarity           | 0.10   | Clear = 1.0, ambiguous = 0.5            |
| D04        | TCO comparison    | 0.15   | Detailed = 1.0, partial = 0.7           |
| D05        | User-friendliness | 0.10   | Intuitive = 1.0, complex = 0.5          |
| D06        | Consistency       | 0.10   | No contradictions = 1.0, 1+ errors = 0.5 |
| D07        | Documentation     | 0.15   | Full = 1.0, partial = 0.7               |
| D08        | Versioning        | 0.10   | Versioned = 1.0, unversioned = 0.5      |

## Actions
| Score     | Action         |
|-----------|----------------|
| GOLDEN    | Approve        |
| PUBLISH   | Publish        |
| REVIEW    | Peer review    |
| REJECT    | Reject         |

## Bypass
| conditions                          | approver       | audit trail              |
|------------------------------------|----------------|--------------------------|
| Critical project with senior approval | CTO           | "Bypassed by CTO on 2023-10-01" |

## Examples

## Golden Example  
```yaml  
title: ROI Calculator for Cloud Migration  
author: A. Smith, Financial Analyst  
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
