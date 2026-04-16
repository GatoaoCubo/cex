---
id: kc_cohort_analysis
kind: knowledge_card
title: Cohort Analysis for Retention and LTV Modeling
version: 1.0.0
quality: 8.5
pillar: P01
density_score: 1.0
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
