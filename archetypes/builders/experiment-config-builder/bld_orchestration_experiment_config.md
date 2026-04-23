---
kind: collaboration
id: bld_collaboration_experiment_config
pillar: P12
llm_function: COLLABORATE
purpose: How experiment-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, collaboration, P12]
tldr: "Crew roles for experiment-config-builder: receives variant seeds, produces complete experiment spec, feeds winning results to feature-flag-builder."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - experiment-config-builder
  - bld_collaboration_builder
  - bld_architecture_experiment_config
  - bld_collaboration_model_card
  - bld_collaboration_feature_flag
  - bld_collaboration_env_config
  - p03_sp_experiment_config_builder
  - bld_architecture_kind
  - bld_collaboration_trace_config
  - bld_collaboration_quality_gate
---

# Collaboration: experiment-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what variants does this experiment compare,
how is traffic allocated, and what metrics determine success?"
I do not define the variant content (prompt templates do that). I do not decide permanence
(feature-flag-builder does that after I conclude). I specify the experiment framework so
controlled trials are statistically valid and operationally safe.

## Crew Compositions
### Crew: "Prompt Optimization"
```
  1. prompt-template-builder -> "create control and treatment prompt variants"
  2. experiment-config-builder -> "define A/B test: traffic split, metrics, statistics"
  3. quality-gate-builder -> "scoring rubric for evaluation"
  4. learning-record-builder -> "capture learnings when experiment concludes"
```

### Crew: "Feature Rollout"
```
  1. experiment-config-builder -> "validate new feature via controlled trial"
  2. feature-flag-builder -> "promote winning variant to permanent rollout"
  3. env-config-builder -> "update environment variables for new configuration"
  4. trace-config-builder -> "tag traces with experiment_id and variant"
```

### Crew: "Model Comparison"
```
  1. agent-builder -> "define agent for each model variant"
  2. experiment-config-builder -> "A/B test model A vs model B traffic allocation"
  3. benchmark-builder -> "define scoring criteria for model quality"
  4. learning-record-builder -> "record model selection decision"
```

## Handoff Protocol
### I Receive
- seeds: experiment name, domain (what is being tested), variant descriptions
- optional: traffic split preferences, metric definitions, segment constraints
- optional: statistical targets (MDE, significance threshold)

### I Produce
- experiment_config artifact (.md + .yaml frontmatter)
- committed to: `P09_config/examples/p09_ec_{name_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
- on conclusion: signal to feature-flag-builder or learning-record-builder

## Builders I Depend On
- prompt-template-builder: provides variant prompt content referenced in variant descriptions
- trace-config-builder: confirms experiment_id tagging is in place before launch

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| feature-flag-builder | Receives winning variant from concluded experiments for permanent promotion |
| learning-record-builder | Receives experiment findings, effect size, and decision rationale |
| env-config-builder | Receives any environment variable changes required by winning variant |
| agent-builder | Reads active experiment config to select variant parameters per request |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[experiment-config-builder]] | upstream | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_architecture_experiment_config]] | upstream | 0.38 |
| [[bld_collaboration_model_card]] | sibling | 0.37 |
| [[bld_collaboration_feature_flag]] | sibling | 0.37 |
| [[bld_collaboration_env_config]] | sibling | 0.35 |
| [[p03_sp_experiment_config_builder]] | upstream | 0.35 |
| [[bld_architecture_kind]] | upstream | 0.35 |
| [[bld_collaboration_trace_config]] | sibling | 0.34 |
| [[bld_collaboration_quality_gate]] | sibling | 0.34 |
