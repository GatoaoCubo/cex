---
kind: knowledge_card
id: bld_knowledge_card_feature_flag
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for feature_flag production — feature toggle specification
sources: Fowler 2017 "Feature Toggles", LaunchDarkly, Unleash, Split.io
quality: 9.1
title: "Knowledge Card Feature Flag"
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
  - bld_collaboration_feature_flag
  - p10_lr_feature_flag_builder
  - bld_instruction_feature_flag
  - p01_kc_feature_flag
  - bld_examples_feature_flag
  - bld_schema_feature_flag
  - bld_output_template_feature_flag
  - bld_config_feature_flag
---

# Domain Knowledge: feature_flag
## Executive Summary
Feature flags are on/off toggles that control feature availability at runtime without code deploys. They support four categories: release (ship incomplete code safely), experiment (A/B tests), ops (kill switches), and permission (premium features). Feature flags differ from env configs (generic variables), permissions (access control), and runtime rules (behavior parameters).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| llm_function | GOVERN |
| Frontmatter fields | 15+ |
| Quality gates | 8 HARD + 10 SOFT |
| Categories | release, experiment, ops, permission |
| Default state | OFF for new features, ON for kill switches |
| Rollout pattern | 0% → 5% → 25% → 50% → 100% |
## Patterns
- **Four toggle categories** (Fowler 2017):
| Category | Lifecycle | Default | Example |
|----------|-----------|---------|---------|
| Release | Short (remove after launch) | OFF | enable_new_checkout |
| Experiment | Medium (remove after A/B) | OFF | test_search_algorithm_v2 |
| Ops | Long (keep for emergencies) | ON | enable_cache_layer |
| Permission | Permanent | OFF | premium_export_feature |
- **Gradual rollout**: increase percentage in stages (0→5→25→50→100), monitoring metrics at each step
- **Kill switch pattern**: ops flags start ON, turn OFF to disable in emergency — instant recovery without deploy
- **Cohort targeting**: by user ID, region, or plan tier — more controlled than random percentage
- **Stale flag cleanup**: remove flags after full rollout — every active flag is tech debt
- **Flag naming**: descriptive with domain prefix (enable_dark_mode, use_new_search_v2)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Never removing flags after launch | Accumulates tech debt; code becomes unreadable |
| Kill switch defaults to OFF | Emergency recovery requires deployment — defeats purpose |
| 100% rollout on day one | No gradual confidence building; hard to rollback |
| Flag controls multiple features | Coupling; cannot toggle independently |
| No monitoring at rollout stages | Cannot detect regressions caused by new feature |
| Vague flag name ("flag_1") | Nobody knows what it controls; becomes permanent tech debt |
## Application
1. Define flag: name (descriptive), category (release/experiment/ops/permission)
2. Set default state: OFF for new features, ON for kill switches
3. Design rollout: percentage stages with monitoring criteria at each step
4. Define targeting: random percentage, cohort (user ID/region), or all
5. Plan lifecycle: when to remove flag (release/experiment) or keep (ops/permission)
6. Validate: name is descriptive, category matches lifecycle, default is correct
## References
- Fowler 2017: Feature Toggles (martinfowler.com/articles/feature-toggles.html)
- LaunchDarkly: feature flag lifecycle and best forctices
- Unleash: gradual rollout strategies and user targeting
- Hodgson 2017: Feature Toggles patterns and forctices

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[feature-flag-builder]] | downstream | 0.62 |
| [[p03_sp_feature_flag_builder]] | downstream | 0.58 |
| [[bld_collaboration_feature_flag]] | downstream | 0.56 |
| [[p10_lr_feature_flag_builder]] | downstream | 0.52 |
| [[bld_instruction_feature_flag]] | downstream | 0.46 |
| [[p01_kc_feature_flag]] | sibling | 0.45 |
| [[bld_examples_feature_flag]] | downstream | 0.37 |
| [[bld_schema_feature_flag]] | downstream | 0.35 |
| [[bld_output_template_feature_flag]] | downstream | 0.34 |
| [[bld_config_feature_flag]] | downstream | 0.34 |
