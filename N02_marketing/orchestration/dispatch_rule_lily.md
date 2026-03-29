---
id: p12_dr_lily_marketing
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-11
updated: 2023-10-11
author: dispatch-rule-builder
domain: lily_marketing
quality: null
tags: [marketing, copywriting, lily]
tldr: Routes marketing and e-commerce copy tasks to the Lily Marketing nucleus.
scope: lily_marketing
keywords: [marketing, publicidade, advertising, campanha, campaign, copy, conversao, SEO]
satellite: lily
model: sonnet
priority: 8
confidence_threshold: 0.70
fallback: gateway
conditions: null
load_balance: false
routing_strategy: hybrid

---
## Lily Marketing Dispatch Rule

### Purpose
Routes marketing and e-commerce copywriting tasks, including SEO and advertising campaign creation, to the Lily Marketing satellite. This satellite is optimized for high-conversion marketing initiatives.

### Keyword Rationale
The keywords were selected to trigger on tasks related to marketing, advertising, copywriting, and conversion efforts. Both English and Portuguese terms ensure bilingual coverage for operators and task descriptions.

### Fallback Logic
Fallback to the gateway satellite when Lily Marketing is unavailable, ensuring all tasks have a route for processing or deferral.