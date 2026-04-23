---
kind: quality_gate
id: p01_qg_competitive_matrix
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for competitive_matrix
quality: 9.0
title: "Quality Gate Competitive Matrix"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for competitive_matrix artifacts"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_competitive_matrix
  - p03_sp_competitive_matrix_builder
  - bld_knowledge_card_competitive_matrix
  - p05_qg_github_issue_template
  - competitive-matrix-builder
  - bld_schema_competitive_matrix
  - p05_qg_analyst_briefing
  - bld_instruction_competitive_matrix
  - p07_qg_eval_metric
  - p11_qg_quality_gate
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| ID pattern | ^p01_cm_[a-z][a-z0-9_]+\\.md$ | matches | all competitive_matrix files |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p01_cm_[a-z][a-z0-9_]+\\.md$ | ID does not match pattern |
| H03 | kind field equals "competitive_matrix" | kind != "competitive_matrix" |
| H04 | Feature parity grid present with 3+ competitors | fewer than 3 competitors in matrix |
| H05 | All data sources cited with access date | unverified or undated data |
| H06 | Battle card section present for primary competitor | no us-vs-them comparison present |
| H07 | No subjective language without data support | unsubstantiated claims (e.g., "best", "leading") |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Completeness | 0.20 | All features mapped to all competitors = 1.0; gaps = proportional |
| D2 | Data accuracy | 0.20 | Primary sources cited, dated within 12 months = 1.0; outdated/secondary = 0.5 |
| D3 | Differentiation clarity | 0.15 | Win reasons explicit per capability = 1.0; vague = 0.0 |
| D4 | Battle card usability | 0.15 | Objection + counter present for primary competitor = 1.0; missing = 0.0 |
| D5 | MQ positioning | 0.15 | Gartner-style quadrant placement with rationale = 1.0; absent = 0.0 |
| D6 | Anti-FUD coverage | 0.15 | At least 3 factual FUD counters with sources = 1.0; none = 0.0 |

## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | Auto-publish to sales portal |
| >= 8.0 | Review by PM then publish |
| >= 7.0 | Flag for QA revision |
| < 7.0 | Revise and resubmit |

## Bypass
| conditions | approver | audit trail |
|------------|----------|-------------|
| Urgent RFP deadline with incomplete competitor data | CTO | Email log with RFP reference and deadline |

## Examples

## Golden Example
```markdown
---
title: "Competitive Matrix: CRM Solutions"
date: 2023-10-15
author: Sales Strategy Team
version: 1.2
---

| Feature                | Salesforce       | HubSpot          | Pipedrive        |
|-----------------------|------------------|------------------|------------------|
| Lead Scoring          | Advanced (AI)    | Basic            | Customizable     |
| Automation            | Full workflow    | Limited          | Mid-level        |
| Integration (API)     | 500+ apps        | 300+ apps        | 150+ apps        |
| Pricing Model         | Tiered (per user)| Flat fee         | Per deal         |
| Support               | 24/7 premium     | Business hours   | Email only       |
| Strengths             | Enterprise scale | Marketing focus  | Sales simplicity |
| Weaknesses            | Complex UI       | Limited AI       | No marketing tools |
```

## Anti-Example 1: Vague Vendor Names
```markdown
| Feature       | ProviderA | ProviderB |
|---------------|-----------|-----------|
| Speed         | Fast      | Slow      |
| Cost          | High      | Low       |
| Ease of Use   | Easy      | Hard      |
```
## Why it fails: Uses generic placeholder names (ProviderA/ProviderB) instead of real vendor names, making the matrix unactionable for sales teams needing specific competitive insights.

## Anti-Example 2: Missing Competitive Dimensions
```markdown
| Feature       | Salesforce | HubSpot |
|---------------|------------|---------|
| Pricing       | $150/user  | $50/user|
| UI            | Complex    | Simple  |
```
## Why it fails: Only includes basic features without critical competitive dimensions like automation capabilities, integration depth, or support models, which are essential for procurement evaluations.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
