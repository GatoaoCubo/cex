---
kind: architecture
id: bld_architecture_path_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of path_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - path-config-builder
  - p03_ins_path_config
  - p11_qg_path_config
  - p03_sp_path_config_builder
  - bld_memory_path_config
  - p01_kc_path_config
  - bld_schema_path_config
  - bld_knowledge_card_path_config
  - bld_collaboration_path_config
  - bld_examples_path_config
---

# Architecture: path_config in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, platform, scope, etc.) | path-config-builder | active |
| path_catalog | Master list of all paths with type, default, and description | author | active |
| platform_rules | Platform-specific separator and expansion rules (Windows/Linux/Mac) | author | active |
| resolution_strategy | How relative paths resolve to absolute paths at runtime | author | active |
| directory_hierarchy | Parent-child relationships between directories | author | active |
| validation_rules | Checks for path existence, permissions, and platform compliance | author | active |
## Dependency Graph
```
env_config      --produces-->  path_config  --consumed_by-->  agent
boot_config     --depends-->   path_config  --consumed_by-->  spawn_config
path_config     --signals-->   path_resolution_error
```
| From | To | Type | Data |
|------|----|------|------|
| env_config (P09) | path_config | data_flow | environment variables used in path expansion |
| path_config | agent (P02) | consumes | agent reads paths for file operations |
| path_config | spawn_config (P12) | consumes | spawn scripts use paths for working directories |
| boot_config (P02) | path_config | dependency | boot sequence needs paths for initialization |
| path_config | path_resolution_error (P12) | signals | emitted when a path fails validation |
| permission (P09) | path_config | dependency | access control may restrict certain paths |
## Boundary Table
| path_config IS | path_config IS NOT |
|----------------|-------------------|
| A specification of filesystem paths with platform awareness | A generic environment variable store (env_config P09) |
| Scoped to a domain with directory hierarchy documented | An access control rule for paths (permission P09) |
| Platform-aware with Windows/Linux/Mac resolution rules | A feature toggle (feature_flag P09) |
| Includes validation for existence and permissions | A runtime behavior parameter (runtime_rule P09) |
| Documents parent-child directory relationships | A naming convention for artifacts (naming_rule P05) |
| Resolves relative to absolute using defined strategy | A hardcoded absolute path without expansion |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Environment | env_config, platform_rules | Supply variables and platform constraints |
| Catalog | frontmatter, path_catalog, directory_hierarchy | List all paths with relationships |
| Resolution | resolution_strategy | Define how paths are expanded and resolved |
| Validation | validation_rules | Check paths exist and are accessible |
| Consumers | agent, spawn_config, boot_config | Systems that read and use the configured paths |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[path-config-builder]] | downstream | 0.57 |
| [[p03_ins_path_config]] | upstream | 0.52 |
| [[p11_qg_path_config]] | downstream | 0.50 |
| [[p03_sp_path_config_builder]] | upstream | 0.47 |
| [[bld_memory_path_config]] | downstream | 0.46 |
| [[p01_kc_path_config]] | downstream | 0.43 |
| [[bld_schema_path_config]] | upstream | 0.40 |
| [[bld_knowledge_card_path_config]] | upstream | 0.39 |
| [[bld_collaboration_path_config]] | downstream | 0.38 |
| [[bld_examples_path_config]] | upstream | 0.36 |
