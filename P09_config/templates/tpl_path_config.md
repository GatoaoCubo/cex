---
id: "p09_path_{{SCOPE_SLUG}}"
kind: path_config
pillar: P09
version: 1.0.0
title: Template - Path Config
tags: [template, path, config, directory, filesystem]
tldr: Filesystem paths for CEX instance. Maps logical names to physical paths. Supports env vars.
quality: null
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
- Windows: `\` -> `/` normalization
- Symlinks: Resolve to real path
- Missing dirs: Auto-create with `ensure_dir()`
## Quality Gate
- [ ] Forward slashes only (cross-platform)
- [ ] No hardcoded absolute paths
- [ ] Missing dirs auto-created
- [ ] Env vars documented
