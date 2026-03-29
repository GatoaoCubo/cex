---

```yaml
id: p07_sr_marketing_nucleus
kind: scoring_rubric
pillar: P07
title: "Rubric: Marketing Nucleus"
version: "1.0.0"
created: "2023-10-20"
updated: "2023-10-20"
author: "scoring-rubric-builder"
framework: "Marketing Campaign Evaluation"
target_kinds: [marketing_campaign]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "Marketing"
quality: null
tags: [scoring-rubric, marketing, evaluation]
tldr: "5-dimension rubric for marketing: engagement 30%, conversion 25%, visibility 20%, ROI 15%, brand perception 10%"
density_score: 0.85
calibration_set: [p07_gt_mkt_campaign_successful, p07_gt_mkt_campaign_unsuccessful]
inter_rater_agreement: 0.82
appeals_process: "Submit appeal to marketing evaluation board with rationale."
linked_artifacts:
  primary: "marketing-strategy-builder"
  related: [p11_qg_mkt_publish, p07_gt_mkt_campaign_successful]
---

## Purpose
This rubric evaluates marketing campaigns to ensure they meet quality standards across key dimensions such as audience engagement, conversion rates, brand visibility, return on investment (ROI), and brand perception. It serves to provide a consistent and objective framework for assessing campaign effectiveness.

## Dimensions

| Dimension          | Weight | Scale | Criteria                                                                                 | Example (10)                                          | Example (5)                                          |
|--------------------|--------|-------|------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| Engagement         | 30%    | 0-10  | Measured by audience interactions, comments, shares, and likes relative to the benchmark | Highly interactive, exceeds industry engagement norms | Moderate engagement with limited audience activity  |
| Conversion         | 25%    | 0-10  | Conversion rate from leads to sales or desired action                                    | Exceptionally high conversion rate, minimal leakage   | Conversion rate below campaign goals                |
| Visibility         | 20%    | 0-10  | Reach and impressions across all channels                                                | Extensive reach across multiple platforms             | Limited to few channels with minimal visibility     |
| ROI                | 15%    | 0-10  | Return on investment from marketing spend                                                 | Exceeds ROI expectations with significant profit      | Break-even ROI, not achieving profitability         |
| Brand Perception   | 10%    | 0-10  | Public and audience perception analysis                                                   | Strong positive sentiment, enhances brand valuation   | Neutral perception with no significant brand impact |

## Tier Thresholds

| Tier    | Score | Action                            |
|---------|-------|-----------------------------------|
| GOLDEN  | >= 9.5 | Adopt as best practice example; highlight in reports |
| PUBLISH | >= 8.0 | Approve for publication and broader distribution |
| REVIEW  | >= 7.0 | Requires revisions; provide feedback on weak dimensions |
| REJECT  | < 7.0 | Do not proceed; rework and resubmit with new strategy |

## Calibration

- **GOLDEN**: Exemplary marketing campaigns with top performance in all dimensions.
- **PUBLISH**: Solid campaigns with effective strategies achieving a majority of objectives.
- **REVIEW**: Average campaigns missing key performance goals but showing potential for improvement.
- **REJECT**: Campaigns failing to reach baseline metrics, necessitating complete overhaul.

## Automation

| Dimension          | Status          | Tool               |
|--------------------|-----------------|--------------------|
| Engagement         | semi-automated  | engagement_metric_tool.py |
| Conversion         | automated       | conversion_analysis_tool.py |
| Visibility         | automated       | visibility_tracking_tool.py |
| ROI                | automated       | roi_calculator_tool.py |
| Brand Perception   | manual          | sentiment_analysis_tool.py |

## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- MarketingNucleusTools v3.0
- SampleCampaignDataSet2023