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

