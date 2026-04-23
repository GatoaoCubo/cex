---
kind: architecture
id: bld_architecture_feature_flag
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of feature_flag — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Feature Flag"
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
  - p03_sp_feature_flag_builder
  - bld_output_template_feature_flag
  - p01_kc_feature_flag
  - p11_qg_feature_flag
  - bld_examples_feature_flag
  - bld_schema_feature_flag
  - bld_instruction_feature_flag
  - bld_knowledge_card_feature_flag
  - bld_collaboration_feature_flag
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| flag_id | Unique identifier for the flag; used by consumers to query state | feature_flag | required |
| flag_state | Default on/off value when no targeting rule matches | feature_flag | required |
| flag_category | Classification: release, experiment, ops, or permission | feature_flag | required |
| rollout_strategy | How the flag activates: instant, percentage-based, or cohort-based | feature_flag | required |
| rollout_percentage | Fraction of traffic (0–100%) receiving the enabled state | feature_flag | conditional |
| targeting_rules | Conditions (user cohort, environment, region) that override default state | feature_flag | optional |
| kill_switch | Emergency override that forces flag off regardless of rollout state | feature_flag | required |
| fallback_default | Value returned when evaluation fails or flag is undefined | feature_flag | required |
| evaluation_context | Runtime data (user ID, env, request metadata) used by targeting rules | feature_flag | required |
## Dependency Graph
```
feature_flag --depends-->  guardrail (P11)
feature_flag --produces--> agent (P02)
feature_flag --produces--> router (P02)
feature_flag --produces--> skill (P04)
kill_switch   --signals-->  feature_flag
targeting_rules --depends--> evaluation_context
```
| From | To | Type | Data |
|------|----|------|------|
| guardrail (P11) | feature_flag | depends | safety rules constraining flag behavior and kill-switch policy |
| feature_flag | agent (P02) | produces | on/off decision consumed before feature execution |
| feature_flag | router (P02) | produces | A/B routing decision based on flag state |
| feature_flag | skill (P04) | produces | optional phase enablement within skill execution |
| kill_switch | feature_flag | signals | emergency-off override forces disabled state |
| evaluation_context | targeting_rules | data_flow | runtime metadata used to resolve cohort and percentage rules |
## Boundary Table
| feature_flag IS | feature_flag IS NOT |
|-----------------|---------------------|
| A logical on/off toggle for a named feature | A generic configuration variable (that is env_config) |
| Evaluated at runtime per request or per user | A static value read once at startup |
| Owner of rollout strategies (percentage, cohort, instant) | An access-control rule determining who can use a resource |
| Capable of gradual canary rollout (1% → 10% → 100%) | A filesystem path or infrastructure variable |
| Equipped with a kill switch for emergency disable | A timeout or retry rule governing technical behavior |
| Classified by category: release, experiment, ops, permission | A permission artifact controlling read/write access |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Identity | flag_id, flag_category | Name and classify the flag for discovery and routing |
| State | flag_state, fallback_default | Define default behavior when no targeting rule applies |
| Rollout | rollout_strategy, rollout_percentage, targeting_rules | Control progressive activation across traffic segments |
| Context | evaluation_context | Supply runtime data for targeting rule evaluation |
| Safety | kill_switch, guardrail (P11) | Enable emergency override and constrain flag behavior |
| Consumers | agent (P02), router (P02), skill (P04) | Receive and act on the evaluated flag decision |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[feature-flag-builder]] | downstream | 0.48 |
| [[p03_sp_feature_flag_builder]] | upstream | 0.46 |
| [[bld_output_template_feature_flag]] | upstream | 0.40 |
| [[p01_kc_feature_flag]] | downstream | 0.40 |
| [[p11_qg_feature_flag]] | downstream | 0.38 |
| [[bld_examples_feature_flag]] | upstream | 0.36 |
| [[bld_schema_feature_flag]] | upstream | 0.36 |
| [[bld_instruction_feature_flag]] | upstream | 0.35 |
| [[bld_knowledge_card_feature_flag]] | upstream | 0.33 |
| [[bld_collaboration_feature_flag]] | downstream | 0.32 |
