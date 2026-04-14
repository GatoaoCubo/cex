---
id: p10_lr_feature_flag_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Feature flags without expiration dates accumulate as permanent tech debt — stale flags found after 18+ months. rollout_percentage as string '50%' fails schema; must be integer 0-100. category confused with 'feature' or 'toggle' (invalid) instead of valid values: release, experiment, ops, permission. Kill switch absent from ops flags causes outage risk — no one knows how to disable a live feature under incident. Lifecycle omitted means no retirement plan, flags never get removed."
pattern: "Every feature flag requires: default_state (on/off only), rollout_percentage (integer 0-100), category (release/experiment/ops/permission), expires date, kill_switch procedure, and a ## Lifecycle section. Ops flags default to on and need emergency disable documented. Release and experiment flags default to off and expire in 2-6 weeks. Permission flags are permanent but need documented revocation path. Never use flag to represent WHO has access — that is a permission artifact."
evidence: "9 feature flag artifacts validated. 100% of flags missing expires field had no documented retirement..."
confidence: 0.75
outcome: SUCCESS
domain: feature_flag
tags: [feature_flag, rollout, kill_switch, gradual_rollout, lifecycle, ops_safety]
tldr: "Set expires on every flag; document kill_switch for ops flags; rollout_percentage is integer not string."
impact_score: 7.5
decay_rate: 0.04
agent_group: edison
keywords: [feature_flag, rollout_percentage, kill_switch, default_state, category, expires, lifecycle, gradual_rollout]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Feature Flag"
density_score: 0.90
llm_function: INJECT
---
## Summary
Feature flags enable gradual rollout and emergency disable without code deployment. The builder must enforce four category types, integer rollout percentages, expiration dates, and kill switch documentation or flags become permanent liabilities that no one knows how to safely disable.
## Pattern
1. `default_state` accepts only `"on"` or `"off"` — no intermediate values.
2. `rollout_percentage` is an integer 0-100 with no percent symbol.
3. `category` is one of four values: `release` (new feature), `experiment` (A/B test), `ops` (operational toggle), `permission` (access control).
4. Every flag has an `expires` date. Release and experiment flags expire in 2-6 weeks. Ops and permission flags set expires to a review date, not infinity.
5. Ops flags default to `on` and must document a kill switch procedure — the exact steps to disable under incident conditions.
6. Every artifact includes a `## Lifecycle` section: how the flag is created, monitored, and retired.
7. Targeting rules (user segment, region, percentage) live in the targeting block, not in the flag description.
## Anti-Pattern
1. `default_state: "maybe"` or `"partial"` — only `"on"` or `"off"` are valid.
2. `rollout_percentage: "50%"` — string with percent symbol fails schema.
3. `category: "feature"` or `"toggle"` — these are not valid category values.
4. Omitting `expires` creates permanent flags with no retirement plan.
5. Omitting kill switch for ops flags means no runbook during incidents.
6. Using a feature flag to represent WHO has access — that is a permission artifact, not a flag.
7. Body exceeding 1536 bytes — P09 has the tightest size limit; every word must earn its place.
## Context
Applies when: shipping a new feature behind a gate, running an A/B experiment, adding an emergency ops toggle, or restricting access to a capability.
Does not apply when: the decision is permanent and binary with no rollout phase needed.
Boundary: feature_flag controls whether a feature exists; permission controls who can use it. Do not conflate.
Category decision: if the flag will exist beyond 6 weeks permanently, evaluate whether it should be a permission instead.

## Builder Context

This ISO operates within the `feature-flag-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_feature_flag_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_feature_flag_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | feature_flag |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
