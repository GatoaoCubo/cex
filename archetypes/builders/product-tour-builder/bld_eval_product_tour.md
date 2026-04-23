---
kind: quality_gate
id: p05_qg_product_tour
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for product_tour
quality: 9.1
title: "Quality Gate Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for product_tour"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_product_tour
  - p05_qg_interactive_demo
  - p05_qg_integration_guide
  - p03_qg_multimodal_prompt
  - p05_qg_pricing_page
  - p11_qg_usage_report
  - p07_qg_eval_metric
  - p05_qg_quickstart_guide
  - p03_sp_product_tour_builder
  - p05_qg_user_journey
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric       | threshold | operator | scope      |
|--------------|-----------|----------|------------|
| completion_rate | 85%       | >=       | all users  |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID          | Check                          | Fail Condition                                      |
|-------------|--------------------------------|-----------------------------------------------------|
| H01         | YAML frontmatter valid         | Invalid YAML syntax or missing required fields      |
| H02         | ID matches ^p05_pt_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern              |
| H03         | kind field matches 'product_tour' | kind field is incorrect or missing                  |
| H04         | Steps are sequential and non-overlapping | Steps are out of order or overlap                 |
| H05         | Tooltips have clear, concise text | Tooltip text is ambiguous or exceeds 150 characters |
| H06         | Triggers are user-initiated      | Triggers are automatic or non-interactive         |
| H07         | Accessibility compliance (ARIA)  | Missing ARIA attributes or keyboard navigation fails |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension       | Weight | Scoring Guide                                      |
|-----|------------------|--------|----------------------------------------------------|
| D01 | Usability        | 0.15   | 1.0: Seamless; 0.5: Minor friction; 0.0: Broken     |
| D02 | Clarity          | 0.15   | 1.0: Clear instructions; 0.5: Ambiguous; 0.0: Confusing |
| D03 | Engagement       | 0.10   | 1.0: High retention; 0.5: Moderate; 0.0: Low        |
| D04 | Accessibility    | 0.15   | 1.0: Full compliance; 0.5: Partial; 0.0: Non-compliant |
| D05 | Consistency      | 0.10   | 1.0: Uniform design; 0.5: Inconsistent; 0.0: Disjointed |
| D06 | Performance      | 0.10   | 1.0: <200ms load; 0.5: 200-500ms; 0.0: >500ms       |
| D07 | Localization     | 0.10   | 1.0: All locales covered; 0.5: Partial; 0.0: Missing |
| D08 | Visual Design    | 0.15   | 1.0: Polished; 0.5: Minor flaws; 0.0: Poor          |

## Actions
(Table: Score | Action)
| Score      | Action                          |
|------------|---------------------------------|
| GOLDEN     | Auto-approve and deploy         |
| PUBLISH    | Manual review required          |
| REVIEW     | QA validation needed            |
| REJECT     | Reject and request major fixes  |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                | approver        | audit trail                          |
|---------------------------|------------------|--------------------------------------|
| Critical bug fix required | Product Manager  | Bypass logged with reason and date   |

## Examples

## Golden Example
```markdown
---
title: "Tour: Analytics Dashboard Features"
kind: product_tour
vendor: Pendo
description: "Guided walkthrough of key analytics dashboard features for new users"
---
**Steps:**
1. **Step 1: Filter Bar**
   - Trigger: User clicks "Add Filter" button
   - Tooltip: "Use this bar to narrow down data by date, region, or user segment"
2. **Step 2: Visualization Panel**
   - Trigger: User hovers over chart
   - Tooltip: "Click to edit chart type (bar, line, pie) or export as PNG"
3. **Step 3: Export Options**
   - Trigger: User clicks "Export" dropdown
   - Tooltip: "Download data as CSV, PDF, or share via email"
```

## Anti-Example 1: Confusing with onboarding_flow
```markdown
---
title: "Tour: First Login Setup"
kind: onboarding_flow
vendor: Intercom
description: "Walkthrough for completing user profile during first login"
---
**Steps:**
1. **Step 1: Name Input**
   - Trigger: User arrives at profile page
   - Tooltip: "Enter your full name to personalize your experience"
```
## Why it fails
Mixes product tour with onboarding_flow (activation). Product tours focus on feature discovery, not account setup.

## Anti-Example 2: Missing trigger logic
```markdown
---
title: "Tour: Collaboration Tools"
kind: product_tour
vendor: UserGuiding
description: "Showcase collaboration features"
---
**Steps:**
1. **Step 1: Comment Section**
   - Tooltip: "Add comments to specific data points for team discussion"
```
## Why it fails
No trigger defined - the tour cannot be activated automatically or contextually. Triggers are essential for timed or event-based tours.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
