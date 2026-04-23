---
id: tpl_workflow_strategic_outreach
kind: template
pillar: P12
title: "Workflow — Strategic Outreach Campaign"
version: 1.0.0
quality: 9.1
created: 2026-04-07
author: n03_builder
origin: gato-ao-cubo/N02_marketing/p12_wf_gato_strategic_outreach.md
variables: [BRAND_NAME, CHANNELS, OUTREACH_STAGES, SEGMENTS, TARGET_COUNT, REGION]
density_score: 0.95
tags: [template, workflow, outreach, campaign, lead-nurturing, b2b, instance-extraction]
tldr: "Multi-channel outreach campaign workflow — convert CRM prospects into brand partners via segmented communication."
updated: "2026-04-13"
related:
  - p12_wf_builder_8f_pipeline
  - p03_ins_workflow
  - p12_wf_engineering_pipeline
  - p11_qg_workflow
  - p12_wf_content_factory_v1
  - p10_lr_chain_builder
  - p12_wf_marketing_pipeline
  - bld_architecture_chain
  - p12_wf_create_orchestration_agent
  - bld_knowledge_card_workflow
---

# {{BRAND_NAME}} — Strategic Outreach Campaign

## Campaign Objective

Convert **{{TARGET_COUNT}}** {{REGION}} prospects into {{BRAND_NAME}} partners via multi-channel outreach. Segmented by business type, personalized by data signals.

---

## Segment Definitions

{{#SEGMENTS}}
| Segment | Description | Priority | Approach |
|---------|-------------|:--------:|----------|
{{#each}}
| {{name}} | {{description}} | {{priority}} | {{approach}} |
{{/each}}
{{/SEGMENTS}}

---

## Workflow Waves

### Wave 1: Content Preparation (Parallel)

| Step | Agent | Action | Output | Signal |
|:----:|:-----:|--------|--------|--------|
| 1 | N02 | Create segment-specific outreach copy ({{SEGMENTS.count}} segments) | `outreach_copy.md` | `copy_complete` |
| 2 | N02 | Develop relationship tactics for {{CHANNELS}} | `social_strategy.md` | `social_complete` |
| 3 | N02 | Build case studies, ROI calculator, partnership guide | `conversion_assets.md` | `assets_complete` |

### Wave 2: Automation Setup (Sequential)

| Step | Agent | Action | Output | Depends On |
|:----:|:-----:|--------|--------|:----------:|
| 4 | N02 | Design {{OUTREACH_STAGES.touch_count | default: '5'}}-touch nurturing sequence | `nurturing_sequence.md` | Steps 1, 3 |
| 5 | N05 | Set up email/messaging automation | `automation_config.yaml` | Step 4 |

### Wave 3: Execution (Sequential by priority)

| Step | Agent | Action | Output | Depends On |
|:----:|:-----:|--------|--------|:----------:|
| 6 | N01 | Score and prioritize leads (S+/S/A/B/C) | `scored_leads.json` | CRM data |
| 7 | N02 | Execute outreach: S+ tier first → cascade | `outreach_log.json` | Steps 5, 6 |
| 8 | N07 | Monitor responses, adjust strategy | `campaign_report.md` | Step 7 |

---

## Channel Strategy

{{#CHANNELS}}
### {{name}}

| Attribute | Value |
|-----------|-------|
| Platform | {{platform}} |
| Content type | {{content_type}} |
| Frequency | {{frequency}} |
| Personalization | {{personalization_level}} |
| Tracking | {{tracking_method}} |

{{/CHANNELS}}

---

## Nurturing Sequence

| Touch | Timing | Content | Channel | Goal |
|:-----:|--------|---------|---------|------|
{{#OUTREACH_STAGES.touches}}
| {{number}} | {{timing}} | {{content}} | {{channel}} | {{goal}} |
{{/OUTREACH_STAGES.touches}}

---

## Response Classification

| Response | Action | Next Step |
|----------|--------|-----------|
| Interested | Schedule meeting | Move to `negotiating` |
| Maybe later | Add to nurture sequence | Touch +30 days |
| Not interested | Respect + archive | Move to `inactive` |
| No response (3 touches) | Pause outreach | Reactivate in 90 days |

---

## KPIs

| Metric | Target | Formula |
|--------|:------:|---------|
| Open rate | 40%+ | opens / sent |
| Response rate | 15%+ | responses / sent |
| Meeting rate | 5%+ | meetings / sent |
| Conversion rate | 2%+ | partners / sent |
| Cost per lead | < $5 | total_cost / leads_contacted |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_builder_8f_pipeline]] | related | 0.25 |
| [[p03_ins_workflow]] | upstream | 0.24 |
| [[p12_wf_engineering_pipeline]] | related | 0.23 |
| [[p11_qg_workflow]] | related | 0.23 |
| [[p12_wf_content_factory_v1]] | related | 0.23 |
| [[p10_lr_chain_builder]] | upstream | 0.22 |
| [[p12_wf_marketing_pipeline]] | related | 0.22 |
| [[bld_architecture_chain]] | upstream | 0.22 |
| [[p12_wf_create_orchestration_agent]] | related | 0.21 |
| [[bld_knowledge_card_workflow]] | upstream | 0.21 |
