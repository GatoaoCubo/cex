---
id: p10_lr_effort_profile_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
observation: "effort_profile artifacts require explicit model + thinking level pairs with cost/quality rationale. Vague levels like 'smart' cause dispatch failures."
pattern: "Map builder to concrete model (haiku/sonnet/opus) and thinking level (low/medium/high/max). Validate against SCHEMA.md. Keep body under 4096 bytes."
evidence: "Pattern extracted from Anthropic model tiers, Claude thinking budget documentation, and production dispatch configurations across 99 builder types."
confidence: 0.7
outcome: SUCCESS
domain: effort_profile
tags: [effort-profile, P09, type-builder]
tldr: "Concrete model + thinking level with rationale. Validate against schema. Stay under 4096 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_node: edison
keywords: [effort, thinking, model, haiku, sonnet, opus, low, medium, high, max]
---

## Summary
Effort and thinking level configuration for builder execution — maps builder to model and reasoning depth.
The difference between a useful effort_profile and a useless one is concrete model/thinking pairs with rationale versus placeholder text.
## Pattern
**Concrete model + thinking level with rationale.**
Every configuration must have: target builder, model, thinking level, and why that combination was chosen.
Required body sections: Overview, Configuration, Levels, Integration.
Body budget: 4096 bytes max.
## Anti-Pattern
- Over-provisioning: Using opus/max for simple formatting tasks wastes tokens and money
- Under-provisioning: Using haiku/low for complex reasoning tasks produces garbage output
- Missing escalation: No fallback when primary model fails or is unavailable
- Ignoring cost: No cost awareness leads to budget blowout on batch runs
## Context
The 4096-byte body limit keeps effort_profile artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
