---
id: ex_chain_content_factory
kind: chain
pillar: P03
title: "Example Chain: Content Factory"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: null
brand_placeholders:
  - BRAND_VOICE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
tags: [chain, content-factory, prompt, n02]
tldr: "Prompt chain that turns a raw brief into publishable content with review checkpoints."
density_score: 0.9
---

# Chain

```yaml
steps:
  - name: clarify_brief
    prompt_goal: resolve audience, offer, stage, and CTA
  - name: choose_angle
    prompt_goal: select one strong hook from {{BRAND_CONTENT_THEMES}}
  - name: draft
    prompt_goal: write the first version in {{BRAND_VOICE}}
  - name: tighten
    prompt_goal: remove fluff, sharpen proof, improve CTA
  - name: approve
    prompt_goal: verify accuracy, brand fit, and readiness
```

## Pass-Forward Data

- `clarify_brief` outputs a structured brief.
- `choose_angle` outputs hook, tension, and desired action.
- `draft` outputs the main copy.
- `tighten` outputs the candidate final.
- `approve` outputs publish or revise.

