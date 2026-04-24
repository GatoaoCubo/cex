---
id: ex_workflow_q2_production
kind: workflow
8f: F8_collaborate
pillar: P12
title: "Example Workflow: Q2 Production"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: q2_content_pipeline
quality: 8.7
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
tags: [workflow, editorial, q2, production, n02]
tldr: "Reusable production workflow for running a quarter-scale editorial program without one artifact per asset."
density_score: 0.91
related:
  - p04_rp_weekly_market_intelligence_brief_output_template
  - p12_wf_weekly_fashion_content
---

# Workflow

1. Load quarter goals.
2. Build a weekly topic map from `{{BRAND_CONTENT_THEMES}}`.
3. Generate the weekly blog brief.
4. Derive social variants from the same source angle.
5. Run quality gate and output validation.
6. Schedule publication and archive performance notes.

## Success Metrics

- Weekly throughput achieved
- Balanced theme coverage
- Reuse rate from blog to social
- CTA consistency across formats

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_rp_weekly_market_intelligence_brief_output_template]] | upstream | 0.16 |
| [[p12_wf_weekly_fashion_content]] | sibling | 0.15 |
