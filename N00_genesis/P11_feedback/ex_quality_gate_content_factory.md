---
id: ex_quality_gate_content_factory
kind: quality_gate
pillar: P11
title: "Example Quality Gate: Content Factory"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: 8.9
brand_placeholders:
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_AUDIENCE
tags: [quality_gate, content-factory, review, n02]
tldr: "Pre-publish gate for brand fit, factual safety, format compliance, and CTA quality."
density_score: 0.91
related:
  - p03_pt_marketing_task_execution
  - p07_sr_5d_marketing
  - n02_tool_copy_analyzer
  - p11_qg_artifact
  - p01_kc_refinement
  - p01_kc_brand_voice_consistency_channels
  - p03_sp_marketing_nucleus
  - p01_kc_iterative_refinement_skill
  - p08_ac_n02
  - p03_pt_brand_task_driver
---

# Hard Gates

| gate_id | Check | Pass Condition |
|---------|-------|----------------|
| CF01 | Brand voice | Matches `{{BRAND_VOICE}}` and `{{BRAND_TONE}}` |
| CF02 | Audience relevance | Speaks to `{{BRAND_AUDIENCE}}` |
| CF03 | Factual grounding | No unsupported claims |
| CF04 | CTA clarity | Desired action is explicit |
| CF05 | Channel fit | Copy length and structure fit the destination |
| CF06 | Safety | No medical, legal, or harmful overreach |
| CF07 | Formatting | Frontmatter and output schema parse cleanly |

## Decision Logic

```yaml
publish:
  requires_all_hard_gates: true
revise:
  if_failed_gates: [CF01, CF02, CF04, CF05]
escalate:
  if_failed_gates: [CF03, CF06]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_marketing_task_execution]] | upstream | 0.23 |
| [[p07_sr_5d_marketing]] | upstream | 0.20 |
| [[n02_tool_copy_analyzer]] | upstream | 0.20 |
| [[p11_qg_artifact]] | sibling | 0.19 |
| [[p01_kc_refinement]] | upstream | 0.18 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.18 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.18 |
| [[p01_kc_iterative_refinement_skill]] | upstream | 0.17 |
| [[p08_ac_n02]] | upstream | 0.16 |
| [[p03_pt_brand_task_driver]] | upstream | 0.16 |
