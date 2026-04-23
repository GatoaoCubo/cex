---
kind: knowledge_card
id: bld_knowledge_card_effort_profile
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for effort_profile production
sources: Anthropic model documentation, Claude thinking budget specs, production dispatch configurations, cost/quality tradeoff analysis
quality: 9.0
title: "Knowledge Card Effort Profile"
version: "1.0.0"
author: n03_builder
tags: [effort_profile, builder, examples]
tldr: "Golden and anti-examples for effort profile construction, demonstrating ideal structure and common pitfalls."
domain: "effort profile construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_effort_profile_builder
  - bld_examples_effort_profile
  - effort-profile-builder
  - p01_kc_effort_profile
  - bld_collaboration_effort_profile
  - p03_sp_effort_profile_builder
  - bld_instruction_effort_profile
  - p02_mc_claude_opus_4
  - bld_collaboration_thinking_config
  - thinking-config-builder
---

# Domain Knowledge: effort_profile
## Executive Summary
Effort and thinking level configuration for builder execution — maps builder to model and reasoning depth. Produced as P09 artifacts with concrete model/thinking pairs and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 |
| llm_function | CONSTRAIN |
| Max bytes | 4096 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Minimal effort | haiku + low thinking | Simple formatting, templating, boilerplate tasks |
| Balanced effort | sonnet + medium thinking | Standard builds, moderate complexity, good cost/quality |
| Deep effort | opus + high thinking | Complex reasoning, multi-step planning, architecture |
| Maximum effort | opus + max thinking | Critical artifacts, orchestration, novel problems |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Over-provisioning | Using opus/max for simple tasks wastes tokens and budget |
| Under-provisioning | Using haiku/low for complex reasoning produces garbage output |
| Missing escalation | No fallback model when primary is unavailable or rate-limited |
| Ignoring cost | No cost tier awareness leads to budget blowout on batch runs |
## Application
1. Identify the target builder and its typical task complexity
2. Select apownte model/thinking pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 4096 bytes
6. Verify id matches `^p09_effort_[a-z][a-z0-9_]+$`
## References
- Anthropic model documentation (haiku, sonnet, opus capabilities)
- Claude thinking budget specifications (low, medium, high, max)
- Production dispatch configurations across CEX nucleus architecture
- Cost/quality tradeoff analysis for builder execution patterns

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_effort_profile_builder]] | downstream | 0.62 |
| [[bld_examples_effort_profile]] | downstream | 0.47 |
| [[effort-profile-builder]] | downstream | 0.45 |
| [[p01_kc_effort_profile]] | sibling | 0.43 |
| [[bld_collaboration_effort_profile]] | downstream | 0.39 |
| [[p03_sp_effort_profile_builder]] | downstream | 0.36 |
| [[bld_instruction_effort_profile]] | downstream | 0.35 |
| [[p02_mc_claude_opus_4]] | downstream | 0.34 |
| [[bld_collaboration_thinking_config]] | downstream | 0.33 |
| [[thinking-config-builder]] | downstream | 0.30 |
