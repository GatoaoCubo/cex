---
id: p01_kc_customer_segment
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Customer Segment: ICP Targeting and Cohort Definition"
version: "2.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: "knowledge-card-builder"
domain: product_marketing
quality: 8.5
tags: [customer-segment, icp, firmographics, psychographics, cohort, segmentation, knowledge]
tldr: "Customer segments group buyers by shared firmographic + psychographic traits, powering ICP targeting, pricing tiers, and churn prevention — min 3 criteria per segment."
when_to_use: "When building ICP definitions, pricing pages, onboarding flows, NPS surveys, or churn models that require distinct audience targeting."
keywords: [customer-segment, icp-definition, cohort-analysis, buyer-persona]
long_tails:
  - How to define a customer segment for a B2B SaaS product
  - Difference between customer segment and buyer persona in product marketing
axioms:
  - ALWAYS define a segment with at least 3 criteria (demographic + behavioral + need-based)
  - NEVER collapse segments with different willingness-to-pay into one tier
  - IF a segment has no measurable outcome metric, THEN it is a persona, not a segment
linked_artifacts:
  primary: null
  related: [p01_kc_user_journey, p01_kc_user_model, p01_kc_cohort_analysis]
density_score: 0.88
data_source: "https://www.sequoiacap.com/article/icp-customer-development/"
---

# Customer Segment: ICP Targeting and Cohort Definition

## Quick Reference
```yaml
topic: customer_segment
scope: B2B and B2C product targeting, pricing design, churn prevention
owner: product_marketing
criticality: high
```

## Key Concepts
- **Firmographics**: measurable org attributes — industry (SaaS/Fintech/Healthcare), headcount (<50 / 50-500 / 500+), ARR ($0-1M / $1-10M / $10M+), geography (NA / EU / APAC)
- **Psychographics**: behavioral attributes — pain intensity (critical / moderate / low), buying process (champion-driven / committee / self-serve), tech posture (early adopter / pragmatist / conservative)
- **Segment Size**: total addressable accounts within criteria; min viable = 100 accounts for meaningful signal
- **Willingness-to-Pay (WTP)**: the monetary ceiling per segment; drives tier design; enterprise WTP 5-20x SMB
- **Segment Stability**: segment is valid only if members stay in it for >= 12 months without reclassification

## Strategy Phases
1. **Discover**: run 15-20 win/loss interviews; tag each deal with firmographic + psychographic traits
2. **Cluster**: group deals by shared trait combinations; target >= 20% of total deals per cluster to qualify
3. **Validate**: confirm cluster with outcome metrics (ACV, churn rate, time-to-value); discard clusters with no differentiated outcome
4. **Name and Define**: assign 3-criteria minimum definition; document in a segment spec artifact
5. **Activate**: load segment definitions into ICP scoring, pricing page copy, onboarding flows, and NPS survey cohorts

## Golden Rules
- SEGMENT by WTP first — one pricing tier per WTP band, never mix
- MEASURE with ACV + NRR per segment quarterly; kill segments with NRR < 90%
- LINK every segment to a user_journey artifact for end-to-end traceability
- AVOID "Enterprise" as the only differentiator — add industry or use-case vertical

## Flow
```text
[Raw Deal Data] -> [Firmographic Tag] -> [Psychographic Tag]
                                              |
                                   [Cluster by Shared Traits]
                                              |
                              [Validate with ACV + Churn Signal]
                                              |
                       VALID: [Define Spec + Activate in ICP]
                       INVALID: [Merge into adjacent segment]
```

## Comparativo

| Dimension | SMB Segment | Mid-Market | Enterprise |
|-----------|-------------|------------|------------|
| Headcount | 1-50 | 51-500 | 500+ |
| ACV range | $1K-$10K | $10K-$80K | $80K+ |
| Sales motion | Self-serve / PLG | Inside sales | Field + legal |
| Churn risk | High (30-50% annual) | Medium (10-20%) | Low (5-10%) |
| Decision speed | Days | Weeks (1-3) | Months (3-9) |
| Buying trigger | Pain (individual) | Pain (team) | Strategic initiative |

## References
- Related: [[kc_user_journey]] (segment-to-journey mapping)
- Related: [[p01_kc_user_model]] (per-segment behavioral model)
- Source: https://www.sequoiacap.com/article/icp-customer-development/
- Source: https://www.heavybit.com/library/article/ideal-customer-profile

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_user_journey]] | sibling | 0.72 |
| [[p01_kc_user_model]] | sibling | 0.68 |
| [[p01_kc_cohort_analysis]] | sibling | 0.61 |
| [[bld_collaboration_customer_segment]] | downstream | 0.40 |
| [[p02_qg_customer_segment]] | downstream | 0.37 |
| [[customer-segment-builder]] | downstream | 0.35 |
| [[p10_lr_churn_prevention_playbook_builder]] | downstream | 0.33 |
| [[bld_schema_customer_segment]] | downstream | 0.30 |
| [[bld_instruction_customer_segment]] | downstream | 0.27 |
| [[p03_sp_customer_segment_builder]] | downstream | 0.22 |
