---
id: kc_cohort_analysis
kind: knowledge_card
title: Cohort Analysis for Retention and LTV Modeling
version: 1.0.0
quality: 8.5
pillar: P01
density_score: 1.0
related:
  - cohort-analysis-builder
  - bld_instruction_cohort_analysis
  - bld_knowledge_card_cohort_analysis
  - p10_mem_cohort_analysis_builder
  - p03_sp_cohort_analysis_builder
  - leverage_map_v2_n06_verification
  - bld_examples_cohort_analysis
  - bld_collaboration_cohort_analysis
  - p07_qg_cohort_analysis
  - bld_tools_cohort_analysis
---

**Definition**: Cohort analysis is a statistical technique that groups users by shared characteristics (e.g., acquisition date, behavior patterns) to measure retention rates and lifetime value (LTV) over time.

**Purpose**:
- Track user retention across time intervals
- Model lifetime value trajectories
- Identify at-risk cohorts
- Optimize marketing strategies

**Key Metrics**:
- Churn rate (percentage of users lost per period)
- Cohort retention curve (retention rate over time)
- Average LTV per cohort
- Customer lifetime value (CLV) by acquisition channel

**Analysis Types**:
1. Time-based cohorts (e.g., monthly cohorts)
2. Behavior-based cohorts (e.g., first purchase behavior)
3. Demographic cohorts (e.g., age groups)
4. Funnel-stage cohorts (e.g., conversion paths)

**Tools**:
- SQL/Python for cohort segmentation
- Retention tables with time-to-event analysis
- LTV models incorporating cohort-specific decay rates
- Visualization tools for cohort heatmaps

**Example**:
A 30-day cohort might show:
- 65% retention at 30 days
- 40% retention at 90 days
- Average LTV of $120 for this cohort
- 25% higher churn in users who didn't complete onboarding

**Best Practices**:
- Use consistent time intervals for comparison
- Include both absolute numbers and percentages
- Segment by relevant dimensions (e.g., product usage)
- Combine with customer journey mapping

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[cohort-analysis-builder]] | downstream | 0.56 |
| [[bld_instruction_cohort_analysis]] | downstream | 0.52 |
| [[bld_knowledge_card_cohort_analysis]] | sibling | 0.51 |
| [[p10_mem_cohort_analysis_builder]] | downstream | 0.51 |
| [[p03_sp_cohort_analysis_builder]] | downstream | 0.47 |
| [[leverage_map_v2_n06_verification]] | sibling | 0.39 |
| [[bld_examples_cohort_analysis]] | downstream | 0.38 |
| [[bld_collaboration_cohort_analysis]] | downstream | 0.31 |
| [[p07_qg_cohort_analysis]] | downstream | 0.30 |
| [[bld_tools_cohort_analysis]] | downstream | 0.28 |
