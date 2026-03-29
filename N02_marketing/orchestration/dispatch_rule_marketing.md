---
id: p12_dr_marketing
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-23
updated: 2023-10-23
author: marketing_specialist
domain: marketing
quality: null
tags: [dispatch, marketing, apollo]
tldr: Route marketing-related tasks to the appropriate satellite for execution
scope: marketing
keywords: [marketing, campanha, campaign, publicidade, advertisement, ads, promo, promoção, lead, contato]
satellite: apollo
model: sonnet
priority: 7
confidence_threshold: 0.70
fallback: edison
# marketing Dispatch Rule
## Purpose
Routes marketing tasks such as creating campaigns, managing advertisements, and generating leads to the designated marketing satellite.
## Keyword Rationale
The selected keywords cover both English and Portuguese terms related to marketing functions, ensuring that tasks are correctly identified and routed.
## Fallback Logic
Fallback fires when the `apollo` satellite is unavailable, routing the task to `edison` to ensure continuity in marketing operations.
---

This dispatch_rule routes marketing tasks to the `apollo` satellite with a bilingual keyword list, ensuring proper identification and execution of relevant tasks. In case of unavailability, the `edison` satellite serves as a fallback. The configuration adheres to all specified requirements and constraints.