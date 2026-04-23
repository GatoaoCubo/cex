---
kind: collaboration
id: bld_collaboration_path_config
pillar: P09
llm_function: COLLABORATE
purpose: How path-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_env_config
  - bld_collaboration_permission
  - path-config-builder
  - bld_collaboration_retriever_config
  - bld_collaboration_trace_config
  - bld_collaboration_boot_config
  - bld_collaboration_builder
  - bld_collaboration_secret_config
  - bld_memory_path_config
  - p03_ins_path_config
---

# Collaboration: path-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what filesystem paths does this scope need, on which platforms, with what defaults?"
I define directories, file locations, path resolution rules, and platform-specific separators. I do NOT handle generic environment variables (env-config-builder), access control (permission-builder), or on/off toggles (feature-flag-builder).
## Crew Compositions
### Crew: "System Configuration Bootstrap"
```
  1. path-config-builder  -> "defines all filesystem paths the system needs"
  2. env-config-builder   -> "defines environment variables that reference those paths"
  3. permission-builder   -> "defines who can read/write each path"
```
### Crew: "Plugin Deployment Setup"
```
  1. plugin-builder       -> "defines the plugin and its required directories"
  2. path-config-builder  -> "specifies install path, config path, log path per platform"
  3. boot-config-builder  -> "wires path config into system startup sequence"
```
### Crew: "Data Pipeline Setup"
```
  1. path-config-builder  -> "input/output/staging/cache directory structure"
  2. env-config-builder   -> "env vars for pipeline configuration"
  3. runtime-rule-builder -> "timeout and retry rules for pipeline steps"
```
## Handoff Protocol
### I Receive
- seeds: scope name, target platforms (Windows/Linux/Mac), directory types needed (workspace/logs/config/cache)
- optional: existing directory structure to document, relative vs absolute preference
### I Produce
- path_config artifact (Markdown, max 4KB)
- committed to: `cex/P09/examples/p09_path_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- plugin-builder: declares what directories a plugin requires before I specify them
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| env-config-builder | references my paths as values for environment variables |
| permission-builder | applies access rules to paths I defined |
| boot-config-builder | uses my paths during system startup sequence |
| daemon-builder | needs log_dir, pid file, and working directory paths |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_env_config]] | sibling | 0.48 |
| [[bld_collaboration_permission]] | sibling | 0.45 |
| [[path-config-builder]] | related | 0.40 |
| [[bld_collaboration_retriever_config]] | sibling | 0.39 |
| [[bld_collaboration_trace_config]] | sibling | 0.38 |
| [[bld_collaboration_boot_config]] | sibling | 0.37 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_collaboration_secret_config]] | sibling | 0.35 |
| [[bld_memory_path_config]] | downstream | 0.35 |
| [[p03_ins_path_config]] | upstream | 0.34 |
