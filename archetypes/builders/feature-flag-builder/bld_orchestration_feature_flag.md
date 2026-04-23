---
kind: collaboration
id: bld_collaboration_feature_flag
pillar: P12
llm_function: COLLABORATE
purpose: How feature-flag-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - feature-flag-builder
  - bld_collaboration_env_config
  - p03_sp_feature_flag_builder
  - bld_knowledge_card_feature_flag
  - bld_collaboration_path_config
  - bld_collaboration_experiment_config
  - bld_collaboration_builder
  - p10_lr_feature_flag_builder
  - p01_kc_feature_flag
  - bld_collaboration_boot_config
---

# Collaboration: feature-flag-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "should this feature be on or off, for whom, and with what rollout strategy?"
I do not set environment variables. I do not control access permissions.
I specify feature toggles so teams can control rollout, experiments, and kill switches.
## Crew Compositions
### Crew: "Deployment Configuration"
```
  1. boot-config-builder -> "provider startup configuration"
  2. env-config-builder -> "environment variables"
  3. feature-flag-builder -> "feature toggles (on/off, rollout %, cohorts)"
```
### Crew: "Gradual Rollout"
```
  1. feature-flag-builder -> "flag definition with rollout strategy"
  2. benchmark-builder -> "performance impact measurement per cohort"
  3. bugloop-builder -> "auto-rollback if metrics degrade"
```
## Handoff Protocol
### I Receive
- seeds: feature name, flag category (release, experiment, ops, permission)
- optional: rollout percentage, cohort targeting, kill switch config, expiry date
### I Produce
- feature_flag artifact (.md + .yaml frontmatter)
- committed to: `cex/P09/examples/p09_flag_{feature}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Flags are defined from product requirements.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| env-config-builder | May reference flags as environment overrides |
| bugloop-builder | Uses flag state as detection trigger for rollback |
| benchmark-builder | Measures performance per flag cohort |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[feature-flag-builder]] | upstream | 0.54 |
| [[bld_collaboration_env_config]] | sibling | 0.52 |
| [[p03_sp_feature_flag_builder]] | upstream | 0.50 |
| [[bld_knowledge_card_feature_flag]] | upstream | 0.44 |
| [[bld_collaboration_path_config]] | sibling | 0.40 |
| [[bld_collaboration_experiment_config]] | sibling | 0.40 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[p10_lr_feature_flag_builder]] | upstream | 0.36 |
| [[p01_kc_feature_flag]] | upstream | 0.36 |
| [[bld_collaboration_boot_config]] | sibling | 0.35 |
