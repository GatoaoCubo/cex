---
id: ex_workflow_content_factory
kind: workflow
pillar: P12
title: "Example Workflow: Content Factory"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: 8.8
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
  - BRAND_DOMAIN
tags: [workflow, content-factory, editorial, n02]
tldr: "Multi-stage workflow for planning, drafting, reviewing, publishing, and repurposing branded content."
density_score: 0.93
related:
  - workflow_campaign_pipeline
  - input_schema_campaign_brief
---

# Stages

1. Intake brief and objective.
2. Match brief to content pillar from `{{BRAND_CONTENT_THEMES}}`.
3. Generate draft in `{{BRAND_VOICE}}`.
4. Validate brand, accuracy, and publishability.
5. Route approved assets to distribution.
6. Capture performance and feedback for the next cycle.

## Inputs

- campaign_goal
- audience_segment
- source_material
- channel
- publish_deadline

## Outputs

- approved_copy
- creative_brief
- publish_payload
- feedback_log

## SLA

- Draft turnaround: same day for short-form, two business days for long-form.
- Revision limit: two rounds before escalation.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow_campaign_pipeline]] | sibling | 0.15 |
| [[input_schema_campaign_brief]] | upstream | 0.15 |
