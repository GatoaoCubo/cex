---
kind: collaboration
id: bld_collaboration_env_config
pillar: P12
llm_function: COLLABORATE
purpose: How env-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_boot_config
  - bld_collaboration_path_config
  - bld_collaboration_trace_config
  - bld_collaboration_model_provider
  - bld_collaboration_feature_flag
  - bld_collaboration_agent
  - bld_collaboration_secret_config
  - env-config-builder
  - bld_collaboration_runtime_rule
  - bld_collaboration_cost_budget
---

# Collaboration: env-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what environment variables does this scope need, with what defaults and validation?"
I do not configure provider startup. I do not define feature toggles.
I specify environment variables so deployments have correct configuration and secrets.
## Crew Compositions
### Crew: "Deployment Configuration"
```
  1. boot-config-builder -> "provider startup configuration"
  2. env-config-builder -> "environment variables (secrets, settings, paths)"
  3. feature-flag-builder -> "feature toggles for gradual rollout"
```
### Crew: "Multi-Provider Deployment"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "config per provider"
  3. env-config-builder -> "env vars per deployment target"
  4. fallback-chain-builder -> "degradation per environment"
```
## Handoff Protocol
### I Receive
- seeds: scope (global, service, agent), variable list
- optional: sensitivity flags, validation rules, override precedence, defaults
### I Produce
- env_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P09/examples/p09_env_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- boot-config-builder: reveals which variables each provider needs
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| client-builder | API clients reference env vars for credentials |
| connector-builder | Connectors reference env vars for connection settings |
| daemon-builder | Background processes read env vars at startup |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_boot_config]] | sibling | 0.56 |
| [[bld_collaboration_path_config]] | sibling | 0.52 |
| [[bld_collaboration_trace_config]] | sibling | 0.44 |
| [[bld_collaboration_model_provider]] | sibling | 0.43 |
| [[bld_collaboration_feature_flag]] | sibling | 0.42 |
| [[bld_collaboration_agent]] | sibling | 0.40 |
| [[bld_collaboration_secret_config]] | sibling | 0.40 |
| [[env-config-builder]] | upstream | 0.40 |
| [[bld_collaboration_runtime_rule]] | sibling | 0.39 |
| [[bld_collaboration_cost_budget]] | sibling | 0.39 |
