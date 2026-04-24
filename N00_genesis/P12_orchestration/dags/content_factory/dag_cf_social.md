---
id: p12_dag_cf_social
kind: dag
8f: F8_collaborate
pillar: P12
lp: P12
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
pipeline: "content_factory_social"
nodes:
  - id: "receive_longform"
    label: "Receive master longform draft and brand context from dag_cf_master"
    agent_group: "n07_orchestrator"
  - id: "extract_hooks"
    label: "Extract 10-15 hook-worthy snippets, quotes, stats from longform"
    agent_group: "n01_research"
  - id: "define_campaign"
    label: "Map hooks to platforms (X, LinkedIn, Instagram, TikTok) with posting cadence"
    agent_group: "n02_marketing"
  - id: "generate_posts"
    label: "Write platform-native copy per hook (char limits, hashtags, CTAs)"
    agent_group: "n02_marketing"
  - id: "create_carousels"
    label: "Design carousel/infographic assets for Instagram and LinkedIn"
    agent_group: "n03_builder"
  - id: "create_short_clips"
    label: "Generate 15-60s video clips for Reels/TikTok/Shorts from key hooks"
    agent_group: "n03_builder"
  - id: "apply_branding"
    label: "Apply brand palette, logo, fonts, and templates to all visual assets"
    agent_group: "n06_brand"
  - id: "assemble_schedule"
    label: "Build publishing calendar with optimal posting times per platform"
    agent_group: "n02_marketing"
  - id: "quality_check"
    label: "Validate all posts against platform constraints and brand guidelines"
    agent_group: "n04_knowledge"
  - id: "publish"
    label: "Push scheduled posts to social platforms via API or Buffer/Hootsuite"
    agent_group: "n05_operations"
edges:
  - from: "receive_longform"
    to: "extract_hooks"
  - from: "extract_hooks"
    to: "define_campaign"
  - from: "define_campaign"
    to: "generate_posts"
  - from: "define_campaign"
    to: "create_carousels"
  - from: "define_campaign"
    to: "create_short_clips"
  - from: "generate_posts"
    to: "apply_branding"
  - from: "create_carousels"
    to: "apply_branding"
  - from: "create_short_clips"
    to: "apply_branding"
  - from: "apply_branding"
    to: "assemble_schedule"
  - from: "assemble_schedule"
    to: "quality_check"
  - from: "quality_check"
    to: "publish"
domain: "orchestration"
quality: 9.0
tags: [dag, content-factory, social-campaign, multi-platform, scheduling]
tldr: "10-node social DAG: longform→hooks→campaign→parallel(posts+carousels+clips)→brand→schedule→QA→publish"
execution_order:
  - ["receive_longform"]
  - ["extract_hooks"]
  - ["define_campaign"]
  - ["generate_posts", "create_carousels", "create_short_clips"]
  - ["apply_branding"]
  - ["assemble_schedule"]
  - ["quality_check"]
  - ["publish"]
parallel_groups:
  - ["generate_posts", "create_carousels", "create_short_clips"]
critical_path: ["receive_longform", "extract_hooks", "define_campaign", "create_short_clips", "apply_branding", "assemble_schedule", "quality_check", "publish"]
estimated_duration: "50min"
node_count: 10
edge_count: 11
max_parallelism: 3
keywords: [social, campaign, hooks, scheduling, multi-platform, content-factory]
linked_artifacts:
  primary: "P12_orchestration/dags/content_factory/dag_cf_master.md"
  related:
    - "P03_prompts/constraints/content_factory/p03_constraint_cf_brief.md"
density_score: 1.0
related:
  - p12_dag_cf_video
  - p12_dag_cf_presentation
  - p12_dag_cf_course
  - p12_dag_cf_ebook
  - p12_dag_cf_master
  - wave2_quality_report
  - p12_wf_content_factory_v1
  - n04_output_monetization_curriculum
  - n01_output_cf_dags_and_specs
  - p12_wf_marketing_pipeline
---

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| receive_longform | Receive longform draft + brand context | n07_orchestrator | input |
| extract_hooks | Extract 10-15 hook snippets, quotes, stats | n01_research | compute |
| define_campaign | Map hooks to platforms with posting cadence | n02_marketing | compute |
| generate_posts | Write platform-native copy (char limits, CTAs) | n02_marketing | compute |
| create_carousels | Design carousel/infographic assets | n03_builder | compute |
| create_short_clips | Generate 15-60s video clips from hooks | n03_builder | compute |
| apply_branding | Brand palette, logo, fonts on all assets | n06_brand | transform |
| assemble_schedule | Build publishing calendar with optimal times | n02_marketing | compute |
| quality_check | Validate posts against platform + brand rules | n04_knowledge | gate |
| publish | Push to social platforms via API/Buffer | n05_operations | output |

## Edges

| From | To | Type |
|------|----|------|
| receive_longform | extract_hooks | data |
| extract_hooks | define_campaign | data |
| define_campaign | generate_posts | data |
| define_campaign | create_carousels | data |
| define_campaign | create_short_clips | data |
| generate_posts | apply_branding | data |
| create_carousels | apply_branding | data |
| create_short_clips | apply_branding | data |
| apply_branding | assemble_schedule | data |
| assemble_schedule | quality_check | control |
| quality_check | publish | control |

## Topological Order

receive_longform → extract_hooks → define_campaign → generate_posts → create_carousels → create_short_clips → apply_branding → assemble_schedule → quality_check → publish

## Parallel Groups

- **Wave 1**: receive_longform
- **Wave 2**: extract_hooks
- **Wave 3**: define_campaign
- **Wave 4**: generate_posts, create_carousels, create_short_clips (max parallelism = 3)
- **Wave 5**: apply_branding (join barrier — waits for all 3)
- **Wave 6**: assemble_schedule
- **Wave 7**: quality_check
- **Wave 8**: publish

## Critical Path

receive_longform (1min) → extract_hooks (8min) → define_campaign (5min) → create_short_clips (15min) → apply_branding (5min) → assemble_schedule (5min) → quality_check (3min) → publish (3min) = **45min**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dag_cf_video]] | sibling | 0.57 |
| [[p12_dag_cf_presentation]] | sibling | 0.56 |
| [[p12_dag_cf_course]] | sibling | 0.53 |
| [[p12_dag_cf_ebook]] | sibling | 0.45 |
| [[p12_dag_cf_master]] | sibling | 0.25 |
| [[wave2_quality_report]] | upstream | 0.21 |
| [[p12_wf_content_factory_v1]] | related | 0.20 |
| [[n04_output_monetization_curriculum]] | upstream | 0.19 |
| [[n01_output_cf_dags_and_specs]] | upstream | 0.19 |
| [[p12_wf_marketing_pipeline]] | related | 0.19 |
