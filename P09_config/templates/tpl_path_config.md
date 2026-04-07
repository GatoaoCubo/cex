---
id: "p09_path_{{SCOPE_SLUG}}"
kind: path_config
pillar: P09
version: 1.0.0
title: Template - Path Config
tags: [template, path, config, directory, filesystem]
tldr: Filesystem paths for CEX instance. Maps logical names to physical paths. Supports env vars.
quality: 9.0
updated: "2026-04-07"
domain: "configuration management"
author: n03_builder
created: "2026-04-07"
density_score: 0.96
---

# Path Config: [NAME]

## Purpose
[WHAT this path_config does]
## Path Registry
```yaml
root: "${CEX_ROOT}"
builders: "${root}/archetypes/builders"
knowledge: "${root}/P01_knowledge"
runtime: "${root}/.cex/runtime"

handoffs: "${root}/.cex/runtime/handoffs"
signals: "${root}/.cex/runtime/signals"
compiled: "${root}/compiled"
learning: "${root}/.cex/learning_records"
```
## Resolution Rules
| Input | Resolution |
|-------|-----------|
| Absolute | Use as-is |
| Relative | Resolve from CEX_ROOT |
| `${VAR}` | Expand env var |
| `~` | Expand home dir |
## Platform
1. Windows: `\` -> `/` normalization
2. Symlinks: Resolve to real path
3. Missing dirs: Auto-create with `ensure_dir()`
## Quality Gate
1. [ ] Forward slashes only (cross-platform)
2. [ ] No hardcoded absolute paths
3. [ ] Missing dirs auto-created
4. [ ] Env vars documented

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `path_config` |
| Pillar | P09 |
| Domain | configuration management |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |
