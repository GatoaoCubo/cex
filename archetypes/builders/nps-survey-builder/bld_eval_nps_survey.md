---
kind: quality_gate
id: p11_qg_nps_survey
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for nps_survey
quality: 9.1
title: "Quality Gate Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for nps_survey"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_nps_survey
  - bld_output_template_nps_survey
  - p03_sp_nps_survey_builder
  - bld_instruction_nps_survey
  - p10_lr_nps_survey_builder
  - p12_qg_renewal_workflow
  - p11_qg_audit_log
  - p05_qg_github_issue_template
  - bld_knowledge_card_nps_survey
  - p01_qg_faq_entry
---

## Quality Gate

## Definition
| Metric                   | Threshold | Operator | Scope                        |
|--------------------------|-----------|----------|------------------------------|
| Bain NPS standard        | 100%      | equals   | All nps_survey artifacts     |
| Scale range              | 0-10      | equals   | All score fields             |

## HARD Gates
| ID  | Check                                              | Fail Condition                              |
|-----|----------------------------------------------------|---------------------------------------------|
| H01 | YAML frontmatter valid                             | Invalid YAML or missing required fields     |
| H02 | ID matches `^p11_nps_[a-z][a-z0-9_]+\.yaml$`      | Pattern mismatch                            |
| H03 | kind = `nps_survey`                               | Wrong or missing kind                       |
| H04 | scale.min=0 AND scale.max=10                       | Non-Bain scale                              |
| H05 | survey_type is `transactional` or `relational`     | Missing or invalid type                     |
| H06 | Routing rules cover promoter, passive, detractor   | Any score band unrouted                     |
| H07 | follow_up_question present and open-ended          | Missing or scored follow-up                 |

## SOFT Scoring
| Dim | Dimension                                        | Weight | Scoring Guide                                              |
|-----|--------------------------------------------------|--------|------------------------------------------------------------|
| D01 | NPS question phrasing (Bain standard)            | 0.30   | Exact likelihood-to-recommend phrasing = 1.0, paraphrase = 0.5, missing = 0 |
| D02 | Segmentation specificity                         | 0.20   | Measurable filters (tier, tenure, ARR) = 1.0, generic = 0.5, absent = 0 |
| D03 | Cadence completeness (frequency + cooldown)      | 0.20   | Both present = 1.0, frequency only = 0.5, neither = 0     |
| D04 | Routing destination specificity                  | 0.20   | Named system per band = 1.0, generic = 0.5, missing = 0   |
| D05 | Follow-up question quality                       | 0.10   | Band-specific + open-ended = 1.0, generic = 0.5, absent = 0|

## Actions
| Score   | Threshold | Action                              |
|---------|-----------|-------------------------------------|
| GOLDEN  | >=9.5     | Auto-publish, no review             |
| PUBLISH | >=8.0     | Auto-publish after validation       |
| REVIEW  | >=7.0     | Require manual review               |
| REJECT  | <7.0      | Reject and flag for rework          |

## Bypass
| Condition                  | Approver     | Audit Trail         |
|----------------------------|--------------|---------------------|
| Emergency churn spike      | CS Director  | Escalation log      |

## Examples

## Golden Example -- Transactional NPS (Post-Support)
```yaml
---
id: p11_nps_post_support_close.yaml
kind: nps_survey
pillar: P11
survey_type: transactional
cadence: post_support_close
quality: null
---
question: "On a scale of 0 to 10, how likely are you to recommend Acme to a colleague?"
scale:
  min: 0
  max: 10
follow_up:
  promoter: "What made this support experience great?"
  passive: "What one thing would have made this better?"
  detractor: "What went wrong and how can we fix it?"
filters:
  - field: ticket_resolved
    operator: "="
    value: true
  - field: tenure_days
    operator: ">="
    value: 30
exclusion_rules:
  - surveyed_within_days: 90
routing:
  promoter: success_team_referral_queue
  passive: nurture_30d_sequence
  detractor: support_escalation_p1
```

## Anti-Example 1: Non-Bain Scale
```yaml
question: "Rate your experience from 1 to 5"
scale:
  min: 1
  max: 5
```
Why it fails: Uses 1-5 scale instead of Bain standard 0-10. Score calculation
(% promoters - % detractors) is meaningless without the 0-10 range. H04 HARD gate rejects.

## Anti-Example 2: Missing Routing for Passive Band
```yaml
routing:
  promoter: referral_queue
  detractor: escalation_queue
  # passive band absent
```
Why it fails: Passive respondents (7-8) have no destination. They represent 40-60% of
typical responses. H06 HARD gate rejects -- all three bands must be explicitly routed.

## Anti-Example 3: Cohort Analysis Confusion
```yaml
kind: nps_survey
body: |
  "Analyse 90-day NPS trend by customer cohort.
   Compute churn correlation. Generate retention forecast."
```
Why it fails: This is cohort_analysis, not nps_survey. The nps_survey kind configures
survey mechanics only. Analysis belongs in a separate cohort_analysis artifact (P07).

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
