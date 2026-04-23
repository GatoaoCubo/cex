---
kind: output_template
id: bld_output_template_nps_survey
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for nps_survey production
quality: 8.9
title: "Output Template Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, output_template]
tldr: "Template with vars for nps_survey production"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_nps_survey
  - bld_instruction_nps_survey
  - kc_nps_survey
  - p11_qg_nps_survey
  - p03_sp_nps_survey_builder
  - nps-survey-builder
  - bld_collaboration_nps_survey
  - bld_knowledge_card_nps_survey
  - p10_lr_nps_survey_builder
  - bld_tools_nps_survey
---

```yaml
---
id: p11_nps_{{name}}.yaml
kind: nps_survey
pillar: P11
title: "NPS Survey: {{title}}"
version: "1.0.0"
survey_type: {{survey_type}}   # transactional | relational
cadence: {{cadence}}           # post_interaction | quarterly | annual
created: "{{date}}"
updated: "{{date}}"
quality: null
tags: [nps_survey, {{segment_tag}}]
---

## Survey Configuration
question: "On a scale of 0 to 10, how likely are you to recommend {{product_name}} to a colleague?"
scale:
  min: 0
  max: 10
  labels:
    0: "Not at all likely"
    10: "Extremely likely"
follow_up:
  promoter: "What do you love most about {{product_name}}?"
  passive: "What one thing would make {{product_name}} better for you?"
  detractor: "What is the most important improvement we could make?"

## Segmentation
filters:
  - field: customer_tier
    values: [{{tier_values}}]    # e.g., enterprise, mid-market
  - field: tenure_days
    operator: ">="
    value: {{min_tenure}}        # e.g., 30
  - field: region
    values: [{{regions}}]

exclusion_rules:
  - surveyed_within_days: 90
  - status: churned

## Cadence Rules
trigger: {{trigger}}             # e.g., post_onboarding, post_support_close, quarterly_cron
cooldown_days: {{cooldown}}      # e.g., 90
max_per_year: {{max_per_year}}   # e.g., 4

## Score Routing
promoter:   # 9-10
  destination: {{promoter_destination}}   # e.g., success_team_expansion_queue
  action: flag_for_referral

passive:    # 7-8
  destination: {{passive_destination}}    # e.g., nurture_sequence
  action: schedule_qbr

detractor:  # 0-6
  destination: {{detractor_destination}}  # e.g., support_escalation_queue
  action: create_ticket_priority_high
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_nps_survey]] | downstream | 0.45 |
| [[bld_instruction_nps_survey]] | upstream | 0.31 |
| [[kc_nps_survey]] | upstream | 0.29 |
| [[p11_qg_nps_survey]] | downstream | 0.29 |
| [[p03_sp_nps_survey_builder]] | upstream | 0.28 |
| [[nps-survey-builder]] | downstream | 0.27 |
| [[bld_collaboration_nps_survey]] | downstream | 0.22 |
| [[bld_knowledge_card_nps_survey]] | upstream | 0.22 |
| [[p10_lr_nps_survey_builder]] | downstream | 0.21 |
| [[bld_tools_nps_survey]] | upstream | 0.18 |
